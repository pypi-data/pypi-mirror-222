"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7107 import AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7108 import AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7109 import AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7110 import AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7111 import AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7112 import AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7113 import AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7114 import AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7115 import BearingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7116 import BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7117 import BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7118 import BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7119 import BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7120 import BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7121 import BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7122 import BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7123 import BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7124 import BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7125 import BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7126 import BoltCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7127 import BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7128 import ClutchCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7129 import ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7130 import ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7131 import CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7132 import ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7133 import ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7134 import ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7135 import ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7136 import ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7137 import ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7138 import ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7139 import ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7140 import ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7141 import ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7142 import ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7143 import ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7144 import CouplingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7145 import CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7146 import CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7147 import CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7148 import CVTCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7149 import CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7150 import CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7151 import CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7152 import CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7153 import CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7154 import CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7155 import CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7156 import CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7157 import CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7158 import DatumCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7159 import ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7160 import FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7161 import FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7162 import FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7163 import FEPartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7164 import FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7165 import GearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7166 import GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7167 import GearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7168 import GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7169 import HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7170 import HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7171 import HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7172 import InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7173 import KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7174 import KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7175 import KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7176 import KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7177 import KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7178 import KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7179 import KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7180 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7181 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7182 import MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7183 import MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7184 import MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7185 import OilSealCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7186 import PartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7187 import PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7188 import PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7189 import PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7190 import PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7191 import PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7192 import PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7193 import PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7194 import PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7195 import PulleyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7196 import RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7197 import RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7198 import RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7199 import RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7200 import RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7201 import RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7202 import ShaftCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7203 import ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7204 import ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7205 import SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7206 import SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7207 import SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7208 import SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7209 import SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7210 import SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7211 import SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7212 import StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7213 import StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7214 import StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7215 import StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7216 import StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7217 import StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7218 import StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7219 import StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7220 import SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7221 import SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7222 import SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7223 import SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7224 import TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7225 import TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7226 import TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7227 import TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7228 import UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7229 import VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7230 import WormGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7231 import WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7232 import WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7233 import ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7234 import ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7235 import ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
else:
    import_structure = {
        '_7107': ['AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7108': ['AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7109': ['AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7110': ['AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7111': ['AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7112': ['AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7113': ['AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7114': ['AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7115': ['BearingCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7116': ['BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7117': ['BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7118': ['BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7119': ['BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7120': ['BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7121': ['BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7122': ['BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7123': ['BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7124': ['BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7125': ['BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7126': ['BoltCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7127': ['BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7128': ['ClutchCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7129': ['ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7130': ['ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7131': ['CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7132': ['ComponentCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7133': ['ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7134': ['ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7135': ['ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7136': ['ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7137': ['ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7138': ['ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7139': ['ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7140': ['ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7141': ['ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7142': ['ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7143': ['ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7144': ['CouplingCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7145': ['CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7146': ['CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7147': ['CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7148': ['CVTCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7149': ['CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7150': ['CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7151': ['CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7152': ['CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7153': ['CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7154': ['CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7155': ['CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7156': ['CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7157': ['CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7158': ['DatumCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7159': ['ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7160': ['FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7161': ['FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7162': ['FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7163': ['FEPartCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7164': ['FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7165': ['GearCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7166': ['GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7167': ['GearSetCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7168': ['GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7169': ['HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7170': ['HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7171': ['HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7172': ['InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7173': ['KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7174': ['KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7175': ['KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7176': ['KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7177': ['KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7178': ['KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7179': ['KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7180': ['KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7181': ['KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7182': ['MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7183': ['MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7184': ['MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7185': ['OilSealCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7186': ['PartCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7187': ['PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7188': ['PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7189': ['PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7190': ['PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7191': ['PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7192': ['PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7193': ['PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7194': ['PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7195': ['PulleyCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7196': ['RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7197': ['RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7198': ['RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7199': ['RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7200': ['RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7201': ['RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7202': ['ShaftCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7203': ['ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7204': ['ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7205': ['SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7206': ['SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7207': ['SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7208': ['SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7209': ['SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7210': ['SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7211': ['SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7212': ['StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7213': ['StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7214': ['StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7215': ['StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7216': ['StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7217': ['StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7218': ['StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7219': ['StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7220': ['SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7221': ['SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7222': ['SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7223': ['SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7224': ['TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7225': ['TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7226': ['TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7227': ['TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7228': ['UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7229': ['VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7230': ['WormGearCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7231': ['WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7232': ['WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7233': ['ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7234': ['ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_7235': ['ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
