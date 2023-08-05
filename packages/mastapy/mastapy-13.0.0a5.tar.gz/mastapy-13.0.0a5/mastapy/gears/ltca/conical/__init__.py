"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._860 import ConicalGearBendingStiffness
    from ._861 import ConicalGearBendingStiffnessNode
    from ._862 import ConicalGearContactStiffness
    from ._863 import ConicalGearContactStiffnessNode
    from ._864 import ConicalGearLoadDistributionAnalysis
    from ._865 import ConicalGearSetLoadDistributionAnalysis
    from ._866 import ConicalMeshedGearLoadDistributionAnalysis
    from ._867 import ConicalMeshLoadDistributionAnalysis
    from ._868 import ConicalMeshLoadDistributionAtRotation
    from ._869 import ConicalMeshLoadedContactLine
else:
    import_structure = {
        '_860': ['ConicalGearBendingStiffness'],
        '_861': ['ConicalGearBendingStiffnessNode'],
        '_862': ['ConicalGearContactStiffness'],
        '_863': ['ConicalGearContactStiffnessNode'],
        '_864': ['ConicalGearLoadDistributionAnalysis'],
        '_865': ['ConicalGearSetLoadDistributionAnalysis'],
        '_866': ['ConicalMeshedGearLoadDistributionAnalysis'],
        '_867': ['ConicalMeshLoadDistributionAnalysis'],
        '_868': ['ConicalMeshLoadDistributionAtRotation'],
        '_869': ['ConicalMeshLoadedContactLine'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
