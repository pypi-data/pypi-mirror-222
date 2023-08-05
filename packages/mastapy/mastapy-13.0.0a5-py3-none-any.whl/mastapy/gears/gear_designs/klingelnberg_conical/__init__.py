"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._978 import KlingelnbergConicalGearDesign
    from ._979 import KlingelnbergConicalGearMeshDesign
    from ._980 import KlingelnbergConicalGearSetDesign
    from ._981 import KlingelnbergConicalMeshedGearDesign
else:
    import_structure = {
        '_978': ['KlingelnbergConicalGearDesign'],
        '_979': ['KlingelnbergConicalGearMeshDesign'],
        '_980': ['KlingelnbergConicalGearSetDesign'],
        '_981': ['KlingelnbergConicalMeshedGearDesign'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
