"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7501 import AnalysisCase
    from ._7502 import AbstractAnalysisOptions
    from ._7503 import CompoundAnalysisCase
    from ._7504 import ConnectionAnalysisCase
    from ._7505 import ConnectionCompoundAnalysis
    from ._7506 import ConnectionFEAnalysis
    from ._7507 import ConnectionStaticLoadAnalysisCase
    from ._7508 import ConnectionTimeSeriesLoadAnalysisCase
    from ._7509 import DesignEntityCompoundAnalysis
    from ._7510 import FEAnalysis
    from ._7511 import PartAnalysisCase
    from ._7512 import PartCompoundAnalysis
    from ._7513 import PartFEAnalysis
    from ._7514 import PartStaticLoadAnalysisCase
    from ._7515 import PartTimeSeriesLoadAnalysisCase
    from ._7516 import StaticLoadAnalysisCase
    from ._7517 import TimeSeriesLoadAnalysisCase
else:
    import_structure = {
        '_7501': ['AnalysisCase'],
        '_7502': ['AbstractAnalysisOptions'],
        '_7503': ['CompoundAnalysisCase'],
        '_7504': ['ConnectionAnalysisCase'],
        '_7505': ['ConnectionCompoundAnalysis'],
        '_7506': ['ConnectionFEAnalysis'],
        '_7507': ['ConnectionStaticLoadAnalysisCase'],
        '_7508': ['ConnectionTimeSeriesLoadAnalysisCase'],
        '_7509': ['DesignEntityCompoundAnalysis'],
        '_7510': ['FEAnalysis'],
        '_7511': ['PartAnalysisCase'],
        '_7512': ['PartCompoundAnalysis'],
        '_7513': ['PartFEAnalysis'],
        '_7514': ['PartStaticLoadAnalysisCase'],
        '_7515': ['PartTimeSeriesLoadAnalysisCase'],
        '_7516': ['StaticLoadAnalysisCase'],
        '_7517': ['TimeSeriesLoadAnalysisCase'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
