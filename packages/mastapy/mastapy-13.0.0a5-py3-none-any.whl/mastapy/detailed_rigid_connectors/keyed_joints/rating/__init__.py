"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1431 import KeywayHalfRating
    from ._1432 import KeywayRating
else:
    import_structure = {
        '_1431': ['KeywayHalfRating'],
        '_1432': ['KeywayRating'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
