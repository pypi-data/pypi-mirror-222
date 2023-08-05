"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6376 import AbstractAssemblyCompoundDynamicAnalysis
    from ._6377 import AbstractShaftCompoundDynamicAnalysis
    from ._6378 import AbstractShaftOrHousingCompoundDynamicAnalysis
    from ._6379 import AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis
    from ._6380 import AGMAGleasonConicalGearCompoundDynamicAnalysis
    from ._6381 import AGMAGleasonConicalGearMeshCompoundDynamicAnalysis
    from ._6382 import AGMAGleasonConicalGearSetCompoundDynamicAnalysis
    from ._6383 import AssemblyCompoundDynamicAnalysis
    from ._6384 import BearingCompoundDynamicAnalysis
    from ._6385 import BeltConnectionCompoundDynamicAnalysis
    from ._6386 import BeltDriveCompoundDynamicAnalysis
    from ._6387 import BevelDifferentialGearCompoundDynamicAnalysis
    from ._6388 import BevelDifferentialGearMeshCompoundDynamicAnalysis
    from ._6389 import BevelDifferentialGearSetCompoundDynamicAnalysis
    from ._6390 import BevelDifferentialPlanetGearCompoundDynamicAnalysis
    from ._6391 import BevelDifferentialSunGearCompoundDynamicAnalysis
    from ._6392 import BevelGearCompoundDynamicAnalysis
    from ._6393 import BevelGearMeshCompoundDynamicAnalysis
    from ._6394 import BevelGearSetCompoundDynamicAnalysis
    from ._6395 import BoltCompoundDynamicAnalysis
    from ._6396 import BoltedJointCompoundDynamicAnalysis
    from ._6397 import ClutchCompoundDynamicAnalysis
    from ._6398 import ClutchConnectionCompoundDynamicAnalysis
    from ._6399 import ClutchHalfCompoundDynamicAnalysis
    from ._6400 import CoaxialConnectionCompoundDynamicAnalysis
    from ._6401 import ComponentCompoundDynamicAnalysis
    from ._6402 import ConceptCouplingCompoundDynamicAnalysis
    from ._6403 import ConceptCouplingConnectionCompoundDynamicAnalysis
    from ._6404 import ConceptCouplingHalfCompoundDynamicAnalysis
    from ._6405 import ConceptGearCompoundDynamicAnalysis
    from ._6406 import ConceptGearMeshCompoundDynamicAnalysis
    from ._6407 import ConceptGearSetCompoundDynamicAnalysis
    from ._6408 import ConicalGearCompoundDynamicAnalysis
    from ._6409 import ConicalGearMeshCompoundDynamicAnalysis
    from ._6410 import ConicalGearSetCompoundDynamicAnalysis
    from ._6411 import ConnectionCompoundDynamicAnalysis
    from ._6412 import ConnectorCompoundDynamicAnalysis
    from ._6413 import CouplingCompoundDynamicAnalysis
    from ._6414 import CouplingConnectionCompoundDynamicAnalysis
    from ._6415 import CouplingHalfCompoundDynamicAnalysis
    from ._6416 import CVTBeltConnectionCompoundDynamicAnalysis
    from ._6417 import CVTCompoundDynamicAnalysis
    from ._6418 import CVTPulleyCompoundDynamicAnalysis
    from ._6419 import CycloidalAssemblyCompoundDynamicAnalysis
    from ._6420 import CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis
    from ._6421 import CycloidalDiscCompoundDynamicAnalysis
    from ._6422 import CycloidalDiscPlanetaryBearingConnectionCompoundDynamicAnalysis
    from ._6423 import CylindricalGearCompoundDynamicAnalysis
    from ._6424 import CylindricalGearMeshCompoundDynamicAnalysis
    from ._6425 import CylindricalGearSetCompoundDynamicAnalysis
    from ._6426 import CylindricalPlanetGearCompoundDynamicAnalysis
    from ._6427 import DatumCompoundDynamicAnalysis
    from ._6428 import ExternalCADModelCompoundDynamicAnalysis
    from ._6429 import FaceGearCompoundDynamicAnalysis
    from ._6430 import FaceGearMeshCompoundDynamicAnalysis
    from ._6431 import FaceGearSetCompoundDynamicAnalysis
    from ._6432 import FEPartCompoundDynamicAnalysis
    from ._6433 import FlexiblePinAssemblyCompoundDynamicAnalysis
    from ._6434 import GearCompoundDynamicAnalysis
    from ._6435 import GearMeshCompoundDynamicAnalysis
    from ._6436 import GearSetCompoundDynamicAnalysis
    from ._6437 import GuideDxfModelCompoundDynamicAnalysis
    from ._6438 import HypoidGearCompoundDynamicAnalysis
    from ._6439 import HypoidGearMeshCompoundDynamicAnalysis
    from ._6440 import HypoidGearSetCompoundDynamicAnalysis
    from ._6441 import InterMountableComponentConnectionCompoundDynamicAnalysis
    from ._6442 import KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis
    from ._6443 import KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis
    from ._6444 import KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis
    from ._6445 import KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis
    from ._6446 import KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis
    from ._6447 import KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis
    from ._6448 import KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis
    from ._6449 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis
    from ._6450 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis
    from ._6451 import MassDiscCompoundDynamicAnalysis
    from ._6452 import MeasurementComponentCompoundDynamicAnalysis
    from ._6453 import MountableComponentCompoundDynamicAnalysis
    from ._6454 import OilSealCompoundDynamicAnalysis
    from ._6455 import PartCompoundDynamicAnalysis
    from ._6456 import PartToPartShearCouplingCompoundDynamicAnalysis
    from ._6457 import PartToPartShearCouplingConnectionCompoundDynamicAnalysis
    from ._6458 import PartToPartShearCouplingHalfCompoundDynamicAnalysis
    from ._6459 import PlanetaryConnectionCompoundDynamicAnalysis
    from ._6460 import PlanetaryGearSetCompoundDynamicAnalysis
    from ._6461 import PlanetCarrierCompoundDynamicAnalysis
    from ._6462 import PointLoadCompoundDynamicAnalysis
    from ._6463 import PowerLoadCompoundDynamicAnalysis
    from ._6464 import PulleyCompoundDynamicAnalysis
    from ._6465 import RingPinsCompoundDynamicAnalysis
    from ._6466 import RingPinsToDiscConnectionCompoundDynamicAnalysis
    from ._6467 import RollingRingAssemblyCompoundDynamicAnalysis
    from ._6468 import RollingRingCompoundDynamicAnalysis
    from ._6469 import RollingRingConnectionCompoundDynamicAnalysis
    from ._6470 import RootAssemblyCompoundDynamicAnalysis
    from ._6471 import ShaftCompoundDynamicAnalysis
    from ._6472 import ShaftHubConnectionCompoundDynamicAnalysis
    from ._6473 import ShaftToMountableComponentConnectionCompoundDynamicAnalysis
    from ._6474 import SpecialisedAssemblyCompoundDynamicAnalysis
    from ._6475 import SpiralBevelGearCompoundDynamicAnalysis
    from ._6476 import SpiralBevelGearMeshCompoundDynamicAnalysis
    from ._6477 import SpiralBevelGearSetCompoundDynamicAnalysis
    from ._6478 import SpringDamperCompoundDynamicAnalysis
    from ._6479 import SpringDamperConnectionCompoundDynamicAnalysis
    from ._6480 import SpringDamperHalfCompoundDynamicAnalysis
    from ._6481 import StraightBevelDiffGearCompoundDynamicAnalysis
    from ._6482 import StraightBevelDiffGearMeshCompoundDynamicAnalysis
    from ._6483 import StraightBevelDiffGearSetCompoundDynamicAnalysis
    from ._6484 import StraightBevelGearCompoundDynamicAnalysis
    from ._6485 import StraightBevelGearMeshCompoundDynamicAnalysis
    from ._6486 import StraightBevelGearSetCompoundDynamicAnalysis
    from ._6487 import StraightBevelPlanetGearCompoundDynamicAnalysis
    from ._6488 import StraightBevelSunGearCompoundDynamicAnalysis
    from ._6489 import SynchroniserCompoundDynamicAnalysis
    from ._6490 import SynchroniserHalfCompoundDynamicAnalysis
    from ._6491 import SynchroniserPartCompoundDynamicAnalysis
    from ._6492 import SynchroniserSleeveCompoundDynamicAnalysis
    from ._6493 import TorqueConverterCompoundDynamicAnalysis
    from ._6494 import TorqueConverterConnectionCompoundDynamicAnalysis
    from ._6495 import TorqueConverterPumpCompoundDynamicAnalysis
    from ._6496 import TorqueConverterTurbineCompoundDynamicAnalysis
    from ._6497 import UnbalancedMassCompoundDynamicAnalysis
    from ._6498 import VirtualComponentCompoundDynamicAnalysis
    from ._6499 import WormGearCompoundDynamicAnalysis
    from ._6500 import WormGearMeshCompoundDynamicAnalysis
    from ._6501 import WormGearSetCompoundDynamicAnalysis
    from ._6502 import ZerolBevelGearCompoundDynamicAnalysis
    from ._6503 import ZerolBevelGearMeshCompoundDynamicAnalysis
    from ._6504 import ZerolBevelGearSetCompoundDynamicAnalysis
else:
    import_structure = {
        '_6376': ['AbstractAssemblyCompoundDynamicAnalysis'],
        '_6377': ['AbstractShaftCompoundDynamicAnalysis'],
        '_6378': ['AbstractShaftOrHousingCompoundDynamicAnalysis'],
        '_6379': ['AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis'],
        '_6380': ['AGMAGleasonConicalGearCompoundDynamicAnalysis'],
        '_6381': ['AGMAGleasonConicalGearMeshCompoundDynamicAnalysis'],
        '_6382': ['AGMAGleasonConicalGearSetCompoundDynamicAnalysis'],
        '_6383': ['AssemblyCompoundDynamicAnalysis'],
        '_6384': ['BearingCompoundDynamicAnalysis'],
        '_6385': ['BeltConnectionCompoundDynamicAnalysis'],
        '_6386': ['BeltDriveCompoundDynamicAnalysis'],
        '_6387': ['BevelDifferentialGearCompoundDynamicAnalysis'],
        '_6388': ['BevelDifferentialGearMeshCompoundDynamicAnalysis'],
        '_6389': ['BevelDifferentialGearSetCompoundDynamicAnalysis'],
        '_6390': ['BevelDifferentialPlanetGearCompoundDynamicAnalysis'],
        '_6391': ['BevelDifferentialSunGearCompoundDynamicAnalysis'],
        '_6392': ['BevelGearCompoundDynamicAnalysis'],
        '_6393': ['BevelGearMeshCompoundDynamicAnalysis'],
        '_6394': ['BevelGearSetCompoundDynamicAnalysis'],
        '_6395': ['BoltCompoundDynamicAnalysis'],
        '_6396': ['BoltedJointCompoundDynamicAnalysis'],
        '_6397': ['ClutchCompoundDynamicAnalysis'],
        '_6398': ['ClutchConnectionCompoundDynamicAnalysis'],
        '_6399': ['ClutchHalfCompoundDynamicAnalysis'],
        '_6400': ['CoaxialConnectionCompoundDynamicAnalysis'],
        '_6401': ['ComponentCompoundDynamicAnalysis'],
        '_6402': ['ConceptCouplingCompoundDynamicAnalysis'],
        '_6403': ['ConceptCouplingConnectionCompoundDynamicAnalysis'],
        '_6404': ['ConceptCouplingHalfCompoundDynamicAnalysis'],
        '_6405': ['ConceptGearCompoundDynamicAnalysis'],
        '_6406': ['ConceptGearMeshCompoundDynamicAnalysis'],
        '_6407': ['ConceptGearSetCompoundDynamicAnalysis'],
        '_6408': ['ConicalGearCompoundDynamicAnalysis'],
        '_6409': ['ConicalGearMeshCompoundDynamicAnalysis'],
        '_6410': ['ConicalGearSetCompoundDynamicAnalysis'],
        '_6411': ['ConnectionCompoundDynamicAnalysis'],
        '_6412': ['ConnectorCompoundDynamicAnalysis'],
        '_6413': ['CouplingCompoundDynamicAnalysis'],
        '_6414': ['CouplingConnectionCompoundDynamicAnalysis'],
        '_6415': ['CouplingHalfCompoundDynamicAnalysis'],
        '_6416': ['CVTBeltConnectionCompoundDynamicAnalysis'],
        '_6417': ['CVTCompoundDynamicAnalysis'],
        '_6418': ['CVTPulleyCompoundDynamicAnalysis'],
        '_6419': ['CycloidalAssemblyCompoundDynamicAnalysis'],
        '_6420': ['CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis'],
        '_6421': ['CycloidalDiscCompoundDynamicAnalysis'],
        '_6422': ['CycloidalDiscPlanetaryBearingConnectionCompoundDynamicAnalysis'],
        '_6423': ['CylindricalGearCompoundDynamicAnalysis'],
        '_6424': ['CylindricalGearMeshCompoundDynamicAnalysis'],
        '_6425': ['CylindricalGearSetCompoundDynamicAnalysis'],
        '_6426': ['CylindricalPlanetGearCompoundDynamicAnalysis'],
        '_6427': ['DatumCompoundDynamicAnalysis'],
        '_6428': ['ExternalCADModelCompoundDynamicAnalysis'],
        '_6429': ['FaceGearCompoundDynamicAnalysis'],
        '_6430': ['FaceGearMeshCompoundDynamicAnalysis'],
        '_6431': ['FaceGearSetCompoundDynamicAnalysis'],
        '_6432': ['FEPartCompoundDynamicAnalysis'],
        '_6433': ['FlexiblePinAssemblyCompoundDynamicAnalysis'],
        '_6434': ['GearCompoundDynamicAnalysis'],
        '_6435': ['GearMeshCompoundDynamicAnalysis'],
        '_6436': ['GearSetCompoundDynamicAnalysis'],
        '_6437': ['GuideDxfModelCompoundDynamicAnalysis'],
        '_6438': ['HypoidGearCompoundDynamicAnalysis'],
        '_6439': ['HypoidGearMeshCompoundDynamicAnalysis'],
        '_6440': ['HypoidGearSetCompoundDynamicAnalysis'],
        '_6441': ['InterMountableComponentConnectionCompoundDynamicAnalysis'],
        '_6442': ['KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis'],
        '_6443': ['KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis'],
        '_6444': ['KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis'],
        '_6445': ['KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis'],
        '_6446': ['KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis'],
        '_6447': ['KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis'],
        '_6448': ['KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis'],
        '_6449': ['KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis'],
        '_6450': ['KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis'],
        '_6451': ['MassDiscCompoundDynamicAnalysis'],
        '_6452': ['MeasurementComponentCompoundDynamicAnalysis'],
        '_6453': ['MountableComponentCompoundDynamicAnalysis'],
        '_6454': ['OilSealCompoundDynamicAnalysis'],
        '_6455': ['PartCompoundDynamicAnalysis'],
        '_6456': ['PartToPartShearCouplingCompoundDynamicAnalysis'],
        '_6457': ['PartToPartShearCouplingConnectionCompoundDynamicAnalysis'],
        '_6458': ['PartToPartShearCouplingHalfCompoundDynamicAnalysis'],
        '_6459': ['PlanetaryConnectionCompoundDynamicAnalysis'],
        '_6460': ['PlanetaryGearSetCompoundDynamicAnalysis'],
        '_6461': ['PlanetCarrierCompoundDynamicAnalysis'],
        '_6462': ['PointLoadCompoundDynamicAnalysis'],
        '_6463': ['PowerLoadCompoundDynamicAnalysis'],
        '_6464': ['PulleyCompoundDynamicAnalysis'],
        '_6465': ['RingPinsCompoundDynamicAnalysis'],
        '_6466': ['RingPinsToDiscConnectionCompoundDynamicAnalysis'],
        '_6467': ['RollingRingAssemblyCompoundDynamicAnalysis'],
        '_6468': ['RollingRingCompoundDynamicAnalysis'],
        '_6469': ['RollingRingConnectionCompoundDynamicAnalysis'],
        '_6470': ['RootAssemblyCompoundDynamicAnalysis'],
        '_6471': ['ShaftCompoundDynamicAnalysis'],
        '_6472': ['ShaftHubConnectionCompoundDynamicAnalysis'],
        '_6473': ['ShaftToMountableComponentConnectionCompoundDynamicAnalysis'],
        '_6474': ['SpecialisedAssemblyCompoundDynamicAnalysis'],
        '_6475': ['SpiralBevelGearCompoundDynamicAnalysis'],
        '_6476': ['SpiralBevelGearMeshCompoundDynamicAnalysis'],
        '_6477': ['SpiralBevelGearSetCompoundDynamicAnalysis'],
        '_6478': ['SpringDamperCompoundDynamicAnalysis'],
        '_6479': ['SpringDamperConnectionCompoundDynamicAnalysis'],
        '_6480': ['SpringDamperHalfCompoundDynamicAnalysis'],
        '_6481': ['StraightBevelDiffGearCompoundDynamicAnalysis'],
        '_6482': ['StraightBevelDiffGearMeshCompoundDynamicAnalysis'],
        '_6483': ['StraightBevelDiffGearSetCompoundDynamicAnalysis'],
        '_6484': ['StraightBevelGearCompoundDynamicAnalysis'],
        '_6485': ['StraightBevelGearMeshCompoundDynamicAnalysis'],
        '_6486': ['StraightBevelGearSetCompoundDynamicAnalysis'],
        '_6487': ['StraightBevelPlanetGearCompoundDynamicAnalysis'],
        '_6488': ['StraightBevelSunGearCompoundDynamicAnalysis'],
        '_6489': ['SynchroniserCompoundDynamicAnalysis'],
        '_6490': ['SynchroniserHalfCompoundDynamicAnalysis'],
        '_6491': ['SynchroniserPartCompoundDynamicAnalysis'],
        '_6492': ['SynchroniserSleeveCompoundDynamicAnalysis'],
        '_6493': ['TorqueConverterCompoundDynamicAnalysis'],
        '_6494': ['TorqueConverterConnectionCompoundDynamicAnalysis'],
        '_6495': ['TorqueConverterPumpCompoundDynamicAnalysis'],
        '_6496': ['TorqueConverterTurbineCompoundDynamicAnalysis'],
        '_6497': ['UnbalancedMassCompoundDynamicAnalysis'],
        '_6498': ['VirtualComponentCompoundDynamicAnalysis'],
        '_6499': ['WormGearCompoundDynamicAnalysis'],
        '_6500': ['WormGearMeshCompoundDynamicAnalysis'],
        '_6501': ['WormGearSetCompoundDynamicAnalysis'],
        '_6502': ['ZerolBevelGearCompoundDynamicAnalysis'],
        '_6503': ['ZerolBevelGearMeshCompoundDynamicAnalysis'],
        '_6504': ['ZerolBevelGearSetCompoundDynamicAnalysis'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
