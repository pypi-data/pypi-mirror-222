"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6642 import AbstractAssemblyCompoundCriticalSpeedAnalysis
    from ._6643 import AbstractShaftCompoundCriticalSpeedAnalysis
    from ._6644 import AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
    from ._6645 import AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
    from ._6646 import AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
    from ._6647 import AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
    from ._6648 import AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
    from ._6649 import AssemblyCompoundCriticalSpeedAnalysis
    from ._6650 import BearingCompoundCriticalSpeedAnalysis
    from ._6651 import BeltConnectionCompoundCriticalSpeedAnalysis
    from ._6652 import BeltDriveCompoundCriticalSpeedAnalysis
    from ._6653 import BevelDifferentialGearCompoundCriticalSpeedAnalysis
    from ._6654 import BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
    from ._6655 import BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
    from ._6656 import BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
    from ._6657 import BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
    from ._6658 import BevelGearCompoundCriticalSpeedAnalysis
    from ._6659 import BevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6660 import BevelGearSetCompoundCriticalSpeedAnalysis
    from ._6661 import BoltCompoundCriticalSpeedAnalysis
    from ._6662 import BoltedJointCompoundCriticalSpeedAnalysis
    from ._6663 import ClutchCompoundCriticalSpeedAnalysis
    from ._6664 import ClutchConnectionCompoundCriticalSpeedAnalysis
    from ._6665 import ClutchHalfCompoundCriticalSpeedAnalysis
    from ._6666 import CoaxialConnectionCompoundCriticalSpeedAnalysis
    from ._6667 import ComponentCompoundCriticalSpeedAnalysis
    from ._6668 import ConceptCouplingCompoundCriticalSpeedAnalysis
    from ._6669 import ConceptCouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6670 import ConceptCouplingHalfCompoundCriticalSpeedAnalysis
    from ._6671 import ConceptGearCompoundCriticalSpeedAnalysis
    from ._6672 import ConceptGearMeshCompoundCriticalSpeedAnalysis
    from ._6673 import ConceptGearSetCompoundCriticalSpeedAnalysis
    from ._6674 import ConicalGearCompoundCriticalSpeedAnalysis
    from ._6675 import ConicalGearMeshCompoundCriticalSpeedAnalysis
    from ._6676 import ConicalGearSetCompoundCriticalSpeedAnalysis
    from ._6677 import ConnectionCompoundCriticalSpeedAnalysis
    from ._6678 import ConnectorCompoundCriticalSpeedAnalysis
    from ._6679 import CouplingCompoundCriticalSpeedAnalysis
    from ._6680 import CouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6681 import CouplingHalfCompoundCriticalSpeedAnalysis
    from ._6682 import CVTBeltConnectionCompoundCriticalSpeedAnalysis
    from ._6683 import CVTCompoundCriticalSpeedAnalysis
    from ._6684 import CVTPulleyCompoundCriticalSpeedAnalysis
    from ._6685 import CycloidalAssemblyCompoundCriticalSpeedAnalysis
    from ._6686 import CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis
    from ._6687 import CycloidalDiscCompoundCriticalSpeedAnalysis
    from ._6688 import CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis
    from ._6689 import CylindricalGearCompoundCriticalSpeedAnalysis
    from ._6690 import CylindricalGearMeshCompoundCriticalSpeedAnalysis
    from ._6691 import CylindricalGearSetCompoundCriticalSpeedAnalysis
    from ._6692 import CylindricalPlanetGearCompoundCriticalSpeedAnalysis
    from ._6693 import DatumCompoundCriticalSpeedAnalysis
    from ._6694 import ExternalCADModelCompoundCriticalSpeedAnalysis
    from ._6695 import FaceGearCompoundCriticalSpeedAnalysis
    from ._6696 import FaceGearMeshCompoundCriticalSpeedAnalysis
    from ._6697 import FaceGearSetCompoundCriticalSpeedAnalysis
    from ._6698 import FEPartCompoundCriticalSpeedAnalysis
    from ._6699 import FlexiblePinAssemblyCompoundCriticalSpeedAnalysis
    from ._6700 import GearCompoundCriticalSpeedAnalysis
    from ._6701 import GearMeshCompoundCriticalSpeedAnalysis
    from ._6702 import GearSetCompoundCriticalSpeedAnalysis
    from ._6703 import GuideDxfModelCompoundCriticalSpeedAnalysis
    from ._6704 import HypoidGearCompoundCriticalSpeedAnalysis
    from ._6705 import HypoidGearMeshCompoundCriticalSpeedAnalysis
    from ._6706 import HypoidGearSetCompoundCriticalSpeedAnalysis
    from ._6707 import InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
    from ._6708 import KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
    from ._6709 import KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis
    from ._6710 import KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis
    from ._6711 import KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
    from ._6712 import KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis
    from ._6713 import KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis
    from ._6714 import KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis
    from ._6715 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6716 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis
    from ._6717 import MassDiscCompoundCriticalSpeedAnalysis
    from ._6718 import MeasurementComponentCompoundCriticalSpeedAnalysis
    from ._6719 import MountableComponentCompoundCriticalSpeedAnalysis
    from ._6720 import OilSealCompoundCriticalSpeedAnalysis
    from ._6721 import PartCompoundCriticalSpeedAnalysis
    from ._6722 import PartToPartShearCouplingCompoundCriticalSpeedAnalysis
    from ._6723 import PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6724 import PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis
    from ._6725 import PlanetaryConnectionCompoundCriticalSpeedAnalysis
    from ._6726 import PlanetaryGearSetCompoundCriticalSpeedAnalysis
    from ._6727 import PlanetCarrierCompoundCriticalSpeedAnalysis
    from ._6728 import PointLoadCompoundCriticalSpeedAnalysis
    from ._6729 import PowerLoadCompoundCriticalSpeedAnalysis
    from ._6730 import PulleyCompoundCriticalSpeedAnalysis
    from ._6731 import RingPinsCompoundCriticalSpeedAnalysis
    from ._6732 import RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis
    from ._6733 import RollingRingAssemblyCompoundCriticalSpeedAnalysis
    from ._6734 import RollingRingCompoundCriticalSpeedAnalysis
    from ._6735 import RollingRingConnectionCompoundCriticalSpeedAnalysis
    from ._6736 import RootAssemblyCompoundCriticalSpeedAnalysis
    from ._6737 import ShaftCompoundCriticalSpeedAnalysis
    from ._6738 import ShaftHubConnectionCompoundCriticalSpeedAnalysis
    from ._6739 import ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
    from ._6740 import SpecialisedAssemblyCompoundCriticalSpeedAnalysis
    from ._6741 import SpiralBevelGearCompoundCriticalSpeedAnalysis
    from ._6742 import SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6743 import SpiralBevelGearSetCompoundCriticalSpeedAnalysis
    from ._6744 import SpringDamperCompoundCriticalSpeedAnalysis
    from ._6745 import SpringDamperConnectionCompoundCriticalSpeedAnalysis
    from ._6746 import SpringDamperHalfCompoundCriticalSpeedAnalysis
    from ._6747 import StraightBevelDiffGearCompoundCriticalSpeedAnalysis
    from ._6748 import StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
    from ._6749 import StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
    from ._6750 import StraightBevelGearCompoundCriticalSpeedAnalysis
    from ._6751 import StraightBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6752 import StraightBevelGearSetCompoundCriticalSpeedAnalysis
    from ._6753 import StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
    from ._6754 import StraightBevelSunGearCompoundCriticalSpeedAnalysis
    from ._6755 import SynchroniserCompoundCriticalSpeedAnalysis
    from ._6756 import SynchroniserHalfCompoundCriticalSpeedAnalysis
    from ._6757 import SynchroniserPartCompoundCriticalSpeedAnalysis
    from ._6758 import SynchroniserSleeveCompoundCriticalSpeedAnalysis
    from ._6759 import TorqueConverterCompoundCriticalSpeedAnalysis
    from ._6760 import TorqueConverterConnectionCompoundCriticalSpeedAnalysis
    from ._6761 import TorqueConverterPumpCompoundCriticalSpeedAnalysis
    from ._6762 import TorqueConverterTurbineCompoundCriticalSpeedAnalysis
    from ._6763 import UnbalancedMassCompoundCriticalSpeedAnalysis
    from ._6764 import VirtualComponentCompoundCriticalSpeedAnalysis
    from ._6765 import WormGearCompoundCriticalSpeedAnalysis
    from ._6766 import WormGearMeshCompoundCriticalSpeedAnalysis
    from ._6767 import WormGearSetCompoundCriticalSpeedAnalysis
    from ._6768 import ZerolBevelGearCompoundCriticalSpeedAnalysis
    from ._6769 import ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6770 import ZerolBevelGearSetCompoundCriticalSpeedAnalysis
else:
    import_structure = {
        '_6642': ['AbstractAssemblyCompoundCriticalSpeedAnalysis'],
        '_6643': ['AbstractShaftCompoundCriticalSpeedAnalysis'],
        '_6644': ['AbstractShaftOrHousingCompoundCriticalSpeedAnalysis'],
        '_6645': ['AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis'],
        '_6646': ['AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis'],
        '_6647': ['AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis'],
        '_6648': ['AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis'],
        '_6649': ['AssemblyCompoundCriticalSpeedAnalysis'],
        '_6650': ['BearingCompoundCriticalSpeedAnalysis'],
        '_6651': ['BeltConnectionCompoundCriticalSpeedAnalysis'],
        '_6652': ['BeltDriveCompoundCriticalSpeedAnalysis'],
        '_6653': ['BevelDifferentialGearCompoundCriticalSpeedAnalysis'],
        '_6654': ['BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis'],
        '_6655': ['BevelDifferentialGearSetCompoundCriticalSpeedAnalysis'],
        '_6656': ['BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis'],
        '_6657': ['BevelDifferentialSunGearCompoundCriticalSpeedAnalysis'],
        '_6658': ['BevelGearCompoundCriticalSpeedAnalysis'],
        '_6659': ['BevelGearMeshCompoundCriticalSpeedAnalysis'],
        '_6660': ['BevelGearSetCompoundCriticalSpeedAnalysis'],
        '_6661': ['BoltCompoundCriticalSpeedAnalysis'],
        '_6662': ['BoltedJointCompoundCriticalSpeedAnalysis'],
        '_6663': ['ClutchCompoundCriticalSpeedAnalysis'],
        '_6664': ['ClutchConnectionCompoundCriticalSpeedAnalysis'],
        '_6665': ['ClutchHalfCompoundCriticalSpeedAnalysis'],
        '_6666': ['CoaxialConnectionCompoundCriticalSpeedAnalysis'],
        '_6667': ['ComponentCompoundCriticalSpeedAnalysis'],
        '_6668': ['ConceptCouplingCompoundCriticalSpeedAnalysis'],
        '_6669': ['ConceptCouplingConnectionCompoundCriticalSpeedAnalysis'],
        '_6670': ['ConceptCouplingHalfCompoundCriticalSpeedAnalysis'],
        '_6671': ['ConceptGearCompoundCriticalSpeedAnalysis'],
        '_6672': ['ConceptGearMeshCompoundCriticalSpeedAnalysis'],
        '_6673': ['ConceptGearSetCompoundCriticalSpeedAnalysis'],
        '_6674': ['ConicalGearCompoundCriticalSpeedAnalysis'],
        '_6675': ['ConicalGearMeshCompoundCriticalSpeedAnalysis'],
        '_6676': ['ConicalGearSetCompoundCriticalSpeedAnalysis'],
        '_6677': ['ConnectionCompoundCriticalSpeedAnalysis'],
        '_6678': ['ConnectorCompoundCriticalSpeedAnalysis'],
        '_6679': ['CouplingCompoundCriticalSpeedAnalysis'],
        '_6680': ['CouplingConnectionCompoundCriticalSpeedAnalysis'],
        '_6681': ['CouplingHalfCompoundCriticalSpeedAnalysis'],
        '_6682': ['CVTBeltConnectionCompoundCriticalSpeedAnalysis'],
        '_6683': ['CVTCompoundCriticalSpeedAnalysis'],
        '_6684': ['CVTPulleyCompoundCriticalSpeedAnalysis'],
        '_6685': ['CycloidalAssemblyCompoundCriticalSpeedAnalysis'],
        '_6686': ['CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis'],
        '_6687': ['CycloidalDiscCompoundCriticalSpeedAnalysis'],
        '_6688': ['CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis'],
        '_6689': ['CylindricalGearCompoundCriticalSpeedAnalysis'],
        '_6690': ['CylindricalGearMeshCompoundCriticalSpeedAnalysis'],
        '_6691': ['CylindricalGearSetCompoundCriticalSpeedAnalysis'],
        '_6692': ['CylindricalPlanetGearCompoundCriticalSpeedAnalysis'],
        '_6693': ['DatumCompoundCriticalSpeedAnalysis'],
        '_6694': ['ExternalCADModelCompoundCriticalSpeedAnalysis'],
        '_6695': ['FaceGearCompoundCriticalSpeedAnalysis'],
        '_6696': ['FaceGearMeshCompoundCriticalSpeedAnalysis'],
        '_6697': ['FaceGearSetCompoundCriticalSpeedAnalysis'],
        '_6698': ['FEPartCompoundCriticalSpeedAnalysis'],
        '_6699': ['FlexiblePinAssemblyCompoundCriticalSpeedAnalysis'],
        '_6700': ['GearCompoundCriticalSpeedAnalysis'],
        '_6701': ['GearMeshCompoundCriticalSpeedAnalysis'],
        '_6702': ['GearSetCompoundCriticalSpeedAnalysis'],
        '_6703': ['GuideDxfModelCompoundCriticalSpeedAnalysis'],
        '_6704': ['HypoidGearCompoundCriticalSpeedAnalysis'],
        '_6705': ['HypoidGearMeshCompoundCriticalSpeedAnalysis'],
        '_6706': ['HypoidGearSetCompoundCriticalSpeedAnalysis'],
        '_6707': ['InterMountableComponentConnectionCompoundCriticalSpeedAnalysis'],
        '_6708': ['KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis'],
        '_6709': ['KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis'],
        '_6710': ['KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis'],
        '_6711': ['KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis'],
        '_6712': ['KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis'],
        '_6713': ['KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis'],
        '_6714': ['KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis'],
        '_6715': ['KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis'],
        '_6716': ['KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis'],
        '_6717': ['MassDiscCompoundCriticalSpeedAnalysis'],
        '_6718': ['MeasurementComponentCompoundCriticalSpeedAnalysis'],
        '_6719': ['MountableComponentCompoundCriticalSpeedAnalysis'],
        '_6720': ['OilSealCompoundCriticalSpeedAnalysis'],
        '_6721': ['PartCompoundCriticalSpeedAnalysis'],
        '_6722': ['PartToPartShearCouplingCompoundCriticalSpeedAnalysis'],
        '_6723': ['PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis'],
        '_6724': ['PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis'],
        '_6725': ['PlanetaryConnectionCompoundCriticalSpeedAnalysis'],
        '_6726': ['PlanetaryGearSetCompoundCriticalSpeedAnalysis'],
        '_6727': ['PlanetCarrierCompoundCriticalSpeedAnalysis'],
        '_6728': ['PointLoadCompoundCriticalSpeedAnalysis'],
        '_6729': ['PowerLoadCompoundCriticalSpeedAnalysis'],
        '_6730': ['PulleyCompoundCriticalSpeedAnalysis'],
        '_6731': ['RingPinsCompoundCriticalSpeedAnalysis'],
        '_6732': ['RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis'],
        '_6733': ['RollingRingAssemblyCompoundCriticalSpeedAnalysis'],
        '_6734': ['RollingRingCompoundCriticalSpeedAnalysis'],
        '_6735': ['RollingRingConnectionCompoundCriticalSpeedAnalysis'],
        '_6736': ['RootAssemblyCompoundCriticalSpeedAnalysis'],
        '_6737': ['ShaftCompoundCriticalSpeedAnalysis'],
        '_6738': ['ShaftHubConnectionCompoundCriticalSpeedAnalysis'],
        '_6739': ['ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis'],
        '_6740': ['SpecialisedAssemblyCompoundCriticalSpeedAnalysis'],
        '_6741': ['SpiralBevelGearCompoundCriticalSpeedAnalysis'],
        '_6742': ['SpiralBevelGearMeshCompoundCriticalSpeedAnalysis'],
        '_6743': ['SpiralBevelGearSetCompoundCriticalSpeedAnalysis'],
        '_6744': ['SpringDamperCompoundCriticalSpeedAnalysis'],
        '_6745': ['SpringDamperConnectionCompoundCriticalSpeedAnalysis'],
        '_6746': ['SpringDamperHalfCompoundCriticalSpeedAnalysis'],
        '_6747': ['StraightBevelDiffGearCompoundCriticalSpeedAnalysis'],
        '_6748': ['StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis'],
        '_6749': ['StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis'],
        '_6750': ['StraightBevelGearCompoundCriticalSpeedAnalysis'],
        '_6751': ['StraightBevelGearMeshCompoundCriticalSpeedAnalysis'],
        '_6752': ['StraightBevelGearSetCompoundCriticalSpeedAnalysis'],
        '_6753': ['StraightBevelPlanetGearCompoundCriticalSpeedAnalysis'],
        '_6754': ['StraightBevelSunGearCompoundCriticalSpeedAnalysis'],
        '_6755': ['SynchroniserCompoundCriticalSpeedAnalysis'],
        '_6756': ['SynchroniserHalfCompoundCriticalSpeedAnalysis'],
        '_6757': ['SynchroniserPartCompoundCriticalSpeedAnalysis'],
        '_6758': ['SynchroniserSleeveCompoundCriticalSpeedAnalysis'],
        '_6759': ['TorqueConverterCompoundCriticalSpeedAnalysis'],
        '_6760': ['TorqueConverterConnectionCompoundCriticalSpeedAnalysis'],
        '_6761': ['TorqueConverterPumpCompoundCriticalSpeedAnalysis'],
        '_6762': ['TorqueConverterTurbineCompoundCriticalSpeedAnalysis'],
        '_6763': ['UnbalancedMassCompoundCriticalSpeedAnalysis'],
        '_6764': ['VirtualComponentCompoundCriticalSpeedAnalysis'],
        '_6765': ['WormGearCompoundCriticalSpeedAnalysis'],
        '_6766': ['WormGearMeshCompoundCriticalSpeedAnalysis'],
        '_6767': ['WormGearSetCompoundCriticalSpeedAnalysis'],
        '_6768': ['ZerolBevelGearCompoundCriticalSpeedAnalysis'],
        '_6769': ['ZerolBevelGearMeshCompoundCriticalSpeedAnalysis'],
        '_6770': ['ZerolBevelGearSetCompoundCriticalSpeedAnalysis'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
