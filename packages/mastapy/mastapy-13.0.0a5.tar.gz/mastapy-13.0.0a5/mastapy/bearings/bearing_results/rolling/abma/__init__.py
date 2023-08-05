"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2102 import ANSIABMA112014Results
    from ._2103 import ANSIABMA92015Results
    from ._2104 import ANSIABMAResults
else:
    import_structure = {
        '_2102': ['ANSIABMA112014Results'],
        '_2103': ['ANSIABMA92015Results'],
        '_2104': ['ANSIABMAResults'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
