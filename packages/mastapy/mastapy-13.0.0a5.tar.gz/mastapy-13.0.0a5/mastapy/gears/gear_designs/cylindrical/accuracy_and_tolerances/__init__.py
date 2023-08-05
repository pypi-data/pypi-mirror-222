"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1128 import AGMA2000A88AccuracyGrader
    from ._1129 import AGMA20151A01AccuracyGrader
    from ._1130 import AGMA20151AccuracyGrades
    from ._1131 import AGMAISO13281B14AccuracyGrader
    from ._1132 import CylindricalAccuracyGrader
    from ._1133 import CylindricalAccuracyGraderWithProfileFormAndSlope
    from ._1134 import CylindricalAccuracyGrades
    from ._1135 import CylindricalGearAccuracyTolerances
    from ._1136 import DIN3967SystemOfGearFits
    from ._1137 import ISO132811995AccuracyGrader
    from ._1138 import ISO132812013AccuracyGrader
    from ._1139 import ISO1328AccuracyGraderCommon
    from ._1140 import ISO1328AccuracyGrades
    from ._1141 import OverridableTolerance
else:
    import_structure = {
        '_1128': ['AGMA2000A88AccuracyGrader'],
        '_1129': ['AGMA20151A01AccuracyGrader'],
        '_1130': ['AGMA20151AccuracyGrades'],
        '_1131': ['AGMAISO13281B14AccuracyGrader'],
        '_1132': ['CylindricalAccuracyGrader'],
        '_1133': ['CylindricalAccuracyGraderWithProfileFormAndSlope'],
        '_1134': ['CylindricalAccuracyGrades'],
        '_1135': ['CylindricalGearAccuracyTolerances'],
        '_1136': ['DIN3967SystemOfGearFits'],
        '_1137': ['ISO132811995AccuracyGrader'],
        '_1138': ['ISO132812013AccuracyGrader'],
        '_1139': ['ISO1328AccuracyGraderCommon'],
        '_1140': ['ISO1328AccuracyGrades'],
        '_1141': ['OverridableTolerance'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
