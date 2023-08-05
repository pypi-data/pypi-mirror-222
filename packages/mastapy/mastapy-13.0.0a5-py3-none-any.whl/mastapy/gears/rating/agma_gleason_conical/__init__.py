"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._562 import AGMAGleasonConicalGearMeshRating
    from ._563 import AGMAGleasonConicalGearRating
    from ._564 import AGMAGleasonConicalGearSetRating
    from ._565 import AGMAGleasonConicalRateableMesh
else:
    import_structure = {
        '_562': ['AGMAGleasonConicalGearMeshRating'],
        '_563': ['AGMAGleasonConicalGearRating'],
        '_564': ['AGMAGleasonConicalGearSetRating'],
        '_565': ['AGMAGleasonConicalRateableMesh'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
