"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2667 import AbstractAssemblySystemDeflection
    from ._2668 import AbstractShaftOrHousingSystemDeflection
    from ._2669 import AbstractShaftSystemDeflection
    from ._2670 import AbstractShaftToMountableComponentConnectionSystemDeflection
    from ._2671 import AGMAGleasonConicalGearMeshSystemDeflection
    from ._2672 import AGMAGleasonConicalGearSetSystemDeflection
    from ._2673 import AGMAGleasonConicalGearSystemDeflection
    from ._2674 import AssemblySystemDeflection
    from ._2675 import BearingDynamicElementContactPropertyWrapper
    from ._2676 import BearingDynamicElementPropertyWrapper
    from ._2677 import BearingDynamicPostAnalysisResultWrapper
    from ._2678 import BearingDynamicResultsPropertyWrapper
    from ._2679 import BearingDynamicResultsUIWrapper
    from ._2680 import BearingSystemDeflection
    from ._2681 import BeltConnectionSystemDeflection
    from ._2682 import BeltDriveSystemDeflection
    from ._2683 import BevelDifferentialGearMeshSystemDeflection
    from ._2684 import BevelDifferentialGearSetSystemDeflection
    from ._2685 import BevelDifferentialGearSystemDeflection
    from ._2686 import BevelDifferentialPlanetGearSystemDeflection
    from ._2687 import BevelDifferentialSunGearSystemDeflection
    from ._2688 import BevelGearMeshSystemDeflection
    from ._2689 import BevelGearSetSystemDeflection
    from ._2690 import BevelGearSystemDeflection
    from ._2691 import BoltedJointSystemDeflection
    from ._2692 import BoltSystemDeflection
    from ._2693 import ClutchConnectionSystemDeflection
    from ._2694 import ClutchHalfSystemDeflection
    from ._2695 import ClutchSystemDeflection
    from ._2696 import CoaxialConnectionSystemDeflection
    from ._2697 import ComponentSystemDeflection
    from ._2698 import ConcentricPartGroupCombinationSystemDeflectionResults
    from ._2699 import ConceptCouplingConnectionSystemDeflection
    from ._2700 import ConceptCouplingHalfSystemDeflection
    from ._2701 import ConceptCouplingSystemDeflection
    from ._2702 import ConceptGearMeshSystemDeflection
    from ._2703 import ConceptGearSetSystemDeflection
    from ._2704 import ConceptGearSystemDeflection
    from ._2705 import ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator
    from ._2706 import ConicalGearMeshSystemDeflection
    from ._2707 import ConicalGearSetSystemDeflection
    from ._2708 import ConicalGearSystemDeflection
    from ._2709 import ConnectionSystemDeflection
    from ._2710 import ConnectorSystemDeflection
    from ._2711 import CouplingConnectionSystemDeflection
    from ._2712 import CouplingHalfSystemDeflection
    from ._2713 import CouplingSystemDeflection
    from ._2714 import CVTBeltConnectionSystemDeflection
    from ._2715 import CVTPulleySystemDeflection
    from ._2716 import CVTSystemDeflection
    from ._2717 import CycloidalAssemblySystemDeflection
    from ._2718 import CycloidalDiscCentralBearingConnectionSystemDeflection
    from ._2719 import CycloidalDiscPlanetaryBearingConnectionSystemDeflection
    from ._2720 import CycloidalDiscSystemDeflection
    from ._2721 import CylindricalGearMeshSystemDeflection
    from ._2722 import CylindricalGearMeshSystemDeflectionTimestep
    from ._2723 import CylindricalGearMeshSystemDeflectionWithLTCAResults
    from ._2724 import CylindricalGearSetSystemDeflection
    from ._2725 import CylindricalGearSetSystemDeflectionTimestep
    from ._2726 import CylindricalGearSetSystemDeflectionWithLTCAResults
    from ._2727 import CylindricalGearSystemDeflection
    from ._2728 import CylindricalGearSystemDeflectionTimestep
    from ._2729 import CylindricalGearSystemDeflectionWithLTCAResults
    from ._2730 import CylindricalMeshedGearFlankSystemDeflection
    from ._2731 import CylindricalMeshedGearSystemDeflection
    from ._2732 import CylindricalPlanetGearSystemDeflection
    from ._2733 import DatumSystemDeflection
    from ._2734 import ExternalCADModelSystemDeflection
    from ._2735 import FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator
    from ._2736 import FaceGearMeshSystemDeflection
    from ._2737 import FaceGearSetSystemDeflection
    from ._2738 import FaceGearSystemDeflection
    from ._2739 import FEPartSystemDeflection
    from ._2740 import FlexiblePinAssemblySystemDeflection
    from ._2741 import GearMeshSystemDeflection
    from ._2742 import GearSetSystemDeflection
    from ._2743 import GearSystemDeflection
    from ._2744 import GuideDxfModelSystemDeflection
    from ._2745 import HypoidGearMeshSystemDeflection
    from ._2746 import HypoidGearSetSystemDeflection
    from ._2747 import HypoidGearSystemDeflection
    from ._2748 import InformationForContactAtPointAlongFaceWidth
    from ._2749 import InterMountableComponentConnectionSystemDeflection
    from ._2750 import KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
    from ._2751 import KlingelnbergCycloPalloidConicalGearSetSystemDeflection
    from ._2752 import KlingelnbergCycloPalloidConicalGearSystemDeflection
    from ._2753 import KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
    from ._2754 import KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
    from ._2755 import KlingelnbergCycloPalloidHypoidGearSystemDeflection
    from ._2756 import KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
    from ._2757 import KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
    from ._2758 import KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
    from ._2759 import LoadCaseOverallEfficiencyResult
    from ._2760 import LoadSharingFactorReporter
    from ._2761 import MassDiscSystemDeflection
    from ._2762 import MeasurementComponentSystemDeflection
    from ._2763 import MeshSeparationsAtFaceWidth
    from ._2764 import MountableComponentSystemDeflection
    from ._2765 import ObservedPinStiffnessReporter
    from ._2766 import OilSealSystemDeflection
    from ._2767 import PartSystemDeflection
    from ._2768 import PartToPartShearCouplingConnectionSystemDeflection
    from ._2769 import PartToPartShearCouplingHalfSystemDeflection
    from ._2770 import PartToPartShearCouplingSystemDeflection
    from ._2771 import PlanetaryConnectionSystemDeflection
    from ._2772 import PlanetCarrierSystemDeflection
    from ._2773 import PointLoadSystemDeflection
    from ._2774 import PowerLoadSystemDeflection
    from ._2775 import PulleySystemDeflection
    from ._2776 import RingPinsSystemDeflection
    from ._2777 import RingPinsToDiscConnectionSystemDeflection
    from ._2778 import RingPinToDiscContactReporting
    from ._2779 import RollingRingAssemblySystemDeflection
    from ._2780 import RollingRingConnectionSystemDeflection
    from ._2781 import RollingRingSystemDeflection
    from ._2782 import RootAssemblySystemDeflection
    from ._2783 import ShaftHubConnectionSystemDeflection
    from ._2784 import ShaftSectionEndResultsSystemDeflection
    from ._2785 import ShaftSectionSystemDeflection
    from ._2786 import ShaftSystemDeflection
    from ._2787 import ShaftToMountableComponentConnectionSystemDeflection
    from ._2788 import SpecialisedAssemblySystemDeflection
    from ._2789 import SpiralBevelGearMeshSystemDeflection
    from ._2790 import SpiralBevelGearSetSystemDeflection
    from ._2791 import SpiralBevelGearSystemDeflection
    from ._2792 import SpringDamperConnectionSystemDeflection
    from ._2793 import SpringDamperHalfSystemDeflection
    from ._2794 import SpringDamperSystemDeflection
    from ._2795 import StraightBevelDiffGearMeshSystemDeflection
    from ._2796 import StraightBevelDiffGearSetSystemDeflection
    from ._2797 import StraightBevelDiffGearSystemDeflection
    from ._2798 import StraightBevelGearMeshSystemDeflection
    from ._2799 import StraightBevelGearSetSystemDeflection
    from ._2800 import StraightBevelGearSystemDeflection
    from ._2801 import StraightBevelPlanetGearSystemDeflection
    from ._2802 import StraightBevelSunGearSystemDeflection
    from ._2803 import SynchroniserHalfSystemDeflection
    from ._2804 import SynchroniserPartSystemDeflection
    from ._2805 import SynchroniserSleeveSystemDeflection
    from ._2806 import SynchroniserSystemDeflection
    from ._2807 import SystemDeflection
    from ._2808 import SystemDeflectionDrawStyle
    from ._2809 import SystemDeflectionOptions
    from ._2810 import TorqueConverterConnectionSystemDeflection
    from ._2811 import TorqueConverterPumpSystemDeflection
    from ._2812 import TorqueConverterSystemDeflection
    from ._2813 import TorqueConverterTurbineSystemDeflection
    from ._2814 import TorsionalSystemDeflection
    from ._2815 import TransmissionErrorResult
    from ._2816 import UnbalancedMassSystemDeflection
    from ._2817 import VirtualComponentSystemDeflection
    from ._2818 import WormGearMeshSystemDeflection
    from ._2819 import WormGearSetSystemDeflection
    from ._2820 import WormGearSystemDeflection
    from ._2821 import ZerolBevelGearMeshSystemDeflection
    from ._2822 import ZerolBevelGearSetSystemDeflection
    from ._2823 import ZerolBevelGearSystemDeflection
else:
    import_structure = {
        '_2667': ['AbstractAssemblySystemDeflection'],
        '_2668': ['AbstractShaftOrHousingSystemDeflection'],
        '_2669': ['AbstractShaftSystemDeflection'],
        '_2670': ['AbstractShaftToMountableComponentConnectionSystemDeflection'],
        '_2671': ['AGMAGleasonConicalGearMeshSystemDeflection'],
        '_2672': ['AGMAGleasonConicalGearSetSystemDeflection'],
        '_2673': ['AGMAGleasonConicalGearSystemDeflection'],
        '_2674': ['AssemblySystemDeflection'],
        '_2675': ['BearingDynamicElementContactPropertyWrapper'],
        '_2676': ['BearingDynamicElementPropertyWrapper'],
        '_2677': ['BearingDynamicPostAnalysisResultWrapper'],
        '_2678': ['BearingDynamicResultsPropertyWrapper'],
        '_2679': ['BearingDynamicResultsUIWrapper'],
        '_2680': ['BearingSystemDeflection'],
        '_2681': ['BeltConnectionSystemDeflection'],
        '_2682': ['BeltDriveSystemDeflection'],
        '_2683': ['BevelDifferentialGearMeshSystemDeflection'],
        '_2684': ['BevelDifferentialGearSetSystemDeflection'],
        '_2685': ['BevelDifferentialGearSystemDeflection'],
        '_2686': ['BevelDifferentialPlanetGearSystemDeflection'],
        '_2687': ['BevelDifferentialSunGearSystemDeflection'],
        '_2688': ['BevelGearMeshSystemDeflection'],
        '_2689': ['BevelGearSetSystemDeflection'],
        '_2690': ['BevelGearSystemDeflection'],
        '_2691': ['BoltedJointSystemDeflection'],
        '_2692': ['BoltSystemDeflection'],
        '_2693': ['ClutchConnectionSystemDeflection'],
        '_2694': ['ClutchHalfSystemDeflection'],
        '_2695': ['ClutchSystemDeflection'],
        '_2696': ['CoaxialConnectionSystemDeflection'],
        '_2697': ['ComponentSystemDeflection'],
        '_2698': ['ConcentricPartGroupCombinationSystemDeflectionResults'],
        '_2699': ['ConceptCouplingConnectionSystemDeflection'],
        '_2700': ['ConceptCouplingHalfSystemDeflection'],
        '_2701': ['ConceptCouplingSystemDeflection'],
        '_2702': ['ConceptGearMeshSystemDeflection'],
        '_2703': ['ConceptGearSetSystemDeflection'],
        '_2704': ['ConceptGearSystemDeflection'],
        '_2705': ['ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator'],
        '_2706': ['ConicalGearMeshSystemDeflection'],
        '_2707': ['ConicalGearSetSystemDeflection'],
        '_2708': ['ConicalGearSystemDeflection'],
        '_2709': ['ConnectionSystemDeflection'],
        '_2710': ['ConnectorSystemDeflection'],
        '_2711': ['CouplingConnectionSystemDeflection'],
        '_2712': ['CouplingHalfSystemDeflection'],
        '_2713': ['CouplingSystemDeflection'],
        '_2714': ['CVTBeltConnectionSystemDeflection'],
        '_2715': ['CVTPulleySystemDeflection'],
        '_2716': ['CVTSystemDeflection'],
        '_2717': ['CycloidalAssemblySystemDeflection'],
        '_2718': ['CycloidalDiscCentralBearingConnectionSystemDeflection'],
        '_2719': ['CycloidalDiscPlanetaryBearingConnectionSystemDeflection'],
        '_2720': ['CycloidalDiscSystemDeflection'],
        '_2721': ['CylindricalGearMeshSystemDeflection'],
        '_2722': ['CylindricalGearMeshSystemDeflectionTimestep'],
        '_2723': ['CylindricalGearMeshSystemDeflectionWithLTCAResults'],
        '_2724': ['CylindricalGearSetSystemDeflection'],
        '_2725': ['CylindricalGearSetSystemDeflectionTimestep'],
        '_2726': ['CylindricalGearSetSystemDeflectionWithLTCAResults'],
        '_2727': ['CylindricalGearSystemDeflection'],
        '_2728': ['CylindricalGearSystemDeflectionTimestep'],
        '_2729': ['CylindricalGearSystemDeflectionWithLTCAResults'],
        '_2730': ['CylindricalMeshedGearFlankSystemDeflection'],
        '_2731': ['CylindricalMeshedGearSystemDeflection'],
        '_2732': ['CylindricalPlanetGearSystemDeflection'],
        '_2733': ['DatumSystemDeflection'],
        '_2734': ['ExternalCADModelSystemDeflection'],
        '_2735': ['FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator'],
        '_2736': ['FaceGearMeshSystemDeflection'],
        '_2737': ['FaceGearSetSystemDeflection'],
        '_2738': ['FaceGearSystemDeflection'],
        '_2739': ['FEPartSystemDeflection'],
        '_2740': ['FlexiblePinAssemblySystemDeflection'],
        '_2741': ['GearMeshSystemDeflection'],
        '_2742': ['GearSetSystemDeflection'],
        '_2743': ['GearSystemDeflection'],
        '_2744': ['GuideDxfModelSystemDeflection'],
        '_2745': ['HypoidGearMeshSystemDeflection'],
        '_2746': ['HypoidGearSetSystemDeflection'],
        '_2747': ['HypoidGearSystemDeflection'],
        '_2748': ['InformationForContactAtPointAlongFaceWidth'],
        '_2749': ['InterMountableComponentConnectionSystemDeflection'],
        '_2750': ['KlingelnbergCycloPalloidConicalGearMeshSystemDeflection'],
        '_2751': ['KlingelnbergCycloPalloidConicalGearSetSystemDeflection'],
        '_2752': ['KlingelnbergCycloPalloidConicalGearSystemDeflection'],
        '_2753': ['KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection'],
        '_2754': ['KlingelnbergCycloPalloidHypoidGearSetSystemDeflection'],
        '_2755': ['KlingelnbergCycloPalloidHypoidGearSystemDeflection'],
        '_2756': ['KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection'],
        '_2757': ['KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection'],
        '_2758': ['KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection'],
        '_2759': ['LoadCaseOverallEfficiencyResult'],
        '_2760': ['LoadSharingFactorReporter'],
        '_2761': ['MassDiscSystemDeflection'],
        '_2762': ['MeasurementComponentSystemDeflection'],
        '_2763': ['MeshSeparationsAtFaceWidth'],
        '_2764': ['MountableComponentSystemDeflection'],
        '_2765': ['ObservedPinStiffnessReporter'],
        '_2766': ['OilSealSystemDeflection'],
        '_2767': ['PartSystemDeflection'],
        '_2768': ['PartToPartShearCouplingConnectionSystemDeflection'],
        '_2769': ['PartToPartShearCouplingHalfSystemDeflection'],
        '_2770': ['PartToPartShearCouplingSystemDeflection'],
        '_2771': ['PlanetaryConnectionSystemDeflection'],
        '_2772': ['PlanetCarrierSystemDeflection'],
        '_2773': ['PointLoadSystemDeflection'],
        '_2774': ['PowerLoadSystemDeflection'],
        '_2775': ['PulleySystemDeflection'],
        '_2776': ['RingPinsSystemDeflection'],
        '_2777': ['RingPinsToDiscConnectionSystemDeflection'],
        '_2778': ['RingPinToDiscContactReporting'],
        '_2779': ['RollingRingAssemblySystemDeflection'],
        '_2780': ['RollingRingConnectionSystemDeflection'],
        '_2781': ['RollingRingSystemDeflection'],
        '_2782': ['RootAssemblySystemDeflection'],
        '_2783': ['ShaftHubConnectionSystemDeflection'],
        '_2784': ['ShaftSectionEndResultsSystemDeflection'],
        '_2785': ['ShaftSectionSystemDeflection'],
        '_2786': ['ShaftSystemDeflection'],
        '_2787': ['ShaftToMountableComponentConnectionSystemDeflection'],
        '_2788': ['SpecialisedAssemblySystemDeflection'],
        '_2789': ['SpiralBevelGearMeshSystemDeflection'],
        '_2790': ['SpiralBevelGearSetSystemDeflection'],
        '_2791': ['SpiralBevelGearSystemDeflection'],
        '_2792': ['SpringDamperConnectionSystemDeflection'],
        '_2793': ['SpringDamperHalfSystemDeflection'],
        '_2794': ['SpringDamperSystemDeflection'],
        '_2795': ['StraightBevelDiffGearMeshSystemDeflection'],
        '_2796': ['StraightBevelDiffGearSetSystemDeflection'],
        '_2797': ['StraightBevelDiffGearSystemDeflection'],
        '_2798': ['StraightBevelGearMeshSystemDeflection'],
        '_2799': ['StraightBevelGearSetSystemDeflection'],
        '_2800': ['StraightBevelGearSystemDeflection'],
        '_2801': ['StraightBevelPlanetGearSystemDeflection'],
        '_2802': ['StraightBevelSunGearSystemDeflection'],
        '_2803': ['SynchroniserHalfSystemDeflection'],
        '_2804': ['SynchroniserPartSystemDeflection'],
        '_2805': ['SynchroniserSleeveSystemDeflection'],
        '_2806': ['SynchroniserSystemDeflection'],
        '_2807': ['SystemDeflection'],
        '_2808': ['SystemDeflectionDrawStyle'],
        '_2809': ['SystemDeflectionOptions'],
        '_2810': ['TorqueConverterConnectionSystemDeflection'],
        '_2811': ['TorqueConverterPumpSystemDeflection'],
        '_2812': ['TorqueConverterSystemDeflection'],
        '_2813': ['TorqueConverterTurbineSystemDeflection'],
        '_2814': ['TorsionalSystemDeflection'],
        '_2815': ['TransmissionErrorResult'],
        '_2816': ['UnbalancedMassSystemDeflection'],
        '_2817': ['VirtualComponentSystemDeflection'],
        '_2818': ['WormGearMeshSystemDeflection'],
        '_2819': ['WormGearSetSystemDeflection'],
        '_2820': ['WormGearSystemDeflection'],
        '_2821': ['ZerolBevelGearMeshSystemDeflection'],
        '_2822': ['ZerolBevelGearSetSystemDeflection'],
        '_2823': ['ZerolBevelGearSystemDeflection'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
