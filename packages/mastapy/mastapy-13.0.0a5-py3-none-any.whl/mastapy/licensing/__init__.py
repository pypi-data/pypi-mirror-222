"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1478 import LicenceServer
    from ._7538 import LicenceServerDetails
    from ._7539 import ModuleDetails
    from ._7540 import ModuleLicenceStatus
else:
    import_structure = {
        '_1478': ['LicenceServer'],
        '_7538': ['LicenceServerDetails'],
        '_7539': ['ModuleDetails'],
        '_7540': ['ModuleLicenceStatus'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
