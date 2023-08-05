"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2537 import BoostPressureInputOptions
    from ._2538 import InputPowerInputOptions
    from ._2539 import PressureRatioInputOptions
    from ._2540 import RotorSetDataInputFileOptions
    from ._2541 import RotorSetMeasuredPoint
    from ._2542 import RotorSpeedInputOptions
    from ._2543 import SuperchargerMap
    from ._2544 import SuperchargerMaps
    from ._2545 import SuperchargerRotorSet
    from ._2546 import SuperchargerRotorSetDatabase
    from ._2547 import YVariableForImportedData
else:
    import_structure = {
        '_2537': ['BoostPressureInputOptions'],
        '_2538': ['InputPowerInputOptions'],
        '_2539': ['PressureRatioInputOptions'],
        '_2540': ['RotorSetDataInputFileOptions'],
        '_2541': ['RotorSetMeasuredPoint'],
        '_2542': ['RotorSpeedInputOptions'],
        '_2543': ['SuperchargerMap'],
        '_2544': ['SuperchargerMaps'],
        '_2545': ['SuperchargerRotorSet'],
        '_2546': ['SuperchargerRotorSetDatabase'],
        '_2547': ['YVariableForImportedData'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
