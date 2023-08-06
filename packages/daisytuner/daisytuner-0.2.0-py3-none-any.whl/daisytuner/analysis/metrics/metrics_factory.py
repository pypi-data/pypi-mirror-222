from typing import List


class MetricsFactory:
    @classmethod
    def create(cls, arch: str, groups: List[str]):
        if arch == "broadwellEP":
            from daisytuner.analysis.metrics.broadwellEP_metrics import (
                BroadwellEPMetrics,
            )

            return BroadwellEPMetrics(groups=groups)
        elif arch == "haswellEP":
            from daisytuner.analysis.metrics.haswellEP_metrics import (
                HaswellEPMetrics,
            )

            return HaswellEPMetrics(groups=groups)
        elif arch == "skylake":
            from daisytuner.analysis.metrics.skylakeX_metrics import (
                SkylakeMetrics,
            )

            return SkylakeMetrics(groups=groups)
        elif arch == "skylakeX":
            from daisytuner.analysis.metrics.skylakeX_metrics import (
                SkylakeXMetrics,
            )

            return SkylakeXMetrics(groups=groups)
        elif arch == "zen":
            from daisytuner.analysis.metrics.zen_metrics import (
                ZenMetrics,
            )

            return ZenMetrics(groups=groups)
        elif arch == "zen2":
            from daisytuner.analysis.metrics.zen2_metrics import (
                Zen2Metrics,
            )

            return Zen2Metrics(groups=groups)
        elif arch == "zen3":
            from daisytuner.analysis.metrics.zen3_metrics import (
                Zen3Metrics,
            )

            return Zen3Metrics(groups=groups)
        else:
            assert False
