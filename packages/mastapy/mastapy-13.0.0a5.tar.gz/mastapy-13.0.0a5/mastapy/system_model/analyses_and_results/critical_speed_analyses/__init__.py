"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6511 import AbstractAssemblyCriticalSpeedAnalysis
    from ._6512 import AbstractShaftCriticalSpeedAnalysis
    from ._6513 import AbstractShaftOrHousingCriticalSpeedAnalysis
    from ._6514 import AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
    from ._6515 import AGMAGleasonConicalGearCriticalSpeedAnalysis
    from ._6516 import AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
    from ._6517 import AGMAGleasonConicalGearSetCriticalSpeedAnalysis
    from ._6518 import AssemblyCriticalSpeedAnalysis
    from ._6519 import BearingCriticalSpeedAnalysis
    from ._6520 import BeltConnectionCriticalSpeedAnalysis
    from ._6521 import BeltDriveCriticalSpeedAnalysis
    from ._6522 import BevelDifferentialGearCriticalSpeedAnalysis
    from ._6523 import BevelDifferentialGearMeshCriticalSpeedAnalysis
    from ._6524 import BevelDifferentialGearSetCriticalSpeedAnalysis
    from ._6525 import BevelDifferentialPlanetGearCriticalSpeedAnalysis
    from ._6526 import BevelDifferentialSunGearCriticalSpeedAnalysis
    from ._6527 import BevelGearCriticalSpeedAnalysis
    from ._6528 import BevelGearMeshCriticalSpeedAnalysis
    from ._6529 import BevelGearSetCriticalSpeedAnalysis
    from ._6530 import BoltCriticalSpeedAnalysis
    from ._6531 import BoltedJointCriticalSpeedAnalysis
    from ._6532 import ClutchConnectionCriticalSpeedAnalysis
    from ._6533 import ClutchCriticalSpeedAnalysis
    from ._6534 import ClutchHalfCriticalSpeedAnalysis
    from ._6535 import CoaxialConnectionCriticalSpeedAnalysis
    from ._6536 import ComponentCriticalSpeedAnalysis
    from ._6537 import ConceptCouplingConnectionCriticalSpeedAnalysis
    from ._6538 import ConceptCouplingCriticalSpeedAnalysis
    from ._6539 import ConceptCouplingHalfCriticalSpeedAnalysis
    from ._6540 import ConceptGearCriticalSpeedAnalysis
    from ._6541 import ConceptGearMeshCriticalSpeedAnalysis
    from ._6542 import ConceptGearSetCriticalSpeedAnalysis
    from ._6543 import ConicalGearCriticalSpeedAnalysis
    from ._6544 import ConicalGearMeshCriticalSpeedAnalysis
    from ._6545 import ConicalGearSetCriticalSpeedAnalysis
    from ._6546 import ConnectionCriticalSpeedAnalysis
    from ._6547 import ConnectorCriticalSpeedAnalysis
    from ._6548 import CouplingConnectionCriticalSpeedAnalysis
    from ._6549 import CouplingCriticalSpeedAnalysis
    from ._6550 import CouplingHalfCriticalSpeedAnalysis
    from ._2607 import CriticalSpeedAnalysis
    from ._6551 import CriticalSpeedAnalysisDrawStyle
    from ._6552 import CriticalSpeedAnalysisOptions
    from ._6553 import CVTBeltConnectionCriticalSpeedAnalysis
    from ._6554 import CVTCriticalSpeedAnalysis
    from ._6555 import CVTPulleyCriticalSpeedAnalysis
    from ._6556 import CycloidalAssemblyCriticalSpeedAnalysis
    from ._6557 import CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis
    from ._6558 import CycloidalDiscCriticalSpeedAnalysis
    from ._6559 import CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis
    from ._6560 import CylindricalGearCriticalSpeedAnalysis
    from ._6561 import CylindricalGearMeshCriticalSpeedAnalysis
    from ._6562 import CylindricalGearSetCriticalSpeedAnalysis
    from ._6563 import CylindricalPlanetGearCriticalSpeedAnalysis
    from ._6564 import DatumCriticalSpeedAnalysis
    from ._6565 import ExternalCADModelCriticalSpeedAnalysis
    from ._6566 import FaceGearCriticalSpeedAnalysis
    from ._6567 import FaceGearMeshCriticalSpeedAnalysis
    from ._6568 import FaceGearSetCriticalSpeedAnalysis
    from ._6569 import FEPartCriticalSpeedAnalysis
    from ._6570 import FlexiblePinAssemblyCriticalSpeedAnalysis
    from ._6571 import GearCriticalSpeedAnalysis
    from ._6572 import GearMeshCriticalSpeedAnalysis
    from ._6573 import GearSetCriticalSpeedAnalysis
    from ._6574 import GuideDxfModelCriticalSpeedAnalysis
    from ._6575 import HypoidGearCriticalSpeedAnalysis
    from ._6576 import HypoidGearMeshCriticalSpeedAnalysis
    from ._6577 import HypoidGearSetCriticalSpeedAnalysis
    from ._6578 import InterMountableComponentConnectionCriticalSpeedAnalysis
    from ._6579 import KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
    from ._6580 import KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis
    from ._6581 import KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
    from ._6582 import KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
    from ._6583 import KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis
    from ._6584 import KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
    from ._6585 import KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
    from ._6586 import KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis
    from ._6587 import KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
    from ._6588 import MassDiscCriticalSpeedAnalysis
    from ._6589 import MeasurementComponentCriticalSpeedAnalysis
    from ._6590 import MountableComponentCriticalSpeedAnalysis
    from ._6591 import OilSealCriticalSpeedAnalysis
    from ._6592 import PartCriticalSpeedAnalysis
    from ._6593 import PartToPartShearCouplingConnectionCriticalSpeedAnalysis
    from ._6594 import PartToPartShearCouplingCriticalSpeedAnalysis
    from ._6595 import PartToPartShearCouplingHalfCriticalSpeedAnalysis
    from ._6596 import PlanetaryConnectionCriticalSpeedAnalysis
    from ._6597 import PlanetaryGearSetCriticalSpeedAnalysis
    from ._6598 import PlanetCarrierCriticalSpeedAnalysis
    from ._6599 import PointLoadCriticalSpeedAnalysis
    from ._6600 import PowerLoadCriticalSpeedAnalysis
    from ._6601 import PulleyCriticalSpeedAnalysis
    from ._6602 import RingPinsCriticalSpeedAnalysis
    from ._6603 import RingPinsToDiscConnectionCriticalSpeedAnalysis
    from ._6604 import RollingRingAssemblyCriticalSpeedAnalysis
    from ._6605 import RollingRingConnectionCriticalSpeedAnalysis
    from ._6606 import RollingRingCriticalSpeedAnalysis
    from ._6607 import RootAssemblyCriticalSpeedAnalysis
    from ._6608 import ShaftCriticalSpeedAnalysis
    from ._6609 import ShaftHubConnectionCriticalSpeedAnalysis
    from ._6610 import ShaftToMountableComponentConnectionCriticalSpeedAnalysis
    from ._6611 import SpecialisedAssemblyCriticalSpeedAnalysis
    from ._6612 import SpiralBevelGearCriticalSpeedAnalysis
    from ._6613 import SpiralBevelGearMeshCriticalSpeedAnalysis
    from ._6614 import SpiralBevelGearSetCriticalSpeedAnalysis
    from ._6615 import SpringDamperConnectionCriticalSpeedAnalysis
    from ._6616 import SpringDamperCriticalSpeedAnalysis
    from ._6617 import SpringDamperHalfCriticalSpeedAnalysis
    from ._6618 import StraightBevelDiffGearCriticalSpeedAnalysis
    from ._6619 import StraightBevelDiffGearMeshCriticalSpeedAnalysis
    from ._6620 import StraightBevelDiffGearSetCriticalSpeedAnalysis
    from ._6621 import StraightBevelGearCriticalSpeedAnalysis
    from ._6622 import StraightBevelGearMeshCriticalSpeedAnalysis
    from ._6623 import StraightBevelGearSetCriticalSpeedAnalysis
    from ._6624 import StraightBevelPlanetGearCriticalSpeedAnalysis
    from ._6625 import StraightBevelSunGearCriticalSpeedAnalysis
    from ._6626 import SynchroniserCriticalSpeedAnalysis
    from ._6627 import SynchroniserHalfCriticalSpeedAnalysis
    from ._6628 import SynchroniserPartCriticalSpeedAnalysis
    from ._6629 import SynchroniserSleeveCriticalSpeedAnalysis
    from ._6630 import TorqueConverterConnectionCriticalSpeedAnalysis
    from ._6631 import TorqueConverterCriticalSpeedAnalysis
    from ._6632 import TorqueConverterPumpCriticalSpeedAnalysis
    from ._6633 import TorqueConverterTurbineCriticalSpeedAnalysis
    from ._6634 import UnbalancedMassCriticalSpeedAnalysis
    from ._6635 import VirtualComponentCriticalSpeedAnalysis
    from ._6636 import WormGearCriticalSpeedAnalysis
    from ._6637 import WormGearMeshCriticalSpeedAnalysis
    from ._6638 import WormGearSetCriticalSpeedAnalysis
    from ._6639 import ZerolBevelGearCriticalSpeedAnalysis
    from ._6640 import ZerolBevelGearMeshCriticalSpeedAnalysis
    from ._6641 import ZerolBevelGearSetCriticalSpeedAnalysis
else:
    import_structure = {
        '_6511': ['AbstractAssemblyCriticalSpeedAnalysis'],
        '_6512': ['AbstractShaftCriticalSpeedAnalysis'],
        '_6513': ['AbstractShaftOrHousingCriticalSpeedAnalysis'],
        '_6514': ['AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis'],
        '_6515': ['AGMAGleasonConicalGearCriticalSpeedAnalysis'],
        '_6516': ['AGMAGleasonConicalGearMeshCriticalSpeedAnalysis'],
        '_6517': ['AGMAGleasonConicalGearSetCriticalSpeedAnalysis'],
        '_6518': ['AssemblyCriticalSpeedAnalysis'],
        '_6519': ['BearingCriticalSpeedAnalysis'],
        '_6520': ['BeltConnectionCriticalSpeedAnalysis'],
        '_6521': ['BeltDriveCriticalSpeedAnalysis'],
        '_6522': ['BevelDifferentialGearCriticalSpeedAnalysis'],
        '_6523': ['BevelDifferentialGearMeshCriticalSpeedAnalysis'],
        '_6524': ['BevelDifferentialGearSetCriticalSpeedAnalysis'],
        '_6525': ['BevelDifferentialPlanetGearCriticalSpeedAnalysis'],
        '_6526': ['BevelDifferentialSunGearCriticalSpeedAnalysis'],
        '_6527': ['BevelGearCriticalSpeedAnalysis'],
        '_6528': ['BevelGearMeshCriticalSpeedAnalysis'],
        '_6529': ['BevelGearSetCriticalSpeedAnalysis'],
        '_6530': ['BoltCriticalSpeedAnalysis'],
        '_6531': ['BoltedJointCriticalSpeedAnalysis'],
        '_6532': ['ClutchConnectionCriticalSpeedAnalysis'],
        '_6533': ['ClutchCriticalSpeedAnalysis'],
        '_6534': ['ClutchHalfCriticalSpeedAnalysis'],
        '_6535': ['CoaxialConnectionCriticalSpeedAnalysis'],
        '_6536': ['ComponentCriticalSpeedAnalysis'],
        '_6537': ['ConceptCouplingConnectionCriticalSpeedAnalysis'],
        '_6538': ['ConceptCouplingCriticalSpeedAnalysis'],
        '_6539': ['ConceptCouplingHalfCriticalSpeedAnalysis'],
        '_6540': ['ConceptGearCriticalSpeedAnalysis'],
        '_6541': ['ConceptGearMeshCriticalSpeedAnalysis'],
        '_6542': ['ConceptGearSetCriticalSpeedAnalysis'],
        '_6543': ['ConicalGearCriticalSpeedAnalysis'],
        '_6544': ['ConicalGearMeshCriticalSpeedAnalysis'],
        '_6545': ['ConicalGearSetCriticalSpeedAnalysis'],
        '_6546': ['ConnectionCriticalSpeedAnalysis'],
        '_6547': ['ConnectorCriticalSpeedAnalysis'],
        '_6548': ['CouplingConnectionCriticalSpeedAnalysis'],
        '_6549': ['CouplingCriticalSpeedAnalysis'],
        '_6550': ['CouplingHalfCriticalSpeedAnalysis'],
        '_2607': ['CriticalSpeedAnalysis'],
        '_6551': ['CriticalSpeedAnalysisDrawStyle'],
        '_6552': ['CriticalSpeedAnalysisOptions'],
        '_6553': ['CVTBeltConnectionCriticalSpeedAnalysis'],
        '_6554': ['CVTCriticalSpeedAnalysis'],
        '_6555': ['CVTPulleyCriticalSpeedAnalysis'],
        '_6556': ['CycloidalAssemblyCriticalSpeedAnalysis'],
        '_6557': ['CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis'],
        '_6558': ['CycloidalDiscCriticalSpeedAnalysis'],
        '_6559': ['CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis'],
        '_6560': ['CylindricalGearCriticalSpeedAnalysis'],
        '_6561': ['CylindricalGearMeshCriticalSpeedAnalysis'],
        '_6562': ['CylindricalGearSetCriticalSpeedAnalysis'],
        '_6563': ['CylindricalPlanetGearCriticalSpeedAnalysis'],
        '_6564': ['DatumCriticalSpeedAnalysis'],
        '_6565': ['ExternalCADModelCriticalSpeedAnalysis'],
        '_6566': ['FaceGearCriticalSpeedAnalysis'],
        '_6567': ['FaceGearMeshCriticalSpeedAnalysis'],
        '_6568': ['FaceGearSetCriticalSpeedAnalysis'],
        '_6569': ['FEPartCriticalSpeedAnalysis'],
        '_6570': ['FlexiblePinAssemblyCriticalSpeedAnalysis'],
        '_6571': ['GearCriticalSpeedAnalysis'],
        '_6572': ['GearMeshCriticalSpeedAnalysis'],
        '_6573': ['GearSetCriticalSpeedAnalysis'],
        '_6574': ['GuideDxfModelCriticalSpeedAnalysis'],
        '_6575': ['HypoidGearCriticalSpeedAnalysis'],
        '_6576': ['HypoidGearMeshCriticalSpeedAnalysis'],
        '_6577': ['HypoidGearSetCriticalSpeedAnalysis'],
        '_6578': ['InterMountableComponentConnectionCriticalSpeedAnalysis'],
        '_6579': ['KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis'],
        '_6580': ['KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis'],
        '_6581': ['KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis'],
        '_6582': ['KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis'],
        '_6583': ['KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis'],
        '_6584': ['KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis'],
        '_6585': ['KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis'],
        '_6586': ['KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis'],
        '_6587': ['KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis'],
        '_6588': ['MassDiscCriticalSpeedAnalysis'],
        '_6589': ['MeasurementComponentCriticalSpeedAnalysis'],
        '_6590': ['MountableComponentCriticalSpeedAnalysis'],
        '_6591': ['OilSealCriticalSpeedAnalysis'],
        '_6592': ['PartCriticalSpeedAnalysis'],
        '_6593': ['PartToPartShearCouplingConnectionCriticalSpeedAnalysis'],
        '_6594': ['PartToPartShearCouplingCriticalSpeedAnalysis'],
        '_6595': ['PartToPartShearCouplingHalfCriticalSpeedAnalysis'],
        '_6596': ['PlanetaryConnectionCriticalSpeedAnalysis'],
        '_6597': ['PlanetaryGearSetCriticalSpeedAnalysis'],
        '_6598': ['PlanetCarrierCriticalSpeedAnalysis'],
        '_6599': ['PointLoadCriticalSpeedAnalysis'],
        '_6600': ['PowerLoadCriticalSpeedAnalysis'],
        '_6601': ['PulleyCriticalSpeedAnalysis'],
        '_6602': ['RingPinsCriticalSpeedAnalysis'],
        '_6603': ['RingPinsToDiscConnectionCriticalSpeedAnalysis'],
        '_6604': ['RollingRingAssemblyCriticalSpeedAnalysis'],
        '_6605': ['RollingRingConnectionCriticalSpeedAnalysis'],
        '_6606': ['RollingRingCriticalSpeedAnalysis'],
        '_6607': ['RootAssemblyCriticalSpeedAnalysis'],
        '_6608': ['ShaftCriticalSpeedAnalysis'],
        '_6609': ['ShaftHubConnectionCriticalSpeedAnalysis'],
        '_6610': ['ShaftToMountableComponentConnectionCriticalSpeedAnalysis'],
        '_6611': ['SpecialisedAssemblyCriticalSpeedAnalysis'],
        '_6612': ['SpiralBevelGearCriticalSpeedAnalysis'],
        '_6613': ['SpiralBevelGearMeshCriticalSpeedAnalysis'],
        '_6614': ['SpiralBevelGearSetCriticalSpeedAnalysis'],
        '_6615': ['SpringDamperConnectionCriticalSpeedAnalysis'],
        '_6616': ['SpringDamperCriticalSpeedAnalysis'],
        '_6617': ['SpringDamperHalfCriticalSpeedAnalysis'],
        '_6618': ['StraightBevelDiffGearCriticalSpeedAnalysis'],
        '_6619': ['StraightBevelDiffGearMeshCriticalSpeedAnalysis'],
        '_6620': ['StraightBevelDiffGearSetCriticalSpeedAnalysis'],
        '_6621': ['StraightBevelGearCriticalSpeedAnalysis'],
        '_6622': ['StraightBevelGearMeshCriticalSpeedAnalysis'],
        '_6623': ['StraightBevelGearSetCriticalSpeedAnalysis'],
        '_6624': ['StraightBevelPlanetGearCriticalSpeedAnalysis'],
        '_6625': ['StraightBevelSunGearCriticalSpeedAnalysis'],
        '_6626': ['SynchroniserCriticalSpeedAnalysis'],
        '_6627': ['SynchroniserHalfCriticalSpeedAnalysis'],
        '_6628': ['SynchroniserPartCriticalSpeedAnalysis'],
        '_6629': ['SynchroniserSleeveCriticalSpeedAnalysis'],
        '_6630': ['TorqueConverterConnectionCriticalSpeedAnalysis'],
        '_6631': ['TorqueConverterCriticalSpeedAnalysis'],
        '_6632': ['TorqueConverterPumpCriticalSpeedAnalysis'],
        '_6633': ['TorqueConverterTurbineCriticalSpeedAnalysis'],
        '_6634': ['UnbalancedMassCriticalSpeedAnalysis'],
        '_6635': ['VirtualComponentCriticalSpeedAnalysis'],
        '_6636': ['WormGearCriticalSpeedAnalysis'],
        '_6637': ['WormGearMeshCriticalSpeedAnalysis'],
        '_6638': ['WormGearSetCriticalSpeedAnalysis'],
        '_6639': ['ZerolBevelGearCriticalSpeedAnalysis'],
        '_6640': ['ZerolBevelGearMeshCriticalSpeedAnalysis'],
        '_6641': ['ZerolBevelGearSetCriticalSpeedAnalysis'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
