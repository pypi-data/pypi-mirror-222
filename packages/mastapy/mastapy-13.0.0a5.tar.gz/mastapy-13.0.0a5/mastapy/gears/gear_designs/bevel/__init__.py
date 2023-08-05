"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1175 import AGMAGleasonConicalGearGeometryMethods
    from ._1176 import BevelGearDesign
    from ._1177 import BevelGearMeshDesign
    from ._1178 import BevelGearSetDesign
    from ._1179 import BevelMeshedGearDesign
    from ._1180 import DrivenMachineCharacteristicGleason
    from ._1181 import EdgeRadiusType
    from ._1182 import FinishingMethods
    from ._1183 import MachineCharacteristicAGMAKlingelnberg
    from ._1184 import PrimeMoverCharacteristicGleason
    from ._1185 import ToothProportionsInputMethod
    from ._1186 import ToothThicknessSpecificationMethod
    from ._1187 import WheelFinishCutterPointWidthRestrictionMethod
else:
    import_structure = {
        '_1175': ['AGMAGleasonConicalGearGeometryMethods'],
        '_1176': ['BevelGearDesign'],
        '_1177': ['BevelGearMeshDesign'],
        '_1178': ['BevelGearSetDesign'],
        '_1179': ['BevelMeshedGearDesign'],
        '_1180': ['DrivenMachineCharacteristicGleason'],
        '_1181': ['EdgeRadiusType'],
        '_1182': ['FinishingMethods'],
        '_1183': ['MachineCharacteristicAGMAKlingelnberg'],
        '_1184': ['PrimeMoverCharacteristicGleason'],
        '_1185': ['ToothProportionsInputMethod'],
        '_1186': ['ToothThicknessSpecificationMethod'],
        '_1187': ['WheelFinishCutterPointWidthRestrictionMethod'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
