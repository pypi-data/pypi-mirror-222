"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3227 import AbstractAssemblySteadyStateSynchronousResponseOnAShaft
    from ._3228 import AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft
    from ._3229 import AbstractShaftSteadyStateSynchronousResponseOnAShaft
    from ._3230 import AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
    from ._3231 import AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft
    from ._3232 import AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft
    from ._3233 import AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft
    from ._3234 import AssemblySteadyStateSynchronousResponseOnAShaft
    from ._3235 import BearingSteadyStateSynchronousResponseOnAShaft
    from ._3236 import BeltConnectionSteadyStateSynchronousResponseOnAShaft
    from ._3237 import BeltDriveSteadyStateSynchronousResponseOnAShaft
    from ._3238 import BevelDifferentialGearMeshSteadyStateSynchronousResponseOnAShaft
    from ._3239 import BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft
    from ._3240 import BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft
    from ._3241 import BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft
    from ._3242 import BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft
    from ._3243 import BevelGearMeshSteadyStateSynchronousResponseOnAShaft
    from ._3244 import BevelGearSetSteadyStateSynchronousResponseOnAShaft
    from ._3245 import BevelGearSteadyStateSynchronousResponseOnAShaft
    from ._3246 import BoltedJointSteadyStateSynchronousResponseOnAShaft
    from ._3247 import BoltSteadyStateSynchronousResponseOnAShaft
    from ._3248 import ClutchConnectionSteadyStateSynchronousResponseOnAShaft
    from ._3249 import ClutchHalfSteadyStateSynchronousResponseOnAShaft
    from ._3250 import ClutchSteadyStateSynchronousResponseOnAShaft
    from ._3251 import CoaxialConnectionSteadyStateSynchronousResponseOnAShaft
    from ._3252 import ComponentSteadyStateSynchronousResponseOnAShaft
    from ._3253 import ConceptCouplingConnectionSteadyStateSynchronousResponseOnAShaft
    from ._3254 import ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft
    from ._3255 import ConceptCouplingSteadyStateSynchronousResponseOnAShaft
    from ._3256 import ConceptGearMeshSteadyStateSynchronousResponseOnAShaft
    from ._3257 import ConceptGearSetSteadyStateSynchronousResponseOnAShaft
    from ._3258 import ConceptGearSteadyStateSynchronousResponseOnAShaft
    from ._3259 import ConicalGearMeshSteadyStateSynchronousResponseOnAShaft
    from ._3260 import ConicalGearSetSteadyStateSynchronousResponseOnAShaft
    from ._3261 import ConicalGearSteadyStateSynchronousResponseOnAShaft
    from ._3262 import ConnectionSteadyStateSynchronousResponseOnAShaft
    from ._3263 import ConnectorSteadyStateSynchronousResponseOnAShaft
    from ._3264 import CouplingConnectionSteadyStateSynchronousResponseOnAShaft
    from ._3265 import CouplingHalfSteadyStateSynchronousResponseOnAShaft
    from ._3266 import CouplingSteadyStateSynchronousResponseOnAShaft
    from ._3267 import CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft
    from ._3268 import CVTPulleySteadyStateSynchronousResponseOnAShaft
    from ._3269 import CVTSteadyStateSynchronousResponseOnAShaft
    from ._3270 import CycloidalAssemblySteadyStateSynchronousResponseOnAShaft
    from ._3271 import CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft
    from ._3272 import CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft
    from ._3273 import CycloidalDiscSteadyStateSynchronousResponseOnAShaft
    from ._3274 import CylindricalGearMeshSteadyStateSynchronousResponseOnAShaft
    from ._3275 import CylindricalGearSetSteadyStateSynchronousResponseOnAShaft
    from ._3276 import CylindricalGearSteadyStateSynchronousResponseOnAShaft
    from ._3277 import CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft
    from ._3278 import DatumSteadyStateSynchronousResponseOnAShaft
    from ._3279 import ExternalCADModelSteadyStateSynchronousResponseOnAShaft
    from ._3280 import FaceGearMeshSteadyStateSynchronousResponseOnAShaft
    from ._3281 import FaceGearSetSteadyStateSynchronousResponseOnAShaft
    from ._3282 import FaceGearSteadyStateSynchronousResponseOnAShaft
    from ._3283 import FEPartSteadyStateSynchronousResponseOnAShaft
    from ._3284 import FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft
    from ._3285 import GearMeshSteadyStateSynchronousResponseOnAShaft
    from ._3286 import GearSetSteadyStateSynchronousResponseOnAShaft
    from ._3287 import GearSteadyStateSynchronousResponseOnAShaft
    from ._3288 import GuideDxfModelSteadyStateSynchronousResponseOnAShaft
    from ._3289 import HypoidGearMeshSteadyStateSynchronousResponseOnAShaft
    from ._3290 import HypoidGearSetSteadyStateSynchronousResponseOnAShaft
    from ._3291 import HypoidGearSteadyStateSynchronousResponseOnAShaft
    from ._3292 import InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
    from ._3293 import KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft
    from ._3294 import KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft
    from ._3295 import KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft
    from ._3296 import KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseOnAShaft
    from ._3297 import KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft
    from ._3298 import KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseOnAShaft
    from ._3299 import KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft
    from ._3300 import KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
    from ._3301 import KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft
    from ._3302 import MassDiscSteadyStateSynchronousResponseOnAShaft
    from ._3303 import MeasurementComponentSteadyStateSynchronousResponseOnAShaft
    from ._3304 import MountableComponentSteadyStateSynchronousResponseOnAShaft
    from ._3305 import OilSealSteadyStateSynchronousResponseOnAShaft
    from ._3306 import PartSteadyStateSynchronousResponseOnAShaft
    from ._3307 import PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft
    from ._3308 import PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft
    from ._3309 import PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft
    from ._3310 import PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft
    from ._3311 import PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft
    from ._3312 import PlanetCarrierSteadyStateSynchronousResponseOnAShaft
    from ._3313 import PointLoadSteadyStateSynchronousResponseOnAShaft
    from ._3314 import PowerLoadSteadyStateSynchronousResponseOnAShaft
    from ._3315 import PulleySteadyStateSynchronousResponseOnAShaft
    from ._3316 import RingPinsSteadyStateSynchronousResponseOnAShaft
    from ._3317 import RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft
    from ._3318 import RollingRingAssemblySteadyStateSynchronousResponseOnAShaft
    from ._3319 import RollingRingConnectionSteadyStateSynchronousResponseOnAShaft
    from ._3320 import RollingRingSteadyStateSynchronousResponseOnAShaft
    from ._3321 import RootAssemblySteadyStateSynchronousResponseOnAShaft
    from ._3322 import ShaftHubConnectionSteadyStateSynchronousResponseOnAShaft
    from ._3323 import ShaftSteadyStateSynchronousResponseOnAShaft
    from ._3324 import ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
    from ._3325 import SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
    from ._3326 import SpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft
    from ._3327 import SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
    from ._3328 import SpiralBevelGearSteadyStateSynchronousResponseOnAShaft
    from ._3329 import SpringDamperConnectionSteadyStateSynchronousResponseOnAShaft
    from ._3330 import SpringDamperHalfSteadyStateSynchronousResponseOnAShaft
    from ._3331 import SpringDamperSteadyStateSynchronousResponseOnAShaft
    from ._3332 import SteadyStateSynchronousResponseOnAShaft
    from ._3333 import StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft
    from ._3334 import StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft
    from ._3335 import StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft
    from ._3336 import StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft
    from ._3337 import StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft
    from ._3338 import StraightBevelGearSteadyStateSynchronousResponseOnAShaft
    from ._3339 import StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft
    from ._3340 import StraightBevelSunGearSteadyStateSynchronousResponseOnAShaft
    from ._3341 import SynchroniserHalfSteadyStateSynchronousResponseOnAShaft
    from ._3342 import SynchroniserPartSteadyStateSynchronousResponseOnAShaft
    from ._3343 import SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft
    from ._3344 import SynchroniserSteadyStateSynchronousResponseOnAShaft
    from ._3345 import TorqueConverterConnectionSteadyStateSynchronousResponseOnAShaft
    from ._3346 import TorqueConverterPumpSteadyStateSynchronousResponseOnAShaft
    from ._3347 import TorqueConverterSteadyStateSynchronousResponseOnAShaft
    from ._3348 import TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft
    from ._3349 import UnbalancedMassSteadyStateSynchronousResponseOnAShaft
    from ._3350 import VirtualComponentSteadyStateSynchronousResponseOnAShaft
    from ._3351 import WormGearMeshSteadyStateSynchronousResponseOnAShaft
    from ._3352 import WormGearSetSteadyStateSynchronousResponseOnAShaft
    from ._3353 import WormGearSteadyStateSynchronousResponseOnAShaft
    from ._3354 import ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft
    from ._3355 import ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft
    from ._3356 import ZerolBevelGearSteadyStateSynchronousResponseOnAShaft
else:
    import_structure = {
        '_3227': ['AbstractAssemblySteadyStateSynchronousResponseOnAShaft'],
        '_3228': ['AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft'],
        '_3229': ['AbstractShaftSteadyStateSynchronousResponseOnAShaft'],
        '_3230': ['AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft'],
        '_3231': ['AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft'],
        '_3232': ['AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft'],
        '_3233': ['AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft'],
        '_3234': ['AssemblySteadyStateSynchronousResponseOnAShaft'],
        '_3235': ['BearingSteadyStateSynchronousResponseOnAShaft'],
        '_3236': ['BeltConnectionSteadyStateSynchronousResponseOnAShaft'],
        '_3237': ['BeltDriveSteadyStateSynchronousResponseOnAShaft'],
        '_3238': ['BevelDifferentialGearMeshSteadyStateSynchronousResponseOnAShaft'],
        '_3239': ['BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft'],
        '_3240': ['BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft'],
        '_3241': ['BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft'],
        '_3242': ['BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft'],
        '_3243': ['BevelGearMeshSteadyStateSynchronousResponseOnAShaft'],
        '_3244': ['BevelGearSetSteadyStateSynchronousResponseOnAShaft'],
        '_3245': ['BevelGearSteadyStateSynchronousResponseOnAShaft'],
        '_3246': ['BoltedJointSteadyStateSynchronousResponseOnAShaft'],
        '_3247': ['BoltSteadyStateSynchronousResponseOnAShaft'],
        '_3248': ['ClutchConnectionSteadyStateSynchronousResponseOnAShaft'],
        '_3249': ['ClutchHalfSteadyStateSynchronousResponseOnAShaft'],
        '_3250': ['ClutchSteadyStateSynchronousResponseOnAShaft'],
        '_3251': ['CoaxialConnectionSteadyStateSynchronousResponseOnAShaft'],
        '_3252': ['ComponentSteadyStateSynchronousResponseOnAShaft'],
        '_3253': ['ConceptCouplingConnectionSteadyStateSynchronousResponseOnAShaft'],
        '_3254': ['ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft'],
        '_3255': ['ConceptCouplingSteadyStateSynchronousResponseOnAShaft'],
        '_3256': ['ConceptGearMeshSteadyStateSynchronousResponseOnAShaft'],
        '_3257': ['ConceptGearSetSteadyStateSynchronousResponseOnAShaft'],
        '_3258': ['ConceptGearSteadyStateSynchronousResponseOnAShaft'],
        '_3259': ['ConicalGearMeshSteadyStateSynchronousResponseOnAShaft'],
        '_3260': ['ConicalGearSetSteadyStateSynchronousResponseOnAShaft'],
        '_3261': ['ConicalGearSteadyStateSynchronousResponseOnAShaft'],
        '_3262': ['ConnectionSteadyStateSynchronousResponseOnAShaft'],
        '_3263': ['ConnectorSteadyStateSynchronousResponseOnAShaft'],
        '_3264': ['CouplingConnectionSteadyStateSynchronousResponseOnAShaft'],
        '_3265': ['CouplingHalfSteadyStateSynchronousResponseOnAShaft'],
        '_3266': ['CouplingSteadyStateSynchronousResponseOnAShaft'],
        '_3267': ['CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft'],
        '_3268': ['CVTPulleySteadyStateSynchronousResponseOnAShaft'],
        '_3269': ['CVTSteadyStateSynchronousResponseOnAShaft'],
        '_3270': ['CycloidalAssemblySteadyStateSynchronousResponseOnAShaft'],
        '_3271': ['CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft'],
        '_3272': ['CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft'],
        '_3273': ['CycloidalDiscSteadyStateSynchronousResponseOnAShaft'],
        '_3274': ['CylindricalGearMeshSteadyStateSynchronousResponseOnAShaft'],
        '_3275': ['CylindricalGearSetSteadyStateSynchronousResponseOnAShaft'],
        '_3276': ['CylindricalGearSteadyStateSynchronousResponseOnAShaft'],
        '_3277': ['CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft'],
        '_3278': ['DatumSteadyStateSynchronousResponseOnAShaft'],
        '_3279': ['ExternalCADModelSteadyStateSynchronousResponseOnAShaft'],
        '_3280': ['FaceGearMeshSteadyStateSynchronousResponseOnAShaft'],
        '_3281': ['FaceGearSetSteadyStateSynchronousResponseOnAShaft'],
        '_3282': ['FaceGearSteadyStateSynchronousResponseOnAShaft'],
        '_3283': ['FEPartSteadyStateSynchronousResponseOnAShaft'],
        '_3284': ['FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft'],
        '_3285': ['GearMeshSteadyStateSynchronousResponseOnAShaft'],
        '_3286': ['GearSetSteadyStateSynchronousResponseOnAShaft'],
        '_3287': ['GearSteadyStateSynchronousResponseOnAShaft'],
        '_3288': ['GuideDxfModelSteadyStateSynchronousResponseOnAShaft'],
        '_3289': ['HypoidGearMeshSteadyStateSynchronousResponseOnAShaft'],
        '_3290': ['HypoidGearSetSteadyStateSynchronousResponseOnAShaft'],
        '_3291': ['HypoidGearSteadyStateSynchronousResponseOnAShaft'],
        '_3292': ['InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft'],
        '_3293': ['KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft'],
        '_3294': ['KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft'],
        '_3295': ['KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft'],
        '_3296': ['KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseOnAShaft'],
        '_3297': ['KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft'],
        '_3298': ['KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseOnAShaft'],
        '_3299': ['KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft'],
        '_3300': ['KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft'],
        '_3301': ['KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft'],
        '_3302': ['MassDiscSteadyStateSynchronousResponseOnAShaft'],
        '_3303': ['MeasurementComponentSteadyStateSynchronousResponseOnAShaft'],
        '_3304': ['MountableComponentSteadyStateSynchronousResponseOnAShaft'],
        '_3305': ['OilSealSteadyStateSynchronousResponseOnAShaft'],
        '_3306': ['PartSteadyStateSynchronousResponseOnAShaft'],
        '_3307': ['PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft'],
        '_3308': ['PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft'],
        '_3309': ['PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft'],
        '_3310': ['PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft'],
        '_3311': ['PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft'],
        '_3312': ['PlanetCarrierSteadyStateSynchronousResponseOnAShaft'],
        '_3313': ['PointLoadSteadyStateSynchronousResponseOnAShaft'],
        '_3314': ['PowerLoadSteadyStateSynchronousResponseOnAShaft'],
        '_3315': ['PulleySteadyStateSynchronousResponseOnAShaft'],
        '_3316': ['RingPinsSteadyStateSynchronousResponseOnAShaft'],
        '_3317': ['RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft'],
        '_3318': ['RollingRingAssemblySteadyStateSynchronousResponseOnAShaft'],
        '_3319': ['RollingRingConnectionSteadyStateSynchronousResponseOnAShaft'],
        '_3320': ['RollingRingSteadyStateSynchronousResponseOnAShaft'],
        '_3321': ['RootAssemblySteadyStateSynchronousResponseOnAShaft'],
        '_3322': ['ShaftHubConnectionSteadyStateSynchronousResponseOnAShaft'],
        '_3323': ['ShaftSteadyStateSynchronousResponseOnAShaft'],
        '_3324': ['ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft'],
        '_3325': ['SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft'],
        '_3326': ['SpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft'],
        '_3327': ['SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft'],
        '_3328': ['SpiralBevelGearSteadyStateSynchronousResponseOnAShaft'],
        '_3329': ['SpringDamperConnectionSteadyStateSynchronousResponseOnAShaft'],
        '_3330': ['SpringDamperHalfSteadyStateSynchronousResponseOnAShaft'],
        '_3331': ['SpringDamperSteadyStateSynchronousResponseOnAShaft'],
        '_3332': ['SteadyStateSynchronousResponseOnAShaft'],
        '_3333': ['StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft'],
        '_3334': ['StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft'],
        '_3335': ['StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft'],
        '_3336': ['StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft'],
        '_3337': ['StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft'],
        '_3338': ['StraightBevelGearSteadyStateSynchronousResponseOnAShaft'],
        '_3339': ['StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft'],
        '_3340': ['StraightBevelSunGearSteadyStateSynchronousResponseOnAShaft'],
        '_3341': ['SynchroniserHalfSteadyStateSynchronousResponseOnAShaft'],
        '_3342': ['SynchroniserPartSteadyStateSynchronousResponseOnAShaft'],
        '_3343': ['SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft'],
        '_3344': ['SynchroniserSteadyStateSynchronousResponseOnAShaft'],
        '_3345': ['TorqueConverterConnectionSteadyStateSynchronousResponseOnAShaft'],
        '_3346': ['TorqueConverterPumpSteadyStateSynchronousResponseOnAShaft'],
        '_3347': ['TorqueConverterSteadyStateSynchronousResponseOnAShaft'],
        '_3348': ['TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft'],
        '_3349': ['UnbalancedMassSteadyStateSynchronousResponseOnAShaft'],
        '_3350': ['VirtualComponentSteadyStateSynchronousResponseOnAShaft'],
        '_3351': ['WormGearMeshSteadyStateSynchronousResponseOnAShaft'],
        '_3352': ['WormGearSetSteadyStateSynchronousResponseOnAShaft'],
        '_3353': ['WormGearSteadyStateSynchronousResponseOnAShaft'],
        '_3354': ['ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft'],
        '_3355': ['ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft'],
        '_3356': ['ZerolBevelGearSteadyStateSynchronousResponseOnAShaft'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
