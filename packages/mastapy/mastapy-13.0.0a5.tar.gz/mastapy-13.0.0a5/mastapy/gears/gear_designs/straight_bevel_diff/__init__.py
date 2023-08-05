"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._962 import StraightBevelDiffGearDesign
    from ._963 import StraightBevelDiffGearMeshDesign
    from ._964 import StraightBevelDiffGearSetDesign
    from ._965 import StraightBevelDiffMeshedGearDesign
else:
    import_structure = {
        '_962': ['StraightBevelDiffGearDesign'],
        '_963': ['StraightBevelDiffGearMeshDesign'],
        '_964': ['StraightBevelDiffGearSetDesign'],
        '_965': ['StraightBevelDiffMeshedGearDesign'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
