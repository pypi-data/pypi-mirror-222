"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1089 import CylindricalGearBiasModification
    from ._1090 import CylindricalGearCommonFlankMicroGeometry
    from ._1091 import CylindricalGearFlankMicroGeometry
    from ._1092 import CylindricalGearLeadModification
    from ._1093 import CylindricalGearLeadModificationAtProfilePosition
    from ._1094 import CylindricalGearMeshMicroGeometry
    from ._1095 import CylindricalGearMeshMicroGeometryDutyCycle
    from ._1096 import CylindricalGearMicroGeometry
    from ._1097 import CylindricalGearMicroGeometryBase
    from ._1098 import CylindricalGearMicroGeometryDutyCycle
    from ._1099 import CylindricalGearMicroGeometryMap
    from ._1100 import CylindricalGearMicroGeometryPerTooth
    from ._1101 import CylindricalGearProfileModification
    from ._1102 import CylindricalGearProfileModificationAtFaceWidthPosition
    from ._1103 import CylindricalGearSetMicroGeometry
    from ._1104 import CylindricalGearSetMicroGeometryDutyCycle
    from ._1105 import CylindricalGearToothMicroGeometry
    from ._1106 import CylindricalGearTriangularEndModification
    from ._1107 import CylindricalGearTriangularEndModificationAtOrientation
    from ._1108 import DrawDefiningGearOrBoth
    from ._1109 import GearAlignment
    from ._1110 import LeadFormReliefWithDeviation
    from ._1111 import LeadReliefWithDeviation
    from ._1112 import LeadSlopeReliefWithDeviation
    from ._1113 import LinearCylindricalGearTriangularEndModification
    from ._1114 import MeasuredMapDataTypes
    from ._1115 import MeshAlignment
    from ._1116 import MeshedCylindricalGearFlankMicroGeometry
    from ._1117 import MeshedCylindricalGearMicroGeometry
    from ._1118 import MicroGeometryLeadToleranceChartView
    from ._1119 import MicroGeometryViewingOptions
    from ._1120 import ParabolicCylindricalGearTriangularEndModification
    from ._1121 import ProfileFormReliefWithDeviation
    from ._1122 import ProfileReliefWithDeviation
    from ._1123 import ProfileSlopeReliefWithDeviation
    from ._1124 import ReliefWithDeviation
    from ._1125 import SingleCylindricalGearTriangularEndModification
    from ._1126 import TotalLeadReliefWithDeviation
    from ._1127 import TotalProfileReliefWithDeviation
else:
    import_structure = {
        '_1089': ['CylindricalGearBiasModification'],
        '_1090': ['CylindricalGearCommonFlankMicroGeometry'],
        '_1091': ['CylindricalGearFlankMicroGeometry'],
        '_1092': ['CylindricalGearLeadModification'],
        '_1093': ['CylindricalGearLeadModificationAtProfilePosition'],
        '_1094': ['CylindricalGearMeshMicroGeometry'],
        '_1095': ['CylindricalGearMeshMicroGeometryDutyCycle'],
        '_1096': ['CylindricalGearMicroGeometry'],
        '_1097': ['CylindricalGearMicroGeometryBase'],
        '_1098': ['CylindricalGearMicroGeometryDutyCycle'],
        '_1099': ['CylindricalGearMicroGeometryMap'],
        '_1100': ['CylindricalGearMicroGeometryPerTooth'],
        '_1101': ['CylindricalGearProfileModification'],
        '_1102': ['CylindricalGearProfileModificationAtFaceWidthPosition'],
        '_1103': ['CylindricalGearSetMicroGeometry'],
        '_1104': ['CylindricalGearSetMicroGeometryDutyCycle'],
        '_1105': ['CylindricalGearToothMicroGeometry'],
        '_1106': ['CylindricalGearTriangularEndModification'],
        '_1107': ['CylindricalGearTriangularEndModificationAtOrientation'],
        '_1108': ['DrawDefiningGearOrBoth'],
        '_1109': ['GearAlignment'],
        '_1110': ['LeadFormReliefWithDeviation'],
        '_1111': ['LeadReliefWithDeviation'],
        '_1112': ['LeadSlopeReliefWithDeviation'],
        '_1113': ['LinearCylindricalGearTriangularEndModification'],
        '_1114': ['MeasuredMapDataTypes'],
        '_1115': ['MeshAlignment'],
        '_1116': ['MeshedCylindricalGearFlankMicroGeometry'],
        '_1117': ['MeshedCylindricalGearMicroGeometry'],
        '_1118': ['MicroGeometryLeadToleranceChartView'],
        '_1119': ['MicroGeometryViewingOptions'],
        '_1120': ['ParabolicCylindricalGearTriangularEndModification'],
        '_1121': ['ProfileFormReliefWithDeviation'],
        '_1122': ['ProfileReliefWithDeviation'],
        '_1123': ['ProfileSlopeReliefWithDeviation'],
        '_1124': ['ReliefWithDeviation'],
        '_1125': ['SingleCylindricalGearTriangularEndModification'],
        '_1126': ['TotalLeadReliefWithDeviation'],
        '_1127': ['TotalProfileReliefWithDeviation'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
