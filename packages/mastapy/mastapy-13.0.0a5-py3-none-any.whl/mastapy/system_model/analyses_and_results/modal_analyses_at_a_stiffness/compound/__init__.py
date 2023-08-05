"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4963 import AbstractAssemblyCompoundModalAnalysisAtAStiffness
    from ._4964 import AbstractShaftCompoundModalAnalysisAtAStiffness
    from ._4965 import AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness
    from ._4966 import AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
    from ._4967 import AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
    from ._4968 import AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness
    from ._4969 import AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
    from ._4970 import AssemblyCompoundModalAnalysisAtAStiffness
    from ._4971 import BearingCompoundModalAnalysisAtAStiffness
    from ._4972 import BeltConnectionCompoundModalAnalysisAtAStiffness
    from ._4973 import BeltDriveCompoundModalAnalysisAtAStiffness
    from ._4974 import BevelDifferentialGearCompoundModalAnalysisAtAStiffness
    from ._4975 import BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness
    from ._4976 import BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness
    from ._4977 import BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness
    from ._4978 import BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness
    from ._4979 import BevelGearCompoundModalAnalysisAtAStiffness
    from ._4980 import BevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._4981 import BevelGearSetCompoundModalAnalysisAtAStiffness
    from ._4982 import BoltCompoundModalAnalysisAtAStiffness
    from ._4983 import BoltedJointCompoundModalAnalysisAtAStiffness
    from ._4984 import ClutchCompoundModalAnalysisAtAStiffness
    from ._4985 import ClutchConnectionCompoundModalAnalysisAtAStiffness
    from ._4986 import ClutchHalfCompoundModalAnalysisAtAStiffness
    from ._4987 import CoaxialConnectionCompoundModalAnalysisAtAStiffness
    from ._4988 import ComponentCompoundModalAnalysisAtAStiffness
    from ._4989 import ConceptCouplingCompoundModalAnalysisAtAStiffness
    from ._4990 import ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness
    from ._4991 import ConceptCouplingHalfCompoundModalAnalysisAtAStiffness
    from ._4992 import ConceptGearCompoundModalAnalysisAtAStiffness
    from ._4993 import ConceptGearMeshCompoundModalAnalysisAtAStiffness
    from ._4994 import ConceptGearSetCompoundModalAnalysisAtAStiffness
    from ._4995 import ConicalGearCompoundModalAnalysisAtAStiffness
    from ._4996 import ConicalGearMeshCompoundModalAnalysisAtAStiffness
    from ._4997 import ConicalGearSetCompoundModalAnalysisAtAStiffness
    from ._4998 import ConnectionCompoundModalAnalysisAtAStiffness
    from ._4999 import ConnectorCompoundModalAnalysisAtAStiffness
    from ._5000 import CouplingCompoundModalAnalysisAtAStiffness
    from ._5001 import CouplingConnectionCompoundModalAnalysisAtAStiffness
    from ._5002 import CouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5003 import CVTBeltConnectionCompoundModalAnalysisAtAStiffness
    from ._5004 import CVTCompoundModalAnalysisAtAStiffness
    from ._5005 import CVTPulleyCompoundModalAnalysisAtAStiffness
    from ._5006 import CycloidalAssemblyCompoundModalAnalysisAtAStiffness
    from ._5007 import CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness
    from ._5008 import CycloidalDiscCompoundModalAnalysisAtAStiffness
    from ._5009 import CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness
    from ._5010 import CylindricalGearCompoundModalAnalysisAtAStiffness
    from ._5011 import CylindricalGearMeshCompoundModalAnalysisAtAStiffness
    from ._5012 import CylindricalGearSetCompoundModalAnalysisAtAStiffness
    from ._5013 import CylindricalPlanetGearCompoundModalAnalysisAtAStiffness
    from ._5014 import DatumCompoundModalAnalysisAtAStiffness
    from ._5015 import ExternalCADModelCompoundModalAnalysisAtAStiffness
    from ._5016 import FaceGearCompoundModalAnalysisAtAStiffness
    from ._5017 import FaceGearMeshCompoundModalAnalysisAtAStiffness
    from ._5018 import FaceGearSetCompoundModalAnalysisAtAStiffness
    from ._5019 import FEPartCompoundModalAnalysisAtAStiffness
    from ._5020 import FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness
    from ._5021 import GearCompoundModalAnalysisAtAStiffness
    from ._5022 import GearMeshCompoundModalAnalysisAtAStiffness
    from ._5023 import GearSetCompoundModalAnalysisAtAStiffness
    from ._5024 import GuideDxfModelCompoundModalAnalysisAtAStiffness
    from ._5025 import HypoidGearCompoundModalAnalysisAtAStiffness
    from ._5026 import HypoidGearMeshCompoundModalAnalysisAtAStiffness
    from ._5027 import HypoidGearSetCompoundModalAnalysisAtAStiffness
    from ._5028 import InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
    from ._5029 import KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness
    from ._5030 import KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness
    from ._5031 import KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness
    from ._5032 import KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness
    from ._5033 import KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness
    from ._5034 import KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness
    from ._5035 import KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness
    from ._5036 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5037 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5038 import MassDiscCompoundModalAnalysisAtAStiffness
    from ._5039 import MeasurementComponentCompoundModalAnalysisAtAStiffness
    from ._5040 import MountableComponentCompoundModalAnalysisAtAStiffness
    from ._5041 import OilSealCompoundModalAnalysisAtAStiffness
    from ._5042 import PartCompoundModalAnalysisAtAStiffness
    from ._5043 import PartToPartShearCouplingCompoundModalAnalysisAtAStiffness
    from ._5044 import PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness
    from ._5045 import PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5046 import PlanetaryConnectionCompoundModalAnalysisAtAStiffness
    from ._5047 import PlanetaryGearSetCompoundModalAnalysisAtAStiffness
    from ._5048 import PlanetCarrierCompoundModalAnalysisAtAStiffness
    from ._5049 import PointLoadCompoundModalAnalysisAtAStiffness
    from ._5050 import PowerLoadCompoundModalAnalysisAtAStiffness
    from ._5051 import PulleyCompoundModalAnalysisAtAStiffness
    from ._5052 import RingPinsCompoundModalAnalysisAtAStiffness
    from ._5053 import RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness
    from ._5054 import RollingRingAssemblyCompoundModalAnalysisAtAStiffness
    from ._5055 import RollingRingCompoundModalAnalysisAtAStiffness
    from ._5056 import RollingRingConnectionCompoundModalAnalysisAtAStiffness
    from ._5057 import RootAssemblyCompoundModalAnalysisAtAStiffness
    from ._5058 import ShaftCompoundModalAnalysisAtAStiffness
    from ._5059 import ShaftHubConnectionCompoundModalAnalysisAtAStiffness
    from ._5060 import ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
    from ._5061 import SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
    from ._5062 import SpiralBevelGearCompoundModalAnalysisAtAStiffness
    from ._5063 import SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5064 import SpiralBevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5065 import SpringDamperCompoundModalAnalysisAtAStiffness
    from ._5066 import SpringDamperConnectionCompoundModalAnalysisAtAStiffness
    from ._5067 import SpringDamperHalfCompoundModalAnalysisAtAStiffness
    from ._5068 import StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
    from ._5069 import StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness
    from ._5070 import StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness
    from ._5071 import StraightBevelGearCompoundModalAnalysisAtAStiffness
    from ._5072 import StraightBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5073 import StraightBevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5074 import StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
    from ._5075 import StraightBevelSunGearCompoundModalAnalysisAtAStiffness
    from ._5076 import SynchroniserCompoundModalAnalysisAtAStiffness
    from ._5077 import SynchroniserHalfCompoundModalAnalysisAtAStiffness
    from ._5078 import SynchroniserPartCompoundModalAnalysisAtAStiffness
    from ._5079 import SynchroniserSleeveCompoundModalAnalysisAtAStiffness
    from ._5080 import TorqueConverterCompoundModalAnalysisAtAStiffness
    from ._5081 import TorqueConverterConnectionCompoundModalAnalysisAtAStiffness
    from ._5082 import TorqueConverterPumpCompoundModalAnalysisAtAStiffness
    from ._5083 import TorqueConverterTurbineCompoundModalAnalysisAtAStiffness
    from ._5084 import UnbalancedMassCompoundModalAnalysisAtAStiffness
    from ._5085 import VirtualComponentCompoundModalAnalysisAtAStiffness
    from ._5086 import WormGearCompoundModalAnalysisAtAStiffness
    from ._5087 import WormGearMeshCompoundModalAnalysisAtAStiffness
    from ._5088 import WormGearSetCompoundModalAnalysisAtAStiffness
    from ._5089 import ZerolBevelGearCompoundModalAnalysisAtAStiffness
    from ._5090 import ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5091 import ZerolBevelGearSetCompoundModalAnalysisAtAStiffness
else:
    import_structure = {
        '_4963': ['AbstractAssemblyCompoundModalAnalysisAtAStiffness'],
        '_4964': ['AbstractShaftCompoundModalAnalysisAtAStiffness'],
        '_4965': ['AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness'],
        '_4966': ['AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness'],
        '_4967': ['AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness'],
        '_4968': ['AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness'],
        '_4969': ['AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness'],
        '_4970': ['AssemblyCompoundModalAnalysisAtAStiffness'],
        '_4971': ['BearingCompoundModalAnalysisAtAStiffness'],
        '_4972': ['BeltConnectionCompoundModalAnalysisAtAStiffness'],
        '_4973': ['BeltDriveCompoundModalAnalysisAtAStiffness'],
        '_4974': ['BevelDifferentialGearCompoundModalAnalysisAtAStiffness'],
        '_4975': ['BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness'],
        '_4976': ['BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness'],
        '_4977': ['BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness'],
        '_4978': ['BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness'],
        '_4979': ['BevelGearCompoundModalAnalysisAtAStiffness'],
        '_4980': ['BevelGearMeshCompoundModalAnalysisAtAStiffness'],
        '_4981': ['BevelGearSetCompoundModalAnalysisAtAStiffness'],
        '_4982': ['BoltCompoundModalAnalysisAtAStiffness'],
        '_4983': ['BoltedJointCompoundModalAnalysisAtAStiffness'],
        '_4984': ['ClutchCompoundModalAnalysisAtAStiffness'],
        '_4985': ['ClutchConnectionCompoundModalAnalysisAtAStiffness'],
        '_4986': ['ClutchHalfCompoundModalAnalysisAtAStiffness'],
        '_4987': ['CoaxialConnectionCompoundModalAnalysisAtAStiffness'],
        '_4988': ['ComponentCompoundModalAnalysisAtAStiffness'],
        '_4989': ['ConceptCouplingCompoundModalAnalysisAtAStiffness'],
        '_4990': ['ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness'],
        '_4991': ['ConceptCouplingHalfCompoundModalAnalysisAtAStiffness'],
        '_4992': ['ConceptGearCompoundModalAnalysisAtAStiffness'],
        '_4993': ['ConceptGearMeshCompoundModalAnalysisAtAStiffness'],
        '_4994': ['ConceptGearSetCompoundModalAnalysisAtAStiffness'],
        '_4995': ['ConicalGearCompoundModalAnalysisAtAStiffness'],
        '_4996': ['ConicalGearMeshCompoundModalAnalysisAtAStiffness'],
        '_4997': ['ConicalGearSetCompoundModalAnalysisAtAStiffness'],
        '_4998': ['ConnectionCompoundModalAnalysisAtAStiffness'],
        '_4999': ['ConnectorCompoundModalAnalysisAtAStiffness'],
        '_5000': ['CouplingCompoundModalAnalysisAtAStiffness'],
        '_5001': ['CouplingConnectionCompoundModalAnalysisAtAStiffness'],
        '_5002': ['CouplingHalfCompoundModalAnalysisAtAStiffness'],
        '_5003': ['CVTBeltConnectionCompoundModalAnalysisAtAStiffness'],
        '_5004': ['CVTCompoundModalAnalysisAtAStiffness'],
        '_5005': ['CVTPulleyCompoundModalAnalysisAtAStiffness'],
        '_5006': ['CycloidalAssemblyCompoundModalAnalysisAtAStiffness'],
        '_5007': ['CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness'],
        '_5008': ['CycloidalDiscCompoundModalAnalysisAtAStiffness'],
        '_5009': ['CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness'],
        '_5010': ['CylindricalGearCompoundModalAnalysisAtAStiffness'],
        '_5011': ['CylindricalGearMeshCompoundModalAnalysisAtAStiffness'],
        '_5012': ['CylindricalGearSetCompoundModalAnalysisAtAStiffness'],
        '_5013': ['CylindricalPlanetGearCompoundModalAnalysisAtAStiffness'],
        '_5014': ['DatumCompoundModalAnalysisAtAStiffness'],
        '_5015': ['ExternalCADModelCompoundModalAnalysisAtAStiffness'],
        '_5016': ['FaceGearCompoundModalAnalysisAtAStiffness'],
        '_5017': ['FaceGearMeshCompoundModalAnalysisAtAStiffness'],
        '_5018': ['FaceGearSetCompoundModalAnalysisAtAStiffness'],
        '_5019': ['FEPartCompoundModalAnalysisAtAStiffness'],
        '_5020': ['FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness'],
        '_5021': ['GearCompoundModalAnalysisAtAStiffness'],
        '_5022': ['GearMeshCompoundModalAnalysisAtAStiffness'],
        '_5023': ['GearSetCompoundModalAnalysisAtAStiffness'],
        '_5024': ['GuideDxfModelCompoundModalAnalysisAtAStiffness'],
        '_5025': ['HypoidGearCompoundModalAnalysisAtAStiffness'],
        '_5026': ['HypoidGearMeshCompoundModalAnalysisAtAStiffness'],
        '_5027': ['HypoidGearSetCompoundModalAnalysisAtAStiffness'],
        '_5028': ['InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness'],
        '_5029': ['KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness'],
        '_5030': ['KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness'],
        '_5031': ['KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness'],
        '_5032': ['KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness'],
        '_5033': ['KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness'],
        '_5034': ['KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness'],
        '_5035': ['KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness'],
        '_5036': ['KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness'],
        '_5037': ['KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness'],
        '_5038': ['MassDiscCompoundModalAnalysisAtAStiffness'],
        '_5039': ['MeasurementComponentCompoundModalAnalysisAtAStiffness'],
        '_5040': ['MountableComponentCompoundModalAnalysisAtAStiffness'],
        '_5041': ['OilSealCompoundModalAnalysisAtAStiffness'],
        '_5042': ['PartCompoundModalAnalysisAtAStiffness'],
        '_5043': ['PartToPartShearCouplingCompoundModalAnalysisAtAStiffness'],
        '_5044': ['PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness'],
        '_5045': ['PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness'],
        '_5046': ['PlanetaryConnectionCompoundModalAnalysisAtAStiffness'],
        '_5047': ['PlanetaryGearSetCompoundModalAnalysisAtAStiffness'],
        '_5048': ['PlanetCarrierCompoundModalAnalysisAtAStiffness'],
        '_5049': ['PointLoadCompoundModalAnalysisAtAStiffness'],
        '_5050': ['PowerLoadCompoundModalAnalysisAtAStiffness'],
        '_5051': ['PulleyCompoundModalAnalysisAtAStiffness'],
        '_5052': ['RingPinsCompoundModalAnalysisAtAStiffness'],
        '_5053': ['RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness'],
        '_5054': ['RollingRingAssemblyCompoundModalAnalysisAtAStiffness'],
        '_5055': ['RollingRingCompoundModalAnalysisAtAStiffness'],
        '_5056': ['RollingRingConnectionCompoundModalAnalysisAtAStiffness'],
        '_5057': ['RootAssemblyCompoundModalAnalysisAtAStiffness'],
        '_5058': ['ShaftCompoundModalAnalysisAtAStiffness'],
        '_5059': ['ShaftHubConnectionCompoundModalAnalysisAtAStiffness'],
        '_5060': ['ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness'],
        '_5061': ['SpecialisedAssemblyCompoundModalAnalysisAtAStiffness'],
        '_5062': ['SpiralBevelGearCompoundModalAnalysisAtAStiffness'],
        '_5063': ['SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness'],
        '_5064': ['SpiralBevelGearSetCompoundModalAnalysisAtAStiffness'],
        '_5065': ['SpringDamperCompoundModalAnalysisAtAStiffness'],
        '_5066': ['SpringDamperConnectionCompoundModalAnalysisAtAStiffness'],
        '_5067': ['SpringDamperHalfCompoundModalAnalysisAtAStiffness'],
        '_5068': ['StraightBevelDiffGearCompoundModalAnalysisAtAStiffness'],
        '_5069': ['StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness'],
        '_5070': ['StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness'],
        '_5071': ['StraightBevelGearCompoundModalAnalysisAtAStiffness'],
        '_5072': ['StraightBevelGearMeshCompoundModalAnalysisAtAStiffness'],
        '_5073': ['StraightBevelGearSetCompoundModalAnalysisAtAStiffness'],
        '_5074': ['StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness'],
        '_5075': ['StraightBevelSunGearCompoundModalAnalysisAtAStiffness'],
        '_5076': ['SynchroniserCompoundModalAnalysisAtAStiffness'],
        '_5077': ['SynchroniserHalfCompoundModalAnalysisAtAStiffness'],
        '_5078': ['SynchroniserPartCompoundModalAnalysisAtAStiffness'],
        '_5079': ['SynchroniserSleeveCompoundModalAnalysisAtAStiffness'],
        '_5080': ['TorqueConverterCompoundModalAnalysisAtAStiffness'],
        '_5081': ['TorqueConverterConnectionCompoundModalAnalysisAtAStiffness'],
        '_5082': ['TorqueConverterPumpCompoundModalAnalysisAtAStiffness'],
        '_5083': ['TorqueConverterTurbineCompoundModalAnalysisAtAStiffness'],
        '_5084': ['UnbalancedMassCompoundModalAnalysisAtAStiffness'],
        '_5085': ['VirtualComponentCompoundModalAnalysisAtAStiffness'],
        '_5086': ['WormGearCompoundModalAnalysisAtAStiffness'],
        '_5087': ['WormGearMeshCompoundModalAnalysisAtAStiffness'],
        '_5088': ['WormGearSetCompoundModalAnalysisAtAStiffness'],
        '_5089': ['ZerolBevelGearCompoundModalAnalysisAtAStiffness'],
        '_5090': ['ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness'],
        '_5091': ['ZerolBevelGearSetCompoundModalAnalysisAtAStiffness'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
