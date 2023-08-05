"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1799 import NamedTuple1
    from ._1800 import NamedTuple2
    from ._1801 import NamedTuple3
    from ._1802 import NamedTuple4
    from ._1803 import NamedTuple5
    from ._1804 import NamedTuple6
    from ._1805 import NamedTuple7
else:
    import_structure = {
        '_1799': ['NamedTuple1'],
        '_1800': ['NamedTuple2'],
        '_1801': ['NamedTuple3'],
        '_1802': ['NamedTuple4'],
        '_1803': ['NamedTuple5'],
        '_1804': ['NamedTuple6'],
        '_1805': ['NamedTuple7'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
