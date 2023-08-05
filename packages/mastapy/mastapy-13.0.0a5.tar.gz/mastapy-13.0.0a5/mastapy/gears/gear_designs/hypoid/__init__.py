"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._982 import HypoidGearDesign
    from ._983 import HypoidGearMeshDesign
    from ._984 import HypoidGearSetDesign
    from ._985 import HypoidMeshedGearDesign
else:
    import_structure = {
        '_982': ['HypoidGearDesign'],
        '_983': ['HypoidGearMeshDesign'],
        '_984': ['HypoidGearSetDesign'],
        '_985': ['HypoidMeshedGearDesign'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
