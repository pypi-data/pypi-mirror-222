"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._551 import BevelGearMeshRating
    from ._552 import BevelGearRating
    from ._553 import BevelGearSetRating
else:
    import_structure = {
        '_551': ['BevelGearMeshRating'],
        '_552': ['BevelGearRating'],
        '_553': ['BevelGearSetRating'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
