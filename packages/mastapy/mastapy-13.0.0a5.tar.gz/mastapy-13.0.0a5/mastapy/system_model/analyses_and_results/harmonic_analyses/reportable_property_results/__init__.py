"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5824 import AbstractSingleWhineAnalysisResultsPropertyAccessor
    from ._5825 import DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic
    from ._5826 import DataPointForResponseOfANodeAtAFrequencyToAHarmonic
    from ._5827 import FEPartHarmonicAnalysisResultsPropertyAccessor
    from ._5828 import FEPartSingleWhineAnalysisResultsPropertyAccessor
    from ._5829 import HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic
    from ._5830 import HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic
    from ._5831 import HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic
    from ._5832 import HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic
    from ._5833 import HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic
    from ._5834 import HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic
    from ._5835 import HarmonicAnalysisResultsPropertyAccessor
    from ._5836 import ResultsForMultipleOrders
    from ._5837 import ResultsForMultipleOrdersForFESurface
    from ._5838 import ResultsForMultipleOrdersForGroups
    from ._5839 import ResultsForOrder
    from ._5840 import ResultsForOrderIncludingGroups
    from ._5841 import ResultsForOrderIncludingNodes
    from ._5842 import ResultsForOrderIncludingSurfaces
    from ._5843 import ResultsForResponseOfAComponentOrSurfaceInAHarmonic
    from ._5844 import ResultsForResponseOfANodeOnAHarmonic
    from ._5845 import ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic
    from ._5846 import RootAssemblyHarmonicAnalysisResultsPropertyAccessor
    from ._5847 import RootAssemblySingleWhineAnalysisResultsPropertyAccessor
    from ._5848 import SingleWhineAnalysisResultsPropertyAccessor
else:
    import_structure = {
        '_5824': ['AbstractSingleWhineAnalysisResultsPropertyAccessor'],
        '_5825': ['DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic'],
        '_5826': ['DataPointForResponseOfANodeAtAFrequencyToAHarmonic'],
        '_5827': ['FEPartHarmonicAnalysisResultsPropertyAccessor'],
        '_5828': ['FEPartSingleWhineAnalysisResultsPropertyAccessor'],
        '_5829': ['HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic'],
        '_5830': ['HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic'],
        '_5831': ['HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic'],
        '_5832': ['HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic'],
        '_5833': ['HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic'],
        '_5834': ['HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic'],
        '_5835': ['HarmonicAnalysisResultsPropertyAccessor'],
        '_5836': ['ResultsForMultipleOrders'],
        '_5837': ['ResultsForMultipleOrdersForFESurface'],
        '_5838': ['ResultsForMultipleOrdersForGroups'],
        '_5839': ['ResultsForOrder'],
        '_5840': ['ResultsForOrderIncludingGroups'],
        '_5841': ['ResultsForOrderIncludingNodes'],
        '_5842': ['ResultsForOrderIncludingSurfaces'],
        '_5843': ['ResultsForResponseOfAComponentOrSurfaceInAHarmonic'],
        '_5844': ['ResultsForResponseOfANodeOnAHarmonic'],
        '_5845': ['ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic'],
        '_5846': ['RootAssemblyHarmonicAnalysisResultsPropertyAccessor'],
        '_5847': ['RootAssemblySingleWhineAnalysisResultsPropertyAccessor'],
        '_5848': ['SingleWhineAnalysisResultsPropertyAccessor'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
