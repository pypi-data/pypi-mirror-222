"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2244 import AdvancedTimeSteppingAnalysisForModulationModeViewOptions
    from ._2245 import ExcitationAnalysisViewOption
    from ._2246 import ModalContributionViewOptions
else:
    import_structure = {
        '_2244': ['AdvancedTimeSteppingAnalysisForModulationModeViewOptions'],
        '_2245': ['ExcitationAnalysisViewOption'],
        '_2246': ['ModalContributionViewOptions'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
