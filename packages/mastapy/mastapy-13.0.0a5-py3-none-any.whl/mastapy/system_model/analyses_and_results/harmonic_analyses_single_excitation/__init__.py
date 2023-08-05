"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5978 import AbstractAssemblyHarmonicAnalysisOfSingleExcitation
    from ._5979 import AbstractShaftHarmonicAnalysisOfSingleExcitation
    from ._5980 import AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation
    from ._5981 import AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
    from ._5982 import AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
    from ._5983 import AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation
    from ._5984 import AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
    from ._5985 import AssemblyHarmonicAnalysisOfSingleExcitation
    from ._5986 import BearingHarmonicAnalysisOfSingleExcitation
    from ._5987 import BeltConnectionHarmonicAnalysisOfSingleExcitation
    from ._5988 import BeltDriveHarmonicAnalysisOfSingleExcitation
    from ._5989 import BevelDifferentialGearHarmonicAnalysisOfSingleExcitation
    from ._5990 import BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation
    from ._5991 import BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation
    from ._5992 import BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation
    from ._5993 import BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation
    from ._5994 import BevelGearHarmonicAnalysisOfSingleExcitation
    from ._5995 import BevelGearMeshHarmonicAnalysisOfSingleExcitation
    from ._5996 import BevelGearSetHarmonicAnalysisOfSingleExcitation
    from ._5997 import BoltedJointHarmonicAnalysisOfSingleExcitation
    from ._5998 import BoltHarmonicAnalysisOfSingleExcitation
    from ._5999 import ClutchConnectionHarmonicAnalysisOfSingleExcitation
    from ._6000 import ClutchHalfHarmonicAnalysisOfSingleExcitation
    from ._6001 import ClutchHarmonicAnalysisOfSingleExcitation
    from ._6002 import CoaxialConnectionHarmonicAnalysisOfSingleExcitation
    from ._6003 import ComponentHarmonicAnalysisOfSingleExcitation
    from ._6004 import ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation
    from ._6005 import ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation
    from ._6006 import ConceptCouplingHarmonicAnalysisOfSingleExcitation
    from ._6007 import ConceptGearHarmonicAnalysisOfSingleExcitation
    from ._6008 import ConceptGearMeshHarmonicAnalysisOfSingleExcitation
    from ._6009 import ConceptGearSetHarmonicAnalysisOfSingleExcitation
    from ._6010 import ConicalGearHarmonicAnalysisOfSingleExcitation
    from ._6011 import ConicalGearMeshHarmonicAnalysisOfSingleExcitation
    from ._6012 import ConicalGearSetHarmonicAnalysisOfSingleExcitation
    from ._6013 import ConnectionHarmonicAnalysisOfSingleExcitation
    from ._6014 import ConnectorHarmonicAnalysisOfSingleExcitation
    from ._6015 import CouplingConnectionHarmonicAnalysisOfSingleExcitation
    from ._6016 import CouplingHalfHarmonicAnalysisOfSingleExcitation
    from ._6017 import CouplingHarmonicAnalysisOfSingleExcitation
    from ._6018 import CVTBeltConnectionHarmonicAnalysisOfSingleExcitation
    from ._6019 import CVTHarmonicAnalysisOfSingleExcitation
    from ._6020 import CVTPulleyHarmonicAnalysisOfSingleExcitation
    from ._6021 import CycloidalAssemblyHarmonicAnalysisOfSingleExcitation
    from ._6022 import CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation
    from ._6023 import CycloidalDiscHarmonicAnalysisOfSingleExcitation
    from ._6024 import CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysisOfSingleExcitation
    from ._6025 import CylindricalGearHarmonicAnalysisOfSingleExcitation
    from ._6026 import CylindricalGearMeshHarmonicAnalysisOfSingleExcitation
    from ._6027 import CylindricalGearSetHarmonicAnalysisOfSingleExcitation
    from ._6028 import CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation
    from ._6029 import DatumHarmonicAnalysisOfSingleExcitation
    from ._6030 import ExternalCADModelHarmonicAnalysisOfSingleExcitation
    from ._6031 import FaceGearHarmonicAnalysisOfSingleExcitation
    from ._6032 import FaceGearMeshHarmonicAnalysisOfSingleExcitation
    from ._6033 import FaceGearSetHarmonicAnalysisOfSingleExcitation
    from ._6034 import FEPartHarmonicAnalysisOfSingleExcitation
    from ._6035 import FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation
    from ._6036 import GearHarmonicAnalysisOfSingleExcitation
    from ._6037 import GearMeshHarmonicAnalysisOfSingleExcitation
    from ._6038 import GearSetHarmonicAnalysisOfSingleExcitation
    from ._6039 import GuideDxfModelHarmonicAnalysisOfSingleExcitation
    from ._6040 import HarmonicAnalysisOfSingleExcitation
    from ._6041 import HypoidGearHarmonicAnalysisOfSingleExcitation
    from ._6042 import HypoidGearMeshHarmonicAnalysisOfSingleExcitation
    from ._6043 import HypoidGearSetHarmonicAnalysisOfSingleExcitation
    from ._6044 import InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
    from ._6045 import KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation
    from ._6046 import KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation
    from ._6047 import KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation
    from ._6048 import KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation
    from ._6049 import KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation
    from ._6050 import KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation
    from ._6051 import KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation
    from ._6052 import KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
    from ._6053 import KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
    from ._6054 import MassDiscHarmonicAnalysisOfSingleExcitation
    from ._6055 import MeasurementComponentHarmonicAnalysisOfSingleExcitation
    from ._2620 import ModalAnalysisForHarmonicAnalysis
    from ._6056 import MountableComponentHarmonicAnalysisOfSingleExcitation
    from ._6057 import OilSealHarmonicAnalysisOfSingleExcitation
    from ._6058 import PartHarmonicAnalysisOfSingleExcitation
    from ._6059 import PartToPartShearCouplingConnectionHarmonicAnalysisOfSingleExcitation
    from ._6060 import PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation
    from ._6061 import PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation
    from ._6062 import PlanetaryConnectionHarmonicAnalysisOfSingleExcitation
    from ._6063 import PlanetaryGearSetHarmonicAnalysisOfSingleExcitation
    from ._6064 import PlanetCarrierHarmonicAnalysisOfSingleExcitation
    from ._6065 import PointLoadHarmonicAnalysisOfSingleExcitation
    from ._6066 import PowerLoadHarmonicAnalysisOfSingleExcitation
    from ._6067 import PulleyHarmonicAnalysisOfSingleExcitation
    from ._6068 import RingPinsHarmonicAnalysisOfSingleExcitation
    from ._6069 import RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation
    from ._6070 import RollingRingAssemblyHarmonicAnalysisOfSingleExcitation
    from ._6071 import RollingRingConnectionHarmonicAnalysisOfSingleExcitation
    from ._6072 import RollingRingHarmonicAnalysisOfSingleExcitation
    from ._6073 import RootAssemblyHarmonicAnalysisOfSingleExcitation
    from ._6074 import ShaftHarmonicAnalysisOfSingleExcitation
    from ._6075 import ShaftHubConnectionHarmonicAnalysisOfSingleExcitation
    from ._6076 import ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
    from ._6077 import SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
    from ._6078 import SpiralBevelGearHarmonicAnalysisOfSingleExcitation
    from ._6079 import SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
    from ._6080 import SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
    from ._6081 import SpringDamperConnectionHarmonicAnalysisOfSingleExcitation
    from ._6082 import SpringDamperHalfHarmonicAnalysisOfSingleExcitation
    from ._6083 import SpringDamperHarmonicAnalysisOfSingleExcitation
    from ._6084 import StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation
    from ._6085 import StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation
    from ._6086 import StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation
    from ._6087 import StraightBevelGearHarmonicAnalysisOfSingleExcitation
    from ._6088 import StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation
    from ._6089 import StraightBevelGearSetHarmonicAnalysisOfSingleExcitation
    from ._6090 import StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation
    from ._6091 import StraightBevelSunGearHarmonicAnalysisOfSingleExcitation
    from ._6092 import SynchroniserHalfHarmonicAnalysisOfSingleExcitation
    from ._6093 import SynchroniserHarmonicAnalysisOfSingleExcitation
    from ._6094 import SynchroniserPartHarmonicAnalysisOfSingleExcitation
    from ._6095 import SynchroniserSleeveHarmonicAnalysisOfSingleExcitation
    from ._6096 import TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation
    from ._6097 import TorqueConverterHarmonicAnalysisOfSingleExcitation
    from ._6098 import TorqueConverterPumpHarmonicAnalysisOfSingleExcitation
    from ._6099 import TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation
    from ._6100 import UnbalancedMassHarmonicAnalysisOfSingleExcitation
    from ._6101 import VirtualComponentHarmonicAnalysisOfSingleExcitation
    from ._6102 import WormGearHarmonicAnalysisOfSingleExcitation
    from ._6103 import WormGearMeshHarmonicAnalysisOfSingleExcitation
    from ._6104 import WormGearSetHarmonicAnalysisOfSingleExcitation
    from ._6105 import ZerolBevelGearHarmonicAnalysisOfSingleExcitation
    from ._6106 import ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation
    from ._6107 import ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation
else:
    import_structure = {
        '_5978': ['AbstractAssemblyHarmonicAnalysisOfSingleExcitation'],
        '_5979': ['AbstractShaftHarmonicAnalysisOfSingleExcitation'],
        '_5980': ['AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation'],
        '_5981': ['AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation'],
        '_5982': ['AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation'],
        '_5983': ['AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation'],
        '_5984': ['AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation'],
        '_5985': ['AssemblyHarmonicAnalysisOfSingleExcitation'],
        '_5986': ['BearingHarmonicAnalysisOfSingleExcitation'],
        '_5987': ['BeltConnectionHarmonicAnalysisOfSingleExcitation'],
        '_5988': ['BeltDriveHarmonicAnalysisOfSingleExcitation'],
        '_5989': ['BevelDifferentialGearHarmonicAnalysisOfSingleExcitation'],
        '_5990': ['BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation'],
        '_5991': ['BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation'],
        '_5992': ['BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation'],
        '_5993': ['BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation'],
        '_5994': ['BevelGearHarmonicAnalysisOfSingleExcitation'],
        '_5995': ['BevelGearMeshHarmonicAnalysisOfSingleExcitation'],
        '_5996': ['BevelGearSetHarmonicAnalysisOfSingleExcitation'],
        '_5997': ['BoltedJointHarmonicAnalysisOfSingleExcitation'],
        '_5998': ['BoltHarmonicAnalysisOfSingleExcitation'],
        '_5999': ['ClutchConnectionHarmonicAnalysisOfSingleExcitation'],
        '_6000': ['ClutchHalfHarmonicAnalysisOfSingleExcitation'],
        '_6001': ['ClutchHarmonicAnalysisOfSingleExcitation'],
        '_6002': ['CoaxialConnectionHarmonicAnalysisOfSingleExcitation'],
        '_6003': ['ComponentHarmonicAnalysisOfSingleExcitation'],
        '_6004': ['ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation'],
        '_6005': ['ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation'],
        '_6006': ['ConceptCouplingHarmonicAnalysisOfSingleExcitation'],
        '_6007': ['ConceptGearHarmonicAnalysisOfSingleExcitation'],
        '_6008': ['ConceptGearMeshHarmonicAnalysisOfSingleExcitation'],
        '_6009': ['ConceptGearSetHarmonicAnalysisOfSingleExcitation'],
        '_6010': ['ConicalGearHarmonicAnalysisOfSingleExcitation'],
        '_6011': ['ConicalGearMeshHarmonicAnalysisOfSingleExcitation'],
        '_6012': ['ConicalGearSetHarmonicAnalysisOfSingleExcitation'],
        '_6013': ['ConnectionHarmonicAnalysisOfSingleExcitation'],
        '_6014': ['ConnectorHarmonicAnalysisOfSingleExcitation'],
        '_6015': ['CouplingConnectionHarmonicAnalysisOfSingleExcitation'],
        '_6016': ['CouplingHalfHarmonicAnalysisOfSingleExcitation'],
        '_6017': ['CouplingHarmonicAnalysisOfSingleExcitation'],
        '_6018': ['CVTBeltConnectionHarmonicAnalysisOfSingleExcitation'],
        '_6019': ['CVTHarmonicAnalysisOfSingleExcitation'],
        '_6020': ['CVTPulleyHarmonicAnalysisOfSingleExcitation'],
        '_6021': ['CycloidalAssemblyHarmonicAnalysisOfSingleExcitation'],
        '_6022': ['CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation'],
        '_6023': ['CycloidalDiscHarmonicAnalysisOfSingleExcitation'],
        '_6024': ['CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysisOfSingleExcitation'],
        '_6025': ['CylindricalGearHarmonicAnalysisOfSingleExcitation'],
        '_6026': ['CylindricalGearMeshHarmonicAnalysisOfSingleExcitation'],
        '_6027': ['CylindricalGearSetHarmonicAnalysisOfSingleExcitation'],
        '_6028': ['CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation'],
        '_6029': ['DatumHarmonicAnalysisOfSingleExcitation'],
        '_6030': ['ExternalCADModelHarmonicAnalysisOfSingleExcitation'],
        '_6031': ['FaceGearHarmonicAnalysisOfSingleExcitation'],
        '_6032': ['FaceGearMeshHarmonicAnalysisOfSingleExcitation'],
        '_6033': ['FaceGearSetHarmonicAnalysisOfSingleExcitation'],
        '_6034': ['FEPartHarmonicAnalysisOfSingleExcitation'],
        '_6035': ['FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation'],
        '_6036': ['GearHarmonicAnalysisOfSingleExcitation'],
        '_6037': ['GearMeshHarmonicAnalysisOfSingleExcitation'],
        '_6038': ['GearSetHarmonicAnalysisOfSingleExcitation'],
        '_6039': ['GuideDxfModelHarmonicAnalysisOfSingleExcitation'],
        '_6040': ['HarmonicAnalysisOfSingleExcitation'],
        '_6041': ['HypoidGearHarmonicAnalysisOfSingleExcitation'],
        '_6042': ['HypoidGearMeshHarmonicAnalysisOfSingleExcitation'],
        '_6043': ['HypoidGearSetHarmonicAnalysisOfSingleExcitation'],
        '_6044': ['InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation'],
        '_6045': ['KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation'],
        '_6046': ['KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation'],
        '_6047': ['KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation'],
        '_6048': ['KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation'],
        '_6049': ['KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation'],
        '_6050': ['KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation'],
        '_6051': ['KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation'],
        '_6052': ['KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation'],
        '_6053': ['KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation'],
        '_6054': ['MassDiscHarmonicAnalysisOfSingleExcitation'],
        '_6055': ['MeasurementComponentHarmonicAnalysisOfSingleExcitation'],
        '_2620': ['ModalAnalysisForHarmonicAnalysis'],
        '_6056': ['MountableComponentHarmonicAnalysisOfSingleExcitation'],
        '_6057': ['OilSealHarmonicAnalysisOfSingleExcitation'],
        '_6058': ['PartHarmonicAnalysisOfSingleExcitation'],
        '_6059': ['PartToPartShearCouplingConnectionHarmonicAnalysisOfSingleExcitation'],
        '_6060': ['PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation'],
        '_6061': ['PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation'],
        '_6062': ['PlanetaryConnectionHarmonicAnalysisOfSingleExcitation'],
        '_6063': ['PlanetaryGearSetHarmonicAnalysisOfSingleExcitation'],
        '_6064': ['PlanetCarrierHarmonicAnalysisOfSingleExcitation'],
        '_6065': ['PointLoadHarmonicAnalysisOfSingleExcitation'],
        '_6066': ['PowerLoadHarmonicAnalysisOfSingleExcitation'],
        '_6067': ['PulleyHarmonicAnalysisOfSingleExcitation'],
        '_6068': ['RingPinsHarmonicAnalysisOfSingleExcitation'],
        '_6069': ['RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation'],
        '_6070': ['RollingRingAssemblyHarmonicAnalysisOfSingleExcitation'],
        '_6071': ['RollingRingConnectionHarmonicAnalysisOfSingleExcitation'],
        '_6072': ['RollingRingHarmonicAnalysisOfSingleExcitation'],
        '_6073': ['RootAssemblyHarmonicAnalysisOfSingleExcitation'],
        '_6074': ['ShaftHarmonicAnalysisOfSingleExcitation'],
        '_6075': ['ShaftHubConnectionHarmonicAnalysisOfSingleExcitation'],
        '_6076': ['ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation'],
        '_6077': ['SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation'],
        '_6078': ['SpiralBevelGearHarmonicAnalysisOfSingleExcitation'],
        '_6079': ['SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation'],
        '_6080': ['SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation'],
        '_6081': ['SpringDamperConnectionHarmonicAnalysisOfSingleExcitation'],
        '_6082': ['SpringDamperHalfHarmonicAnalysisOfSingleExcitation'],
        '_6083': ['SpringDamperHarmonicAnalysisOfSingleExcitation'],
        '_6084': ['StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation'],
        '_6085': ['StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation'],
        '_6086': ['StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation'],
        '_6087': ['StraightBevelGearHarmonicAnalysisOfSingleExcitation'],
        '_6088': ['StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation'],
        '_6089': ['StraightBevelGearSetHarmonicAnalysisOfSingleExcitation'],
        '_6090': ['StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation'],
        '_6091': ['StraightBevelSunGearHarmonicAnalysisOfSingleExcitation'],
        '_6092': ['SynchroniserHalfHarmonicAnalysisOfSingleExcitation'],
        '_6093': ['SynchroniserHarmonicAnalysisOfSingleExcitation'],
        '_6094': ['SynchroniserPartHarmonicAnalysisOfSingleExcitation'],
        '_6095': ['SynchroniserSleeveHarmonicAnalysisOfSingleExcitation'],
        '_6096': ['TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation'],
        '_6097': ['TorqueConverterHarmonicAnalysisOfSingleExcitation'],
        '_6098': ['TorqueConverterPumpHarmonicAnalysisOfSingleExcitation'],
        '_6099': ['TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation'],
        '_6100': ['UnbalancedMassHarmonicAnalysisOfSingleExcitation'],
        '_6101': ['VirtualComponentHarmonicAnalysisOfSingleExcitation'],
        '_6102': ['WormGearHarmonicAnalysisOfSingleExcitation'],
        '_6103': ['WormGearMeshHarmonicAnalysisOfSingleExcitation'],
        '_6104': ['WormGearSetHarmonicAnalysisOfSingleExcitation'],
        '_6105': ['ZerolBevelGearHarmonicAnalysisOfSingleExcitation'],
        '_6106': ['ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation'],
        '_6107': ['ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
