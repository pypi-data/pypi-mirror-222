"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._505 import CylindricalGearToothFatigueFractureResults
    from ._506 import CylindricalGearToothFatigueFractureResultsN1457
    from ._507 import HelicalGearMicroGeometryOption
    from ._508 import ISO63361996GearSingleFlankRating
    from ._509 import ISO63361996MeshSingleFlankRating
    from ._510 import ISO63362006GearSingleFlankRating
    from ._511 import ISO63362006MeshSingleFlankRating
    from ._512 import ISO63362019GearSingleFlankRating
    from ._513 import ISO63362019MeshSingleFlankRating
    from ._514 import ISO6336AbstractGearSingleFlankRating
    from ._515 import ISO6336AbstractMeshSingleFlankRating
    from ._516 import ISO6336AbstractMetalGearSingleFlankRating
    from ._517 import ISO6336AbstractMetalMeshSingleFlankRating
    from ._518 import ISO6336MeanStressInfluenceFactor
    from ._519 import ISO6336MetalRateableMesh
    from ._520 import ISO6336RateableMesh
    from ._521 import ToothFlankFractureAnalysisContactPoint
    from ._522 import ToothFlankFractureAnalysisContactPointCommon
    from ._523 import ToothFlankFractureAnalysisContactPointMethodA
    from ._524 import ToothFlankFractureAnalysisContactPointN1457
    from ._525 import ToothFlankFractureAnalysisPoint
    from ._526 import ToothFlankFractureAnalysisPointN1457
    from ._527 import ToothFlankFractureAnalysisRowN1457
    from ._528 import ToothFlankFractureStressStepAtAnalysisPointN1457
else:
    import_structure = {
        '_505': ['CylindricalGearToothFatigueFractureResults'],
        '_506': ['CylindricalGearToothFatigueFractureResultsN1457'],
        '_507': ['HelicalGearMicroGeometryOption'],
        '_508': ['ISO63361996GearSingleFlankRating'],
        '_509': ['ISO63361996MeshSingleFlankRating'],
        '_510': ['ISO63362006GearSingleFlankRating'],
        '_511': ['ISO63362006MeshSingleFlankRating'],
        '_512': ['ISO63362019GearSingleFlankRating'],
        '_513': ['ISO63362019MeshSingleFlankRating'],
        '_514': ['ISO6336AbstractGearSingleFlankRating'],
        '_515': ['ISO6336AbstractMeshSingleFlankRating'],
        '_516': ['ISO6336AbstractMetalGearSingleFlankRating'],
        '_517': ['ISO6336AbstractMetalMeshSingleFlankRating'],
        '_518': ['ISO6336MeanStressInfluenceFactor'],
        '_519': ['ISO6336MetalRateableMesh'],
        '_520': ['ISO6336RateableMesh'],
        '_521': ['ToothFlankFractureAnalysisContactPoint'],
        '_522': ['ToothFlankFractureAnalysisContactPointCommon'],
        '_523': ['ToothFlankFractureAnalysisContactPointMethodA'],
        '_524': ['ToothFlankFractureAnalysisContactPointN1457'],
        '_525': ['ToothFlankFractureAnalysisPoint'],
        '_526': ['ToothFlankFractureAnalysisPointN1457'],
        '_527': ['ToothFlankFractureAnalysisRowN1457'],
        '_528': ['ToothFlankFractureStressStepAtAnalysisPointN1457'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
