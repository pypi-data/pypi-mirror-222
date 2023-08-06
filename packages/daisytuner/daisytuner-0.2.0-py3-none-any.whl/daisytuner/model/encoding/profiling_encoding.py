import torch
import numpy as np

from abc import ABC, abstractmethod

from daisytuner.loop_nest import LoopNest
from daisytuner.architecture import minimal_groups
from daisytuner.analysis.profiling import Profiling


class ProfilingEncoding(ABC):
    def __init__(self, loop_nest: LoopNest, hostname: str, arch: str) -> None:
        self._loop_nest = loop_nest
        self._hostname = hostname
        self._arch = arch
        self._encoding = None

    def encode(self, cache_only: bool = False) -> torch.tensor:
        if self._encoding is not None:
            return self._encoding

        # Gather instrumentation data
        instrumentation = Profiling(
            loop_nest=self._loop_nest,
            hostname=self._hostname,
            arch=self._arch,
            groups=minimal_groups(self._arch),
        )
        data = instrumentation.analyze(cache_only=cache_only)

        # Compute statistics over threads; median over repetitions
        data = data.groupby("REPETITION").agg(["min", "max", "sum", "mean", "std"])
        data = data.median()
        data = self._vectorize(data)

        self._encoding = torch.tensor(data, dtype=torch.float)[None, :]
        return self._encoding

    @abstractmethod
    def _vectorize(self, data) -> np.ndarray:
        pass

    @classmethod
    def _normalize(cls, counters, name) -> np.ndarray:
        stats = np.zeros(5)
        for i, stat in enumerate(["min", "max", "sum", "mean", "std"]):
            stats[i] = counters[name][stat]

        return stats

    @classmethod
    def create(cls, loop_nest: LoopNest, hostname: str, arch: str):
        if arch == "broadwellEP":
            from daisytuner.model.encoding.broadwellEP_encoding import (
                BroadwellEPEncoding,
            )

            return BroadwellEPEncoding(loop_nest=loop_nest, hostname=hostname)
        elif arch == "haswellEP":
            from daisytuner.model.encoding.haswellEP_encoding import HaswellEPEncoding

            return HaswellEPEncoding(loop_nest=loop_nest, hostname=hostname)
        elif arch == "skylakeX":
            from daisytuner.model.encoding.skylakeX_encoding import SkylakeXEncoding

            return SkylakeXEncoding(loop_nest=loop_nest, hostname=hostname)
        elif arch == "zen":
            from daisytuner.model.encoding.zen_encoding import ZenEncoding

            return ZenEncoding(loop_nest=loop_nest, hostname=hostname)
        elif arch == "zen2":
            from daisytuner.model.encoding.zen2_encoding import Zen2Encoding

            return Zen2Encoding(loop_nest=loop_nest, hostname=hostname)
        elif arch == "zen3":
            from daisytuner.model.encoding.zen3_encoding import Zen3Encoding

            return Zen3Encoding(loop_nest=loop_nest, hostname=hostname)
        else:
            raise ValueError("Unsupported architecture: ", arch)
