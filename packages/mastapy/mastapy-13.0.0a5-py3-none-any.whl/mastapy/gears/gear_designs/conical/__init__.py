"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1146 import ActiveConicalFlank
    from ._1147 import BacklashDistributionRule
    from ._1148 import ConicalFlanks
    from ._1149 import ConicalGearCutter
    from ._1150 import ConicalGearDesign
    from ._1151 import ConicalGearMeshDesign
    from ._1152 import ConicalGearSetDesign
    from ._1153 import ConicalMachineSettingCalculationMethods
    from ._1154 import ConicalManufactureMethods
    from ._1155 import ConicalMeshedGearDesign
    from ._1156 import ConicalMeshMisalignments
    from ._1157 import CutterBladeType
    from ._1158 import CutterGaugeLengths
    from ._1159 import DummyConicalGearCutter
    from ._1160 import FrontEndTypes
    from ._1161 import GleasonSafetyRequirements
    from ._1162 import KIMoSBevelHypoidSingleLoadCaseResultsData
    from ._1163 import KIMoSBevelHypoidSingleRotationAngleResult
    from ._1164 import KlingelnbergFinishingMethods
    from ._1165 import LoadDistributionFactorMethods
    from ._1166 import TopremEntryType
    from ._1167 import TopremLetter
else:
    import_structure = {
        '_1146': ['ActiveConicalFlank'],
        '_1147': ['BacklashDistributionRule'],
        '_1148': ['ConicalFlanks'],
        '_1149': ['ConicalGearCutter'],
        '_1150': ['ConicalGearDesign'],
        '_1151': ['ConicalGearMeshDesign'],
        '_1152': ['ConicalGearSetDesign'],
        '_1153': ['ConicalMachineSettingCalculationMethods'],
        '_1154': ['ConicalManufactureMethods'],
        '_1155': ['ConicalMeshedGearDesign'],
        '_1156': ['ConicalMeshMisalignments'],
        '_1157': ['CutterBladeType'],
        '_1158': ['CutterGaugeLengths'],
        '_1159': ['DummyConicalGearCutter'],
        '_1160': ['FrontEndTypes'],
        '_1161': ['GleasonSafetyRequirements'],
        '_1162': ['KIMoSBevelHypoidSingleLoadCaseResultsData'],
        '_1163': ['KIMoSBevelHypoidSingleRotationAngleResult'],
        '_1164': ['KlingelnbergFinishingMethods'],
        '_1165': ['LoadDistributionFactorMethods'],
        '_1166': ['TopremEntryType'],
        '_1167': ['TopremLetter'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
