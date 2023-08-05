"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2965 import AbstractAssemblySteadyStateSynchronousResponse
    from ._2966 import AbstractShaftOrHousingSteadyStateSynchronousResponse
    from ._2967 import AbstractShaftSteadyStateSynchronousResponse
    from ._2968 import AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse
    from ._2969 import AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse
    from ._2970 import AGMAGleasonConicalGearSetSteadyStateSynchronousResponse
    from ._2971 import AGMAGleasonConicalGearSteadyStateSynchronousResponse
    from ._2972 import AssemblySteadyStateSynchronousResponse
    from ._2973 import BearingSteadyStateSynchronousResponse
    from ._2974 import BeltConnectionSteadyStateSynchronousResponse
    from ._2975 import BeltDriveSteadyStateSynchronousResponse
    from ._2976 import BevelDifferentialGearMeshSteadyStateSynchronousResponse
    from ._2977 import BevelDifferentialGearSetSteadyStateSynchronousResponse
    from ._2978 import BevelDifferentialGearSteadyStateSynchronousResponse
    from ._2979 import BevelDifferentialPlanetGearSteadyStateSynchronousResponse
    from ._2980 import BevelDifferentialSunGearSteadyStateSynchronousResponse
    from ._2981 import BevelGearMeshSteadyStateSynchronousResponse
    from ._2982 import BevelGearSetSteadyStateSynchronousResponse
    from ._2983 import BevelGearSteadyStateSynchronousResponse
    from ._2984 import BoltedJointSteadyStateSynchronousResponse
    from ._2985 import BoltSteadyStateSynchronousResponse
    from ._2986 import ClutchConnectionSteadyStateSynchronousResponse
    from ._2987 import ClutchHalfSteadyStateSynchronousResponse
    from ._2988 import ClutchSteadyStateSynchronousResponse
    from ._2989 import CoaxialConnectionSteadyStateSynchronousResponse
    from ._2990 import ComponentSteadyStateSynchronousResponse
    from ._2991 import ConceptCouplingConnectionSteadyStateSynchronousResponse
    from ._2992 import ConceptCouplingHalfSteadyStateSynchronousResponse
    from ._2993 import ConceptCouplingSteadyStateSynchronousResponse
    from ._2994 import ConceptGearMeshSteadyStateSynchronousResponse
    from ._2995 import ConceptGearSetSteadyStateSynchronousResponse
    from ._2996 import ConceptGearSteadyStateSynchronousResponse
    from ._2997 import ConicalGearMeshSteadyStateSynchronousResponse
    from ._2998 import ConicalGearSetSteadyStateSynchronousResponse
    from ._2999 import ConicalGearSteadyStateSynchronousResponse
    from ._3000 import ConnectionSteadyStateSynchronousResponse
    from ._3001 import ConnectorSteadyStateSynchronousResponse
    from ._3002 import CouplingConnectionSteadyStateSynchronousResponse
    from ._3003 import CouplingHalfSteadyStateSynchronousResponse
    from ._3004 import CouplingSteadyStateSynchronousResponse
    from ._3005 import CVTBeltConnectionSteadyStateSynchronousResponse
    from ._3006 import CVTPulleySteadyStateSynchronousResponse
    from ._3007 import CVTSteadyStateSynchronousResponse
    from ._3008 import CycloidalAssemblySteadyStateSynchronousResponse
    from ._3009 import CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse
    from ._3010 import CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse
    from ._3011 import CycloidalDiscSteadyStateSynchronousResponse
    from ._3012 import CylindricalGearMeshSteadyStateSynchronousResponse
    from ._3013 import CylindricalGearSetSteadyStateSynchronousResponse
    from ._3014 import CylindricalGearSteadyStateSynchronousResponse
    from ._3015 import CylindricalPlanetGearSteadyStateSynchronousResponse
    from ._3016 import DatumSteadyStateSynchronousResponse
    from ._3017 import DynamicModelForSteadyStateSynchronousResponse
    from ._3018 import ExternalCADModelSteadyStateSynchronousResponse
    from ._3019 import FaceGearMeshSteadyStateSynchronousResponse
    from ._3020 import FaceGearSetSteadyStateSynchronousResponse
    from ._3021 import FaceGearSteadyStateSynchronousResponse
    from ._3022 import FEPartSteadyStateSynchronousResponse
    from ._3023 import FlexiblePinAssemblySteadyStateSynchronousResponse
    from ._3024 import GearMeshSteadyStateSynchronousResponse
    from ._3025 import GearSetSteadyStateSynchronousResponse
    from ._3026 import GearSteadyStateSynchronousResponse
    from ._3027 import GuideDxfModelSteadyStateSynchronousResponse
    from ._3028 import HypoidGearMeshSteadyStateSynchronousResponse
    from ._3029 import HypoidGearSetSteadyStateSynchronousResponse
    from ._3030 import HypoidGearSteadyStateSynchronousResponse
    from ._3031 import InterMountableComponentConnectionSteadyStateSynchronousResponse
    from ._3032 import KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse
    from ._3033 import KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse
    from ._3034 import KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse
    from ._3035 import KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse
    from ._3036 import KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse
    from ._3037 import KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse
    from ._3038 import KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse
    from ._3039 import KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse
    from ._3040 import KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse
    from ._3041 import MassDiscSteadyStateSynchronousResponse
    from ._3042 import MeasurementComponentSteadyStateSynchronousResponse
    from ._3043 import MountableComponentSteadyStateSynchronousResponse
    from ._3044 import OilSealSteadyStateSynchronousResponse
    from ._3045 import PartSteadyStateSynchronousResponse
    from ._3046 import PartToPartShearCouplingConnectionSteadyStateSynchronousResponse
    from ._3047 import PartToPartShearCouplingHalfSteadyStateSynchronousResponse
    from ._3048 import PartToPartShearCouplingSteadyStateSynchronousResponse
    from ._3049 import PlanetaryConnectionSteadyStateSynchronousResponse
    from ._3050 import PlanetaryGearSetSteadyStateSynchronousResponse
    from ._3051 import PlanetCarrierSteadyStateSynchronousResponse
    from ._3052 import PointLoadSteadyStateSynchronousResponse
    from ._3053 import PowerLoadSteadyStateSynchronousResponse
    from ._3054 import PulleySteadyStateSynchronousResponse
    from ._3055 import RingPinsSteadyStateSynchronousResponse
    from ._3056 import RingPinsToDiscConnectionSteadyStateSynchronousResponse
    from ._3057 import RollingRingAssemblySteadyStateSynchronousResponse
    from ._3058 import RollingRingConnectionSteadyStateSynchronousResponse
    from ._3059 import RollingRingSteadyStateSynchronousResponse
    from ._3060 import RootAssemblySteadyStateSynchronousResponse
    from ._3061 import ShaftHubConnectionSteadyStateSynchronousResponse
    from ._3062 import ShaftSteadyStateSynchronousResponse
    from ._3063 import ShaftToMountableComponentConnectionSteadyStateSynchronousResponse
    from ._3064 import SpecialisedAssemblySteadyStateSynchronousResponse
    from ._3065 import SpiralBevelGearMeshSteadyStateSynchronousResponse
    from ._3066 import SpiralBevelGearSetSteadyStateSynchronousResponse
    from ._3067 import SpiralBevelGearSteadyStateSynchronousResponse
    from ._3068 import SpringDamperConnectionSteadyStateSynchronousResponse
    from ._3069 import SpringDamperHalfSteadyStateSynchronousResponse
    from ._3070 import SpringDamperSteadyStateSynchronousResponse
    from ._3071 import SteadyStateSynchronousResponse
    from ._3072 import SteadyStateSynchronousResponseDrawStyle
    from ._3073 import SteadyStateSynchronousResponseOptions
    from ._3074 import StraightBevelDiffGearMeshSteadyStateSynchronousResponse
    from ._3075 import StraightBevelDiffGearSetSteadyStateSynchronousResponse
    from ._3076 import StraightBevelDiffGearSteadyStateSynchronousResponse
    from ._3077 import StraightBevelGearMeshSteadyStateSynchronousResponse
    from ._3078 import StraightBevelGearSetSteadyStateSynchronousResponse
    from ._3079 import StraightBevelGearSteadyStateSynchronousResponse
    from ._3080 import StraightBevelPlanetGearSteadyStateSynchronousResponse
    from ._3081 import StraightBevelSunGearSteadyStateSynchronousResponse
    from ._3082 import SynchroniserHalfSteadyStateSynchronousResponse
    from ._3083 import SynchroniserPartSteadyStateSynchronousResponse
    from ._3084 import SynchroniserSleeveSteadyStateSynchronousResponse
    from ._3085 import SynchroniserSteadyStateSynchronousResponse
    from ._3086 import TorqueConverterConnectionSteadyStateSynchronousResponse
    from ._3087 import TorqueConverterPumpSteadyStateSynchronousResponse
    from ._3088 import TorqueConverterSteadyStateSynchronousResponse
    from ._3089 import TorqueConverterTurbineSteadyStateSynchronousResponse
    from ._3090 import UnbalancedMassSteadyStateSynchronousResponse
    from ._3091 import VirtualComponentSteadyStateSynchronousResponse
    from ._3092 import WormGearMeshSteadyStateSynchronousResponse
    from ._3093 import WormGearSetSteadyStateSynchronousResponse
    from ._3094 import WormGearSteadyStateSynchronousResponse
    from ._3095 import ZerolBevelGearMeshSteadyStateSynchronousResponse
    from ._3096 import ZerolBevelGearSetSteadyStateSynchronousResponse
    from ._3097 import ZerolBevelGearSteadyStateSynchronousResponse
else:
    import_structure = {
        '_2965': ['AbstractAssemblySteadyStateSynchronousResponse'],
        '_2966': ['AbstractShaftOrHousingSteadyStateSynchronousResponse'],
        '_2967': ['AbstractShaftSteadyStateSynchronousResponse'],
        '_2968': ['AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse'],
        '_2969': ['AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse'],
        '_2970': ['AGMAGleasonConicalGearSetSteadyStateSynchronousResponse'],
        '_2971': ['AGMAGleasonConicalGearSteadyStateSynchronousResponse'],
        '_2972': ['AssemblySteadyStateSynchronousResponse'],
        '_2973': ['BearingSteadyStateSynchronousResponse'],
        '_2974': ['BeltConnectionSteadyStateSynchronousResponse'],
        '_2975': ['BeltDriveSteadyStateSynchronousResponse'],
        '_2976': ['BevelDifferentialGearMeshSteadyStateSynchronousResponse'],
        '_2977': ['BevelDifferentialGearSetSteadyStateSynchronousResponse'],
        '_2978': ['BevelDifferentialGearSteadyStateSynchronousResponse'],
        '_2979': ['BevelDifferentialPlanetGearSteadyStateSynchronousResponse'],
        '_2980': ['BevelDifferentialSunGearSteadyStateSynchronousResponse'],
        '_2981': ['BevelGearMeshSteadyStateSynchronousResponse'],
        '_2982': ['BevelGearSetSteadyStateSynchronousResponse'],
        '_2983': ['BevelGearSteadyStateSynchronousResponse'],
        '_2984': ['BoltedJointSteadyStateSynchronousResponse'],
        '_2985': ['BoltSteadyStateSynchronousResponse'],
        '_2986': ['ClutchConnectionSteadyStateSynchronousResponse'],
        '_2987': ['ClutchHalfSteadyStateSynchronousResponse'],
        '_2988': ['ClutchSteadyStateSynchronousResponse'],
        '_2989': ['CoaxialConnectionSteadyStateSynchronousResponse'],
        '_2990': ['ComponentSteadyStateSynchronousResponse'],
        '_2991': ['ConceptCouplingConnectionSteadyStateSynchronousResponse'],
        '_2992': ['ConceptCouplingHalfSteadyStateSynchronousResponse'],
        '_2993': ['ConceptCouplingSteadyStateSynchronousResponse'],
        '_2994': ['ConceptGearMeshSteadyStateSynchronousResponse'],
        '_2995': ['ConceptGearSetSteadyStateSynchronousResponse'],
        '_2996': ['ConceptGearSteadyStateSynchronousResponse'],
        '_2997': ['ConicalGearMeshSteadyStateSynchronousResponse'],
        '_2998': ['ConicalGearSetSteadyStateSynchronousResponse'],
        '_2999': ['ConicalGearSteadyStateSynchronousResponse'],
        '_3000': ['ConnectionSteadyStateSynchronousResponse'],
        '_3001': ['ConnectorSteadyStateSynchronousResponse'],
        '_3002': ['CouplingConnectionSteadyStateSynchronousResponse'],
        '_3003': ['CouplingHalfSteadyStateSynchronousResponse'],
        '_3004': ['CouplingSteadyStateSynchronousResponse'],
        '_3005': ['CVTBeltConnectionSteadyStateSynchronousResponse'],
        '_3006': ['CVTPulleySteadyStateSynchronousResponse'],
        '_3007': ['CVTSteadyStateSynchronousResponse'],
        '_3008': ['CycloidalAssemblySteadyStateSynchronousResponse'],
        '_3009': ['CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse'],
        '_3010': ['CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse'],
        '_3011': ['CycloidalDiscSteadyStateSynchronousResponse'],
        '_3012': ['CylindricalGearMeshSteadyStateSynchronousResponse'],
        '_3013': ['CylindricalGearSetSteadyStateSynchronousResponse'],
        '_3014': ['CylindricalGearSteadyStateSynchronousResponse'],
        '_3015': ['CylindricalPlanetGearSteadyStateSynchronousResponse'],
        '_3016': ['DatumSteadyStateSynchronousResponse'],
        '_3017': ['DynamicModelForSteadyStateSynchronousResponse'],
        '_3018': ['ExternalCADModelSteadyStateSynchronousResponse'],
        '_3019': ['FaceGearMeshSteadyStateSynchronousResponse'],
        '_3020': ['FaceGearSetSteadyStateSynchronousResponse'],
        '_3021': ['FaceGearSteadyStateSynchronousResponse'],
        '_3022': ['FEPartSteadyStateSynchronousResponse'],
        '_3023': ['FlexiblePinAssemblySteadyStateSynchronousResponse'],
        '_3024': ['GearMeshSteadyStateSynchronousResponse'],
        '_3025': ['GearSetSteadyStateSynchronousResponse'],
        '_3026': ['GearSteadyStateSynchronousResponse'],
        '_3027': ['GuideDxfModelSteadyStateSynchronousResponse'],
        '_3028': ['HypoidGearMeshSteadyStateSynchronousResponse'],
        '_3029': ['HypoidGearSetSteadyStateSynchronousResponse'],
        '_3030': ['HypoidGearSteadyStateSynchronousResponse'],
        '_3031': ['InterMountableComponentConnectionSteadyStateSynchronousResponse'],
        '_3032': ['KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse'],
        '_3033': ['KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse'],
        '_3034': ['KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse'],
        '_3035': ['KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse'],
        '_3036': ['KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse'],
        '_3037': ['KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse'],
        '_3038': ['KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse'],
        '_3039': ['KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse'],
        '_3040': ['KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse'],
        '_3041': ['MassDiscSteadyStateSynchronousResponse'],
        '_3042': ['MeasurementComponentSteadyStateSynchronousResponse'],
        '_3043': ['MountableComponentSteadyStateSynchronousResponse'],
        '_3044': ['OilSealSteadyStateSynchronousResponse'],
        '_3045': ['PartSteadyStateSynchronousResponse'],
        '_3046': ['PartToPartShearCouplingConnectionSteadyStateSynchronousResponse'],
        '_3047': ['PartToPartShearCouplingHalfSteadyStateSynchronousResponse'],
        '_3048': ['PartToPartShearCouplingSteadyStateSynchronousResponse'],
        '_3049': ['PlanetaryConnectionSteadyStateSynchronousResponse'],
        '_3050': ['PlanetaryGearSetSteadyStateSynchronousResponse'],
        '_3051': ['PlanetCarrierSteadyStateSynchronousResponse'],
        '_3052': ['PointLoadSteadyStateSynchronousResponse'],
        '_3053': ['PowerLoadSteadyStateSynchronousResponse'],
        '_3054': ['PulleySteadyStateSynchronousResponse'],
        '_3055': ['RingPinsSteadyStateSynchronousResponse'],
        '_3056': ['RingPinsToDiscConnectionSteadyStateSynchronousResponse'],
        '_3057': ['RollingRingAssemblySteadyStateSynchronousResponse'],
        '_3058': ['RollingRingConnectionSteadyStateSynchronousResponse'],
        '_3059': ['RollingRingSteadyStateSynchronousResponse'],
        '_3060': ['RootAssemblySteadyStateSynchronousResponse'],
        '_3061': ['ShaftHubConnectionSteadyStateSynchronousResponse'],
        '_3062': ['ShaftSteadyStateSynchronousResponse'],
        '_3063': ['ShaftToMountableComponentConnectionSteadyStateSynchronousResponse'],
        '_3064': ['SpecialisedAssemblySteadyStateSynchronousResponse'],
        '_3065': ['SpiralBevelGearMeshSteadyStateSynchronousResponse'],
        '_3066': ['SpiralBevelGearSetSteadyStateSynchronousResponse'],
        '_3067': ['SpiralBevelGearSteadyStateSynchronousResponse'],
        '_3068': ['SpringDamperConnectionSteadyStateSynchronousResponse'],
        '_3069': ['SpringDamperHalfSteadyStateSynchronousResponse'],
        '_3070': ['SpringDamperSteadyStateSynchronousResponse'],
        '_3071': ['SteadyStateSynchronousResponse'],
        '_3072': ['SteadyStateSynchronousResponseDrawStyle'],
        '_3073': ['SteadyStateSynchronousResponseOptions'],
        '_3074': ['StraightBevelDiffGearMeshSteadyStateSynchronousResponse'],
        '_3075': ['StraightBevelDiffGearSetSteadyStateSynchronousResponse'],
        '_3076': ['StraightBevelDiffGearSteadyStateSynchronousResponse'],
        '_3077': ['StraightBevelGearMeshSteadyStateSynchronousResponse'],
        '_3078': ['StraightBevelGearSetSteadyStateSynchronousResponse'],
        '_3079': ['StraightBevelGearSteadyStateSynchronousResponse'],
        '_3080': ['StraightBevelPlanetGearSteadyStateSynchronousResponse'],
        '_3081': ['StraightBevelSunGearSteadyStateSynchronousResponse'],
        '_3082': ['SynchroniserHalfSteadyStateSynchronousResponse'],
        '_3083': ['SynchroniserPartSteadyStateSynchronousResponse'],
        '_3084': ['SynchroniserSleeveSteadyStateSynchronousResponse'],
        '_3085': ['SynchroniserSteadyStateSynchronousResponse'],
        '_3086': ['TorqueConverterConnectionSteadyStateSynchronousResponse'],
        '_3087': ['TorqueConverterPumpSteadyStateSynchronousResponse'],
        '_3088': ['TorqueConverterSteadyStateSynchronousResponse'],
        '_3089': ['TorqueConverterTurbineSteadyStateSynchronousResponse'],
        '_3090': ['UnbalancedMassSteadyStateSynchronousResponse'],
        '_3091': ['VirtualComponentSteadyStateSynchronousResponse'],
        '_3092': ['WormGearMeshSteadyStateSynchronousResponse'],
        '_3093': ['WormGearSetSteadyStateSynchronousResponse'],
        '_3094': ['WormGearSteadyStateSynchronousResponse'],
        '_3095': ['ZerolBevelGearMeshSteadyStateSynchronousResponse'],
        '_3096': ['ZerolBevelGearSetSteadyStateSynchronousResponse'],
        '_3097': ['ZerolBevelGearSteadyStateSynchronousResponse'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
