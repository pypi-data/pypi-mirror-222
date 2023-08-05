"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1204 import CylindricalGearLTCAContactChartDataAsTextFile
    from ._1205 import CylindricalGearLTCAContactCharts
    from ._1206 import CylindricalGearWorstLTCAContactChartDataAsTextFile
    from ._1207 import CylindricalGearWorstLTCAContactCharts
    from ._1208 import GearLTCAContactChartDataAsTextFile
    from ._1209 import GearLTCAContactCharts
    from ._1210 import PointsWithWorstResults
else:
    import_structure = {
        '_1204': ['CylindricalGearLTCAContactChartDataAsTextFile'],
        '_1205': ['CylindricalGearLTCAContactCharts'],
        '_1206': ['CylindricalGearWorstLTCAContactChartDataAsTextFile'],
        '_1207': ['CylindricalGearWorstLTCAContactCharts'],
        '_1208': ['GearLTCAContactChartDataAsTextFile'],
        '_1209': ['GearLTCAContactCharts'],
        '_1210': ['PointsWithWorstResults'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
