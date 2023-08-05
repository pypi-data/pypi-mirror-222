"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1782 import Fix
    from ._1783 import Severity
    from ._1784 import Status
    from ._1785 import StatusItem
    from ._1786 import StatusItemSeverity
else:
    import_structure = {
        '_1782': ['Fix'],
        '_1783': ['Severity'],
        '_1784': ['Status'],
        '_1785': ['StatusItem'],
        '_1786': ['StatusItemSeverity'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
