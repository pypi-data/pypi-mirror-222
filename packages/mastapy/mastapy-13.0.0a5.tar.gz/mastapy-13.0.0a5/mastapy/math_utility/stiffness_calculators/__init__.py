"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1527 import IndividualContactPosition
    from ._1528 import SurfaceToSurfaceContact
else:
    import_structure = {
        '_1527': ['IndividualContactPosition'],
        '_1528': ['SurfaceToSurfaceContact'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
