"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1433 import AssemblyMethods
    from ._1434 import CalculationMethods
    from ._1435 import InterferenceFitDesign
    from ._1436 import InterferenceFitHalfDesign
    from ._1437 import StressRegions
    from ._1438 import Table4JointInterfaceTypes
else:
    import_structure = {
        '_1433': ['AssemblyMethods'],
        '_1434': ['CalculationMethods'],
        '_1435': ['InterferenceFitDesign'],
        '_1436': ['InterferenceFitHalfDesign'],
        '_1437': ['StressRegions'],
        '_1438': ['Table4JointInterfaceTypes'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
