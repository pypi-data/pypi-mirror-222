import dace
import itertools

from typing import Any, Dict

from dace.transformation import pass_pipeline as ppl
from dace.transformation.optimizer import Optimizer
from dace.transformation.dataflow import (
    MapFission,
    PruneConnectors,
    AugAssignToWCR,
    MapCollapse,
    MapFusion,
    TrivialTaskletElimination,
    TaskletFusion,
    MapExpansion,
)
from dace.transformation.interstate import (
    InlineSDFG,
    LoopToMap,
    MoveLoopIntoMap,
    InlineSDFG,
)

from daisytuner.loop_nest import LoopNest
from daisytuner.transformations import MapDistribute, TaskletSimplification


class LoopNestNormalFormPass(ppl.Pass):
    """
    Expands library nodes of an SDFG with implementations according to an order of implementations.
    """

    CATEGORY: str = "Simplification"

    recursive = True

    def __init__(self) -> None:
        super().__init__()

    def modifies(self) -> ppl.Modifies:
        return ppl.Modifies.Everything

    def should_reapply(self, modified: ppl.Modifies) -> bool:
        return False

    def apply_pass(self, sdfg: dace.SDFG, pipeline_results: Dict[str, Any]) -> int:
        sdfg.apply_transformations_repeated(TrivialTaskletElimination, validate=False)
        while True:
            xforms = Optimizer(sdfg).get_pattern_matches(patterns=(TaskletFusion,))
            target = None
            for xform in xforms:
                state = xform._sdfg.node(xform.state_id)
                if state.out_degree(xform.t1) == 1:
                    target = xform
                    break

            if target is None:
                break

            try:
                target.apply(state, xform._sdfg)
                sdfg.apply_transformations_repeated(
                    TaskletSimplification, validate=False
                )
            except TypeError:
                break

        # First round of parallelization
        sdfg.apply_transformations_repeated(
            (TaskletSimplification, AugAssignToWCR, InlineSDFG, LoopToMap),
            validate=False,
        )
        dace.propagate_memlets_sdfg(sdfg)
        sdfg.simplify()

        # Second round of parallelization
        sdfg.apply_transformations_repeated(
            (MoveLoopIntoMap, AugAssignToWCR, InlineSDFG, LoopToMap), validate=False
        )
        dace.propagate_memlets_sdfg(sdfg)
        sdfg.simplify()

        # Move states out of maps
        sdfg.apply_transformations_repeated(
            (MapDistribute, PruneConnectors, MapCollapse), validate=False
        )
        dace.propagate_memlets_sdfg(sdfg)
        sdfg.simplify()

        while True:
            xforms = Optimizer(sdfg).get_pattern_matches(patterns=(MapFission,))
            target = None
            for xform in xforms:
                state = xform._sdfg.node(xform.state_id)
                map_entry = xform.map_entry
                map_exit = state.exit_node(map_entry)

                # Dont' fission init maps
                if state.in_degree(map_entry) == 0:
                    continue

                # Don't fission is nested SDFG is nested or has loops
                if xform.expr_index == 1:
                    if xform._sdfg.parent_nsdfg_node is not None:
                        continue

                    if xform.nested_sdfg.sdfg.has_cycles():
                        continue

                    target = xform
                    break
                else:
                    if state.out_degree(map_exit) == 1:
                        continue

                target = xform

            if target is None:
                break

            state = target._sdfg.node(target.state_id)
            target.apply(state, target._sdfg)

            sdfg.apply_transformations_repeated(
                (MapDistribute, PruneConnectors, InlineSDFG), validate=False
            )

        sdfg.apply_transformations_repeated(MapCollapse, validate=False)

        # Third round of parallelization
        sdfg.apply_transformations_repeated(
            (TaskletSimplification, AugAssignToWCR), permissive=True, validate=False
        )
        dace.propagate_memlets_sdfg(sdfg)
        sdfg.apply_transformations_repeated(LoopToMap, validate=False)

        dace.propagate_memlets_sdfg(sdfg)
        sdfg.simplify()

        sdfg.apply_transformations_repeated(
            (MapDistribute, PruneConnectors),
            validate=False,
        )
        dace.propagate_memlets_sdfg(sdfg)
        sdfg.simplify()

        # Second round of fission
        while True:
            xforms = Optimizer(sdfg).get_pattern_matches(patterns=(MapFission,))
            target = None
            for xform in xforms:
                state = xform._sdfg.node(xform.state_id)
                map_entry = xform.map_entry
                map_exit = state.exit_node(map_entry)

                if xform.expr_index == 1:
                    if xform._sdfg.parent_nsdfg_node is not None:
                        continue

                    if xform.nested_sdfg.sdfg.has_cycles():
                        continue

                    target = xform
                    break
                else:
                    if state.out_degree(map_exit) == 1:
                        continue

                target = xform

            if target is None:
                break

            state = target._sdfg.node(target.state_id)
            target.apply(state, target._sdfg)

            sdfg.apply_transformations_repeated(
                (MapDistribute, PruneConnectors, InlineSDFG), validate=False
            )

        dace.propagate_memlets_sdfg(sdfg)
        sdfg.simplify()

        sdfg.apply_transformations_repeated(MapCollapse, validate=False)
        sdfg.apply_transformations_repeated(MapFusion, validate=False)

        for nsdfg in sdfg.all_sdfgs_recursive():
            for state in nsdfg.states():
                for node in state.nodes():
                    if not isinstance(node, dace.nodes.MapEntry):
                        continue
                    if len(node.map.params) < 2:
                        continue

                    map_entry = node
                    map_exit = state.exit_node(map_entry)
                    read_memlets = state.out_edges(map_entry)
                    write_memlets = state.in_edges(map_exit)

                    all_strides = {}
                    for edge in read_memlets:
                        memlet = edge.data
                        all_strides[memlet] = []
                        for i in range(len(map_entry.map.params)):
                            stride = int(
                                dace.symbolic.evaluate(
                                    memlet.get_stride(nsdfg, map_entry.map, dim=i),
                                    symbols=sdfg.constants,
                                )
                            )
                            all_strides[memlet].append(stride)

                    for edge in write_memlets:
                        memlet = edge.data
                        all_strides[memlet] = []
                        for i in range(len(map_entry.map.params)):
                            stride = int(
                                dace.symbolic.evaluate(
                                    memlet.get_stride(nsdfg, map_entry.map, dim=i),
                                    symbols=sdfg.constants,
                                )
                            )
                            all_strides[memlet].append(stride)

                    permutations = list(
                        itertools.permutations(tuple(range(len(map_entry.map.params))))
                    )
                    new_perm = tuple(range(len(map_entry.map.params)))
                    for perm in permutations[1:]:
                        changes = {}
                        for memlet, strides in all_strides.items():
                            new_strides = [strides[i] for i in perm]

                            change = 0
                            for s, s_ in zip(strides[::-1], new_strides[::-1]):
                                if s > s_:
                                    change = 1
                                    break
                                elif s < s_:
                                    change = -1
                                    break
                                else:
                                    continue

                            changes[memlet] = change

                        success = all(map(lambda e: e >= 0, changes.values())) and any(
                            map(lambda e: e == 1, changes.values())
                        )
                        if success:
                            new_perm = perm
                            break

                    new_params = [map_entry.map.params[i] for i in new_perm]
                    map_entry.range.ranges = [
                        r
                        for list_param in new_params
                        for map_param, r in zip(
                            map_entry.map.params, map_entry.range.ranges
                        )
                        if list_param == map_param
                    ]
                    map_entry.map.params = new_params

        sdfg.apply_transformations_repeated(MapCollapse)
        sdfg.simplify()

        loop_nests = {}
        for nsdfg in sdfg.all_sdfgs_recursive():
            for state in nsdfg.states():
                for node in state.nodes():
                    if not isinstance(node, dace.nodes.MapEntry):
                        continue

                    entry_node = state.entry_node(node)
                    if isinstance(entry_node, dace.nodes.MapEntry):
                        continue

                    if state.in_degree(node) == 0:
                        continue

                    if entry_node is None:
                        try:
                            loop_nest = LoopNest.create(nsdfg, state, node)
                            loop_nests[node] = loop_nest
                        except:
                            continue
                    else:
                        assert isinstance(entry_node, dace.nodes.NestedSDFG)
                        assert False

        pipeline_results["loop_nests"] = loop_nests
