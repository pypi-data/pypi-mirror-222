"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._810 import PinionFinishCutter
    from ._811 import PinionRoughCutter
    from ._812 import WheelFinishCutter
    from ._813 import WheelRoughCutter
else:
    import_structure = {
        '_810': ['PinionFinishCutter'],
        '_811': ['PinionRoughCutter'],
        '_812': ['WheelFinishCutter'],
        '_813': ['WheelRoughCutter'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
