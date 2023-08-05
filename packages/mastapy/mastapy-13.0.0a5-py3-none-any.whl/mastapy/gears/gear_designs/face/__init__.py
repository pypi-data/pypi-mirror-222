"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._986 import FaceGearDesign
    from ._987 import FaceGearDiameterFaceWidthSpecificationMethod
    from ._988 import FaceGearMeshDesign
    from ._989 import FaceGearMeshMicroGeometry
    from ._990 import FaceGearMicroGeometry
    from ._991 import FaceGearPinionDesign
    from ._992 import FaceGearSetDesign
    from ._993 import FaceGearSetMicroGeometry
    from ._994 import FaceGearWheelDesign
else:
    import_structure = {
        '_986': ['FaceGearDesign'],
        '_987': ['FaceGearDiameterFaceWidthSpecificationMethod'],
        '_988': ['FaceGearMeshDesign'],
        '_989': ['FaceGearMeshMicroGeometry'],
        '_990': ['FaceGearMicroGeometry'],
        '_991': ['FaceGearPinionDesign'],
        '_992': ['FaceGearSetDesign'],
        '_993': ['FaceGearSetMicroGeometry'],
        '_994': ['FaceGearWheelDesign'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
