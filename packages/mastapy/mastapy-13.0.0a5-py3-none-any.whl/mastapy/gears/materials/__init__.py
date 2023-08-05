"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._580 import AGMACylindricalGearMaterial
    from ._581 import BevelGearAbstractMaterialDatabase
    from ._582 import BevelGearISOMaterial
    from ._583 import BevelGearISOMaterialDatabase
    from ._584 import BevelGearMaterial
    from ._585 import BevelGearMaterialDatabase
    from ._586 import CylindricalGearAGMAMaterialDatabase
    from ._587 import CylindricalGearISOMaterialDatabase
    from ._588 import CylindricalGearMaterial
    from ._589 import CylindricalGearMaterialDatabase
    from ._590 import CylindricalGearPlasticMaterialDatabase
    from ._591 import GearMaterial
    from ._592 import GearMaterialDatabase
    from ._593 import GearMaterialExpertSystemFactorSettings
    from ._594 import ISOCylindricalGearMaterial
    from ._595 import ISOTR1417912001CoefficientOfFrictionConstants
    from ._596 import ISOTR1417912001CoefficientOfFrictionConstantsDatabase
    from ._597 import KlingelnbergConicalGearMaterialDatabase
    from ._598 import KlingelnbergCycloPalloidConicalGearMaterial
    from ._599 import ManufactureRating
    from ._600 import PlasticCylindricalGearMaterial
    from ._601 import PlasticSNCurve
    from ._602 import RatingMethods
    from ._603 import RawMaterial
    from ._604 import RawMaterialDatabase
    from ._605 import SNCurveDefinition
else:
    import_structure = {
        '_580': ['AGMACylindricalGearMaterial'],
        '_581': ['BevelGearAbstractMaterialDatabase'],
        '_582': ['BevelGearISOMaterial'],
        '_583': ['BevelGearISOMaterialDatabase'],
        '_584': ['BevelGearMaterial'],
        '_585': ['BevelGearMaterialDatabase'],
        '_586': ['CylindricalGearAGMAMaterialDatabase'],
        '_587': ['CylindricalGearISOMaterialDatabase'],
        '_588': ['CylindricalGearMaterial'],
        '_589': ['CylindricalGearMaterialDatabase'],
        '_590': ['CylindricalGearPlasticMaterialDatabase'],
        '_591': ['GearMaterial'],
        '_592': ['GearMaterialDatabase'],
        '_593': ['GearMaterialExpertSystemFactorSettings'],
        '_594': ['ISOCylindricalGearMaterial'],
        '_595': ['ISOTR1417912001CoefficientOfFrictionConstants'],
        '_596': ['ISOTR1417912001CoefficientOfFrictionConstantsDatabase'],
        '_597': ['KlingelnbergConicalGearMaterialDatabase'],
        '_598': ['KlingelnbergCycloPalloidConicalGearMaterial'],
        '_599': ['ManufactureRating'],
        '_600': ['PlasticCylindricalGearMaterial'],
        '_601': ['PlasticSNCurve'],
        '_602': ['RatingMethods'],
        '_603': ['RawMaterial'],
        '_604': ['RawMaterialDatabase'],
        '_605': ['SNCurveDefinition'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
