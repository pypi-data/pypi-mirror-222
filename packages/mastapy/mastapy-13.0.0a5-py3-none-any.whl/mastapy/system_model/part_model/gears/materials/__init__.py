"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2548 import GearMaterialExpertSystemMaterialDetails
    from ._2549 import GearMaterialExpertSystemMaterialOptions
else:
    import_structure = {
        '_2548': ['GearMaterialExpertSystemMaterialDetails'],
        '_2549': ['GearMaterialExpertSystemMaterialOptions'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
