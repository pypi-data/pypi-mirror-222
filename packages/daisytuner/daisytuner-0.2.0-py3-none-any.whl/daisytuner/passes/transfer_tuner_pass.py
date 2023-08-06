import dace

from dace.transformation import pass_pipeline as ppl
from typing import Any, Dict

from daisytuner.tuning import TransferTuner


@dace.properties.make_properties
class TransferTunerPass(ppl.ScopePass):

    CATEGORY: str = "Optimization"

    def __init__(self, hostname: str, arch: str, topK: int, static_only: bool) -> None:
        super().__init__()

        self._hostname = hostname
        self._arch = arch
        self._topK = topK
        self._static_only = static_only
        self._tuner = TransferTuner(hostname=self._hostname, arch=self._arch)

    def modifies(self) -> ppl.Modifies:
        return ppl.Modifies.Scopes

    def should_reapply(self, modified: ppl.Modifies) -> bool:
        return False

    def apply(
        self,
        scope: dace.nodes.EntryNode,
        state: dace.SDFGState,
        pipeline_results: Dict[str, Any],
    ) -> int:
        if scope not in pipeline_results["loop_nests"]:
            return None

        schedule = self._tuner.tune(
            loop_nest=pipeline_results["loop_nests"][scope],
            topK=self._topK,
            static_only=self._static_only,
        )
        if not "transfer_tuning" in pipeline_results:
            pipeline_results["transfer_tuning"] = {}
        pipeline_results["transfer_tuning"][scope] = schedule
