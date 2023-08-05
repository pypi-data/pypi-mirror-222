"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1808 import BearingForceArrowOption
    from ._1809 import TableAndChartOptions
    from ._1810 import ThreeDViewContourOption
    from ._1811 import ThreeDViewContourOptionFirstSelection
    from ._1812 import ThreeDViewContourOptionSecondSelection
else:
    import_structure = {
        '_1808': ['BearingForceArrowOption'],
        '_1809': ['TableAndChartOptions'],
        '_1810': ['ThreeDViewContourOption'],
        '_1811': ['ThreeDViewContourOptionFirstSelection'],
        '_1812': ['ThreeDViewContourOptionSecondSelection'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
