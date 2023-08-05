"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2122 import AngularContactBallBearing
    from ._2123 import AngularContactThrustBallBearing
    from ._2124 import AsymmetricSphericalRollerBearing
    from ._2125 import AxialThrustCylindricalRollerBearing
    from ._2126 import AxialThrustNeedleRollerBearing
    from ._2127 import BallBearing
    from ._2128 import BallBearingShoulderDefinition
    from ._2129 import BarrelRollerBearing
    from ._2130 import BearingProtection
    from ._2131 import BearingProtectionDetailsModifier
    from ._2132 import BearingProtectionLevel
    from ._2133 import BearingTypeExtraInformation
    from ._2134 import CageBridgeShape
    from ._2135 import CrossedRollerBearing
    from ._2136 import CylindricalRollerBearing
    from ._2137 import DeepGrooveBallBearing
    from ._2138 import DiameterSeries
    from ._2139 import FatigueLoadLimitCalculationMethodEnum
    from ._2140 import FourPointContactAngleDefinition
    from ._2141 import FourPointContactBallBearing
    from ._2142 import GeometricConstants
    from ._2143 import GeometricConstantsForRollingFrictionalMoments
    from ._2144 import GeometricConstantsForSlidingFrictionalMoments
    from ._2145 import HeightSeries
    from ._2146 import MultiPointContactBallBearing
    from ._2147 import NeedleRollerBearing
    from ._2148 import NonBarrelRollerBearing
    from ._2149 import RollerBearing
    from ._2150 import RollerEndShape
    from ._2151 import RollerRibDetail
    from ._2152 import RollingBearing
    from ._2153 import SelfAligningBallBearing
    from ._2154 import SKFSealFrictionalMomentConstants
    from ._2155 import SleeveType
    from ._2156 import SphericalRollerBearing
    from ._2157 import SphericalRollerThrustBearing
    from ._2158 import TaperRollerBearing
    from ._2159 import ThreePointContactBallBearing
    from ._2160 import ThrustBallBearing
    from ._2161 import ToroidalRollerBearing
    from ._2162 import WidthSeries
else:
    import_structure = {
        '_2122': ['AngularContactBallBearing'],
        '_2123': ['AngularContactThrustBallBearing'],
        '_2124': ['AsymmetricSphericalRollerBearing'],
        '_2125': ['AxialThrustCylindricalRollerBearing'],
        '_2126': ['AxialThrustNeedleRollerBearing'],
        '_2127': ['BallBearing'],
        '_2128': ['BallBearingShoulderDefinition'],
        '_2129': ['BarrelRollerBearing'],
        '_2130': ['BearingProtection'],
        '_2131': ['BearingProtectionDetailsModifier'],
        '_2132': ['BearingProtectionLevel'],
        '_2133': ['BearingTypeExtraInformation'],
        '_2134': ['CageBridgeShape'],
        '_2135': ['CrossedRollerBearing'],
        '_2136': ['CylindricalRollerBearing'],
        '_2137': ['DeepGrooveBallBearing'],
        '_2138': ['DiameterSeries'],
        '_2139': ['FatigueLoadLimitCalculationMethodEnum'],
        '_2140': ['FourPointContactAngleDefinition'],
        '_2141': ['FourPointContactBallBearing'],
        '_2142': ['GeometricConstants'],
        '_2143': ['GeometricConstantsForRollingFrictionalMoments'],
        '_2144': ['GeometricConstantsForSlidingFrictionalMoments'],
        '_2145': ['HeightSeries'],
        '_2146': ['MultiPointContactBallBearing'],
        '_2147': ['NeedleRollerBearing'],
        '_2148': ['NonBarrelRollerBearing'],
        '_2149': ['RollerBearing'],
        '_2150': ['RollerEndShape'],
        '_2151': ['RollerRibDetail'],
        '_2152': ['RollingBearing'],
        '_2153': ['SelfAligningBallBearing'],
        '_2154': ['SKFSealFrictionalMomentConstants'],
        '_2155': ['SleeveType'],
        '_2156': ['SphericalRollerBearing'],
        '_2157': ['SphericalRollerThrustBearing'],
        '_2158': ['TaperRollerBearing'],
        '_2159': ['ThreePointContactBallBearing'],
        '_2160': ['ThrustBallBearing'],
        '_2161': ['ToroidalRollerBearing'],
        '_2162': ['WidthSeries'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
