"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._814 import ConicalGearManufacturingControlParameters
    from ._815 import ConicalManufacturingSGMControlParameters
    from ._816 import ConicalManufacturingSGTControlParameters
    from ._817 import ConicalManufacturingSMTControlParameters
else:
    import_structure = {
        '_814': ['ConicalGearManufacturingControlParameters'],
        '_815': ['ConicalManufacturingSGMControlParameters'],
        '_816': ['ConicalManufacturingSGTControlParameters'],
        '_817': ['ConicalManufacturingSMTControlParameters'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
