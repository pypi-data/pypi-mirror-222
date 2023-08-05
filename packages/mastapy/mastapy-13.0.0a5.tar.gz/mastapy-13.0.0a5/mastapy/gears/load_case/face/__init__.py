"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._876 import FaceGearLoadCase
    from ._877 import FaceGearSetLoadCase
    from ._878 import FaceMeshLoadCase
else:
    import_structure = {
        '_876': ['FaceGearLoadCase'],
        '_877': ['FaceGearSetLoadCase'],
        '_878': ['FaceMeshLoadCase'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
