"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1730 import ScriptingSetup
    from ._1731 import UserDefinedPropertyKey
    from ._1732 import UserSpecifiedData
else:
    import_structure = {
        '_1730': ['ScriptingSetup'],
        '_1731': ['UserDefinedPropertyKey'],
        '_1732': ['UserSpecifiedData'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
