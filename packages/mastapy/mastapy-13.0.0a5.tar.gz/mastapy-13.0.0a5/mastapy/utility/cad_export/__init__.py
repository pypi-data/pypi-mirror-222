"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1821 import CADExportSettings
    from ._1822 import StockDrawings
else:
    import_structure = {
        '_1821': ['CADExportSettings'],
        '_1822': ['StockDrawings'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
