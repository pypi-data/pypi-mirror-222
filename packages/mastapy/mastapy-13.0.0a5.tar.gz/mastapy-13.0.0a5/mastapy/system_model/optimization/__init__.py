"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2213 import ConicalGearOptimisationStrategy
    from ._2214 import ConicalGearOptimizationStep
    from ._2215 import ConicalGearOptimizationStrategyDatabase
    from ._2216 import CylindricalGearOptimisationStrategy
    from ._2217 import CylindricalGearOptimizationStep
    from ._2218 import CylindricalGearSetOptimizer
    from ._2219 import MeasuredAndFactorViewModel
    from ._2220 import MicroGeometryOptimisationTarget
    from ._2221 import OptimizationStep
    from ._2222 import OptimizationStrategy
    from ._2223 import OptimizationStrategyBase
    from ._2224 import OptimizationStrategyDatabase
else:
    import_structure = {
        '_2213': ['ConicalGearOptimisationStrategy'],
        '_2214': ['ConicalGearOptimizationStep'],
        '_2215': ['ConicalGearOptimizationStrategyDatabase'],
        '_2216': ['CylindricalGearOptimisationStrategy'],
        '_2217': ['CylindricalGearOptimizationStep'],
        '_2218': ['CylindricalGearSetOptimizer'],
        '_2219': ['MeasuredAndFactorViewModel'],
        '_2220': ['MicroGeometryOptimisationTarget'],
        '_2221': ['OptimizationStep'],
        '_2222': ['OptimizationStrategy'],
        '_2223': ['OptimizationStrategyBase'],
        '_2224': ['OptimizationStrategyDatabase'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
