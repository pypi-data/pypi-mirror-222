// Copyright (c) 2023, Tri Dao.

// Splitting the different head dimensions to different files to speed up compilation.

#include "fmha_bwd_launch_template.h"

void run_fmha_bwd_hdim64(FMHA_dgrad_params &params, cudaStream_t stream, const bool configure) {
    using elem_type = cutlass::half_t;
    using Kernel_traits = FMHA_bwd_kernel_traits<64, 32, 128, 8, elem_type>;
    run_fmha_bwd_loop<Kernel_traits>(params, stream, configure);
}