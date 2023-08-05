"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2475 import AbstractShaftFromCAD
    from ._2476 import ClutchFromCAD
    from ._2477 import ComponentFromCAD
    from ._2478 import ConceptBearingFromCAD
    from ._2479 import ConnectorFromCAD
    from ._2480 import CylindricalGearFromCAD
    from ._2481 import CylindricalGearInPlanetarySetFromCAD
    from ._2482 import CylindricalPlanetGearFromCAD
    from ._2483 import CylindricalRingGearFromCAD
    from ._2484 import CylindricalSunGearFromCAD
    from ._2485 import HousedOrMounted
    from ._2486 import MountableComponentFromCAD
    from ._2487 import PlanetShaftFromCAD
    from ._2488 import PulleyFromCAD
    from ._2489 import RigidConnectorFromCAD
    from ._2490 import RollingBearingFromCAD
    from ._2491 import ShaftFromCAD
else:
    import_structure = {
        '_2475': ['AbstractShaftFromCAD'],
        '_2476': ['ClutchFromCAD'],
        '_2477': ['ComponentFromCAD'],
        '_2478': ['ConceptBearingFromCAD'],
        '_2479': ['ConnectorFromCAD'],
        '_2480': ['CylindricalGearFromCAD'],
        '_2481': ['CylindricalGearInPlanetarySetFromCAD'],
        '_2482': ['CylindricalPlanetGearFromCAD'],
        '_2483': ['CylindricalRingGearFromCAD'],
        '_2484': ['CylindricalSunGearFromCAD'],
        '_2485': ['HousedOrMounted'],
        '_2486': ['MountableComponentFromCAD'],
        '_2487': ['PlanetShaftFromCAD'],
        '_2488': ['PulleyFromCAD'],
        '_2489': ['RigidConnectorFromCAD'],
        '_2490': ['RollingBearingFromCAD'],
        '_2491': ['ShaftFromCAD'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
