"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1235 import ProSolveMpcType
    from ._1236 import ProSolveSolverType
else:
    import_structure = {
        '_1235': ['ProSolveMpcType'],
        '_1236': ['ProSolveSolverType'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
