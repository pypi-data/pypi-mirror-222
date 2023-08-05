"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._449 import AGMAScuffingResultsRow
    from ._450 import CylindricalGearDesignAndRatingSettings
    from ._451 import CylindricalGearDesignAndRatingSettingsDatabase
    from ._452 import CylindricalGearDesignAndRatingSettingsItem
    from ._453 import CylindricalGearDutyCycleRating
    from ._454 import CylindricalGearFlankDutyCycleRating
    from ._455 import CylindricalGearFlankRating
    from ._456 import CylindricalGearMeshRating
    from ._457 import CylindricalGearMicroPittingResults
    from ._458 import CylindricalGearRating
    from ._459 import CylindricalGearRatingGeometryDataSource
    from ._460 import CylindricalGearScuffingResults
    from ._461 import CylindricalGearSetDutyCycleRating
    from ._462 import CylindricalGearSetRating
    from ._463 import CylindricalGearSingleFlankRating
    from ._464 import CylindricalMeshDutyCycleRating
    from ._465 import CylindricalMeshSingleFlankRating
    from ._466 import CylindricalPlasticGearRatingSettings
    from ._467 import CylindricalPlasticGearRatingSettingsDatabase
    from ._468 import CylindricalPlasticGearRatingSettingsItem
    from ._469 import CylindricalRateableMesh
    from ._470 import DynamicFactorMethods
    from ._471 import GearBlankFactorCalculationOptions
    from ._472 import ISOScuffingResultsRow
    from ._473 import MeshRatingForReports
    from ._474 import MicropittingRatingMethod
    from ._475 import MicroPittingResultsRow
    from ._476 import MisalignmentContactPatternEnhancements
    from ._477 import RatingMethod
    from ._478 import ScuffingFlashTemperatureRatingMethod
    from ._479 import ScuffingIntegralTemperatureRatingMethod
    from ._480 import ScuffingMethods
    from ._481 import ScuffingResultsRow
    from ._482 import ScuffingResultsRowGear
    from ._483 import TipReliefScuffingOptions
    from ._484 import ToothThicknesses
    from ._485 import VDI2737SafetyFactorReportingObject
else:
    import_structure = {
        '_449': ['AGMAScuffingResultsRow'],
        '_450': ['CylindricalGearDesignAndRatingSettings'],
        '_451': ['CylindricalGearDesignAndRatingSettingsDatabase'],
        '_452': ['CylindricalGearDesignAndRatingSettingsItem'],
        '_453': ['CylindricalGearDutyCycleRating'],
        '_454': ['CylindricalGearFlankDutyCycleRating'],
        '_455': ['CylindricalGearFlankRating'],
        '_456': ['CylindricalGearMeshRating'],
        '_457': ['CylindricalGearMicroPittingResults'],
        '_458': ['CylindricalGearRating'],
        '_459': ['CylindricalGearRatingGeometryDataSource'],
        '_460': ['CylindricalGearScuffingResults'],
        '_461': ['CylindricalGearSetDutyCycleRating'],
        '_462': ['CylindricalGearSetRating'],
        '_463': ['CylindricalGearSingleFlankRating'],
        '_464': ['CylindricalMeshDutyCycleRating'],
        '_465': ['CylindricalMeshSingleFlankRating'],
        '_466': ['CylindricalPlasticGearRatingSettings'],
        '_467': ['CylindricalPlasticGearRatingSettingsDatabase'],
        '_468': ['CylindricalPlasticGearRatingSettingsItem'],
        '_469': ['CylindricalRateableMesh'],
        '_470': ['DynamicFactorMethods'],
        '_471': ['GearBlankFactorCalculationOptions'],
        '_472': ['ISOScuffingResultsRow'],
        '_473': ['MeshRatingForReports'],
        '_474': ['MicropittingRatingMethod'],
        '_475': ['MicroPittingResultsRow'],
        '_476': ['MisalignmentContactPatternEnhancements'],
        '_477': ['RatingMethod'],
        '_478': ['ScuffingFlashTemperatureRatingMethod'],
        '_479': ['ScuffingIntegralTemperatureRatingMethod'],
        '_480': ['ScuffingMethods'],
        '_481': ['ScuffingResultsRow'],
        '_482': ['ScuffingResultsRowGear'],
        '_483': ['TipReliefScuffingOptions'],
        '_484': ['ToothThicknesses'],
        '_485': ['VDI2737SafetyFactorReportingObject'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
