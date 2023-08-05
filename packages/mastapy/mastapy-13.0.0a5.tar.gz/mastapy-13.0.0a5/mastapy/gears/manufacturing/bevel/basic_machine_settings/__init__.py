"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._818 import BasicConicalGearMachineSettings
    from ._819 import BasicConicalGearMachineSettingsFormate
    from ._820 import BasicConicalGearMachineSettingsGenerated
    from ._821 import CradleStyleConicalMachineSettingsGenerated
else:
    import_structure = {
        '_818': ['BasicConicalGearMachineSettings'],
        '_819': ['BasicConicalGearMachineSettingsFormate'],
        '_820': ['BasicConicalGearMachineSettingsGenerated'],
        '_821': ['CradleStyleConicalMachineSettingsGenerated'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
