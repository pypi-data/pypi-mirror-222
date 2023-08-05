"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6973 import AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._6974 import AbstractShaftAdvancedTimeSteppingAnalysisForModulation
    from ._6975 import AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation
    from ._6976 import AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._2605 import AdvancedTimeSteppingAnalysisForModulation
    from ._6977 import AtsamExcitationsOrOthers
    from ._6978 import AtsamNaturalFrequencyViewOption
    from ._6979 import AdvancedTimeSteppingAnalysisForModulationOptions
    from ._6980 import AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
    from ._6981 import AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._6982 import AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._6983 import AssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._6984 import ATSAMResultsVsLargeTimeStepSettings
    from ._6985 import BearingAdvancedTimeSteppingAnalysisForModulation
    from ._6986 import BeltConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._6987 import BeltDriveAdvancedTimeSteppingAnalysisForModulation
    from ._6988 import BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
    from ._6989 import BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._6990 import BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._6991 import BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation
    from ._6992 import BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation
    from ._6993 import BevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._6994 import BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._6995 import BevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._6996 import BoltAdvancedTimeSteppingAnalysisForModulation
    from ._6997 import BoltedJointAdvancedTimeSteppingAnalysisForModulation
    from ._6998 import ClutchAdvancedTimeSteppingAnalysisForModulation
    from ._6999 import ClutchConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7000 import ClutchHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7001 import CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7002 import ComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7003 import ConceptCouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7004 import ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7005 import ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7006 import ConceptGearAdvancedTimeSteppingAnalysisForModulation
    from ._7007 import ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7008 import ConceptGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7009 import ConicalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7010 import ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7011 import ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7012 import ConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7013 import ConnectorAdvancedTimeSteppingAnalysisForModulation
    from ._7014 import CouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7015 import CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7016 import CouplingHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7017 import CVTAdvancedTimeSteppingAnalysisForModulation
    from ._7018 import CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7019 import CVTPulleyAdvancedTimeSteppingAnalysisForModulation
    from ._7020 import CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7021 import CycloidalDiscAdvancedTimeSteppingAnalysisForModulation
    from ._7022 import CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7023 import CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7024 import CylindricalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7025 import CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7026 import CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7027 import CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation
    from ._7028 import DatumAdvancedTimeSteppingAnalysisForModulation
    from ._7029 import ExternalCADModelAdvancedTimeSteppingAnalysisForModulation
    from ._7030 import FaceGearAdvancedTimeSteppingAnalysisForModulation
    from ._7031 import FaceGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7032 import FaceGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7033 import FEPartAdvancedTimeSteppingAnalysisForModulation
    from ._7034 import FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7035 import GearAdvancedTimeSteppingAnalysisForModulation
    from ._7036 import GearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7037 import GearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7038 import GuideDxfModelAdvancedTimeSteppingAnalysisForModulation
    from ._7039 import HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation
    from ._7040 import HypoidGearAdvancedTimeSteppingAnalysisForModulation
    from ._7041 import HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7042 import HypoidGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7043 import InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7044 import KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7045 import KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7046 import KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7047 import KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation
    from ._7048 import KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7049 import KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7050 import KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7051 import KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7052 import KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7053 import MassDiscAdvancedTimeSteppingAnalysisForModulation
    from ._7054 import MeasurementComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7055 import MountableComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7056 import OilSealAdvancedTimeSteppingAnalysisForModulation
    from ._7057 import PartAdvancedTimeSteppingAnalysisForModulation
    from ._7058 import PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7059 import PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7060 import PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7061 import PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7062 import PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7063 import PlanetCarrierAdvancedTimeSteppingAnalysisForModulation
    from ._7064 import PointLoadAdvancedTimeSteppingAnalysisForModulation
    from ._7065 import PowerLoadAdvancedTimeSteppingAnalysisForModulation
    from ._7066 import PulleyAdvancedTimeSteppingAnalysisForModulation
    from ._7067 import RingPinsAdvancedTimeSteppingAnalysisForModulation
    from ._7068 import RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7069 import RollingRingAdvancedTimeSteppingAnalysisForModulation
    from ._7070 import RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7071 import RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7072 import RootAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7073 import ShaftAdvancedTimeSteppingAnalysisForModulation
    from ._7074 import ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7075 import ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7076 import SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7077 import SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7078 import SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7079 import SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7080 import SpringDamperAdvancedTimeSteppingAnalysisForModulation
    from ._7081 import SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7082 import SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7083 import StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
    from ._7084 import StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7085 import StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7086 import StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7087 import StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7088 import StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7089 import StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation
    from ._7090 import StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
    from ._7091 import SynchroniserAdvancedTimeSteppingAnalysisForModulation
    from ._7092 import SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7093 import SynchroniserPartAdvancedTimeSteppingAnalysisForModulation
    from ._7094 import SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation
    from ._7095 import TorqueConverterAdvancedTimeSteppingAnalysisForModulation
    from ._7096 import TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7097 import TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation
    from ._7098 import TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation
    from ._7099 import UnbalancedMassAdvancedTimeSteppingAnalysisForModulation
    from ._7100 import VirtualComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7101 import WormGearAdvancedTimeSteppingAnalysisForModulation
    from ._7102 import WormGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7103 import WormGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7104 import ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7105 import ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7106 import ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
else:
    import_structure = {
        '_6973': ['AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation'],
        '_6974': ['AbstractShaftAdvancedTimeSteppingAnalysisForModulation'],
        '_6975': ['AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation'],
        '_6976': ['AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation'],
        '_2605': ['AdvancedTimeSteppingAnalysisForModulation'],
        '_6977': ['AtsamExcitationsOrOthers'],
        '_6978': ['AtsamNaturalFrequencyViewOption'],
        '_6979': ['AdvancedTimeSteppingAnalysisForModulationOptions'],
        '_6980': ['AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation'],
        '_6981': ['AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation'],
        '_6982': ['AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation'],
        '_6983': ['AssemblyAdvancedTimeSteppingAnalysisForModulation'],
        '_6984': ['ATSAMResultsVsLargeTimeStepSettings'],
        '_6985': ['BearingAdvancedTimeSteppingAnalysisForModulation'],
        '_6986': ['BeltConnectionAdvancedTimeSteppingAnalysisForModulation'],
        '_6987': ['BeltDriveAdvancedTimeSteppingAnalysisForModulation'],
        '_6988': ['BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation'],
        '_6989': ['BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation'],
        '_6990': ['BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation'],
        '_6991': ['BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation'],
        '_6992': ['BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation'],
        '_6993': ['BevelGearAdvancedTimeSteppingAnalysisForModulation'],
        '_6994': ['BevelGearMeshAdvancedTimeSteppingAnalysisForModulation'],
        '_6995': ['BevelGearSetAdvancedTimeSteppingAnalysisForModulation'],
        '_6996': ['BoltAdvancedTimeSteppingAnalysisForModulation'],
        '_6997': ['BoltedJointAdvancedTimeSteppingAnalysisForModulation'],
        '_6998': ['ClutchAdvancedTimeSteppingAnalysisForModulation'],
        '_6999': ['ClutchConnectionAdvancedTimeSteppingAnalysisForModulation'],
        '_7000': ['ClutchHalfAdvancedTimeSteppingAnalysisForModulation'],
        '_7001': ['CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation'],
        '_7002': ['ComponentAdvancedTimeSteppingAnalysisForModulation'],
        '_7003': ['ConceptCouplingAdvancedTimeSteppingAnalysisForModulation'],
        '_7004': ['ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation'],
        '_7005': ['ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation'],
        '_7006': ['ConceptGearAdvancedTimeSteppingAnalysisForModulation'],
        '_7007': ['ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation'],
        '_7008': ['ConceptGearSetAdvancedTimeSteppingAnalysisForModulation'],
        '_7009': ['ConicalGearAdvancedTimeSteppingAnalysisForModulation'],
        '_7010': ['ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation'],
        '_7011': ['ConicalGearSetAdvancedTimeSteppingAnalysisForModulation'],
        '_7012': ['ConnectionAdvancedTimeSteppingAnalysisForModulation'],
        '_7013': ['ConnectorAdvancedTimeSteppingAnalysisForModulation'],
        '_7014': ['CouplingAdvancedTimeSteppingAnalysisForModulation'],
        '_7015': ['CouplingConnectionAdvancedTimeSteppingAnalysisForModulation'],
        '_7016': ['CouplingHalfAdvancedTimeSteppingAnalysisForModulation'],
        '_7017': ['CVTAdvancedTimeSteppingAnalysisForModulation'],
        '_7018': ['CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation'],
        '_7019': ['CVTPulleyAdvancedTimeSteppingAnalysisForModulation'],
        '_7020': ['CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation'],
        '_7021': ['CycloidalDiscAdvancedTimeSteppingAnalysisForModulation'],
        '_7022': ['CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation'],
        '_7023': ['CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation'],
        '_7024': ['CylindricalGearAdvancedTimeSteppingAnalysisForModulation'],
        '_7025': ['CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation'],
        '_7026': ['CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation'],
        '_7027': ['CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation'],
        '_7028': ['DatumAdvancedTimeSteppingAnalysisForModulation'],
        '_7029': ['ExternalCADModelAdvancedTimeSteppingAnalysisForModulation'],
        '_7030': ['FaceGearAdvancedTimeSteppingAnalysisForModulation'],
        '_7031': ['FaceGearMeshAdvancedTimeSteppingAnalysisForModulation'],
        '_7032': ['FaceGearSetAdvancedTimeSteppingAnalysisForModulation'],
        '_7033': ['FEPartAdvancedTimeSteppingAnalysisForModulation'],
        '_7034': ['FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation'],
        '_7035': ['GearAdvancedTimeSteppingAnalysisForModulation'],
        '_7036': ['GearMeshAdvancedTimeSteppingAnalysisForModulation'],
        '_7037': ['GearSetAdvancedTimeSteppingAnalysisForModulation'],
        '_7038': ['GuideDxfModelAdvancedTimeSteppingAnalysisForModulation'],
        '_7039': ['HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation'],
        '_7040': ['HypoidGearAdvancedTimeSteppingAnalysisForModulation'],
        '_7041': ['HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation'],
        '_7042': ['HypoidGearSetAdvancedTimeSteppingAnalysisForModulation'],
        '_7043': ['InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation'],
        '_7044': ['KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation'],
        '_7045': ['KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation'],
        '_7046': ['KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation'],
        '_7047': ['KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation'],
        '_7048': ['KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation'],
        '_7049': ['KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation'],
        '_7050': ['KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation'],
        '_7051': ['KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation'],
        '_7052': ['KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation'],
        '_7053': ['MassDiscAdvancedTimeSteppingAnalysisForModulation'],
        '_7054': ['MeasurementComponentAdvancedTimeSteppingAnalysisForModulation'],
        '_7055': ['MountableComponentAdvancedTimeSteppingAnalysisForModulation'],
        '_7056': ['OilSealAdvancedTimeSteppingAnalysisForModulation'],
        '_7057': ['PartAdvancedTimeSteppingAnalysisForModulation'],
        '_7058': ['PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation'],
        '_7059': ['PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation'],
        '_7060': ['PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation'],
        '_7061': ['PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation'],
        '_7062': ['PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation'],
        '_7063': ['PlanetCarrierAdvancedTimeSteppingAnalysisForModulation'],
        '_7064': ['PointLoadAdvancedTimeSteppingAnalysisForModulation'],
        '_7065': ['PowerLoadAdvancedTimeSteppingAnalysisForModulation'],
        '_7066': ['PulleyAdvancedTimeSteppingAnalysisForModulation'],
        '_7067': ['RingPinsAdvancedTimeSteppingAnalysisForModulation'],
        '_7068': ['RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation'],
        '_7069': ['RollingRingAdvancedTimeSteppingAnalysisForModulation'],
        '_7070': ['RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation'],
        '_7071': ['RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation'],
        '_7072': ['RootAssemblyAdvancedTimeSteppingAnalysisForModulation'],
        '_7073': ['ShaftAdvancedTimeSteppingAnalysisForModulation'],
        '_7074': ['ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation'],
        '_7075': ['ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation'],
        '_7076': ['SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation'],
        '_7077': ['SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation'],
        '_7078': ['SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation'],
        '_7079': ['SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation'],
        '_7080': ['SpringDamperAdvancedTimeSteppingAnalysisForModulation'],
        '_7081': ['SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation'],
        '_7082': ['SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation'],
        '_7083': ['StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation'],
        '_7084': ['StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation'],
        '_7085': ['StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation'],
        '_7086': ['StraightBevelGearAdvancedTimeSteppingAnalysisForModulation'],
        '_7087': ['StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation'],
        '_7088': ['StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation'],
        '_7089': ['StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation'],
        '_7090': ['StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation'],
        '_7091': ['SynchroniserAdvancedTimeSteppingAnalysisForModulation'],
        '_7092': ['SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation'],
        '_7093': ['SynchroniserPartAdvancedTimeSteppingAnalysisForModulation'],
        '_7094': ['SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation'],
        '_7095': ['TorqueConverterAdvancedTimeSteppingAnalysisForModulation'],
        '_7096': ['TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation'],
        '_7097': ['TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation'],
        '_7098': ['TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation'],
        '_7099': ['UnbalancedMassAdvancedTimeSteppingAnalysisForModulation'],
        '_7100': ['VirtualComponentAdvancedTimeSteppingAnalysisForModulation'],
        '_7101': ['WormGearAdvancedTimeSteppingAnalysisForModulation'],
        '_7102': ['WormGearMeshAdvancedTimeSteppingAnalysisForModulation'],
        '_7103': ['WormGearSetAdvancedTimeSteppingAnalysisForModulation'],
        '_7104': ['ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation'],
        '_7105': ['ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation'],
        '_7106': ['ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
