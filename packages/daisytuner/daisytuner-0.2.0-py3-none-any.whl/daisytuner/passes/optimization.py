from dace.transformation import pass_pipeline as ppl

from daisytuner.utils import host
from daisytuner.architecture import architecture
from daisytuner.passes.expansion_pass import ExpansionPass
from daisytuner.passes.loop_nest_normal_form_pass import LoopNestNormalFormPass
from daisytuner.passes.transfer_tuner_pass import TransferTunerPass
from daisytuner.passes.set_scheduling_options import SetSchedulingOptions


class Optimization:
    @classmethod
    def create(cls, topK: int, static_only: bool) -> ppl.Pipeline:
        pipeline = ppl.Pipeline(
            [
                ExpansionPass(),
                LoopNestNormalFormPass(),
                TransferTunerPass(
                    hostname=host(),
                    arch=architecture()["cpu"],
                    topK=topK,
                    static_only=static_only,
                ),
                SetSchedulingOptions(),
            ]
        )
        return pipeline
