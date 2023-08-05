"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1368 import ElectricMachineHarmonicLoadDataBase
    from ._1369 import ForceDisplayOption
    from ._1370 import HarmonicLoadDataBase
    from ._1371 import HarmonicLoadDataControlExcitationOptionBase
    from ._1372 import HarmonicLoadDataType
    from ._1373 import SpeedDependentHarmonicLoadData
    from ._1374 import StatorToothInterpolator
    from ._1375 import StatorToothLoadInterpolator
    from ._1376 import StatorToothMomentInterpolator
else:
    import_structure = {
        '_1368': ['ElectricMachineHarmonicLoadDataBase'],
        '_1369': ['ForceDisplayOption'],
        '_1370': ['HarmonicLoadDataBase'],
        '_1371': ['HarmonicLoadDataControlExcitationOptionBase'],
        '_1372': ['HarmonicLoadDataType'],
        '_1373': ['SpeedDependentHarmonicLoadData'],
        '_1374': ['StatorToothInterpolator'],
        '_1375': ['StatorToothLoadInterpolator'],
        '_1376': ['StatorToothMomentInterpolator'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
