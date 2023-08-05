"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._974 import KlingelnbergCycloPalloidHypoidGearDesign
    from ._975 import KlingelnbergCycloPalloidHypoidGearMeshDesign
    from ._976 import KlingelnbergCycloPalloidHypoidGearSetDesign
    from ._977 import KlingelnbergCycloPalloidHypoidMeshedGearDesign
else:
    import_structure = {
        '_974': ['KlingelnbergCycloPalloidHypoidGearDesign'],
        '_975': ['KlingelnbergCycloPalloidHypoidGearMeshDesign'],
        '_976': ['KlingelnbergCycloPalloidHypoidGearSetDesign'],
        '_977': ['KlingelnbergCycloPalloidHypoidMeshedGearDesign'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
