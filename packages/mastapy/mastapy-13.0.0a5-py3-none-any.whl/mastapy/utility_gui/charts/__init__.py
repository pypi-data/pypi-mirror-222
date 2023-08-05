"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1840 import BubbleChartDefinition
    from ._1841 import ConstantLine
    from ._1842 import CustomLineChart
    from ._1843 import CustomTableAndChart
    from ._1844 import LegacyChartMathChartDefinition
    from ._1845 import ModeConstantLine
    from ._1846 import NDChartDefinition
    from ._1847 import ParallelCoordinatesChartDefinition
    from ._1848 import PointsForSurface
    from ._1849 import ScatterChartDefinition
    from ._1850 import Series2D
    from ._1851 import SMTAxis
    from ._1852 import ThreeDChartDefinition
    from ._1853 import ThreeDVectorChartDefinition
    from ._1854 import TwoDChartDefinition
else:
    import_structure = {
        '_1840': ['BubbleChartDefinition'],
        '_1841': ['ConstantLine'],
        '_1842': ['CustomLineChart'],
        '_1843': ['CustomTableAndChart'],
        '_1844': ['LegacyChartMathChartDefinition'],
        '_1845': ['ModeConstantLine'],
        '_1846': ['NDChartDefinition'],
        '_1847': ['ParallelCoordinatesChartDefinition'],
        '_1848': ['PointsForSurface'],
        '_1849': ['ScatterChartDefinition'],
        '_1850': ['Series2D'],
        '_1851': ['SMTAxis'],
        '_1852': ['ThreeDChartDefinition'],
        '_1853': ['ThreeDVectorChartDefinition'],
        '_1854': ['TwoDChartDefinition'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
