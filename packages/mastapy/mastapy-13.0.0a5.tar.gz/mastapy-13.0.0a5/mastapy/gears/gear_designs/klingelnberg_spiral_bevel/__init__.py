"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._970 import KlingelnbergCycloPalloidSpiralBevelGearDesign
    from ._971 import KlingelnbergCycloPalloidSpiralBevelGearMeshDesign
    from ._972 import KlingelnbergCycloPalloidSpiralBevelGearSetDesign
    from ._973 import KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign
else:
    import_structure = {
        '_970': ['KlingelnbergCycloPalloidSpiralBevelGearDesign'],
        '_971': ['KlingelnbergCycloPalloidSpiralBevelGearMeshDesign'],
        '_972': ['KlingelnbergCycloPalloidSpiralBevelGearSetDesign'],
        '_973': ['KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
