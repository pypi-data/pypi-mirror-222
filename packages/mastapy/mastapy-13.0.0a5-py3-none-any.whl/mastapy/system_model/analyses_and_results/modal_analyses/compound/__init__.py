"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4704 import AbstractAssemblyCompoundModalAnalysis
    from ._4705 import AbstractShaftCompoundModalAnalysis
    from ._4706 import AbstractShaftOrHousingCompoundModalAnalysis
    from ._4707 import AbstractShaftToMountableComponentConnectionCompoundModalAnalysis
    from ._4708 import AGMAGleasonConicalGearCompoundModalAnalysis
    from ._4709 import AGMAGleasonConicalGearMeshCompoundModalAnalysis
    from ._4710 import AGMAGleasonConicalGearSetCompoundModalAnalysis
    from ._4711 import AssemblyCompoundModalAnalysis
    from ._4712 import BearingCompoundModalAnalysis
    from ._4713 import BeltConnectionCompoundModalAnalysis
    from ._4714 import BeltDriveCompoundModalAnalysis
    from ._4715 import BevelDifferentialGearCompoundModalAnalysis
    from ._4716 import BevelDifferentialGearMeshCompoundModalAnalysis
    from ._4717 import BevelDifferentialGearSetCompoundModalAnalysis
    from ._4718 import BevelDifferentialPlanetGearCompoundModalAnalysis
    from ._4719 import BevelDifferentialSunGearCompoundModalAnalysis
    from ._4720 import BevelGearCompoundModalAnalysis
    from ._4721 import BevelGearMeshCompoundModalAnalysis
    from ._4722 import BevelGearSetCompoundModalAnalysis
    from ._4723 import BoltCompoundModalAnalysis
    from ._4724 import BoltedJointCompoundModalAnalysis
    from ._4725 import ClutchCompoundModalAnalysis
    from ._4726 import ClutchConnectionCompoundModalAnalysis
    from ._4727 import ClutchHalfCompoundModalAnalysis
    from ._4728 import CoaxialConnectionCompoundModalAnalysis
    from ._4729 import ComponentCompoundModalAnalysis
    from ._4730 import ConceptCouplingCompoundModalAnalysis
    from ._4731 import ConceptCouplingConnectionCompoundModalAnalysis
    from ._4732 import ConceptCouplingHalfCompoundModalAnalysis
    from ._4733 import ConceptGearCompoundModalAnalysis
    from ._4734 import ConceptGearMeshCompoundModalAnalysis
    from ._4735 import ConceptGearSetCompoundModalAnalysis
    from ._4736 import ConicalGearCompoundModalAnalysis
    from ._4737 import ConicalGearMeshCompoundModalAnalysis
    from ._4738 import ConicalGearSetCompoundModalAnalysis
    from ._4739 import ConnectionCompoundModalAnalysis
    from ._4740 import ConnectorCompoundModalAnalysis
    from ._4741 import CouplingCompoundModalAnalysis
    from ._4742 import CouplingConnectionCompoundModalAnalysis
    from ._4743 import CouplingHalfCompoundModalAnalysis
    from ._4744 import CVTBeltConnectionCompoundModalAnalysis
    from ._4745 import CVTCompoundModalAnalysis
    from ._4746 import CVTPulleyCompoundModalAnalysis
    from ._4747 import CycloidalAssemblyCompoundModalAnalysis
    from ._4748 import CycloidalDiscCentralBearingConnectionCompoundModalAnalysis
    from ._4749 import CycloidalDiscCompoundModalAnalysis
    from ._4750 import CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis
    from ._4751 import CylindricalGearCompoundModalAnalysis
    from ._4752 import CylindricalGearMeshCompoundModalAnalysis
    from ._4753 import CylindricalGearSetCompoundModalAnalysis
    from ._4754 import CylindricalPlanetGearCompoundModalAnalysis
    from ._4755 import DatumCompoundModalAnalysis
    from ._4756 import ExternalCADModelCompoundModalAnalysis
    from ._4757 import FaceGearCompoundModalAnalysis
    from ._4758 import FaceGearMeshCompoundModalAnalysis
    from ._4759 import FaceGearSetCompoundModalAnalysis
    from ._4760 import FEPartCompoundModalAnalysis
    from ._4761 import FlexiblePinAssemblyCompoundModalAnalysis
    from ._4762 import GearCompoundModalAnalysis
    from ._4763 import GearMeshCompoundModalAnalysis
    from ._4764 import GearSetCompoundModalAnalysis
    from ._4765 import GuideDxfModelCompoundModalAnalysis
    from ._4766 import HypoidGearCompoundModalAnalysis
    from ._4767 import HypoidGearMeshCompoundModalAnalysis
    from ._4768 import HypoidGearSetCompoundModalAnalysis
    from ._4769 import InterMountableComponentConnectionCompoundModalAnalysis
    from ._4770 import KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
    from ._4771 import KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis
    from ._4772 import KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
    from ._4773 import KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
    from ._4774 import KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis
    from ._4775 import KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
    from ._4776 import KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
    from ._4777 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis
    from ._4778 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
    from ._4779 import MassDiscCompoundModalAnalysis
    from ._4780 import MeasurementComponentCompoundModalAnalysis
    from ._4781 import MountableComponentCompoundModalAnalysis
    from ._4782 import OilSealCompoundModalAnalysis
    from ._4783 import PartCompoundModalAnalysis
    from ._4784 import PartToPartShearCouplingCompoundModalAnalysis
    from ._4785 import PartToPartShearCouplingConnectionCompoundModalAnalysis
    from ._4786 import PartToPartShearCouplingHalfCompoundModalAnalysis
    from ._4787 import PlanetaryConnectionCompoundModalAnalysis
    from ._4788 import PlanetaryGearSetCompoundModalAnalysis
    from ._4789 import PlanetCarrierCompoundModalAnalysis
    from ._4790 import PointLoadCompoundModalAnalysis
    from ._4791 import PowerLoadCompoundModalAnalysis
    from ._4792 import PulleyCompoundModalAnalysis
    from ._4793 import RingPinsCompoundModalAnalysis
    from ._4794 import RingPinsToDiscConnectionCompoundModalAnalysis
    from ._4795 import RollingRingAssemblyCompoundModalAnalysis
    from ._4796 import RollingRingCompoundModalAnalysis
    from ._4797 import RollingRingConnectionCompoundModalAnalysis
    from ._4798 import RootAssemblyCompoundModalAnalysis
    from ._4799 import ShaftCompoundModalAnalysis
    from ._4800 import ShaftHubConnectionCompoundModalAnalysis
    from ._4801 import ShaftToMountableComponentConnectionCompoundModalAnalysis
    from ._4802 import SpecialisedAssemblyCompoundModalAnalysis
    from ._4803 import SpiralBevelGearCompoundModalAnalysis
    from ._4804 import SpiralBevelGearMeshCompoundModalAnalysis
    from ._4805 import SpiralBevelGearSetCompoundModalAnalysis
    from ._4806 import SpringDamperCompoundModalAnalysis
    from ._4807 import SpringDamperConnectionCompoundModalAnalysis
    from ._4808 import SpringDamperHalfCompoundModalAnalysis
    from ._4809 import StraightBevelDiffGearCompoundModalAnalysis
    from ._4810 import StraightBevelDiffGearMeshCompoundModalAnalysis
    from ._4811 import StraightBevelDiffGearSetCompoundModalAnalysis
    from ._4812 import StraightBevelGearCompoundModalAnalysis
    from ._4813 import StraightBevelGearMeshCompoundModalAnalysis
    from ._4814 import StraightBevelGearSetCompoundModalAnalysis
    from ._4815 import StraightBevelPlanetGearCompoundModalAnalysis
    from ._4816 import StraightBevelSunGearCompoundModalAnalysis
    from ._4817 import SynchroniserCompoundModalAnalysis
    from ._4818 import SynchroniserHalfCompoundModalAnalysis
    from ._4819 import SynchroniserPartCompoundModalAnalysis
    from ._4820 import SynchroniserSleeveCompoundModalAnalysis
    from ._4821 import TorqueConverterCompoundModalAnalysis
    from ._4822 import TorqueConverterConnectionCompoundModalAnalysis
    from ._4823 import TorqueConverterPumpCompoundModalAnalysis
    from ._4824 import TorqueConverterTurbineCompoundModalAnalysis
    from ._4825 import UnbalancedMassCompoundModalAnalysis
    from ._4826 import VirtualComponentCompoundModalAnalysis
    from ._4827 import WormGearCompoundModalAnalysis
    from ._4828 import WormGearMeshCompoundModalAnalysis
    from ._4829 import WormGearSetCompoundModalAnalysis
    from ._4830 import ZerolBevelGearCompoundModalAnalysis
    from ._4831 import ZerolBevelGearMeshCompoundModalAnalysis
    from ._4832 import ZerolBevelGearSetCompoundModalAnalysis
else:
    import_structure = {
        '_4704': ['AbstractAssemblyCompoundModalAnalysis'],
        '_4705': ['AbstractShaftCompoundModalAnalysis'],
        '_4706': ['AbstractShaftOrHousingCompoundModalAnalysis'],
        '_4707': ['AbstractShaftToMountableComponentConnectionCompoundModalAnalysis'],
        '_4708': ['AGMAGleasonConicalGearCompoundModalAnalysis'],
        '_4709': ['AGMAGleasonConicalGearMeshCompoundModalAnalysis'],
        '_4710': ['AGMAGleasonConicalGearSetCompoundModalAnalysis'],
        '_4711': ['AssemblyCompoundModalAnalysis'],
        '_4712': ['BearingCompoundModalAnalysis'],
        '_4713': ['BeltConnectionCompoundModalAnalysis'],
        '_4714': ['BeltDriveCompoundModalAnalysis'],
        '_4715': ['BevelDifferentialGearCompoundModalAnalysis'],
        '_4716': ['BevelDifferentialGearMeshCompoundModalAnalysis'],
        '_4717': ['BevelDifferentialGearSetCompoundModalAnalysis'],
        '_4718': ['BevelDifferentialPlanetGearCompoundModalAnalysis'],
        '_4719': ['BevelDifferentialSunGearCompoundModalAnalysis'],
        '_4720': ['BevelGearCompoundModalAnalysis'],
        '_4721': ['BevelGearMeshCompoundModalAnalysis'],
        '_4722': ['BevelGearSetCompoundModalAnalysis'],
        '_4723': ['BoltCompoundModalAnalysis'],
        '_4724': ['BoltedJointCompoundModalAnalysis'],
        '_4725': ['ClutchCompoundModalAnalysis'],
        '_4726': ['ClutchConnectionCompoundModalAnalysis'],
        '_4727': ['ClutchHalfCompoundModalAnalysis'],
        '_4728': ['CoaxialConnectionCompoundModalAnalysis'],
        '_4729': ['ComponentCompoundModalAnalysis'],
        '_4730': ['ConceptCouplingCompoundModalAnalysis'],
        '_4731': ['ConceptCouplingConnectionCompoundModalAnalysis'],
        '_4732': ['ConceptCouplingHalfCompoundModalAnalysis'],
        '_4733': ['ConceptGearCompoundModalAnalysis'],
        '_4734': ['ConceptGearMeshCompoundModalAnalysis'],
        '_4735': ['ConceptGearSetCompoundModalAnalysis'],
        '_4736': ['ConicalGearCompoundModalAnalysis'],
        '_4737': ['ConicalGearMeshCompoundModalAnalysis'],
        '_4738': ['ConicalGearSetCompoundModalAnalysis'],
        '_4739': ['ConnectionCompoundModalAnalysis'],
        '_4740': ['ConnectorCompoundModalAnalysis'],
        '_4741': ['CouplingCompoundModalAnalysis'],
        '_4742': ['CouplingConnectionCompoundModalAnalysis'],
        '_4743': ['CouplingHalfCompoundModalAnalysis'],
        '_4744': ['CVTBeltConnectionCompoundModalAnalysis'],
        '_4745': ['CVTCompoundModalAnalysis'],
        '_4746': ['CVTPulleyCompoundModalAnalysis'],
        '_4747': ['CycloidalAssemblyCompoundModalAnalysis'],
        '_4748': ['CycloidalDiscCentralBearingConnectionCompoundModalAnalysis'],
        '_4749': ['CycloidalDiscCompoundModalAnalysis'],
        '_4750': ['CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis'],
        '_4751': ['CylindricalGearCompoundModalAnalysis'],
        '_4752': ['CylindricalGearMeshCompoundModalAnalysis'],
        '_4753': ['CylindricalGearSetCompoundModalAnalysis'],
        '_4754': ['CylindricalPlanetGearCompoundModalAnalysis'],
        '_4755': ['DatumCompoundModalAnalysis'],
        '_4756': ['ExternalCADModelCompoundModalAnalysis'],
        '_4757': ['FaceGearCompoundModalAnalysis'],
        '_4758': ['FaceGearMeshCompoundModalAnalysis'],
        '_4759': ['FaceGearSetCompoundModalAnalysis'],
        '_4760': ['FEPartCompoundModalAnalysis'],
        '_4761': ['FlexiblePinAssemblyCompoundModalAnalysis'],
        '_4762': ['GearCompoundModalAnalysis'],
        '_4763': ['GearMeshCompoundModalAnalysis'],
        '_4764': ['GearSetCompoundModalAnalysis'],
        '_4765': ['GuideDxfModelCompoundModalAnalysis'],
        '_4766': ['HypoidGearCompoundModalAnalysis'],
        '_4767': ['HypoidGearMeshCompoundModalAnalysis'],
        '_4768': ['HypoidGearSetCompoundModalAnalysis'],
        '_4769': ['InterMountableComponentConnectionCompoundModalAnalysis'],
        '_4770': ['KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis'],
        '_4771': ['KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis'],
        '_4772': ['KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis'],
        '_4773': ['KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis'],
        '_4774': ['KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis'],
        '_4775': ['KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis'],
        '_4776': ['KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis'],
        '_4777': ['KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis'],
        '_4778': ['KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis'],
        '_4779': ['MassDiscCompoundModalAnalysis'],
        '_4780': ['MeasurementComponentCompoundModalAnalysis'],
        '_4781': ['MountableComponentCompoundModalAnalysis'],
        '_4782': ['OilSealCompoundModalAnalysis'],
        '_4783': ['PartCompoundModalAnalysis'],
        '_4784': ['PartToPartShearCouplingCompoundModalAnalysis'],
        '_4785': ['PartToPartShearCouplingConnectionCompoundModalAnalysis'],
        '_4786': ['PartToPartShearCouplingHalfCompoundModalAnalysis'],
        '_4787': ['PlanetaryConnectionCompoundModalAnalysis'],
        '_4788': ['PlanetaryGearSetCompoundModalAnalysis'],
        '_4789': ['PlanetCarrierCompoundModalAnalysis'],
        '_4790': ['PointLoadCompoundModalAnalysis'],
        '_4791': ['PowerLoadCompoundModalAnalysis'],
        '_4792': ['PulleyCompoundModalAnalysis'],
        '_4793': ['RingPinsCompoundModalAnalysis'],
        '_4794': ['RingPinsToDiscConnectionCompoundModalAnalysis'],
        '_4795': ['RollingRingAssemblyCompoundModalAnalysis'],
        '_4796': ['RollingRingCompoundModalAnalysis'],
        '_4797': ['RollingRingConnectionCompoundModalAnalysis'],
        '_4798': ['RootAssemblyCompoundModalAnalysis'],
        '_4799': ['ShaftCompoundModalAnalysis'],
        '_4800': ['ShaftHubConnectionCompoundModalAnalysis'],
        '_4801': ['ShaftToMountableComponentConnectionCompoundModalAnalysis'],
        '_4802': ['SpecialisedAssemblyCompoundModalAnalysis'],
        '_4803': ['SpiralBevelGearCompoundModalAnalysis'],
        '_4804': ['SpiralBevelGearMeshCompoundModalAnalysis'],
        '_4805': ['SpiralBevelGearSetCompoundModalAnalysis'],
        '_4806': ['SpringDamperCompoundModalAnalysis'],
        '_4807': ['SpringDamperConnectionCompoundModalAnalysis'],
        '_4808': ['SpringDamperHalfCompoundModalAnalysis'],
        '_4809': ['StraightBevelDiffGearCompoundModalAnalysis'],
        '_4810': ['StraightBevelDiffGearMeshCompoundModalAnalysis'],
        '_4811': ['StraightBevelDiffGearSetCompoundModalAnalysis'],
        '_4812': ['StraightBevelGearCompoundModalAnalysis'],
        '_4813': ['StraightBevelGearMeshCompoundModalAnalysis'],
        '_4814': ['StraightBevelGearSetCompoundModalAnalysis'],
        '_4815': ['StraightBevelPlanetGearCompoundModalAnalysis'],
        '_4816': ['StraightBevelSunGearCompoundModalAnalysis'],
        '_4817': ['SynchroniserCompoundModalAnalysis'],
        '_4818': ['SynchroniserHalfCompoundModalAnalysis'],
        '_4819': ['SynchroniserPartCompoundModalAnalysis'],
        '_4820': ['SynchroniserSleeveCompoundModalAnalysis'],
        '_4821': ['TorqueConverterCompoundModalAnalysis'],
        '_4822': ['TorqueConverterConnectionCompoundModalAnalysis'],
        '_4823': ['TorqueConverterPumpCompoundModalAnalysis'],
        '_4824': ['TorqueConverterTurbineCompoundModalAnalysis'],
        '_4825': ['UnbalancedMassCompoundModalAnalysis'],
        '_4826': ['VirtualComponentCompoundModalAnalysis'],
        '_4827': ['WormGearCompoundModalAnalysis'],
        '_4828': ['WormGearMeshCompoundModalAnalysis'],
        '_4829': ['WormGearSetCompoundModalAnalysis'],
        '_4830': ['ZerolBevelGearCompoundModalAnalysis'],
        '_4831': ['ZerolBevelGearMeshCompoundModalAnalysis'],
        '_4832': ['ZerolBevelGearSetCompoundModalAnalysis'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
