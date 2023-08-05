"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._545 import ConceptGearDutyCycleRating
    from ._546 import ConceptGearMeshDutyCycleRating
    from ._547 import ConceptGearMeshRating
    from ._548 import ConceptGearRating
    from ._549 import ConceptGearSetDutyCycleRating
    from ._550 import ConceptGearSetRating
else:
    import_structure = {
        '_545': ['ConceptGearDutyCycleRating'],
        '_546': ['ConceptGearMeshDutyCycleRating'],
        '_547': ['ConceptGearMeshRating'],
        '_548': ['ConceptGearRating'],
        '_549': ['ConceptGearSetDutyCycleRating'],
        '_550': ['ConceptGearSetRating'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
