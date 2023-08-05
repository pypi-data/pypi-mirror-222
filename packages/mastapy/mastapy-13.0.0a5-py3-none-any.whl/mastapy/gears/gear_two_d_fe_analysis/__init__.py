"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._891 import CylindricalGearMeshTIFFAnalysis
    from ._892 import CylindricalGearMeshTIFFAnalysisDutyCycle
    from ._893 import CylindricalGearSetTIFFAnalysis
    from ._894 import CylindricalGearSetTIFFAnalysisDutyCycle
    from ._895 import CylindricalGearTIFFAnalysis
    from ._896 import CylindricalGearTIFFAnalysisDutyCycle
    from ._897 import CylindricalGearTwoDimensionalFEAnalysis
    from ._898 import FindleyCriticalPlaneAnalysis
else:
    import_structure = {
        '_891': ['CylindricalGearMeshTIFFAnalysis'],
        '_892': ['CylindricalGearMeshTIFFAnalysisDutyCycle'],
        '_893': ['CylindricalGearSetTIFFAnalysis'],
        '_894': ['CylindricalGearSetTIFFAnalysisDutyCycle'],
        '_895': ['CylindricalGearTIFFAnalysis'],
        '_896': ['CylindricalGearTIFFAnalysisDutyCycle'],
        '_897': ['CylindricalGearTwoDimensionalFEAnalysis'],
        '_898': ['FindleyCriticalPlaneAnalysis'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
