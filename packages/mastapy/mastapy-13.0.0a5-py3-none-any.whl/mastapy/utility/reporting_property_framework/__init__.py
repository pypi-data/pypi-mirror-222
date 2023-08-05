"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1779 import CellValuePosition
    from ._1780 import CustomChartType
else:
    import_structure = {
        '_1779': ['CellValuePosition'],
        '_1780': ['CustomChartType'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
