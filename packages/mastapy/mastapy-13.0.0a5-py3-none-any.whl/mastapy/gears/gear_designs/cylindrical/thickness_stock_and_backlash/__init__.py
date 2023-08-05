"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1085 import FinishStockSpecification
    from ._1086 import FinishStockType
    from ._1087 import NominalValueSpecification
    from ._1088 import NoValueSpecification
else:
    import_structure = {
        '_1085': ['FinishStockSpecification'],
        '_1086': ['FinishStockType'],
        '_1087': ['NominalValueSpecification'],
        '_1088': ['NoValueSpecification'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
