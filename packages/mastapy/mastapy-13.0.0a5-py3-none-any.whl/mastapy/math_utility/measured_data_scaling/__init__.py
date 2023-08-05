"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1560 import DataScalingOptions
    from ._1561 import DataScalingReferenceValues
    from ._1562 import DataScalingReferenceValuesBase
else:
    import_structure = {
        '_1560': ['DataScalingOptions'],
        '_1561': ['DataScalingReferenceValues'],
        '_1562': ['DataScalingReferenceValuesBase'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
