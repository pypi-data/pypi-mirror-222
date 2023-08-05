"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1835 import ColumnInputOptions
    from ._1836 import DataInputFileOptions
    from ._1837 import DataLoggerItem
    from ._1838 import DataLoggerWithCharts
    from ._1839 import ScalingDrawStyle
else:
    import_structure = {
        '_1835': ['ColumnInputOptions'],
        '_1836': ['DataInputFileOptions'],
        '_1837': ['DataLoggerItem'],
        '_1838': ['DataLoggerWithCharts'],
        '_1839': ['ScalingDrawStyle'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
