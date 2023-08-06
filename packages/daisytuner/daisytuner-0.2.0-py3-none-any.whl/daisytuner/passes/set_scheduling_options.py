import dace

from typing import Any, Dict, List

from dace.transformation import pass_pipeline as ppl
from dace.transformation.auto.auto_optimize import make_transients_persistent


class SetSchedulingOptions(ppl.Pass):
    """
    Expands library nodes of an SDFG with implementations according to an order of implementations.
    """

    CATEGORY: str = "Simplification"

    def __init__(self) -> None:
        super().__init__()

    def modifies(self) -> ppl.Modifies:
        return ppl.Modifies.Everything

    def should_reapply(self, modified: ppl.Modifies) -> bool:
        return False

    def apply_pass(self, sdfg: dace.SDFG, pipeline_results: Dict[str, Any]) -> int:
        sdfg.expand_library_nodes()
        sdfg.openmp_sections = False
        dace.sdfg.infer_types.infer_connector_types(sdfg)
        dace.sdfg.infer_types.set_default_schedule_and_storage_types(sdfg, None)
        make_transients_persistent(sdfg, dace.DeviceType.CPU)
