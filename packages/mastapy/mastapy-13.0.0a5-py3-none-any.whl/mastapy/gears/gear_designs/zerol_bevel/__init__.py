"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._949 import ZerolBevelGearDesign
    from ._950 import ZerolBevelGearMeshDesign
    from ._951 import ZerolBevelGearSetDesign
    from ._952 import ZerolBevelMeshedGearDesign
else:
    import_structure = {
        '_949': ['ZerolBevelGearDesign'],
        '_950': ['ZerolBevelGearMeshDesign'],
        '_951': ['ZerolBevelGearSetDesign'],
        '_952': ['ZerolBevelMeshedGearDesign'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
