"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1813 import Database
    from ._1814 import DatabaseConnectionSettings
    from ._1815 import DatabaseKey
    from ._1816 import DatabaseSettings
    from ._1817 import NamedDatabase
    from ._1818 import NamedDatabaseItem
    from ._1819 import NamedKey
    from ._1820 import SQLDatabase
else:
    import_structure = {
        '_1813': ['Database'],
        '_1814': ['DatabaseConnectionSettings'],
        '_1815': ['DatabaseKey'],
        '_1816': ['DatabaseSettings'],
        '_1817': ['NamedDatabase'],
        '_1818': ['NamedDatabaseItem'],
        '_1819': ['NamedKey'],
        '_1820': ['SQLDatabase'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
