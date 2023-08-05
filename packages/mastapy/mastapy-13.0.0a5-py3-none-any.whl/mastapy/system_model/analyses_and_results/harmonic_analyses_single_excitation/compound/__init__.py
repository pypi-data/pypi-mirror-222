"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6108 import AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
    from ._6109 import AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation
    from ._6110 import AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation
    from ._6111 import AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
    from ._6112 import AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation
    from ._6113 import AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
    from ._6114 import AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
    from ._6115 import AssemblyCompoundHarmonicAnalysisOfSingleExcitation
    from ._6116 import BearingCompoundHarmonicAnalysisOfSingleExcitation
    from ._6117 import BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation
    from ._6118 import BeltDriveCompoundHarmonicAnalysisOfSingleExcitation
    from ._6119 import BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation
    from ._6120 import BevelDifferentialGearMeshCompoundHarmonicAnalysisOfSingleExcitation
    from ._6121 import BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation
    from ._6122 import BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
    from ._6123 import BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation
    from ._6124 import BevelGearCompoundHarmonicAnalysisOfSingleExcitation
    from ._6125 import BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
    from ._6126 import BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
    from ._6127 import BoltCompoundHarmonicAnalysisOfSingleExcitation
    from ._6128 import BoltedJointCompoundHarmonicAnalysisOfSingleExcitation
    from ._6129 import ClutchCompoundHarmonicAnalysisOfSingleExcitation
    from ._6130 import ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation
    from ._6131 import ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation
    from ._6132 import CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation
    from ._6133 import ComponentCompoundHarmonicAnalysisOfSingleExcitation
    from ._6134 import ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation
    from ._6135 import ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation
    from ._6136 import ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
    from ._6137 import ConceptGearCompoundHarmonicAnalysisOfSingleExcitation
    from ._6138 import ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation
    from ._6139 import ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation
    from ._6140 import ConicalGearCompoundHarmonicAnalysisOfSingleExcitation
    from ._6141 import ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
    from ._6142 import ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
    from ._6143 import ConnectionCompoundHarmonicAnalysisOfSingleExcitation
    from ._6144 import ConnectorCompoundHarmonicAnalysisOfSingleExcitation
    from ._6145 import CouplingCompoundHarmonicAnalysisOfSingleExcitation
    from ._6146 import CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation
    from ._6147 import CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
    from ._6148 import CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation
    from ._6149 import CVTCompoundHarmonicAnalysisOfSingleExcitation
    from ._6150 import CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation
    from ._6151 import CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation
    from ._6152 import CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation
    from ._6153 import CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation
    from ._6154 import CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation
    from ._6155 import CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation
    from ._6156 import CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
    from ._6157 import CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation
    from ._6158 import CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
    from ._6159 import DatumCompoundHarmonicAnalysisOfSingleExcitation
    from ._6160 import ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation
    from ._6161 import FaceGearCompoundHarmonicAnalysisOfSingleExcitation
    from ._6162 import FaceGearMeshCompoundHarmonicAnalysisOfSingleExcitation
    from ._6163 import FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation
    from ._6164 import FEPartCompoundHarmonicAnalysisOfSingleExcitation
    from ._6165 import FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation
    from ._6166 import GearCompoundHarmonicAnalysisOfSingleExcitation
    from ._6167 import GearMeshCompoundHarmonicAnalysisOfSingleExcitation
    from ._6168 import GearSetCompoundHarmonicAnalysisOfSingleExcitation
    from ._6169 import GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation
    from ._6170 import HypoidGearCompoundHarmonicAnalysisOfSingleExcitation
    from ._6171 import HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation
    from ._6172 import HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
    from ._6173 import InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
    from ._6174 import KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation
    from ._6175 import KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
    from ._6176 import KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
    from ._6177 import KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation
    from ._6178 import KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation
    from ._6179 import KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
    from ._6180 import KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
    from ._6181 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
    from ._6182 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
    from ._6183 import MassDiscCompoundHarmonicAnalysisOfSingleExcitation
    from ._6184 import MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation
    from ._6185 import MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
    from ._6186 import OilSealCompoundHarmonicAnalysisOfSingleExcitation
    from ._6187 import PartCompoundHarmonicAnalysisOfSingleExcitation
    from ._6188 import PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation
    from ._6189 import PartToPartShearCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation
    from ._6190 import PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
    from ._6191 import PlanetaryConnectionCompoundHarmonicAnalysisOfSingleExcitation
    from ._6192 import PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation
    from ._6193 import PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation
    from ._6194 import PointLoadCompoundHarmonicAnalysisOfSingleExcitation
    from ._6195 import PowerLoadCompoundHarmonicAnalysisOfSingleExcitation
    from ._6196 import PulleyCompoundHarmonicAnalysisOfSingleExcitation
    from ._6197 import RingPinsCompoundHarmonicAnalysisOfSingleExcitation
    from ._6198 import RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation
    from ._6199 import RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation
    from ._6200 import RollingRingCompoundHarmonicAnalysisOfSingleExcitation
    from ._6201 import RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation
    from ._6202 import RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation
    from ._6203 import ShaftCompoundHarmonicAnalysisOfSingleExcitation
    from ._6204 import ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation
    from ._6205 import ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
    from ._6206 import SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
    from ._6207 import SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
    from ._6208 import SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
    from ._6209 import SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
    from ._6210 import SpringDamperCompoundHarmonicAnalysisOfSingleExcitation
    from ._6211 import SpringDamperConnectionCompoundHarmonicAnalysisOfSingleExcitation
    from ._6212 import SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation
    from ._6213 import StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation
    from ._6214 import StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation
    from ._6215 import StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation
    from ._6216 import StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation
    from ._6217 import StraightBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
    from ._6218 import StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
    from ._6219 import StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
    from ._6220 import StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation
    from ._6221 import SynchroniserCompoundHarmonicAnalysisOfSingleExcitation
    from ._6222 import SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation
    from ._6223 import SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation
    from ._6224 import SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation
    from ._6225 import TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation
    from ._6226 import TorqueConverterConnectionCompoundHarmonicAnalysisOfSingleExcitation
    from ._6227 import TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation
    from ._6228 import TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation
    from ._6229 import UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation
    from ._6230 import VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation
    from ._6231 import WormGearCompoundHarmonicAnalysisOfSingleExcitation
    from ._6232 import WormGearMeshCompoundHarmonicAnalysisOfSingleExcitation
    from ._6233 import WormGearSetCompoundHarmonicAnalysisOfSingleExcitation
    from ._6234 import ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation
    from ._6235 import ZerolBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
    from ._6236 import ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
else:
    import_structure = {
        '_6108': ['AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6109': ['AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6110': ['AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6111': ['AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6112': ['AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6113': ['AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6114': ['AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6115': ['AssemblyCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6116': ['BearingCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6117': ['BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6118': ['BeltDriveCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6119': ['BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6120': ['BevelDifferentialGearMeshCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6121': ['BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6122': ['BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6123': ['BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6124': ['BevelGearCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6125': ['BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6126': ['BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6127': ['BoltCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6128': ['BoltedJointCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6129': ['ClutchCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6130': ['ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6131': ['ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6132': ['CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6133': ['ComponentCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6134': ['ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6135': ['ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6136': ['ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6137': ['ConceptGearCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6138': ['ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6139': ['ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6140': ['ConicalGearCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6141': ['ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6142': ['ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6143': ['ConnectionCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6144': ['ConnectorCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6145': ['CouplingCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6146': ['CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6147': ['CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6148': ['CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6149': ['CVTCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6150': ['CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6151': ['CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6152': ['CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6153': ['CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6154': ['CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6155': ['CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6156': ['CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6157': ['CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6158': ['CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6159': ['DatumCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6160': ['ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6161': ['FaceGearCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6162': ['FaceGearMeshCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6163': ['FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6164': ['FEPartCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6165': ['FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6166': ['GearCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6167': ['GearMeshCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6168': ['GearSetCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6169': ['GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6170': ['HypoidGearCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6171': ['HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6172': ['HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6173': ['InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6174': ['KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6175': ['KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6176': ['KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6177': ['KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6178': ['KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6179': ['KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6180': ['KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6181': ['KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6182': ['KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6183': ['MassDiscCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6184': ['MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6185': ['MountableComponentCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6186': ['OilSealCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6187': ['PartCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6188': ['PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6189': ['PartToPartShearCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6190': ['PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6191': ['PlanetaryConnectionCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6192': ['PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6193': ['PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6194': ['PointLoadCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6195': ['PowerLoadCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6196': ['PulleyCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6197': ['RingPinsCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6198': ['RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6199': ['RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6200': ['RollingRingCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6201': ['RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6202': ['RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6203': ['ShaftCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6204': ['ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6205': ['ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6206': ['SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6207': ['SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6208': ['SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6209': ['SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6210': ['SpringDamperCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6211': ['SpringDamperConnectionCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6212': ['SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6213': ['StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6214': ['StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6215': ['StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6216': ['StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6217': ['StraightBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6218': ['StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6219': ['StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6220': ['StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6221': ['SynchroniserCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6222': ['SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6223': ['SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6224': ['SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6225': ['TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6226': ['TorqueConverterConnectionCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6227': ['TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6228': ['TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6229': ['UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6230': ['VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6231': ['WormGearCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6232': ['WormGearMeshCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6233': ['WormGearSetCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6234': ['ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6235': ['ZerolBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation'],
        '_6236': ['ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
