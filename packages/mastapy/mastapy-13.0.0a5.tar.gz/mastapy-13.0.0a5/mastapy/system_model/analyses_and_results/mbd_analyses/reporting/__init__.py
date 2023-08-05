"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5496 import AbstractMeasuredDynamicResponseAtTime
    from ._5497 import DynamicForceResultAtTime
    from ._5498 import DynamicForceVector3DResult
    from ._5499 import DynamicTorqueResultAtTime
    from ._5500 import DynamicTorqueVector3DResult
else:
    import_structure = {
        '_5496': ['AbstractMeasuredDynamicResponseAtTime'],
        '_5497': ['DynamicForceResultAtTime'],
        '_5498': ['DynamicForceVector3DResult'],
        '_5499': ['DynamicTorqueResultAtTime'],
        '_5500': ['DynamicTorqueVector3DResult'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
