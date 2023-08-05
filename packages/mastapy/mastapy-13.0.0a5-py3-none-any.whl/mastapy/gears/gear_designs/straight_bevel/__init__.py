"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._958 import StraightBevelGearDesign
    from ._959 import StraightBevelGearMeshDesign
    from ._960 import StraightBevelGearSetDesign
    from ._961 import StraightBevelMeshedGearDesign
else:
    import_structure = {
        '_958': ['StraightBevelGearDesign'],
        '_959': ['StraightBevelGearMeshDesign'],
        '_960': ['StraightBevelGearSetDesign'],
        '_961': ['StraightBevelMeshedGearDesign'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
