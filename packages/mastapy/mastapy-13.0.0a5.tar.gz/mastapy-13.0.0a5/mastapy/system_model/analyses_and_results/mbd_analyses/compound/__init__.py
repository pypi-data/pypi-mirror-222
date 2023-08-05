"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5502 import AbstractAssemblyCompoundMultibodyDynamicsAnalysis
    from ._5503 import AbstractShaftCompoundMultibodyDynamicsAnalysis
    from ._5504 import AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis
    from ._5505 import AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
    from ._5506 import AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
    from ._5507 import AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5508 import AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis
    from ._5509 import AssemblyCompoundMultibodyDynamicsAnalysis
    from ._5510 import BearingCompoundMultibodyDynamicsAnalysis
    from ._5511 import BeltConnectionCompoundMultibodyDynamicsAnalysis
    from ._5512 import BeltDriveCompoundMultibodyDynamicsAnalysis
    from ._5513 import BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
    from ._5514 import BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5515 import BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis
    from ._5516 import BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis
    from ._5517 import BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis
    from ._5518 import BevelGearCompoundMultibodyDynamicsAnalysis
    from ._5519 import BevelGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5520 import BevelGearSetCompoundMultibodyDynamicsAnalysis
    from ._5521 import BoltCompoundMultibodyDynamicsAnalysis
    from ._5522 import BoltedJointCompoundMultibodyDynamicsAnalysis
    from ._5523 import ClutchCompoundMultibodyDynamicsAnalysis
    from ._5524 import ClutchConnectionCompoundMultibodyDynamicsAnalysis
    from ._5525 import ClutchHalfCompoundMultibodyDynamicsAnalysis
    from ._5526 import CoaxialConnectionCompoundMultibodyDynamicsAnalysis
    from ._5527 import ComponentCompoundMultibodyDynamicsAnalysis
    from ._5528 import ConceptCouplingCompoundMultibodyDynamicsAnalysis
    from ._5529 import ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis
    from ._5530 import ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis
    from ._5531 import ConceptGearCompoundMultibodyDynamicsAnalysis
    from ._5532 import ConceptGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5533 import ConceptGearSetCompoundMultibodyDynamicsAnalysis
    from ._5534 import ConicalGearCompoundMultibodyDynamicsAnalysis
    from ._5535 import ConicalGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5536 import ConicalGearSetCompoundMultibodyDynamicsAnalysis
    from ._5537 import ConnectionCompoundMultibodyDynamicsAnalysis
    from ._5538 import ConnectorCompoundMultibodyDynamicsAnalysis
    from ._5539 import CouplingCompoundMultibodyDynamicsAnalysis
    from ._5540 import CouplingConnectionCompoundMultibodyDynamicsAnalysis
    from ._5541 import CouplingHalfCompoundMultibodyDynamicsAnalysis
    from ._5542 import CVTBeltConnectionCompoundMultibodyDynamicsAnalysis
    from ._5543 import CVTCompoundMultibodyDynamicsAnalysis
    from ._5544 import CVTPulleyCompoundMultibodyDynamicsAnalysis
    from ._5545 import CycloidalAssemblyCompoundMultibodyDynamicsAnalysis
    from ._5546 import CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis
    from ._5547 import CycloidalDiscCompoundMultibodyDynamicsAnalysis
    from ._5548 import CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis
    from ._5549 import CylindricalGearCompoundMultibodyDynamicsAnalysis
    from ._5550 import CylindricalGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5551 import CylindricalGearSetCompoundMultibodyDynamicsAnalysis
    from ._5552 import CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis
    from ._5553 import DatumCompoundMultibodyDynamicsAnalysis
    from ._5554 import ExternalCADModelCompoundMultibodyDynamicsAnalysis
    from ._5555 import FaceGearCompoundMultibodyDynamicsAnalysis
    from ._5556 import FaceGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5557 import FaceGearSetCompoundMultibodyDynamicsAnalysis
    from ._5558 import FEPartCompoundMultibodyDynamicsAnalysis
    from ._5559 import FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis
    from ._5560 import GearCompoundMultibodyDynamicsAnalysis
    from ._5561 import GearMeshCompoundMultibodyDynamicsAnalysis
    from ._5562 import GearSetCompoundMultibodyDynamicsAnalysis
    from ._5563 import GuideDxfModelCompoundMultibodyDynamicsAnalysis
    from ._5564 import HypoidGearCompoundMultibodyDynamicsAnalysis
    from ._5565 import HypoidGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5566 import HypoidGearSetCompoundMultibodyDynamicsAnalysis
    from ._5567 import InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
    from ._5568 import KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis
    from ._5569 import KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5570 import KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis
    from ._5571 import KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis
    from ._5572 import KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5573 import KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis
    from ._5574 import KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis
    from ._5575 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5576 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
    from ._5577 import MassDiscCompoundMultibodyDynamicsAnalysis
    from ._5578 import MeasurementComponentCompoundMultibodyDynamicsAnalysis
    from ._5579 import MountableComponentCompoundMultibodyDynamicsAnalysis
    from ._5580 import OilSealCompoundMultibodyDynamicsAnalysis
    from ._5581 import PartCompoundMultibodyDynamicsAnalysis
    from ._5582 import PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis
    from ._5583 import PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis
    from ._5584 import PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis
    from ._5585 import PlanetaryConnectionCompoundMultibodyDynamicsAnalysis
    from ._5586 import PlanetaryGearSetCompoundMultibodyDynamicsAnalysis
    from ._5587 import PlanetCarrierCompoundMultibodyDynamicsAnalysis
    from ._5588 import PointLoadCompoundMultibodyDynamicsAnalysis
    from ._5589 import PowerLoadCompoundMultibodyDynamicsAnalysis
    from ._5590 import PulleyCompoundMultibodyDynamicsAnalysis
    from ._5591 import RingPinsCompoundMultibodyDynamicsAnalysis
    from ._5592 import RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis
    from ._5593 import RollingRingAssemblyCompoundMultibodyDynamicsAnalysis
    from ._5594 import RollingRingCompoundMultibodyDynamicsAnalysis
    from ._5595 import RollingRingConnectionCompoundMultibodyDynamicsAnalysis
    from ._5596 import RootAssemblyCompoundMultibodyDynamicsAnalysis
    from ._5597 import ShaftCompoundMultibodyDynamicsAnalysis
    from ._5598 import ShaftHubConnectionCompoundMultibodyDynamicsAnalysis
    from ._5599 import ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
    from ._5600 import SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
    from ._5601 import SpiralBevelGearCompoundMultibodyDynamicsAnalysis
    from ._5602 import SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5603 import SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
    from ._5604 import SpringDamperCompoundMultibodyDynamicsAnalysis
    from ._5605 import SpringDamperConnectionCompoundMultibodyDynamicsAnalysis
    from ._5606 import SpringDamperHalfCompoundMultibodyDynamicsAnalysis
    from ._5607 import StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
    from ._5608 import StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5609 import StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis
    from ._5610 import StraightBevelGearCompoundMultibodyDynamicsAnalysis
    from ._5611 import StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5612 import StraightBevelGearSetCompoundMultibodyDynamicsAnalysis
    from ._5613 import StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis
    from ._5614 import StraightBevelSunGearCompoundMultibodyDynamicsAnalysis
    from ._5615 import SynchroniserCompoundMultibodyDynamicsAnalysis
    from ._5616 import SynchroniserHalfCompoundMultibodyDynamicsAnalysis
    from ._5617 import SynchroniserPartCompoundMultibodyDynamicsAnalysis
    from ._5618 import SynchroniserSleeveCompoundMultibodyDynamicsAnalysis
    from ._5619 import TorqueConverterCompoundMultibodyDynamicsAnalysis
    from ._5620 import TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis
    from ._5621 import TorqueConverterPumpCompoundMultibodyDynamicsAnalysis
    from ._5622 import TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis
    from ._5623 import UnbalancedMassCompoundMultibodyDynamicsAnalysis
    from ._5624 import VirtualComponentCompoundMultibodyDynamicsAnalysis
    from ._5625 import WormGearCompoundMultibodyDynamicsAnalysis
    from ._5626 import WormGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5627 import WormGearSetCompoundMultibodyDynamicsAnalysis
    from ._5628 import ZerolBevelGearCompoundMultibodyDynamicsAnalysis
    from ._5629 import ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5630 import ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis
else:
    import_structure = {
        '_5502': ['AbstractAssemblyCompoundMultibodyDynamicsAnalysis'],
        '_5503': ['AbstractShaftCompoundMultibodyDynamicsAnalysis'],
        '_5504': ['AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis'],
        '_5505': ['AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis'],
        '_5506': ['AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis'],
        '_5507': ['AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis'],
        '_5508': ['AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis'],
        '_5509': ['AssemblyCompoundMultibodyDynamicsAnalysis'],
        '_5510': ['BearingCompoundMultibodyDynamicsAnalysis'],
        '_5511': ['BeltConnectionCompoundMultibodyDynamicsAnalysis'],
        '_5512': ['BeltDriveCompoundMultibodyDynamicsAnalysis'],
        '_5513': ['BevelDifferentialGearCompoundMultibodyDynamicsAnalysis'],
        '_5514': ['BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis'],
        '_5515': ['BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis'],
        '_5516': ['BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis'],
        '_5517': ['BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis'],
        '_5518': ['BevelGearCompoundMultibodyDynamicsAnalysis'],
        '_5519': ['BevelGearMeshCompoundMultibodyDynamicsAnalysis'],
        '_5520': ['BevelGearSetCompoundMultibodyDynamicsAnalysis'],
        '_5521': ['BoltCompoundMultibodyDynamicsAnalysis'],
        '_5522': ['BoltedJointCompoundMultibodyDynamicsAnalysis'],
        '_5523': ['ClutchCompoundMultibodyDynamicsAnalysis'],
        '_5524': ['ClutchConnectionCompoundMultibodyDynamicsAnalysis'],
        '_5525': ['ClutchHalfCompoundMultibodyDynamicsAnalysis'],
        '_5526': ['CoaxialConnectionCompoundMultibodyDynamicsAnalysis'],
        '_5527': ['ComponentCompoundMultibodyDynamicsAnalysis'],
        '_5528': ['ConceptCouplingCompoundMultibodyDynamicsAnalysis'],
        '_5529': ['ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis'],
        '_5530': ['ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis'],
        '_5531': ['ConceptGearCompoundMultibodyDynamicsAnalysis'],
        '_5532': ['ConceptGearMeshCompoundMultibodyDynamicsAnalysis'],
        '_5533': ['ConceptGearSetCompoundMultibodyDynamicsAnalysis'],
        '_5534': ['ConicalGearCompoundMultibodyDynamicsAnalysis'],
        '_5535': ['ConicalGearMeshCompoundMultibodyDynamicsAnalysis'],
        '_5536': ['ConicalGearSetCompoundMultibodyDynamicsAnalysis'],
        '_5537': ['ConnectionCompoundMultibodyDynamicsAnalysis'],
        '_5538': ['ConnectorCompoundMultibodyDynamicsAnalysis'],
        '_5539': ['CouplingCompoundMultibodyDynamicsAnalysis'],
        '_5540': ['CouplingConnectionCompoundMultibodyDynamicsAnalysis'],
        '_5541': ['CouplingHalfCompoundMultibodyDynamicsAnalysis'],
        '_5542': ['CVTBeltConnectionCompoundMultibodyDynamicsAnalysis'],
        '_5543': ['CVTCompoundMultibodyDynamicsAnalysis'],
        '_5544': ['CVTPulleyCompoundMultibodyDynamicsAnalysis'],
        '_5545': ['CycloidalAssemblyCompoundMultibodyDynamicsAnalysis'],
        '_5546': ['CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis'],
        '_5547': ['CycloidalDiscCompoundMultibodyDynamicsAnalysis'],
        '_5548': ['CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis'],
        '_5549': ['CylindricalGearCompoundMultibodyDynamicsAnalysis'],
        '_5550': ['CylindricalGearMeshCompoundMultibodyDynamicsAnalysis'],
        '_5551': ['CylindricalGearSetCompoundMultibodyDynamicsAnalysis'],
        '_5552': ['CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis'],
        '_5553': ['DatumCompoundMultibodyDynamicsAnalysis'],
        '_5554': ['ExternalCADModelCompoundMultibodyDynamicsAnalysis'],
        '_5555': ['FaceGearCompoundMultibodyDynamicsAnalysis'],
        '_5556': ['FaceGearMeshCompoundMultibodyDynamicsAnalysis'],
        '_5557': ['FaceGearSetCompoundMultibodyDynamicsAnalysis'],
        '_5558': ['FEPartCompoundMultibodyDynamicsAnalysis'],
        '_5559': ['FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis'],
        '_5560': ['GearCompoundMultibodyDynamicsAnalysis'],
        '_5561': ['GearMeshCompoundMultibodyDynamicsAnalysis'],
        '_5562': ['GearSetCompoundMultibodyDynamicsAnalysis'],
        '_5563': ['GuideDxfModelCompoundMultibodyDynamicsAnalysis'],
        '_5564': ['HypoidGearCompoundMultibodyDynamicsAnalysis'],
        '_5565': ['HypoidGearMeshCompoundMultibodyDynamicsAnalysis'],
        '_5566': ['HypoidGearSetCompoundMultibodyDynamicsAnalysis'],
        '_5567': ['InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis'],
        '_5568': ['KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis'],
        '_5569': ['KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis'],
        '_5570': ['KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis'],
        '_5571': ['KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis'],
        '_5572': ['KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis'],
        '_5573': ['KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis'],
        '_5574': ['KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis'],
        '_5575': ['KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis'],
        '_5576': ['KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis'],
        '_5577': ['MassDiscCompoundMultibodyDynamicsAnalysis'],
        '_5578': ['MeasurementComponentCompoundMultibodyDynamicsAnalysis'],
        '_5579': ['MountableComponentCompoundMultibodyDynamicsAnalysis'],
        '_5580': ['OilSealCompoundMultibodyDynamicsAnalysis'],
        '_5581': ['PartCompoundMultibodyDynamicsAnalysis'],
        '_5582': ['PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis'],
        '_5583': ['PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis'],
        '_5584': ['PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis'],
        '_5585': ['PlanetaryConnectionCompoundMultibodyDynamicsAnalysis'],
        '_5586': ['PlanetaryGearSetCompoundMultibodyDynamicsAnalysis'],
        '_5587': ['PlanetCarrierCompoundMultibodyDynamicsAnalysis'],
        '_5588': ['PointLoadCompoundMultibodyDynamicsAnalysis'],
        '_5589': ['PowerLoadCompoundMultibodyDynamicsAnalysis'],
        '_5590': ['PulleyCompoundMultibodyDynamicsAnalysis'],
        '_5591': ['RingPinsCompoundMultibodyDynamicsAnalysis'],
        '_5592': ['RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis'],
        '_5593': ['RollingRingAssemblyCompoundMultibodyDynamicsAnalysis'],
        '_5594': ['RollingRingCompoundMultibodyDynamicsAnalysis'],
        '_5595': ['RollingRingConnectionCompoundMultibodyDynamicsAnalysis'],
        '_5596': ['RootAssemblyCompoundMultibodyDynamicsAnalysis'],
        '_5597': ['ShaftCompoundMultibodyDynamicsAnalysis'],
        '_5598': ['ShaftHubConnectionCompoundMultibodyDynamicsAnalysis'],
        '_5599': ['ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis'],
        '_5600': ['SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis'],
        '_5601': ['SpiralBevelGearCompoundMultibodyDynamicsAnalysis'],
        '_5602': ['SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis'],
        '_5603': ['SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis'],
        '_5604': ['SpringDamperCompoundMultibodyDynamicsAnalysis'],
        '_5605': ['SpringDamperConnectionCompoundMultibodyDynamicsAnalysis'],
        '_5606': ['SpringDamperHalfCompoundMultibodyDynamicsAnalysis'],
        '_5607': ['StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis'],
        '_5608': ['StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis'],
        '_5609': ['StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis'],
        '_5610': ['StraightBevelGearCompoundMultibodyDynamicsAnalysis'],
        '_5611': ['StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis'],
        '_5612': ['StraightBevelGearSetCompoundMultibodyDynamicsAnalysis'],
        '_5613': ['StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis'],
        '_5614': ['StraightBevelSunGearCompoundMultibodyDynamicsAnalysis'],
        '_5615': ['SynchroniserCompoundMultibodyDynamicsAnalysis'],
        '_5616': ['SynchroniserHalfCompoundMultibodyDynamicsAnalysis'],
        '_5617': ['SynchroniserPartCompoundMultibodyDynamicsAnalysis'],
        '_5618': ['SynchroniserSleeveCompoundMultibodyDynamicsAnalysis'],
        '_5619': ['TorqueConverterCompoundMultibodyDynamicsAnalysis'],
        '_5620': ['TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis'],
        '_5621': ['TorqueConverterPumpCompoundMultibodyDynamicsAnalysis'],
        '_5622': ['TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis'],
        '_5623': ['UnbalancedMassCompoundMultibodyDynamicsAnalysis'],
        '_5624': ['VirtualComponentCompoundMultibodyDynamicsAnalysis'],
        '_5625': ['WormGearCompoundMultibodyDynamicsAnalysis'],
        '_5626': ['WormGearMeshCompoundMultibodyDynamicsAnalysis'],
        '_5627': ['WormGearSetCompoundMultibodyDynamicsAnalysis'],
        '_5628': ['ZerolBevelGearCompoundMultibodyDynamicsAnalysis'],
        '_5629': ['ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis'],
        '_5630': ['ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
