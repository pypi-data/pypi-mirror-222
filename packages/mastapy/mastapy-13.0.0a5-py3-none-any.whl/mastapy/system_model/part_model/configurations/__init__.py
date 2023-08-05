"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2593 import ActiveFESubstructureSelection
    from ._2594 import ActiveFESubstructureSelectionGroup
    from ._2595 import ActiveShaftDesignSelection
    from ._2596 import ActiveShaftDesignSelectionGroup
    from ._2597 import BearingDetailConfiguration
    from ._2598 import BearingDetailSelection
    from ._2599 import PartDetailConfiguration
    from ._2600 import PartDetailSelection
else:
    import_structure = {
        '_2593': ['ActiveFESubstructureSelection'],
        '_2594': ['ActiveFESubstructureSelectionGroup'],
        '_2595': ['ActiveShaftDesignSelection'],
        '_2596': ['ActiveShaftDesignSelectionGroup'],
        '_2597': ['BearingDetailConfiguration'],
        '_2598': ['BearingDetailSelection'],
        '_2599': ['PartDetailConfiguration'],
        '_2600': ['PartDetailSelection'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
