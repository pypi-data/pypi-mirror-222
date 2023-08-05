"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._487 import MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating
    from ._488 import PlasticGearVDI2736AbstractGearSingleFlankRating
    from ._489 import PlasticGearVDI2736AbstractMeshSingleFlankRating
    from ._490 import PlasticGearVDI2736AbstractRateableMesh
    from ._491 import PlasticPlasticVDI2736MeshSingleFlankRating
    from ._492 import PlasticSNCurveForTheSpecifiedOperatingConditions
    from ._493 import PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh
    from ._494 import PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh
    from ._495 import VDI2736MetalPlasticRateableMesh
    from ._496 import VDI2736PlasticMetalRateableMesh
    from ._497 import VDI2736PlasticPlasticRateableMesh
else:
    import_structure = {
        '_487': ['MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating'],
        '_488': ['PlasticGearVDI2736AbstractGearSingleFlankRating'],
        '_489': ['PlasticGearVDI2736AbstractMeshSingleFlankRating'],
        '_490': ['PlasticGearVDI2736AbstractRateableMesh'],
        '_491': ['PlasticPlasticVDI2736MeshSingleFlankRating'],
        '_492': ['PlasticSNCurveForTheSpecifiedOperatingConditions'],
        '_493': ['PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh'],
        '_494': ['PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh'],
        '_495': ['VDI2736MetalPlasticRateableMesh'],
        '_496': ['VDI2736PlasticMetalRateableMesh'],
        '_497': ['VDI2736PlasticPlasticRateableMesh'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
