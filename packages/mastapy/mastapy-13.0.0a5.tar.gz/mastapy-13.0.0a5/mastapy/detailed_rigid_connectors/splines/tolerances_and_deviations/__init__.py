"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1411 import FitAndTolerance
    from ._1412 import SAESplineTolerances
else:
    import_structure = {
        '_1411': ['FitAndTolerance'],
        '_1412': ['SAESplineTolerances'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
