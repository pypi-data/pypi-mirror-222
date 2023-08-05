"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._498 import CylindricalGearSetRatingOptimisationHelper
    from ._499 import OptimisationResultsPair
    from ._500 import SafetyFactorOptimisationResults
    from ._501 import SafetyFactorOptimisationStepResult
    from ._502 import SafetyFactorOptimisationStepResultAngle
    from ._503 import SafetyFactorOptimisationStepResultNumber
    from ._504 import SafetyFactorOptimisationStepResultShortLength
else:
    import_structure = {
        '_498': ['CylindricalGearSetRatingOptimisationHelper'],
        '_499': ['OptimisationResultsPair'],
        '_500': ['SafetyFactorOptimisationResults'],
        '_501': ['SafetyFactorOptimisationStepResult'],
        '_502': ['SafetyFactorOptimisationStepResultAngle'],
        '_503': ['SafetyFactorOptimisationStepResultNumber'],
        '_504': ['SafetyFactorOptimisationStepResultShortLength'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
