"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1556 import GriddedSurfaceAccessor
    from ._1557 import LookupTableBase
    from ._1558 import OnedimensionalFunctionLookupTable
    from ._1559 import TwodimensionalFunctionLookupTable
else:
    import_structure = {
        '_1556': ['GriddedSurfaceAccessor'],
        '_1557': ['LookupTableBase'],
        '_1558': ['OnedimensionalFunctionLookupTable'],
        '_1559': ['TwodimensionalFunctionLookupTable'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
