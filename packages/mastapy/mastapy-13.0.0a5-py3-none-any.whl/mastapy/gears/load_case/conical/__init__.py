"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._882 import ConicalGearLoadCase
    from ._883 import ConicalGearSetLoadCase
    from ._884 import ConicalMeshLoadCase
else:
    import_structure = {
        '_882': ['ConicalGearLoadCase'],
        '_883': ['ConicalGearSetLoadCase'],
        '_884': ['ConicalMeshLoadCase'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
