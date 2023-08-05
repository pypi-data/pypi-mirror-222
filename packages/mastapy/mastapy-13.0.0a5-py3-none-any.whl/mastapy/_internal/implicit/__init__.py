"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from .overridable import *
    from .enum_with_selected_value import *
    from .list_with_selected_item import *
else:
    import_structure = {
        'overridable': ['*'],
        'enum_with_selected_value': ['*'],
        'list_with_selected_item': ['*'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
