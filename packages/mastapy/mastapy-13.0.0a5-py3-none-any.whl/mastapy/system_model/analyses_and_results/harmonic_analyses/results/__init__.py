"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5814 import ConnectedComponentType
    from ._5815 import ExcitationSourceSelection
    from ._5816 import ExcitationSourceSelectionBase
    from ._5817 import ExcitationSourceSelectionGroup
    from ._5818 import HarmonicSelection
    from ._5819 import ModalContributionDisplayMethod
    from ._5820 import ModalContributionFilteringMethod
    from ._5821 import ResultLocationSelectionGroup
    from ._5822 import ResultLocationSelectionGroups
    from ._5823 import ResultNodeSelection
else:
    import_structure = {
        '_5814': ['ConnectedComponentType'],
        '_5815': ['ExcitationSourceSelection'],
        '_5816': ['ExcitationSourceSelectionBase'],
        '_5817': ['ExcitationSourceSelectionGroup'],
        '_5818': ['HarmonicSelection'],
        '_5819': ['ModalContributionDisplayMethod'],
        '_5820': ['ModalContributionFilteringMethod'],
        '_5821': ['ResultLocationSelectionGroup'],
        '_5822': ['ResultLocationSelectionGroups'],
        '_5823': ['ResultNodeSelection'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
