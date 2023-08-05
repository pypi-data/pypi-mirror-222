# [2022-10-23] Downloaded from https://github.com/openai/triton/blob/master/python/tutorials/06-fused-attention.py

"""
Fused Attention
===============
This is a Triton implementation of the Flash Attention algorithm
(see: Dao et al., https://arxiv.org/pdf/2205.14135v2.pdf; Rabe and Staats https://arxiv.org/pdf/2112.05682v2.pdf)
"""
import math

import torch

from einops import rearrange

import triton
import triton.language as tl


@triton.autotune(
    configs=[
        triton.Config({"BLOCK_M": 128, "BLOCK_N": 128}, num_warps=8, num_stages=1),
        triton.Config({"BLOCK_M": 64, "BLOCK_N": 64}, num_warps=4, num_stages=1),
    ],
    key=['CACHE_KEY_SEQLEN_Q', 'CACHE_KEY_SEQLEN_K', 'IS_CAUSAL', 'BLOCK_HEADDIM']
)
@triton.heuristics(
    {
        "EVEN_M": lambda args: args["seqlen_q"] % args["BLOCK_M"] == 0,
        "EVEN_N": lambda args: args["seqlen_k"] % (args["BLOCK_N"]) == 0,
    }
)
@triton.jit
def _fwd_kernel(
    Q, K, V, Out,
    Lse, TMP,  # NOTE: TMP is a scratchpad buffer to workaround a compiler bug
    softmax_scale,
    stride_qb, stride_qh, stride_qm,
    stride_kb, stride_kh, stride_kn,
    stride_vb, stride_vh, stride_vn,
    stride_ob, stride_oh, stride_om,
    nheads, seqlen_q, seqlen_k,
    CACHE_KEY_SEQLEN_Q, CACHE_KEY_SEQLEN_K,
    IS_CAUSAL: tl.constexpr,
    BLOCK_HEADDIM: tl.constexpr,
    EVEN_M: tl.constexpr, EVEN_N: tl.constexpr,
    BLOCK_M: tl.constexpr, BLOCK_N: tl.constexpr,
):
    start_m = tl.program_id(0)
    off_hb = tl.program_id(1)
    off_b = off_hb // nheads
    off_h = off_hb % nheads
    # off_b = tl.program_id(1)
    # off_h = tl.program_id(2)
    # off_hb = off_b * nheads + off_h
    # initialize offsets
    offs_m = start_m * BLOCK_M + tl.arange(0, BLOCK_M)
    offs_n = tl.arange(0, BLOCK_N)
    offs_d = tl.arange(0, BLOCK_HEADDIM)
    # Initialize pointers to Q, K, V
    # Adding parenthesis around indexing might use int32 math instead of int64 math?
    # https://github.com/openai/triton/issues/741
    # I'm seeing a tiny bit of difference (5-7us)
    q_ptrs = Q + off_b * stride_qb + off_h * stride_qh + (offs_m[:, None] * stride_qm + offs_d[None, :])
    k_ptrs = K + off_b * stride_kb + off_h * stride_kh + (offs_n[:, None] * stride_kn + offs_d[None, :])
    v_ptrs = V + off_b * stride_vb + off_h * stride_vh + (offs_n[:, None] * stride_vn + offs_d[None, :])
    # initialize pointer to m and l
    t_ptrs = TMP + off_hb * seqlen_q + offs_m
    lse_i = tl.zeros([BLOCK_M], dtype=tl.float32) - float("inf")
    m_i = tl.zeros([BLOCK_M], dtype=tl.float32) - float("inf")
    acc_o = tl.zeros([BLOCK_M, BLOCK_HEADDIM], dtype=tl.float32)
    # load q: it will stay in SRAM throughout
    if EVEN_M:
        q = tl.load(q_ptrs)
    else:
        q = tl.load(q_ptrs, mask=offs_m[:, None] < seqlen_q, other=0.0)
    # loop over k, v and update accumulator
    end_n = seqlen_k if not IS_CAUSAL else (start_m + 1) * BLOCK_M
    for start_n in range(0, end_n, BLOCK_N):
        start_n = tl.multiple_of(start_n, BLOCK_N)
        # -- compute qk ----
        if EVEN_N:
            k = tl.load(k_ptrs + start_n * stride_kn)
        else:
            k = tl.load(k_ptrs + start_n * stride_kn, mask=(start_n + offs_n)[:, None] < seqlen_k,
                        other=0.0)
        qk = tl.zeros([BLOCK_M, BLOCK_N], dtype=tl.float32)
        qk += tl.dot(q, k, trans_b=True)
        # qk *= softmax_scale
        # if EVEN_N:
        #     if IS_CAUSAL:
        #         qk += tl.where(offs_m[:, None] >= (start_n + offs_n)[None, :], 0, float("-inf"))
        # else:  # Need to mask out otherwise the softmax is wrong
        #     if not IS_CAUSAL:
        #         qk += tl.where((start_n + offs_n)[None, :] < seqlen_k, 0, float("-inf"))
        #     else:
        #         qk += tl.where((offs_m[:, None] >= (start_n + offs_n)[None, :])
        #                        & ((start_n + offs_n)[None, :] < seqlen_k), 0, float("-inf"))
        if not EVEN_N:
            qk += tl.where((start_n + offs_n)[None, :] < seqlen_k, 0, float("-inf"))
        if IS_CAUSAL:
            qk += tl.where(offs_m[:, None] >= (start_n + offs_n)[None, :], 0, float("-inf"))
        m_ij = tl.maximum(tl.max(qk, 1) * softmax_scale, lse_i)
        # Slightly faster to multiply the softmax_scale here since the compiler can then
        # fuse the mult and add into an fma instruction.
        p = tl.exp(qk * softmax_scale - m_ij[:, None])
        l_ij = tl.sum(p, 1)

        # scale acc_o
        acc_o_scale = tl.exp(m_i - m_ij)

        # # -- update output accumulator --
        # BUG: have to store and immediately load
        tl.store(t_ptrs, acc_o_scale)
        acc_o_scale = tl.load(t_ptrs)
        acc_o = acc_o * acc_o_scale[:, None]
        # update acc_o
        if EVEN_N:
            v = tl.load(v_ptrs + start_n * stride_vn)
        else:
            v = tl.load(v_ptrs + start_n * stride_vn, mask=(start_n + offs_n)[:, None] < seqlen_k,
                        other=0.0)
        p = p.to(v.dtype)
        acc_o += tl.dot(p, v)

        # -- update statistics
        m_i = m_ij
        l_i_new = tl.exp(lse_i - m_ij) + l_ij
        lse_i = m_ij + tl.log(l_i_new)

    o_scale = tl.exp(m_i - lse_i)
    # BUG: have to store and immediately load
    tl.store(t_ptrs, o_scale)
    o_scale = tl.load(t_ptrs)
    acc_o = acc_o * o_scale[:, None]
    # rematerialize offsets to save registers
    start_m = tl.program_id(0)
    offs_m = start_m * BLOCK_M + tl.arange(0, BLOCK_M)
    # write back l and m
    lse_ptrs = Lse + off_hb * seqlen_q + offs_m
    tl.store(lse_ptrs, lse_i)
    # initialize pointers to output
    offs_n = tl.arange(0, BLOCK_HEADDIM)
    out_ptrs = Out + off_b * stride_ob + off_h * stride_oh + (offs_m[:, None] * stride_om + offs_n[None, :])
    if EVEN_M:
        tl.store(out_ptrs, acc_o)
    else:
        tl.store(out_ptrs, acc_o, mask=offs_m[:, None] < seqlen_q)


@triton.heuristics(
    {
        "EVEN_M": lambda args: args["seqlen_q"] % args["BLOCK_M"] == 0,
    }
)
@triton.jit
def _bwd_preprocess_do_o_dot(
    Out, DO, Delta,
    stride_ob, stride_oh, stride_om,
    stride_dob, stride_doh, stride_dom,
    nheads, seqlen_q, seqlen_q_rounded,
    EVEN_M: tl.constexpr,
    BLOCK_M: tl.constexpr, BLOCK_HEADDIM: tl.constexpr,
):
    start_m = tl.program_id(0)
    off_hb = tl.program_id(1)
    off_b = off_hb // nheads
    off_h = off_hb % nheads
    # initialize offsets
    offs_m = start_m * BLOCK_M + tl.arange(0, BLOCK_M)
    offs_d = tl.arange(0, BLOCK_HEADDIM)
    # load
    if EVEN_M:
        o = tl.load(Out + off_b * stride_ob + off_h * stride_oh + offs_m[:, None] * stride_om + offs_d[None, :]).to(tl.float32)
        do = tl.load(DO + off_b * stride_dob + off_h * stride_doh + offs_m[:, None] * stride_dom + offs_d[None, :]).to(tl.float32)
    else:
        o = tl.load(Out + off_b * stride_ob + off_h * stride_oh + offs_m[:, None] * stride_om + offs_d[None, :],
                    mask=offs_m[:, None] < seqlen_q, other=0.0).to(tl.float32)
        do = tl.load(DO + off_b * stride_dob + off_h * stride_doh + offs_m[:, None] * stride_dom + offs_d[None, :],
                     mask=offs_m[:, None] < seqlen_q, other=0.0).to(tl.float32)
    delta = tl.sum(o * do, axis=1)
    # write-back
    tl.store(Delta + off_hb * seqlen_q_rounded + offs_m, delta)


@triton.jit
def _bwd_kernel_one_col_block(
    start_n,
    Q, K, V, softmax_scale,
    DO, DQ, DK, DV,
    LSE, D,
    stride_qm, stride_kn, stride_vn, stride_dom, stride_dqm, stride_dkn, stride_dvn,
    seqlen_q, seqlen_k, seqlen_do, seqlen_dq,
    ATOMIC_ADD: tl.constexpr,
    IS_CAUSAL: tl.constexpr,
    BLOCK_HEADDIM: tl.constexpr,
    EVEN_M: tl.constexpr, EVEN_N: tl.constexpr,
    BLOCK_M: tl.constexpr, BLOCK_N: tl.constexpr,
):
    # We need to make sure begin_m is a multiple of BLOCK_M (not BLOCK_N)
    begin_m = 0 if not IS_CAUSAL else ((start_n * BLOCK_N) // BLOCK_M) * BLOCK_M
    # initialize row/col offsets
    offs_qm = begin_m + tl.arange(0, BLOCK_M)
    offs_n = start_n * BLOCK_N + tl.arange(0, BLOCK_N)
    offs_m = tl.arange(0, BLOCK_M)
    offs_k = tl.arange(0, BLOCK_HEADDIM)
    # initialize pointers to value-like data
    q_ptrs = Q + (offs_qm[:, None] * stride_qm + offs_k[None, :])
    k_ptrs = K + (offs_n[:, None] * stride_kn + offs_k[None, :])
    v_ptrs = V + (offs_n[:, None] * stride_vn + offs_k[None, :])
    do_ptrs = DO + (offs_qm[:, None] * stride_dom + offs_k[None, :])
    dq_ptrs = DQ + (offs_qm[:, None] * stride_dqm + offs_k[None, :])
    # initialize dv amd dk
    dv = tl.zeros([BLOCK_N, BLOCK_HEADDIM], dtype=tl.float32)
    dk = tl.zeros([BLOCK_N, BLOCK_HEADDIM], dtype=tl.float32)
    # k and v stay in SRAM throughout
    if EVEN_N:
        k = tl.load(k_ptrs)
        v = tl.load(v_ptrs)
    else:
        k = tl.load(k_ptrs, mask=offs_n[:, None] < seqlen_k, other=0.0)
        v = tl.load(v_ptrs, mask=offs_n[:, None] < seqlen_k, other=0.0)
    # loop over rows
    num_block_m = tl.cdiv(seqlen_q, BLOCK_M)
    for start_m in range(begin_m, num_block_m * BLOCK_M, BLOCK_M):
        start_m = tl.multiple_of(start_m, BLOCK_M)
        offs_m_curr = start_m + offs_m
        # load q, k, v, do on-chip
        # if True:
        if True:
            q = tl.load(q_ptrs)
        else:
            q = tl.load(q_ptrs, mask=offs_m_curr[:, None] < seqlen_q, other=0.0)
        # recompute p = softmax(qk, dim=-1).T
        qk = tl.dot(q, k, trans_b=True)
        if EVEN_N:
            if IS_CAUSAL:
                qk = tl.where(offs_m_curr[:, None] >= (offs_n[None, :]), qk, float("-inf"))
        else:    # Need to mask out otherwise the softmax is wrong
            if not IS_CAUSAL:
                qk += tl.where(offs_n[None, :] < seqlen_k, 0, float("-inf"))
            else:
                qk = tl.where((offs_m_curr[:, None] >= (offs_n[None, :]))
                              & (offs_n[None, :] < seqlen_k), qk, float("-inf"))
        # if EVEN_M:
        if True:
            lse_i = tl.load(LSE + offs_m_curr)
        else:
            lse_i = tl.load(LSE + offs_m_curr, mask=offs_m_curr < seqlen_q, other=float('inf'))
        p = tl.exp(qk * softmax_scale - lse_i[:, None])
        # compute dv
        # if EVEN_M:
        if True:
            do = tl.load(do_ptrs)
        else:
            # do = tl.load(do_ptrs, mask=offs_m_curr[:, None] < seqlen_q, other=0.0)
            do = tl.load(do_ptrs, mask=offs_m_curr[:, None] < seqlen_do, other=0.0)
        dv += tl.dot(p.to(do.dtype), do, trans_a=True)
        # compute dp = dot(v, do)
        dp = tl.dot(do, v, trans_b=True)
        # compute ds = p * (dp - delta[:, None])
        # Putting the subtraction after the dp matmul (instead of before) is slightly faster
        Di = tl.load(D + offs_m_curr)
        # Converting ds to q.dtype here reduces register pressure and makes it much faster
        # for BLOCK_HEADDIM=128
        ds = (p * (dp - Di[:, None]) * softmax_scale).to(q.dtype)
        # compute dk = dot(ds.T, q)
        dk += tl.dot(ds, q, trans_a=True)
        # compute dq
        if not ATOMIC_ADD:
            # if EVEN_M:
            if True:
                dq = tl.load(dq_ptrs, eviction_policy="evict_last")
            else:
                # dq = tl.load(dq_ptrs, mask=offs_m_curr[:, None] < seqlen_q, other=0.0,
                dq = tl.load(dq_ptrs, mask=offs_m_curr[:, None] < seqlen_dq, other=0.0,
                             eviction_policy="evict_last")
            dq += tl.dot(ds, k)
            # if EVEN_M:
            if True:
                tl.store(dq_ptrs, dq, eviction_policy="evict_last")
            else:
                # tl.store(dq_ptrs, dq, mask=offs_m_curr[:, None] < seqlen_q,
                tl.store(dq_ptrs, dq, mask=offs_m_curr[:, None] < seqlen_dq,
                         eviction_policy="evict_last")
        else:  # If we're parallelizing across the seqlen_k dimension
            dq = tl.dot(ds, k)
            # if EVEN_M:
            if True:
                tl.atomic_add(dq_ptrs, dq)
            else:
                # tl.atomic_add(dq_ptrs, dq, mask=offs_m_curr[:, None] < seqlen_q)
                tl.atomic_add(dq_ptrs, dq, mask=offs_m_curr[:, None] < seqlen_dq)
        # increment pointers
        dq_ptrs += BLOCK_M * stride_dqm
        q_ptrs += BLOCK_M * stride_qm
        do_ptrs += BLOCK_M * stride_dom
    # write-back
    dv_ptrs = DV + (offs_n[:, None] * stride_dvn + offs_k[None, :])
    dk_ptrs = DK + (offs_n[:, None] * stride_dkn + offs_k[None, :])
    if EVEN_N:
        tl.store(dv_ptrs, dv)
        tl.store(dk_ptrs, dk)
    else:
        tl.store(dv_ptrs, dv, mask=offs_n[:, None] < seqlen_k)
        tl.store(dk_ptrs, dk, mask=offs_n[:, None] < seqlen_k)


def init_to_zero(name):
    # def fn(nargs):
    #     with torch.no_grad():
    #         nargs[name].zero_()
    # return fn
    return lambda nargs: nargs[name].zero_()

@triton.autotune(
    configs=[
        triton.Config({"BLOCK_M": 128, "BLOCK_N": 128, "SEQUENCE_PARALLEL": False}, num_warps=8, num_stages=1, pre_hook=init_to_zero('DQ')),
        # triton.Config({"BLOCK_M": 128, "BLOCK_N": 128, "SEQUENCE_PARALLEL": True}, num_warps=8, num_stages=1, pre_hook=init_to_zero('DQ')),
        # triton.Config({"BLOCK_M": 128, "BLOCK_N": 64, "SEQUENCE_PARALLEL": False}, num_warps=8, num_stages=1, pre_hook=init_to_zero('DQ')),
        # triton.Config({"BLOCK_M": 128, "BLOCK_N": 64, "SEQUENCE_PARALLEL": True}, num_warps=8, num_stages=1, pre_hook=init_to_zero('DQ')),
        # triton.Config({"BLOCK_M": 64, "BLOCK_N": 64, "SEQUENCE_PARALLEL": False}, num_warps=4, num_stages=1, pre_hook=init_to_zero('DQ')),
        # triton.Config({"BLOCK_M": 64, "BLOCK_N": 64, "SEQUENCE_PARALLEL": True}, num_warps=4, num_stages=1, pre_hook=init_to_zero('DQ')),
        # triton.Config({"BLOCK_M": 128, "BLOCK_N": 128, "SEQUENCE_PARALLEL": False}, num_warps=8, num_stages=1),
        # triton.Config({"BLOCK_M": 128, "BLOCK_N": 128, "SEQUENCE_PARALLEL": True}, num_warps=8, num_stages=1),
        # triton.Config({"BLOCK_M": 128, "BLOCK_N": 64, "SEQUENCE_PARALLEL": False}, num_warps=4, num_stages=1),
        # triton.Config({"BLOCK_M": 128, "BLOCK_N": 64, "SEQUENCE_PARALLEL": True}, num_warps=4, num_stages=1),
        # triton.Config({"BLOCK_M": 64, "BLOCK_N": 64, "SEQUENCE_PARALLEL": False}, num_warps=4, num_stages=1),
        # triton.Config({"BLOCK_M": 64, "BLOCK_N": 64, "SEQUENCE_PARALLEL": True}, num_warps=4, num_stages=1),
    ],
    key=['CACHE_KEY_SEQLEN_Q', 'CACHE_KEY_SEQLEN_K', 'IS_CAUSAL', 'BLOCK_HEADDIM'],
    # reset_to_zero=['DQ']
)
@triton.heuristics(
    {
        "EVEN_M": lambda args: args["seqlen_q"] % args["BLOCK_M"] == 0,
        "EVEN_N": lambda args: args["seqlen_k"] % (args["BLOCK_N"]) == 0,
    }
)
@triton.jit
def _bwd_kernel(
    Q, K, V,
    DO, DQ, DK, DV,
    LSE, D,
    softmax_scale,
    stride_qb, stride_qh, stride_qm,
    stride_kb, stride_kh, stride_kn,
    stride_vb, stride_vh, stride_vn,
    stride_dob, stride_doh, stride_dom,
    stride_dqb, stride_dqh, stride_dqm,
    stride_dkb, stride_dkh, stride_dkn,
    stride_dvb, stride_dvh, stride_dvn,
    nheads, seqlen_q, seqlen_k, seqlen_q_rounded, seqlen_do, seqlen_dq,
    CACHE_KEY_SEQLEN_Q, CACHE_KEY_SEQLEN_K,
    IS_CAUSAL: tl.constexpr,
    BLOCK_HEADDIM: tl.constexpr,
    SEQUENCE_PARALLEL: tl.constexpr,
    EVEN_M: tl.constexpr, EVEN_N: tl.constexpr,
    BLOCK_M: tl.constexpr, BLOCK_N: tl.constexpr,
):
    off_hb = tl.program_id(1)
    off_b = off_hb // nheads
    off_h = off_hb % nheads
    # offset pointers for batch/head
    Q += off_b * stride_qb + off_h * stride_qh
    K += off_b * stride_kb + off_h * stride_kh
    V += off_b * stride_vb + off_h * stride_vh
    DO += off_b * stride_dob + off_h * stride_doh
    DQ += off_b * stride_dqb + off_h * stride_dqh
    DK += off_b * stride_dkb + off_h * stride_dkh
    DV += off_b * stride_dvb + off_h * stride_dvh
    # pointer to row-wise quantities in value-like data
    D += off_hb * seqlen_q_rounded
    LSE += off_hb * seqlen_q_rounded
    if not SEQUENCE_PARALLEL:
        num_block_n = tl.cdiv(seqlen_k, BLOCK_N)
        # num_block_n = 1
        for start_n in range(0, num_block_n):
            _bwd_kernel_one_col_block(
                start_n,
                Q, K, V, softmax_scale,
                DO, DQ, DK, DV,
                LSE, D,
                stride_qm, stride_kn, stride_vn, stride_dom, stride_dqm, stride_dkn, stride_dvn,
                seqlen_q, seqlen_k, seqlen_do, seqlen_dq,
                ATOMIC_ADD=False,
                IS_CAUSAL=IS_CAUSAL,
                BLOCK_HEADDIM=BLOCK_HEADDIM,
                EVEN_M=EVEN_M, EVEN_N=EVEN_N,
                BLOCK_M=BLOCK_M, BLOCK_N=BLOCK_N
            )
    else:
        start_n = tl.program_id(0)
        _bwd_kernel_one_col_block(
            start_n,
            Q, K, V, softmax_scale,
            DO, DQ, DK, DV,
            LSE, D,
            stride_qm, stride_kn, stride_vn, stride_dom, stride_dqm, stride_dkn, stride_dvn,
            seqlen_q, seqlen_k, seqlen_do, seqlen_dq,
            ATOMIC_ADD=True,
            IS_CAUSAL=IS_CAUSAL,
            BLOCK_HEADDIM=BLOCK_HEADDIM,
            EVEN_M=EVEN_M, EVEN_N=EVEN_N,
            BLOCK_M=BLOCK_M, BLOCK_N=BLOCK_N
        )


def _flash_attn_forward(q, k, v, causal=False, softmax_scale=None):
    # shape constraints
    batch, seqlen_q, nheads, d = q.shape
    _, seqlen_k, _, _ = k.shape
    assert k.shape == (batch, seqlen_k, nheads, d)
    assert v.shape == (batch, seqlen_k, nheads, d)
    assert d in {16, 32, 64, 128}
    assert q.dtype == k.dtype == v.dtype, 'All tensors must have the same type'
    assert q.dtype in [torch.float16, torch.bfloat16], 'Only support fp16 and bf16'
    assert q.is_cuda and k.is_cuda and v.is_cuda
    softmax_scale = softmax_scale or 1.0 / math.sqrt(d)
    seqlen_q_rounded = math.ceil(seqlen_q / 128) * 128
    lse = torch.empty((batch, nheads, seqlen_q_rounded), device=q.device, dtype=torch.float32)
    # lse = torch.full((batch, nheads, seqlen_q_rounded), float('inf'), device=q.device,
                     # dtype=torch.float32)
    tmp = torch.empty((batch, nheads, seqlen_q_rounded), device=q.device, dtype=torch.float32)
    o = torch.empty_like(q)

    # BLOCK = 128
    # num_warps = 4 if d <= 64 else 8
    grid = lambda META: (triton.cdiv(seqlen_q, META["BLOCK_M"]), batch * nheads)
    _fwd_kernel[grid](
        q, k, v, o,
        lse, tmp,
        softmax_scale,
        q.stride(0), q.stride(2), q.stride(1),
        k.stride(0), k.stride(2), k.stride(1),
        v.stride(0), v.stride(2), v.stride(1),
        o.stride(0), o.stride(2), o.stride(1),
        nheads, seqlen_q, seqlen_k,
        seqlen_q // 32,  seqlen_k // 32, # key for triton cache (limit number of compilations)
        # Can't use kwargs here because triton autotune expects key to be args, not kwargs
        # IS_CAUSAL=causal, BLOCK_HEADDIM=d,
        causal, d,
        # BLOCK_M=BLOCK, BLOCK_N=BLOCK,
        # num_warps=num_warps,
        # num_stages=1,
    )
    return o, lse, softmax_scale  # softmax_scale could have been updated


def _flash_attn_backward(do, q, k, v, o, lse, dq, dk, dv, causal=False, softmax_scale=None):
    # Make sure that the last dimension is contiguous
    seqlen_q = q.shape[1]
    seqlen_q_rounded = math.ceil(seqlen_q / 128) * 128
    attn = torch.softmax(torch.einsum('bthd,bshd->bhts', q * softmax_scale, k), dim=-1)
    # do = torch.nn.functional.pad(do, (0, 0, 0, 0, 0, seqlen_q_rounded - seqlen_q))
    # o = torch.nn.functional.pad(o, (0, 0, 0, 0, 0, seqlen_q_rounded - seqlen_q))
    q = torch.nn.functional.pad(q, (0, 0, 0, 0, 0, seqlen_q_rounded - seqlen_q))
    attn_new = torch.softmax(torch.einsum('bthd,bshd->bhts', q * softmax_scale, k), dim=-1)
    if do.stride(-1) != 1:
        do = do.contiguous()
    batch, seqlen_q, nheads, d = q.shape
    _, seqlen_k, _, _ = k.shape
    seqlen_q_rounded = math.ceil(seqlen_q / 128) * 128
    assert lse.shape == (batch, nheads, seqlen_q_rounded)
    # dq_accum = torch.zeros_like(q, dtype=torch.float32)
    # dq_accum = torch.empty_like(q, dtype=torch.float32)
    # dq_accum = torch.empty(batch, seqlen_q_rounded, nheads, d, device=q.device, dtype=torch.float32)
    dq_accum = torch.empty(batch, do.shape[1], nheads, d, device=q.device, dtype=torch.float32)
    delta = torch.empty_like(lse)
    # delta = torch.zeros_like(lse)
    grid = lambda META: (triton.cdiv(seqlen_q, META["BLOCK_M"]), batch * nheads)
    _bwd_preprocess_do_o_dot[grid](
        o, do, delta,
        o.stride(0), o.stride(2), o.stride(1),
        do.stride(0), do.stride(2), do.stride(1),
        # nheads, seqlen_q, seqlen_q_rounded,
        nheads, o.shape[1], seqlen_q_rounded,
        BLOCK_M=128, BLOCK_HEADDIM=d,
    )

    # TODO: There are 2 Memcpy DtoD when I use the autotuner.
    # BLOCK_M = 128
    # BLOCK_N = 64
    # num_warps = 4
    grid = lambda META: (triton.cdiv(seqlen_k, META["BLOCK_N"]) if META["SEQUENCE_PARALLEL"] else 1,
                    batch * nheads)
    _bwd_kernel[grid](
        q, k, v,
        do, dq_accum, dk, dv,
        lse, delta,
        softmax_scale,
        q.stride(0), q.stride(2), q.stride(1),
        k.stride(0), k.stride(2), k.stride(1),
        v.stride(0), v.stride(2), v.stride(1),
        do.stride(0), do.stride(2), do.stride(1),
        dq_accum.stride(0), dq_accum.stride(2), dq_accum.stride(1),
        dk.stride(0), dk.stride(2), dk.stride(1),
        dv.stride(0), dv.stride(2), dv.stride(1),
        nheads, seqlen_q, seqlen_k, seqlen_q_rounded, do.shape[1], dq.shape[1],
        seqlen_q // 32,  seqlen_k // 32, # key for triton cache (limit number of compilations)
        # Can't use kwargs here because triton autotune expects key to be args, not kwargs
        # IS_CAUSAL=causal, BLOCK_HEADDIM=d,
        causal, d,
        # SEQUENCE_PARALLEL=False,
        # BLOCK_M=BLOCK_M, BLOCK_N=BLOCK_N,
        # num_warps=num_warps,
        # num_stages=1,
    )
    # dq.copy_(dq_accum)
    # dq.copy_(dq_accum[:, :seqlen_q])
    dq.copy_(dq_accum[:, :dq.shape[1]])


class _attention(torch.autograd.Function):

    @staticmethod
    def forward(ctx, q, k, v, causal=False, softmax_scale=None):
        # Make sure that the last dimension is contiguous
        q, k, v = [x if x.stride(-1) == 1 else x.contiguous() for x in [q, k, v]]
        o, lse, ctx.softmax_scale = _flash_attn_forward(q, k, v, causal=causal,
                                                        softmax_scale=softmax_scale)
        ctx.save_for_backward(q, k, v, o, lse)
        ctx.causal = causal
        return o

    @staticmethod
    def backward(ctx, do):
        q, k, v, o, lse = ctx.saved_tensors
        dq = torch.empty_like(q)
        dk = torch.empty_like(k)
        dv = torch.empty_like(v)
        _flash_attn_backward(do, q, k, v, o, lse, dq, dk, dv,
                             causal=ctx.causal, softmax_scale=ctx.softmax_scale)
        return dq, dk, dv, None, None


attention = _attention.apply
