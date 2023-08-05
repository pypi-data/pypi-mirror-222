"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1593 import DegreesMinutesSeconds
    from ._1594 import EnumUnit
    from ._1595 import InverseUnit
    from ._1596 import MeasurementBase
    from ._1597 import MeasurementSettings
    from ._1598 import MeasurementSystem
    from ._1599 import SafetyFactorUnit
    from ._1600 import TimeUnit
    from ._1601 import Unit
    from ._1602 import UnitGradient
else:
    import_structure = {
        '_1593': ['DegreesMinutesSeconds'],
        '_1594': ['EnumUnit'],
        '_1595': ['InverseUnit'],
        '_1596': ['MeasurementBase'],
        '_1597': ['MeasurementSettings'],
        '_1598': ['MeasurementSystem'],
        '_1599': ['SafetyFactorUnit'],
        '_1600': ['TimeUnit'],
        '_1601': ['Unit'],
        '_1602': ['UnitGradient'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
