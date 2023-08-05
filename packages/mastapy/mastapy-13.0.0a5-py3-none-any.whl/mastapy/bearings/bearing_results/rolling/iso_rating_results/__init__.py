"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2088 import BallISO2812007Results
    from ._2089 import BallISOTS162812008Results
    from ._2090 import ISO2812007Results
    from ._2091 import ISO762006Results
    from ._2092 import ISOResults
    from ._2093 import ISOTS162812008Results
    from ._2094 import RollerISO2812007Results
    from ._2095 import RollerISOTS162812008Results
    from ._2096 import StressConcentrationMethod
else:
    import_structure = {
        '_2088': ['BallISO2812007Results'],
        '_2089': ['BallISOTS162812008Results'],
        '_2090': ['ISO2812007Results'],
        '_2091': ['ISO762006Results'],
        '_2092': ['ISOResults'],
        '_2093': ['ISOTS162812008Results'],
        '_2094': ['RollerISO2812007Results'],
        '_2095': ['RollerISOTS162812008Results'],
        '_2096': ['StressConcentrationMethod'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
