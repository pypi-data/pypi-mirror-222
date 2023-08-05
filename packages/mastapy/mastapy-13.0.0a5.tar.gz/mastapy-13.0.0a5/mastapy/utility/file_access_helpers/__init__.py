"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1806 import ColumnTitle
    from ._1807 import TextFileDelimiterOptions
else:
    import_structure = {
        '_1806': ['ColumnTitle'],
        '_1807': ['TextFileDelimiterOptions'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
