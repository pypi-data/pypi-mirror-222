"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._554 import AGMASpiralBevelGearSingleFlankRating
    from ._555 import AGMASpiralBevelMeshSingleFlankRating
    from ._556 import GleasonSpiralBevelGearSingleFlankRating
    from ._557 import GleasonSpiralBevelMeshSingleFlankRating
    from ._558 import SpiralBevelGearSingleFlankRating
    from ._559 import SpiralBevelMeshSingleFlankRating
    from ._560 import SpiralBevelRateableGear
    from ._561 import SpiralBevelRateableMesh
else:
    import_structure = {
        '_554': ['AGMASpiralBevelGearSingleFlankRating'],
        '_555': ['AGMASpiralBevelMeshSingleFlankRating'],
        '_556': ['GleasonSpiralBevelGearSingleFlankRating'],
        '_557': ['GleasonSpiralBevelMeshSingleFlankRating'],
        '_558': ['SpiralBevelGearSingleFlankRating'],
        '_559': ['SpiralBevelMeshSingleFlankRating'],
        '_560': ['SpiralBevelRateableGear'],
        '_561': ['SpiralBevelRateableMesh'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
