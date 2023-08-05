"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1455 import AxialLoadType
    from ._1456 import BoltedJointMaterial
    from ._1457 import BoltedJointMaterialDatabase
    from ._1458 import BoltGeometry
    from ._1459 import BoltGeometryDatabase
    from ._1460 import BoltMaterial
    from ._1461 import BoltMaterialDatabase
    from ._1462 import BoltSection
    from ._1463 import BoltShankType
    from ._1464 import BoltTypes
    from ._1465 import ClampedSection
    from ._1466 import ClampedSectionMaterialDatabase
    from ._1467 import DetailedBoltDesign
    from ._1468 import DetailedBoltedJointDesign
    from ._1469 import HeadCapTypes
    from ._1470 import JointGeometries
    from ._1471 import JointTypes
    from ._1472 import LoadedBolt
    from ._1473 import RolledBeforeOrAfterHeatTreatment
    from ._1474 import StandardSizes
    from ._1475 import StrengthGrades
    from ._1476 import ThreadTypes
    from ._1477 import TighteningTechniques
else:
    import_structure = {
        '_1455': ['AxialLoadType'],
        '_1456': ['BoltedJointMaterial'],
        '_1457': ['BoltedJointMaterialDatabase'],
        '_1458': ['BoltGeometry'],
        '_1459': ['BoltGeometryDatabase'],
        '_1460': ['BoltMaterial'],
        '_1461': ['BoltMaterialDatabase'],
        '_1462': ['BoltSection'],
        '_1463': ['BoltShankType'],
        '_1464': ['BoltTypes'],
        '_1465': ['ClampedSection'],
        '_1466': ['ClampedSectionMaterialDatabase'],
        '_1467': ['DetailedBoltDesign'],
        '_1468': ['DetailedBoltedJointDesign'],
        '_1469': ['HeadCapTypes'],
        '_1470': ['JointGeometries'],
        '_1471': ['JointTypes'],
        '_1472': ['LoadedBolt'],
        '_1473': ['RolledBeforeOrAfterHeatTreatment'],
        '_1474': ['StandardSizes'],
        '_1475': ['StrengthGrades'],
        '_1476': ['ThreadTypes'],
        '_1477': ['TighteningTechniques'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
