"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4006 import RotorDynamicsDrawStyle
    from ._4007 import ShaftComplexShape
    from ._4008 import ShaftForcedComplexShape
    from ._4009 import ShaftModalComplexShape
    from ._4010 import ShaftModalComplexShapeAtSpeeds
    from ._4011 import ShaftModalComplexShapeAtStiffness
else:
    import_structure = {
        '_4006': ['RotorDynamicsDrawStyle'],
        '_4007': ['ShaftComplexShape'],
        '_4008': ['ShaftForcedComplexShape'],
        '_4009': ['ShaftModalComplexShape'],
        '_4010': ['ShaftModalComplexShapeAtSpeeds'],
        '_4011': ['ShaftModalComplexShapeAtStiffness'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
