"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7526 import MeasurementType
    from ._7527 import MeasurementTypeExtensions
else:
    import_structure = {
        '_7526': ['MeasurementType'],
        '_7527': ['MeasurementTypeExtensions'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
