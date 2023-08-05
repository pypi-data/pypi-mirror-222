"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3877 import AbstractAssemblyCompoundStabilityAnalysis
    from ._3878 import AbstractShaftCompoundStabilityAnalysis
    from ._3879 import AbstractShaftOrHousingCompoundStabilityAnalysis
    from ._3880 import AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis
    from ._3881 import AGMAGleasonConicalGearCompoundStabilityAnalysis
    from ._3882 import AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
    from ._3883 import AGMAGleasonConicalGearSetCompoundStabilityAnalysis
    from ._3884 import AssemblyCompoundStabilityAnalysis
    from ._3885 import BearingCompoundStabilityAnalysis
    from ._3886 import BeltConnectionCompoundStabilityAnalysis
    from ._3887 import BeltDriveCompoundStabilityAnalysis
    from ._3888 import BevelDifferentialGearCompoundStabilityAnalysis
    from ._3889 import BevelDifferentialGearMeshCompoundStabilityAnalysis
    from ._3890 import BevelDifferentialGearSetCompoundStabilityAnalysis
    from ._3891 import BevelDifferentialPlanetGearCompoundStabilityAnalysis
    from ._3892 import BevelDifferentialSunGearCompoundStabilityAnalysis
    from ._3893 import BevelGearCompoundStabilityAnalysis
    from ._3894 import BevelGearMeshCompoundStabilityAnalysis
    from ._3895 import BevelGearSetCompoundStabilityAnalysis
    from ._3896 import BoltCompoundStabilityAnalysis
    from ._3897 import BoltedJointCompoundStabilityAnalysis
    from ._3898 import ClutchCompoundStabilityAnalysis
    from ._3899 import ClutchConnectionCompoundStabilityAnalysis
    from ._3900 import ClutchHalfCompoundStabilityAnalysis
    from ._3901 import CoaxialConnectionCompoundStabilityAnalysis
    from ._3902 import ComponentCompoundStabilityAnalysis
    from ._3903 import ConceptCouplingCompoundStabilityAnalysis
    from ._3904 import ConceptCouplingConnectionCompoundStabilityAnalysis
    from ._3905 import ConceptCouplingHalfCompoundStabilityAnalysis
    from ._3906 import ConceptGearCompoundStabilityAnalysis
    from ._3907 import ConceptGearMeshCompoundStabilityAnalysis
    from ._3908 import ConceptGearSetCompoundStabilityAnalysis
    from ._3909 import ConicalGearCompoundStabilityAnalysis
    from ._3910 import ConicalGearMeshCompoundStabilityAnalysis
    from ._3911 import ConicalGearSetCompoundStabilityAnalysis
    from ._3912 import ConnectionCompoundStabilityAnalysis
    from ._3913 import ConnectorCompoundStabilityAnalysis
    from ._3914 import CouplingCompoundStabilityAnalysis
    from ._3915 import CouplingConnectionCompoundStabilityAnalysis
    from ._3916 import CouplingHalfCompoundStabilityAnalysis
    from ._3917 import CVTBeltConnectionCompoundStabilityAnalysis
    from ._3918 import CVTCompoundStabilityAnalysis
    from ._3919 import CVTPulleyCompoundStabilityAnalysis
    from ._3920 import CycloidalAssemblyCompoundStabilityAnalysis
    from ._3921 import CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis
    from ._3922 import CycloidalDiscCompoundStabilityAnalysis
    from ._3923 import CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis
    from ._3924 import CylindricalGearCompoundStabilityAnalysis
    from ._3925 import CylindricalGearMeshCompoundStabilityAnalysis
    from ._3926 import CylindricalGearSetCompoundStabilityAnalysis
    from ._3927 import CylindricalPlanetGearCompoundStabilityAnalysis
    from ._3928 import DatumCompoundStabilityAnalysis
    from ._3929 import ExternalCADModelCompoundStabilityAnalysis
    from ._3930 import FaceGearCompoundStabilityAnalysis
    from ._3931 import FaceGearMeshCompoundStabilityAnalysis
    from ._3932 import FaceGearSetCompoundStabilityAnalysis
    from ._3933 import FEPartCompoundStabilityAnalysis
    from ._3934 import FlexiblePinAssemblyCompoundStabilityAnalysis
    from ._3935 import GearCompoundStabilityAnalysis
    from ._3936 import GearMeshCompoundStabilityAnalysis
    from ._3937 import GearSetCompoundStabilityAnalysis
    from ._3938 import GuideDxfModelCompoundStabilityAnalysis
    from ._3939 import HypoidGearCompoundStabilityAnalysis
    from ._3940 import HypoidGearMeshCompoundStabilityAnalysis
    from ._3941 import HypoidGearSetCompoundStabilityAnalysis
    from ._3942 import InterMountableComponentConnectionCompoundStabilityAnalysis
    from ._3943 import KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
    from ._3944 import KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis
    from ._3945 import KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
    from ._3946 import KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis
    from ._3947 import KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis
    from ._3948 import KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
    from ._3949 import KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis
    from ._3950 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis
    from ._3951 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis
    from ._3952 import MassDiscCompoundStabilityAnalysis
    from ._3953 import MeasurementComponentCompoundStabilityAnalysis
    from ._3954 import MountableComponentCompoundStabilityAnalysis
    from ._3955 import OilSealCompoundStabilityAnalysis
    from ._3956 import PartCompoundStabilityAnalysis
    from ._3957 import PartToPartShearCouplingCompoundStabilityAnalysis
    from ._3958 import PartToPartShearCouplingConnectionCompoundStabilityAnalysis
    from ._3959 import PartToPartShearCouplingHalfCompoundStabilityAnalysis
    from ._3960 import PlanetaryConnectionCompoundStabilityAnalysis
    from ._3961 import PlanetaryGearSetCompoundStabilityAnalysis
    from ._3962 import PlanetCarrierCompoundStabilityAnalysis
    from ._3963 import PointLoadCompoundStabilityAnalysis
    from ._3964 import PowerLoadCompoundStabilityAnalysis
    from ._3965 import PulleyCompoundStabilityAnalysis
    from ._3966 import RingPinsCompoundStabilityAnalysis
    from ._3967 import RingPinsToDiscConnectionCompoundStabilityAnalysis
    from ._3968 import RollingRingAssemblyCompoundStabilityAnalysis
    from ._3969 import RollingRingCompoundStabilityAnalysis
    from ._3970 import RollingRingConnectionCompoundStabilityAnalysis
    from ._3971 import RootAssemblyCompoundStabilityAnalysis
    from ._3972 import ShaftCompoundStabilityAnalysis
    from ._3973 import ShaftHubConnectionCompoundStabilityAnalysis
    from ._3974 import ShaftToMountableComponentConnectionCompoundStabilityAnalysis
    from ._3975 import SpecialisedAssemblyCompoundStabilityAnalysis
    from ._3976 import SpiralBevelGearCompoundStabilityAnalysis
    from ._3977 import SpiralBevelGearMeshCompoundStabilityAnalysis
    from ._3978 import SpiralBevelGearSetCompoundStabilityAnalysis
    from ._3979 import SpringDamperCompoundStabilityAnalysis
    from ._3980 import SpringDamperConnectionCompoundStabilityAnalysis
    from ._3981 import SpringDamperHalfCompoundStabilityAnalysis
    from ._3982 import StraightBevelDiffGearCompoundStabilityAnalysis
    from ._3983 import StraightBevelDiffGearMeshCompoundStabilityAnalysis
    from ._3984 import StraightBevelDiffGearSetCompoundStabilityAnalysis
    from ._3985 import StraightBevelGearCompoundStabilityAnalysis
    from ._3986 import StraightBevelGearMeshCompoundStabilityAnalysis
    from ._3987 import StraightBevelGearSetCompoundStabilityAnalysis
    from ._3988 import StraightBevelPlanetGearCompoundStabilityAnalysis
    from ._3989 import StraightBevelSunGearCompoundStabilityAnalysis
    from ._3990 import SynchroniserCompoundStabilityAnalysis
    from ._3991 import SynchroniserHalfCompoundStabilityAnalysis
    from ._3992 import SynchroniserPartCompoundStabilityAnalysis
    from ._3993 import SynchroniserSleeveCompoundStabilityAnalysis
    from ._3994 import TorqueConverterCompoundStabilityAnalysis
    from ._3995 import TorqueConverterConnectionCompoundStabilityAnalysis
    from ._3996 import TorqueConverterPumpCompoundStabilityAnalysis
    from ._3997 import TorqueConverterTurbineCompoundStabilityAnalysis
    from ._3998 import UnbalancedMassCompoundStabilityAnalysis
    from ._3999 import VirtualComponentCompoundStabilityAnalysis
    from ._4000 import WormGearCompoundStabilityAnalysis
    from ._4001 import WormGearMeshCompoundStabilityAnalysis
    from ._4002 import WormGearSetCompoundStabilityAnalysis
    from ._4003 import ZerolBevelGearCompoundStabilityAnalysis
    from ._4004 import ZerolBevelGearMeshCompoundStabilityAnalysis
    from ._4005 import ZerolBevelGearSetCompoundStabilityAnalysis
else:
    import_structure = {
        '_3877': ['AbstractAssemblyCompoundStabilityAnalysis'],
        '_3878': ['AbstractShaftCompoundStabilityAnalysis'],
        '_3879': ['AbstractShaftOrHousingCompoundStabilityAnalysis'],
        '_3880': ['AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis'],
        '_3881': ['AGMAGleasonConicalGearCompoundStabilityAnalysis'],
        '_3882': ['AGMAGleasonConicalGearMeshCompoundStabilityAnalysis'],
        '_3883': ['AGMAGleasonConicalGearSetCompoundStabilityAnalysis'],
        '_3884': ['AssemblyCompoundStabilityAnalysis'],
        '_3885': ['BearingCompoundStabilityAnalysis'],
        '_3886': ['BeltConnectionCompoundStabilityAnalysis'],
        '_3887': ['BeltDriveCompoundStabilityAnalysis'],
        '_3888': ['BevelDifferentialGearCompoundStabilityAnalysis'],
        '_3889': ['BevelDifferentialGearMeshCompoundStabilityAnalysis'],
        '_3890': ['BevelDifferentialGearSetCompoundStabilityAnalysis'],
        '_3891': ['BevelDifferentialPlanetGearCompoundStabilityAnalysis'],
        '_3892': ['BevelDifferentialSunGearCompoundStabilityAnalysis'],
        '_3893': ['BevelGearCompoundStabilityAnalysis'],
        '_3894': ['BevelGearMeshCompoundStabilityAnalysis'],
        '_3895': ['BevelGearSetCompoundStabilityAnalysis'],
        '_3896': ['BoltCompoundStabilityAnalysis'],
        '_3897': ['BoltedJointCompoundStabilityAnalysis'],
        '_3898': ['ClutchCompoundStabilityAnalysis'],
        '_3899': ['ClutchConnectionCompoundStabilityAnalysis'],
        '_3900': ['ClutchHalfCompoundStabilityAnalysis'],
        '_3901': ['CoaxialConnectionCompoundStabilityAnalysis'],
        '_3902': ['ComponentCompoundStabilityAnalysis'],
        '_3903': ['ConceptCouplingCompoundStabilityAnalysis'],
        '_3904': ['ConceptCouplingConnectionCompoundStabilityAnalysis'],
        '_3905': ['ConceptCouplingHalfCompoundStabilityAnalysis'],
        '_3906': ['ConceptGearCompoundStabilityAnalysis'],
        '_3907': ['ConceptGearMeshCompoundStabilityAnalysis'],
        '_3908': ['ConceptGearSetCompoundStabilityAnalysis'],
        '_3909': ['ConicalGearCompoundStabilityAnalysis'],
        '_3910': ['ConicalGearMeshCompoundStabilityAnalysis'],
        '_3911': ['ConicalGearSetCompoundStabilityAnalysis'],
        '_3912': ['ConnectionCompoundStabilityAnalysis'],
        '_3913': ['ConnectorCompoundStabilityAnalysis'],
        '_3914': ['CouplingCompoundStabilityAnalysis'],
        '_3915': ['CouplingConnectionCompoundStabilityAnalysis'],
        '_3916': ['CouplingHalfCompoundStabilityAnalysis'],
        '_3917': ['CVTBeltConnectionCompoundStabilityAnalysis'],
        '_3918': ['CVTCompoundStabilityAnalysis'],
        '_3919': ['CVTPulleyCompoundStabilityAnalysis'],
        '_3920': ['CycloidalAssemblyCompoundStabilityAnalysis'],
        '_3921': ['CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis'],
        '_3922': ['CycloidalDiscCompoundStabilityAnalysis'],
        '_3923': ['CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis'],
        '_3924': ['CylindricalGearCompoundStabilityAnalysis'],
        '_3925': ['CylindricalGearMeshCompoundStabilityAnalysis'],
        '_3926': ['CylindricalGearSetCompoundStabilityAnalysis'],
        '_3927': ['CylindricalPlanetGearCompoundStabilityAnalysis'],
        '_3928': ['DatumCompoundStabilityAnalysis'],
        '_3929': ['ExternalCADModelCompoundStabilityAnalysis'],
        '_3930': ['FaceGearCompoundStabilityAnalysis'],
        '_3931': ['FaceGearMeshCompoundStabilityAnalysis'],
        '_3932': ['FaceGearSetCompoundStabilityAnalysis'],
        '_3933': ['FEPartCompoundStabilityAnalysis'],
        '_3934': ['FlexiblePinAssemblyCompoundStabilityAnalysis'],
        '_3935': ['GearCompoundStabilityAnalysis'],
        '_3936': ['GearMeshCompoundStabilityAnalysis'],
        '_3937': ['GearSetCompoundStabilityAnalysis'],
        '_3938': ['GuideDxfModelCompoundStabilityAnalysis'],
        '_3939': ['HypoidGearCompoundStabilityAnalysis'],
        '_3940': ['HypoidGearMeshCompoundStabilityAnalysis'],
        '_3941': ['HypoidGearSetCompoundStabilityAnalysis'],
        '_3942': ['InterMountableComponentConnectionCompoundStabilityAnalysis'],
        '_3943': ['KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis'],
        '_3944': ['KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis'],
        '_3945': ['KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis'],
        '_3946': ['KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis'],
        '_3947': ['KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis'],
        '_3948': ['KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis'],
        '_3949': ['KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis'],
        '_3950': ['KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis'],
        '_3951': ['KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis'],
        '_3952': ['MassDiscCompoundStabilityAnalysis'],
        '_3953': ['MeasurementComponentCompoundStabilityAnalysis'],
        '_3954': ['MountableComponentCompoundStabilityAnalysis'],
        '_3955': ['OilSealCompoundStabilityAnalysis'],
        '_3956': ['PartCompoundStabilityAnalysis'],
        '_3957': ['PartToPartShearCouplingCompoundStabilityAnalysis'],
        '_3958': ['PartToPartShearCouplingConnectionCompoundStabilityAnalysis'],
        '_3959': ['PartToPartShearCouplingHalfCompoundStabilityAnalysis'],
        '_3960': ['PlanetaryConnectionCompoundStabilityAnalysis'],
        '_3961': ['PlanetaryGearSetCompoundStabilityAnalysis'],
        '_3962': ['PlanetCarrierCompoundStabilityAnalysis'],
        '_3963': ['PointLoadCompoundStabilityAnalysis'],
        '_3964': ['PowerLoadCompoundStabilityAnalysis'],
        '_3965': ['PulleyCompoundStabilityAnalysis'],
        '_3966': ['RingPinsCompoundStabilityAnalysis'],
        '_3967': ['RingPinsToDiscConnectionCompoundStabilityAnalysis'],
        '_3968': ['RollingRingAssemblyCompoundStabilityAnalysis'],
        '_3969': ['RollingRingCompoundStabilityAnalysis'],
        '_3970': ['RollingRingConnectionCompoundStabilityAnalysis'],
        '_3971': ['RootAssemblyCompoundStabilityAnalysis'],
        '_3972': ['ShaftCompoundStabilityAnalysis'],
        '_3973': ['ShaftHubConnectionCompoundStabilityAnalysis'],
        '_3974': ['ShaftToMountableComponentConnectionCompoundStabilityAnalysis'],
        '_3975': ['SpecialisedAssemblyCompoundStabilityAnalysis'],
        '_3976': ['SpiralBevelGearCompoundStabilityAnalysis'],
        '_3977': ['SpiralBevelGearMeshCompoundStabilityAnalysis'],
        '_3978': ['SpiralBevelGearSetCompoundStabilityAnalysis'],
        '_3979': ['SpringDamperCompoundStabilityAnalysis'],
        '_3980': ['SpringDamperConnectionCompoundStabilityAnalysis'],
        '_3981': ['SpringDamperHalfCompoundStabilityAnalysis'],
        '_3982': ['StraightBevelDiffGearCompoundStabilityAnalysis'],
        '_3983': ['StraightBevelDiffGearMeshCompoundStabilityAnalysis'],
        '_3984': ['StraightBevelDiffGearSetCompoundStabilityAnalysis'],
        '_3985': ['StraightBevelGearCompoundStabilityAnalysis'],
        '_3986': ['StraightBevelGearMeshCompoundStabilityAnalysis'],
        '_3987': ['StraightBevelGearSetCompoundStabilityAnalysis'],
        '_3988': ['StraightBevelPlanetGearCompoundStabilityAnalysis'],
        '_3989': ['StraightBevelSunGearCompoundStabilityAnalysis'],
        '_3990': ['SynchroniserCompoundStabilityAnalysis'],
        '_3991': ['SynchroniserHalfCompoundStabilityAnalysis'],
        '_3992': ['SynchroniserPartCompoundStabilityAnalysis'],
        '_3993': ['SynchroniserSleeveCompoundStabilityAnalysis'],
        '_3994': ['TorqueConverterCompoundStabilityAnalysis'],
        '_3995': ['TorqueConverterConnectionCompoundStabilityAnalysis'],
        '_3996': ['TorqueConverterPumpCompoundStabilityAnalysis'],
        '_3997': ['TorqueConverterTurbineCompoundStabilityAnalysis'],
        '_3998': ['UnbalancedMassCompoundStabilityAnalysis'],
        '_3999': ['VirtualComponentCompoundStabilityAnalysis'],
        '_4000': ['WormGearCompoundStabilityAnalysis'],
        '_4001': ['WormGearMeshCompoundStabilityAnalysis'],
        '_4002': ['WormGearSetCompoundStabilityAnalysis'],
        '_4003': ['ZerolBevelGearCompoundStabilityAnalysis'],
        '_4004': ['ZerolBevelGearMeshCompoundStabilityAnalysis'],
        '_4005': ['ZerolBevelGearSetCompoundStabilityAnalysis'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
