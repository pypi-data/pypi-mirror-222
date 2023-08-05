"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6237 import CombinationAnalysis
    from ._6238 import FlexiblePinAnalysis
    from ._6239 import FlexiblePinAnalysisConceptLevel
    from ._6240 import FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass
    from ._6241 import FlexiblePinAnalysisGearAndBearingRating
    from ._6242 import FlexiblePinAnalysisManufactureLevel
    from ._6243 import FlexiblePinAnalysisOptions
    from ._6244 import FlexiblePinAnalysisStopStartAnalysis
    from ._6245 import WindTurbineCertificationReport
else:
    import_structure = {
        '_6237': ['CombinationAnalysis'],
        '_6238': ['FlexiblePinAnalysis'],
        '_6239': ['FlexiblePinAnalysisConceptLevel'],
        '_6240': ['FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass'],
        '_6241': ['FlexiblePinAnalysisGearAndBearingRating'],
        '_6242': ['FlexiblePinAnalysisManufactureLevel'],
        '_6243': ['FlexiblePinAnalysisOptions'],
        '_6244': ['FlexiblePinAnalysisStopStartAnalysis'],
        '_6245': ['WindTurbineCertificationReport'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
