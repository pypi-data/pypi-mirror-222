"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5092 import AbstractAssemblyModalAnalysisAtASpeed
    from ._5093 import AbstractShaftModalAnalysisAtASpeed
    from ._5094 import AbstractShaftOrHousingModalAnalysisAtASpeed
    from ._5095 import AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed
    from ._5096 import AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
    from ._5097 import AGMAGleasonConicalGearModalAnalysisAtASpeed
    from ._5098 import AGMAGleasonConicalGearSetModalAnalysisAtASpeed
    from ._5099 import AssemblyModalAnalysisAtASpeed
    from ._5100 import BearingModalAnalysisAtASpeed
    from ._5101 import BeltConnectionModalAnalysisAtASpeed
    from ._5102 import BeltDriveModalAnalysisAtASpeed
    from ._5103 import BevelDifferentialGearMeshModalAnalysisAtASpeed
    from ._5104 import BevelDifferentialGearModalAnalysisAtASpeed
    from ._5105 import BevelDifferentialGearSetModalAnalysisAtASpeed
    from ._5106 import BevelDifferentialPlanetGearModalAnalysisAtASpeed
    from ._5107 import BevelDifferentialSunGearModalAnalysisAtASpeed
    from ._5108 import BevelGearMeshModalAnalysisAtASpeed
    from ._5109 import BevelGearModalAnalysisAtASpeed
    from ._5110 import BevelGearSetModalAnalysisAtASpeed
    from ._5111 import BoltedJointModalAnalysisAtASpeed
    from ._5112 import BoltModalAnalysisAtASpeed
    from ._5113 import ClutchConnectionModalAnalysisAtASpeed
    from ._5114 import ClutchHalfModalAnalysisAtASpeed
    from ._5115 import ClutchModalAnalysisAtASpeed
    from ._5116 import CoaxialConnectionModalAnalysisAtASpeed
    from ._5117 import ComponentModalAnalysisAtASpeed
    from ._5118 import ConceptCouplingConnectionModalAnalysisAtASpeed
    from ._5119 import ConceptCouplingHalfModalAnalysisAtASpeed
    from ._5120 import ConceptCouplingModalAnalysisAtASpeed
    from ._5121 import ConceptGearMeshModalAnalysisAtASpeed
    from ._5122 import ConceptGearModalAnalysisAtASpeed
    from ._5123 import ConceptGearSetModalAnalysisAtASpeed
    from ._5124 import ConicalGearMeshModalAnalysisAtASpeed
    from ._5125 import ConicalGearModalAnalysisAtASpeed
    from ._5126 import ConicalGearSetModalAnalysisAtASpeed
    from ._5127 import ConnectionModalAnalysisAtASpeed
    from ._5128 import ConnectorModalAnalysisAtASpeed
    from ._5129 import CouplingConnectionModalAnalysisAtASpeed
    from ._5130 import CouplingHalfModalAnalysisAtASpeed
    from ._5131 import CouplingModalAnalysisAtASpeed
    from ._5132 import CVTBeltConnectionModalAnalysisAtASpeed
    from ._5133 import CVTModalAnalysisAtASpeed
    from ._5134 import CVTPulleyModalAnalysisAtASpeed
    from ._5135 import CycloidalAssemblyModalAnalysisAtASpeed
    from ._5136 import CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed
    from ._5137 import CycloidalDiscModalAnalysisAtASpeed
    from ._5138 import CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed
    from ._5139 import CylindricalGearMeshModalAnalysisAtASpeed
    from ._5140 import CylindricalGearModalAnalysisAtASpeed
    from ._5141 import CylindricalGearSetModalAnalysisAtASpeed
    from ._5142 import CylindricalPlanetGearModalAnalysisAtASpeed
    from ._5143 import DatumModalAnalysisAtASpeed
    from ._5144 import ExternalCADModelModalAnalysisAtASpeed
    from ._5145 import FaceGearMeshModalAnalysisAtASpeed
    from ._5146 import FaceGearModalAnalysisAtASpeed
    from ._5147 import FaceGearSetModalAnalysisAtASpeed
    from ._5148 import FEPartModalAnalysisAtASpeed
    from ._5149 import FlexiblePinAssemblyModalAnalysisAtASpeed
    from ._5150 import GearMeshModalAnalysisAtASpeed
    from ._5151 import GearModalAnalysisAtASpeed
    from ._5152 import GearSetModalAnalysisAtASpeed
    from ._5153 import GuideDxfModelModalAnalysisAtASpeed
    from ._5154 import HypoidGearMeshModalAnalysisAtASpeed
    from ._5155 import HypoidGearModalAnalysisAtASpeed
    from ._5156 import HypoidGearSetModalAnalysisAtASpeed
    from ._5157 import InterMountableComponentConnectionModalAnalysisAtASpeed
    from ._5158 import KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
    from ._5159 import KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed
    from ._5160 import KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed
    from ._5161 import KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed
    from ._5162 import KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed
    from ._5163 import KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed
    from ._5164 import KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed
    from ._5165 import KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed
    from ._5166 import KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed
    from ._5167 import MassDiscModalAnalysisAtASpeed
    from ._5168 import MeasurementComponentModalAnalysisAtASpeed
    from ._2618 import ModalAnalysisAtASpeed
    from ._5169 import MountableComponentModalAnalysisAtASpeed
    from ._5170 import OilSealModalAnalysisAtASpeed
    from ._5171 import PartModalAnalysisAtASpeed
    from ._5172 import PartToPartShearCouplingConnectionModalAnalysisAtASpeed
    from ._5173 import PartToPartShearCouplingHalfModalAnalysisAtASpeed
    from ._5174 import PartToPartShearCouplingModalAnalysisAtASpeed
    from ._5175 import PlanetaryConnectionModalAnalysisAtASpeed
    from ._5176 import PlanetaryGearSetModalAnalysisAtASpeed
    from ._5177 import PlanetCarrierModalAnalysisAtASpeed
    from ._5178 import PointLoadModalAnalysisAtASpeed
    from ._5179 import PowerLoadModalAnalysisAtASpeed
    from ._5180 import PulleyModalAnalysisAtASpeed
    from ._5181 import RingPinsModalAnalysisAtASpeed
    from ._5182 import RingPinsToDiscConnectionModalAnalysisAtASpeed
    from ._5183 import RollingRingAssemblyModalAnalysisAtASpeed
    from ._5184 import RollingRingConnectionModalAnalysisAtASpeed
    from ._5185 import RollingRingModalAnalysisAtASpeed
    from ._5186 import RootAssemblyModalAnalysisAtASpeed
    from ._5187 import ShaftHubConnectionModalAnalysisAtASpeed
    from ._5188 import ShaftModalAnalysisAtASpeed
    from ._5189 import ShaftToMountableComponentConnectionModalAnalysisAtASpeed
    from ._5190 import SpecialisedAssemblyModalAnalysisAtASpeed
    from ._5191 import SpiralBevelGearMeshModalAnalysisAtASpeed
    from ._5192 import SpiralBevelGearModalAnalysisAtASpeed
    from ._5193 import SpiralBevelGearSetModalAnalysisAtASpeed
    from ._5194 import SpringDamperConnectionModalAnalysisAtASpeed
    from ._5195 import SpringDamperHalfModalAnalysisAtASpeed
    from ._5196 import SpringDamperModalAnalysisAtASpeed
    from ._5197 import StraightBevelDiffGearMeshModalAnalysisAtASpeed
    from ._5198 import StraightBevelDiffGearModalAnalysisAtASpeed
    from ._5199 import StraightBevelDiffGearSetModalAnalysisAtASpeed
    from ._5200 import StraightBevelGearMeshModalAnalysisAtASpeed
    from ._5201 import StraightBevelGearModalAnalysisAtASpeed
    from ._5202 import StraightBevelGearSetModalAnalysisAtASpeed
    from ._5203 import StraightBevelPlanetGearModalAnalysisAtASpeed
    from ._5204 import StraightBevelSunGearModalAnalysisAtASpeed
    from ._5205 import SynchroniserHalfModalAnalysisAtASpeed
    from ._5206 import SynchroniserModalAnalysisAtASpeed
    from ._5207 import SynchroniserPartModalAnalysisAtASpeed
    from ._5208 import SynchroniserSleeveModalAnalysisAtASpeed
    from ._5209 import TorqueConverterConnectionModalAnalysisAtASpeed
    from ._5210 import TorqueConverterModalAnalysisAtASpeed
    from ._5211 import TorqueConverterPumpModalAnalysisAtASpeed
    from ._5212 import TorqueConverterTurbineModalAnalysisAtASpeed
    from ._5213 import UnbalancedMassModalAnalysisAtASpeed
    from ._5214 import VirtualComponentModalAnalysisAtASpeed
    from ._5215 import WormGearMeshModalAnalysisAtASpeed
    from ._5216 import WormGearModalAnalysisAtASpeed
    from ._5217 import WormGearSetModalAnalysisAtASpeed
    from ._5218 import ZerolBevelGearMeshModalAnalysisAtASpeed
    from ._5219 import ZerolBevelGearModalAnalysisAtASpeed
    from ._5220 import ZerolBevelGearSetModalAnalysisAtASpeed
else:
    import_structure = {
        '_5092': ['AbstractAssemblyModalAnalysisAtASpeed'],
        '_5093': ['AbstractShaftModalAnalysisAtASpeed'],
        '_5094': ['AbstractShaftOrHousingModalAnalysisAtASpeed'],
        '_5095': ['AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed'],
        '_5096': ['AGMAGleasonConicalGearMeshModalAnalysisAtASpeed'],
        '_5097': ['AGMAGleasonConicalGearModalAnalysisAtASpeed'],
        '_5098': ['AGMAGleasonConicalGearSetModalAnalysisAtASpeed'],
        '_5099': ['AssemblyModalAnalysisAtASpeed'],
        '_5100': ['BearingModalAnalysisAtASpeed'],
        '_5101': ['BeltConnectionModalAnalysisAtASpeed'],
        '_5102': ['BeltDriveModalAnalysisAtASpeed'],
        '_5103': ['BevelDifferentialGearMeshModalAnalysisAtASpeed'],
        '_5104': ['BevelDifferentialGearModalAnalysisAtASpeed'],
        '_5105': ['BevelDifferentialGearSetModalAnalysisAtASpeed'],
        '_5106': ['BevelDifferentialPlanetGearModalAnalysisAtASpeed'],
        '_5107': ['BevelDifferentialSunGearModalAnalysisAtASpeed'],
        '_5108': ['BevelGearMeshModalAnalysisAtASpeed'],
        '_5109': ['BevelGearModalAnalysisAtASpeed'],
        '_5110': ['BevelGearSetModalAnalysisAtASpeed'],
        '_5111': ['BoltedJointModalAnalysisAtASpeed'],
        '_5112': ['BoltModalAnalysisAtASpeed'],
        '_5113': ['ClutchConnectionModalAnalysisAtASpeed'],
        '_5114': ['ClutchHalfModalAnalysisAtASpeed'],
        '_5115': ['ClutchModalAnalysisAtASpeed'],
        '_5116': ['CoaxialConnectionModalAnalysisAtASpeed'],
        '_5117': ['ComponentModalAnalysisAtASpeed'],
        '_5118': ['ConceptCouplingConnectionModalAnalysisAtASpeed'],
        '_5119': ['ConceptCouplingHalfModalAnalysisAtASpeed'],
        '_5120': ['ConceptCouplingModalAnalysisAtASpeed'],
        '_5121': ['ConceptGearMeshModalAnalysisAtASpeed'],
        '_5122': ['ConceptGearModalAnalysisAtASpeed'],
        '_5123': ['ConceptGearSetModalAnalysisAtASpeed'],
        '_5124': ['ConicalGearMeshModalAnalysisAtASpeed'],
        '_5125': ['ConicalGearModalAnalysisAtASpeed'],
        '_5126': ['ConicalGearSetModalAnalysisAtASpeed'],
        '_5127': ['ConnectionModalAnalysisAtASpeed'],
        '_5128': ['ConnectorModalAnalysisAtASpeed'],
        '_5129': ['CouplingConnectionModalAnalysisAtASpeed'],
        '_5130': ['CouplingHalfModalAnalysisAtASpeed'],
        '_5131': ['CouplingModalAnalysisAtASpeed'],
        '_5132': ['CVTBeltConnectionModalAnalysisAtASpeed'],
        '_5133': ['CVTModalAnalysisAtASpeed'],
        '_5134': ['CVTPulleyModalAnalysisAtASpeed'],
        '_5135': ['CycloidalAssemblyModalAnalysisAtASpeed'],
        '_5136': ['CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed'],
        '_5137': ['CycloidalDiscModalAnalysisAtASpeed'],
        '_5138': ['CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed'],
        '_5139': ['CylindricalGearMeshModalAnalysisAtASpeed'],
        '_5140': ['CylindricalGearModalAnalysisAtASpeed'],
        '_5141': ['CylindricalGearSetModalAnalysisAtASpeed'],
        '_5142': ['CylindricalPlanetGearModalAnalysisAtASpeed'],
        '_5143': ['DatumModalAnalysisAtASpeed'],
        '_5144': ['ExternalCADModelModalAnalysisAtASpeed'],
        '_5145': ['FaceGearMeshModalAnalysisAtASpeed'],
        '_5146': ['FaceGearModalAnalysisAtASpeed'],
        '_5147': ['FaceGearSetModalAnalysisAtASpeed'],
        '_5148': ['FEPartModalAnalysisAtASpeed'],
        '_5149': ['FlexiblePinAssemblyModalAnalysisAtASpeed'],
        '_5150': ['GearMeshModalAnalysisAtASpeed'],
        '_5151': ['GearModalAnalysisAtASpeed'],
        '_5152': ['GearSetModalAnalysisAtASpeed'],
        '_5153': ['GuideDxfModelModalAnalysisAtASpeed'],
        '_5154': ['HypoidGearMeshModalAnalysisAtASpeed'],
        '_5155': ['HypoidGearModalAnalysisAtASpeed'],
        '_5156': ['HypoidGearSetModalAnalysisAtASpeed'],
        '_5157': ['InterMountableComponentConnectionModalAnalysisAtASpeed'],
        '_5158': ['KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed'],
        '_5159': ['KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed'],
        '_5160': ['KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed'],
        '_5161': ['KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed'],
        '_5162': ['KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed'],
        '_5163': ['KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed'],
        '_5164': ['KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed'],
        '_5165': ['KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed'],
        '_5166': ['KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed'],
        '_5167': ['MassDiscModalAnalysisAtASpeed'],
        '_5168': ['MeasurementComponentModalAnalysisAtASpeed'],
        '_2618': ['ModalAnalysisAtASpeed'],
        '_5169': ['MountableComponentModalAnalysisAtASpeed'],
        '_5170': ['OilSealModalAnalysisAtASpeed'],
        '_5171': ['PartModalAnalysisAtASpeed'],
        '_5172': ['PartToPartShearCouplingConnectionModalAnalysisAtASpeed'],
        '_5173': ['PartToPartShearCouplingHalfModalAnalysisAtASpeed'],
        '_5174': ['PartToPartShearCouplingModalAnalysisAtASpeed'],
        '_5175': ['PlanetaryConnectionModalAnalysisAtASpeed'],
        '_5176': ['PlanetaryGearSetModalAnalysisAtASpeed'],
        '_5177': ['PlanetCarrierModalAnalysisAtASpeed'],
        '_5178': ['PointLoadModalAnalysisAtASpeed'],
        '_5179': ['PowerLoadModalAnalysisAtASpeed'],
        '_5180': ['PulleyModalAnalysisAtASpeed'],
        '_5181': ['RingPinsModalAnalysisAtASpeed'],
        '_5182': ['RingPinsToDiscConnectionModalAnalysisAtASpeed'],
        '_5183': ['RollingRingAssemblyModalAnalysisAtASpeed'],
        '_5184': ['RollingRingConnectionModalAnalysisAtASpeed'],
        '_5185': ['RollingRingModalAnalysisAtASpeed'],
        '_5186': ['RootAssemblyModalAnalysisAtASpeed'],
        '_5187': ['ShaftHubConnectionModalAnalysisAtASpeed'],
        '_5188': ['ShaftModalAnalysisAtASpeed'],
        '_5189': ['ShaftToMountableComponentConnectionModalAnalysisAtASpeed'],
        '_5190': ['SpecialisedAssemblyModalAnalysisAtASpeed'],
        '_5191': ['SpiralBevelGearMeshModalAnalysisAtASpeed'],
        '_5192': ['SpiralBevelGearModalAnalysisAtASpeed'],
        '_5193': ['SpiralBevelGearSetModalAnalysisAtASpeed'],
        '_5194': ['SpringDamperConnectionModalAnalysisAtASpeed'],
        '_5195': ['SpringDamperHalfModalAnalysisAtASpeed'],
        '_5196': ['SpringDamperModalAnalysisAtASpeed'],
        '_5197': ['StraightBevelDiffGearMeshModalAnalysisAtASpeed'],
        '_5198': ['StraightBevelDiffGearModalAnalysisAtASpeed'],
        '_5199': ['StraightBevelDiffGearSetModalAnalysisAtASpeed'],
        '_5200': ['StraightBevelGearMeshModalAnalysisAtASpeed'],
        '_5201': ['StraightBevelGearModalAnalysisAtASpeed'],
        '_5202': ['StraightBevelGearSetModalAnalysisAtASpeed'],
        '_5203': ['StraightBevelPlanetGearModalAnalysisAtASpeed'],
        '_5204': ['StraightBevelSunGearModalAnalysisAtASpeed'],
        '_5205': ['SynchroniserHalfModalAnalysisAtASpeed'],
        '_5206': ['SynchroniserModalAnalysisAtASpeed'],
        '_5207': ['SynchroniserPartModalAnalysisAtASpeed'],
        '_5208': ['SynchroniserSleeveModalAnalysisAtASpeed'],
        '_5209': ['TorqueConverterConnectionModalAnalysisAtASpeed'],
        '_5210': ['TorqueConverterModalAnalysisAtASpeed'],
        '_5211': ['TorqueConverterPumpModalAnalysisAtASpeed'],
        '_5212': ['TorqueConverterTurbineModalAnalysisAtASpeed'],
        '_5213': ['UnbalancedMassModalAnalysisAtASpeed'],
        '_5214': ['VirtualComponentModalAnalysisAtASpeed'],
        '_5215': ['WormGearMeshModalAnalysisAtASpeed'],
        '_5216': ['WormGearModalAnalysisAtASpeed'],
        '_5217': ['WormGearSetModalAnalysisAtASpeed'],
        '_5218': ['ZerolBevelGearMeshModalAnalysisAtASpeed'],
        '_5219': ['ZerolBevelGearModalAnalysisAtASpeed'],
        '_5220': ['ZerolBevelGearSetModalAnalysisAtASpeed'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
