"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._566 import BiasModification
    from ._567 import FlankMicroGeometry
    from ._568 import FlankSide
    from ._569 import LeadModification
    from ._570 import LocationOfEvaluationLowerLimit
    from ._571 import LocationOfEvaluationUpperLimit
    from ._572 import LocationOfRootReliefEvaluation
    from ._573 import LocationOfTipReliefEvaluation
    from ._574 import MainProfileReliefEndsAtTheStartOfRootReliefOption
    from ._575 import MainProfileReliefEndsAtTheStartOfTipReliefOption
    from ._576 import Modification
    from ._577 import ParabolicRootReliefStartsTangentToMainProfileRelief
    from ._578 import ParabolicTipReliefStartsTangentToMainProfileRelief
    from ._579 import ProfileModification
else:
    import_structure = {
        '_566': ['BiasModification'],
        '_567': ['FlankMicroGeometry'],
        '_568': ['FlankSide'],
        '_569': ['LeadModification'],
        '_570': ['LocationOfEvaluationLowerLimit'],
        '_571': ['LocationOfEvaluationUpperLimit'],
        '_572': ['LocationOfRootReliefEvaluation'],
        '_573': ['LocationOfTipReliefEvaluation'],
        '_574': ['MainProfileReliefEndsAtTheStartOfRootReliefOption'],
        '_575': ['MainProfileReliefEndsAtTheStartOfTipReliefOption'],
        '_576': ['Modification'],
        '_577': ['ParabolicRootReliefStartsTangentToMainProfileRelief'],
        '_578': ['ParabolicTipReliefStartsTangentToMainProfileRelief'],
        '_579': ['ProfileModification'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
