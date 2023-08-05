"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._870 import GearLoadCaseBase
    from ._871 import GearSetLoadCaseBase
    from ._872 import MeshLoadCase
else:
    import_structure = {
        '_870': ['GearLoadCaseBase'],
        '_871': ['GearSetLoadCaseBase'],
        '_872': ['MeshLoadCase'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
