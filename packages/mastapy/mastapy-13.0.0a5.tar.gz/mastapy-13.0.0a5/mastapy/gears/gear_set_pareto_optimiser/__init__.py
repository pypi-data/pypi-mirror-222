"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._899 import BarForPareto
    from ._900 import CandidateDisplayChoice
    from ._901 import ChartInfoBase
    from ._902 import CylindricalGearSetParetoOptimiser
    from ._903 import DesignSpaceSearchBase
    from ._904 import DesignSpaceSearchCandidateBase
    from ._905 import FaceGearSetParetoOptimiser
    from ._906 import GearNameMapper
    from ._907 import GearNamePicker
    from ._908 import GearSetOptimiserCandidate
    from ._909 import GearSetParetoOptimiser
    from ._910 import HypoidGearSetParetoOptimiser
    from ._911 import InputSliderForPareto
    from ._912 import LargerOrSmaller
    from ._913 import MicroGeometryDesignSpaceSearch
    from ._914 import MicroGeometryDesignSpaceSearchCandidate
    from ._915 import MicroGeometryDesignSpaceSearchChartInformation
    from ._916 import MicroGeometryGearSetDesignSpaceSearch
    from ._917 import MicroGeometryGearSetDesignSpaceSearchStrategyDatabase
    from ._918 import MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase
    from ._919 import OptimisationTarget
    from ._920 import ParetoConicalRatingOptimisationStrategyDatabase
    from ._921 import ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase
    from ._922 import ParetoCylindricalGearSetOptimisationStrategyDatabase
    from ._923 import ParetoCylindricalRatingOptimisationStrategyDatabase
    from ._924 import ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase
    from ._925 import ParetoFaceGearSetOptimisationStrategyDatabase
    from ._926 import ParetoFaceRatingOptimisationStrategyDatabase
    from ._927 import ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase
    from ._928 import ParetoHypoidGearSetOptimisationStrategyDatabase
    from ._929 import ParetoOptimiserChartInformation
    from ._930 import ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
    from ._931 import ParetoSpiralBevelGearSetOptimisationStrategyDatabase
    from ._932 import ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase
    from ._933 import ParetoStraightBevelGearSetOptimisationStrategyDatabase
    from ._934 import ReasonsForInvalidDesigns
    from ._935 import SpiralBevelGearSetParetoOptimiser
    from ._936 import StraightBevelGearSetParetoOptimiser
else:
    import_structure = {
        '_899': ['BarForPareto'],
        '_900': ['CandidateDisplayChoice'],
        '_901': ['ChartInfoBase'],
        '_902': ['CylindricalGearSetParetoOptimiser'],
        '_903': ['DesignSpaceSearchBase'],
        '_904': ['DesignSpaceSearchCandidateBase'],
        '_905': ['FaceGearSetParetoOptimiser'],
        '_906': ['GearNameMapper'],
        '_907': ['GearNamePicker'],
        '_908': ['GearSetOptimiserCandidate'],
        '_909': ['GearSetParetoOptimiser'],
        '_910': ['HypoidGearSetParetoOptimiser'],
        '_911': ['InputSliderForPareto'],
        '_912': ['LargerOrSmaller'],
        '_913': ['MicroGeometryDesignSpaceSearch'],
        '_914': ['MicroGeometryDesignSpaceSearchCandidate'],
        '_915': ['MicroGeometryDesignSpaceSearchChartInformation'],
        '_916': ['MicroGeometryGearSetDesignSpaceSearch'],
        '_917': ['MicroGeometryGearSetDesignSpaceSearchStrategyDatabase'],
        '_918': ['MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase'],
        '_919': ['OptimisationTarget'],
        '_920': ['ParetoConicalRatingOptimisationStrategyDatabase'],
        '_921': ['ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase'],
        '_922': ['ParetoCylindricalGearSetOptimisationStrategyDatabase'],
        '_923': ['ParetoCylindricalRatingOptimisationStrategyDatabase'],
        '_924': ['ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase'],
        '_925': ['ParetoFaceGearSetOptimisationStrategyDatabase'],
        '_926': ['ParetoFaceRatingOptimisationStrategyDatabase'],
        '_927': ['ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase'],
        '_928': ['ParetoHypoidGearSetOptimisationStrategyDatabase'],
        '_929': ['ParetoOptimiserChartInformation'],
        '_930': ['ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase'],
        '_931': ['ParetoSpiralBevelGearSetOptimisationStrategyDatabase'],
        '_932': ['ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase'],
        '_933': ['ParetoStraightBevelGearSetOptimisationStrategyDatabase'],
        '_934': ['ReasonsForInvalidDesigns'],
        '_935': ['SpiralBevelGearSetParetoOptimiser'],
        '_936': ['StraightBevelGearSetParetoOptimiser'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
