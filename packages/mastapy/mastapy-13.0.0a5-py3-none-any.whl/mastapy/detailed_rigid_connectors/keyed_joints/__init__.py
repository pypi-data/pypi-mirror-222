"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1427 import KeyedJointDesign
    from ._1428 import KeyTypes
    from ._1429 import KeywayJointHalfDesign
    from ._1430 import NumberOfKeys
else:
    import_structure = {
        '_1427': ['KeyedJointDesign'],
        '_1428': ['KeyTypes'],
        '_1429': ['KeywayJointHalfDesign'],
        '_1430': ['NumberOfKeys'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
