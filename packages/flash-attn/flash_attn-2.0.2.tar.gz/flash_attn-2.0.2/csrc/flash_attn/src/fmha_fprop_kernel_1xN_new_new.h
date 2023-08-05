/***************************************************************************************************
 * Copyright (c) 2022, Tri Dao.
 * Copyright (c) 2011-2021, NVIDIA CORPORATION.  All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in the
 *       documentation and/or other materials provided with the distribution.
 *     * Neither the name of the NVIDIA CORPORATION nor the
 *       names of its contributors may be used to endorse or promote products
 *       derived from this software without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL NVIDIA CORPORATION BE LIABLE FOR ANY
 * DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 ******************************************************************************/

#pragma once

// #include "cute/algorithm/copy.hpp"
// #include "cute/atom/mma_atom.hpp"
// #include "cute/atom/copy_atom.hpp"

#include "fmha_kernel.h"
#include <fmha/kernel_traits.h>
#include <fmha/gemm.h>
#include <fmha/utils.h>
#include <fmha/epilogue.h>

#include "cutlass/cutlass.h"
#include "cutlass/layout/layout.h"
#include <cutlass/array.h>
#include <cutlass/numeric_types.h>
#include "cutlass/numeric_conversion.h"
#include <cutlass/arch/mma.h>
#include "cutlass/gemm/warp/default_mma_tensor_op.h"
#include "cutlass/gemm/warp/mma_tensor_op_tile_iterator.h"
#include "cutlass/gemm/threadblock/default_mma_core.h"
#include "cutlass/gemm/threadblock/default_mma_core_sm75.h"
#include "cutlass/gemm/threadblock/default_mma_core_sm80.h"
#include "cutlass/epilogue/warp/fragment_iterator_tensor_op.h"
#include "cutlass/epilogue/warp/tile_iterator_tensor_op.h"
#include "cutlass/epilogue/threadblock/default_thread_map_tensor_op.h"
#include "cutlass/epilogue/threadblock/default_epilogue_tensor_op.h"
#include "cutlass/epilogue/threadblock/predicated_tile_iterator.h"

namespace fmha {

using namespace cute;

////////////////////////////////////////////////////////////////////////////////////////////////////

// template<typename Kernel_traits>
// struct Gemm_Q_K_base {
//     using Smem_O = fmha::FMHAEpilogue<typename Kernel_traits::MmaCorePV>;
//     using WarpMma = typename Kernel_traits::MmaCoreQK::MmaTensorOp;

//     // The description of the CTA tile for the 1st batched GEMM.
//     using Cta_tile_p = typename Kernel_traits::Cta_tile_p;

//     static constexpr size_t SMEM_BYTES_SOFTMAX = Cta_tile_p::M * Cta_tile_p::WARPS_N * sizeof(float) * 2;

//     __device__ inline Gemm_Q_K_base(char * smem_ptr_q, char * smem_ptr_k)
//         : smem_q_ptr(smem_ptr_q)
//         , smem_k_ptr(smem_ptr_k) {

//     }

//     __device__ inline void load_q(int byte_offset=0) {
//         typename WarpMma::LayoutA layout_A = WarpMma::LayoutA::packed({Cta_tile_p::M, Cta_tile_p::K});
//         // typename WarpMma::IteratorA iter_A({reinterpret_cast<typename WarpMma::ElementA *>(smem_q_ptr + byte_offset), layout_A}, threadIdx.x % 32);
//         // iter_A.load(frag_q[0]);
//     }


//     __device__ inline void reload_q(int byte_offset=0) {
//         typename WarpMma::LayoutA layout_A = WarpMma::LayoutA::packed({Cta_tile_p::M, Cta_tile_p::K});
//         // typename WarpMma::IteratorA iter_A({reinterpret_cast<typename WarpMma::ElementA *>(smem_q_ptr + byte_offset), layout_A}, threadIdx.x % 32);
//         // iter_A.load(frag_q[0]);
//     }

//     typename WarpMma::FragmentA frag_q[2];
//     char *smem_q_ptr;
//     char *smem_k_ptr;
// };

// template<typename Kernel_traits, bool K_in_regs>
// struct Gemm_Q_K : public Gemm_Q_K_base<Kernel_traits> {

//     using Base = Gemm_Q_K_base<Kernel_traits>;
//     using Cta_tile_p = typename Base::Cta_tile_p;
//     using Smem_O = typename Base::Smem_O;
//     using WarpMma = typename Base::WarpMma;

//     static constexpr int kIterations = WarpMma::Shape::kK / WarpMma::InstructionShape::kK;

//     static constexpr bool SHARE_SMEM_FOR_K_AND_V = Kernel_traits::SHARE_SMEM_FOR_K_AND_V;
//     // If V is stored in shared memory, we can't load K using the same shared memory.
//     static_assert(Kernel_traits::V_IN_REGS);

//     static constexpr size_t SMEM_OFFSET_O = Kernel_traits::BYTES_PER_SMEM_Q;
//     static constexpr size_t SMEM_OFFSET_SOFTMAX = SMEM_OFFSET_O + sizeof(typename Smem_O::SharedStorage);
//     static constexpr size_t SMEM_OFFSET_V = Kernel_traits::BYTES_PER_SMEM_Q + (SHARE_SMEM_FOR_K_AND_V ? 0 : Kernel_traits::BYTES_PER_SMEM_K);

//     // Q | K / V
//     //   | O | SOFTMAX
//     static constexpr size_t SMEM_BYTES = Kernel_traits::BYTES_PER_SMEM_Q
//         + std::max((size_t)(SHARE_SMEM_FOR_K_AND_V ? 1 : 2) * Kernel_traits::BYTES_PER_SMEM_K,
//                    sizeof(typename Smem_O::SharedStorage) + Base::SMEM_BYTES_SOFTMAX);

//     __device__ inline Gemm_Q_K(char * smem_)
//         : Base(smem_, smem_ + Kernel_traits::BYTES_PER_SMEM_Q) {
//     }

//     __device__ inline void load_k(){
//         typename WarpMma::LayoutB layout_B = WarpMma::LayoutB::packed({Cta_tile_p::K, Cta_tile_p::N});
//         typename WarpMma::IteratorB iter_B({reinterpret_cast<typename WarpMma::ElementB *>(Base::smem_k_ptr), layout_B}, threadIdx.x % 32);
//         const int warp_idx = threadIdx.x / 32;
//         iter_B.add_tile_offset({0, warp_idx});
//         #pragma unroll
//         for( int ki = 0; ki < kIterations; ++ki ) {
//             iter_B.load(frag_k[ki]);
//             ++iter_B;
//         }
//     }

//     __device__ inline void operator()(WarpMma warp_mma, typename WarpMma::FragmentC &acc_p, int byte_offset_q=0){
//         typename WarpMma::LayoutA layout_A = WarpMma::LayoutA::packed({Base::Cta_tile_p::M, Base::Cta_tile_p::K});
//         // typename WarpMma::IteratorA iter_A({reinterpret_cast<typename WarpMma::ElementB *>(Base::smem_q_ptr + byte_offset_q), layout_A}, threadIdx.x % 32);
//         // ++iter_A;
//         // Do this part of P^T = (Q * K^T)^T.
//         #pragma unroll
//         for( int ki = 0; ki < kIterations; ++ki ) {
//             // Trigger the load from shared memory for the next series of Q values.
//             // if (ki + 1 < kIterations) { iter_A.load(Base::frag_q[(ki + 1) % 2]); ++iter_A; }
//             // Do the math for the values already in registers.
//             warp_mma(acc_p, Base::frag_q[ki % 2], frag_k[ki], acc_p);
//         }
//     }

//     __device__ inline void reload_k(){
//         // Noop.
//     }

//     typename WarpMma::FragmentB frag_k[kIterations];
// };


// template<typename Kernel_traits>
// struct Gemm_Q_K<Kernel_traits, false> : public Gemm_Q_K_base<Kernel_traits> {
//     using Base = Gemm_Q_K_base<Kernel_traits>;
//     using Cta_tile_p = typename Base::Cta_tile_p;
//     using Smem_O = typename Base::Smem_O;
//     using WarpMma = typename Base::WarpMma;

//     static constexpr bool SHARE_SMEM_FOR_K_AND_V = Kernel_traits::SHARE_SMEM_FOR_K_AND_V;
//     static constexpr bool V_IN_REGS = Kernel_traits::V_IN_REGS;
//     static_assert(V_IN_REGS || !SHARE_SMEM_FOR_K_AND_V);

//     static constexpr size_t SMEM_OFFSET_V = Kernel_traits::BYTES_PER_SMEM_Q + (SHARE_SMEM_FOR_K_AND_V ? 0 : Kernel_traits::BYTES_PER_SMEM_K);
//     static constexpr size_t SMEM_OFFSET_O = SMEM_OFFSET_V + Kernel_traits::BYTES_PER_SMEM_V;
//     static constexpr size_t SMEM_OFFSET_SOFTMAX = SMEM_OFFSET_O + sizeof(typename Smem_O::SharedStorage);

//     // If V_IN_REGS and SHARE_SMEM_FOR_K_AND_V:      Q | K/V | O | SOFTMAX
//     // If !V_IN_REGS (then !SHARE_SMEM_FOR_K_AND_V): Q | K   | V | O | SOFTMAX
//     static constexpr size_t SMEM_BYTES = Kernel_traits::BYTES_PER_SMEM_Q
//         + (SHARE_SMEM_FOR_K_AND_V ? 1 : 2) * Kernel_traits::BYTES_PER_SMEM_K
//         + sizeof(typename Smem_O::SharedStorage) + Base::SMEM_BYTES_SOFTMAX;

//     __device__ inline Gemm_Q_K(char * smem_)
//         : Base(smem_, smem_ + Kernel_traits::BYTES_PER_SMEM_Q) {
//     }

//     __device__ inline void load_k(){
//         typename WarpMma::LayoutB layout_B = WarpMma::LayoutB::packed({Cta_tile_p::K, Cta_tile_p::N});
//         typename WarpMma::IteratorB iter_B({reinterpret_cast<typename WarpMma::ElementB *>(Base::smem_k_ptr), layout_B}, threadIdx.x % 32);
//         const int warp_idx = threadIdx.x / 32;
//         iter_B.add_tile_offset({0, warp_idx});
//         iter_B.load(frag_k[0]);
//     }

//     __device__ inline void operator()(WarpMma warp_mma, typename WarpMma::FragmentC &acc_p, int byte_offset_q=0){
//         typename WarpMma::LayoutA layout_A = WarpMma::LayoutA::packed({Base::Cta_tile_p::M, Base::Cta_tile_p::K});
//         typename WarpMma::IteratorA iter_A({reinterpret_cast<typename WarpMma::ElementA *>(Base::smem_q_ptr + byte_offset_q), layout_A}, threadIdx.x % 32);
//         ++iter_A;
//         typename WarpMma::LayoutB layout_B = WarpMma::LayoutB::packed({Cta_tile_p::K, Cta_tile_p::N});
//         typename WarpMma::IteratorB iter_B({reinterpret_cast<typename WarpMma::ElementB *>(Base::smem_k_ptr), layout_B}, threadIdx.x % 32);
//         const int warp_idx = threadIdx.x / 32;
//         iter_B.add_tile_offset({0, warp_idx});
//         ++iter_B;

//         // Do this part of P^T = (Q * K^T)^T.
//         constexpr int kIterations = WarpMma::Shape::kK / WarpMma::InstructionShape::kK;
//         #pragma unroll
//         for( int ki = 0; ki < kIterations; ++ki ) {
//             // Trigger the load from shared memory for the next series of Q values.
//             if (ki + 1 < kIterations) {
//                 iter_A.load(Base::frag_q[(ki + 1) % 2]); ++iter_A;
//                 iter_B.load(frag_k[(ki + 1) % 2]); ++iter_B;
//             }
//             // Do the math for the values already in registers.
//             warp_mma(acc_p, Base::frag_q[ki % 2], frag_k[ki % 2], acc_p);
//         }
//     }
//     __device__ inline void reload_k(){
//         typename WarpMma::LayoutB layout_B = WarpMma::LayoutB::packed({Cta_tile_p::K, Cta_tile_p::N});
//         typename WarpMma::IteratorB iter_B({reinterpret_cast<typename WarpMma::ElementB *>(Base::smem_k_ptr), layout_B}, threadIdx.x % 32);
//         const int warp_idx = threadIdx.x / 32;
//         iter_B.add_tile_offset({0, warp_idx});
//         iter_B.load(frag_k[0]);
//     }

//     typename WarpMma::FragmentB frag_k[2];
// };

// template<typename Kernel_traits>
// constexpr size_t get_dynamic_smem_size(){
//     return Gemm_Q_K<Kernel_traits, Kernel_traits::K_IN_REGS>::SMEM_BYTES;
// }

template<typename Kernel_traits, bool Is_dropout, bool Is_causal, bool Return_softmax, bool Is_first, bool Is_last, typename Params, typename Prng>
inline __device__ void device_1xN_(const Params &params, const int bidb, const int bidh, int begin, int steps, Prng &ph0, Prng &ph1, const int loop_step_idx) {

    // The description of the CTA tile for the 1st batched GEMM.
    using Cta_tile_p = typename Kernel_traits::Cta_tile_p;
    // The description of the CTA tile for the 2nd batched GEMM.
    using Cta_tile_o = typename Kernel_traits::Cta_tile_o;

    // The MMA tile for the 1st GEMM.
    using Mma_tile_p = fmha::Hmma_tile<Cta_tile_p>;
    // The MMA tile for the 2nd GEMM.
    using Mma_tile_o = fmha::Hmma_tile<Cta_tile_o>;

    using InstructionShape = typename Kernel_traits::MmaInstructionShape;
    using Element = typename Kernel_traits::Element;
    using ElementAccum = typename Kernel_traits::ElementAccum;

    using ThreadblockShapeQK = typename Kernel_traits::ThreadblockShapeQK;
    using LayoutQ = typename Kernel_traits::LayoutQ;
    using LayoutK = typename Kernel_traits::LayoutK;
    using LayoutP = typename Kernel_traits::LayoutP;
    using MmaCoreQK = typename Kernel_traits::MmaCoreQK;
    using WarpMmaQK = typename MmaCoreQK::MmaTensorOp;
    using SmemLayoutQ = typename MmaCoreQK::SmemLayoutA;
    using SmemLayoutK = typename MmaCoreQK::SmemLayoutB;
    using SmemIteratorQ = typename MmaCoreQK::SmemIteratorA;
    using SmemIteratorK = typename MmaCoreQK::SmemIteratorB;

    using ThreadblockShapePV = typename Kernel_traits::ThreadblockShapePV;
    using LayoutV = typename Kernel_traits::LayoutV;
    using LayoutO = typename Kernel_traits::LayoutO;
    using MmaCorePV = typename Kernel_traits::MmaCorePV;
    using WarpMmaPV = typename MmaCorePV::MmaTensorOp;
    using WarpIteratorV = typename WarpMmaPV::IteratorB;
    using SmemLayoutV = typename MmaCorePV::SmemLayoutB;
    using SmemLayoutVTransposed = typename MmaCorePV::SmemLayoutBTransposed;
    using SmemIteratorV = typename MmaCorePV::SmemIteratorB;
    // using SmemIteratorV = typename MmaCoreQK::SmemIteratorB;
    constexpr int kIterationsPV = WarpMmaPV::Shape::kK / WarpMmaPV::InstructionShape::kK;

    // // The global memory tile to load Q.
    // // Copy from mma_piplined_testbed.h
    // using GmemIteratorQ = typename Kernel_traits::GmemIteratorQ;
    // // The global memory tile to load K.
    // using GmemIteratorK = typename Kernel_traits::GmemIteratorK;
    // // The global memory tile to load V.
    // using GmemIteratorV = typename Kernel_traits::GmemIteratorV;
    // // The global memory tile to store O.
    // using GmemIteratorO = typename fmha::FMHAEpilogue<MmaCorePV>::GmemIterator;
    // using GmemIteratorOAccum = typename fmha::FMHAEpilogue<MmaCorePV>::GmemIteratorAccum;

    using Gmem_tile_s = typename Kernel_traits::Gmem_tile_s;

    using Gmem_softmax_sum = typename Kernel_traits::Gmem_softmax_sum;

    using Smem_softmax_lse = typename Kernel_traits::Smem_softmax_lse;

    // using Gemm1 = Gemm_Q_K<Kernel_traits, Kernel_traits::K_IN_REGS>;

    using Softmax = fmha::Softmax<Cta_tile_p, Kernel_traits>;

    // Shared memory.
    extern __shared__ char smem_[];

    // The thread index.
    const int tidx = threadIdx.x;

    const BlockInfoPadded<Kernel_traits::THREADS> binfo(params, bidb, bidh, tidx);
    if( binfo.stop_early(loop_step_idx * Cta_tile_p::N) ) return;

    // Gemm1 gemm_q_k(smem_);
    // Allocate the global memory tile loader for S.
    Gmem_tile_s gmem_s(params, binfo, tidx);
    Gmem_softmax_sum gmem_softmax_lse(params.softmax_lse_ptr, params, tidx);

    // Wind gmem tiles to the correct position.
    static_assert(Cta_tile_p::N % Cta_tile_p::M == 0);
    const int begin_og = begin;
    begin = Is_causal ? std::max(begin, loop_step_idx * Cta_tile_p::N / Cta_tile_p::M) : begin;
    const int steps_og = steps;
    steps -= begin - begin_og;
    if (Return_softmax) { gmem_s.move(begin); }
    gmem_softmax_lse.move(begin);

    fmha::Mask<Cta_tile_p, Is_causal> mask(binfo, tidx, loop_step_idx);

    // The base pointer of smem_v;
    // char *smem_v_addr = &smem_[Gemm1::SMEM_OFFSET_V];

    // // Allocate the shared memory tile loader for V. We use the same as K so be careful!!!

    // SmemLayoutQ layout_Q = SmemLayoutQ::packed({ThreadblockShapeQK::kM, ThreadblockShapeQK::kK});
    // // SmemIteratorQ smem_q({reinterpret_cast<Element *>(smem_), layout_Q}, tidx);
    // SmemLayoutK layout_K = SmemLayoutK::packed({ThreadblockShapeQK::kK, ThreadblockShapeQK::kN});
    // SmemIteratorK smem_k({reinterpret_cast<Element *>(smem_ + Kernel_traits::BYTES_PER_SMEM_Q), layout_K}, tidx);
    // SmemLayoutV layout_V = SmemLayoutV::packed({ThreadblockShapePV::kK, ThreadblockShapePV::kN});
    // SmemLayoutVTransposed layout_VTransposed = SmemLayoutVTransposed::packed({ThreadblockShapePV::kN, ThreadblockShapePV::kK});
    // // SmemIterator stores to smem and WarpIterator loads from smem
    // // SmemIteratorV smem_v({reinterpret_cast<Element *>(smem_v_addr), layout_V}, tidx);
    // // SmemIteratorK smem_v({reinterpret_cast<Element *>(smem_v_addr), layout_K}, tidx);
    // SmemIteratorV smem_v({reinterpret_cast<Element *>(smem_v_addr), layout_VTransposed}, tidx);
    // WarpIteratorV iter_V({reinterpret_cast<Element *>(smem_v_addr), layout_V}, threadIdx.x % 32);

    // // Allocate the shared memory tile loader for O. We use the same as K so be careful!!!
    // using Smem_O = fmha::FMHAEpilogue<MmaCorePV>;
    // Smem_O smem_o(&smem_[Gemm1::SMEM_OFFSET_O], tidx);

    // // Allocate the global memory tile loader for Q.
    // // cutlass::transform::threadblock::PredicatedTileIterator deals with seqlen not divisible
    // // by 16 in a different way than we want. If the seqlen_q is 36, the first iteration would
    // // load 4 rows and the next two iterations would load 16 rows each. Instead we round the
    // // actual_seqlen_q to be multiple of 16, then change the mask in the last iteration, so
    // // that in this case we would load 16, 16, 4.
    // LayoutQ gmem_layout_Q(params.q_row_stride_in_elts);
    // typename GmemIteratorQ::Params gmem_Q_params(gmem_layout_Q);
    const uint32_t row_offset_q = (binfo.sum_s_q + begin * ThreadblockShapeQK::kM) * params.q_row_stride_in_elts + binfo.bidh * params.q_head_stride_in_elts;
    // const int actual_seqlen_q = binfo.actual_seqlen_q - begin * ThreadblockShapeQK::kM;
    // const int seqlen_q_remainder = actual_seqlen_q % ThreadblockShapeQK::kM;
    // const int extent_q = ((actual_seqlen_q <= ThreadblockShapeQK::kM) || (seqlen_q_remainder == 0)) ? actual_seqlen_q : actual_seqlen_q + ThreadblockShapeQK::kM - seqlen_q_remainder;
    // GmemIteratorQ gmem_q(gmem_Q_params,
    //                      reinterpret_cast<Element *>(params.q_ptr) + row_offset_q,
    //                      {extent_q, params.d},
    //                      tidx);

    // // Allocate the global memory tile loader for K.
    // LayoutK gmem_layout_K(params.k_row_stride_in_elts);
    // typename GmemIteratorK::Params gmem_K_params(gmem_layout_K);
    const uint32_t row_offset_k = (binfo.sum_s_k + loop_step_idx * ThreadblockShapeQK::kN) * params.k_row_stride_in_elts + binfo.bidh * params.k_head_stride_in_elts;
    // const int extent_k = min(binfo.actual_seqlen_k - loop_step_idx * ThreadblockShapeQK::kN, ThreadblockShapeQK::kN);
    // GmemIteratorK gmem_k(gmem_K_params,
    //                      reinterpret_cast<Element *>(params.k_ptr) + row_offset_k,
    //                      {params.d, extent_k},
    //                      tidx);

    // // Allocate the global memory tile loader for V.
    // LayoutV gmem_layout_V(params.v_row_stride_in_elts);
    // typename GmemIteratorV::Params gmem_V_params(gmem_layout_V);
    const uint32_t row_offset_v = (binfo.sum_s_k + loop_step_idx * ThreadblockShapePV::kK) * params.v_row_stride_in_elts + binfo.bidh * params.v_head_stride_in_elts;
    // // extent_v is the same as extent_k
    // GmemIteratorV gmem_v(gmem_V_params,
    //                      reinterpret_cast<Element *>(params.v_ptr) + row_offset_v,
    //                      {extent_k, params.d},
    //                      tidx);

    // // Allocate the global memory tile loader for O.
    // LayoutO gmem_layout_O(params.o_row_stride_in_elts);
    // typename GmemIteratorO::Params gmem_O_params(gmem_layout_O);
    const uint32_t row_offset_o = (binfo.sum_s_q + begin * ThreadblockShapeQK::kM) * params.o_row_stride_in_elts + binfo.bidh * params.o_head_stride_in_elts;
    // GmemIteratorO gmem_o(gmem_O_params,
    //                      reinterpret_cast<Element *>(params.o_ptr) + row_offset_o,
    //                      {actual_seqlen_q, params.d},
    //                      tidx);

    // typename GmemIteratorOAccum::Params gmem_Oaccum_params(gmem_layout_O);
    // GmemIteratorOAccum gmem_o_accum(gmem_Oaccum_params,
    //                                 reinterpret_cast<ElementAccum *>(params.o_tmp_ptr) + row_offset_o,
    //                                 {actual_seqlen_q, params.d},
    //                                 tidx);

    // // Create the object to do the softmax.
    // Softmax softmax(params, &smem_[Gemm1::SMEM_OFFSET_SOFTMAX], tidx);

    // Smem_softmax_lse smem_softmax_lse(reinterpret_cast<float *>(&smem_[Gemm1::SMEM_BYTES]));

    // if (!Is_first) {
    //     if (Return_softmax) { gmem_s.move(loop_step_idx * steps_og); }
    // }

    // if (!Is_first) { __syncthreads(); }

    // // Trigger the loads for V.
    // typename GmemIteratorV::Fragment gmem_frag_v;
    // gmem_frag_v.clear();
    // gmem_v.load(gmem_frag_v);

    // // Trigger the loads for Q.
    // typename GmemIteratorQ::Fragment gmem_frag_q;
    // gmem_frag_q.clear();
    // gmem_q.load(gmem_frag_q);

    // // Trigger the loads for K.
    // typename GmemIteratorK::Fragment gmem_frag_k;
    // gmem_frag_k.clear();
    // gmem_k.load(gmem_frag_k);

    // float p_prev_lse[Mma_tile_p::MMAS_M * 2];
    // if (!Is_first) {
    //     gmem_softmax_lse.load(reinterpret_cast<uint32_t(&)[Mma_tile_p::MMAS_M * 2]>(p_prev_lse));
    // }

    // // Commit the data for Q and V to shared memory.
    // smem_v.store(gmem_frag_v);
    // // smem_q.store(gmem_frag_q);

    // // Commit the data for K to shared memory.
    // if( !Kernel_traits::SHARE_SMEM_FOR_K_AND_V ) {
    //     smem_k.store(gmem_frag_k);
    // }

    // __syncthreads();

    using X = Underscore;

    constexpr int kBlockM = Kernel_traits::kBlockM;
    constexpr int kBlockN = Kernel_traits::kBlockN;
    constexpr int kHeadDim = Kernel_traits::kHeadDim;

    typename Kernel_traits::GmemTiledCopyQKV gmem_tiled_copy_qkv;

    // if (cute::thread0()) { gmem_tiled_copy_qkv.print_all(); }

    // We assume that params.d == kHeadDim for now
    Tensor mQ = make_tensor(make_gmem_ptr(reinterpret_cast<Element *>(params.q_ptr) + row_offset_q),
                            // make_shape(binfo.actual_seqlen_q, params.d),
                            // Need static shape in the k dim here
                            make_shape(binfo.actual_seqlen_q, Int<kHeadDim>{}),
                            make_stride(params.q_row_stride_in_elts, _1{}));
    // if (cute::thread0()) { print(mQ.layout()); printf("\n"); }
    Tensor mK = make_tensor(make_gmem_ptr(reinterpret_cast<Element *>(params.k_ptr) + row_offset_k),
                            make_shape(binfo.actual_seqlen_k, Int<kHeadDim>{}),
                            make_stride(params.k_row_stride_in_elts, _1{}));
    Tensor mV = make_tensor(make_gmem_ptr(reinterpret_cast<Element *>(params.v_ptr) + row_offset_v),
                            make_shape(binfo.actual_seqlen_k, Int<kHeadDim>{}),
                            make_stride(params.v_row_stride_in_elts, _1{}));

    // Tensor gQ = local_tile(mQ, Shape<Int<kBlockM>>{}, make_coord(blockIdx.z));  // (kBlockM, kHeadDim)
    Tensor gQ = local_tile(mQ, Shape<Int<kBlockM>>{}, make_coord(blockIdx.x));  // (kBlockM, kHeadDim)
    // if (cute::thread0()) { print(gQ.layout()); printf("\n"); }
    // Tensor gK = local_tile(mK, Shape<Int<kBlockN>, Int<kHeadDim>>{}, make_coord(_, _0{}));  // (kBlockN, kHeadDim, n)
    Tensor gK = make_tensor(make_gmem_ptr(reinterpret_cast<Element *>(params.k_ptr) + row_offset_k),
                            Shape<Int<kBlockN>, Int<kHeadDim>>{}, make_stride(params.k_row_stride_in_elts, _1{}));
    // if (cute::thread0()) { print(gK.layout()); printf("\n"); }
    // Tensor gV = local_tile(mV, Shape<Int<kBlockN>, Int<kHeadDim>>{}, make_coord(_, _0{}));  // (kBlockN, kHeadDim, n)
    Tensor gV = make_tensor(make_gmem_ptr(reinterpret_cast<Element *>(params.v_ptr) + row_offset_v),
                            Shape<Int<kBlockN>, Int<kHeadDim>>{}, make_stride(params.v_row_stride_in_elts, _1{}));

    auto copy_qkv_thr = gmem_tiled_copy_qkv.get_slice(tidx);
    Tensor tQgQ = copy_qkv_thr.partition_S(gQ);
    // if (cute::thread0()) { print(tQgQ); }
    // Tensor tKgK = copy_q_thr.partition_S(gK);  // (KCPY, KCPY_N, KCPY_K, n)
    Tensor tKgK = copy_qkv_thr.partition_S(gK);  // (KCPY, KCPY_N, KCPY_K)
    // if (cute::thread0()) { print(tKgK.layout()); printf("\n"); }
    // Tensor tVgV = copy_qkv_thr.partition_S(gV);  // (VCPY, VCPY_N, VCPY_K, n)
    Tensor tVgV = copy_qkv_thr.partition_S(gV);  // (VCPY, VCPY_N, VCPY_K)

    Tensor sQ = make_tensor(make_smem_ptr(reinterpret_cast<Element *>(smem_)),
                            typename Kernel_traits::SmemLayoutQ{});
    Tensor tQsQ = copy_qkv_thr.partition_D(sQ);
    // Careful we're using the same smem for sQ and sK | sV
    // Tensor sK = make_tensor(make_smem_ptr(reinterpret_cast<Element *>(smem_)),
    Tensor sK = make_tensor(make_smem_ptr(reinterpret_cast<Element *>(smem_) + kBlockM * kHeadDim),
                            typename Kernel_traits::SmemLayoutK{});
    Tensor tKsK = copy_qkv_thr.partition_D(sK);
    // Tensor sV = make_tensor(make_smem_ptr(reinterpret_cast<Element *>(smem_) + 128 * 64 + 64 * 64), typename Kernel_traits::SmemLayoutV{});
    Tensor sV = make_tensor(sK.data() + kBlockN * kHeadDim, typename Kernel_traits::SmemLayoutV{});
    Tensor tVsV = copy_qkv_thr.partition_D(sV);
    // Tensor sVtransposed = make_tensor(make_smem_ptr(reinterpret_cast<Element *>(smem_) + 128 * 64 + 64 * 64), typename Kernel_traits::SmemLayoutVtransposed{});
    Tensor sVtransposed = make_tensor(sV.data(), typename Kernel_traits::SmemLayoutVtransposed{});
    Tensor sVtransposedNoSwizzle = make_tensor(sV.data(),
                                               typename Kernel_traits::SmemLayoutVtransposedNoSwizzle{});
    // if (cute::thread0()) { print(sVtransposed); }

    typename Kernel_traits::TiledMma tiled_mma;
    auto thr_mma = tiled_mma.get_thread_slice(tidx);
    Tensor tSrQ  = thr_mma.partition_fragment_A(sQ);                           // (MMA,MMA_M,MMA_K)
    // if (cute::thread0()) { print(tSrQ.layout()); }
    Tensor tSrK  = thr_mma.partition_fragment_B(sK);                           // (MMA,MMA_N,MMA_K)
    // if (cute::thread(1, 0)) { print(tSrQ); print(tSrK); }

    CUTE_STATIC_ASSERT_V(size<2>(tSrQ) == size<2>(tSrK));                      // MMA_K

    //
    // Copy Atom retiling
    //

    auto smem_tiled_copy_Q = make_tiled_copy_A(typename Kernel_traits::SmemCopyAtomQ{}, tiled_mma);
    auto smem_thr_copy_Q = smem_tiled_copy_Q.get_thread_slice(tidx);
    Tensor tSsQ           = smem_thr_copy_Q.partition_S(sQ);
    Tensor tSrQ_copy_view = smem_thr_copy_Q.retile_D(tSrQ);
    CUTE_STATIC_ASSERT_V(size<1>(tSsQ) == size<1>(tSrQ_copy_view));            // M

    auto smem_tiled_copy_K = make_tiled_copy_B(typename Kernel_traits::SmemCopyAtomK{}, tiled_mma);
    auto smem_thr_copy_K = smem_tiled_copy_K.get_thread_slice(tidx);
    Tensor tSsK           = smem_thr_copy_K.partition_S(sK);
    Tensor tSrK_copy_view = smem_thr_copy_K.retile_D(tSrK);
    CUTE_STATIC_ASSERT_V(size<1>(tSsK) == size<1>(tSrK_copy_view));            // N

    Tensor acc_o = partition_fragment_C(tiled_mma, Shape<Int<kBlockM>, Int<kHeadDim>>{});  // MMA, MMA_M, MMA_K
    // Tensor tOrV  = thr_mma.partition_fragment_B(sVtransposed);                           // (MMA, MMA_K,MMA_N)
    Tensor tOrV  = thr_mma.partition_fragment_B(sVtransposedNoSwizzle);                           // (MMA, MMA_K,MMA_N)
    // Tensor tOrVt  = thr_mma.partition_fragment_B(sV);                           // (MMA, MMA_N, MMA_K)
    // Layout vt_l = tOrVt.layout();
    // Tensor tOrV = make_tensor(tOrVt.data(),
    //                           make_layout(get<0>(vt_l), get<2>(vt_l), get<1>(vt_l)));
    // if (cute::thread0()) { print(tOrV.layout()); printf("\n"); }
    // if (cute::thread0()) { print(acc_o.layout()); printf("\n"); }
    // // if (cute::thread(1, 0)) { print(tSrQ); print(tSrK); }
    // // if (cute::thread(0, 0)) { print(tSrQ); }

    // if (cute::thread0()) { printf("size1 = %\n", size<1>(tOrVt)); print(tOrVt); print(tOrV); print(acc_o); }
    // if (cute::thread0()) { print(tOrV); print(acc_o); }
    CUTE_STATIC_ASSERT_V(size<1>(tOrV) == size<2>(acc_o));                     // MMA_N

    //
    // Copy Atom retiling
    //

    auto smem_tiled_copy_V = make_tiled_copy_B(typename Kernel_traits::SmemCopyAtomV{}, tiled_mma);
    auto smem_thr_copy_V = smem_tiled_copy_V.get_thread_slice(tidx);
    Tensor tOsV           = smem_thr_copy_V.partition_S(sVtransposed);
    // Tensor tOsV           = smem_thr_copy_V.partition_S(sV);
    // using RegistersSrc = typename SM75_U16x8_LDSM_T::SRegisters;
    // using RegTypeSrc   = typename std::remove_extent<RegistersSrc>::type;
    // constexpr int RegNumSrc = std::extent<RegistersSrc>::value;

    // Tensor rS = recast<RegTypeSrc>(tOsV(_, _, 0));
    // if (cute::thread0()) {
    //     print(sV.layout()); printf("\n");
    //     print(sVtransposed.layout()); printf("\n");
    //     print(tOsV.layout()); printf("\n"); print(tOsV(_, _, 0).layout()); printf("size(rS) = %d, Int<RegNumSrc>{} = %d\n", int(size(rS)), RegNumSrc);
    // }

    Tensor tOrV_copy_view = smem_thr_copy_V.retile_D(tOrV);
    CUTE_STATIC_ASSERT_V(size<1>(tOsV) == size<1>(tOrV_copy_view));            // N
    // if (cute::thread0()) { print(tOsV); print(tOrV_copy_view); }

    // TODO: this might need to change if we change the mma instruction in SM70
    Tensor scores_max = make_tensor<float>(Shape<Int<2 * size<1>(acc_o)>>{});
    Tensor scores_sum = make_fragment_like(scores_max);

    // Prologue
    clear(acc_o);
    // fill(scores_max, -INFINITY);

    // Tensor tQrQ = make_fragment_like(tQgQ);
    // copy(gmem_tiled_copy_qkv, tQgQ, tQrQ);
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

    // copy(smem_tiled_copy_Q, tSsQ, tSrQ_copy_view);
    // __syncthreads();

    // // Copy rmem to smem
    // copy(tKrK, tKsK);
    copy(gmem_tiled_copy_qkv, tKgK, tKsK);
    cute::cp_async_fence();

    int n_block_max = (binfo.actual_seqlen_k + kBlockN - 1) / kBlockN;

    // Seems to help a bit even though it says there's more register spilling
    #pragma unroll 2
    for (int n_block = 0; n_block < n_block_max; ++n_block) {
        Tensor acc_s = partition_fragment_C(tiled_mma, Shape<Int<kBlockM>, Int<kBlockN>>{});  // (MMA=4, MMA_M, MMA_N)
        // if (cute::thread0()) { print(acc_s); }
        CUTE_STATIC_ASSERT_V(size<1>(tSrQ) == size<1>(acc_s));                     // MMA_M
        CUTE_STATIC_ASSERT_V(size<1>(tSrK) == size<2>(acc_s));                     // MMA_N

        clear(acc_s);
        cute::cp_async_wait<0>();
        __syncthreads();
        // if (cute::thread(1, 0)) { print(tKsK); }

        // if (cute::thread0()) { print(gV); }
        if (n_block > 0) {
            tVgV.data() = tVgV.data() + kBlockN * params.v_row_stride_in_elts;
        }
        // Tensor tVrV = make_fragment_like(tVsV);
        // // copy(gmem_tiled_copy_qkv, tVgV(_, _, _, n_block), tVrV);
        // copy(gmem_tiled_copy_qkv, tVgV, tVrV);
        // // if (cute::thread(0, 0)) { print(tVrV); }
        copy(gmem_tiled_copy_qkv, tVgV, tVsV);
        cute::cp_async_fence();

        copy(smem_tiled_copy_Q, tSsQ(_, _, _0{}), tSrQ_copy_view(_, _, _0{}));
        copy(smem_tiled_copy_K, tSsK(_, _, _0{}), tSrK_copy_view(_, _, _0{}));

        // if (cute::thread(1, 0)) { print(tSsQ); print(tSsK); }
        // if (cute::thread(0, 0)) { print(tSrQ); print(tSrK); print(acc_s); }

        #pragma unroll
        for (int i = 0; i < size<2>(tSrQ); ++i) {
        // for (int i = 0; i < 1; ++i) {
            // if (cute::thread(0, 0)) { print(tSrQ(_, _, i)); print(tSrK(_, _, i)); }
            // if (cute::thread(0, 0)) { print(tSrQ_copy_view(_, _, i)); print(tSrK_copy_view(_, _, i)); }
            // __syncthreads();
            // if (cute::thread(1, 0)) { print(tSrQ_copy_view(_, _, i)); print(tSrK_copy_view(_, _, i)); }
            // __syncthreads();
            // if (cute::thread(2, 0)) { print(tSrQ_copy_view(_, _, i)); print(tSrK_copy_view(_, _, i)); }
            // __syncthreads();
            // if (cute::thread(3, 0)) { print(tSrQ_copy_view(_, _, i)); print(tSrK_copy_view(_, _, i)); }
            if (i < size<2>(tSrQ) - 1) {
                copy(smem_tiled_copy_Q, tSsQ(_, _, i + 1), tSrQ_copy_view(_, _, i + 1));
                copy(smem_tiled_copy_K, tSsK(_, _, i + 1), tSrK_copy_view(_, _, i + 1));
            }
            cute::gemm(tiled_mma, tSrQ(_, _, i), tSrK(_, _, i), acc_s);
        }

        // if (cute::thread0() && n_block == 0) { print(acc_s.layout()); printf("\n"); }

        // Reshape acc_s from (MMA=4, MMA_M, MMA_N) to (col=(2, MMA_M), row=(2, MMA_N))
        Layout s_l = logical_divide(acc_s.layout(), Shape<_2>{});  // ((2, 2), MMA_M, MMA_N)
        Tensor scores = make_tensor(acc_s.data(),
                                    make_layout(make_layout(get<0, 1>(s_l), get<1>(s_l)),
                                                make_layout(get<0, 0>(s_l), get<2>(s_l))));
        if (cute::thread(0, 0)) { print(scores); }

        // // Copy rmem to smem
        // copy(tVrV, tVsV);

        if (n_block == 0) {
            fmha::template reduce_max</*zero_init=*/true>(scores, scores_max);
        } else {
            Tensor scores_max_prev = make_fragment_like(scores_max);
            copy(scores_max, scores_max_prev);
            fmha::template reduce_max</*zero_init=*/false>(scores, scores_max);
            // Reshape acc_o from (MMA=4, MMA_M, MMA_K) to (col=(2, MMA_M), row=(2, MMA_K))
            Layout o_l = logical_divide(acc_o.layout(), Shape<_2>{});  // ((2, 2), MMA_M, MMA_N)
            Tensor acc_o_reshaped = make_tensor(acc_o.data(),
                                                make_layout(make_layout(get<0, 1>(o_l), get<1>(o_l)),
                                                            make_layout(get<0, 0>(o_l), get<2>(o_l))));
            #pragma unroll
            for (int mi = 0; mi < size(scores_max); ++mi) {
                // float scores_scale = __expf((scores_max_prev(mi) - scores_max(mi)) * params.scale_bmm1);
                float scores_scale = exp2f((scores_max_prev(mi) - scores_max(mi)) * params.scale_log2);
                scores_sum(mi) *= scores_scale;
                #pragma unroll
                for (int ni = 0; ni < size<1>(acc_o_reshaped); ++ni) {
                    acc_o_reshaped(mi, ni) *= scores_scale;
                }
            }
            // if (cute::thread(0, 0)) { print(scores_max_prev); print(scores_sum); }
        }
        // if (cute::thread(0, 0)) { print(scores_max); }
        // Compute the exponential value.
        // fmha::scale_apply_exp(scores, scores_max, params.scale_bmm1);
        fmha::scale_apply_exp2(scores, scores_max, params.scale_log2);
        // if (cute::thread(1, 0)) { print(scores); }

        Tensor scores_sum_prev = make_fragment_like(scores_sum);
        if (n_block == 0) {
            fmha::reduce_sum(scores, scores_sum);
        } else {
            copy(scores_sum, scores_sum_prev);
            fmha::reduce_sum(scores, scores_sum);
            #pragma unroll
            for (int mi = 0; mi < size(scores_sum); ++mi) {
                scores_sum(mi) += scores_sum_prev(mi);
            }
        }

        // if (cute::thread(0, 0)) { print(scores_sum); }

        // Convert acc_s from fp32 to fp16
        cutlass::NumericArrayConverter<Element, ElementAccum, size(scores), cutlass::FloatRoundStyle::round_to_nearest> convert_p;
        // auto frag_p = convert_p(reinterpret_cast<const cutlass::Array<float, size(scores)>(&)>(scores));
        auto frag_p = convert_p(*reinterpret_cast<const cutlass::Array<float, size(scores)>*>(scores.data()));
        Tensor rP = make_tensor(make_rmem_ptr<Element>(&frag_p), scores.layout());
        // for (int i = 0; i < size(acc_s); ++i) {
        //     rP(i) = acc_s(i);
        // }
        // if (cute::thread(1, 0)) { print(rP); }
        // Reshape rP from (col=(2, MMA_M), row=(2, MMA_N)) to ((2, 2, 2), MMA_M, MMA_N / 2)
        Layout p_l = logical_divide(rP.layout(), Shape<X, Shape<X, _2>>{});  // ((2, MMA_M), (2, (2, MMA_N / 2)))
        Tensor tOrP = make_tensor(rP.data(),
                                  make_layout(make_layout(get<1, 0>(p_l), get<0, 0>(p_l), get<1, 1, 0>(p_l)),
                                              get<0, 1>(p_l),
                                              get<1, 1, 1>(p_l)));
        if (Is_dropout) {
            // if (cute::thread0()) {print(tOrP);}
            fmha::apply_dropout(tOrP, ph0, params.p_dropout_in_uint8_t);
            // fmha::apply_dropout(tOrP, ph0, params.p_dropout_in_uint16_t);
            // auto seeds = at::cuda::philox::unpack(params.philox_args);
            // fmha::apply_dropout_philox(tOrP, params.p_dropout_in_uint16_t,
            //                            std::get<0>(seeds), std::get<1>(seeds));
            // if (cute::thread0()) {print(tOrP);}
        }
        // if (cute::thread0() && n_block == 0) { print(tOrP.layout()); printf("\n"); }

        cute::cp_async_wait<0>();
        __syncthreads();
        // if (cute::thread(0, 0)) { print(tVsV); }
        // Tensor sVNoSwizzle = make_tensor(make_smem_ptr(reinterpret_cast<Element *>(smem_) + 128 * 64 + 64 * 64), typename Kernel_traits::SmemLayoutVNoSwizzle{});
        // if (cute::thread0()) { print(sVNoSwizzle); }

        if (n_block < n_block_max - 1) {
            // Advance gK
            tKgK.data() = tKgK.data() + kBlockN * params.k_row_stride_in_elts;
            // copy(gmem_tiled_copy_qkv, tKgK, tKrK);
            copy(gmem_tiled_copy_qkv, tKgK, tKsK);
            cute::cp_async_fence();
            // copy(gmem_tiled_copy_qkv, tKgK(_, _, _, n_block + 1), tKrK);
        }

        CUTE_STATIC_ASSERT_V(size<1>(tOrP) == size<1>(acc_o));                     // MMA_M
        CUTE_STATIC_ASSERT_V(size<2>(tOrP) == size<2>(tOrV));                     // MMA_K
        copy(smem_tiled_copy_V, tOsV(_, _, 0), tOrV_copy_view(_, _, 0));

        #pragma unroll
        for (int i = 0; i < size<2>(tOrP); ++i) {
            if (i < size<2>(tOrP) - 1) { copy(smem_tiled_copy_V, tOsV(_, _, i + 1), tOrV_copy_view(_, _, i + 1)); }
            cute::gemm(tiled_mma, tOrP(_, _, i), tOrV(_, _, i), acc_o);
        }

        // // if (cute::thread0()) { print(acc_o); }
        // // Copy rmem to smem
        // if (n_block < n_block_max - 1) {
        //     copy(tKrK, tKsK);
        // }

    }

    __syncthreads();

    // Epilogue

    // Reshape acc_o from (MMA=4, MMA_M, MMA_K) to (col=(2, MMA_M), row=(2, MMA_K))
    Layout o_l = logical_divide(acc_o.layout(), Shape<_2>{});  // ((2, 2), MMA_M, MMA_N)
    Tensor acc_o_reshaped = make_tensor(acc_o.data(),
                                        make_layout(make_layout(get<0, 1>(o_l), get<1>(o_l)),
                                                    make_layout(get<0, 0>(o_l), get<2>(o_l))));
    #pragma unroll
    for (int mi = 0; mi < size<0>(acc_o_reshaped); ++mi) {
        float sum = scores_sum(mi);
        float inv_sum = (sum == 0.f || sum != sum) ? 1.f : 1.f / sum;
        #pragma unroll
        for (int ni = 0; ni < size<1>(acc_o_reshaped); ++ni) {
            acc_o_reshaped(mi, ni) *= inv_sum;
        }
    }

    // Convert acc_o from fp32 to fp16
    cutlass::NumericArrayConverter<Element, ElementAccum, size(acc_o), cutlass::FloatRoundStyle::round_to_nearest> convert_o;
    auto frag_o = convert_o(*reinterpret_cast<const cutlass::Array<float, size(acc_o)>*>(acc_o.data()));
    Tensor rO = make_tensor(make_rmem_ptr<Element>(&frag_o), shape(acc_o), stride(acc_o));

    Tensor sO = make_tensor(make_smem_ptr(reinterpret_cast<Element *>(smem_)), typename Kernel_traits::SmemLayoutO{});              // (SMEM_M,SMEM_N)

    // Partition sO to match the accumulator partitioning
    auto tOsmem = make_tiled_copy_C(typename Kernel_traits::CopyAtomOR2S{}, tiled_mma).get_thread_slice(tidx);
    Tensor tOaO = tOsmem.retile_S(rO);                                          // ((Atom,AtomNum), MMA_M, MMA_N)
    Tensor tOsmemsO = tOsmem.partition_D(sO);                                                 // ((Atom,AtomNum),PIPE_M,PIPE_N)

    copy(tOsmem, tOaO, tOsmemsO);

    __syncthreads();

    Tensor mO = make_tensor(make_gmem_ptr(reinterpret_cast<Element *>(params.o_ptr) + row_offset_o),
                            make_shape(binfo.actual_seqlen_q, Int<kHeadDim>{}),
                            make_stride(params.o_row_stride_in_elts, _1{}));
    // Tensor gO = local_tile(mO, Shape<Int<kBlockM>>{}, make_coord(blockIdx.z));  // (kBlockM, kHeadDim)
    Tensor gO = local_tile(mO, Shape<Int<kBlockM>>{}, make_coord(blockIdx.x));  // (kBlockM, kHeadDim)
    auto tO = typename Kernel_traits::GmemTiledCopyO{}.get_thread_slice(tidx);
    Tensor tOsO = tO.partition_S(sO);                                   //               ((Atom,AtomNum),ATOM_M,ATOM_N)
    Tensor tDgO = tO.partition_D(gO);

    Tensor tOrO = make_tensor<Element>(shape(tDgO));
    copy(tO, tOsO, tOrO);

    copy(typename Kernel_traits::CopyAtomOR2G{}, tOrO, tDgO);

    // // Load the fragments for Q.
    // gemm_q_k.load_q();

    // // Load the fragments for V. We keep the data in registers during the entire
    // // kernel. copied from mma_pipelined.h
    // const int warp_idx = threadIdx.x / 32;
    // iter_V.add_tile_offset({kIterationsPV * warp_idx, 0});
    // typename WarpIteratorV::Fragment frag_v[kIterationsPV];
    // static_assert(WarpIteratorV::Fragment::kStorageElements == 4 * Mma_tile_o::MMAS_N || WarpIteratorV::Fragment::kStorageElements == 2 * Mma_tile_o::MMAS_N );
    // #pragma unroll
    // for( int ki = 0; ki < kIterationsPV; ++ki ) {
    //     if ((threadIdx.x == 0) && (blockIdx.x == 0) && (blockIdx.y == 0) && (blockIdx.z == 0)) {
    //         printf("ki = %d\n", ki);
    //     }
    //     iter_V.load(frag_v[ki]);
    //     ++iter_V;
    // }

    // // Commit the data for K to shared memory if it has not been done already.
    // if( Kernel_traits::SHARE_SMEM_FOR_K_AND_V ) {
    //     // Make sure we are done loading the fragments for K.
    //     __syncthreads();

    //     // Commit the data to shared memory for K.
    //     smem_k.store(gmem_frag_k);

    //     // Make sure the data is in shared memory.
    //     __syncthreads();
    // }

    // // return;

    // // Load the fragments for K.
    // gemm_q_k.load_k();

    // return;
    // // Load over the entire sequence length.
    // for( int l = 0; l < steps; l++ ) {
    //     if((begin + l) * Cta_tile_p::M >= binfo.actual_seqlen_q) break;

    //     // Declare the accum for the 1st gemm.
    //     WarpMmaQK mma_qk;
    //     typename WarpMmaQK::FragmentC acc_p;
    //     acc_p.clear();

    //     // Do this part of P = Q * K^T.
    //     gemm_q_k(mma_qk, acc_p);

    //     typename Smem_O::OutputFragment out[Smem_O::kIterationsStore];
    //     static_assert(GmemIteratorOAccum::kIterations == Smem_O::kIterationsStore);
    //     static_assert(GmemIteratorO::kIterations == Smem_O::kIterationsStore);
    //     if (!Is_first) {
    //         #pragma unroll
    //         for (int iter = 0; iter < GmemIteratorOAccum::kIterations; ++iter) {
    //             gmem_o_accum.load(out[iter]);
    //             gmem_o_accum.move();
    //         }
    //     }

    //     // Trigger the load for the next Q values.
    //     if( l < steps - 1) {
    //         ++gmem_q;
    //         // If actual_seqlen_q is not a multiple of 16, we change the mask in the last iteration
    //         // to load the "residue" tile.
    //         if ((l + 1 == steps - 1) && (actual_seqlen_q % ThreadblockShapeQK::kM != 0)) {
    //             // TODO: this probably only works for head_dim = 64 and head_dim = 128, which is
    //             // what we have right now. Maybe for head_dim = 32 or 96, this could be different.
    //             const int row_idx = tidx / (GmemIteratorQ::Shape::kColumn / GmemIteratorQ::Fragment::kElements);
    //             if (row_idx >= actual_seqlen_q - (l + 1) * ThreadblockShapeQK::kM) {
    //                 gmem_q.clear_mask();
    //             }
    //         }
    //         gmem_q.load(gmem_frag_q);
    //     }

    //     // Load the mask for that iteration.
    //     mask.load(begin + l);

    //     // Convert from the accumulator type to FP32 for Softmax.
    //     softmax.unpack_noscale(acc_p);

    //     // Apply the mask.
    //     softmax.apply_mask(mask);

    //     if( Kernel_traits::SHARE_SMEM_FOR_K_AND_V && l == 0 ) {
    //         // if we share K and V, it could be that V was not fully read yet but we write into smem for reduction
    //         __syncthreads();
    //     }

    //     // Compute the max.
    //     float p_max[Mma_tile_p::MMAS_M * 2];
    //     if (!Is_first) {
    //         smem_softmax_lse.store_pair(p_prev_lse);
    //         for (int mi = 0; mi < Mma_tile_p::MMAS_M * 2; mi++) { p_max[mi] = p_prev_lse[mi] / params.scale_bmm1; }
    //     }

    //     // Trigger the load for the next LSE values.
    //     if( l < steps - 1) {
    //         if (!Is_first) {
    //             gmem_softmax_lse.load_next(reinterpret_cast<uint32_t(&)[Mma_tile_p::MMAS_M * 2]>(p_prev_lse));
    //         }
    //     }

    //     softmax.template reduce_max</*zero_init=*/Is_first>(p_max);

    //     // Compute the exponential value.
    //     softmax.scale_apply_exp(p_max, params.scale_bmm1);

    //     // We don't finalize the sum reduction here, as that would incur an extra sync_threads().
    //     // Instead, we reduce the sum from each warp, write to smem, then wait until the sync_threads()
    //     // from storing acc_o. Then we read the sum of each warp from smem and finalize the reduction.
    //     // As a consequence, we don't scale acc_p by the inverse sum, we scale the output by the inverse sum.
    //     // Compute the sum.
    //     float p_sum[Mma_tile_p::MMAS_M * 2];
    //     // softmax.reduce_sum(p_sum);
    //     softmax.reduce_sum_before_sync_(p_sum);

    //     constexpr bool encode_dropout_in_sign_bit = Return_softmax;
    //     if (Is_dropout) {
    //         softmax.template apply_dropout_16bits<encode_dropout_in_sign_bit>(ph0, ph1, params.p_dropout_in_uint16_t);
    //     }

    //     static_assert(Mma_tile_o::MMAS_M == Mma_tile_p::MMAS_M);
    //     static_assert(Mma_tile_o::MMAS_K == Mma_tile_p::MMAS_N);
    //     softmax.pack_noconvert(acc_p);
    //     cutlass::NumericArrayConverter<Element, ElementAccum, decltype(acc_p)::kElements, cutlass::FloatRoundStyle::round_to_nearest> convert_p;
    //     auto frag_p = convert_p(acc_p);

    //     if (Return_softmax) {
    //         gmem_s.store(reinterpret_cast<const cutlass::Array<Element, 8>(&)[Mma_tile_o::MMAS_K][Mma_tile_o::MMAS_M]>(frag_p), mask);
    //         gmem_s.move();
    //     }

    //     // Commit the values for Q into shared memory.
    //     // if (l < steps - 1) { smem_q.store(gmem_frag_q); }

    //     if (Is_dropout && encode_dropout_in_sign_bit) {
    //         cutlass::epilogue::thread::ReLu<decltype(frag_p)> relu;
    //         frag_p = relu(frag_p);
    //     }

    //     // Declare the accum for the 2nd gemm.
    //     WarpMmaPV mma_pv;
    //     typename WarpMmaPV::FragmentC acc_o;
    //     static_assert(WarpMmaPV::FragmentC::kElements == Mma_tile_o::MMAS_M * Mma_tile_o::MMAS_N * 8);
    //     acc_o.clear();

    //     // For some reason, WarpMmaPV::FragmentA has length K * N * (8|4) instead of just N * (8|4).
    //     // We have to first cast frag_p to be array of k x (N * (8|4)), then cast each row to be
    //     // an array of WarpMmaPV::FragmentA (which is what mma_pv expects).
    //     static_assert(decltype(frag_p)::kElements == kIterationsPV * Mma_tile_o::MMAS_M * WarpMmaPV::FragmentA::kElements);
    //     const auto frag_p_reshaped = reinterpret_cast<const cutlass::Array<Element, WarpMmaPV::FragmentA::kElements> (&)[kIterationsPV]>(frag_p);
    //     #pragma unroll
    //     for( int ki = 0; ki < kIterationsPV; ++ki ) {
    //         mma_pv(acc_o, reinterpret_cast<const typename WarpMmaPV::FragmentA(&)>(frag_p_reshaped[ki]), frag_v[ki], acc_o);
    //     }
    //     // Swizzle the elements and do the final reduction.
    //     smem_o.store(acc_o);

    //     // The mapping from tidx to rows changes between the softmax and the
    //     // O-reduction. So we recalculate the max.
    //     using OutputTileThreadMap = typename Smem_O::OutputTileThreadMap;
    //     constexpr int kOutputRowsPerThread = OutputTileThreadMap::Iterations::kRow * Smem_O::kIterationsStore;
    //     float p_max_o[kOutputRowsPerThread][Mma_tile_o::MMAS_M];
    //     int rows[kOutputRowsPerThread];
    //     cutlass::MatrixCoord output_thread_offset = OutputTileThreadMap::initial_offset(tidx);
    //     const int output_thread_start_row = output_thread_offset.row();
    //     const int output_thread_start_column = output_thread_offset.column();
    //     for (int iter = 0; iter < Smem_O::kIterationsStore; ++iter) {
    //         for (int row = 0; row < OutputTileThreadMap::Iterations::kRow; ++row) {
    //             rows[iter * OutputTileThreadMap::Iterations::kRow + row] = output_thread_start_row + iter * OutputTileThreadMap::Shape::kRow + row;
    //         }
    //     }

    //     softmax.reduce_max_after_sync_(p_max_o, rows);
    //     static_assert(Mma_tile_o::MMAS_M == 1);
    //     for (int jj = 0; jj < kOutputRowsPerThread; jj++) {
    //         p_max_o[jj][0] *= params.scale_bmm1;
    //     }
    //     float p_prev_scale_o[kOutputRowsPerThread];
    //     if (!Is_first) {
    //         smem_softmax_lse.load(p_prev_scale_o, rows);
    //     }

    //     // Make sure the data is in shared memory.
    //     __syncthreads();

    //     static_assert(Mma_tile_o::MMAS_M == 1);
    //     float p_sum_o[kOutputRowsPerThread][Mma_tile_o::MMAS_M];
    //     softmax.reduce_sum_after_sync_(p_sum_o, rows);
    //     if (!Is_first) {
    //         for (int jj = 0; jj < kOutputRowsPerThread; jj++) {
    //             p_prev_scale_o[jj] = expf(p_prev_scale_o[jj] - p_max_o[jj][0]);
    //             p_sum_o[jj][0] += p_prev_scale_o[jj];
    //         }
    //     }

    //     float p_sum_log[kOutputRowsPerThread][Mma_tile_o::MMAS_M];
    //     #pragma unroll
    //     for (int jj = 0; jj < kOutputRowsPerThread; jj++) {
    //         float sum = p_sum_o[jj][0];
    //         p_sum_log[jj][0] = (sum == 0.f || sum != sum) ? -INFINITY : p_max_o[jj][0] + __logf(sum);
    //         if (output_thread_start_column == 0) {
    //             gmem_softmax_lse.store_row(
    //                 reinterpret_cast<uint32_t(&)[Mma_tile_p::MMAS_M]>(p_sum_log[jj]), rows[jj]);
    //         }
    //     }
    //     gmem_softmax_lse.move();

    //     // Load from shared memory.
    //     using ArrayTypeO = cutlass::Array<ElementAccum, OutputTileThreadMap::kElementsPerAccess>;
    //     static_assert(OutputTileThreadMap::kElementsPerAccess * kOutputRowsPerThread == Smem_O::kIterationsStore * Smem_O::OutputFragment::kElements);
    //     cutlass::multiplies<ArrayTypeO> multiply_fragments;
    //     if (!Is_first) {
    //         auto out_reshaped = reinterpret_cast<ArrayTypeO (&)[kOutputRowsPerThread]>(out);
    //         for (int jj = 0; jj < kOutputRowsPerThread; jj++) {
    //             out_reshaped[jj] = multiply_fragments(out_reshaped[jj], p_prev_scale_o[jj]);
    //         }
    //     }
    //     smem_o.template load</*zero_init=*/Is_first>(out, tidx);

    //     const bool is_final_write =
    //         Is_last
    //         || ((loop_step_idx + 1) * Cta_tile_p::N >= binfo.actual_seqlen_k)
    //         || ((Is_causal) && ((begin + l) * Cta_tile_p::M < (loop_step_idx + 1) * Cta_tile_p::N));
    //     auto out_reshaped = reinterpret_cast<ArrayTypeO (&)[kOutputRowsPerThread]>(out);
    //     #pragma unroll
    //     for (int jj = 0; jj < kOutputRowsPerThread; jj++) {
    //         float sum = p_sum_o[jj][0];
    //         float inv_sum = (sum == 0.f || sum != sum) ? 1.f : 1.f / sum;
    //         if (Is_dropout && is_final_write) {
    //             inv_sum *= params.rp_dropout;
    //         }
    //         out_reshaped[jj] = multiply_fragments(out_reshaped[jj], inv_sum);
    //     }

    //     // Output the values.
    //     if (is_final_write) {
    //         typename GmemIteratorO::Fragment out_converted;
    //         cutlass::NumericArrayConverter<Element, ElementAccum, decltype(out_converted)::kElements, cutlass::FloatRoundStyle::round_to_nearest> convert_o;
    //         #pragma unroll
    //         for (int iter = 0; iter < GmemIteratorO::kIterations; ++iter) {
    //             out_converted = convert_o(out[iter]);
    //             gmem_o.store(out_converted);
    //             gmem_o.move();
    //         }
    //         // We also need to move gmem_o_accum. For example, if Is_causal=true and seqlen=512,
    //         // in the first loop, we write the first 256 rows to gmem_o and the last 256 rows to gmem_o_accum.
    //         if (Is_first && !Is_last) { gmem_o_accum.move(GmemIteratorOAccum::kIterations); }
    //     } else {
    //         if (!Is_first) { gmem_o_accum.move(-GmemIteratorOAccum::kIterations); }
    //         #pragma unroll
    //         for (int iter = 0; iter < GmemIteratorOAccum::kIterations; ++iter) {
    //             gmem_o_accum.store(out[iter]);
    //             gmem_o_accum.move();
    //         }
    //     }

    //     gemm_q_k.reload_k();

    //     // Trigger the load from shared memory for the next series of Q values.
    //     if(l < steps - 1) {
    //         gemm_q_k.reload_q();
    //     }

    // }  // Outer loop over the sequence length.
}

////////////////////////////////////////////////////////////////////////////////////////////////////

template<typename Kernel_traits, bool Is_dropout, bool Is_causal, bool Return_softmax, typename Params>
inline __device__ void device_1xN_loop(const Params &params) {

    // The block index for the batch.
    // const int bidb = blockIdx.x;
    const int bidb = blockIdx.y;
    // The block index for the head.
    // const int bidh = blockIdx.y;
    const int bidh = blockIdx.z;
    // The thread index.
    const int tidx = threadIdx.x;

    const int tidx_global = (bidb * params.h + bidh) * blockDim.x * 2 + tidx;
    auto seeds = at::cuda::philox::unpack(params.philox_args);
    // We use 2 Philox generators to match the dropout pattern in the backward pass.
    // Forward pass uses 128 threads while backward pass uses 256 threads, so each thread
    // in the forward pass is simulating the droout pattern of 2 threads in the backward pass.
    Philox ph0(std::get<0>(seeds), tidx_global, std::get<1>(seeds));
    Philox ph1(std::get<0>(seeds), tidx_global + blockDim.x, std::get<1>(seeds));
    constexpr int M = Kernel_traits::Cta_tile_p::M;
    const int STEPS = (params.seqlen_q + M - 1) / M;

    constexpr int blocksize_c = Kernel_traits::Cta_tile_p::N;
    // if (params.seqlen_k == blocksize_c) {
    //     fmha::device_1xN_<Kernel_traits, Is_dropout, Is_causal, Return_softmax, true, true>(params, bidb, bidh, 0, STEPS, ph0, ph1, 0);
    // } else {
    //     const int max_loop_steps = (params.seqlen_k + blocksize_c - 1) / blocksize_c;
    //     fmha::device_1xN_<Kernel_traits, Is_dropout, Is_causal, Return_softmax, true, false>(params, bidb, bidh, 0, STEPS, ph0, ph1, 0);
    //     for (int loop_step_idx = 1; loop_step_idx < max_loop_steps - 1; loop_step_idx++) {
    //         fmha::device_1xN_<Kernel_traits, Is_dropout, Is_causal, Return_softmax, false, false>(params, bidb, bidh, 0, STEPS, ph0, ph1, loop_step_idx);
    //     }
    //     fmha::device_1xN_<Kernel_traits, Is_dropout, Is_causal, Return_softmax, false, true>(params, bidb, bidh, 0, STEPS, ph0, ph1, max_loop_steps - 1);
    // }
    fmha::device_1xN_<Kernel_traits, Is_dropout, Is_causal, Return_softmax, true, true>(params, bidb, bidh, 0, STEPS, ph0, ph1, 0);
}

////////////////////////////////////////////////////////////////////////////////////////////////////

} // namespace fmha
