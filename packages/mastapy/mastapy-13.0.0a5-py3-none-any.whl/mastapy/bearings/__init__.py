"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1856 import BearingCatalog
    from ._1857 import BasicDynamicLoadRatingCalculationMethod
    from ._1858 import BasicStaticLoadRatingCalculationMethod
    from ._1859 import BearingCageMaterial
    from ._1860 import BearingDampingMatrixOption
    from ._1861 import BearingLoadCaseResultsForPST
    from ._1862 import BearingLoadCaseResultsLightweight
    from ._1863 import BearingMeasurementType
    from ._1864 import BearingModel
    from ._1865 import BearingRow
    from ._1866 import BearingSettings
    from ._1867 import BearingSettingsDatabase
    from ._1868 import BearingSettingsItem
    from ._1869 import BearingStiffnessMatrixOption
    from ._1870 import ExponentAndReductionFactorsInISO16281Calculation
    from ._1871 import FluidFilmTemperatureOptions
    from ._1872 import HybridSteelAll
    from ._1873 import JournalBearingType
    from ._1874 import JournalOilFeedType
    from ._1875 import MountingPointSurfaceFinishes
    from ._1876 import OuterRingMounting
    from ._1877 import RatingLife
    from ._1878 import RollerBearingProfileTypes
    from ._1879 import RollingBearingArrangement
    from ._1880 import RollingBearingDatabase
    from ._1881 import RollingBearingKey
    from ._1882 import RollingBearingRaceType
    from ._1883 import RollingBearingType
    from ._1884 import RotationalDirections
    from ._1885 import SealLocation
    from ._1886 import SKFSettings
    from ._1887 import TiltingPadTypes
else:
    import_structure = {
        '_1856': ['BearingCatalog'],
        '_1857': ['BasicDynamicLoadRatingCalculationMethod'],
        '_1858': ['BasicStaticLoadRatingCalculationMethod'],
        '_1859': ['BearingCageMaterial'],
        '_1860': ['BearingDampingMatrixOption'],
        '_1861': ['BearingLoadCaseResultsForPST'],
        '_1862': ['BearingLoadCaseResultsLightweight'],
        '_1863': ['BearingMeasurementType'],
        '_1864': ['BearingModel'],
        '_1865': ['BearingRow'],
        '_1866': ['BearingSettings'],
        '_1867': ['BearingSettingsDatabase'],
        '_1868': ['BearingSettingsItem'],
        '_1869': ['BearingStiffnessMatrixOption'],
        '_1870': ['ExponentAndReductionFactorsInISO16281Calculation'],
        '_1871': ['FluidFilmTemperatureOptions'],
        '_1872': ['HybridSteelAll'],
        '_1873': ['JournalBearingType'],
        '_1874': ['JournalOilFeedType'],
        '_1875': ['MountingPointSurfaceFinishes'],
        '_1876': ['OuterRingMounting'],
        '_1877': ['RatingLife'],
        '_1878': ['RollerBearingProfileTypes'],
        '_1879': ['RollingBearingArrangement'],
        '_1880': ['RollingBearingDatabase'],
        '_1881': ['RollingBearingKey'],
        '_1882': ['RollingBearingRaceType'],
        '_1883': ['RollingBearingType'],
        '_1884': ['RotationalDirections'],
        '_1885': ['SealLocation'],
        '_1886': ['SKFSettings'],
        '_1887': ['TiltingPadTypes'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
