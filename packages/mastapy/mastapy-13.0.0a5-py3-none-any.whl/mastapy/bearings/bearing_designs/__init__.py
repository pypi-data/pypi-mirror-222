"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2117 import BearingDesign
    from ._2118 import DetailedBearing
    from ._2119 import DummyRollingBearing
    from ._2120 import LinearBearing
    from ._2121 import NonLinearBearing
else:
    import_structure = {
        '_2117': ['BearingDesign'],
        '_2118': ['DetailedBearing'],
        '_2119': ['DummyRollingBearing'],
        '_2120': ['LinearBearing'],
        '_2121': ['NonLinearBearing'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
