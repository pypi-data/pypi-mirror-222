"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2183 import BearingNodePosition
    from ._2184 import ConceptAxialClearanceBearing
    from ._2185 import ConceptClearanceBearing
    from ._2186 import ConceptRadialClearanceBearing
else:
    import_structure = {
        '_2183': ['BearingNodePosition'],
        '_2184': ['ConceptAxialClearanceBearing'],
        '_2185': ['ConceptClearanceBearing'],
        '_2186': ['ConceptRadialClearanceBearing'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
