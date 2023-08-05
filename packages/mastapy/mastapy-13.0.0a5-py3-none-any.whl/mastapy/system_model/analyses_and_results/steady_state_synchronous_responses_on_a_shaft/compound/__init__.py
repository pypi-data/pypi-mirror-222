"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3357 import AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3358 import AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3359 import AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3360 import AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3361 import AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3362 import AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3363 import AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3364 import AssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3365 import BearingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3366 import BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3367 import BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3368 import BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3369 import BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3370 import BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3371 import BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3372 import BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3373 import BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3374 import BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3375 import BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3376 import BoltCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3377 import BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3378 import ClutchCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3379 import ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3380 import ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3381 import CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3382 import ComponentCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3383 import ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3384 import ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3385 import ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3386 import ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3387 import ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3388 import ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3389 import ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3390 import ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3391 import ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3392 import ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3393 import ConnectorCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3394 import CouplingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3395 import CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3396 import CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3397 import CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3398 import CVTCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3399 import CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3400 import CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3401 import CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3402 import CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3403 import CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3404 import CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3405 import CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3406 import CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3407 import CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3408 import DatumCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3409 import ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3410 import FaceGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3411 import FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3412 import FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3413 import FEPartCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3414 import FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3415 import GearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3416 import GearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3417 import GearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3418 import GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3419 import HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3420 import HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3421 import HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3422 import InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3423 import KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3424 import KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3425 import KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3426 import KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3427 import KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3428 import KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3429 import KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3430 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3431 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3432 import MassDiscCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3433 import MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3434 import MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3435 import OilSealCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3436 import PartCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3437 import PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3438 import PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3439 import PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3440 import PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3441 import PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3442 import PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3443 import PointLoadCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3444 import PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3445 import PulleyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3446 import RingPinsCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3447 import RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3448 import RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3449 import RollingRingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3450 import RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3451 import RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3452 import ShaftCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3453 import ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3454 import ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3455 import SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3456 import SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3457 import SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3458 import SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3459 import SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3460 import SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3461 import SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3462 import StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3463 import StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3464 import StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3465 import StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3466 import StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3467 import StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3468 import StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3469 import StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3470 import SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3471 import SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3472 import SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3473 import SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3474 import TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3475 import TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3476 import TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3477 import TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3478 import UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3479 import VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3480 import WormGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3481 import WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3482 import WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3483 import ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3484 import ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3485 import ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
else:
    import_structure = {
        '_3357': ['AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3358': ['AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3359': ['AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3360': ['AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3361': ['AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3362': ['AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3363': ['AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3364': ['AssemblyCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3365': ['BearingCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3366': ['BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3367': ['BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3368': ['BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3369': ['BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3370': ['BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3371': ['BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3372': ['BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3373': ['BevelGearCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3374': ['BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3375': ['BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3376': ['BoltCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3377': ['BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3378': ['ClutchCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3379': ['ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3380': ['ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3381': ['CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3382': ['ComponentCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3383': ['ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3384': ['ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3385': ['ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3386': ['ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3387': ['ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3388': ['ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3389': ['ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3390': ['ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3391': ['ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3392': ['ConnectionCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3393': ['ConnectorCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3394': ['CouplingCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3395': ['CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3396': ['CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3397': ['CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3398': ['CVTCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3399': ['CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3400': ['CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3401': ['CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3402': ['CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3403': ['CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3404': ['CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3405': ['CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3406': ['CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3407': ['CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3408': ['DatumCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3409': ['ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3410': ['FaceGearCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3411': ['FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3412': ['FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3413': ['FEPartCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3414': ['FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3415': ['GearCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3416': ['GearMeshCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3417': ['GearSetCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3418': ['GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3419': ['HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3420': ['HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3421': ['HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3422': ['InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3423': ['KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3424': ['KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3425': ['KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3426': ['KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3427': ['KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3428': ['KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3429': ['KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3430': ['KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3431': ['KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3432': ['MassDiscCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3433': ['MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3434': ['MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3435': ['OilSealCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3436': ['PartCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3437': ['PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3438': ['PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3439': ['PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3440': ['PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3441': ['PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3442': ['PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3443': ['PointLoadCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3444': ['PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3445': ['PulleyCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3446': ['RingPinsCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3447': ['RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3448': ['RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3449': ['RollingRingCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3450': ['RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3451': ['RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3452': ['ShaftCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3453': ['ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3454': ['ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3455': ['SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3456': ['SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3457': ['SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3458': ['SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3459': ['SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3460': ['SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3461': ['SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3462': ['StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3463': ['StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3464': ['StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3465': ['StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3466': ['StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3467': ['StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3468': ['StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3469': ['StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3470': ['SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3471': ['SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3472': ['SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3473': ['SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3474': ['TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3475': ['TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3476': ['TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3477': ['TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3478': ['UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3479': ['VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3480': ['WormGearCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3481': ['WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3482': ['WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3483': ['ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3484': ['ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft'],
        '_3485': ['ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
