"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._888 import BevelLoadCase
    from ._889 import BevelMeshLoadCase
    from ._890 import BevelSetLoadCase
else:
    import_structure = {
        '_888': ['BevelLoadCase'],
        '_889': ['BevelMeshLoadCase'],
        '_890': ['BevelSetLoadCase'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
