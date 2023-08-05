"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2316 import CycloidalDiscAxialLeftSocket
    from ._2317 import CycloidalDiscAxialRightSocket
    from ._2318 import CycloidalDiscCentralBearingConnection
    from ._2319 import CycloidalDiscInnerSocket
    from ._2320 import CycloidalDiscOuterSocket
    from ._2321 import CycloidalDiscPlanetaryBearingConnection
    from ._2322 import CycloidalDiscPlanetaryBearingSocket
    from ._2323 import RingPinsSocket
    from ._2324 import RingPinsToDiscConnection
else:
    import_structure = {
        '_2316': ['CycloidalDiscAxialLeftSocket'],
        '_2317': ['CycloidalDiscAxialRightSocket'],
        '_2318': ['CycloidalDiscCentralBearingConnection'],
        '_2319': ['CycloidalDiscInnerSocket'],
        '_2320': ['CycloidalDiscOuterSocket'],
        '_2321': ['CycloidalDiscPlanetaryBearingConnection'],
        '_2322': ['CycloidalDiscPlanetaryBearingSocket'],
        '_2323': ['RingPinsSocket'],
        '_2324': ['RingPinsToDiscConnection'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
