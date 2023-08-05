"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1197 import CylindricalGearFEModel
    from ._1198 import CylindricalGearMeshFEModel
    from ._1199 import CylindricalGearSetFEModel
else:
    import_structure = {
        '_1197': ['CylindricalGearFEModel'],
        '_1198': ['CylindricalGearMeshFEModel'],
        '_1199': ['CylindricalGearSetFEModel'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
