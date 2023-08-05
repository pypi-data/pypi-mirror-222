"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1193 import GearFEModel
    from ._1194 import GearMeshFEModel
    from ._1195 import GearMeshingElementOptions
    from ._1196 import GearSetFEModel
else:
    import_structure = {
        '_1193': ['GearFEModel'],
        '_1194': ['GearMeshFEModel'],
        '_1195': ['GearMeshingElementOptions'],
        '_1196': ['GearSetFEModel'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
