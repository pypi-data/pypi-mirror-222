"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3616 import AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3617 import AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3618 import AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3619 import AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3620 import AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3621 import AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3622 import AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3623 import AssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3624 import BearingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3625 import BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3626 import BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3627 import BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3628 import BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3629 import BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3630 import BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3631 import BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3632 import BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3633 import BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3634 import BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3635 import BoltCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3636 import BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3637 import ClutchCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3638 import ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3639 import ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3640 import CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3641 import ComponentCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3642 import ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3643 import ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3644 import ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3645 import ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3646 import ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3647 import ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3648 import ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3649 import ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3650 import ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3651 import ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3652 import ConnectorCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3653 import CouplingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3654 import CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3655 import CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3656 import CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3657 import CVTCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3658 import CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3659 import CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3660 import CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3661 import CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3662 import CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3663 import CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3664 import CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3665 import CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3666 import CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3667 import DatumCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3668 import ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3669 import FaceGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3670 import FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3671 import FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3672 import FEPartCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3673 import FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3674 import GearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3675 import GearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3676 import GearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3677 import GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3678 import HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3679 import HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3680 import HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3681 import InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3682 import KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3683 import KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3684 import KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3685 import KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3686 import KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3687 import KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3688 import KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3689 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3690 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3691 import MassDiscCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3692 import MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3693 import MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3694 import OilSealCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3695 import PartCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3696 import PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3697 import PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3698 import PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3699 import PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3700 import PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3701 import PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3702 import PointLoadCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3703 import PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3704 import PulleyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3705 import RingPinsCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3706 import RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3707 import RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3708 import RollingRingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3709 import RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3710 import RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3711 import ShaftCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3712 import ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3713 import ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3714 import SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3715 import SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3716 import SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3717 import SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3718 import SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3719 import SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3720 import SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3721 import StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3722 import StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3723 import StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3724 import StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3725 import StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3726 import StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3727 import StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3728 import StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3729 import SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3730 import SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3731 import SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3732 import SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3733 import TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3734 import TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3735 import TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3736 import TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3737 import UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3738 import VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3739 import WormGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3740 import WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3741 import WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3742 import ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3743 import ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3744 import ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
else:
    import_structure = {
        '_3616': ['AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3617': ['AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3618': ['AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3619': ['AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3620': ['AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3621': ['AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3622': ['AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3623': ['AssemblyCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3624': ['BearingCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3625': ['BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3626': ['BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3627': ['BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3628': ['BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3629': ['BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3630': ['BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3631': ['BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3632': ['BevelGearCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3633': ['BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3634': ['BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3635': ['BoltCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3636': ['BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3637': ['ClutchCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3638': ['ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3639': ['ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3640': ['CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3641': ['ComponentCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3642': ['ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3643': ['ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3644': ['ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3645': ['ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3646': ['ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3647': ['ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3648': ['ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3649': ['ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3650': ['ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3651': ['ConnectionCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3652': ['ConnectorCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3653': ['CouplingCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3654': ['CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3655': ['CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3656': ['CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3657': ['CVTCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3658': ['CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3659': ['CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3660': ['CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3661': ['CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3662': ['CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3663': ['CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3664': ['CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3665': ['CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3666': ['CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3667': ['DatumCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3668': ['ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3669': ['FaceGearCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3670': ['FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3671': ['FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3672': ['FEPartCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3673': ['FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3674': ['GearCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3675': ['GearMeshCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3676': ['GearSetCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3677': ['GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3678': ['HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3679': ['HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3680': ['HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3681': ['InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3682': ['KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3683': ['KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3684': ['KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3685': ['KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3686': ['KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3687': ['KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3688': ['KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3689': ['KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3690': ['KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3691': ['MassDiscCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3692': ['MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3693': ['MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3694': ['OilSealCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3695': ['PartCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3696': ['PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3697': ['PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3698': ['PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3699': ['PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3700': ['PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3701': ['PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3702': ['PointLoadCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3703': ['PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3704': ['PulleyCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3705': ['RingPinsCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3706': ['RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3707': ['RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3708': ['RollingRingCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3709': ['RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3710': ['RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3711': ['ShaftCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3712': ['ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3713': ['ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3714': ['SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3715': ['SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3716': ['SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3717': ['SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3718': ['SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3719': ['SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3720': ['SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3721': ['StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3722': ['StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3723': ['StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3724': ['StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3725': ['StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3726': ['StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3727': ['StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3728': ['StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3729': ['SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3730': ['SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3731': ['SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3732': ['SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3733': ['TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3734': ['TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3735': ['TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3736': ['TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3737': ['UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3738': ['VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3739': ['WormGearCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3740': ['WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3741': ['WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3742': ['ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3743': ['ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed'],
        '_3744': ['ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
