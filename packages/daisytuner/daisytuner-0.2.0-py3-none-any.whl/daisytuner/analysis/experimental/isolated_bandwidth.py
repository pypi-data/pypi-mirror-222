import copy
import dace
import pandas as pd

from typing import List

from daisytuner.loop_nest import LoopNest
from daisytuner.utils import host
from daisytuner.architecture import architecture, minimal_groups
from daisytuner.analysis.profiling import Profiling


class IsolatedBandwidth:
    def __init__(
        self,
        loop_nest: LoopNest,
        hostname: str,
        arch: str,
        groups: List[str] = ["CACHE"],
    ) -> None:
        assert hostname is not None and arch is not None

        self._cache_path = loop_nest.cache_folder / "analysis" / "bandwidth_analysis"
        self._loop_nest = loop_nest

        self._hostname = hostname
        self._arch = arch
        self._groups = groups
        if self._hostname is None:
            self._hostname = host()
            self._arch = architecture()["cpu"]

        if self._groups is None:
            self._groups = minimal_groups(self._arch)

        self._input_arrays = None
        self._kernels = None
        self._bandwidths = None

    def analyze(self, cache_only: bool = False) -> pd.DataFrame:
        sdfg = self._loop_nest.cutout
        state = sdfg.start_state
        self._input_arrays = set()
        for node in state.data_nodes():
            if state.in_degree(node) == 0 and isinstance(
                sdfg.arrays[node.data], dace.data.Array
            ):
                self._input_arrays.add(node.data)

        # Create kernels
        self._kernels = {}
        for array in self._input_arrays:
            self._kernels[array] = self._create_kernel(array)

        # Measure
        self._bandwidths = {}
        for array, kernel in self._kernels.items():
            loop_nest = LoopNest.create(
                kernel, kernel.start_state, build_folder=self._cache_path / array
            )
            inst = Profiling(
                loop_nest=loop_nest,
                hostname=self._hostname,
                arch=self._arch,
                groups=self._groups,
            )
            _ = inst.analyze(cache_only=cache_only)
            metrics = inst.performance_metrics()
            self._bandwidths[array] = metrics

        return self._bandwidths

    def _create_kernel(self, array: dace.data.Array):
        kernel = copy.deepcopy(self._loop_nest.cutout)

        # Remove memlet paths of all other arrays
        state = kernel.start_state
        for node in state.data_nodes():
            if state.in_degree(node) == 0 and node.data != array:
                for edge in state.out_edges(node):
                    state.remove_memlet_path(edge)

        syms = {**kernel.constants}
        for sym in kernel.free_symbols:
            syms[sym] = 1
        kernel.specialize(syms)

        kernel.validate()

        return kernel
