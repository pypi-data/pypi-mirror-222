"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1230 import BeamSectionType
    from ._1231 import ContactPairConstrainedSurfaceType
    from ._1232 import ContactPairReferenceSurfaceType
    from ._1233 import ElementPropertiesShellWallType
else:
    import_structure = {
        '_1230': ['BeamSectionType'],
        '_1231': ['ContactPairConstrainedSurfaceType'],
        '_1232': ['ContactPairReferenceSurfaceType'],
        '_1233': ['ElementPropertiesShellWallType'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
