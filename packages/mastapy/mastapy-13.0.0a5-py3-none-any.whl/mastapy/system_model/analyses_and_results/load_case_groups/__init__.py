"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5631 import AbstractDesignStateLoadCaseGroup
    from ._5632 import AbstractLoadCaseGroup
    from ._5633 import AbstractStaticLoadCaseGroup
    from ._5634 import ClutchEngagementStatus
    from ._5635 import ConceptSynchroGearEngagementStatus
    from ._5636 import DesignState
    from ._5637 import DutyCycle
    from ._5638 import GenericClutchEngagementStatus
    from ._5639 import LoadCaseGroupHistograms
    from ._5640 import SubGroupInSingleDesignState
    from ._5641 import SystemOptimisationGearSet
    from ._5642 import SystemOptimiserGearSetOptimisation
    from ._5643 import SystemOptimiserTargets
    from ._5644 import TimeSeriesLoadCaseGroup
else:
    import_structure = {
        '_5631': ['AbstractDesignStateLoadCaseGroup'],
        '_5632': ['AbstractLoadCaseGroup'],
        '_5633': ['AbstractStaticLoadCaseGroup'],
        '_5634': ['ClutchEngagementStatus'],
        '_5635': ['ConceptSynchroGearEngagementStatus'],
        '_5636': ['DesignState'],
        '_5637': ['DutyCycle'],
        '_5638': ['GenericClutchEngagementStatus'],
        '_5639': ['LoadCaseGroupHistograms'],
        '_5640': ['SubGroupInSingleDesignState'],
        '_5641': ['SystemOptimisationGearSet'],
        '_5642': ['SystemOptimiserGearSetOptimisation'],
        '_5643': ['SystemOptimiserTargets'],
        '_5644': ['TimeSeriesLoadCaseGroup'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
