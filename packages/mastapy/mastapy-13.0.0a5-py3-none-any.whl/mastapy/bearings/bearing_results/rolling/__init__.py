"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1953 import BallBearingAnalysisMethod
    from ._1954 import BallBearingContactCalculation
    from ._1955 import BallBearingRaceContactGeometry
    from ._1956 import DIN7322010Results
    from ._1957 import ForceAtLaminaGroupReportable
    from ._1958 import ForceAtLaminaReportable
    from ._1959 import FrictionModelForGyroscopicMoment
    from ._1960 import InternalClearance
    from ._1961 import ISO14179Settings
    from ._1962 import ISO14179SettingsDatabase
    from ._1963 import ISO14179SettingsPerBearingType
    from ._1964 import ISO153122018Results
    from ._1965 import ISOTR1417912001Results
    from ._1966 import ISOTR141792001Results
    from ._1967 import ISOTR1417922001Results
    from ._1968 import LoadedAbstractSphericalRollerBearingStripLoadResults
    from ._1969 import LoadedAngularContactBallBearingElement
    from ._1970 import LoadedAngularContactBallBearingResults
    from ._1971 import LoadedAngularContactBallBearingRow
    from ._1972 import LoadedAngularContactThrustBallBearingElement
    from ._1973 import LoadedAngularContactThrustBallBearingResults
    from ._1974 import LoadedAngularContactThrustBallBearingRow
    from ._1975 import LoadedAsymmetricSphericalRollerBearingElement
    from ._1976 import LoadedAsymmetricSphericalRollerBearingResults
    from ._1977 import LoadedAsymmetricSphericalRollerBearingRow
    from ._1978 import LoadedAsymmetricSphericalRollerBearingStripLoadResults
    from ._1979 import LoadedAxialThrustCylindricalRollerBearingDutyCycle
    from ._1980 import LoadedAxialThrustCylindricalRollerBearingElement
    from ._1981 import LoadedAxialThrustCylindricalRollerBearingResults
    from ._1982 import LoadedAxialThrustCylindricalRollerBearingRow
    from ._1983 import LoadedAxialThrustNeedleRollerBearingElement
    from ._1984 import LoadedAxialThrustNeedleRollerBearingResults
    from ._1985 import LoadedAxialThrustNeedleRollerBearingRow
    from ._1986 import LoadedBallBearingDutyCycle
    from ._1987 import LoadedBallBearingElement
    from ._1988 import LoadedBallBearingRaceResults
    from ._1989 import LoadedBallBearingResults
    from ._1990 import LoadedBallBearingRow
    from ._1991 import LoadedCrossedRollerBearingElement
    from ._1992 import LoadedCrossedRollerBearingResults
    from ._1993 import LoadedCrossedRollerBearingRow
    from ._1994 import LoadedCylindricalRollerBearingDutyCycle
    from ._1995 import LoadedCylindricalRollerBearingElement
    from ._1996 import LoadedCylindricalRollerBearingResults
    from ._1997 import LoadedCylindricalRollerBearingRow
    from ._1998 import LoadedDeepGrooveBallBearingElement
    from ._1999 import LoadedDeepGrooveBallBearingResults
    from ._2000 import LoadedDeepGrooveBallBearingRow
    from ._2001 import LoadedElement
    from ._2002 import LoadedFourPointContactBallBearingElement
    from ._2003 import LoadedFourPointContactBallBearingRaceResults
    from ._2004 import LoadedFourPointContactBallBearingResults
    from ._2005 import LoadedFourPointContactBallBearingRow
    from ._2006 import LoadedMultiPointContactBallBearingElement
    from ._2007 import LoadedNeedleRollerBearingElement
    from ._2008 import LoadedNeedleRollerBearingResults
    from ._2009 import LoadedNeedleRollerBearingRow
    from ._2010 import LoadedNonBarrelRollerBearingDutyCycle
    from ._2011 import LoadedNonBarrelRollerBearingResults
    from ._2012 import LoadedNonBarrelRollerBearingRow
    from ._2013 import LoadedNonBarrelRollerBearingStripLoadResults
    from ._2014 import LoadedNonBarrelRollerElement
    from ._2015 import LoadedRollerBearingElement
    from ._2016 import LoadedRollerBearingResults
    from ._2017 import LoadedRollerBearingRow
    from ._2018 import LoadedRollerStripLoadResults
    from ._2019 import LoadedRollingBearingRaceResults
    from ._2020 import LoadedRollingBearingResults
    from ._2021 import LoadedRollingBearingRow
    from ._2022 import LoadedSelfAligningBallBearingElement
    from ._2023 import LoadedSelfAligningBallBearingResults
    from ._2024 import LoadedSelfAligningBallBearingRow
    from ._2025 import LoadedSphericalRadialRollerBearingElement
    from ._2026 import LoadedSphericalRollerBearingElement
    from ._2027 import LoadedSphericalRollerRadialBearingResults
    from ._2028 import LoadedSphericalRollerRadialBearingRow
    from ._2029 import LoadedSphericalRollerRadialBearingStripLoadResults
    from ._2030 import LoadedSphericalRollerThrustBearingResults
    from ._2031 import LoadedSphericalRollerThrustBearingRow
    from ._2032 import LoadedSphericalThrustRollerBearingElement
    from ._2033 import LoadedTaperRollerBearingDutyCycle
    from ._2034 import LoadedTaperRollerBearingElement
    from ._2035 import LoadedTaperRollerBearingResults
    from ._2036 import LoadedTaperRollerBearingRow
    from ._2037 import LoadedThreePointContactBallBearingElement
    from ._2038 import LoadedThreePointContactBallBearingResults
    from ._2039 import LoadedThreePointContactBallBearingRow
    from ._2040 import LoadedThrustBallBearingElement
    from ._2041 import LoadedThrustBallBearingResults
    from ._2042 import LoadedThrustBallBearingRow
    from ._2043 import LoadedToroidalRollerBearingElement
    from ._2044 import LoadedToroidalRollerBearingResults
    from ._2045 import LoadedToroidalRollerBearingRow
    from ._2046 import LoadedToroidalRollerBearingStripLoadResults
    from ._2047 import MaximumStaticContactStress
    from ._2048 import MaximumStaticContactStressDutyCycle
    from ._2049 import MaximumStaticContactStressResultsAbstract
    from ._2050 import MaxStripLoadStressObject
    from ._2051 import PermissibleContinuousAxialLoadResults
    from ._2052 import PowerRatingF1EstimationMethod
    from ._2053 import PreloadFactorLookupTable
    from ._2054 import ResultsAtRollerOffset
    from ._2055 import RingForceAndDisplacement
    from ._2056 import RollerAnalysisMethod
    from ._2057 import RollingBearingFrictionCoefficients
    from ._2058 import RollingBearingSpeedResults
    from ._2059 import SMTRibStressResults
    from ._2060 import StressAtPosition
    from ._2061 import ThreePointContactInternalClearance
    from ._2062 import TrackTruncationSafetyFactorResults
else:
    import_structure = {
        '_1953': ['BallBearingAnalysisMethod'],
        '_1954': ['BallBearingContactCalculation'],
        '_1955': ['BallBearingRaceContactGeometry'],
        '_1956': ['DIN7322010Results'],
        '_1957': ['ForceAtLaminaGroupReportable'],
        '_1958': ['ForceAtLaminaReportable'],
        '_1959': ['FrictionModelForGyroscopicMoment'],
        '_1960': ['InternalClearance'],
        '_1961': ['ISO14179Settings'],
        '_1962': ['ISO14179SettingsDatabase'],
        '_1963': ['ISO14179SettingsPerBearingType'],
        '_1964': ['ISO153122018Results'],
        '_1965': ['ISOTR1417912001Results'],
        '_1966': ['ISOTR141792001Results'],
        '_1967': ['ISOTR1417922001Results'],
        '_1968': ['LoadedAbstractSphericalRollerBearingStripLoadResults'],
        '_1969': ['LoadedAngularContactBallBearingElement'],
        '_1970': ['LoadedAngularContactBallBearingResults'],
        '_1971': ['LoadedAngularContactBallBearingRow'],
        '_1972': ['LoadedAngularContactThrustBallBearingElement'],
        '_1973': ['LoadedAngularContactThrustBallBearingResults'],
        '_1974': ['LoadedAngularContactThrustBallBearingRow'],
        '_1975': ['LoadedAsymmetricSphericalRollerBearingElement'],
        '_1976': ['LoadedAsymmetricSphericalRollerBearingResults'],
        '_1977': ['LoadedAsymmetricSphericalRollerBearingRow'],
        '_1978': ['LoadedAsymmetricSphericalRollerBearingStripLoadResults'],
        '_1979': ['LoadedAxialThrustCylindricalRollerBearingDutyCycle'],
        '_1980': ['LoadedAxialThrustCylindricalRollerBearingElement'],
        '_1981': ['LoadedAxialThrustCylindricalRollerBearingResults'],
        '_1982': ['LoadedAxialThrustCylindricalRollerBearingRow'],
        '_1983': ['LoadedAxialThrustNeedleRollerBearingElement'],
        '_1984': ['LoadedAxialThrustNeedleRollerBearingResults'],
        '_1985': ['LoadedAxialThrustNeedleRollerBearingRow'],
        '_1986': ['LoadedBallBearingDutyCycle'],
        '_1987': ['LoadedBallBearingElement'],
        '_1988': ['LoadedBallBearingRaceResults'],
        '_1989': ['LoadedBallBearingResults'],
        '_1990': ['LoadedBallBearingRow'],
        '_1991': ['LoadedCrossedRollerBearingElement'],
        '_1992': ['LoadedCrossedRollerBearingResults'],
        '_1993': ['LoadedCrossedRollerBearingRow'],
        '_1994': ['LoadedCylindricalRollerBearingDutyCycle'],
        '_1995': ['LoadedCylindricalRollerBearingElement'],
        '_1996': ['LoadedCylindricalRollerBearingResults'],
        '_1997': ['LoadedCylindricalRollerBearingRow'],
        '_1998': ['LoadedDeepGrooveBallBearingElement'],
        '_1999': ['LoadedDeepGrooveBallBearingResults'],
        '_2000': ['LoadedDeepGrooveBallBearingRow'],
        '_2001': ['LoadedElement'],
        '_2002': ['LoadedFourPointContactBallBearingElement'],
        '_2003': ['LoadedFourPointContactBallBearingRaceResults'],
        '_2004': ['LoadedFourPointContactBallBearingResults'],
        '_2005': ['LoadedFourPointContactBallBearingRow'],
        '_2006': ['LoadedMultiPointContactBallBearingElement'],
        '_2007': ['LoadedNeedleRollerBearingElement'],
        '_2008': ['LoadedNeedleRollerBearingResults'],
        '_2009': ['LoadedNeedleRollerBearingRow'],
        '_2010': ['LoadedNonBarrelRollerBearingDutyCycle'],
        '_2011': ['LoadedNonBarrelRollerBearingResults'],
        '_2012': ['LoadedNonBarrelRollerBearingRow'],
        '_2013': ['LoadedNonBarrelRollerBearingStripLoadResults'],
        '_2014': ['LoadedNonBarrelRollerElement'],
        '_2015': ['LoadedRollerBearingElement'],
        '_2016': ['LoadedRollerBearingResults'],
        '_2017': ['LoadedRollerBearingRow'],
        '_2018': ['LoadedRollerStripLoadResults'],
        '_2019': ['LoadedRollingBearingRaceResults'],
        '_2020': ['LoadedRollingBearingResults'],
        '_2021': ['LoadedRollingBearingRow'],
        '_2022': ['LoadedSelfAligningBallBearingElement'],
        '_2023': ['LoadedSelfAligningBallBearingResults'],
        '_2024': ['LoadedSelfAligningBallBearingRow'],
        '_2025': ['LoadedSphericalRadialRollerBearingElement'],
        '_2026': ['LoadedSphericalRollerBearingElement'],
        '_2027': ['LoadedSphericalRollerRadialBearingResults'],
        '_2028': ['LoadedSphericalRollerRadialBearingRow'],
        '_2029': ['LoadedSphericalRollerRadialBearingStripLoadResults'],
        '_2030': ['LoadedSphericalRollerThrustBearingResults'],
        '_2031': ['LoadedSphericalRollerThrustBearingRow'],
        '_2032': ['LoadedSphericalThrustRollerBearingElement'],
        '_2033': ['LoadedTaperRollerBearingDutyCycle'],
        '_2034': ['LoadedTaperRollerBearingElement'],
        '_2035': ['LoadedTaperRollerBearingResults'],
        '_2036': ['LoadedTaperRollerBearingRow'],
        '_2037': ['LoadedThreePointContactBallBearingElement'],
        '_2038': ['LoadedThreePointContactBallBearingResults'],
        '_2039': ['LoadedThreePointContactBallBearingRow'],
        '_2040': ['LoadedThrustBallBearingElement'],
        '_2041': ['LoadedThrustBallBearingResults'],
        '_2042': ['LoadedThrustBallBearingRow'],
        '_2043': ['LoadedToroidalRollerBearingElement'],
        '_2044': ['LoadedToroidalRollerBearingResults'],
        '_2045': ['LoadedToroidalRollerBearingRow'],
        '_2046': ['LoadedToroidalRollerBearingStripLoadResults'],
        '_2047': ['MaximumStaticContactStress'],
        '_2048': ['MaximumStaticContactStressDutyCycle'],
        '_2049': ['MaximumStaticContactStressResultsAbstract'],
        '_2050': ['MaxStripLoadStressObject'],
        '_2051': ['PermissibleContinuousAxialLoadResults'],
        '_2052': ['PowerRatingF1EstimationMethod'],
        '_2053': ['PreloadFactorLookupTable'],
        '_2054': ['ResultsAtRollerOffset'],
        '_2055': ['RingForceAndDisplacement'],
        '_2056': ['RollerAnalysisMethod'],
        '_2057': ['RollingBearingFrictionCoefficients'],
        '_2058': ['RollingBearingSpeedResults'],
        '_2059': ['SMTRibStressResults'],
        '_2060': ['StressAtPosition'],
        '_2061': ['ThreePointContactInternalClearance'],
        '_2062': ['TrackTruncationSafetyFactorResults'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
