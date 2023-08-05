"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2553 import BeltCreationOptions
    from ._2554 import CycloidalAssemblyCreationOptions
    from ._2555 import CylindricalGearLinearTrainCreationOptions
    from ._2556 import PlanetCarrierCreationOptions
    from ._2557 import ShaftCreationOptions
else:
    import_structure = {
        '_2553': ['BeltCreationOptions'],
        '_2554': ['CycloidalAssemblyCreationOptions'],
        '_2555': ['CylindricalGearLinearTrainCreationOptions'],
        '_2556': ['PlanetCarrierCreationOptions'],
        '_2557': ['ShaftCreationOptions'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
