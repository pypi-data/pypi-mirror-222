"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3745 import AbstractAssemblyStabilityAnalysis
    from ._3746 import AbstractShaftOrHousingStabilityAnalysis
    from ._3747 import AbstractShaftStabilityAnalysis
    from ._3748 import AbstractShaftToMountableComponentConnectionStabilityAnalysis
    from ._3749 import AGMAGleasonConicalGearMeshStabilityAnalysis
    from ._3750 import AGMAGleasonConicalGearSetStabilityAnalysis
    from ._3751 import AGMAGleasonConicalGearStabilityAnalysis
    from ._3752 import AssemblyStabilityAnalysis
    from ._3753 import BearingStabilityAnalysis
    from ._3754 import BeltConnectionStabilityAnalysis
    from ._3755 import BeltDriveStabilityAnalysis
    from ._3756 import BevelDifferentialGearMeshStabilityAnalysis
    from ._3757 import BevelDifferentialGearSetStabilityAnalysis
    from ._3758 import BevelDifferentialGearStabilityAnalysis
    from ._3759 import BevelDifferentialPlanetGearStabilityAnalysis
    from ._3760 import BevelDifferentialSunGearStabilityAnalysis
    from ._3761 import BevelGearMeshStabilityAnalysis
    from ._3762 import BevelGearSetStabilityAnalysis
    from ._3763 import BevelGearStabilityAnalysis
    from ._3764 import BoltedJointStabilityAnalysis
    from ._3765 import BoltStabilityAnalysis
    from ._3766 import ClutchConnectionStabilityAnalysis
    from ._3767 import ClutchHalfStabilityAnalysis
    from ._3768 import ClutchStabilityAnalysis
    from ._3769 import CoaxialConnectionStabilityAnalysis
    from ._3770 import ComponentStabilityAnalysis
    from ._3771 import ConceptCouplingConnectionStabilityAnalysis
    from ._3772 import ConceptCouplingHalfStabilityAnalysis
    from ._3773 import ConceptCouplingStabilityAnalysis
    from ._3774 import ConceptGearMeshStabilityAnalysis
    from ._3775 import ConceptGearSetStabilityAnalysis
    from ._3776 import ConceptGearStabilityAnalysis
    from ._3777 import ConicalGearMeshStabilityAnalysis
    from ._3778 import ConicalGearSetStabilityAnalysis
    from ._3779 import ConicalGearStabilityAnalysis
    from ._3780 import ConnectionStabilityAnalysis
    from ._3781 import ConnectorStabilityAnalysis
    from ._3782 import CouplingConnectionStabilityAnalysis
    from ._3783 import CouplingHalfStabilityAnalysis
    from ._3784 import CouplingStabilityAnalysis
    from ._3785 import CriticalSpeed
    from ._3786 import CVTBeltConnectionStabilityAnalysis
    from ._3787 import CVTPulleyStabilityAnalysis
    from ._3788 import CVTStabilityAnalysis
    from ._3789 import CycloidalAssemblyStabilityAnalysis
    from ._3790 import CycloidalDiscCentralBearingConnectionStabilityAnalysis
    from ._3791 import CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis
    from ._3792 import CycloidalDiscStabilityAnalysis
    from ._3793 import CylindricalGearMeshStabilityAnalysis
    from ._3794 import CylindricalGearSetStabilityAnalysis
    from ._3795 import CylindricalGearStabilityAnalysis
    from ._3796 import CylindricalPlanetGearStabilityAnalysis
    from ._3797 import DatumStabilityAnalysis
    from ._2612 import DynamicModelForStabilityAnalysis
    from ._3798 import ExternalCADModelStabilityAnalysis
    from ._3799 import FaceGearMeshStabilityAnalysis
    from ._3800 import FaceGearSetStabilityAnalysis
    from ._3801 import FaceGearStabilityAnalysis
    from ._3802 import FEPartStabilityAnalysis
    from ._3803 import FlexiblePinAssemblyStabilityAnalysis
    from ._3804 import GearMeshStabilityAnalysis
    from ._3805 import GearSetStabilityAnalysis
    from ._3806 import GearStabilityAnalysis
    from ._3807 import GuideDxfModelStabilityAnalysis
    from ._3808 import HypoidGearMeshStabilityAnalysis
    from ._3809 import HypoidGearSetStabilityAnalysis
    from ._3810 import HypoidGearStabilityAnalysis
    from ._3811 import InterMountableComponentConnectionStabilityAnalysis
    from ._3812 import KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis
    from ._3813 import KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
    from ._3814 import KlingelnbergCycloPalloidConicalGearStabilityAnalysis
    from ._3815 import KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis
    from ._3816 import KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
    from ._3817 import KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
    from ._3818 import KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis
    from ._3819 import KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
    from ._3820 import KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
    from ._3821 import MassDiscStabilityAnalysis
    from ._3822 import MeasurementComponentStabilityAnalysis
    from ._3823 import MountableComponentStabilityAnalysis
    from ._3824 import OilSealStabilityAnalysis
    from ._3825 import PartStabilityAnalysis
    from ._3826 import PartToPartShearCouplingConnectionStabilityAnalysis
    from ._3827 import PartToPartShearCouplingHalfStabilityAnalysis
    from ._3828 import PartToPartShearCouplingStabilityAnalysis
    from ._3829 import PlanetaryConnectionStabilityAnalysis
    from ._3830 import PlanetaryGearSetStabilityAnalysis
    from ._3831 import PlanetCarrierStabilityAnalysis
    from ._3832 import PointLoadStabilityAnalysis
    from ._3833 import PowerLoadStabilityAnalysis
    from ._3834 import PulleyStabilityAnalysis
    from ._3835 import RingPinsStabilityAnalysis
    from ._3836 import RingPinsToDiscConnectionStabilityAnalysis
    from ._3837 import RollingRingAssemblyStabilityAnalysis
    from ._3838 import RollingRingConnectionStabilityAnalysis
    from ._3839 import RollingRingStabilityAnalysis
    from ._3840 import RootAssemblyStabilityAnalysis
    from ._3841 import ShaftHubConnectionStabilityAnalysis
    from ._3842 import ShaftStabilityAnalysis
    from ._3843 import ShaftToMountableComponentConnectionStabilityAnalysis
    from ._3844 import SpecialisedAssemblyStabilityAnalysis
    from ._3845 import SpiralBevelGearMeshStabilityAnalysis
    from ._3846 import SpiralBevelGearSetStabilityAnalysis
    from ._3847 import SpiralBevelGearStabilityAnalysis
    from ._3848 import SpringDamperConnectionStabilityAnalysis
    from ._3849 import SpringDamperHalfStabilityAnalysis
    from ._3850 import SpringDamperStabilityAnalysis
    from ._2624 import StabilityAnalysis
    from ._3851 import StabilityAnalysisDrawStyle
    from ._3852 import StabilityAnalysisOptions
    from ._3853 import StraightBevelDiffGearMeshStabilityAnalysis
    from ._3854 import StraightBevelDiffGearSetStabilityAnalysis
    from ._3855 import StraightBevelDiffGearStabilityAnalysis
    from ._3856 import StraightBevelGearMeshStabilityAnalysis
    from ._3857 import StraightBevelGearSetStabilityAnalysis
    from ._3858 import StraightBevelGearStabilityAnalysis
    from ._3859 import StraightBevelPlanetGearStabilityAnalysis
    from ._3860 import StraightBevelSunGearStabilityAnalysis
    from ._3861 import SynchroniserHalfStabilityAnalysis
    from ._3862 import SynchroniserPartStabilityAnalysis
    from ._3863 import SynchroniserSleeveStabilityAnalysis
    from ._3864 import SynchroniserStabilityAnalysis
    from ._3865 import TorqueConverterConnectionStabilityAnalysis
    from ._3866 import TorqueConverterPumpStabilityAnalysis
    from ._3867 import TorqueConverterStabilityAnalysis
    from ._3868 import TorqueConverterTurbineStabilityAnalysis
    from ._3869 import UnbalancedMassStabilityAnalysis
    from ._3870 import VirtualComponentStabilityAnalysis
    from ._3871 import WormGearMeshStabilityAnalysis
    from ._3872 import WormGearSetStabilityAnalysis
    from ._3873 import WormGearStabilityAnalysis
    from ._3874 import ZerolBevelGearMeshStabilityAnalysis
    from ._3875 import ZerolBevelGearSetStabilityAnalysis
    from ._3876 import ZerolBevelGearStabilityAnalysis
else:
    import_structure = {
        '_3745': ['AbstractAssemblyStabilityAnalysis'],
        '_3746': ['AbstractShaftOrHousingStabilityAnalysis'],
        '_3747': ['AbstractShaftStabilityAnalysis'],
        '_3748': ['AbstractShaftToMountableComponentConnectionStabilityAnalysis'],
        '_3749': ['AGMAGleasonConicalGearMeshStabilityAnalysis'],
        '_3750': ['AGMAGleasonConicalGearSetStabilityAnalysis'],
        '_3751': ['AGMAGleasonConicalGearStabilityAnalysis'],
        '_3752': ['AssemblyStabilityAnalysis'],
        '_3753': ['BearingStabilityAnalysis'],
        '_3754': ['BeltConnectionStabilityAnalysis'],
        '_3755': ['BeltDriveStabilityAnalysis'],
        '_3756': ['BevelDifferentialGearMeshStabilityAnalysis'],
        '_3757': ['BevelDifferentialGearSetStabilityAnalysis'],
        '_3758': ['BevelDifferentialGearStabilityAnalysis'],
        '_3759': ['BevelDifferentialPlanetGearStabilityAnalysis'],
        '_3760': ['BevelDifferentialSunGearStabilityAnalysis'],
        '_3761': ['BevelGearMeshStabilityAnalysis'],
        '_3762': ['BevelGearSetStabilityAnalysis'],
        '_3763': ['BevelGearStabilityAnalysis'],
        '_3764': ['BoltedJointStabilityAnalysis'],
        '_3765': ['BoltStabilityAnalysis'],
        '_3766': ['ClutchConnectionStabilityAnalysis'],
        '_3767': ['ClutchHalfStabilityAnalysis'],
        '_3768': ['ClutchStabilityAnalysis'],
        '_3769': ['CoaxialConnectionStabilityAnalysis'],
        '_3770': ['ComponentStabilityAnalysis'],
        '_3771': ['ConceptCouplingConnectionStabilityAnalysis'],
        '_3772': ['ConceptCouplingHalfStabilityAnalysis'],
        '_3773': ['ConceptCouplingStabilityAnalysis'],
        '_3774': ['ConceptGearMeshStabilityAnalysis'],
        '_3775': ['ConceptGearSetStabilityAnalysis'],
        '_3776': ['ConceptGearStabilityAnalysis'],
        '_3777': ['ConicalGearMeshStabilityAnalysis'],
        '_3778': ['ConicalGearSetStabilityAnalysis'],
        '_3779': ['ConicalGearStabilityAnalysis'],
        '_3780': ['ConnectionStabilityAnalysis'],
        '_3781': ['ConnectorStabilityAnalysis'],
        '_3782': ['CouplingConnectionStabilityAnalysis'],
        '_3783': ['CouplingHalfStabilityAnalysis'],
        '_3784': ['CouplingStabilityAnalysis'],
        '_3785': ['CriticalSpeed'],
        '_3786': ['CVTBeltConnectionStabilityAnalysis'],
        '_3787': ['CVTPulleyStabilityAnalysis'],
        '_3788': ['CVTStabilityAnalysis'],
        '_3789': ['CycloidalAssemblyStabilityAnalysis'],
        '_3790': ['CycloidalDiscCentralBearingConnectionStabilityAnalysis'],
        '_3791': ['CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis'],
        '_3792': ['CycloidalDiscStabilityAnalysis'],
        '_3793': ['CylindricalGearMeshStabilityAnalysis'],
        '_3794': ['CylindricalGearSetStabilityAnalysis'],
        '_3795': ['CylindricalGearStabilityAnalysis'],
        '_3796': ['CylindricalPlanetGearStabilityAnalysis'],
        '_3797': ['DatumStabilityAnalysis'],
        '_2612': ['DynamicModelForStabilityAnalysis'],
        '_3798': ['ExternalCADModelStabilityAnalysis'],
        '_3799': ['FaceGearMeshStabilityAnalysis'],
        '_3800': ['FaceGearSetStabilityAnalysis'],
        '_3801': ['FaceGearStabilityAnalysis'],
        '_3802': ['FEPartStabilityAnalysis'],
        '_3803': ['FlexiblePinAssemblyStabilityAnalysis'],
        '_3804': ['GearMeshStabilityAnalysis'],
        '_3805': ['GearSetStabilityAnalysis'],
        '_3806': ['GearStabilityAnalysis'],
        '_3807': ['GuideDxfModelStabilityAnalysis'],
        '_3808': ['HypoidGearMeshStabilityAnalysis'],
        '_3809': ['HypoidGearSetStabilityAnalysis'],
        '_3810': ['HypoidGearStabilityAnalysis'],
        '_3811': ['InterMountableComponentConnectionStabilityAnalysis'],
        '_3812': ['KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis'],
        '_3813': ['KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis'],
        '_3814': ['KlingelnbergCycloPalloidConicalGearStabilityAnalysis'],
        '_3815': ['KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis'],
        '_3816': ['KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis'],
        '_3817': ['KlingelnbergCycloPalloidHypoidGearStabilityAnalysis'],
        '_3818': ['KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis'],
        '_3819': ['KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis'],
        '_3820': ['KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis'],
        '_3821': ['MassDiscStabilityAnalysis'],
        '_3822': ['MeasurementComponentStabilityAnalysis'],
        '_3823': ['MountableComponentStabilityAnalysis'],
        '_3824': ['OilSealStabilityAnalysis'],
        '_3825': ['PartStabilityAnalysis'],
        '_3826': ['PartToPartShearCouplingConnectionStabilityAnalysis'],
        '_3827': ['PartToPartShearCouplingHalfStabilityAnalysis'],
        '_3828': ['PartToPartShearCouplingStabilityAnalysis'],
        '_3829': ['PlanetaryConnectionStabilityAnalysis'],
        '_3830': ['PlanetaryGearSetStabilityAnalysis'],
        '_3831': ['PlanetCarrierStabilityAnalysis'],
        '_3832': ['PointLoadStabilityAnalysis'],
        '_3833': ['PowerLoadStabilityAnalysis'],
        '_3834': ['PulleyStabilityAnalysis'],
        '_3835': ['RingPinsStabilityAnalysis'],
        '_3836': ['RingPinsToDiscConnectionStabilityAnalysis'],
        '_3837': ['RollingRingAssemblyStabilityAnalysis'],
        '_3838': ['RollingRingConnectionStabilityAnalysis'],
        '_3839': ['RollingRingStabilityAnalysis'],
        '_3840': ['RootAssemblyStabilityAnalysis'],
        '_3841': ['ShaftHubConnectionStabilityAnalysis'],
        '_3842': ['ShaftStabilityAnalysis'],
        '_3843': ['ShaftToMountableComponentConnectionStabilityAnalysis'],
        '_3844': ['SpecialisedAssemblyStabilityAnalysis'],
        '_3845': ['SpiralBevelGearMeshStabilityAnalysis'],
        '_3846': ['SpiralBevelGearSetStabilityAnalysis'],
        '_3847': ['SpiralBevelGearStabilityAnalysis'],
        '_3848': ['SpringDamperConnectionStabilityAnalysis'],
        '_3849': ['SpringDamperHalfStabilityAnalysis'],
        '_3850': ['SpringDamperStabilityAnalysis'],
        '_2624': ['StabilityAnalysis'],
        '_3851': ['StabilityAnalysisDrawStyle'],
        '_3852': ['StabilityAnalysisOptions'],
        '_3853': ['StraightBevelDiffGearMeshStabilityAnalysis'],
        '_3854': ['StraightBevelDiffGearSetStabilityAnalysis'],
        '_3855': ['StraightBevelDiffGearStabilityAnalysis'],
        '_3856': ['StraightBevelGearMeshStabilityAnalysis'],
        '_3857': ['StraightBevelGearSetStabilityAnalysis'],
        '_3858': ['StraightBevelGearStabilityAnalysis'],
        '_3859': ['StraightBevelPlanetGearStabilityAnalysis'],
        '_3860': ['StraightBevelSunGearStabilityAnalysis'],
        '_3861': ['SynchroniserHalfStabilityAnalysis'],
        '_3862': ['SynchroniserPartStabilityAnalysis'],
        '_3863': ['SynchroniserSleeveStabilityAnalysis'],
        '_3864': ['SynchroniserStabilityAnalysis'],
        '_3865': ['TorqueConverterConnectionStabilityAnalysis'],
        '_3866': ['TorqueConverterPumpStabilityAnalysis'],
        '_3867': ['TorqueConverterStabilityAnalysis'],
        '_3868': ['TorqueConverterTurbineStabilityAnalysis'],
        '_3869': ['UnbalancedMassStabilityAnalysis'],
        '_3870': ['VirtualComponentStabilityAnalysis'],
        '_3871': ['WormGearMeshStabilityAnalysis'],
        '_3872': ['WormGearSetStabilityAnalysis'],
        '_3873': ['WormGearStabilityAnalysis'],
        '_3874': ['ZerolBevelGearMeshStabilityAnalysis'],
        '_3875': ['ZerolBevelGearSetStabilityAnalysis'],
        '_3876': ['ZerolBevelGearStabilityAnalysis'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
