"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1142 import CylindricalGearPairCreationOptions
    from ._1143 import GearSetCreationOptions
    from ._1144 import HypoidGearSetCreationOptions
    from ._1145 import SpiralBevelGearSetCreationOptions
else:
    import_structure = {
        '_1142': ['CylindricalGearPairCreationOptions'],
        '_1143': ['GearSetCreationOptions'],
        '_1144': ['HypoidGearSetCreationOptions'],
        '_1145': ['SpiralBevelGearSetCreationOptions'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
