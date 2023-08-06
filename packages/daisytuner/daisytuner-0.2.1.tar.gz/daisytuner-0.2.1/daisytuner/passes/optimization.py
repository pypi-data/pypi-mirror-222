from dace.transformation import pass_pipeline as ppl

from daisytuner.passes.expansion_pass import ExpansionPass
from daisytuner.passes.loop_nest_normal_form_pass import LoopNestNormalFormPass
from daisytuner.passes.transfer_tuner_pass import TransferTunerPass
from daisytuner.passes.set_scheduling_options import SetSchedulingOptions


class Optimization:
    @classmethod
    def create(cls, topK: int, use_profiling_features: bool = False) -> ppl.Pipeline:
        pipeline = ppl.Pipeline(
            [
                ExpansionPass(),
                LoopNestNormalFormPass(),
                TransferTunerPass(
                    topK=topK,
                    use_profiling_features=use_profiling_features,
                ),
                SetSchedulingOptions(),
            ]
        )
        return pipeline
