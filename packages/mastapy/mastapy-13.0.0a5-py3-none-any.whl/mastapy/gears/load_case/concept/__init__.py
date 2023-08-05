"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._885 import ConceptGearLoadCase
    from ._886 import ConceptGearSetLoadCase
    from ._887 import ConceptMeshLoadCase
else:
    import_structure = {
        '_885': ['ConceptGearLoadCase'],
        '_886': ['ConceptGearSetLoadCase'],
        '_887': ['ConceptMeshLoadCase'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
