"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5221 import AbstractAssemblyCompoundModalAnalysisAtASpeed
    from ._5222 import AbstractShaftCompoundModalAnalysisAtASpeed
    from ._5223 import AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
    from ._5224 import AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
    from ._5225 import AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
    from ._5226 import AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed
    from ._5227 import AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
    from ._5228 import AssemblyCompoundModalAnalysisAtASpeed
    from ._5229 import BearingCompoundModalAnalysisAtASpeed
    from ._5230 import BeltConnectionCompoundModalAnalysisAtASpeed
    from ._5231 import BeltDriveCompoundModalAnalysisAtASpeed
    from ._5232 import BevelDifferentialGearCompoundModalAnalysisAtASpeed
    from ._5233 import BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed
    from ._5234 import BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
    from ._5235 import BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
    from ._5236 import BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
    from ._5237 import BevelGearCompoundModalAnalysisAtASpeed
    from ._5238 import BevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5239 import BevelGearSetCompoundModalAnalysisAtASpeed
    from ._5240 import BoltCompoundModalAnalysisAtASpeed
    from ._5241 import BoltedJointCompoundModalAnalysisAtASpeed
    from ._5242 import ClutchCompoundModalAnalysisAtASpeed
    from ._5243 import ClutchConnectionCompoundModalAnalysisAtASpeed
    from ._5244 import ClutchHalfCompoundModalAnalysisAtASpeed
    from ._5245 import CoaxialConnectionCompoundModalAnalysisAtASpeed
    from ._5246 import ComponentCompoundModalAnalysisAtASpeed
    from ._5247 import ConceptCouplingCompoundModalAnalysisAtASpeed
    from ._5248 import ConceptCouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5249 import ConceptCouplingHalfCompoundModalAnalysisAtASpeed
    from ._5250 import ConceptGearCompoundModalAnalysisAtASpeed
    from ._5251 import ConceptGearMeshCompoundModalAnalysisAtASpeed
    from ._5252 import ConceptGearSetCompoundModalAnalysisAtASpeed
    from ._5253 import ConicalGearCompoundModalAnalysisAtASpeed
    from ._5254 import ConicalGearMeshCompoundModalAnalysisAtASpeed
    from ._5255 import ConicalGearSetCompoundModalAnalysisAtASpeed
    from ._5256 import ConnectionCompoundModalAnalysisAtASpeed
    from ._5257 import ConnectorCompoundModalAnalysisAtASpeed
    from ._5258 import CouplingCompoundModalAnalysisAtASpeed
    from ._5259 import CouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5260 import CouplingHalfCompoundModalAnalysisAtASpeed
    from ._5261 import CVTBeltConnectionCompoundModalAnalysisAtASpeed
    from ._5262 import CVTCompoundModalAnalysisAtASpeed
    from ._5263 import CVTPulleyCompoundModalAnalysisAtASpeed
    from ._5264 import CycloidalAssemblyCompoundModalAnalysisAtASpeed
    from ._5265 import CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed
    from ._5266 import CycloidalDiscCompoundModalAnalysisAtASpeed
    from ._5267 import CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed
    from ._5268 import CylindricalGearCompoundModalAnalysisAtASpeed
    from ._5269 import CylindricalGearMeshCompoundModalAnalysisAtASpeed
    from ._5270 import CylindricalGearSetCompoundModalAnalysisAtASpeed
    from ._5271 import CylindricalPlanetGearCompoundModalAnalysisAtASpeed
    from ._5272 import DatumCompoundModalAnalysisAtASpeed
    from ._5273 import ExternalCADModelCompoundModalAnalysisAtASpeed
    from ._5274 import FaceGearCompoundModalAnalysisAtASpeed
    from ._5275 import FaceGearMeshCompoundModalAnalysisAtASpeed
    from ._5276 import FaceGearSetCompoundModalAnalysisAtASpeed
    from ._5277 import FEPartCompoundModalAnalysisAtASpeed
    from ._5278 import FlexiblePinAssemblyCompoundModalAnalysisAtASpeed
    from ._5279 import GearCompoundModalAnalysisAtASpeed
    from ._5280 import GearMeshCompoundModalAnalysisAtASpeed
    from ._5281 import GearSetCompoundModalAnalysisAtASpeed
    from ._5282 import GuideDxfModelCompoundModalAnalysisAtASpeed
    from ._5283 import HypoidGearCompoundModalAnalysisAtASpeed
    from ._5284 import HypoidGearMeshCompoundModalAnalysisAtASpeed
    from ._5285 import HypoidGearSetCompoundModalAnalysisAtASpeed
    from ._5286 import InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
    from ._5287 import KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed
    from ._5288 import KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed
    from ._5289 import KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed
    from ._5290 import KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed
    from ._5291 import KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed
    from ._5292 import KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed
    from ._5293 import KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed
    from ._5294 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5295 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed
    from ._5296 import MassDiscCompoundModalAnalysisAtASpeed
    from ._5297 import MeasurementComponentCompoundModalAnalysisAtASpeed
    from ._5298 import MountableComponentCompoundModalAnalysisAtASpeed
    from ._5299 import OilSealCompoundModalAnalysisAtASpeed
    from ._5300 import PartCompoundModalAnalysisAtASpeed
    from ._5301 import PartToPartShearCouplingCompoundModalAnalysisAtASpeed
    from ._5302 import PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5303 import PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed
    from ._5304 import PlanetaryConnectionCompoundModalAnalysisAtASpeed
    from ._5305 import PlanetaryGearSetCompoundModalAnalysisAtASpeed
    from ._5306 import PlanetCarrierCompoundModalAnalysisAtASpeed
    from ._5307 import PointLoadCompoundModalAnalysisAtASpeed
    from ._5308 import PowerLoadCompoundModalAnalysisAtASpeed
    from ._5309 import PulleyCompoundModalAnalysisAtASpeed
    from ._5310 import RingPinsCompoundModalAnalysisAtASpeed
    from ._5311 import RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed
    from ._5312 import RollingRingAssemblyCompoundModalAnalysisAtASpeed
    from ._5313 import RollingRingCompoundModalAnalysisAtASpeed
    from ._5314 import RollingRingConnectionCompoundModalAnalysisAtASpeed
    from ._5315 import RootAssemblyCompoundModalAnalysisAtASpeed
    from ._5316 import ShaftCompoundModalAnalysisAtASpeed
    from ._5317 import ShaftHubConnectionCompoundModalAnalysisAtASpeed
    from ._5318 import ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
    from ._5319 import SpecialisedAssemblyCompoundModalAnalysisAtASpeed
    from ._5320 import SpiralBevelGearCompoundModalAnalysisAtASpeed
    from ._5321 import SpiralBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5322 import SpiralBevelGearSetCompoundModalAnalysisAtASpeed
    from ._5323 import SpringDamperCompoundModalAnalysisAtASpeed
    from ._5324 import SpringDamperConnectionCompoundModalAnalysisAtASpeed
    from ._5325 import SpringDamperHalfCompoundModalAnalysisAtASpeed
    from ._5326 import StraightBevelDiffGearCompoundModalAnalysisAtASpeed
    from ._5327 import StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed
    from ._5328 import StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
    from ._5329 import StraightBevelGearCompoundModalAnalysisAtASpeed
    from ._5330 import StraightBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5331 import StraightBevelGearSetCompoundModalAnalysisAtASpeed
    from ._5332 import StraightBevelPlanetGearCompoundModalAnalysisAtASpeed
    from ._5333 import StraightBevelSunGearCompoundModalAnalysisAtASpeed
    from ._5334 import SynchroniserCompoundModalAnalysisAtASpeed
    from ._5335 import SynchroniserHalfCompoundModalAnalysisAtASpeed
    from ._5336 import SynchroniserPartCompoundModalAnalysisAtASpeed
    from ._5337 import SynchroniserSleeveCompoundModalAnalysisAtASpeed
    from ._5338 import TorqueConverterCompoundModalAnalysisAtASpeed
    from ._5339 import TorqueConverterConnectionCompoundModalAnalysisAtASpeed
    from ._5340 import TorqueConverterPumpCompoundModalAnalysisAtASpeed
    from ._5341 import TorqueConverterTurbineCompoundModalAnalysisAtASpeed
    from ._5342 import UnbalancedMassCompoundModalAnalysisAtASpeed
    from ._5343 import VirtualComponentCompoundModalAnalysisAtASpeed
    from ._5344 import WormGearCompoundModalAnalysisAtASpeed
    from ._5345 import WormGearMeshCompoundModalAnalysisAtASpeed
    from ._5346 import WormGearSetCompoundModalAnalysisAtASpeed
    from ._5347 import ZerolBevelGearCompoundModalAnalysisAtASpeed
    from ._5348 import ZerolBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5349 import ZerolBevelGearSetCompoundModalAnalysisAtASpeed
else:
    import_structure = {
        '_5221': ['AbstractAssemblyCompoundModalAnalysisAtASpeed'],
        '_5222': ['AbstractShaftCompoundModalAnalysisAtASpeed'],
        '_5223': ['AbstractShaftOrHousingCompoundModalAnalysisAtASpeed'],
        '_5224': ['AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed'],
        '_5225': ['AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed'],
        '_5226': ['AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed'],
        '_5227': ['AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed'],
        '_5228': ['AssemblyCompoundModalAnalysisAtASpeed'],
        '_5229': ['BearingCompoundModalAnalysisAtASpeed'],
        '_5230': ['BeltConnectionCompoundModalAnalysisAtASpeed'],
        '_5231': ['BeltDriveCompoundModalAnalysisAtASpeed'],
        '_5232': ['BevelDifferentialGearCompoundModalAnalysisAtASpeed'],
        '_5233': ['BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed'],
        '_5234': ['BevelDifferentialGearSetCompoundModalAnalysisAtASpeed'],
        '_5235': ['BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed'],
        '_5236': ['BevelDifferentialSunGearCompoundModalAnalysisAtASpeed'],
        '_5237': ['BevelGearCompoundModalAnalysisAtASpeed'],
        '_5238': ['BevelGearMeshCompoundModalAnalysisAtASpeed'],
        '_5239': ['BevelGearSetCompoundModalAnalysisAtASpeed'],
        '_5240': ['BoltCompoundModalAnalysisAtASpeed'],
        '_5241': ['BoltedJointCompoundModalAnalysisAtASpeed'],
        '_5242': ['ClutchCompoundModalAnalysisAtASpeed'],
        '_5243': ['ClutchConnectionCompoundModalAnalysisAtASpeed'],
        '_5244': ['ClutchHalfCompoundModalAnalysisAtASpeed'],
        '_5245': ['CoaxialConnectionCompoundModalAnalysisAtASpeed'],
        '_5246': ['ComponentCompoundModalAnalysisAtASpeed'],
        '_5247': ['ConceptCouplingCompoundModalAnalysisAtASpeed'],
        '_5248': ['ConceptCouplingConnectionCompoundModalAnalysisAtASpeed'],
        '_5249': ['ConceptCouplingHalfCompoundModalAnalysisAtASpeed'],
        '_5250': ['ConceptGearCompoundModalAnalysisAtASpeed'],
        '_5251': ['ConceptGearMeshCompoundModalAnalysisAtASpeed'],
        '_5252': ['ConceptGearSetCompoundModalAnalysisAtASpeed'],
        '_5253': ['ConicalGearCompoundModalAnalysisAtASpeed'],
        '_5254': ['ConicalGearMeshCompoundModalAnalysisAtASpeed'],
        '_5255': ['ConicalGearSetCompoundModalAnalysisAtASpeed'],
        '_5256': ['ConnectionCompoundModalAnalysisAtASpeed'],
        '_5257': ['ConnectorCompoundModalAnalysisAtASpeed'],
        '_5258': ['CouplingCompoundModalAnalysisAtASpeed'],
        '_5259': ['CouplingConnectionCompoundModalAnalysisAtASpeed'],
        '_5260': ['CouplingHalfCompoundModalAnalysisAtASpeed'],
        '_5261': ['CVTBeltConnectionCompoundModalAnalysisAtASpeed'],
        '_5262': ['CVTCompoundModalAnalysisAtASpeed'],
        '_5263': ['CVTPulleyCompoundModalAnalysisAtASpeed'],
        '_5264': ['CycloidalAssemblyCompoundModalAnalysisAtASpeed'],
        '_5265': ['CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed'],
        '_5266': ['CycloidalDiscCompoundModalAnalysisAtASpeed'],
        '_5267': ['CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed'],
        '_5268': ['CylindricalGearCompoundModalAnalysisAtASpeed'],
        '_5269': ['CylindricalGearMeshCompoundModalAnalysisAtASpeed'],
        '_5270': ['CylindricalGearSetCompoundModalAnalysisAtASpeed'],
        '_5271': ['CylindricalPlanetGearCompoundModalAnalysisAtASpeed'],
        '_5272': ['DatumCompoundModalAnalysisAtASpeed'],
        '_5273': ['ExternalCADModelCompoundModalAnalysisAtASpeed'],
        '_5274': ['FaceGearCompoundModalAnalysisAtASpeed'],
        '_5275': ['FaceGearMeshCompoundModalAnalysisAtASpeed'],
        '_5276': ['FaceGearSetCompoundModalAnalysisAtASpeed'],
        '_5277': ['FEPartCompoundModalAnalysisAtASpeed'],
        '_5278': ['FlexiblePinAssemblyCompoundModalAnalysisAtASpeed'],
        '_5279': ['GearCompoundModalAnalysisAtASpeed'],
        '_5280': ['GearMeshCompoundModalAnalysisAtASpeed'],
        '_5281': ['GearSetCompoundModalAnalysisAtASpeed'],
        '_5282': ['GuideDxfModelCompoundModalAnalysisAtASpeed'],
        '_5283': ['HypoidGearCompoundModalAnalysisAtASpeed'],
        '_5284': ['HypoidGearMeshCompoundModalAnalysisAtASpeed'],
        '_5285': ['HypoidGearSetCompoundModalAnalysisAtASpeed'],
        '_5286': ['InterMountableComponentConnectionCompoundModalAnalysisAtASpeed'],
        '_5287': ['KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed'],
        '_5288': ['KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed'],
        '_5289': ['KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed'],
        '_5290': ['KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed'],
        '_5291': ['KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed'],
        '_5292': ['KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed'],
        '_5293': ['KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed'],
        '_5294': ['KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed'],
        '_5295': ['KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed'],
        '_5296': ['MassDiscCompoundModalAnalysisAtASpeed'],
        '_5297': ['MeasurementComponentCompoundModalAnalysisAtASpeed'],
        '_5298': ['MountableComponentCompoundModalAnalysisAtASpeed'],
        '_5299': ['OilSealCompoundModalAnalysisAtASpeed'],
        '_5300': ['PartCompoundModalAnalysisAtASpeed'],
        '_5301': ['PartToPartShearCouplingCompoundModalAnalysisAtASpeed'],
        '_5302': ['PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed'],
        '_5303': ['PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed'],
        '_5304': ['PlanetaryConnectionCompoundModalAnalysisAtASpeed'],
        '_5305': ['PlanetaryGearSetCompoundModalAnalysisAtASpeed'],
        '_5306': ['PlanetCarrierCompoundModalAnalysisAtASpeed'],
        '_5307': ['PointLoadCompoundModalAnalysisAtASpeed'],
        '_5308': ['PowerLoadCompoundModalAnalysisAtASpeed'],
        '_5309': ['PulleyCompoundModalAnalysisAtASpeed'],
        '_5310': ['RingPinsCompoundModalAnalysisAtASpeed'],
        '_5311': ['RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed'],
        '_5312': ['RollingRingAssemblyCompoundModalAnalysisAtASpeed'],
        '_5313': ['RollingRingCompoundModalAnalysisAtASpeed'],
        '_5314': ['RollingRingConnectionCompoundModalAnalysisAtASpeed'],
        '_5315': ['RootAssemblyCompoundModalAnalysisAtASpeed'],
        '_5316': ['ShaftCompoundModalAnalysisAtASpeed'],
        '_5317': ['ShaftHubConnectionCompoundModalAnalysisAtASpeed'],
        '_5318': ['ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed'],
        '_5319': ['SpecialisedAssemblyCompoundModalAnalysisAtASpeed'],
        '_5320': ['SpiralBevelGearCompoundModalAnalysisAtASpeed'],
        '_5321': ['SpiralBevelGearMeshCompoundModalAnalysisAtASpeed'],
        '_5322': ['SpiralBevelGearSetCompoundModalAnalysisAtASpeed'],
        '_5323': ['SpringDamperCompoundModalAnalysisAtASpeed'],
        '_5324': ['SpringDamperConnectionCompoundModalAnalysisAtASpeed'],
        '_5325': ['SpringDamperHalfCompoundModalAnalysisAtASpeed'],
        '_5326': ['StraightBevelDiffGearCompoundModalAnalysisAtASpeed'],
        '_5327': ['StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed'],
        '_5328': ['StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed'],
        '_5329': ['StraightBevelGearCompoundModalAnalysisAtASpeed'],
        '_5330': ['StraightBevelGearMeshCompoundModalAnalysisAtASpeed'],
        '_5331': ['StraightBevelGearSetCompoundModalAnalysisAtASpeed'],
        '_5332': ['StraightBevelPlanetGearCompoundModalAnalysisAtASpeed'],
        '_5333': ['StraightBevelSunGearCompoundModalAnalysisAtASpeed'],
        '_5334': ['SynchroniserCompoundModalAnalysisAtASpeed'],
        '_5335': ['SynchroniserHalfCompoundModalAnalysisAtASpeed'],
        '_5336': ['SynchroniserPartCompoundModalAnalysisAtASpeed'],
        '_5337': ['SynchroniserSleeveCompoundModalAnalysisAtASpeed'],
        '_5338': ['TorqueConverterCompoundModalAnalysisAtASpeed'],
        '_5339': ['TorqueConverterConnectionCompoundModalAnalysisAtASpeed'],
        '_5340': ['TorqueConverterPumpCompoundModalAnalysisAtASpeed'],
        '_5341': ['TorqueConverterTurbineCompoundModalAnalysisAtASpeed'],
        '_5342': ['UnbalancedMassCompoundModalAnalysisAtASpeed'],
        '_5343': ['VirtualComponentCompoundModalAnalysisAtASpeed'],
        '_5344': ['WormGearCompoundModalAnalysisAtASpeed'],
        '_5345': ['WormGearMeshCompoundModalAnalysisAtASpeed'],
        '_5346': ['WormGearSetCompoundModalAnalysisAtASpeed'],
        '_5347': ['ZerolBevelGearCompoundModalAnalysisAtASpeed'],
        '_5348': ['ZerolBevelGearMeshCompoundModalAnalysisAtASpeed'],
        '_5349': ['ZerolBevelGearSetCompoundModalAnalysisAtASpeed'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
