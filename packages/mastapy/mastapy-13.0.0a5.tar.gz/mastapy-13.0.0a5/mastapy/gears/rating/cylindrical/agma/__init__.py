"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._531 import AGMA2101GearSingleFlankRating
    from ._532 import AGMA2101MeshSingleFlankRating
    from ._533 import AGMA2101RateableMesh
    from ._534 import ThermalReductionFactorFactorsAndExponents
else:
    import_structure = {
        '_531': ['AGMA2101GearSingleFlankRating'],
        '_532': ['AGMA2101MeshSingleFlankRating'],
        '_533': ['AGMA2101RateableMesh'],
        '_534': ['ThermalReductionFactorFactorsAndExponents'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
