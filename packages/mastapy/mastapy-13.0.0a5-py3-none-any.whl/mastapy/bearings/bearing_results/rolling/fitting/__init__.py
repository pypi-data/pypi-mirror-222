"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2097 import InnerRingFittingThermalResults
    from ._2098 import InterferenceComponents
    from ._2099 import OuterRingFittingThermalResults
    from ._2100 import RingFittingThermalResults
else:
    import_structure = {
        '_2097': ['InnerRingFittingThermalResults'],
        '_2098': ['InterferenceComponents'],
        '_2099': ['OuterRingFittingThermalResults'],
        '_2100': ['RingFittingThermalResults'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
