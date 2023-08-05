"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2248 import AbstractShaftToMountableComponentConnection
    from ._2249 import BearingInnerSocket
    from ._2250 import BearingOuterSocket
    from ._2251 import BeltConnection
    from ._2252 import CoaxialConnection
    from ._2253 import ComponentConnection
    from ._2254 import ComponentMeasurer
    from ._2255 import Connection
    from ._2256 import CVTBeltConnection
    from ._2257 import CVTPulleySocket
    from ._2258 import CylindricalComponentConnection
    from ._2259 import CylindricalSocket
    from ._2260 import DatumMeasurement
    from ._2261 import ElectricMachineStatorSocket
    from ._2262 import InnerShaftSocket
    from ._2263 import InnerShaftSocketBase
    from ._2264 import InterMountableComponentConnection
    from ._2265 import MountableComponentInnerSocket
    from ._2266 import MountableComponentOuterSocket
    from ._2267 import MountableComponentSocket
    from ._2268 import OuterShaftSocket
    from ._2269 import OuterShaftSocketBase
    from ._2270 import PlanetaryConnection
    from ._2271 import PlanetarySocket
    from ._2272 import PlanetarySocketBase
    from ._2273 import PulleySocket
    from ._2274 import RealignmentResult
    from ._2275 import RollingRingConnection
    from ._2276 import RollingRingSocket
    from ._2277 import ShaftSocket
    from ._2278 import ShaftToMountableComponentConnection
    from ._2279 import Socket
    from ._2280 import SocketConnectionOptions
    from ._2281 import SocketConnectionSelection
else:
    import_structure = {
        '_2248': ['AbstractShaftToMountableComponentConnection'],
        '_2249': ['BearingInnerSocket'],
        '_2250': ['BearingOuterSocket'],
        '_2251': ['BeltConnection'],
        '_2252': ['CoaxialConnection'],
        '_2253': ['ComponentConnection'],
        '_2254': ['ComponentMeasurer'],
        '_2255': ['Connection'],
        '_2256': ['CVTBeltConnection'],
        '_2257': ['CVTPulleySocket'],
        '_2258': ['CylindricalComponentConnection'],
        '_2259': ['CylindricalSocket'],
        '_2260': ['DatumMeasurement'],
        '_2261': ['ElectricMachineStatorSocket'],
        '_2262': ['InnerShaftSocket'],
        '_2263': ['InnerShaftSocketBase'],
        '_2264': ['InterMountableComponentConnection'],
        '_2265': ['MountableComponentInnerSocket'],
        '_2266': ['MountableComponentOuterSocket'],
        '_2267': ['MountableComponentSocket'],
        '_2268': ['OuterShaftSocket'],
        '_2269': ['OuterShaftSocketBase'],
        '_2270': ['PlanetaryConnection'],
        '_2271': ['PlanetarySocket'],
        '_2272': ['PlanetarySocketBase'],
        '_2273': ['PulleySocket'],
        '_2274': ['RealignmentResult'],
        '_2275': ['RollingRingConnection'],
        '_2276': ['RollingRingSocket'],
        '_2277': ['ShaftSocket'],
        '_2278': ['ShaftToMountableComponentConnection'],
        '_2279': ['Socket'],
        '_2280': ['SocketConnectionOptions'],
        '_2281': ['SocketConnectionSelection'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
