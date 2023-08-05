"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4012 import AbstractAssemblyPowerFlow
    from ._4013 import AbstractShaftOrHousingPowerFlow
    from ._4014 import AbstractShaftPowerFlow
    from ._4015 import AbstractShaftToMountableComponentConnectionPowerFlow
    from ._4016 import AGMAGleasonConicalGearMeshPowerFlow
    from ._4017 import AGMAGleasonConicalGearPowerFlow
    from ._4018 import AGMAGleasonConicalGearSetPowerFlow
    from ._4019 import AssemblyPowerFlow
    from ._4020 import BearingPowerFlow
    from ._4021 import BeltConnectionPowerFlow
    from ._4022 import BeltDrivePowerFlow
    from ._4023 import BevelDifferentialGearMeshPowerFlow
    from ._4024 import BevelDifferentialGearPowerFlow
    from ._4025 import BevelDifferentialGearSetPowerFlow
    from ._4026 import BevelDifferentialPlanetGearPowerFlow
    from ._4027 import BevelDifferentialSunGearPowerFlow
    from ._4028 import BevelGearMeshPowerFlow
    from ._4029 import BevelGearPowerFlow
    from ._4030 import BevelGearSetPowerFlow
    from ._4031 import BoltedJointPowerFlow
    from ._4032 import BoltPowerFlow
    from ._4033 import ClutchConnectionPowerFlow
    from ._4034 import ClutchHalfPowerFlow
    from ._4035 import ClutchPowerFlow
    from ._4036 import CoaxialConnectionPowerFlow
    from ._4037 import ComponentPowerFlow
    from ._4038 import ConceptCouplingConnectionPowerFlow
    from ._4039 import ConceptCouplingHalfPowerFlow
    from ._4040 import ConceptCouplingPowerFlow
    from ._4041 import ConceptGearMeshPowerFlow
    from ._4042 import ConceptGearPowerFlow
    from ._4043 import ConceptGearSetPowerFlow
    from ._4044 import ConicalGearMeshPowerFlow
    from ._4045 import ConicalGearPowerFlow
    from ._4046 import ConicalGearSetPowerFlow
    from ._4047 import ConnectionPowerFlow
    from ._4048 import ConnectorPowerFlow
    from ._4049 import CouplingConnectionPowerFlow
    from ._4050 import CouplingHalfPowerFlow
    from ._4051 import CouplingPowerFlow
    from ._4052 import CVTBeltConnectionPowerFlow
    from ._4053 import CVTPowerFlow
    from ._4054 import CVTPulleyPowerFlow
    from ._4055 import CycloidalAssemblyPowerFlow
    from ._4056 import CycloidalDiscCentralBearingConnectionPowerFlow
    from ._4057 import CycloidalDiscPlanetaryBearingConnectionPowerFlow
    from ._4058 import CycloidalDiscPowerFlow
    from ._4059 import CylindricalGearGeometricEntityDrawStyle
    from ._4060 import CylindricalGearMeshPowerFlow
    from ._4061 import CylindricalGearPowerFlow
    from ._4062 import CylindricalGearSetPowerFlow
    from ._4063 import CylindricalPlanetGearPowerFlow
    from ._4064 import DatumPowerFlow
    from ._4065 import ExternalCADModelPowerFlow
    from ._4066 import FaceGearMeshPowerFlow
    from ._4067 import FaceGearPowerFlow
    from ._4068 import FaceGearSetPowerFlow
    from ._4069 import FEPartPowerFlow
    from ._4070 import FlexiblePinAssemblyPowerFlow
    from ._4071 import GearMeshPowerFlow
    from ._4072 import GearPowerFlow
    from ._4073 import GearSetPowerFlow
    from ._4074 import GuideDxfModelPowerFlow
    from ._4075 import HypoidGearMeshPowerFlow
    from ._4076 import HypoidGearPowerFlow
    from ._4077 import HypoidGearSetPowerFlow
    from ._4078 import InterMountableComponentConnectionPowerFlow
    from ._4079 import KlingelnbergCycloPalloidConicalGearMeshPowerFlow
    from ._4080 import KlingelnbergCycloPalloidConicalGearPowerFlow
    from ._4081 import KlingelnbergCycloPalloidConicalGearSetPowerFlow
    from ._4082 import KlingelnbergCycloPalloidHypoidGearMeshPowerFlow
    from ._4083 import KlingelnbergCycloPalloidHypoidGearPowerFlow
    from ._4084 import KlingelnbergCycloPalloidHypoidGearSetPowerFlow
    from ._4085 import KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow
    from ._4086 import KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
    from ._4087 import KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
    from ._4088 import MassDiscPowerFlow
    from ._4089 import MeasurementComponentPowerFlow
    from ._4090 import MountableComponentPowerFlow
    from ._4091 import OilSealPowerFlow
    from ._4092 import PartPowerFlow
    from ._4093 import PartToPartShearCouplingConnectionPowerFlow
    from ._4094 import PartToPartShearCouplingHalfPowerFlow
    from ._4095 import PartToPartShearCouplingPowerFlow
    from ._4096 import PlanetaryConnectionPowerFlow
    from ._4097 import PlanetaryGearSetPowerFlow
    from ._4098 import PlanetCarrierPowerFlow
    from ._4099 import PointLoadPowerFlow
    from ._4100 import PowerFlow
    from ._4101 import PowerFlowDrawStyle
    from ._4102 import PowerLoadPowerFlow
    from ._4103 import PulleyPowerFlow
    from ._4104 import RingPinsPowerFlow
    from ._4105 import RingPinsToDiscConnectionPowerFlow
    from ._4106 import RollingRingAssemblyPowerFlow
    from ._4107 import RollingRingConnectionPowerFlow
    from ._4108 import RollingRingPowerFlow
    from ._4109 import RootAssemblyPowerFlow
    from ._4110 import ShaftHubConnectionPowerFlow
    from ._4111 import ShaftPowerFlow
    from ._4112 import ShaftToMountableComponentConnectionPowerFlow
    from ._4113 import SpecialisedAssemblyPowerFlow
    from ._4114 import SpiralBevelGearMeshPowerFlow
    from ._4115 import SpiralBevelGearPowerFlow
    from ._4116 import SpiralBevelGearSetPowerFlow
    from ._4117 import SpringDamperConnectionPowerFlow
    from ._4118 import SpringDamperHalfPowerFlow
    from ._4119 import SpringDamperPowerFlow
    from ._4120 import StraightBevelDiffGearMeshPowerFlow
    from ._4121 import StraightBevelDiffGearPowerFlow
    from ._4122 import StraightBevelDiffGearSetPowerFlow
    from ._4123 import StraightBevelGearMeshPowerFlow
    from ._4124 import StraightBevelGearPowerFlow
    from ._4125 import StraightBevelGearSetPowerFlow
    from ._4126 import StraightBevelPlanetGearPowerFlow
    from ._4127 import StraightBevelSunGearPowerFlow
    from ._4128 import SynchroniserHalfPowerFlow
    from ._4129 import SynchroniserPartPowerFlow
    from ._4130 import SynchroniserPowerFlow
    from ._4131 import SynchroniserSleevePowerFlow
    from ._4132 import ToothPassingHarmonic
    from ._4133 import TorqueConverterConnectionPowerFlow
    from ._4134 import TorqueConverterPowerFlow
    from ._4135 import TorqueConverterPumpPowerFlow
    from ._4136 import TorqueConverterTurbinePowerFlow
    from ._4137 import UnbalancedMassPowerFlow
    from ._4138 import VirtualComponentPowerFlow
    from ._4139 import WormGearMeshPowerFlow
    from ._4140 import WormGearPowerFlow
    from ._4141 import WormGearSetPowerFlow
    from ._4142 import ZerolBevelGearMeshPowerFlow
    from ._4143 import ZerolBevelGearPowerFlow
    from ._4144 import ZerolBevelGearSetPowerFlow
else:
    import_structure = {
        '_4012': ['AbstractAssemblyPowerFlow'],
        '_4013': ['AbstractShaftOrHousingPowerFlow'],
        '_4014': ['AbstractShaftPowerFlow'],
        '_4015': ['AbstractShaftToMountableComponentConnectionPowerFlow'],
        '_4016': ['AGMAGleasonConicalGearMeshPowerFlow'],
        '_4017': ['AGMAGleasonConicalGearPowerFlow'],
        '_4018': ['AGMAGleasonConicalGearSetPowerFlow'],
        '_4019': ['AssemblyPowerFlow'],
        '_4020': ['BearingPowerFlow'],
        '_4021': ['BeltConnectionPowerFlow'],
        '_4022': ['BeltDrivePowerFlow'],
        '_4023': ['BevelDifferentialGearMeshPowerFlow'],
        '_4024': ['BevelDifferentialGearPowerFlow'],
        '_4025': ['BevelDifferentialGearSetPowerFlow'],
        '_4026': ['BevelDifferentialPlanetGearPowerFlow'],
        '_4027': ['BevelDifferentialSunGearPowerFlow'],
        '_4028': ['BevelGearMeshPowerFlow'],
        '_4029': ['BevelGearPowerFlow'],
        '_4030': ['BevelGearSetPowerFlow'],
        '_4031': ['BoltedJointPowerFlow'],
        '_4032': ['BoltPowerFlow'],
        '_4033': ['ClutchConnectionPowerFlow'],
        '_4034': ['ClutchHalfPowerFlow'],
        '_4035': ['ClutchPowerFlow'],
        '_4036': ['CoaxialConnectionPowerFlow'],
        '_4037': ['ComponentPowerFlow'],
        '_4038': ['ConceptCouplingConnectionPowerFlow'],
        '_4039': ['ConceptCouplingHalfPowerFlow'],
        '_4040': ['ConceptCouplingPowerFlow'],
        '_4041': ['ConceptGearMeshPowerFlow'],
        '_4042': ['ConceptGearPowerFlow'],
        '_4043': ['ConceptGearSetPowerFlow'],
        '_4044': ['ConicalGearMeshPowerFlow'],
        '_4045': ['ConicalGearPowerFlow'],
        '_4046': ['ConicalGearSetPowerFlow'],
        '_4047': ['ConnectionPowerFlow'],
        '_4048': ['ConnectorPowerFlow'],
        '_4049': ['CouplingConnectionPowerFlow'],
        '_4050': ['CouplingHalfPowerFlow'],
        '_4051': ['CouplingPowerFlow'],
        '_4052': ['CVTBeltConnectionPowerFlow'],
        '_4053': ['CVTPowerFlow'],
        '_4054': ['CVTPulleyPowerFlow'],
        '_4055': ['CycloidalAssemblyPowerFlow'],
        '_4056': ['CycloidalDiscCentralBearingConnectionPowerFlow'],
        '_4057': ['CycloidalDiscPlanetaryBearingConnectionPowerFlow'],
        '_4058': ['CycloidalDiscPowerFlow'],
        '_4059': ['CylindricalGearGeometricEntityDrawStyle'],
        '_4060': ['CylindricalGearMeshPowerFlow'],
        '_4061': ['CylindricalGearPowerFlow'],
        '_4062': ['CylindricalGearSetPowerFlow'],
        '_4063': ['CylindricalPlanetGearPowerFlow'],
        '_4064': ['DatumPowerFlow'],
        '_4065': ['ExternalCADModelPowerFlow'],
        '_4066': ['FaceGearMeshPowerFlow'],
        '_4067': ['FaceGearPowerFlow'],
        '_4068': ['FaceGearSetPowerFlow'],
        '_4069': ['FEPartPowerFlow'],
        '_4070': ['FlexiblePinAssemblyPowerFlow'],
        '_4071': ['GearMeshPowerFlow'],
        '_4072': ['GearPowerFlow'],
        '_4073': ['GearSetPowerFlow'],
        '_4074': ['GuideDxfModelPowerFlow'],
        '_4075': ['HypoidGearMeshPowerFlow'],
        '_4076': ['HypoidGearPowerFlow'],
        '_4077': ['HypoidGearSetPowerFlow'],
        '_4078': ['InterMountableComponentConnectionPowerFlow'],
        '_4079': ['KlingelnbergCycloPalloidConicalGearMeshPowerFlow'],
        '_4080': ['KlingelnbergCycloPalloidConicalGearPowerFlow'],
        '_4081': ['KlingelnbergCycloPalloidConicalGearSetPowerFlow'],
        '_4082': ['KlingelnbergCycloPalloidHypoidGearMeshPowerFlow'],
        '_4083': ['KlingelnbergCycloPalloidHypoidGearPowerFlow'],
        '_4084': ['KlingelnbergCycloPalloidHypoidGearSetPowerFlow'],
        '_4085': ['KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow'],
        '_4086': ['KlingelnbergCycloPalloidSpiralBevelGearPowerFlow'],
        '_4087': ['KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow'],
        '_4088': ['MassDiscPowerFlow'],
        '_4089': ['MeasurementComponentPowerFlow'],
        '_4090': ['MountableComponentPowerFlow'],
        '_4091': ['OilSealPowerFlow'],
        '_4092': ['PartPowerFlow'],
        '_4093': ['PartToPartShearCouplingConnectionPowerFlow'],
        '_4094': ['PartToPartShearCouplingHalfPowerFlow'],
        '_4095': ['PartToPartShearCouplingPowerFlow'],
        '_4096': ['PlanetaryConnectionPowerFlow'],
        '_4097': ['PlanetaryGearSetPowerFlow'],
        '_4098': ['PlanetCarrierPowerFlow'],
        '_4099': ['PointLoadPowerFlow'],
        '_4100': ['PowerFlow'],
        '_4101': ['PowerFlowDrawStyle'],
        '_4102': ['PowerLoadPowerFlow'],
        '_4103': ['PulleyPowerFlow'],
        '_4104': ['RingPinsPowerFlow'],
        '_4105': ['RingPinsToDiscConnectionPowerFlow'],
        '_4106': ['RollingRingAssemblyPowerFlow'],
        '_4107': ['RollingRingConnectionPowerFlow'],
        '_4108': ['RollingRingPowerFlow'],
        '_4109': ['RootAssemblyPowerFlow'],
        '_4110': ['ShaftHubConnectionPowerFlow'],
        '_4111': ['ShaftPowerFlow'],
        '_4112': ['ShaftToMountableComponentConnectionPowerFlow'],
        '_4113': ['SpecialisedAssemblyPowerFlow'],
        '_4114': ['SpiralBevelGearMeshPowerFlow'],
        '_4115': ['SpiralBevelGearPowerFlow'],
        '_4116': ['SpiralBevelGearSetPowerFlow'],
        '_4117': ['SpringDamperConnectionPowerFlow'],
        '_4118': ['SpringDamperHalfPowerFlow'],
        '_4119': ['SpringDamperPowerFlow'],
        '_4120': ['StraightBevelDiffGearMeshPowerFlow'],
        '_4121': ['StraightBevelDiffGearPowerFlow'],
        '_4122': ['StraightBevelDiffGearSetPowerFlow'],
        '_4123': ['StraightBevelGearMeshPowerFlow'],
        '_4124': ['StraightBevelGearPowerFlow'],
        '_4125': ['StraightBevelGearSetPowerFlow'],
        '_4126': ['StraightBevelPlanetGearPowerFlow'],
        '_4127': ['StraightBevelSunGearPowerFlow'],
        '_4128': ['SynchroniserHalfPowerFlow'],
        '_4129': ['SynchroniserPartPowerFlow'],
        '_4130': ['SynchroniserPowerFlow'],
        '_4131': ['SynchroniserSleevePowerFlow'],
        '_4132': ['ToothPassingHarmonic'],
        '_4133': ['TorqueConverterConnectionPowerFlow'],
        '_4134': ['TorqueConverterPowerFlow'],
        '_4135': ['TorqueConverterPumpPowerFlow'],
        '_4136': ['TorqueConverterTurbinePowerFlow'],
        '_4137': ['UnbalancedMassPowerFlow'],
        '_4138': ['VirtualComponentPowerFlow'],
        '_4139': ['WormGearMeshPowerFlow'],
        '_4140': ['WormGearPowerFlow'],
        '_4141': ['WormGearSetPowerFlow'],
        '_4142': ['ZerolBevelGearMeshPowerFlow'],
        '_4143': ['ZerolBevelGearPowerFlow'],
        '_4144': ['ZerolBevelGearSetPowerFlow'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
