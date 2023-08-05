"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._873 import WormGearLoadCase
    from ._874 import WormGearSetLoadCase
    from ._875 import WormMeshLoadCase
else:
    import_structure = {
        '_873': ['WormGearLoadCase'],
        '_874': ['WormGearSetLoadCase'],
        '_875': ['WormMeshLoadCase'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
