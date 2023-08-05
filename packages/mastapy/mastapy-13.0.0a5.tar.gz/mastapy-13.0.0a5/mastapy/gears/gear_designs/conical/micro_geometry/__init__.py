"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1168 import ConicalGearBiasModification
    from ._1169 import ConicalGearFlankMicroGeometry
    from ._1170 import ConicalGearLeadModification
    from ._1171 import ConicalGearProfileModification
else:
    import_structure = {
        '_1168': ['ConicalGearBiasModification'],
        '_1169': ['ConicalGearFlankMicroGeometry'],
        '_1170': ['ConicalGearLeadModification'],
        '_1171': ['ConicalGearProfileModification'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
