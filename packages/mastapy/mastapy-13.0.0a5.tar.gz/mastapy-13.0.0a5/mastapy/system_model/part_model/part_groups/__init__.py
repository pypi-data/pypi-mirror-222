"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2469 import ConcentricOrParallelPartGroup
    from ._2470 import ConcentricPartGroup
    from ._2471 import ConcentricPartGroupParallelToThis
    from ._2472 import DesignMeasurements
    from ._2473 import ParallelPartGroup
    from ._2474 import PartGroup
else:
    import_structure = {
        '_2469': ['ConcentricOrParallelPartGroup'],
        '_2470': ['ConcentricPartGroup'],
        '_2471': ['ConcentricPartGroupParallelToThis'],
        '_2472': ['DesignMeasurements'],
        '_2473': ['ParallelPartGroup'],
        '_2474': ['PartGroup'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
