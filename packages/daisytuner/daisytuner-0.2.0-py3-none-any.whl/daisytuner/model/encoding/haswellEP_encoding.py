import numpy as np
import pandas as pd

from collections import defaultdict

from daisytuner.loop_nest import LoopNest
from daisytuner.model.encoding.profiling_encoding import ProfilingEncoding


class HaswellEPEncoding(ProfilingEncoding):
    def __init__(self, loop_nest: LoopNest, hostname: str) -> None:
        super().__init__(loop_nest=loop_nest, hostname=hostname, arch="haswellEP")

    def _vectorize(self, data: pd.DataFrame) -> np.ndarray:
        # min, max, sum, mean, std
        num_statistics = 5
        num_counters = 16

        encoding = np.zeros((num_statistics * num_counters,))

        # INSTRUCTIONS
        encoding[
            0 * num_statistics : 1 * num_statistics
        ] = ProfilingEncoding._normalize(data, "INSTR_RETIRED_ANY")

        # FLOPS_SP
        encoding[
            1 * num_statistics : 2 * num_statistics
        ] = ProfilingEncoding._normalize(data, "AVX_INSTS_CALC")
        encoding[2 * num_statistics : 5 * num_statistics] = 0.0

        # FLOPS_DP
        encoding[
            5 * num_statistics : 6 * num_statistics
        ] = ProfilingEncoding._normalize(data, "AVX_INSTS_CALC")
        encoding[6 * num_statistics : 9 * num_statistics] = 0.0

        # BRANCH
        encoding[
            9 * num_statistics : 10 * num_statistics
        ] = ProfilingEncoding._normalize(data, "BR_INST_RETIRED_ALL_BRANCHES")
        encoding[
            10 * num_statistics : 11 * num_statistics
        ] = ProfilingEncoding._normalize(data, "BR_MISP_RETIRED_ALL_BRANCHES")

        # MEM Volume
        encoding[
            11 * num_statistics : 12 * num_statistics
        ] = ProfilingEncoding._normalize(
            data, "CAS_COUNT_RD"
        ) + ProfilingEncoding._normalize(
            data, "CAS_COUNT_WR"
        )

        # L3 Volume
        encoding[
            12 * num_statistics : 13 * num_statistics
        ] = ProfilingEncoding._normalize(
            data, "L2_LINES_IN_ALL"
        ) + ProfilingEncoding._normalize(
            data, "L2_TRANS_L2_WB"
        )

        # L2 Volume
        encoding[
            13 * num_statistics : 14 * num_statistics
        ] = ProfilingEncoding._normalize(
            data, "L1D_REPLACEMENT"
        ) + ProfilingEncoding._normalize(
            data, "L2_TRANS_L1D_WB"
        )

        # DRAM controller
        encoding[
            14 * num_statistics : 15 * num_statistics
        ] = ProfilingEncoding._normalize(data, "MEM_UOPS_RETIRED_LOADS")
        encoding[
            15 * num_statistics : 16 * num_statistics
        ] = ProfilingEncoding._normalize(data, "MEM_UOPS_RETIRED_STORES")

        return encoding
