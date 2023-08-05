"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4145 import AbstractAssemblyCompoundPowerFlow
    from ._4146 import AbstractShaftCompoundPowerFlow
    from ._4147 import AbstractShaftOrHousingCompoundPowerFlow
    from ._4148 import AbstractShaftToMountableComponentConnectionCompoundPowerFlow
    from ._4149 import AGMAGleasonConicalGearCompoundPowerFlow
    from ._4150 import AGMAGleasonConicalGearMeshCompoundPowerFlow
    from ._4151 import AGMAGleasonConicalGearSetCompoundPowerFlow
    from ._4152 import AssemblyCompoundPowerFlow
    from ._4153 import BearingCompoundPowerFlow
    from ._4154 import BeltConnectionCompoundPowerFlow
    from ._4155 import BeltDriveCompoundPowerFlow
    from ._4156 import BevelDifferentialGearCompoundPowerFlow
    from ._4157 import BevelDifferentialGearMeshCompoundPowerFlow
    from ._4158 import BevelDifferentialGearSetCompoundPowerFlow
    from ._4159 import BevelDifferentialPlanetGearCompoundPowerFlow
    from ._4160 import BevelDifferentialSunGearCompoundPowerFlow
    from ._4161 import BevelGearCompoundPowerFlow
    from ._4162 import BevelGearMeshCompoundPowerFlow
    from ._4163 import BevelGearSetCompoundPowerFlow
    from ._4164 import BoltCompoundPowerFlow
    from ._4165 import BoltedJointCompoundPowerFlow
    from ._4166 import ClutchCompoundPowerFlow
    from ._4167 import ClutchConnectionCompoundPowerFlow
    from ._4168 import ClutchHalfCompoundPowerFlow
    from ._4169 import CoaxialConnectionCompoundPowerFlow
    from ._4170 import ComponentCompoundPowerFlow
    from ._4171 import ConceptCouplingCompoundPowerFlow
    from ._4172 import ConceptCouplingConnectionCompoundPowerFlow
    from ._4173 import ConceptCouplingHalfCompoundPowerFlow
    from ._4174 import ConceptGearCompoundPowerFlow
    from ._4175 import ConceptGearMeshCompoundPowerFlow
    from ._4176 import ConceptGearSetCompoundPowerFlow
    from ._4177 import ConicalGearCompoundPowerFlow
    from ._4178 import ConicalGearMeshCompoundPowerFlow
    from ._4179 import ConicalGearSetCompoundPowerFlow
    from ._4180 import ConnectionCompoundPowerFlow
    from ._4181 import ConnectorCompoundPowerFlow
    from ._4182 import CouplingCompoundPowerFlow
    from ._4183 import CouplingConnectionCompoundPowerFlow
    from ._4184 import CouplingHalfCompoundPowerFlow
    from ._4185 import CVTBeltConnectionCompoundPowerFlow
    from ._4186 import CVTCompoundPowerFlow
    from ._4187 import CVTPulleyCompoundPowerFlow
    from ._4188 import CycloidalAssemblyCompoundPowerFlow
    from ._4189 import CycloidalDiscCentralBearingConnectionCompoundPowerFlow
    from ._4190 import CycloidalDiscCompoundPowerFlow
    from ._4191 import CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow
    from ._4192 import CylindricalGearCompoundPowerFlow
    from ._4193 import CylindricalGearMeshCompoundPowerFlow
    from ._4194 import CylindricalGearSetCompoundPowerFlow
    from ._4195 import CylindricalPlanetGearCompoundPowerFlow
    from ._4196 import DatumCompoundPowerFlow
    from ._4197 import ExternalCADModelCompoundPowerFlow
    from ._4198 import FaceGearCompoundPowerFlow
    from ._4199 import FaceGearMeshCompoundPowerFlow
    from ._4200 import FaceGearSetCompoundPowerFlow
    from ._4201 import FEPartCompoundPowerFlow
    from ._4202 import FlexiblePinAssemblyCompoundPowerFlow
    from ._4203 import GearCompoundPowerFlow
    from ._4204 import GearMeshCompoundPowerFlow
    from ._4205 import GearSetCompoundPowerFlow
    from ._4206 import GuideDxfModelCompoundPowerFlow
    from ._4207 import HypoidGearCompoundPowerFlow
    from ._4208 import HypoidGearMeshCompoundPowerFlow
    from ._4209 import HypoidGearSetCompoundPowerFlow
    from ._4210 import InterMountableComponentConnectionCompoundPowerFlow
    from ._4211 import KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
    from ._4212 import KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow
    from ._4213 import KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
    from ._4214 import KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
    from ._4215 import KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow
    from ._4216 import KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
    from ._4217 import KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
    from ._4218 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow
    from ._4219 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
    from ._4220 import MassDiscCompoundPowerFlow
    from ._4221 import MeasurementComponentCompoundPowerFlow
    from ._4222 import MountableComponentCompoundPowerFlow
    from ._4223 import OilSealCompoundPowerFlow
    from ._4224 import PartCompoundPowerFlow
    from ._4225 import PartToPartShearCouplingCompoundPowerFlow
    from ._4226 import PartToPartShearCouplingConnectionCompoundPowerFlow
    from ._4227 import PartToPartShearCouplingHalfCompoundPowerFlow
    from ._4228 import PlanetaryConnectionCompoundPowerFlow
    from ._4229 import PlanetaryGearSetCompoundPowerFlow
    from ._4230 import PlanetCarrierCompoundPowerFlow
    from ._4231 import PointLoadCompoundPowerFlow
    from ._4232 import PowerLoadCompoundPowerFlow
    from ._4233 import PulleyCompoundPowerFlow
    from ._4234 import RingPinsCompoundPowerFlow
    from ._4235 import RingPinsToDiscConnectionCompoundPowerFlow
    from ._4236 import RollingRingAssemblyCompoundPowerFlow
    from ._4237 import RollingRingCompoundPowerFlow
    from ._4238 import RollingRingConnectionCompoundPowerFlow
    from ._4239 import RootAssemblyCompoundPowerFlow
    from ._4240 import ShaftCompoundPowerFlow
    from ._4241 import ShaftHubConnectionCompoundPowerFlow
    from ._4242 import ShaftToMountableComponentConnectionCompoundPowerFlow
    from ._4243 import SpecialisedAssemblyCompoundPowerFlow
    from ._4244 import SpiralBevelGearCompoundPowerFlow
    from ._4245 import SpiralBevelGearMeshCompoundPowerFlow
    from ._4246 import SpiralBevelGearSetCompoundPowerFlow
    from ._4247 import SpringDamperCompoundPowerFlow
    from ._4248 import SpringDamperConnectionCompoundPowerFlow
    from ._4249 import SpringDamperHalfCompoundPowerFlow
    from ._4250 import StraightBevelDiffGearCompoundPowerFlow
    from ._4251 import StraightBevelDiffGearMeshCompoundPowerFlow
    from ._4252 import StraightBevelDiffGearSetCompoundPowerFlow
    from ._4253 import StraightBevelGearCompoundPowerFlow
    from ._4254 import StraightBevelGearMeshCompoundPowerFlow
    from ._4255 import StraightBevelGearSetCompoundPowerFlow
    from ._4256 import StraightBevelPlanetGearCompoundPowerFlow
    from ._4257 import StraightBevelSunGearCompoundPowerFlow
    from ._4258 import SynchroniserCompoundPowerFlow
    from ._4259 import SynchroniserHalfCompoundPowerFlow
    from ._4260 import SynchroniserPartCompoundPowerFlow
    from ._4261 import SynchroniserSleeveCompoundPowerFlow
    from ._4262 import TorqueConverterCompoundPowerFlow
    from ._4263 import TorqueConverterConnectionCompoundPowerFlow
    from ._4264 import TorqueConverterPumpCompoundPowerFlow
    from ._4265 import TorqueConverterTurbineCompoundPowerFlow
    from ._4266 import UnbalancedMassCompoundPowerFlow
    from ._4267 import VirtualComponentCompoundPowerFlow
    from ._4268 import WormGearCompoundPowerFlow
    from ._4269 import WormGearMeshCompoundPowerFlow
    from ._4270 import WormGearSetCompoundPowerFlow
    from ._4271 import ZerolBevelGearCompoundPowerFlow
    from ._4272 import ZerolBevelGearMeshCompoundPowerFlow
    from ._4273 import ZerolBevelGearSetCompoundPowerFlow
else:
    import_structure = {
        '_4145': ['AbstractAssemblyCompoundPowerFlow'],
        '_4146': ['AbstractShaftCompoundPowerFlow'],
        '_4147': ['AbstractShaftOrHousingCompoundPowerFlow'],
        '_4148': ['AbstractShaftToMountableComponentConnectionCompoundPowerFlow'],
        '_4149': ['AGMAGleasonConicalGearCompoundPowerFlow'],
        '_4150': ['AGMAGleasonConicalGearMeshCompoundPowerFlow'],
        '_4151': ['AGMAGleasonConicalGearSetCompoundPowerFlow'],
        '_4152': ['AssemblyCompoundPowerFlow'],
        '_4153': ['BearingCompoundPowerFlow'],
        '_4154': ['BeltConnectionCompoundPowerFlow'],
        '_4155': ['BeltDriveCompoundPowerFlow'],
        '_4156': ['BevelDifferentialGearCompoundPowerFlow'],
        '_4157': ['BevelDifferentialGearMeshCompoundPowerFlow'],
        '_4158': ['BevelDifferentialGearSetCompoundPowerFlow'],
        '_4159': ['BevelDifferentialPlanetGearCompoundPowerFlow'],
        '_4160': ['BevelDifferentialSunGearCompoundPowerFlow'],
        '_4161': ['BevelGearCompoundPowerFlow'],
        '_4162': ['BevelGearMeshCompoundPowerFlow'],
        '_4163': ['BevelGearSetCompoundPowerFlow'],
        '_4164': ['BoltCompoundPowerFlow'],
        '_4165': ['BoltedJointCompoundPowerFlow'],
        '_4166': ['ClutchCompoundPowerFlow'],
        '_4167': ['ClutchConnectionCompoundPowerFlow'],
        '_4168': ['ClutchHalfCompoundPowerFlow'],
        '_4169': ['CoaxialConnectionCompoundPowerFlow'],
        '_4170': ['ComponentCompoundPowerFlow'],
        '_4171': ['ConceptCouplingCompoundPowerFlow'],
        '_4172': ['ConceptCouplingConnectionCompoundPowerFlow'],
        '_4173': ['ConceptCouplingHalfCompoundPowerFlow'],
        '_4174': ['ConceptGearCompoundPowerFlow'],
        '_4175': ['ConceptGearMeshCompoundPowerFlow'],
        '_4176': ['ConceptGearSetCompoundPowerFlow'],
        '_4177': ['ConicalGearCompoundPowerFlow'],
        '_4178': ['ConicalGearMeshCompoundPowerFlow'],
        '_4179': ['ConicalGearSetCompoundPowerFlow'],
        '_4180': ['ConnectionCompoundPowerFlow'],
        '_4181': ['ConnectorCompoundPowerFlow'],
        '_4182': ['CouplingCompoundPowerFlow'],
        '_4183': ['CouplingConnectionCompoundPowerFlow'],
        '_4184': ['CouplingHalfCompoundPowerFlow'],
        '_4185': ['CVTBeltConnectionCompoundPowerFlow'],
        '_4186': ['CVTCompoundPowerFlow'],
        '_4187': ['CVTPulleyCompoundPowerFlow'],
        '_4188': ['CycloidalAssemblyCompoundPowerFlow'],
        '_4189': ['CycloidalDiscCentralBearingConnectionCompoundPowerFlow'],
        '_4190': ['CycloidalDiscCompoundPowerFlow'],
        '_4191': ['CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow'],
        '_4192': ['CylindricalGearCompoundPowerFlow'],
        '_4193': ['CylindricalGearMeshCompoundPowerFlow'],
        '_4194': ['CylindricalGearSetCompoundPowerFlow'],
        '_4195': ['CylindricalPlanetGearCompoundPowerFlow'],
        '_4196': ['DatumCompoundPowerFlow'],
        '_4197': ['ExternalCADModelCompoundPowerFlow'],
        '_4198': ['FaceGearCompoundPowerFlow'],
        '_4199': ['FaceGearMeshCompoundPowerFlow'],
        '_4200': ['FaceGearSetCompoundPowerFlow'],
        '_4201': ['FEPartCompoundPowerFlow'],
        '_4202': ['FlexiblePinAssemblyCompoundPowerFlow'],
        '_4203': ['GearCompoundPowerFlow'],
        '_4204': ['GearMeshCompoundPowerFlow'],
        '_4205': ['GearSetCompoundPowerFlow'],
        '_4206': ['GuideDxfModelCompoundPowerFlow'],
        '_4207': ['HypoidGearCompoundPowerFlow'],
        '_4208': ['HypoidGearMeshCompoundPowerFlow'],
        '_4209': ['HypoidGearSetCompoundPowerFlow'],
        '_4210': ['InterMountableComponentConnectionCompoundPowerFlow'],
        '_4211': ['KlingelnbergCycloPalloidConicalGearCompoundPowerFlow'],
        '_4212': ['KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow'],
        '_4213': ['KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow'],
        '_4214': ['KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow'],
        '_4215': ['KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow'],
        '_4216': ['KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow'],
        '_4217': ['KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow'],
        '_4218': ['KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow'],
        '_4219': ['KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow'],
        '_4220': ['MassDiscCompoundPowerFlow'],
        '_4221': ['MeasurementComponentCompoundPowerFlow'],
        '_4222': ['MountableComponentCompoundPowerFlow'],
        '_4223': ['OilSealCompoundPowerFlow'],
        '_4224': ['PartCompoundPowerFlow'],
        '_4225': ['PartToPartShearCouplingCompoundPowerFlow'],
        '_4226': ['PartToPartShearCouplingConnectionCompoundPowerFlow'],
        '_4227': ['PartToPartShearCouplingHalfCompoundPowerFlow'],
        '_4228': ['PlanetaryConnectionCompoundPowerFlow'],
        '_4229': ['PlanetaryGearSetCompoundPowerFlow'],
        '_4230': ['PlanetCarrierCompoundPowerFlow'],
        '_4231': ['PointLoadCompoundPowerFlow'],
        '_4232': ['PowerLoadCompoundPowerFlow'],
        '_4233': ['PulleyCompoundPowerFlow'],
        '_4234': ['RingPinsCompoundPowerFlow'],
        '_4235': ['RingPinsToDiscConnectionCompoundPowerFlow'],
        '_4236': ['RollingRingAssemblyCompoundPowerFlow'],
        '_4237': ['RollingRingCompoundPowerFlow'],
        '_4238': ['RollingRingConnectionCompoundPowerFlow'],
        '_4239': ['RootAssemblyCompoundPowerFlow'],
        '_4240': ['ShaftCompoundPowerFlow'],
        '_4241': ['ShaftHubConnectionCompoundPowerFlow'],
        '_4242': ['ShaftToMountableComponentConnectionCompoundPowerFlow'],
        '_4243': ['SpecialisedAssemblyCompoundPowerFlow'],
        '_4244': ['SpiralBevelGearCompoundPowerFlow'],
        '_4245': ['SpiralBevelGearMeshCompoundPowerFlow'],
        '_4246': ['SpiralBevelGearSetCompoundPowerFlow'],
        '_4247': ['SpringDamperCompoundPowerFlow'],
        '_4248': ['SpringDamperConnectionCompoundPowerFlow'],
        '_4249': ['SpringDamperHalfCompoundPowerFlow'],
        '_4250': ['StraightBevelDiffGearCompoundPowerFlow'],
        '_4251': ['StraightBevelDiffGearMeshCompoundPowerFlow'],
        '_4252': ['StraightBevelDiffGearSetCompoundPowerFlow'],
        '_4253': ['StraightBevelGearCompoundPowerFlow'],
        '_4254': ['StraightBevelGearMeshCompoundPowerFlow'],
        '_4255': ['StraightBevelGearSetCompoundPowerFlow'],
        '_4256': ['StraightBevelPlanetGearCompoundPowerFlow'],
        '_4257': ['StraightBevelSunGearCompoundPowerFlow'],
        '_4258': ['SynchroniserCompoundPowerFlow'],
        '_4259': ['SynchroniserHalfCompoundPowerFlow'],
        '_4260': ['SynchroniserPartCompoundPowerFlow'],
        '_4261': ['SynchroniserSleeveCompoundPowerFlow'],
        '_4262': ['TorqueConverterCompoundPowerFlow'],
        '_4263': ['TorqueConverterConnectionCompoundPowerFlow'],
        '_4264': ['TorqueConverterPumpCompoundPowerFlow'],
        '_4265': ['TorqueConverterTurbineCompoundPowerFlow'],
        '_4266': ['UnbalancedMassCompoundPowerFlow'],
        '_4267': ['VirtualComponentCompoundPowerFlow'],
        '_4268': ['WormGearCompoundPowerFlow'],
        '_4269': ['WormGearMeshCompoundPowerFlow'],
        '_4270': ['WormGearSetCompoundPowerFlow'],
        '_4271': ['ZerolBevelGearCompoundPowerFlow'],
        '_4272': ['ZerolBevelGearMeshCompoundPowerFlow'],
        '_4273': ['ZerolBevelGearSetCompoundPowerFlow'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
