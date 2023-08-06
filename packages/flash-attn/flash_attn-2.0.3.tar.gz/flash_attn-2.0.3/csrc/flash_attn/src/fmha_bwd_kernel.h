/***************************************************************************************************
 * Copyright (c) 2023, Tri Dao.
 ******************************************************************************/

#pragma once

// #include "cute/algorithm/copy.hpp"
// #include "cute/atom/mma_atom.hpp"
// #include "cute/atom/copy_atom.hpp"

#include "fmha_kernel.h"
#include <fmha/kernel_traits.h>
#include <fmha/utils.h>

#include "cutlass/cutlass.h"
#include "cutlass/layout/layout.h"
#include <cutlass/array.h>
#include <cutlass/numeric_types.h>
#include "cutlass/numeric_conversion.h"

namespace fmha {

using namespace cute;

////////////////////////////////////////////////////////////////////////////////////////////////////

template <int THREADS_PER_ROW, typename elem_type=__half, typename Engine0, typename Layout0,
          typename Engine1, typename Layout1>
inline __device__ void dot_do_o(Tensor<Engine0, Layout0> const &do_, Tensor<Engine0, Layout0> const &o,
                                Tensor<Engine1, Layout1> &gdP_sum, const float scale) {
    static_assert(Layout0::rank == 3, "Only support 2D Tensor");
    static_assert(Layout1::rank == 1, "Only support 1D Tensor");
    // Reshape do_ and o from (8, kBlockM / 32, 1) to (kBlockM / 32, 8)
    static_assert(decltype(size<2>(do_))::value == 1);
    static_assert(decltype(size<2>(o))::value == 1);
    Tensor do_reshaped = make_tensor(do_.data(), make_layout(get<1>(do_.layout()), get<0>(do_.layout())));
    Tensor o_reshaped = make_tensor(o.data(), make_layout(get<1>(o.layout()), get<0>(o.layout())));
    Tensor dP_sum = make_tensor<float>(size<0>(do_reshaped));
    CUTE_STATIC_ASSERT_V(size<0>(do_reshaped) == size<0>(o_reshaped));
    CUTE_STATIC_ASSERT_V(size<1>(do_reshaped) == size<1>(o_reshaped));
    fmha::SumOp<float> sum_op;
    constexpr int kNRows = size<1>(do_reshaped);
    cutlass::NumericArrayConverter<float, elem_type, kNRows, cutlass::FloatRoundStyle::round_to_nearest> convert;
    #pragma unroll
    for (int mi = 0; mi < size<0>(do_reshaped); ++mi) {
        auto do_fp16 = convert(*reinterpret_cast<const cutlass::Array<elem_type, kNRows>*>(do_reshaped(mi, _).data()));
        auto o_fp16 = convert(*reinterpret_cast<const cutlass::Array<elem_type, kNRows>*>(o_reshaped(mi, _).data()));
        dP_sum(mi) = do_fp16[0] * o_fp16[0];
        #pragma unroll
        for (int ni = 1; ni < kNRows; ni++) {
            dP_sum(mi) += do_fp16[ni] * o_fp16[ni];
        }
        dP_sum(mi) = fmha::Allreduce<THREADS_PER_ROW>::run(dP_sum(mi), sum_op) * scale;
        // TODO: when we change headdim from 64 to 128, this indexing should change
        if (threadIdx.x % THREADS_PER_ROW == 0) {
            gdP_sum(mi * 32 + threadIdx.x / THREADS_PER_ROW) = dP_sum(mi);
        }
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////////

template<typename Kernel_traits, bool Is_dropout, bool Is_causal, bool Is_first, bool Is_last, typename Params, typename Prng>
inline __device__ void compute_dq_dk_dv_1col(const Params &params, const int bidb, const int bidh, Prng &ph) {

    using Element = typename Kernel_traits::Element;
    using ElementAccum = typename Kernel_traits::ElementAccum;

    // Shared memory.
    extern __shared__ char smem_[];

    // The thread index.
    const int tidx = threadIdx.x;

    const BlockInfoPadded<Kernel_traits::THREADS> binfo(params, bidb, bidh, tidx);
    // if( binfo.stop_early(loop_step_idx * Cta_tile_p::N) ) return;

    // fmha::Mask<Cta_tile_p, Is_causal> mask(binfo, tidx, loop_step_idx);

    using X = Underscore;

    constexpr int kBlockM = Kernel_traits::kBlockM;
    constexpr int kBlockN = Kernel_traits::kBlockN;
    constexpr int kHeadDim = Kernel_traits::kHeadDim;

    typename Kernel_traits::GmemTiledCopyQKV gmem_tiled_copy_qkv;
    typename Kernel_traits::GmemTiledCopydO gmem_tiled_copy_do;

    // if (cute::thread0()) { gmem_tiled_copy_qkv.print_all(); }

    const uint32_t row_offset_q = binfo.sum_s_q * params.q_row_stride_in_elts + binfo.bidh * params.q_head_stride_in_elts;
    const uint32_t row_offset_k = binfo.sum_s_k * params.k_row_stride_in_elts + binfo.bidh * params.k_head_stride_in_elts;
    const uint32_t row_offset_v = binfo.sum_s_k * params.v_row_stride_in_elts + binfo.bidh * params.v_head_stride_in_elts;
    const uint32_t row_offset_do = binfo.sum_s_q * params.do_row_stride_in_elts + binfo.bidh * params.do_head_stride_in_elts;
    const uint32_t row_offset_o = binfo.sum_s_q * params.o_row_stride_in_elts + binfo.bidh * params.o_head_stride_in_elts;
    const uint32_t row_offset_summary = (bidb * params.h + bidh) * params.seqlen_q;

    // We assume that params.d == kHeadDim for now
    Tensor gQ = make_tensor(make_gmem_ptr(reinterpret_cast<Element *>(params.q_ptr) + row_offset_q),
                            Shape<Int<kBlockM>, Int<kHeadDim>>{}, make_stride(params.q_row_stride_in_elts, _1{}));
    Tensor gK = make_tensor(make_gmem_ptr(reinterpret_cast<Element *>(params.k_ptr) + row_offset_k),
                            Shape<Int<kBlockN>, Int<kHeadDim>>{}, make_stride(params.k_row_stride_in_elts, _1{}));
    Tensor gV = make_tensor(make_gmem_ptr(reinterpret_cast<Element *>(params.v_ptr) + row_offset_v),
                            Shape<Int<kBlockN>, Int<kHeadDim>>{}, make_stride(params.v_row_stride_in_elts, _1{}));
    Tensor gdO = make_tensor(make_gmem_ptr(reinterpret_cast<Element *>(params.do_ptr) + row_offset_do),
                             Shape<Int<kBlockM>, Int<kHeadDim>>{}, make_stride(params.do_row_stride_in_elts, _1{}));
    Tensor gO = make_tensor(make_gmem_ptr(reinterpret_cast<Element *>(params.o_ptr) + row_offset_o),
                            Shape<Int<kBlockM>, Int<kHeadDim>>{}, make_stride(params.do_row_stride_in_elts, _1{}));
    Tensor gLSE = make_tensor(make_gmem_ptr(reinterpret_cast<ElementAccum *>(params.softmax_lse_ptr) + row_offset_summary),
                              Shape<Int<kBlockM>>{}, Stride<_1>{});
    Tensor gdP_sum = make_tensor(make_gmem_ptr(reinterpret_cast<ElementAccum *>(params.dsoftmax_sum) + row_offset_summary),
                                 Shape<Int<kBlockM>>{}, Stride<_1>{});

    auto gmem_thr_copy_qkv = gmem_tiled_copy_qkv.get_slice(tidx);
    Tensor tQgQ = gmem_thr_copy_qkv.partition_S(gQ);
    // if (cute::thread0()) { print(tQgQ); }
    // Tensor tKgK = copy_q_thr.partition_S(gK);  // (KCPY, KCPY_N, KCPY_K, n)
    Tensor tKgK = gmem_thr_copy_qkv.partition_S(gK);  // (KCPY, KCPY_N, KCPY_K)
    // if (cute::thread0()) { print(tKgK.layout()); printf("\n"); }
    // Tensor tVgV = gmem_thr_copy_qkv.partition_S(gV);  // (VCPY, VCPY_N, VCPY_K, n)
    Tensor tVgV = gmem_thr_copy_qkv.partition_S(gV);  // (VCPY, VCPY_N, VCPY_K)

    // Tensor tdOgdO = gmem_thr_copy_qkv.partition_S(gdO);
    auto copy_do_thr = gmem_tiled_copy_do.get_slice(tidx);
    Tensor tdOgdO = gmem_thr_copy_qkv.partition_S(gdO);
    Tensor tdOgO = gmem_thr_copy_qkv.partition_S(gO);

    Tensor sQ = make_tensor(make_smem_ptr(reinterpret_cast<Element *>(smem_)),
                            typename Kernel_traits::SmemLayoutQ{});
    Tensor tQsQ = gmem_thr_copy_qkv.partition_D(sQ);
    Tensor sdO = make_tensor(sQ.data() + kBlockM * kHeadDim, typename Kernel_traits::SmemLayoutdO{});
    Tensor tdOsdO = gmem_thr_copy_qkv.partition_D(sdO);
    Tensor sK = make_tensor(sdO.data() + kBlockM * kHeadDim, typename Kernel_traits::SmemLayoutK{});
    Tensor tKsK = gmem_thr_copy_qkv.partition_D(sK);
    Tensor sV = make_tensor(sK.data() + kBlockN * kHeadDim, typename Kernel_traits::SmemLayoutV{});
    Tensor tVsV = gmem_thr_copy_qkv.partition_D(sV);
    Tensor sKtransposed = make_tensor(sK.data(), typename Kernel_traits::SmemLayoutVtransposed{});
    Tensor sKtransposedNoSwizzle = make_tensor(sK.data(),
                                               typename Kernel_traits::SmemLayoutVtransposedNoSwizzle{});
    // if (cute::thread0()) { print(sKtransposed); }
    Tensor sP = make_tensor(sV.data() + kBlockN * kHeadDim, typename Kernel_traits::SmemLayoutP{});
    Tensor sPtransposed = make_tensor(sP.data(), typename Kernel_traits::SmemLayoutPtransposed{});
    Tensor sPtransposedNoSwizzle = make_tensor(sP.data(), typename Kernel_traits::SmemLayoutPtransposedNoSwizzle{});
    Tensor sdS = make_tensor(sP.data() + kBlockM * kBlockN, typename Kernel_traits::SmemLayoutP{});
    Tensor sdStransposed = make_tensor(sdS.data(), typename Kernel_traits::SmemLayoutPtransposed{});
    Tensor sdStransposedNoSwizzle = make_tensor(sdS.data(), typename Kernel_traits::SmemLayoutPtransposedNoSwizzle{});
    Tensor sdOtransposed = make_tensor(sdO.data(), typename Kernel_traits::SmemLayoutdOtransposed{});
    Tensor sdOtransposedNoSwizzle = make_tensor(sdO.data(),
                                                typename Kernel_traits::SmemLayoutdOtransposedNoSwizzle{});
    Tensor sQtransposed = make_tensor(sQ.data(), typename Kernel_traits::SmemLayoutdOtransposed{});
    Tensor sQtransposedNoSwizzle = make_tensor(sQ.data(),
                                               typename Kernel_traits::SmemLayoutdOtransposedNoSwizzle{});

    typename Kernel_traits::TiledMma tiled_mma;
    auto thr_mma = tiled_mma.get_thread_slice(tidx);
    Tensor tSrQ  = thr_mma.partition_fragment_A(sQ);                           // (MMA,MMA_M,MMA_K)
    // if (cute::thread0()) { print(tSrQ.layout()); }
    Tensor tSrK  = thr_mma.partition_fragment_B(sK);                           // (MMA,MMA_N,MMA_K)
    // if (cute::thread(1, 0)) { print(tSrQ); print(tSrK); }
    Tensor tdPrdO  = thr_mma.partition_fragment_A(sdO);                           // (MMA,MMA_M,MMA_K)
    Tensor tdPrV  = thr_mma.partition_fragment_B(sV);                           // (MMA,MMA_N,MMA_K)

    CUTE_STATIC_ASSERT_V(size<2>(tSrQ) == size<2>(tSrK));                      // MMA_K
    CUTE_STATIC_ASSERT_V(size<2>(tdPrdO) == size<2>(tdPrV));                      // MMA_K

    typename Kernel_traits::TiledMmadKV tiled_mma_dkv;
    auto thr_mma_dkv = tiled_mma_dkv.get_thread_slice(tidx);

    //
    // Copy Atom retiling
    //

    auto smem_thr_copy_QdO = make_tiled_copy_A(typename Kernel_traits::SmemCopyAtomQ{}, tiled_mma).get_thread_slice(tidx);
    auto smem_thr_copy_KV = make_tiled_copy_B(typename Kernel_traits::SmemCopyAtomK{}, tiled_mma).get_thread_slice(tidx);

    Tensor tSsQ           = smem_thr_copy_QdO.partition_S(sQ);
    Tensor tSrQ_copy_view = smem_thr_copy_QdO.retile_D(tSrQ);
    CUTE_STATIC_ASSERT_V(size<1>(tSsQ) == size<1>(tSrQ_copy_view));            // M

    Tensor tSsK           = smem_thr_copy_KV.partition_S(sK);
    Tensor tSrK_copy_view = smem_thr_copy_KV.retile_D(tSrK);
    CUTE_STATIC_ASSERT_V(size<1>(tSsK) == size<1>(tSrK_copy_view));            // N

    Tensor tdPsdO           = smem_thr_copy_QdO.partition_S(sdO);
    Tensor tdPrdO_copy_view = smem_thr_copy_QdO.retile_D(tdPrdO);
    CUTE_STATIC_ASSERT_V(size<1>(tdPsdO) == size<1>(tdPrdO_copy_view));            // M

    Tensor tdPsV           = smem_thr_copy_KV.partition_S(sV);
    Tensor tdPrV_copy_view = smem_thr_copy_KV.retile_D(tdPrV);
    CUTE_STATIC_ASSERT_V(size<1>(tdPsV) == size<1>(tdPrV_copy_view));            // N

    // Partition sP and sdS to match the accumulator partitioning
    // This has to be tiled_mma, not tiled_mma_dkv
    auto tPdSsmem = make_tiled_copy_C(typename Kernel_traits::CopyAtomPR2S{}, tiled_mma).get_thread_slice(tidx);
    Tensor tPsmemsP = tPdSsmem.partition_D(sP);                                                 // ((Atom,AtomNum),PIPE_M,PIPE_N)
    Tensor tdSsmemsdS = tPdSsmem.partition_D(sdS);                                                 // ((Atom,AtomNum),PIPE_M,PIPE_N)

    Tensor acc_dv = partition_fragment_C(tiled_mma_dkv, Shape<Int<kBlockN>, Int<kHeadDim>>{});  // MMA, MMA_N, MMA_K
    Tensor tdVrP  = thr_mma_dkv.partition_fragment_A(sPtransposedNoSwizzle);                           // (MMA, MMA_N, MMA_M)
    CUTE_STATIC_ASSERT_V(size<1>(tdVrP) == size<1>(acc_dv));                     // MMA_N
    if (cute::thread0()) { print(tdVrP.layout()); printf("\n"); }
    Tensor tdVrdO  = thr_mma_dkv.partition_fragment_B(sdOtransposedNoSwizzle);                           // (MMA, MMA_K, MMA_M)
    CUTE_STATIC_ASSERT_V(size<1>(tdVrdO) == size<2>(acc_dv));                     // MMA_M
    if (cute::thread0()) { print(tdVrdO.layout()); printf("\n"); }

    Tensor acc_dk = partition_fragment_C(tiled_mma_dkv, Shape<Int<kBlockN>, Int<kHeadDim>>{});  // MMA, MMA_N, MMA_K
    Tensor tdKrdS  = thr_mma_dkv.partition_fragment_A(sdStransposedNoSwizzle);                           // (MMA, MMA_N, MMA_M)
    CUTE_STATIC_ASSERT_V(size<1>(tdKrdS) == size<1>(acc_dk));                     // MMA_N
    if (cute::thread0()) { print(tdKrdS.layout()); printf("\n"); }
    Tensor tdKrQ  = thr_mma_dkv.partition_fragment_B(sQtransposedNoSwizzle);                           // (MMA, MMA_K, MMA_M)
    CUTE_STATIC_ASSERT_V(size<1>(tdKrQ) == size<2>(acc_dk));                     // MMA_M
    if (cute::thread0()) { print(tdKrQ.layout()); printf("\n"); }

    //
    // Copy Atom retiling
    //

    auto smem_thr_copy_PdStransposed = make_tiled_copy_A(typename Kernel_traits::SmemCopyAtomPtransposed{}, tiled_mma_dkv).get_thread_slice(tidx);
    Tensor tdVsP = smem_thr_copy_PdStransposed.partition_S(sPtransposed);
    Tensor tdVrP_copy_view = smem_thr_copy_PdStransposed.retile_D(tdVrP);
    CUTE_STATIC_ASSERT_V(size<1>(tdVsP) == size<1>(tdVrP_copy_view));            // N
    // if (cute::thread0()) { print(tdVsP.layout()); printf("\n"); print(tdVrP_copy_view.layout()); printf("\n"); }

    auto smem_thr_copy_QdOtransposed = make_tiled_copy_B(typename Kernel_traits::SmemCopyAtomdOtransposed{}, tiled_mma_dkv).get_thread_slice(tidx);
    Tensor tdVsdO = smem_thr_copy_QdOtransposed.partition_S(sdOtransposed);
    Tensor tdVrdO_copy_view = smem_thr_copy_QdOtransposed.retile_D(tdVrdO);
    CUTE_STATIC_ASSERT_V(size<1>(tdVsdO) == size<1>(tdVrdO_copy_view));            // K
    // if (cute::thread0()) { print(tdVsdO.layout()); printf("\n"); print(tdVrdO_copy_view.layout()); printf("\n"); }

    Tensor tdKsdS = smem_thr_copy_PdStransposed.partition_S(sdStransposed);
    Tensor tdKrdS_copy_view = smem_thr_copy_PdStransposed.retile_D(tdKrdS);
    CUTE_STATIC_ASSERT_V(size<1>(tdKsdS) == size<1>(tdKrdS_copy_view));            // N
    // if (cute::thread0()) { print(tdKsdS.layout()); printf("\n"); print(tdKrdS_copy_view.layout()); printf("\n"); }

    Tensor tdKsQ = smem_thr_copy_QdOtransposed.partition_S(sQtransposed);
    Tensor tdKrQ_copy_view = smem_thr_copy_QdOtransposed.retile_D(tdKrQ);
    CUTE_STATIC_ASSERT_V(size<1>(tdKsQ) == size<1>(tdKrQ_copy_view));            // K
    // if (cute::thread0()) { print(tdKsQ.layout()); printf("\n"); print(tdKrQ_copy_view.layout()); printf("\n"); }

    // Prologue
    clear(acc_dv);
    clear(acc_dk);

    // copy(gmem_tiled_copy_qkv, tdOgdO, tdOsdO);
    Tensor tdOrdO = make_fragment_like(tdOgdO);
    Tensor tdOrO = make_fragment_like(tdOgO);
    copy(gmem_tiled_copy_do, tdOgdO, tdOrdO);
    copy(gmem_tiled_copy_do, tdOgO, tdOrO);
    copy(gmem_tiled_copy_qkv, tQgQ, tQsQ);
    // cute::cp_async_fence();
    // if (cute::thread(1, 0)) { print(tQrQ); }

    // Tensor tKrK = make_fragment_like(tKsK);
    // // copy(gmem_tiled_copy_qkv, tKgK(_, _, _, 0), tKrK);
    // copy(gmem_tiled_copy_qkv, tKgK, tKrK);
    // // if (cute::thread(1, 0)) { print(tKrK); }

    // // Copy rmem to smem
    // // copy(tQrQ, tQsQ);
    // cute::cp_async_wait<0>();
    // __syncthreads();
    // // if (cute::thread(1, 0)) { print(tQsQ); }
    // // Tensor sQNoSwizzle = make_tensor(make_smem_ptr(reinterpret_cast<Element *>(smem_)), typename Kernel_traits::SmemLayoutQNoSwizzle{});
    // // if (cute::thread0()) { print(sQNoSwizzle); }

    // // Copy rmem to smem
    // copy(tKrK, tKsK);
    copy(gmem_tiled_copy_qkv, tKgK, tKsK);
    copy(gmem_tiled_copy_qkv, tVgV, tVsV);
    // if (cute::thread0()) { print(tdOrdO); print(tdOrO); }
    copy(tdOrdO, tdOsdO);
    dot_do_o<kHeadDim / 8>(tdOrdO, tdOrO, gdP_sum, 1.0);
    cute::cp_async_fence();

    // int m_block_max = (binfo.actual_seqlen_q + kBlockM - 1) / kBlockM;
    int m_block_max = 1;

    // Seems to help a bit even though it says there's more register spilling
    // #pragma unroll 2
    for (int m_block = 0; m_block < m_block_max; ++m_block) {
        Tensor acc_s = partition_fragment_C(tiled_mma, Shape<Int<kBlockM>, Int<kBlockN>>{});  // (MMA=4, MMA_M, MMA_N)
        // if (cute::thread0()) { print(acc_s); }
        CUTE_STATIC_ASSERT_V(size<1>(tSrQ) == size<1>(acc_s));                     // MMA_M
        CUTE_STATIC_ASSERT_V(size<1>(tSrK) == size<2>(acc_s));                     // MMA_N

        clear(acc_s);
        cute::cp_async_wait<0>();
        __syncthreads();
        // if (cute::thread(0, 0)) { print(sQ); print(sK); }
        // if (cute::thread(1, 0)) { print(tKsK); }

        Tensor lse = make_tensor<ElementAccum>(Shape<Int<2 * size<1>(acc_s)>>{});
        #pragma unroll
        for (int mi = 0; mi < size(lse) / 2; ++mi) {
            // printf("tidx = %d, row0 = %d, row1 = %d\n", tidx, tidx / 32 * 16 + (tidx % 32) / 4 + 0, tidx / 32 * 16 + (tidx % 32) / 4 + 8);
            lse(mi * 2) = gLSE(mi * 16 + (tidx % 32) / 4 + 0);
            lse(mi * 2 + 1) = gLSE(mi * 16 + (tidx % 32) / 4 + 8);
        }
        if (cute::thread0()) { print(lse); }

        // // if (cute::thread0()) { print(gV); }
        // if (m_block > 0) {
        //     tVgV.data() = tVgV.data() + kBlockN * params.v_row_stride_in_elts;
        // }
        // Tensor tVrV = make_fragment_like(tVsV);
        // // copy(gmem_tiled_copy_qkv, tVgV(_, _, _, m_block), tVrV);
        // copy(gmem_tiled_copy_qkv, tVgV, tVrV);
        // // if (cute::thread(0, 0)) { print(tVrV); }
        copy(gmem_tiled_copy_qkv, tVgV, tVsV);
        cute::cp_async_fence();

        copy(smem_thr_copy_QdO, tSsQ(_, _, _0{}), tSrQ_copy_view(_, _, _0{}));
        copy(smem_thr_copy_KV, tSsK(_, _, _0{}), tSrK_copy_view(_, _, _0{}));

        // if (cute::thread(0, 0)) { print(tSsQ); print(tSsK); }
        // if (cute::thread(0, 0)) { print(tSrQ); print(tSrK); print(acc_s); }
        // if (cute::thread(0, 0)) { print(tSrQ.layout()); printf("\n"); print(tSrK.layout()); printf("\n"); }

        #pragma unroll
        for (int i = 0; i < size<2>(tSrQ); ++i) {
        // for (int i = 0; i < 1; ++i) {
            // if (cute::thread(0, 0)) { print(tSrQ(_, _, i)); print(tSrK(_, _, i)); }
            if (i < size<2>(tSrQ) - 1) {
                copy(smem_thr_copy_QdO, tSsQ(_, _, i + 1), tSrQ_copy_view(_, _, i + 1));
                copy(smem_thr_copy_KV, tSsK(_, _, i + 1), tSrK_copy_view(_, _, i + 1));
            }
            // if (cute::thread(0, 0)) { print(tSrQ_copy_view(_, _, i)); print(tSrK_copy_view(_, _, i)); }
            // __syncthreads();
            // if (cute::thread(1, 0)) { print(tSrQ_copy_view(_, _, i)); print(tSrK_copy_view(_, _, i)); }
            // __syncthreads();
            // if (cute::thread(2, 0)) { print(tSrQ_copy_view(_, _, i)); print(tSrK_copy_view(_, _, i)); }
            // __syncthreads();
            // if (cute::thread(3, 0)) { print(tSrQ_copy_view(_, _, i)); print(tSrK_copy_view(_, _, i)); }
            cute::gemm(tiled_mma, tSrQ(_, _, i), tSrK(_, _, i), acc_s);
        }

        // if (cute::thread0()) { print(acc_s); }

        // Reshape acc_s from (MMA=4, MMA_M, MMA_N) to (col=(2, MMA_M), row=(2, MMA_N))
        Layout s_l = logical_divide(acc_s.layout(), Shape<_2>{});  // ((2, 2), MMA_M, MMA_N)
        Tensor scores = make_tensor(acc_s.data(),
                                    make_layout(make_layout(get<0, 1>(s_l), get<1>(s_l)),
                                                make_layout(get<0, 0>(s_l), get<2>(s_l))));
        // if (cute::thread(0, 0)) { print(scores); }

        // // Copy rmem to smem
        // copy(tVrV, tVsV);

        // Compute the exponential value.
        fmha::scale_apply_exp2</*scale_max=*/false>(scores, lse, params.scale_log2);
        // if (cute::thread(0, 0)) { print(scores); }
        // Reshape scores from (col=(2, MMA_M), row=(2, MMA_N)) to ((2, 2), MMA_M, MMA_N) if using m16n8k8
        using MMA_N_divisor = typename std::conditional<std::is_same<typename Kernel_traits::TiledMma::Shape_MNK, Shape<_16, _8, _8>>::value,
            _1, _2>::type;
        // Layout p_l = logical_divide(rP.layout(), Shape<X, Shape<X, _2>>{});  // ((2, MMA_M), (2, (2, MMA_N / 2)))
        Layout p_l = logical_divide(scores.layout(), Shape<X, Shape<X, MMA_N_divisor>>{});  // ((2, MMA_M), (2, (2, MMA_N / 2)))
        Tensor rP = make_tensor(scores.data(),
                                make_layout(make_layout(get<1, 0>(p_l), get<0, 0>(p_l), get<1, 1, 0>(p_l)),
                                            get<0, 1>(p_l),
                                            get<1, 1, 1>(p_l)));

        // Convert rP from fp32 to fp16
        cutlass::NumericArrayConverter<Element, ElementAccum, size(rP), cutlass::FloatRoundStyle::round_to_nearest> convert;
        auto frag_p = convert(*reinterpret_cast<const cutlass::Array<ElementAccum, size(rP)>*>(rP.data()));
        Tensor tPrP = make_tensor(make_rmem_ptr<Element>(&frag_p), rP.layout());
        // if (cute::thread0()) { print(tPrP); }
        Tensor tPaP = tPdSsmem.retile_S(tPrP);                                          // ((Atom,AtomNum), MMA_M, MMA_N)
        copy(tPdSsmem, tPaP, tPsmemsP);
        // if (cute::thread0()) { print(tPaP); }
        // if (cute::thread0()) { print(sP); }


        Tensor acc_dp = partition_fragment_C(tiled_mma, Shape<Int<kBlockM>, Int<kBlockN>>{});  // (MMA=4, MMA_M, MMA_N)
        CUTE_STATIC_ASSERT_V(size<1>(tdPrdO) == size<1>(acc_dp));                     // MMA_M
        CUTE_STATIC_ASSERT_V(size<1>(tdPrV) == size<2>(acc_dp));                     // MMA_N
        CUTE_STATIC_ASSERT_V(size<0>(acc_dp) == size<0>(acc_s));                     // MMA
        CUTE_STATIC_ASSERT_V(size<1>(acc_dp) == size<1>(acc_s));                     // MMA
        CUTE_STATIC_ASSERT_V(size<2>(acc_dp) == size<2>(acc_s));                     // MMA

        clear(acc_dp);
        constexpr int kCols = size<0>(scores);
        Tensor dP_sum = make_tensor<ElementAccum>(Int<kCols>{});
        // TODO: when we change headdim from 64 to 128, this indexing might change
        #pragma unroll
        for (int mi = 0; mi < size(dP_sum) / 2; ++mi) {
            dP_sum(mi * 2) = gdP_sum(mi * 16 + (tidx % 32) / 4 + 0);
            dP_sum(mi * 2 + 1) = gdP_sum(mi * 16 + (tidx % 32) / 4 + 8);
        }
        // if (cute::thread0()) { print(dP_sum); }

        copy(smem_thr_copy_QdO, tdPsdO(_, _, _0{}), tdPrdO_copy_view(_, _, _0{}));
        copy(smem_thr_copy_KV, tdPsV(_, _, _0{}), tdPrV_copy_view(_, _, _0{}));

        #pragma unroll
        for (int i = 0; i < size<2>(tdPrdO); ++i) {
            if (i < size<2>(tdPrdO) - 1) {
                copy(smem_thr_copy_QdO, tdPsdO(_, _, i + 1), tdPrdO_copy_view(_, _, i + 1));
                copy(smem_thr_copy_KV, tdPsV(_, _, i + 1), tdPrV_copy_view(_, _, i + 1));
            }
            cute::gemm(tiled_mma, tdPrdO(_, _, i), tdPrV(_, _, i), acc_dp);
        }

        // Reshape acc_dp from (MMA=4, MMA_M, MMA_N) to (col=(2, MMA_M), row=(2, MMA_N))
        Tensor dS = make_tensor(acc_dp.data(), scores.layout());
        #pragma unroll
        for (int mi = 0; mi < size<0>(dS); ++mi) {
            #pragma unroll
            for (int ni = 0; ni < size<1>(dS); ++ni) {
                dS(mi, ni) = (dS(mi, ni) - dP_sum(mi)) * scores(mi, ni);
            }
        }
        // if (cute::thread0()) { print(dS); }
        Tensor dS_reshaped = make_tensor(dS.data(), acc_dp.layout());

        // Convert dS from fp32 to fp16
        auto frag_ds = convert(*reinterpret_cast<const cutlass::Array<ElementAccum, size(dS_reshaped)>*>(dS_reshaped.data()));
        Tensor tdSrdS = make_tensor(make_rmem_ptr<Element>(&frag_ds), dS_reshaped.layout());
        // if (cute::thread0()) { print(tPrP); }
        Tensor tdSadS = tPdSsmem.retile_S(tdSrdS);                                          // ((Atom,AtomNum), MMA_M, MMA_N)
        copy(tPdSsmem, tdSadS, tdSsmemsdS);

        // __syncwarp(); // We need this, not __syncthreads() since the read/write of P is within a warp
        __syncthreads(); // But I'm getting wrong results if I don't call syncthreads???
        CUTE_STATIC_ASSERT_V(size<1>(tdVrP) == size<1>(acc_dv));                     // MMA_N
        CUTE_STATIC_ASSERT_V(size<2>(tdVrP) == size<2>(tdVrdO));                     // MMA_M
        copy(smem_thr_copy_PdStransposed, tdVsP(_, _, 0), tdVrP_copy_view(_, _, 0));
        copy(smem_thr_copy_QdOtransposed, tdVsdO(_, _, 0), tdVrdO_copy_view(_, _, 0));

        #pragma unroll
        for (int i = 0; i < size<2>(tdVrP); ++i) {
            if (i < size<2>(tdVrP) - 1) {
                copy(smem_thr_copy_PdStransposed, tdVsP(_, _, i + 1), tdVrP_copy_view(_, _, i + 1));
                copy(smem_thr_copy_QdOtransposed, tdVsdO(_, _, i + 1), tdVrdO_copy_view(_, _, i + 1));
            }
            cute::gemm(tiled_mma_dkv, tdVrP(_, _, i), tdVrdO(_, _, i), acc_dv);
        }
        // if (cute::thread0()) { print(acc_dv); }

        CUTE_STATIC_ASSERT_V(size<1>(tdKrdS) == size<1>(acc_dk));                     // MMA_N
        CUTE_STATIC_ASSERT_V(size<2>(tdKrdS) == size<2>(tdKrQ));                     // MMA_M
        copy(smem_thr_copy_PdStransposed, tdKsdS(_, _, 0), tdKrdS_copy_view(_, _, 0));
        copy(smem_thr_copy_QdOtransposed, tdKsQ(_, _, 0), tdKrQ_copy_view(_, _, 0));

        #pragma unroll
        for (int i = 0; i < size<2>(tdKrdS); ++i) {
            if (i < size<2>(tdKrdS) - 1) {
                copy(smem_thr_copy_PdStransposed, tdKsdS(_, _, i + 1), tdKrdS_copy_view(_, _, i + 1));
                copy(smem_thr_copy_QdOtransposed, tdKsQ(_, _, i + 1), tdKrQ_copy_view(_, _, i + 1));
            }
            cute::gemm(tiled_mma_dkv, tdKrdS(_, _, i), tdKrQ(_, _, i), acc_dk);
        }
        if (cute::thread0()) { print(acc_dk); }

    }

    __syncthreads();

    // Epilogue

    // Convert acc_dv from fp32 to fp16
    cutlass::NumericArrayConverter<Element, ElementAccum, size(acc_dv), cutlass::FloatRoundStyle::round_to_nearest> convert_dkv;
    auto frag_dv = convert_dkv(*reinterpret_cast<const cutlass::Array<float, size(acc_dv)>*>(acc_dv.data()));
    Tensor rdV = make_tensor(make_rmem_ptr<Element>(&frag_dv), acc_dv.layout());
    auto frag_dk = convert_dkv(*reinterpret_cast<const cutlass::Array<float, size(acc_dk)>*>(acc_dk.data()));
    Tensor rdK = make_tensor(make_rmem_ptr<Element>(&frag_dk), acc_dk.layout());

    Tensor sdV = make_tensor(make_smem_ptr(reinterpret_cast<Element *>(smem_)), typename Kernel_traits::SmemLayoutdKV{});              // (SMEM_N, SMEM_K)
    Tensor sdK = make_tensor(sdV.data() + kBlockN * kHeadDim, typename Kernel_traits::SmemLayoutdKV{});              // (SMEM_N, SMEM_K)

    // Partition sdV and sdK to match the accumulator partitioning
    auto tdKVsmem = make_tiled_copy_C(typename Kernel_traits::CopyAtomdKVR2S{}, tiled_mma_dkv).get_thread_slice(tidx);
    Tensor tdVadV = tdKVsmem.retile_S(rdV);                                          // ((Atom,AtomNum), MMA_M, MMA_N)
    Tensor tdVsmemsdV = tdKVsmem.partition_D(sdV);                                                 // ((Atom,AtomNum),PIPE_M,PIPE_N)
    Tensor tdKadK = tdKVsmem.retile_S(rdK);                                          // ((Atom,AtomNum), MMA_M, MMA_N)
    Tensor tdKsmemsdK = tdKVsmem.partition_D(sdK);                                                 // ((Atom,AtomNum),PIPE_M,PIPE_N)

    copy(tdKVsmem, tdVadV, tdVsmemsdV);
    copy(tdKVsmem, tdKadK, tdKsmemsdK);

    __syncthreads();

    // Tensor mdV = make_tensor(make_gmem_ptr(reinterpret_cast<Element *>(params.dv_ptr) + row_offset_dv),
    //                          make_shape(binfo.actual_seqlen_k, Int<kHeadDim>{}),
    //                          make_stride(params.dv_row_stride_in_elts, _1{}));
    // Tensor gdV = local_tile(mdV, Shape<Int<kBlockM>>{}, make_coord(blockIdx.x));  // (kBlockM, kHeadDim)
    const uint32_t row_offset_dv = binfo.sum_s_k * params.dv_row_stride_in_elts + binfo.bidh * params.dv_head_stride_in_elts;
    Tensor gdV = make_tensor(make_gmem_ptr(reinterpret_cast<Element *>(params.dv_ptr) + row_offset_dv),
                             Shape<Int<kBlockN>, Int<kHeadDim>>{}, make_stride(params.dv_row_stride_in_elts, _1{}));
    const uint32_t row_offset_dk = binfo.sum_s_k * params.dk_row_stride_in_elts + binfo.bidh * params.dk_head_stride_in_elts;
    Tensor gdK = make_tensor(make_gmem_ptr(reinterpret_cast<Element *>(params.dk_ptr) + row_offset_dk),
                             Shape<Int<kBlockN>, Int<kHeadDim>>{}, make_stride(params.dk_row_stride_in_elts, _1{}));

    auto tdKV = typename Kernel_traits::GmemTiledCopydKV{}.get_thread_slice(tidx);
    Tensor tdVsdV = tdKV.partition_S(sdV);                                   //               ((Atom,AtomNum),ATOM_M,ATOM_N)
    Tensor tDgdV = tdKV.partition_D(gdV);
    Tensor tdKsdK = tdKV.partition_S(sdK);                                   //               ((Atom,AtomNum),ATOM_M,ATOM_N)
    Tensor tDgdK = tdKV.partition_D(gdK);

    Tensor tdVrdV = make_tensor<Element>(shape(tDgdV));
    copy(tdKV, tdVsdV, tdVrdV);
    copy(typename Kernel_traits::CopyAtomdKVR2G{}, tdVrdV, tDgdV);
    Tensor tdKrdK = make_tensor<Element>(shape(tDgdK));
    copy(tdKV, tdKsdK, tdKrdK);
    copy(typename Kernel_traits::CopyAtomdKVR2G{}, tdKrdK, tDgdK);

}

////////////////////////////////////////////////////////////////////////////////////////////////////

template<typename Kernel_traits, bool Is_dropout, bool Is_causal, typename Params>
inline __device__ void compute_dq_dk_dv(const Params &params) {

    // The block index for the batch.
    const int bidb = blockIdx.x;
    // const int bidb = blockIdx.y;
    // The block index for the head.
    const int bidh = blockIdx.y;
    // const int bidh = blockIdx.z;
    // The thread index.
    const int tidx = threadIdx.x;

    const int tidx_global = (bidb * params.h + bidh) * blockDim.x * 2 + tidx;
    auto seeds = at::cuda::philox::unpack(params.philox_args);
    Philox ph(std::get<0>(seeds), tidx_global, std::get<1>(seeds));

    fmha::compute_dq_dk_dv_1col<Kernel_traits, Is_dropout, Is_causal, true, true>(params, bidb, bidh, ph);
}

////////////////////////////////////////////////////////////////////////////////////////////////////

} // namespace fmha
