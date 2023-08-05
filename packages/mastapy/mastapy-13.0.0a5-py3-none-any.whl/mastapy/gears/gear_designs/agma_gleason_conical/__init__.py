"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1188 import AGMAGleasonConicalAccuracyGrades
    from ._1189 import AGMAGleasonConicalGearDesign
    from ._1190 import AGMAGleasonConicalGearMeshDesign
    from ._1191 import AGMAGleasonConicalGearSetDesign
    from ._1192 import AGMAGleasonConicalMeshedGearDesign
else:
    import_structure = {
        '_1188': ['AGMAGleasonConicalAccuracyGrades'],
        '_1189': ['AGMAGleasonConicalGearDesign'],
        '_1190': ['AGMAGleasonConicalGearMeshDesign'],
        '_1191': ['AGMAGleasonConicalGearSetDesign'],
        '_1192': ['AGMAGleasonConicalMeshedGearDesign'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
