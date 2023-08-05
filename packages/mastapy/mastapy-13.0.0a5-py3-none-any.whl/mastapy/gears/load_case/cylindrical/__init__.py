"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._879 import CylindricalGearLoadCase
    from ._880 import CylindricalGearSetLoadCase
    from ._881 import CylindricalMeshLoadCase
else:
    import_structure = {
        '_879': ['CylindricalGearLoadCase'],
        '_880': ['CylindricalGearSetLoadCase'],
        '_881': ['CylindricalMeshLoadCase'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
