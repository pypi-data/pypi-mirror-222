"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6956 import AdditionalForcesObtainedFrom
    from ._6957 import BoostPressureLoadCaseInputOptions
    from ._6958 import DesignStateOptions
    from ._6959 import DestinationDesignState
    from ._6960 import ForceInputOptions
    from ._6961 import GearRatioInputOptions
    from ._6962 import LoadCaseNameOptions
    from ._6963 import MomentInputOptions
    from ._6964 import MultiTimeSeriesDataInputFileOptions
    from ._6965 import PointLoadInputOptions
    from ._6966 import PowerLoadInputOptions
    from ._6967 import RampOrSteadyStateInputOptions
    from ._6968 import SpeedInputOptions
    from ._6969 import TimeSeriesImporter
    from ._6970 import TimeStepInputOptions
    from ._6971 import TorqueInputOptions
    from ._6972 import TorqueValuesObtainedFrom
else:
    import_structure = {
        '_6956': ['AdditionalForcesObtainedFrom'],
        '_6957': ['BoostPressureLoadCaseInputOptions'],
        '_6958': ['DesignStateOptions'],
        '_6959': ['DestinationDesignState'],
        '_6960': ['ForceInputOptions'],
        '_6961': ['GearRatioInputOptions'],
        '_6962': ['LoadCaseNameOptions'],
        '_6963': ['MomentInputOptions'],
        '_6964': ['MultiTimeSeriesDataInputFileOptions'],
        '_6965': ['PointLoadInputOptions'],
        '_6966': ['PowerLoadInputOptions'],
        '_6967': ['RampOrSteadyStateInputOptions'],
        '_6968': ['SpeedInputOptions'],
        '_6969': ['TimeSeriesImporter'],
        '_6970': ['TimeStepInputOptions'],
        '_6971': ['TorqueInputOptions'],
        '_6972': ['TorqueValuesObtainedFrom'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
