"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._529 import DIN3990GearSingleFlankRating
    from ._530 import DIN3990MeshSingleFlankRating
else:
    import_structure = {
        '_529': ['DIN3990GearSingleFlankRating'],
        '_530': ['DIN3990MeshSingleFlankRating'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
