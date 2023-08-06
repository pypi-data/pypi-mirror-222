/******************************************************************************
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

#include "cute/algorithm/copy.hpp"

#include "cutlass/gemm/gemm.h"

#include "cutlass/cutlass.h"
#include "cutlass/layout/layout.h"
#include <cutlass/numeric_types.h>
#include "cutlass/transform/threadblock/predicated_tile_iterator.h"

#include <fmha/gemm.h>
#include <fmha/summary_stats.h>
#include <fmha/mma_core_sm75.h>

////////////////////////////////////////////////////////////////////////////////////////////////////

using namespace cute;

template<int kBlockM_, int kBlockN_, int kHeadDim_, int WARPS_M, int WARPS_N, uint32_t FLAGS = 0x08u, typename elem_type=cutlass::half_t>
struct FMHA_kernel_traits {

    static constexpr int kBlockM = kBlockM_;
    static constexpr int kBlockN = kBlockN_;
    // static constexpr int kBlockN = 128;
    // static constexpr int kBlockN = 64;
    // static constexpr int kBlockN = 32;
    static constexpr int kHeadDim = kHeadDim_;
    static constexpr int kBlockK = (kHeadDim == 32 || kHeadDim == 64) ? kHeadDim : 64;  // Could be 32 if headdim=96?
    static_assert(kBlockK == 32 || kBlockK == 64, "kBlockK must be 32 or 64");
    static constexpr int kSwizzle = kBlockK == 32 ? 2 : 3;
    static constexpr int kSwizzleN = kBlockN == 32 ? 2 : 3;

    static constexpr int S = kBlockM_; // For old kernel traits
    static constexpr int D = kHeadDim;    // For old kernel traits
    static constexpr int STEP = 16;    // For old kernel traits

    using SmemLayoutAtomQ = decltype(
        composition(Swizzle<kSwizzle, 3, 3>{},
                    Layout<Shape<_8, Int<kBlockK>>,
                    // TODO: should this be kHeadDim or kBlockK?
                           Stride<Int<kBlockK>, _1>>{}));
    using SmemLayoutQ = decltype(tile_to_shape(
        SmemLayoutAtomQ{},
        make_shape(Int<kBlockM>{}, Int<kHeadDim>{})));
    using SmemCopyAtomQ = Copy_Atom<SM75_U32x4_LDSM_N, elem_type>;

    using SmemLayoutK = decltype(tile_to_shape(
        SmemLayoutAtomQ{},
        make_shape(Int<kBlockN>{}, Int<kHeadDim>{})));
    using SmemCopyAtomK = Copy_Atom<SM75_U32x4_LDSM_N, elem_type>;

    using SmemLayoutV = SmemLayoutK;
    using SmemLayoutAtomVtransposed = decltype(
        composition(Swizzle<kSwizzle, 3, 3>{},
                    Layout<Shape<Int<kBlockK>, _8>,
                           Stride<_1, Int<kBlockK>>>{}));
                    // TODO: what if blockN > 64?
                    // Layout<Shape<Int<kBlockN>, _8>,
                    //        Stride<_1, Int<kBlockN>>>{}));
    // using SmemLayoutAtomVtransposed = Layout<Shape<Int<kBlockK>, _8>,
    //                                          Stride<_1, Int<kBlockK>>>;
    // using SmemLayoutVtransposed = decltype(tile_to_shape(
    //     SmemLayoutAtomVtransposed{},
    //     // TODO: is this <N, K> or <K, N>?
    //     // make_shape(Int<kBlockN>{}, Int<kHeadDim>{})));
    //     make_shape(Int<kHeadDim>{}, Int<kBlockN>{})));
    using SmemLayoutVtransposed = decltype(
        // TODO: I've no idea if it should be kSwizzleN or kSwizzle
        composition(Swizzle<kSwizzle, 3, 3>{},
        // composition(Swizzle<kSwizzleN, 3, 3>{},
                    Layout<Shape<Int<kHeadDim>, Int<kBlockN>>,
                           Stride<_1, Int<kBlockK>>>{}));
    using SmemLayoutVtransposedNoSwizzle = Layout<Shape<Int<kHeadDim>, Int<kBlockN>>,
                                                  Stride<_1, Int<kBlockK>>>;
    using SmemCopyAtomV = Copy_Atom<SM75_U16x8_LDSM_T, elem_type>;

    using SmemLayoutAtomO = decltype(
        composition(Swizzle<kSwizzle, 3, 3>{},
                    Layout<Shape<_8, Int<kBlockK>>,
                           Stride<Int<kBlockK>, _1>>{}));
    using SmemLayoutO = decltype(tile_to_shape(
        SmemLayoutAtomO{},
        make_shape(Int<kBlockM>{}, Int<kHeadDim>{})));
    using CopyAtomOR2S = Copy_Atom<DefaultCopy, elem_type>;
    using CopyAtomOR2G = Copy_Atom<DefaultCopy, elem_type>;

    // using SmemLayoutAtomQNoSwizzle = Layout<Shape < _8,_64>, Stride<_64, _1>>;
    // using SmemLayoutQNoSwizzle = decltype(tile_to_shape(
    //     SmemLayoutAtomQNoSwizzle{},
    //     make_shape(Int<128>{}, Int<64>{})));
    // using SmemLayoutKNoSwizzle = decltype(tile_to_shape(
    //     SmemLayoutAtomQNoSwizzle{},
    //     make_shape(Int<64>{}, Int<64>{})));
    // // using SmemLayoutAtomVNoSwizzle = Layout<Shape < _64,_8>, Stride<_1, _64>>;
    // using SmemLayoutAtomVNoSwizzle = Layout<Shape < _8,_64>, Stride<_64, _1>>;
    // using SmemLayoutVNoSwizzle = decltype(tile_to_shape(
    //     SmemLayoutAtomVNoSwizzle{},
    //     make_shape(Int<64>{}, Int<64>{})));
    // using SmemLayoutAtomONoSwizzle = Layout<Shape < _8,_64>, Stride<_64, _1>>;
    // using SmemLayoutONoSwizzle = decltype(tile_to_shape(
    //     SmemLayoutAtomONoSwizzle{},
    //     make_shape(Int<128>{}, Int<64>{})));

    using GmemLayoutAtom = typename std::conditional<
        kBlockK == 32,
        Layout<Shape <_32, _4>,  // Thread layout, 4 threads per row
               Stride< _4, _1>>,
        Layout<Shape <_16, _8>,  // Thread layout, 8 threads per row
               Stride< _8, _1>>
    >::type;
    // using GmemLayoutAtom = Layout<Shape <_16, _8>,  // Thread layout, 8 threads per row
    //                               Stride< _8, _1>>;

    using GmemTiledCopyQKV = decltype(
        make_tiled_copy(Copy_Atom<SM80_CP_ASYNC_CACHEALWAYS<cute::uint128_t>, elem_type>{},
        // make_tiled_copy(Copy_Atom<DefaultCopy, elem_type>{},
                        GmemLayoutAtom{},
                        Layout<Shape < _1, _8>>{}));  // Val layout, 8 vals per read
    // using GmemTiledCopyO = GmemTiledCopyQKV;
    using GmemTiledCopyO = decltype(
        make_tiled_copy(Copy_Atom<DefaultCopy, elem_type>{},
                        GmemLayoutAtom{},
                        Layout<Shape < _1, _8>>{}));  // Val layout, 8 vals per store

    using TiledMma = TiledMMA<
        MMA_Atom<SM80_16x8x16_F32F16F16F32_TN>,
        Layout<Shape<_4,_1,_1>>,  // 4x1x1 thread group
        Layout<Shape<_1,_2,_1>>>; // 1x2x1 value group for 16x16x16 MMA and LDSM

    // The CTA description for the 1st GEMM.
    using Cta_tile_p = fmha::Cta_tile_extd<STEP, S, D, WARPS_M, WARPS_N, 1>;
    // The CTA description for the 2nd GEMM.
    using Cta_tile_o = fmha::Cta_tile_extd<STEP, D, S, WARPS_M, 1, WARPS_N>;

    // Do we use one buffer for K and V.
    static constexpr bool SHARE_SMEM_FOR_K_AND_V = (FLAGS & 0x08u) != 0u;
    // Do we keep K in registers.
    static constexpr bool K_IN_REGS = (FLAGS & 0x10u) == 0u;
    // Do we keep V in registers.
    static constexpr bool V_IN_REGS = (FLAGS & 0x100u) == 0u;

    // The global memory tile to load/store S.
    using Gmem_tile_s = fmha::Gmem_tile_mma_s<Cta_tile_p>;

    // The global memory tile to store the softmax sum.
    using Gmem_softmax_sum = fmha::Gmem_summary_stats<Cta_tile_p>;

    // The number of threads.
    static constexpr int THREADS = Cta_tile_p::THREADS_PER_CTA;
    // Make sure the number of threads matches both CTAs.
    static_assert(THREADS == Cta_tile_o::THREADS_PER_CTA, "");

#if defined(__CUDA_ARCH__) && __CUDA_ARCH__ >= 800
    using MmaInstructionShape = cutlass::gemm::GemmShape<16, 8, 16>;
#elif defined(__CUDA_ARCH__) && __CUDA_ARCH__ >= 750
    using MmaInstructionShape = cutlass::gemm::GemmShape<16, 8, 8>;
#else
    // using MmaInstructionShape = cutlass::gemm::GemmShape<8, 8, 4>;
    using MmaInstructionShape = cutlass::gemm::GemmShape<16, 8, 16>;
    // TD [2022-06-02] We don't support Volta (SM70) yet.
#endif

#if defined(__CUDA_ARCH__) &&  __CUDA_ARCH__ >= 800
    using Element = elem_type;
#else
    using Element = cutlass::half_t;
#endif
    using ElementAccum = float;

    static_assert(WARPS_M == 1);
    using ThreadblockShapeQK = cutlass::gemm::GemmShape<STEP, S, D>;
    using WarpCountQK = cutlass::gemm::GemmShape<WARPS_M, WARPS_N, 1>;
    using WarpShapeQK = cutlass::gemm::GemmShape<
       ThreadblockShapeQK::kM,
       ThreadblockShapeQK::kN / WarpCountQK::kN, ThreadblockShapeQK::kK>;
    using LayoutQ = cutlass::layout::RowMajor;
    using LayoutK = cutlass::layout::ColumnMajor;
    using LayoutP = cutlass::layout::RowMajor;
    using MmaCoreQK = typename fmha::FMHAMmaCore<
        ThreadblockShapeQK, WarpShapeQK, MmaInstructionShape, Element, LayoutQ,
        Element, LayoutK, ElementAccum, LayoutP,
        cutlass::arch::OpClassTensorOp>;

    using ThreadblockShapePV = cutlass::gemm::GemmShape<STEP, D, S>;
    using WarpCountPV = cutlass::gemm::GemmShape<WARPS_M, 1, WARPS_N>;
    using WarpShapePV = cutlass::gemm::GemmShape<ThreadblockShapePV::kM, ThreadblockShapePV::kN, ThreadblockShapePV::kK / WarpCountPV::kK>;
    using LayoutV = cutlass::layout::RowMajor;
    using LayoutO = cutlass::layout::RowMajor;
    using MmaCorePV = typename fmha::FMHAMmaCore<
        ThreadblockShapePV, WarpShapePV, MmaInstructionShape, Element, LayoutP,
        Element, LayoutV, ElementAccum, LayoutO,
        cutlass::arch::OpClassTensorOp>;

    // The global memory tile to load Q.
    // Copy from mma_piplined_testbed.h
    using GmemIteratorQ = cutlass::transform::threadblock::PredicatedTileIterator<
      cutlass::MatrixShape<ThreadblockShapeQK::kM, ThreadblockShapeQK::kK>,
      Element,
      LayoutQ,
      0,
      typename MmaCoreQK::IteratorThreadMapA
    >;

    // The global memory tile to load K.
    using GmemIteratorK = cutlass::transform::threadblock::PredicatedTileIterator<
      cutlass::MatrixShape<ThreadblockShapeQK::kK, ThreadblockShapeQK::kN>,
      Element,
      LayoutK,
      1,
      typename MmaCoreQK::IteratorThreadMapB
    >;

    // The global memory tile to load V.
    using GmemIteratorV = cutlass::transform::threadblock::PredicatedTileIterator<
      cutlass::MatrixShape<ThreadblockShapePV::kK, ThreadblockShapePV::kN>,
      Element,
      LayoutV,
      0,
      typename MmaCorePV::IteratorThreadMapB
    >;

    // The shared memory tile to store softmax lse.
    using Smem_softmax_lse = fmha::Smem_tile_softmax_lse<ThreadblockShapeQK::kM, MmaInstructionShape::kM, WarpCountQK::kM>;

    // The amount of shared memory needed to load Q and K.
    static constexpr size_t BYTES_PER_SMEM_Q = ThreadblockShapeQK::kM * ThreadblockShapeQK::kK * sizeof(Element);
    static constexpr size_t BYTES_PER_SMEM_K = ThreadblockShapeQK::kN * ThreadblockShapeQK::kK * sizeof(Element);
    static constexpr size_t BYTES_PER_SMEM_V = ThreadblockShapePV::kN * ThreadblockShapePV::kK * sizeof(Element);
    static_assert(BYTES_PER_SMEM_K == BYTES_PER_SMEM_V);
    static constexpr size_t BYTES_PER_SMEM_QK = BYTES_PER_SMEM_Q + BYTES_PER_SMEM_K;
    // The extra amount of shared memory needed to load V.
    static constexpr size_t BYTES_PER_SMEM_V_EXTRA = SHARE_SMEM_FOR_K_AND_V ? 0u : BYTES_PER_SMEM_V;
    // The amount of shared memory needed for Q, K and V..
    static constexpr size_t BYTES_PER_SMEM_QKV = BYTES_PER_SMEM_QK + BYTES_PER_SMEM_V_EXTRA;

};

////////////////////////////////////////////////////////////////////////////////////////////////////
