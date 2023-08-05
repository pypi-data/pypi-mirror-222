"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2824 import CylindricalGearMeshMisalignmentValue
    from ._2825 import FlexibleGearChart
    from ._2826 import GearInMeshDeflectionResults
    from ._2827 import MeshDeflectionResults
    from ._2828 import PlanetCarrierWindup
    from ._2829 import PlanetPinWindup
    from ._2830 import RigidlyConnectedComponentGroupSystemDeflection
    from ._2831 import ShaftSystemDeflectionSectionsReport
    from ._2832 import SplineFlankContactReporting
else:
    import_structure = {
        '_2824': ['CylindricalGearMeshMisalignmentValue'],
        '_2825': ['FlexibleGearChart'],
        '_2826': ['GearInMeshDeflectionResults'],
        '_2827': ['MeshDeflectionResults'],
        '_2828': ['PlanetCarrierWindup'],
        '_2829': ['PlanetPinWindup'],
        '_2830': ['RigidlyConnectedComponentGroupSystemDeflection'],
        '_2831': ['ShaftSystemDeflectionSectionsReport'],
        '_2832': ['SplineFlankContactReporting'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
