"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1914 import ProfileDataToUse
    from ._1915 import ProfileSet
    from ._1916 import ProfileToFit
    from ._1917 import RollerBearingConicalProfile
    from ._1918 import RollerBearingCrownedProfile
    from ._1919 import RollerBearingDinLundbergProfile
    from ._1920 import RollerBearingFlatProfile
    from ._1921 import RollerBearingJohnsGoharProfile
    from ._1922 import RollerBearingLundbergProfile
    from ._1923 import RollerBearingProfile
    from ._1924 import RollerBearingUserSpecifiedProfile
    from ._1925 import RollerRaceProfilePoint
    from ._1926 import UserSpecifiedProfilePoint
    from ._1927 import UserSpecifiedRollerRaceProfilePoint
else:
    import_structure = {
        '_1914': ['ProfileDataToUse'],
        '_1915': ['ProfileSet'],
        '_1916': ['ProfileToFit'],
        '_1917': ['RollerBearingConicalProfile'],
        '_1918': ['RollerBearingCrownedProfile'],
        '_1919': ['RollerBearingDinLundbergProfile'],
        '_1920': ['RollerBearingFlatProfile'],
        '_1921': ['RollerBearingJohnsGoharProfile'],
        '_1922': ['RollerBearingLundbergProfile'],
        '_1923': ['RollerBearingProfile'],
        '_1924': ['RollerBearingUserSpecifiedProfile'],
        '_1925': ['RollerRaceProfilePoint'],
        '_1926': ['UserSpecifiedProfilePoint'],
        '_1927': ['UserSpecifiedRollerRaceProfilePoint'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
