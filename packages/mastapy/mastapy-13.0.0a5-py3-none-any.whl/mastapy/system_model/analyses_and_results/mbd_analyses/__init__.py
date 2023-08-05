"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5350 import AbstractAssemblyMultibodyDynamicsAnalysis
    from ._5351 import AbstractShaftMultibodyDynamicsAnalysis
    from ._5352 import AbstractShaftOrHousingMultibodyDynamicsAnalysis
    from ._5353 import AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
    from ._5354 import AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
    from ._5355 import AGMAGleasonConicalGearMultibodyDynamicsAnalysis
    from ._5356 import AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
    from ._5357 import AnalysisTypes
    from ._5358 import AssemblyMultibodyDynamicsAnalysis
    from ._5359 import BearingMultibodyDynamicsAnalysis
    from ._5360 import BearingStiffnessModel
    from ._5361 import BeltConnectionMultibodyDynamicsAnalysis
    from ._5362 import BeltDriveMultibodyDynamicsAnalysis
    from ._5363 import BevelDifferentialGearMeshMultibodyDynamicsAnalysis
    from ._5364 import BevelDifferentialGearMultibodyDynamicsAnalysis
    from ._5365 import BevelDifferentialGearSetMultibodyDynamicsAnalysis
    from ._5366 import BevelDifferentialPlanetGearMultibodyDynamicsAnalysis
    from ._5367 import BevelDifferentialSunGearMultibodyDynamicsAnalysis
    from ._5368 import BevelGearMeshMultibodyDynamicsAnalysis
    from ._5369 import BevelGearMultibodyDynamicsAnalysis
    from ._5370 import BevelGearSetMultibodyDynamicsAnalysis
    from ._5371 import BoltedJointMultibodyDynamicsAnalysis
    from ._5372 import BoltMultibodyDynamicsAnalysis
    from ._5373 import ClutchConnectionMultibodyDynamicsAnalysis
    from ._5374 import ClutchHalfMultibodyDynamicsAnalysis
    from ._5375 import ClutchMultibodyDynamicsAnalysis
    from ._5376 import ClutchSpringType
    from ._5377 import CoaxialConnectionMultibodyDynamicsAnalysis
    from ._5378 import ComponentMultibodyDynamicsAnalysis
    from ._5379 import ConceptCouplingConnectionMultibodyDynamicsAnalysis
    from ._5380 import ConceptCouplingHalfMultibodyDynamicsAnalysis
    from ._5381 import ConceptCouplingMultibodyDynamicsAnalysis
    from ._5382 import ConceptGearMeshMultibodyDynamicsAnalysis
    from ._5383 import ConceptGearMultibodyDynamicsAnalysis
    from ._5384 import ConceptGearSetMultibodyDynamicsAnalysis
    from ._5385 import ConicalGearMeshMultibodyDynamicsAnalysis
    from ._5386 import ConicalGearMultibodyDynamicsAnalysis
    from ._5387 import ConicalGearSetMultibodyDynamicsAnalysis
    from ._5388 import ConnectionMultibodyDynamicsAnalysis
    from ._5389 import ConnectorMultibodyDynamicsAnalysis
    from ._5390 import CouplingConnectionMultibodyDynamicsAnalysis
    from ._5391 import CouplingHalfMultibodyDynamicsAnalysis
    from ._5392 import CouplingMultibodyDynamicsAnalysis
    from ._5393 import CVTBeltConnectionMultibodyDynamicsAnalysis
    from ._5394 import CVTMultibodyDynamicsAnalysis
    from ._5395 import CVTPulleyMultibodyDynamicsAnalysis
    from ._5396 import CycloidalAssemblyMultibodyDynamicsAnalysis
    from ._5397 import CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis
    from ._5398 import CycloidalDiscMultibodyDynamicsAnalysis
    from ._5399 import CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis
    from ._5400 import CylindricalGearMeshMultibodyDynamicsAnalysis
    from ._5401 import CylindricalGearMultibodyDynamicsAnalysis
    from ._5402 import CylindricalGearSetMultibodyDynamicsAnalysis
    from ._5403 import CylindricalPlanetGearMultibodyDynamicsAnalysis
    from ._5404 import DatumMultibodyDynamicsAnalysis
    from ._5405 import ExternalCADModelMultibodyDynamicsAnalysis
    from ._5406 import FaceGearMeshMultibodyDynamicsAnalysis
    from ._5407 import FaceGearMultibodyDynamicsAnalysis
    from ._5408 import FaceGearSetMultibodyDynamicsAnalysis
    from ._5409 import FEPartMultibodyDynamicsAnalysis
    from ._5410 import FlexiblePinAssemblyMultibodyDynamicsAnalysis
    from ._5411 import GearMeshMultibodyDynamicsAnalysis
    from ._5412 import GearMeshStiffnessModel
    from ._5413 import GearMultibodyDynamicsAnalysis
    from ._5414 import GearSetMultibodyDynamicsAnalysis
    from ._5415 import GuideDxfModelMultibodyDynamicsAnalysis
    from ._5416 import HypoidGearMeshMultibodyDynamicsAnalysis
    from ._5417 import HypoidGearMultibodyDynamicsAnalysis
    from ._5418 import HypoidGearSetMultibodyDynamicsAnalysis
    from ._5419 import InertiaAdjustedLoadCasePeriodMethod
    from ._5420 import InertiaAdjustedLoadCaseResultsToCreate
    from ._5421 import InputSignalFilterLevel
    from ._5422 import InputVelocityForRunUpProcessingType
    from ._5423 import InterMountableComponentConnectionMultibodyDynamicsAnalysis
    from ._5424 import KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis
    from ._5425 import KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis
    from ._5426 import KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis
    from ._5427 import KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis
    from ._5428 import KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis
    from ._5429 import KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis
    from ._5430 import KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis
    from ._5431 import KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis
    from ._5432 import KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis
    from ._5433 import MassDiscMultibodyDynamicsAnalysis
    from ._5434 import MBDAnalysisDrawStyle
    from ._5435 import MBDAnalysisOptions
    from ._5436 import MBDRunUpAnalysisOptions
    from ._5437 import MeasurementComponentMultibodyDynamicsAnalysis
    from ._5438 import MountableComponentMultibodyDynamicsAnalysis
    from ._2621 import MultibodyDynamicsAnalysis
    from ._5439 import OilSealMultibodyDynamicsAnalysis
    from ._5440 import PartMultibodyDynamicsAnalysis
    from ._5441 import PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis
    from ._5442 import PartToPartShearCouplingHalfMultibodyDynamicsAnalysis
    from ._5443 import PartToPartShearCouplingMultibodyDynamicsAnalysis
    from ._5444 import PlanetaryConnectionMultibodyDynamicsAnalysis
    from ._5445 import PlanetaryGearSetMultibodyDynamicsAnalysis
    from ._5446 import PlanetCarrierMultibodyDynamicsAnalysis
    from ._5447 import PointLoadMultibodyDynamicsAnalysis
    from ._5448 import PowerLoadMultibodyDynamicsAnalysis
    from ._5449 import PulleyMultibodyDynamicsAnalysis
    from ._5450 import RingPinsMultibodyDynamicsAnalysis
    from ._5451 import RingPinsToDiscConnectionMultibodyDynamicsAnalysis
    from ._5452 import RollingRingAssemblyMultibodyDynamicsAnalysis
    from ._5453 import RollingRingConnectionMultibodyDynamicsAnalysis
    from ._5454 import RollingRingMultibodyDynamicsAnalysis
    from ._5455 import RootAssemblyMultibodyDynamicsAnalysis
    from ._5456 import RunUpDrivingMode
    from ._5457 import ShaftAndHousingFlexibilityOption
    from ._5458 import ShaftHubConnectionMultibodyDynamicsAnalysis
    from ._5459 import ShaftMultibodyDynamicsAnalysis
    from ._5460 import ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
    from ._5461 import ShapeOfInitialAccelerationPeriodForRunUp
    from ._5462 import SpecialisedAssemblyMultibodyDynamicsAnalysis
    from ._5463 import SpiralBevelGearMeshMultibodyDynamicsAnalysis
    from ._5464 import SpiralBevelGearMultibodyDynamicsAnalysis
    from ._5465 import SpiralBevelGearSetMultibodyDynamicsAnalysis
    from ._5466 import SpringDamperConnectionMultibodyDynamicsAnalysis
    from ._5467 import SpringDamperHalfMultibodyDynamicsAnalysis
    from ._5468 import SpringDamperMultibodyDynamicsAnalysis
    from ._5469 import StraightBevelDiffGearMeshMultibodyDynamicsAnalysis
    from ._5470 import StraightBevelDiffGearMultibodyDynamicsAnalysis
    from ._5471 import StraightBevelDiffGearSetMultibodyDynamicsAnalysis
    from ._5472 import StraightBevelGearMeshMultibodyDynamicsAnalysis
    from ._5473 import StraightBevelGearMultibodyDynamicsAnalysis
    from ._5474 import StraightBevelGearSetMultibodyDynamicsAnalysis
    from ._5475 import StraightBevelPlanetGearMultibodyDynamicsAnalysis
    from ._5476 import StraightBevelSunGearMultibodyDynamicsAnalysis
    from ._5477 import SynchroniserHalfMultibodyDynamicsAnalysis
    from ._5478 import SynchroniserMultibodyDynamicsAnalysis
    from ._5479 import SynchroniserPartMultibodyDynamicsAnalysis
    from ._5480 import SynchroniserSleeveMultibodyDynamicsAnalysis
    from ._5481 import TorqueConverterConnectionMultibodyDynamicsAnalysis
    from ._5482 import TorqueConverterLockupRule
    from ._5483 import TorqueConverterMultibodyDynamicsAnalysis
    from ._5484 import TorqueConverterPumpMultibodyDynamicsAnalysis
    from ._5485 import TorqueConverterStatus
    from ._5486 import TorqueConverterTurbineMultibodyDynamicsAnalysis
    from ._5487 import UnbalancedMassMultibodyDynamicsAnalysis
    from ._5488 import VirtualComponentMultibodyDynamicsAnalysis
    from ._5489 import WheelSlipType
    from ._5490 import WormGearMeshMultibodyDynamicsAnalysis
    from ._5491 import WormGearMultibodyDynamicsAnalysis
    from ._5492 import WormGearSetMultibodyDynamicsAnalysis
    from ._5493 import ZerolBevelGearMeshMultibodyDynamicsAnalysis
    from ._5494 import ZerolBevelGearMultibodyDynamicsAnalysis
    from ._5495 import ZerolBevelGearSetMultibodyDynamicsAnalysis
else:
    import_structure = {
        '_5350': ['AbstractAssemblyMultibodyDynamicsAnalysis'],
        '_5351': ['AbstractShaftMultibodyDynamicsAnalysis'],
        '_5352': ['AbstractShaftOrHousingMultibodyDynamicsAnalysis'],
        '_5353': ['AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis'],
        '_5354': ['AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis'],
        '_5355': ['AGMAGleasonConicalGearMultibodyDynamicsAnalysis'],
        '_5356': ['AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis'],
        '_5357': ['AnalysisTypes'],
        '_5358': ['AssemblyMultibodyDynamicsAnalysis'],
        '_5359': ['BearingMultibodyDynamicsAnalysis'],
        '_5360': ['BearingStiffnessModel'],
        '_5361': ['BeltConnectionMultibodyDynamicsAnalysis'],
        '_5362': ['BeltDriveMultibodyDynamicsAnalysis'],
        '_5363': ['BevelDifferentialGearMeshMultibodyDynamicsAnalysis'],
        '_5364': ['BevelDifferentialGearMultibodyDynamicsAnalysis'],
        '_5365': ['BevelDifferentialGearSetMultibodyDynamicsAnalysis'],
        '_5366': ['BevelDifferentialPlanetGearMultibodyDynamicsAnalysis'],
        '_5367': ['BevelDifferentialSunGearMultibodyDynamicsAnalysis'],
        '_5368': ['BevelGearMeshMultibodyDynamicsAnalysis'],
        '_5369': ['BevelGearMultibodyDynamicsAnalysis'],
        '_5370': ['BevelGearSetMultibodyDynamicsAnalysis'],
        '_5371': ['BoltedJointMultibodyDynamicsAnalysis'],
        '_5372': ['BoltMultibodyDynamicsAnalysis'],
        '_5373': ['ClutchConnectionMultibodyDynamicsAnalysis'],
        '_5374': ['ClutchHalfMultibodyDynamicsAnalysis'],
        '_5375': ['ClutchMultibodyDynamicsAnalysis'],
        '_5376': ['ClutchSpringType'],
        '_5377': ['CoaxialConnectionMultibodyDynamicsAnalysis'],
        '_5378': ['ComponentMultibodyDynamicsAnalysis'],
        '_5379': ['ConceptCouplingConnectionMultibodyDynamicsAnalysis'],
        '_5380': ['ConceptCouplingHalfMultibodyDynamicsAnalysis'],
        '_5381': ['ConceptCouplingMultibodyDynamicsAnalysis'],
        '_5382': ['ConceptGearMeshMultibodyDynamicsAnalysis'],
        '_5383': ['ConceptGearMultibodyDynamicsAnalysis'],
        '_5384': ['ConceptGearSetMultibodyDynamicsAnalysis'],
        '_5385': ['ConicalGearMeshMultibodyDynamicsAnalysis'],
        '_5386': ['ConicalGearMultibodyDynamicsAnalysis'],
        '_5387': ['ConicalGearSetMultibodyDynamicsAnalysis'],
        '_5388': ['ConnectionMultibodyDynamicsAnalysis'],
        '_5389': ['ConnectorMultibodyDynamicsAnalysis'],
        '_5390': ['CouplingConnectionMultibodyDynamicsAnalysis'],
        '_5391': ['CouplingHalfMultibodyDynamicsAnalysis'],
        '_5392': ['CouplingMultibodyDynamicsAnalysis'],
        '_5393': ['CVTBeltConnectionMultibodyDynamicsAnalysis'],
        '_5394': ['CVTMultibodyDynamicsAnalysis'],
        '_5395': ['CVTPulleyMultibodyDynamicsAnalysis'],
        '_5396': ['CycloidalAssemblyMultibodyDynamicsAnalysis'],
        '_5397': ['CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis'],
        '_5398': ['CycloidalDiscMultibodyDynamicsAnalysis'],
        '_5399': ['CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis'],
        '_5400': ['CylindricalGearMeshMultibodyDynamicsAnalysis'],
        '_5401': ['CylindricalGearMultibodyDynamicsAnalysis'],
        '_5402': ['CylindricalGearSetMultibodyDynamicsAnalysis'],
        '_5403': ['CylindricalPlanetGearMultibodyDynamicsAnalysis'],
        '_5404': ['DatumMultibodyDynamicsAnalysis'],
        '_5405': ['ExternalCADModelMultibodyDynamicsAnalysis'],
        '_5406': ['FaceGearMeshMultibodyDynamicsAnalysis'],
        '_5407': ['FaceGearMultibodyDynamicsAnalysis'],
        '_5408': ['FaceGearSetMultibodyDynamicsAnalysis'],
        '_5409': ['FEPartMultibodyDynamicsAnalysis'],
        '_5410': ['FlexiblePinAssemblyMultibodyDynamicsAnalysis'],
        '_5411': ['GearMeshMultibodyDynamicsAnalysis'],
        '_5412': ['GearMeshStiffnessModel'],
        '_5413': ['GearMultibodyDynamicsAnalysis'],
        '_5414': ['GearSetMultibodyDynamicsAnalysis'],
        '_5415': ['GuideDxfModelMultibodyDynamicsAnalysis'],
        '_5416': ['HypoidGearMeshMultibodyDynamicsAnalysis'],
        '_5417': ['HypoidGearMultibodyDynamicsAnalysis'],
        '_5418': ['HypoidGearSetMultibodyDynamicsAnalysis'],
        '_5419': ['InertiaAdjustedLoadCasePeriodMethod'],
        '_5420': ['InertiaAdjustedLoadCaseResultsToCreate'],
        '_5421': ['InputSignalFilterLevel'],
        '_5422': ['InputVelocityForRunUpProcessingType'],
        '_5423': ['InterMountableComponentConnectionMultibodyDynamicsAnalysis'],
        '_5424': ['KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis'],
        '_5425': ['KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis'],
        '_5426': ['KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis'],
        '_5427': ['KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis'],
        '_5428': ['KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis'],
        '_5429': ['KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis'],
        '_5430': ['KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis'],
        '_5431': ['KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis'],
        '_5432': ['KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis'],
        '_5433': ['MassDiscMultibodyDynamicsAnalysis'],
        '_5434': ['MBDAnalysisDrawStyle'],
        '_5435': ['MBDAnalysisOptions'],
        '_5436': ['MBDRunUpAnalysisOptions'],
        '_5437': ['MeasurementComponentMultibodyDynamicsAnalysis'],
        '_5438': ['MountableComponentMultibodyDynamicsAnalysis'],
        '_2621': ['MultibodyDynamicsAnalysis'],
        '_5439': ['OilSealMultibodyDynamicsAnalysis'],
        '_5440': ['PartMultibodyDynamicsAnalysis'],
        '_5441': ['PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis'],
        '_5442': ['PartToPartShearCouplingHalfMultibodyDynamicsAnalysis'],
        '_5443': ['PartToPartShearCouplingMultibodyDynamicsAnalysis'],
        '_5444': ['PlanetaryConnectionMultibodyDynamicsAnalysis'],
        '_5445': ['PlanetaryGearSetMultibodyDynamicsAnalysis'],
        '_5446': ['PlanetCarrierMultibodyDynamicsAnalysis'],
        '_5447': ['PointLoadMultibodyDynamicsAnalysis'],
        '_5448': ['PowerLoadMultibodyDynamicsAnalysis'],
        '_5449': ['PulleyMultibodyDynamicsAnalysis'],
        '_5450': ['RingPinsMultibodyDynamicsAnalysis'],
        '_5451': ['RingPinsToDiscConnectionMultibodyDynamicsAnalysis'],
        '_5452': ['RollingRingAssemblyMultibodyDynamicsAnalysis'],
        '_5453': ['RollingRingConnectionMultibodyDynamicsAnalysis'],
        '_5454': ['RollingRingMultibodyDynamicsAnalysis'],
        '_5455': ['RootAssemblyMultibodyDynamicsAnalysis'],
        '_5456': ['RunUpDrivingMode'],
        '_5457': ['ShaftAndHousingFlexibilityOption'],
        '_5458': ['ShaftHubConnectionMultibodyDynamicsAnalysis'],
        '_5459': ['ShaftMultibodyDynamicsAnalysis'],
        '_5460': ['ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis'],
        '_5461': ['ShapeOfInitialAccelerationPeriodForRunUp'],
        '_5462': ['SpecialisedAssemblyMultibodyDynamicsAnalysis'],
        '_5463': ['SpiralBevelGearMeshMultibodyDynamicsAnalysis'],
        '_5464': ['SpiralBevelGearMultibodyDynamicsAnalysis'],
        '_5465': ['SpiralBevelGearSetMultibodyDynamicsAnalysis'],
        '_5466': ['SpringDamperConnectionMultibodyDynamicsAnalysis'],
        '_5467': ['SpringDamperHalfMultibodyDynamicsAnalysis'],
        '_5468': ['SpringDamperMultibodyDynamicsAnalysis'],
        '_5469': ['StraightBevelDiffGearMeshMultibodyDynamicsAnalysis'],
        '_5470': ['StraightBevelDiffGearMultibodyDynamicsAnalysis'],
        '_5471': ['StraightBevelDiffGearSetMultibodyDynamicsAnalysis'],
        '_5472': ['StraightBevelGearMeshMultibodyDynamicsAnalysis'],
        '_5473': ['StraightBevelGearMultibodyDynamicsAnalysis'],
        '_5474': ['StraightBevelGearSetMultibodyDynamicsAnalysis'],
        '_5475': ['StraightBevelPlanetGearMultibodyDynamicsAnalysis'],
        '_5476': ['StraightBevelSunGearMultibodyDynamicsAnalysis'],
        '_5477': ['SynchroniserHalfMultibodyDynamicsAnalysis'],
        '_5478': ['SynchroniserMultibodyDynamicsAnalysis'],
        '_5479': ['SynchroniserPartMultibodyDynamicsAnalysis'],
        '_5480': ['SynchroniserSleeveMultibodyDynamicsAnalysis'],
        '_5481': ['TorqueConverterConnectionMultibodyDynamicsAnalysis'],
        '_5482': ['TorqueConverterLockupRule'],
        '_5483': ['TorqueConverterMultibodyDynamicsAnalysis'],
        '_5484': ['TorqueConverterPumpMultibodyDynamicsAnalysis'],
        '_5485': ['TorqueConverterStatus'],
        '_5486': ['TorqueConverterTurbineMultibodyDynamicsAnalysis'],
        '_5487': ['UnbalancedMassMultibodyDynamicsAnalysis'],
        '_5488': ['VirtualComponentMultibodyDynamicsAnalysis'],
        '_5489': ['WheelSlipType'],
        '_5490': ['WormGearMeshMultibodyDynamicsAnalysis'],
        '_5491': ['WormGearMultibodyDynamicsAnalysis'],
        '_5492': ['WormGearSetMultibodyDynamicsAnalysis'],
        '_5493': ['ZerolBevelGearMeshMultibodyDynamicsAnalysis'],
        '_5494': ['ZerolBevelGearMultibodyDynamicsAnalysis'],
        '_5495': ['ZerolBevelGearSetMultibodyDynamicsAnalysis'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
