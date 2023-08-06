import dace

from dace.transformation import pass_pipeline as ppl
from typing import Any, Dict

from daisytuner.tuning import TransferTuner


@dace.properties.make_properties
class TransferTunerPass(ppl.ScopePass):

    CATEGORY: str = "Optimization"

    def __init__(self, topK: int, use_profiling_features: bool) -> None:
        super().__init__()

        self._tuner = TransferTuner()
        self._topK = topK
        self._use_profiling_features = use_profiling_features

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
            use_profiling_features=self._use_profiling_features,
        )
        if not "transfer_tuning" in pipeline_results:
            pipeline_results["transfer_tuning"] = {}
        pipeline_results["transfer_tuning"][scope] = schedule
