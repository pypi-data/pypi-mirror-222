"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._966 import SpiralBevelGearDesign
    from ._967 import SpiralBevelGearMeshDesign
    from ._968 import SpiralBevelGearSetDesign
    from ._969 import SpiralBevelMeshedGearDesign
else:
    import_structure = {
        '_966': ['SpiralBevelGearDesign'],
        '_967': ['SpiralBevelGearMeshDesign'],
        '_968': ['SpiralBevelGearSetDesign'],
        '_969': ['SpiralBevelMeshedGearDesign'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
