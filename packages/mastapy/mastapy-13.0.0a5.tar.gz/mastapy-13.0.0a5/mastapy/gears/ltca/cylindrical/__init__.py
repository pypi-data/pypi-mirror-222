"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._848 import CylindricalGearBendingStiffness
    from ._849 import CylindricalGearBendingStiffnessNode
    from ._850 import CylindricalGearContactStiffness
    from ._851 import CylindricalGearContactStiffnessNode
    from ._852 import CylindricalGearFESettings
    from ._853 import CylindricalGearLoadDistributionAnalysis
    from ._854 import CylindricalGearMeshLoadDistributionAnalysis
    from ._855 import CylindricalGearMeshLoadedContactLine
    from ._856 import CylindricalGearMeshLoadedContactPoint
    from ._857 import CylindricalGearSetLoadDistributionAnalysis
    from ._858 import CylindricalMeshLoadDistributionAtRotation
    from ._859 import FaceGearSetLoadDistributionAnalysis
else:
    import_structure = {
        '_848': ['CylindricalGearBendingStiffness'],
        '_849': ['CylindricalGearBendingStiffnessNode'],
        '_850': ['CylindricalGearContactStiffness'],
        '_851': ['CylindricalGearContactStiffnessNode'],
        '_852': ['CylindricalGearFESettings'],
        '_853': ['CylindricalGearLoadDistributionAnalysis'],
        '_854': ['CylindricalGearMeshLoadDistributionAnalysis'],
        '_855': ['CylindricalGearMeshLoadedContactLine'],
        '_856': ['CylindricalGearMeshLoadedContactPoint'],
        '_857': ['CylindricalGearSetLoadDistributionAnalysis'],
        '_858': ['CylindricalMeshLoadDistributionAtRotation'],
        '_859': ['FaceGearSetLoadDistributionAnalysis'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
