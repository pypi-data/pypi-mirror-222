"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._937 import BevelHypoidGearDesignSettingsDatabase
    from ._938 import BevelHypoidGearDesignSettingsItem
    from ._939 import BevelHypoidGearRatingSettingsDatabase
    from ._940 import BevelHypoidGearRatingSettingsItem
    from ._941 import DesignConstraint
    from ._942 import DesignConstraintCollectionDatabase
    from ._943 import DesignConstraintsCollection
    from ._944 import GearDesign
    from ._945 import GearDesignComponent
    from ._946 import GearMeshDesign
    from ._947 import GearSetDesign
    from ._948 import SelectedDesignConstraintsCollection
else:
    import_structure = {
        '_937': ['BevelHypoidGearDesignSettingsDatabase'],
        '_938': ['BevelHypoidGearDesignSettingsItem'],
        '_939': ['BevelHypoidGearRatingSettingsDatabase'],
        '_940': ['BevelHypoidGearRatingSettingsItem'],
        '_941': ['DesignConstraint'],
        '_942': ['DesignConstraintCollectionDatabase'],
        '_943': ['DesignConstraintsCollection'],
        '_944': ['GearDesign'],
        '_945': ['GearDesignComponent'],
        '_946': ['GearMeshDesign'],
        '_947': ['GearSetDesign'],
        '_948': ['SelectedDesignConstraintsCollection'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
