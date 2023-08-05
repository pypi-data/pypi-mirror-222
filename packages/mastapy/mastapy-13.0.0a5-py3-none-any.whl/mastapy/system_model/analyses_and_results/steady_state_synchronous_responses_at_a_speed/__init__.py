"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3486 import AbstractAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3487 import AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed
    from ._3488 import AbstractShaftSteadyStateSynchronousResponseAtASpeed
    from ._3489 import AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3490 import AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3491 import AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3492 import AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
    from ._3493 import AssemblySteadyStateSynchronousResponseAtASpeed
    from ._3494 import BearingSteadyStateSynchronousResponseAtASpeed
    from ._3495 import BeltConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3496 import BeltDriveSteadyStateSynchronousResponseAtASpeed
    from ._3497 import BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3498 import BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3499 import BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
    from ._3500 import BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed
    from ._3501 import BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed
    from ._3502 import BevelGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3503 import BevelGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3504 import BevelGearSteadyStateSynchronousResponseAtASpeed
    from ._3505 import BoltedJointSteadyStateSynchronousResponseAtASpeed
    from ._3506 import BoltSteadyStateSynchronousResponseAtASpeed
    from ._3507 import ClutchConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3508 import ClutchHalfSteadyStateSynchronousResponseAtASpeed
    from ._3509 import ClutchSteadyStateSynchronousResponseAtASpeed
    from ._3510 import CoaxialConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3511 import ComponentSteadyStateSynchronousResponseAtASpeed
    from ._3512 import ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3513 import ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed
    from ._3514 import ConceptCouplingSteadyStateSynchronousResponseAtASpeed
    from ._3515 import ConceptGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3516 import ConceptGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3517 import ConceptGearSteadyStateSynchronousResponseAtASpeed
    from ._3518 import ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3519 import ConicalGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3520 import ConicalGearSteadyStateSynchronousResponseAtASpeed
    from ._3521 import ConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3522 import ConnectorSteadyStateSynchronousResponseAtASpeed
    from ._3523 import CouplingConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3524 import CouplingHalfSteadyStateSynchronousResponseAtASpeed
    from ._3525 import CouplingSteadyStateSynchronousResponseAtASpeed
    from ._3526 import CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3527 import CVTPulleySteadyStateSynchronousResponseAtASpeed
    from ._3528 import CVTSteadyStateSynchronousResponseAtASpeed
    from ._3529 import CycloidalAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3530 import CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3531 import CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3532 import CycloidalDiscSteadyStateSynchronousResponseAtASpeed
    from ._3533 import CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3534 import CylindricalGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3535 import CylindricalGearSteadyStateSynchronousResponseAtASpeed
    from ._3536 import CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed
    from ._3537 import DatumSteadyStateSynchronousResponseAtASpeed
    from ._3538 import ExternalCADModelSteadyStateSynchronousResponseAtASpeed
    from ._3539 import FaceGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3540 import FaceGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3541 import FaceGearSteadyStateSynchronousResponseAtASpeed
    from ._3542 import FEPartSteadyStateSynchronousResponseAtASpeed
    from ._3543 import FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3544 import GearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3545 import GearSetSteadyStateSynchronousResponseAtASpeed
    from ._3546 import GearSteadyStateSynchronousResponseAtASpeed
    from ._3547 import GuideDxfModelSteadyStateSynchronousResponseAtASpeed
    from ._3548 import HypoidGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3549 import HypoidGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3550 import HypoidGearSteadyStateSynchronousResponseAtASpeed
    from ._3551 import InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3552 import KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3553 import KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3554 import KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed
    from ._3555 import KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3556 import KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3557 import KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed
    from ._3558 import KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3559 import KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3560 import KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed
    from ._3561 import MassDiscSteadyStateSynchronousResponseAtASpeed
    from ._3562 import MeasurementComponentSteadyStateSynchronousResponseAtASpeed
    from ._3563 import MountableComponentSteadyStateSynchronousResponseAtASpeed
    from ._3564 import OilSealSteadyStateSynchronousResponseAtASpeed
    from ._3565 import PartSteadyStateSynchronousResponseAtASpeed
    from ._3566 import PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3567 import PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed
    from ._3568 import PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed
    from ._3569 import PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3570 import PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3571 import PlanetCarrierSteadyStateSynchronousResponseAtASpeed
    from ._3572 import PointLoadSteadyStateSynchronousResponseAtASpeed
    from ._3573 import PowerLoadSteadyStateSynchronousResponseAtASpeed
    from ._3574 import PulleySteadyStateSynchronousResponseAtASpeed
    from ._3575 import RingPinsSteadyStateSynchronousResponseAtASpeed
    from ._3576 import RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3577 import RollingRingAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3578 import RollingRingConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3579 import RollingRingSteadyStateSynchronousResponseAtASpeed
    from ._3580 import RootAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3581 import ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3582 import ShaftSteadyStateSynchronousResponseAtASpeed
    from ._3583 import ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3584 import SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3585 import SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3586 import SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3587 import SpiralBevelGearSteadyStateSynchronousResponseAtASpeed
    from ._3588 import SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3589 import SpringDamperHalfSteadyStateSynchronousResponseAtASpeed
    from ._3590 import SpringDamperSteadyStateSynchronousResponseAtASpeed
    from ._3591 import SteadyStateSynchronousResponseAtASpeed
    from ._3592 import StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3593 import StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3594 import StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
    from ._3595 import StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3596 import StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3597 import StraightBevelGearSteadyStateSynchronousResponseAtASpeed
    from ._3598 import StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed
    from ._3599 import StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed
    from ._3600 import SynchroniserHalfSteadyStateSynchronousResponseAtASpeed
    from ._3601 import SynchroniserPartSteadyStateSynchronousResponseAtASpeed
    from ._3602 import SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed
    from ._3603 import SynchroniserSteadyStateSynchronousResponseAtASpeed
    from ._3604 import TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3605 import TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed
    from ._3606 import TorqueConverterSteadyStateSynchronousResponseAtASpeed
    from ._3607 import TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed
    from ._3608 import UnbalancedMassSteadyStateSynchronousResponseAtASpeed
    from ._3609 import VirtualComponentSteadyStateSynchronousResponseAtASpeed
    from ._3610 import WormGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3611 import WormGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3612 import WormGearSteadyStateSynchronousResponseAtASpeed
    from ._3613 import ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3614 import ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3615 import ZerolBevelGearSteadyStateSynchronousResponseAtASpeed
else:
    import_structure = {
        '_3486': ['AbstractAssemblySteadyStateSynchronousResponseAtASpeed'],
        '_3487': ['AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed'],
        '_3488': ['AbstractShaftSteadyStateSynchronousResponseAtASpeed'],
        '_3489': ['AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed'],
        '_3490': ['AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed'],
        '_3491': ['AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed'],
        '_3492': ['AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed'],
        '_3493': ['AssemblySteadyStateSynchronousResponseAtASpeed'],
        '_3494': ['BearingSteadyStateSynchronousResponseAtASpeed'],
        '_3495': ['BeltConnectionSteadyStateSynchronousResponseAtASpeed'],
        '_3496': ['BeltDriveSteadyStateSynchronousResponseAtASpeed'],
        '_3497': ['BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed'],
        '_3498': ['BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed'],
        '_3499': ['BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed'],
        '_3500': ['BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed'],
        '_3501': ['BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed'],
        '_3502': ['BevelGearMeshSteadyStateSynchronousResponseAtASpeed'],
        '_3503': ['BevelGearSetSteadyStateSynchronousResponseAtASpeed'],
        '_3504': ['BevelGearSteadyStateSynchronousResponseAtASpeed'],
        '_3505': ['BoltedJointSteadyStateSynchronousResponseAtASpeed'],
        '_3506': ['BoltSteadyStateSynchronousResponseAtASpeed'],
        '_3507': ['ClutchConnectionSteadyStateSynchronousResponseAtASpeed'],
        '_3508': ['ClutchHalfSteadyStateSynchronousResponseAtASpeed'],
        '_3509': ['ClutchSteadyStateSynchronousResponseAtASpeed'],
        '_3510': ['CoaxialConnectionSteadyStateSynchronousResponseAtASpeed'],
        '_3511': ['ComponentSteadyStateSynchronousResponseAtASpeed'],
        '_3512': ['ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed'],
        '_3513': ['ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed'],
        '_3514': ['ConceptCouplingSteadyStateSynchronousResponseAtASpeed'],
        '_3515': ['ConceptGearMeshSteadyStateSynchronousResponseAtASpeed'],
        '_3516': ['ConceptGearSetSteadyStateSynchronousResponseAtASpeed'],
        '_3517': ['ConceptGearSteadyStateSynchronousResponseAtASpeed'],
        '_3518': ['ConicalGearMeshSteadyStateSynchronousResponseAtASpeed'],
        '_3519': ['ConicalGearSetSteadyStateSynchronousResponseAtASpeed'],
        '_3520': ['ConicalGearSteadyStateSynchronousResponseAtASpeed'],
        '_3521': ['ConnectionSteadyStateSynchronousResponseAtASpeed'],
        '_3522': ['ConnectorSteadyStateSynchronousResponseAtASpeed'],
        '_3523': ['CouplingConnectionSteadyStateSynchronousResponseAtASpeed'],
        '_3524': ['CouplingHalfSteadyStateSynchronousResponseAtASpeed'],
        '_3525': ['CouplingSteadyStateSynchronousResponseAtASpeed'],
        '_3526': ['CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed'],
        '_3527': ['CVTPulleySteadyStateSynchronousResponseAtASpeed'],
        '_3528': ['CVTSteadyStateSynchronousResponseAtASpeed'],
        '_3529': ['CycloidalAssemblySteadyStateSynchronousResponseAtASpeed'],
        '_3530': ['CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed'],
        '_3531': ['CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed'],
        '_3532': ['CycloidalDiscSteadyStateSynchronousResponseAtASpeed'],
        '_3533': ['CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed'],
        '_3534': ['CylindricalGearSetSteadyStateSynchronousResponseAtASpeed'],
        '_3535': ['CylindricalGearSteadyStateSynchronousResponseAtASpeed'],
        '_3536': ['CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed'],
        '_3537': ['DatumSteadyStateSynchronousResponseAtASpeed'],
        '_3538': ['ExternalCADModelSteadyStateSynchronousResponseAtASpeed'],
        '_3539': ['FaceGearMeshSteadyStateSynchronousResponseAtASpeed'],
        '_3540': ['FaceGearSetSteadyStateSynchronousResponseAtASpeed'],
        '_3541': ['FaceGearSteadyStateSynchronousResponseAtASpeed'],
        '_3542': ['FEPartSteadyStateSynchronousResponseAtASpeed'],
        '_3543': ['FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed'],
        '_3544': ['GearMeshSteadyStateSynchronousResponseAtASpeed'],
        '_3545': ['GearSetSteadyStateSynchronousResponseAtASpeed'],
        '_3546': ['GearSteadyStateSynchronousResponseAtASpeed'],
        '_3547': ['GuideDxfModelSteadyStateSynchronousResponseAtASpeed'],
        '_3548': ['HypoidGearMeshSteadyStateSynchronousResponseAtASpeed'],
        '_3549': ['HypoidGearSetSteadyStateSynchronousResponseAtASpeed'],
        '_3550': ['HypoidGearSteadyStateSynchronousResponseAtASpeed'],
        '_3551': ['InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed'],
        '_3552': ['KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed'],
        '_3553': ['KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed'],
        '_3554': ['KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed'],
        '_3555': ['KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed'],
        '_3556': ['KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed'],
        '_3557': ['KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed'],
        '_3558': ['KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed'],
        '_3559': ['KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed'],
        '_3560': ['KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed'],
        '_3561': ['MassDiscSteadyStateSynchronousResponseAtASpeed'],
        '_3562': ['MeasurementComponentSteadyStateSynchronousResponseAtASpeed'],
        '_3563': ['MountableComponentSteadyStateSynchronousResponseAtASpeed'],
        '_3564': ['OilSealSteadyStateSynchronousResponseAtASpeed'],
        '_3565': ['PartSteadyStateSynchronousResponseAtASpeed'],
        '_3566': ['PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed'],
        '_3567': ['PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed'],
        '_3568': ['PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed'],
        '_3569': ['PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed'],
        '_3570': ['PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed'],
        '_3571': ['PlanetCarrierSteadyStateSynchronousResponseAtASpeed'],
        '_3572': ['PointLoadSteadyStateSynchronousResponseAtASpeed'],
        '_3573': ['PowerLoadSteadyStateSynchronousResponseAtASpeed'],
        '_3574': ['PulleySteadyStateSynchronousResponseAtASpeed'],
        '_3575': ['RingPinsSteadyStateSynchronousResponseAtASpeed'],
        '_3576': ['RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed'],
        '_3577': ['RollingRingAssemblySteadyStateSynchronousResponseAtASpeed'],
        '_3578': ['RollingRingConnectionSteadyStateSynchronousResponseAtASpeed'],
        '_3579': ['RollingRingSteadyStateSynchronousResponseAtASpeed'],
        '_3580': ['RootAssemblySteadyStateSynchronousResponseAtASpeed'],
        '_3581': ['ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed'],
        '_3582': ['ShaftSteadyStateSynchronousResponseAtASpeed'],
        '_3583': ['ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed'],
        '_3584': ['SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed'],
        '_3585': ['SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed'],
        '_3586': ['SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed'],
        '_3587': ['SpiralBevelGearSteadyStateSynchronousResponseAtASpeed'],
        '_3588': ['SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed'],
        '_3589': ['SpringDamperHalfSteadyStateSynchronousResponseAtASpeed'],
        '_3590': ['SpringDamperSteadyStateSynchronousResponseAtASpeed'],
        '_3591': ['SteadyStateSynchronousResponseAtASpeed'],
        '_3592': ['StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed'],
        '_3593': ['StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed'],
        '_3594': ['StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed'],
        '_3595': ['StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed'],
        '_3596': ['StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed'],
        '_3597': ['StraightBevelGearSteadyStateSynchronousResponseAtASpeed'],
        '_3598': ['StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed'],
        '_3599': ['StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed'],
        '_3600': ['SynchroniserHalfSteadyStateSynchronousResponseAtASpeed'],
        '_3601': ['SynchroniserPartSteadyStateSynchronousResponseAtASpeed'],
        '_3602': ['SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed'],
        '_3603': ['SynchroniserSteadyStateSynchronousResponseAtASpeed'],
        '_3604': ['TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed'],
        '_3605': ['TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed'],
        '_3606': ['TorqueConverterSteadyStateSynchronousResponseAtASpeed'],
        '_3607': ['TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed'],
        '_3608': ['UnbalancedMassSteadyStateSynchronousResponseAtASpeed'],
        '_3609': ['VirtualComponentSteadyStateSynchronousResponseAtASpeed'],
        '_3610': ['WormGearMeshSteadyStateSynchronousResponseAtASpeed'],
        '_3611': ['WormGearSetSteadyStateSynchronousResponseAtASpeed'],
        '_3612': ['WormGearSteadyStateSynchronousResponseAtASpeed'],
        '_3613': ['ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed'],
        '_3614': ['ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed'],
        '_3615': ['ZerolBevelGearSteadyStateSynchronousResponseAtASpeed'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
