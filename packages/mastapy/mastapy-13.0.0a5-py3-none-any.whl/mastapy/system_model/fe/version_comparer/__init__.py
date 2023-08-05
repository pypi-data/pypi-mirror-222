"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2395 import DesignResults
    from ._2396 import FESubstructureResults
    from ._2397 import FESubstructureVersionComparer
    from ._2398 import LoadCaseResults
    from ._2399 import LoadCasesToRun
    from ._2400 import NodeComparisonResult
else:
    import_structure = {
        '_2395': ['DesignResults'],
        '_2396': ['FESubstructureResults'],
        '_2397': ['FESubstructureVersionComparer'],
        '_2398': ['LoadCaseResults'],
        '_2399': ['LoadCasesToRun'],
        '_2400': ['NodeComparisonResult'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
