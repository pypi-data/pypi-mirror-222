"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1529 import AbstractOptimisable
    from ._1530 import DesignSpaceSearchStrategyDatabase
    from ._1531 import InputSetter
    from ._1532 import MicroGeometryDesignSpaceSearchStrategyDatabase
    from ._1533 import Optimisable
    from ._1534 import OptimisationHistory
    from ._1535 import OptimizationInput
    from ._1536 import OptimizationVariable
    from ._1537 import ParetoOptimisationFilter
    from ._1538 import ParetoOptimisationInput
    from ._1539 import ParetoOptimisationOutput
    from ._1540 import ParetoOptimisationStrategy
    from ._1541 import ParetoOptimisationStrategyBars
    from ._1542 import ParetoOptimisationStrategyChartInformation
    from ._1543 import ParetoOptimisationStrategyDatabase
    from ._1544 import ParetoOptimisationVariable
    from ._1545 import ParetoOptimisationVariableBase
    from ._1546 import PropertyTargetForDominantCandidateSearch
    from ._1547 import ReportingOptimizationInput
    from ._1548 import SpecifyOptimisationInputAs
    from ._1549 import TargetingPropertyTo
else:
    import_structure = {
        '_1529': ['AbstractOptimisable'],
        '_1530': ['DesignSpaceSearchStrategyDatabase'],
        '_1531': ['InputSetter'],
        '_1532': ['MicroGeometryDesignSpaceSearchStrategyDatabase'],
        '_1533': ['Optimisable'],
        '_1534': ['OptimisationHistory'],
        '_1535': ['OptimizationInput'],
        '_1536': ['OptimizationVariable'],
        '_1537': ['ParetoOptimisationFilter'],
        '_1538': ['ParetoOptimisationInput'],
        '_1539': ['ParetoOptimisationOutput'],
        '_1540': ['ParetoOptimisationStrategy'],
        '_1541': ['ParetoOptimisationStrategyBars'],
        '_1542': ['ParetoOptimisationStrategyChartInformation'],
        '_1543': ['ParetoOptimisationStrategyDatabase'],
        '_1544': ['ParetoOptimisationVariable'],
        '_1545': ['ParetoOptimisationVariableBase'],
        '_1546': ['PropertyTargetForDominantCandidateSearch'],
        '_1547': ['ReportingOptimizationInput'],
        '_1548': ['SpecifyOptimisationInputAs'],
        '_1549': ['TargetingPropertyTo'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
