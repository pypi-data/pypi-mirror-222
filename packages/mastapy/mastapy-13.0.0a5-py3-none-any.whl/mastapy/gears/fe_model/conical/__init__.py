"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1200 import ConicalGearFEModel
    from ._1201 import ConicalMeshFEModel
    from ._1202 import ConicalSetFEModel
    from ._1203 import FlankDataSource
else:
    import_structure = {
        '_1200': ['ConicalGearFEModel'],
        '_1201': ['ConicalMeshFEModel'],
        '_1202': ['ConicalSetFEModel'],
        '_1203': ['FlankDataSource'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
