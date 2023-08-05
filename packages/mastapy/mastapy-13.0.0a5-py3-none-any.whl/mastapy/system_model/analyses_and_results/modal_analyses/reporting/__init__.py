"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4692 import CalculateFullFEResultsForMode
    from ._4693 import CampbellDiagramReport
    from ._4694 import ComponentPerModeResult
    from ._4695 import DesignEntityModalAnalysisGroupResults
    from ._4696 import ModalCMSResultsForModeAndFE
    from ._4697 import PerModeResultsReport
    from ._4698 import RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis
    from ._4699 import RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis
    from ._4700 import RigidlyConnectedDesignEntityGroupModalAnalysis
    from ._4701 import ShaftPerModeResult
    from ._4702 import SingleExcitationResultsModalAnalysis
    from ._4703 import SingleModeResults
else:
    import_structure = {
        '_4692': ['CalculateFullFEResultsForMode'],
        '_4693': ['CampbellDiagramReport'],
        '_4694': ['ComponentPerModeResult'],
        '_4695': ['DesignEntityModalAnalysisGroupResults'],
        '_4696': ['ModalCMSResultsForModeAndFE'],
        '_4697': ['PerModeResultsReport'],
        '_4698': ['RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis'],
        '_4699': ['RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis'],
        '_4700': ['RigidlyConnectedDesignEntityGroupModalAnalysis'],
        '_4701': ['ShaftPerModeResult'],
        '_4702': ['SingleExcitationResultsModalAnalysis'],
        '_4703': ['SingleModeResults'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
