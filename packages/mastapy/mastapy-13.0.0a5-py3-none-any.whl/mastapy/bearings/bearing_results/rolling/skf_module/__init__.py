"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2063 import AdjustedSpeed
    from ._2064 import AdjustmentFactors
    from ._2065 import BearingLoads
    from ._2066 import BearingRatingLife
    from ._2067 import DynamicAxialLoadCarryingCapacity
    from ._2068 import Frequencies
    from ._2069 import FrequencyOfOverRolling
    from ._2070 import Friction
    from ._2071 import FrictionalMoment
    from ._2072 import FrictionSources
    from ._2073 import Grease
    from ._2074 import GreaseLifeAndRelubricationInterval
    from ._2075 import GreaseQuantity
    from ._2076 import InitialFill
    from ._2077 import LifeModel
    from ._2078 import MinimumLoad
    from ._2079 import OperatingViscosity
    from ._2080 import PermissibleAxialLoad
    from ._2081 import RotationalFrequency
    from ._2082 import SKFAuthentication
    from ._2083 import SKFCalculationResult
    from ._2084 import SKFCredentials
    from ._2085 import SKFModuleResults
    from ._2086 import StaticSafetyFactors
    from ._2087 import Viscosities
else:
    import_structure = {
        '_2063': ['AdjustedSpeed'],
        '_2064': ['AdjustmentFactors'],
        '_2065': ['BearingLoads'],
        '_2066': ['BearingRatingLife'],
        '_2067': ['DynamicAxialLoadCarryingCapacity'],
        '_2068': ['Frequencies'],
        '_2069': ['FrequencyOfOverRolling'],
        '_2070': ['Friction'],
        '_2071': ['FrictionalMoment'],
        '_2072': ['FrictionSources'],
        '_2073': ['Grease'],
        '_2074': ['GreaseLifeAndRelubricationInterval'],
        '_2075': ['GreaseQuantity'],
        '_2076': ['InitialFill'],
        '_2077': ['LifeModel'],
        '_2078': ['MinimumLoad'],
        '_2079': ['OperatingViscosity'],
        '_2080': ['PermissibleAxialLoad'],
        '_2081': ['RotationalFrequency'],
        '_2082': ['SKFAuthentication'],
        '_2083': ['SKFCalculationResult'],
        '_2084': ['SKFCredentials'],
        '_2085': ['SKFModuleResults'],
        '_2086': ['StaticSafetyFactors'],
        '_2087': ['Viscosities'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
