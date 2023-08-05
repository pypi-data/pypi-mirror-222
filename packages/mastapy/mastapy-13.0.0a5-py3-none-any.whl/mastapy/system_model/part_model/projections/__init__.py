"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2467 import SpecifiedConcentricPartGroupDrawingOrder
    from ._2468 import SpecifiedParallelPartGroupDrawingOrder
else:
    import_structure = {
        '_2467': ['SpecifiedConcentricPartGroupDrawingOrder'],
        '_2468': ['SpecifiedParallelPartGroupDrawingOrder'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
