"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1237 import ElementPropertyClass
    from ._1238 import MaterialPropertyClass
else:
    import_structure = {
        '_1237': ['ElementPropertyClass'],
        '_1238': ['MaterialPropertyClass'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
