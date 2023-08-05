"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2465 import Shaft
    from ._2466 import ShaftBow
else:
    import_structure = {
        '_2465': ['Shaft'],
        '_2466': ['ShaftBow'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
