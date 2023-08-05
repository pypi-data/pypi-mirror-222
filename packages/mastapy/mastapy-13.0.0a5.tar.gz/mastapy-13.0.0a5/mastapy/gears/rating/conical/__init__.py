"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._535 import ConicalGearDutyCycleRating
    from ._536 import ConicalGearMeshRating
    from ._537 import ConicalGearRating
    from ._538 import ConicalGearSetDutyCycleRating
    from ._539 import ConicalGearSetRating
    from ._540 import ConicalGearSingleFlankRating
    from ._541 import ConicalMeshDutyCycleRating
    from ._542 import ConicalMeshedGearRating
    from ._543 import ConicalMeshSingleFlankRating
    from ._544 import ConicalRateableMesh
else:
    import_structure = {
        '_535': ['ConicalGearDutyCycleRating'],
        '_536': ['ConicalGearMeshRating'],
        '_537': ['ConicalGearRating'],
        '_538': ['ConicalGearSetDutyCycleRating'],
        '_539': ['ConicalGearSetRating'],
        '_540': ['ConicalGearSingleFlankRating'],
        '_541': ['ConicalMeshDutyCycleRating'],
        '_542': ['ConicalMeshedGearRating'],
        '_543': ['ConicalMeshSingleFlankRating'],
        '_544': ['ConicalRateableMesh'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
