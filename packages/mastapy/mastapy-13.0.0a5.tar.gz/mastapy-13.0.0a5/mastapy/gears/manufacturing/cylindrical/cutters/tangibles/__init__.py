"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._720 import CutterShapeDefinition
    from ._721 import CylindricalGearFormedWheelGrinderTangible
    from ._722 import CylindricalGearHobShape
    from ._723 import CylindricalGearShaperTangible
    from ._724 import CylindricalGearShaverTangible
    from ._725 import CylindricalGearWormGrinderShape
    from ._726 import NamedPoint
    from ._727 import RackShape
else:
    import_structure = {
        '_720': ['CutterShapeDefinition'],
        '_721': ['CylindricalGearFormedWheelGrinderTangible'],
        '_722': ['CylindricalGearHobShape'],
        '_723': ['CylindricalGearShaperTangible'],
        '_724': ['CylindricalGearShaverTangible'],
        '_725': ['CylindricalGearWormGrinderShape'],
        '_726': ['NamedPoint'],
        '_727': ['RackShape'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
