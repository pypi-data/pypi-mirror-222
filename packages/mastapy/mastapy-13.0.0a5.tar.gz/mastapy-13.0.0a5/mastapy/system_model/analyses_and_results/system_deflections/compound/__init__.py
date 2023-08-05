"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2833 import AbstractAssemblyCompoundSystemDeflection
    from ._2834 import AbstractShaftCompoundSystemDeflection
    from ._2835 import AbstractShaftOrHousingCompoundSystemDeflection
    from ._2836 import AbstractShaftToMountableComponentConnectionCompoundSystemDeflection
    from ._2837 import AGMAGleasonConicalGearCompoundSystemDeflection
    from ._2838 import AGMAGleasonConicalGearMeshCompoundSystemDeflection
    from ._2839 import AGMAGleasonConicalGearSetCompoundSystemDeflection
    from ._2840 import AssemblyCompoundSystemDeflection
    from ._2841 import BearingCompoundSystemDeflection
    from ._2842 import BeltConnectionCompoundSystemDeflection
    from ._2843 import BeltDriveCompoundSystemDeflection
    from ._2844 import BevelDifferentialGearCompoundSystemDeflection
    from ._2845 import BevelDifferentialGearMeshCompoundSystemDeflection
    from ._2846 import BevelDifferentialGearSetCompoundSystemDeflection
    from ._2847 import BevelDifferentialPlanetGearCompoundSystemDeflection
    from ._2848 import BevelDifferentialSunGearCompoundSystemDeflection
    from ._2849 import BevelGearCompoundSystemDeflection
    from ._2850 import BevelGearMeshCompoundSystemDeflection
    from ._2851 import BevelGearSetCompoundSystemDeflection
    from ._2852 import BoltCompoundSystemDeflection
    from ._2853 import BoltedJointCompoundSystemDeflection
    from ._2854 import ClutchCompoundSystemDeflection
    from ._2855 import ClutchConnectionCompoundSystemDeflection
    from ._2856 import ClutchHalfCompoundSystemDeflection
    from ._2857 import CoaxialConnectionCompoundSystemDeflection
    from ._2858 import ComponentCompoundSystemDeflection
    from ._2859 import ConceptCouplingCompoundSystemDeflection
    from ._2860 import ConceptCouplingConnectionCompoundSystemDeflection
    from ._2861 import ConceptCouplingHalfCompoundSystemDeflection
    from ._2862 import ConceptGearCompoundSystemDeflection
    from ._2863 import ConceptGearMeshCompoundSystemDeflection
    from ._2864 import ConceptGearSetCompoundSystemDeflection
    from ._2865 import ConicalGearCompoundSystemDeflection
    from ._2866 import ConicalGearMeshCompoundSystemDeflection
    from ._2867 import ConicalGearSetCompoundSystemDeflection
    from ._2868 import ConnectionCompoundSystemDeflection
    from ._2869 import ConnectorCompoundSystemDeflection
    from ._2870 import CouplingCompoundSystemDeflection
    from ._2871 import CouplingConnectionCompoundSystemDeflection
    from ._2872 import CouplingHalfCompoundSystemDeflection
    from ._2873 import CVTBeltConnectionCompoundSystemDeflection
    from ._2874 import CVTCompoundSystemDeflection
    from ._2875 import CVTPulleyCompoundSystemDeflection
    from ._2876 import CycloidalAssemblyCompoundSystemDeflection
    from ._2877 import CycloidalDiscCentralBearingConnectionCompoundSystemDeflection
    from ._2878 import CycloidalDiscCompoundSystemDeflection
    from ._2879 import CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection
    from ._2880 import CylindricalGearCompoundSystemDeflection
    from ._2881 import CylindricalGearMeshCompoundSystemDeflection
    from ._2882 import CylindricalGearSetCompoundSystemDeflection
    from ._2883 import CylindricalPlanetGearCompoundSystemDeflection
    from ._2884 import DatumCompoundSystemDeflection
    from ._2885 import DutyCycleEfficiencyResults
    from ._2886 import ExternalCADModelCompoundSystemDeflection
    from ._2887 import FaceGearCompoundSystemDeflection
    from ._2888 import FaceGearMeshCompoundSystemDeflection
    from ._2889 import FaceGearSetCompoundSystemDeflection
    from ._2890 import FEPartCompoundSystemDeflection
    from ._2891 import FlexiblePinAssemblyCompoundSystemDeflection
    from ._2892 import GearCompoundSystemDeflection
    from ._2893 import GearMeshCompoundSystemDeflection
    from ._2894 import GearSetCompoundSystemDeflection
    from ._2895 import GuideDxfModelCompoundSystemDeflection
    from ._2896 import HypoidGearCompoundSystemDeflection
    from ._2897 import HypoidGearMeshCompoundSystemDeflection
    from ._2898 import HypoidGearSetCompoundSystemDeflection
    from ._2899 import InterMountableComponentConnectionCompoundSystemDeflection
    from ._2900 import KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
    from ._2901 import KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection
    from ._2902 import KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
    from ._2903 import KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
    from ._2904 import KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection
    from ._2905 import KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
    from ._2906 import KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
    from ._2907 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection
    from ._2908 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection
    from ._2909 import MassDiscCompoundSystemDeflection
    from ._2910 import MeasurementComponentCompoundSystemDeflection
    from ._2911 import MountableComponentCompoundSystemDeflection
    from ._2912 import OilSealCompoundSystemDeflection
    from ._2913 import PartCompoundSystemDeflection
    from ._2914 import PartToPartShearCouplingCompoundSystemDeflection
    from ._2915 import PartToPartShearCouplingConnectionCompoundSystemDeflection
    from ._2916 import PartToPartShearCouplingHalfCompoundSystemDeflection
    from ._2917 import PlanetaryConnectionCompoundSystemDeflection
    from ._2918 import PlanetaryGearSetCompoundSystemDeflection
    from ._2919 import PlanetCarrierCompoundSystemDeflection
    from ._2920 import PointLoadCompoundSystemDeflection
    from ._2921 import PowerLoadCompoundSystemDeflection
    from ._2922 import PulleyCompoundSystemDeflection
    from ._2923 import RingPinsCompoundSystemDeflection
    from ._2924 import RingPinsToDiscConnectionCompoundSystemDeflection
    from ._2925 import RollingRingAssemblyCompoundSystemDeflection
    from ._2926 import RollingRingCompoundSystemDeflection
    from ._2927 import RollingRingConnectionCompoundSystemDeflection
    from ._2928 import RootAssemblyCompoundSystemDeflection
    from ._2929 import ShaftCompoundSystemDeflection
    from ._2930 import ShaftDutyCycleSystemDeflection
    from ._2931 import ShaftHubConnectionCompoundSystemDeflection
    from ._2932 import ShaftToMountableComponentConnectionCompoundSystemDeflection
    from ._2933 import SpecialisedAssemblyCompoundSystemDeflection
    from ._2934 import SpiralBevelGearCompoundSystemDeflection
    from ._2935 import SpiralBevelGearMeshCompoundSystemDeflection
    from ._2936 import SpiralBevelGearSetCompoundSystemDeflection
    from ._2937 import SpringDamperCompoundSystemDeflection
    from ._2938 import SpringDamperConnectionCompoundSystemDeflection
    from ._2939 import SpringDamperHalfCompoundSystemDeflection
    from ._2940 import StraightBevelDiffGearCompoundSystemDeflection
    from ._2941 import StraightBevelDiffGearMeshCompoundSystemDeflection
    from ._2942 import StraightBevelDiffGearSetCompoundSystemDeflection
    from ._2943 import StraightBevelGearCompoundSystemDeflection
    from ._2944 import StraightBevelGearMeshCompoundSystemDeflection
    from ._2945 import StraightBevelGearSetCompoundSystemDeflection
    from ._2946 import StraightBevelPlanetGearCompoundSystemDeflection
    from ._2947 import StraightBevelSunGearCompoundSystemDeflection
    from ._2948 import SynchroniserCompoundSystemDeflection
    from ._2949 import SynchroniserHalfCompoundSystemDeflection
    from ._2950 import SynchroniserPartCompoundSystemDeflection
    from ._2951 import SynchroniserSleeveCompoundSystemDeflection
    from ._2952 import TorqueConverterCompoundSystemDeflection
    from ._2953 import TorqueConverterConnectionCompoundSystemDeflection
    from ._2954 import TorqueConverterPumpCompoundSystemDeflection
    from ._2955 import TorqueConverterTurbineCompoundSystemDeflection
    from ._2956 import UnbalancedMassCompoundSystemDeflection
    from ._2957 import VirtualComponentCompoundSystemDeflection
    from ._2958 import WormGearCompoundSystemDeflection
    from ._2959 import WormGearMeshCompoundSystemDeflection
    from ._2960 import WormGearSetCompoundSystemDeflection
    from ._2961 import ZerolBevelGearCompoundSystemDeflection
    from ._2962 import ZerolBevelGearMeshCompoundSystemDeflection
    from ._2963 import ZerolBevelGearSetCompoundSystemDeflection
else:
    import_structure = {
        '_2833': ['AbstractAssemblyCompoundSystemDeflection'],
        '_2834': ['AbstractShaftCompoundSystemDeflection'],
        '_2835': ['AbstractShaftOrHousingCompoundSystemDeflection'],
        '_2836': ['AbstractShaftToMountableComponentConnectionCompoundSystemDeflection'],
        '_2837': ['AGMAGleasonConicalGearCompoundSystemDeflection'],
        '_2838': ['AGMAGleasonConicalGearMeshCompoundSystemDeflection'],
        '_2839': ['AGMAGleasonConicalGearSetCompoundSystemDeflection'],
        '_2840': ['AssemblyCompoundSystemDeflection'],
        '_2841': ['BearingCompoundSystemDeflection'],
        '_2842': ['BeltConnectionCompoundSystemDeflection'],
        '_2843': ['BeltDriveCompoundSystemDeflection'],
        '_2844': ['BevelDifferentialGearCompoundSystemDeflection'],
        '_2845': ['BevelDifferentialGearMeshCompoundSystemDeflection'],
        '_2846': ['BevelDifferentialGearSetCompoundSystemDeflection'],
        '_2847': ['BevelDifferentialPlanetGearCompoundSystemDeflection'],
        '_2848': ['BevelDifferentialSunGearCompoundSystemDeflection'],
        '_2849': ['BevelGearCompoundSystemDeflection'],
        '_2850': ['BevelGearMeshCompoundSystemDeflection'],
        '_2851': ['BevelGearSetCompoundSystemDeflection'],
        '_2852': ['BoltCompoundSystemDeflection'],
        '_2853': ['BoltedJointCompoundSystemDeflection'],
        '_2854': ['ClutchCompoundSystemDeflection'],
        '_2855': ['ClutchConnectionCompoundSystemDeflection'],
        '_2856': ['ClutchHalfCompoundSystemDeflection'],
        '_2857': ['CoaxialConnectionCompoundSystemDeflection'],
        '_2858': ['ComponentCompoundSystemDeflection'],
        '_2859': ['ConceptCouplingCompoundSystemDeflection'],
        '_2860': ['ConceptCouplingConnectionCompoundSystemDeflection'],
        '_2861': ['ConceptCouplingHalfCompoundSystemDeflection'],
        '_2862': ['ConceptGearCompoundSystemDeflection'],
        '_2863': ['ConceptGearMeshCompoundSystemDeflection'],
        '_2864': ['ConceptGearSetCompoundSystemDeflection'],
        '_2865': ['ConicalGearCompoundSystemDeflection'],
        '_2866': ['ConicalGearMeshCompoundSystemDeflection'],
        '_2867': ['ConicalGearSetCompoundSystemDeflection'],
        '_2868': ['ConnectionCompoundSystemDeflection'],
        '_2869': ['ConnectorCompoundSystemDeflection'],
        '_2870': ['CouplingCompoundSystemDeflection'],
        '_2871': ['CouplingConnectionCompoundSystemDeflection'],
        '_2872': ['CouplingHalfCompoundSystemDeflection'],
        '_2873': ['CVTBeltConnectionCompoundSystemDeflection'],
        '_2874': ['CVTCompoundSystemDeflection'],
        '_2875': ['CVTPulleyCompoundSystemDeflection'],
        '_2876': ['CycloidalAssemblyCompoundSystemDeflection'],
        '_2877': ['CycloidalDiscCentralBearingConnectionCompoundSystemDeflection'],
        '_2878': ['CycloidalDiscCompoundSystemDeflection'],
        '_2879': ['CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection'],
        '_2880': ['CylindricalGearCompoundSystemDeflection'],
        '_2881': ['CylindricalGearMeshCompoundSystemDeflection'],
        '_2882': ['CylindricalGearSetCompoundSystemDeflection'],
        '_2883': ['CylindricalPlanetGearCompoundSystemDeflection'],
        '_2884': ['DatumCompoundSystemDeflection'],
        '_2885': ['DutyCycleEfficiencyResults'],
        '_2886': ['ExternalCADModelCompoundSystemDeflection'],
        '_2887': ['FaceGearCompoundSystemDeflection'],
        '_2888': ['FaceGearMeshCompoundSystemDeflection'],
        '_2889': ['FaceGearSetCompoundSystemDeflection'],
        '_2890': ['FEPartCompoundSystemDeflection'],
        '_2891': ['FlexiblePinAssemblyCompoundSystemDeflection'],
        '_2892': ['GearCompoundSystemDeflection'],
        '_2893': ['GearMeshCompoundSystemDeflection'],
        '_2894': ['GearSetCompoundSystemDeflection'],
        '_2895': ['GuideDxfModelCompoundSystemDeflection'],
        '_2896': ['HypoidGearCompoundSystemDeflection'],
        '_2897': ['HypoidGearMeshCompoundSystemDeflection'],
        '_2898': ['HypoidGearSetCompoundSystemDeflection'],
        '_2899': ['InterMountableComponentConnectionCompoundSystemDeflection'],
        '_2900': ['KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection'],
        '_2901': ['KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection'],
        '_2902': ['KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection'],
        '_2903': ['KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection'],
        '_2904': ['KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection'],
        '_2905': ['KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection'],
        '_2906': ['KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection'],
        '_2907': ['KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection'],
        '_2908': ['KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection'],
        '_2909': ['MassDiscCompoundSystemDeflection'],
        '_2910': ['MeasurementComponentCompoundSystemDeflection'],
        '_2911': ['MountableComponentCompoundSystemDeflection'],
        '_2912': ['OilSealCompoundSystemDeflection'],
        '_2913': ['PartCompoundSystemDeflection'],
        '_2914': ['PartToPartShearCouplingCompoundSystemDeflection'],
        '_2915': ['PartToPartShearCouplingConnectionCompoundSystemDeflection'],
        '_2916': ['PartToPartShearCouplingHalfCompoundSystemDeflection'],
        '_2917': ['PlanetaryConnectionCompoundSystemDeflection'],
        '_2918': ['PlanetaryGearSetCompoundSystemDeflection'],
        '_2919': ['PlanetCarrierCompoundSystemDeflection'],
        '_2920': ['PointLoadCompoundSystemDeflection'],
        '_2921': ['PowerLoadCompoundSystemDeflection'],
        '_2922': ['PulleyCompoundSystemDeflection'],
        '_2923': ['RingPinsCompoundSystemDeflection'],
        '_2924': ['RingPinsToDiscConnectionCompoundSystemDeflection'],
        '_2925': ['RollingRingAssemblyCompoundSystemDeflection'],
        '_2926': ['RollingRingCompoundSystemDeflection'],
        '_2927': ['RollingRingConnectionCompoundSystemDeflection'],
        '_2928': ['RootAssemblyCompoundSystemDeflection'],
        '_2929': ['ShaftCompoundSystemDeflection'],
        '_2930': ['ShaftDutyCycleSystemDeflection'],
        '_2931': ['ShaftHubConnectionCompoundSystemDeflection'],
        '_2932': ['ShaftToMountableComponentConnectionCompoundSystemDeflection'],
        '_2933': ['SpecialisedAssemblyCompoundSystemDeflection'],
        '_2934': ['SpiralBevelGearCompoundSystemDeflection'],
        '_2935': ['SpiralBevelGearMeshCompoundSystemDeflection'],
        '_2936': ['SpiralBevelGearSetCompoundSystemDeflection'],
        '_2937': ['SpringDamperCompoundSystemDeflection'],
        '_2938': ['SpringDamperConnectionCompoundSystemDeflection'],
        '_2939': ['SpringDamperHalfCompoundSystemDeflection'],
        '_2940': ['StraightBevelDiffGearCompoundSystemDeflection'],
        '_2941': ['StraightBevelDiffGearMeshCompoundSystemDeflection'],
        '_2942': ['StraightBevelDiffGearSetCompoundSystemDeflection'],
        '_2943': ['StraightBevelGearCompoundSystemDeflection'],
        '_2944': ['StraightBevelGearMeshCompoundSystemDeflection'],
        '_2945': ['StraightBevelGearSetCompoundSystemDeflection'],
        '_2946': ['StraightBevelPlanetGearCompoundSystemDeflection'],
        '_2947': ['StraightBevelSunGearCompoundSystemDeflection'],
        '_2948': ['SynchroniserCompoundSystemDeflection'],
        '_2949': ['SynchroniserHalfCompoundSystemDeflection'],
        '_2950': ['SynchroniserPartCompoundSystemDeflection'],
        '_2951': ['SynchroniserSleeveCompoundSystemDeflection'],
        '_2952': ['TorqueConverterCompoundSystemDeflection'],
        '_2953': ['TorqueConverterConnectionCompoundSystemDeflection'],
        '_2954': ['TorqueConverterPumpCompoundSystemDeflection'],
        '_2955': ['TorqueConverterTurbineCompoundSystemDeflection'],
        '_2956': ['UnbalancedMassCompoundSystemDeflection'],
        '_2957': ['VirtualComponentCompoundSystemDeflection'],
        '_2958': ['WormGearCompoundSystemDeflection'],
        '_2959': ['WormGearMeshCompoundSystemDeflection'],
        '_2960': ['WormGearSetCompoundSystemDeflection'],
        '_2961': ['ZerolBevelGearCompoundSystemDeflection'],
        '_2962': ['ZerolBevelGearMeshCompoundSystemDeflection'],
        '_2963': ['ZerolBevelGearSetCompoundSystemDeflection'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
