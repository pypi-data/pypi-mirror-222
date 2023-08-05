"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._953 import WormDesign
    from ._954 import WormGearDesign
    from ._955 import WormGearMeshDesign
    from ._956 import WormGearSetDesign
    from ._957 import WormWheelDesign
else:
    import_structure = {
        '_953': ['WormDesign'],
        '_954': ['WormGearDesign'],
        '_955': ['WormGearMeshDesign'],
        '_956': ['WormGearSetDesign'],
        '_957': ['WormWheelDesign'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
