"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1377 import DetailedRigidConnectorDesign
    from ._1378 import DetailedRigidConnectorHalfDesign
else:
    import_structure = {
        '_1377': ['DetailedRigidConnectorDesign'],
        '_1378': ['DetailedRigidConnectorHalfDesign'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
