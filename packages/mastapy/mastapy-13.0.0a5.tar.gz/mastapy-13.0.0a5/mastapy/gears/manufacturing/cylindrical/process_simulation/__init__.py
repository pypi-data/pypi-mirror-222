"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._636 import CutterProcessSimulation
    from ._637 import FormWheelGrindingProcessSimulation
    from ._638 import ShapingProcessSimulation
else:
    import_structure = {
        '_636': ['CutterProcessSimulation'],
        '_637': ['FormWheelGrindingProcessSimulation'],
        '_638': ['ShapingProcessSimulation'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
