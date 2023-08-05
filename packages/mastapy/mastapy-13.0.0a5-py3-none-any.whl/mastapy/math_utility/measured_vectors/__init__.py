"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1550 import AbstractForceAndDisplacementResults
    from ._1551 import ForceAndDisplacementResults
    from ._1552 import ForceResults
    from ._1553 import NodeResults
    from ._1554 import OverridableDisplacementBoundaryCondition
    from ._1555 import VectorWithLinearAndAngularComponents
else:
    import_structure = {
        '_1550': ['AbstractForceAndDisplacementResults'],
        '_1551': ['ForceAndDisplacementResults'],
        '_1552': ['ForceResults'],
        '_1553': ['NodeResults'],
        '_1554': ['OverridableDisplacementBoundaryCondition'],
        '_1555': ['VectorWithLinearAndAngularComponents'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
