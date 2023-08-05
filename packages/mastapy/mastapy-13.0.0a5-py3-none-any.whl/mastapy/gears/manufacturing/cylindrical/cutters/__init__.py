"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._700 import CurveInLinkedList
    from ._701 import CustomisableEdgeProfile
    from ._702 import CylindricalFormedWheelGrinderDatabase
    from ._703 import CylindricalGearAbstractCutterDesign
    from ._704 import CylindricalGearFormGrindingWheel
    from ._705 import CylindricalGearGrindingWorm
    from ._706 import CylindricalGearHobDesign
    from ._707 import CylindricalGearPlungeShaver
    from ._708 import CylindricalGearPlungeShaverDatabase
    from ._709 import CylindricalGearRackDesign
    from ._710 import CylindricalGearRealCutterDesign
    from ._711 import CylindricalGearShaper
    from ._712 import CylindricalGearShaver
    from ._713 import CylindricalGearShaverDatabase
    from ._714 import CylindricalWormGrinderDatabase
    from ._715 import InvoluteCutterDesign
    from ._716 import MutableCommon
    from ._717 import MutableCurve
    from ._718 import MutableFillet
    from ._719 import RoughCutterCreationSettings
else:
    import_structure = {
        '_700': ['CurveInLinkedList'],
        '_701': ['CustomisableEdgeProfile'],
        '_702': ['CylindricalFormedWheelGrinderDatabase'],
        '_703': ['CylindricalGearAbstractCutterDesign'],
        '_704': ['CylindricalGearFormGrindingWheel'],
        '_705': ['CylindricalGearGrindingWorm'],
        '_706': ['CylindricalGearHobDesign'],
        '_707': ['CylindricalGearPlungeShaver'],
        '_708': ['CylindricalGearPlungeShaverDatabase'],
        '_709': ['CylindricalGearRackDesign'],
        '_710': ['CylindricalGearRealCutterDesign'],
        '_711': ['CylindricalGearShaper'],
        '_712': ['CylindricalGearShaver'],
        '_713': ['CylindricalGearShaverDatabase'],
        '_714': ['CylindricalWormGrinderDatabase'],
        '_715': ['InvoluteCutterDesign'],
        '_716': ['MutableCommon'],
        '_717': ['MutableCurve'],
        '_718': ['MutableFillet'],
        '_719': ['RoughCutterCreationSettings'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
