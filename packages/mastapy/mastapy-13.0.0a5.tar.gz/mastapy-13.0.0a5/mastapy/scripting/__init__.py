"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7528 import ApiEnumForAttribute
    from ._7529 import ApiVersion
    from ._7530 import SMTBitmap
    from ._7532 import MastaPropertyAttribute
    from ._7533 import PythonCommand
    from ._7534 import ScriptingCommand
    from ._7535 import ScriptingExecutionCommand
    from ._7536 import ScriptingObjectCommand
    from ._7537 import ApiVersioning
else:
    import_structure = {
        '_7528': ['ApiEnumForAttribute'],
        '_7529': ['ApiVersion'],
        '_7530': ['SMTBitmap'],
        '_7532': ['MastaPropertyAttribute'],
        '_7533': ['PythonCommand'],
        '_7534': ['ScriptingCommand'],
        '_7535': ['ScriptingExecutionCommand'],
        '_7536': ['ScriptingObjectCommand'],
        '_7537': ['ApiVersioning'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
