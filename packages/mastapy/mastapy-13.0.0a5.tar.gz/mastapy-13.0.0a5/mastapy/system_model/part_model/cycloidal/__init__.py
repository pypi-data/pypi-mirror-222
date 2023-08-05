"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2550 import CycloidalAssembly
    from ._2551 import CycloidalDisc
    from ._2552 import RingPins
else:
    import_structure = {
        '_2550': ['CycloidalAssembly'],
        '_2551': ['CycloidalDisc'],
        '_2552': ['RingPins'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
