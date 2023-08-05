"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5849 import AbstractAssemblyCompoundHarmonicAnalysis
    from ._5850 import AbstractShaftCompoundHarmonicAnalysis
    from ._5851 import AbstractShaftOrHousingCompoundHarmonicAnalysis
    from ._5852 import AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis
    from ._5853 import AGMAGleasonConicalGearCompoundHarmonicAnalysis
    from ._5854 import AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
    from ._5855 import AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
    from ._5856 import AssemblyCompoundHarmonicAnalysis
    from ._5857 import BearingCompoundHarmonicAnalysis
    from ._5858 import BeltConnectionCompoundHarmonicAnalysis
    from ._5859 import BeltDriveCompoundHarmonicAnalysis
    from ._5860 import BevelDifferentialGearCompoundHarmonicAnalysis
    from ._5861 import BevelDifferentialGearMeshCompoundHarmonicAnalysis
    from ._5862 import BevelDifferentialGearSetCompoundHarmonicAnalysis
    from ._5863 import BevelDifferentialPlanetGearCompoundHarmonicAnalysis
    from ._5864 import BevelDifferentialSunGearCompoundHarmonicAnalysis
    from ._5865 import BevelGearCompoundHarmonicAnalysis
    from ._5866 import BevelGearMeshCompoundHarmonicAnalysis
    from ._5867 import BevelGearSetCompoundHarmonicAnalysis
    from ._5868 import BoltCompoundHarmonicAnalysis
    from ._5869 import BoltedJointCompoundHarmonicAnalysis
    from ._5870 import ClutchCompoundHarmonicAnalysis
    from ._5871 import ClutchConnectionCompoundHarmonicAnalysis
    from ._5872 import ClutchHalfCompoundHarmonicAnalysis
    from ._5873 import CoaxialConnectionCompoundHarmonicAnalysis
    from ._5874 import ComponentCompoundHarmonicAnalysis
    from ._5875 import ConceptCouplingCompoundHarmonicAnalysis
    from ._5876 import ConceptCouplingConnectionCompoundHarmonicAnalysis
    from ._5877 import ConceptCouplingHalfCompoundHarmonicAnalysis
    from ._5878 import ConceptGearCompoundHarmonicAnalysis
    from ._5879 import ConceptGearMeshCompoundHarmonicAnalysis
    from ._5880 import ConceptGearSetCompoundHarmonicAnalysis
    from ._5881 import ConicalGearCompoundHarmonicAnalysis
    from ._5882 import ConicalGearMeshCompoundHarmonicAnalysis
    from ._5883 import ConicalGearSetCompoundHarmonicAnalysis
    from ._5884 import ConnectionCompoundHarmonicAnalysis
    from ._5885 import ConnectorCompoundHarmonicAnalysis
    from ._5886 import CouplingCompoundHarmonicAnalysis
    from ._5887 import CouplingConnectionCompoundHarmonicAnalysis
    from ._5888 import CouplingHalfCompoundHarmonicAnalysis
    from ._5889 import CVTBeltConnectionCompoundHarmonicAnalysis
    from ._5890 import CVTCompoundHarmonicAnalysis
    from ._5891 import CVTPulleyCompoundHarmonicAnalysis
    from ._5892 import CycloidalAssemblyCompoundHarmonicAnalysis
    from ._5893 import CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis
    from ._5894 import CycloidalDiscCompoundHarmonicAnalysis
    from ._5895 import CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis
    from ._5896 import CylindricalGearCompoundHarmonicAnalysis
    from ._5897 import CylindricalGearMeshCompoundHarmonicAnalysis
    from ._5898 import CylindricalGearSetCompoundHarmonicAnalysis
    from ._5899 import CylindricalPlanetGearCompoundHarmonicAnalysis
    from ._5900 import DatumCompoundHarmonicAnalysis
    from ._5901 import ExternalCADModelCompoundHarmonicAnalysis
    from ._5902 import FaceGearCompoundHarmonicAnalysis
    from ._5903 import FaceGearMeshCompoundHarmonicAnalysis
    from ._5904 import FaceGearSetCompoundHarmonicAnalysis
    from ._5905 import FEPartCompoundHarmonicAnalysis
    from ._5906 import FlexiblePinAssemblyCompoundHarmonicAnalysis
    from ._5907 import GearCompoundHarmonicAnalysis
    from ._5908 import GearMeshCompoundHarmonicAnalysis
    from ._5909 import GearSetCompoundHarmonicAnalysis
    from ._5910 import GuideDxfModelCompoundHarmonicAnalysis
    from ._5911 import HypoidGearCompoundHarmonicAnalysis
    from ._5912 import HypoidGearMeshCompoundHarmonicAnalysis
    from ._5913 import HypoidGearSetCompoundHarmonicAnalysis
    from ._5914 import InterMountableComponentConnectionCompoundHarmonicAnalysis
    from ._5915 import KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
    from ._5916 import KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis
    from ._5917 import KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis
    from ._5918 import KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis
    from ._5919 import KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis
    from ._5920 import KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis
    from ._5921 import KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis
    from ._5922 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis
    from ._5923 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis
    from ._5924 import MassDiscCompoundHarmonicAnalysis
    from ._5925 import MeasurementComponentCompoundHarmonicAnalysis
    from ._5926 import MountableComponentCompoundHarmonicAnalysis
    from ._5927 import OilSealCompoundHarmonicAnalysis
    from ._5928 import PartCompoundHarmonicAnalysis
    from ._5929 import PartToPartShearCouplingCompoundHarmonicAnalysis
    from ._5930 import PartToPartShearCouplingConnectionCompoundHarmonicAnalysis
    from ._5931 import PartToPartShearCouplingHalfCompoundHarmonicAnalysis
    from ._5932 import PlanetaryConnectionCompoundHarmonicAnalysis
    from ._5933 import PlanetaryGearSetCompoundHarmonicAnalysis
    from ._5934 import PlanetCarrierCompoundHarmonicAnalysis
    from ._5935 import PointLoadCompoundHarmonicAnalysis
    from ._5936 import PowerLoadCompoundHarmonicAnalysis
    from ._5937 import PulleyCompoundHarmonicAnalysis
    from ._5938 import RingPinsCompoundHarmonicAnalysis
    from ._5939 import RingPinsToDiscConnectionCompoundHarmonicAnalysis
    from ._5940 import RollingRingAssemblyCompoundHarmonicAnalysis
    from ._5941 import RollingRingCompoundHarmonicAnalysis
    from ._5942 import RollingRingConnectionCompoundHarmonicAnalysis
    from ._5943 import RootAssemblyCompoundHarmonicAnalysis
    from ._5944 import ShaftCompoundHarmonicAnalysis
    from ._5945 import ShaftHubConnectionCompoundHarmonicAnalysis
    from ._5946 import ShaftToMountableComponentConnectionCompoundHarmonicAnalysis
    from ._5947 import SpecialisedAssemblyCompoundHarmonicAnalysis
    from ._5948 import SpiralBevelGearCompoundHarmonicAnalysis
    from ._5949 import SpiralBevelGearMeshCompoundHarmonicAnalysis
    from ._5950 import SpiralBevelGearSetCompoundHarmonicAnalysis
    from ._5951 import SpringDamperCompoundHarmonicAnalysis
    from ._5952 import SpringDamperConnectionCompoundHarmonicAnalysis
    from ._5953 import SpringDamperHalfCompoundHarmonicAnalysis
    from ._5954 import StraightBevelDiffGearCompoundHarmonicAnalysis
    from ._5955 import StraightBevelDiffGearMeshCompoundHarmonicAnalysis
    from ._5956 import StraightBevelDiffGearSetCompoundHarmonicAnalysis
    from ._5957 import StraightBevelGearCompoundHarmonicAnalysis
    from ._5958 import StraightBevelGearMeshCompoundHarmonicAnalysis
    from ._5959 import StraightBevelGearSetCompoundHarmonicAnalysis
    from ._5960 import StraightBevelPlanetGearCompoundHarmonicAnalysis
    from ._5961 import StraightBevelSunGearCompoundHarmonicAnalysis
    from ._5962 import SynchroniserCompoundHarmonicAnalysis
    from ._5963 import SynchroniserHalfCompoundHarmonicAnalysis
    from ._5964 import SynchroniserPartCompoundHarmonicAnalysis
    from ._5965 import SynchroniserSleeveCompoundHarmonicAnalysis
    from ._5966 import TorqueConverterCompoundHarmonicAnalysis
    from ._5967 import TorqueConverterConnectionCompoundHarmonicAnalysis
    from ._5968 import TorqueConverterPumpCompoundHarmonicAnalysis
    from ._5969 import TorqueConverterTurbineCompoundHarmonicAnalysis
    from ._5970 import UnbalancedMassCompoundHarmonicAnalysis
    from ._5971 import VirtualComponentCompoundHarmonicAnalysis
    from ._5972 import WormGearCompoundHarmonicAnalysis
    from ._5973 import WormGearMeshCompoundHarmonicAnalysis
    from ._5974 import WormGearSetCompoundHarmonicAnalysis
    from ._5975 import ZerolBevelGearCompoundHarmonicAnalysis
    from ._5976 import ZerolBevelGearMeshCompoundHarmonicAnalysis
    from ._5977 import ZerolBevelGearSetCompoundHarmonicAnalysis
else:
    import_structure = {
        '_5849': ['AbstractAssemblyCompoundHarmonicAnalysis'],
        '_5850': ['AbstractShaftCompoundHarmonicAnalysis'],
        '_5851': ['AbstractShaftOrHousingCompoundHarmonicAnalysis'],
        '_5852': ['AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis'],
        '_5853': ['AGMAGleasonConicalGearCompoundHarmonicAnalysis'],
        '_5854': ['AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis'],
        '_5855': ['AGMAGleasonConicalGearSetCompoundHarmonicAnalysis'],
        '_5856': ['AssemblyCompoundHarmonicAnalysis'],
        '_5857': ['BearingCompoundHarmonicAnalysis'],
        '_5858': ['BeltConnectionCompoundHarmonicAnalysis'],
        '_5859': ['BeltDriveCompoundHarmonicAnalysis'],
        '_5860': ['BevelDifferentialGearCompoundHarmonicAnalysis'],
        '_5861': ['BevelDifferentialGearMeshCompoundHarmonicAnalysis'],
        '_5862': ['BevelDifferentialGearSetCompoundHarmonicAnalysis'],
        '_5863': ['BevelDifferentialPlanetGearCompoundHarmonicAnalysis'],
        '_5864': ['BevelDifferentialSunGearCompoundHarmonicAnalysis'],
        '_5865': ['BevelGearCompoundHarmonicAnalysis'],
        '_5866': ['BevelGearMeshCompoundHarmonicAnalysis'],
        '_5867': ['BevelGearSetCompoundHarmonicAnalysis'],
        '_5868': ['BoltCompoundHarmonicAnalysis'],
        '_5869': ['BoltedJointCompoundHarmonicAnalysis'],
        '_5870': ['ClutchCompoundHarmonicAnalysis'],
        '_5871': ['ClutchConnectionCompoundHarmonicAnalysis'],
        '_5872': ['ClutchHalfCompoundHarmonicAnalysis'],
        '_5873': ['CoaxialConnectionCompoundHarmonicAnalysis'],
        '_5874': ['ComponentCompoundHarmonicAnalysis'],
        '_5875': ['ConceptCouplingCompoundHarmonicAnalysis'],
        '_5876': ['ConceptCouplingConnectionCompoundHarmonicAnalysis'],
        '_5877': ['ConceptCouplingHalfCompoundHarmonicAnalysis'],
        '_5878': ['ConceptGearCompoundHarmonicAnalysis'],
        '_5879': ['ConceptGearMeshCompoundHarmonicAnalysis'],
        '_5880': ['ConceptGearSetCompoundHarmonicAnalysis'],
        '_5881': ['ConicalGearCompoundHarmonicAnalysis'],
        '_5882': ['ConicalGearMeshCompoundHarmonicAnalysis'],
        '_5883': ['ConicalGearSetCompoundHarmonicAnalysis'],
        '_5884': ['ConnectionCompoundHarmonicAnalysis'],
        '_5885': ['ConnectorCompoundHarmonicAnalysis'],
        '_5886': ['CouplingCompoundHarmonicAnalysis'],
        '_5887': ['CouplingConnectionCompoundHarmonicAnalysis'],
        '_5888': ['CouplingHalfCompoundHarmonicAnalysis'],
        '_5889': ['CVTBeltConnectionCompoundHarmonicAnalysis'],
        '_5890': ['CVTCompoundHarmonicAnalysis'],
        '_5891': ['CVTPulleyCompoundHarmonicAnalysis'],
        '_5892': ['CycloidalAssemblyCompoundHarmonicAnalysis'],
        '_5893': ['CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis'],
        '_5894': ['CycloidalDiscCompoundHarmonicAnalysis'],
        '_5895': ['CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis'],
        '_5896': ['CylindricalGearCompoundHarmonicAnalysis'],
        '_5897': ['CylindricalGearMeshCompoundHarmonicAnalysis'],
        '_5898': ['CylindricalGearSetCompoundHarmonicAnalysis'],
        '_5899': ['CylindricalPlanetGearCompoundHarmonicAnalysis'],
        '_5900': ['DatumCompoundHarmonicAnalysis'],
        '_5901': ['ExternalCADModelCompoundHarmonicAnalysis'],
        '_5902': ['FaceGearCompoundHarmonicAnalysis'],
        '_5903': ['FaceGearMeshCompoundHarmonicAnalysis'],
        '_5904': ['FaceGearSetCompoundHarmonicAnalysis'],
        '_5905': ['FEPartCompoundHarmonicAnalysis'],
        '_5906': ['FlexiblePinAssemblyCompoundHarmonicAnalysis'],
        '_5907': ['GearCompoundHarmonicAnalysis'],
        '_5908': ['GearMeshCompoundHarmonicAnalysis'],
        '_5909': ['GearSetCompoundHarmonicAnalysis'],
        '_5910': ['GuideDxfModelCompoundHarmonicAnalysis'],
        '_5911': ['HypoidGearCompoundHarmonicAnalysis'],
        '_5912': ['HypoidGearMeshCompoundHarmonicAnalysis'],
        '_5913': ['HypoidGearSetCompoundHarmonicAnalysis'],
        '_5914': ['InterMountableComponentConnectionCompoundHarmonicAnalysis'],
        '_5915': ['KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis'],
        '_5916': ['KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis'],
        '_5917': ['KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis'],
        '_5918': ['KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis'],
        '_5919': ['KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis'],
        '_5920': ['KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis'],
        '_5921': ['KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis'],
        '_5922': ['KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis'],
        '_5923': ['KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis'],
        '_5924': ['MassDiscCompoundHarmonicAnalysis'],
        '_5925': ['MeasurementComponentCompoundHarmonicAnalysis'],
        '_5926': ['MountableComponentCompoundHarmonicAnalysis'],
        '_5927': ['OilSealCompoundHarmonicAnalysis'],
        '_5928': ['PartCompoundHarmonicAnalysis'],
        '_5929': ['PartToPartShearCouplingCompoundHarmonicAnalysis'],
        '_5930': ['PartToPartShearCouplingConnectionCompoundHarmonicAnalysis'],
        '_5931': ['PartToPartShearCouplingHalfCompoundHarmonicAnalysis'],
        '_5932': ['PlanetaryConnectionCompoundHarmonicAnalysis'],
        '_5933': ['PlanetaryGearSetCompoundHarmonicAnalysis'],
        '_5934': ['PlanetCarrierCompoundHarmonicAnalysis'],
        '_5935': ['PointLoadCompoundHarmonicAnalysis'],
        '_5936': ['PowerLoadCompoundHarmonicAnalysis'],
        '_5937': ['PulleyCompoundHarmonicAnalysis'],
        '_5938': ['RingPinsCompoundHarmonicAnalysis'],
        '_5939': ['RingPinsToDiscConnectionCompoundHarmonicAnalysis'],
        '_5940': ['RollingRingAssemblyCompoundHarmonicAnalysis'],
        '_5941': ['RollingRingCompoundHarmonicAnalysis'],
        '_5942': ['RollingRingConnectionCompoundHarmonicAnalysis'],
        '_5943': ['RootAssemblyCompoundHarmonicAnalysis'],
        '_5944': ['ShaftCompoundHarmonicAnalysis'],
        '_5945': ['ShaftHubConnectionCompoundHarmonicAnalysis'],
        '_5946': ['ShaftToMountableComponentConnectionCompoundHarmonicAnalysis'],
        '_5947': ['SpecialisedAssemblyCompoundHarmonicAnalysis'],
        '_5948': ['SpiralBevelGearCompoundHarmonicAnalysis'],
        '_5949': ['SpiralBevelGearMeshCompoundHarmonicAnalysis'],
        '_5950': ['SpiralBevelGearSetCompoundHarmonicAnalysis'],
        '_5951': ['SpringDamperCompoundHarmonicAnalysis'],
        '_5952': ['SpringDamperConnectionCompoundHarmonicAnalysis'],
        '_5953': ['SpringDamperHalfCompoundHarmonicAnalysis'],
        '_5954': ['StraightBevelDiffGearCompoundHarmonicAnalysis'],
        '_5955': ['StraightBevelDiffGearMeshCompoundHarmonicAnalysis'],
        '_5956': ['StraightBevelDiffGearSetCompoundHarmonicAnalysis'],
        '_5957': ['StraightBevelGearCompoundHarmonicAnalysis'],
        '_5958': ['StraightBevelGearMeshCompoundHarmonicAnalysis'],
        '_5959': ['StraightBevelGearSetCompoundHarmonicAnalysis'],
        '_5960': ['StraightBevelPlanetGearCompoundHarmonicAnalysis'],
        '_5961': ['StraightBevelSunGearCompoundHarmonicAnalysis'],
        '_5962': ['SynchroniserCompoundHarmonicAnalysis'],
        '_5963': ['SynchroniserHalfCompoundHarmonicAnalysis'],
        '_5964': ['SynchroniserPartCompoundHarmonicAnalysis'],
        '_5965': ['SynchroniserSleeveCompoundHarmonicAnalysis'],
        '_5966': ['TorqueConverterCompoundHarmonicAnalysis'],
        '_5967': ['TorqueConverterConnectionCompoundHarmonicAnalysis'],
        '_5968': ['TorqueConverterPumpCompoundHarmonicAnalysis'],
        '_5969': ['TorqueConverterTurbineCompoundHarmonicAnalysis'],
        '_5970': ['UnbalancedMassCompoundHarmonicAnalysis'],
        '_5971': ['VirtualComponentCompoundHarmonicAnalysis'],
        '_5972': ['WormGearCompoundHarmonicAnalysis'],
        '_5973': ['WormGearMeshCompoundHarmonicAnalysis'],
        '_5974': ['WormGearSetCompoundHarmonicAnalysis'],
        '_5975': ['ZerolBevelGearCompoundHarmonicAnalysis'],
        '_5976': ['ZerolBevelGearMeshCompoundHarmonicAnalysis'],
        '_5977': ['ZerolBevelGearSetCompoundHarmonicAnalysis'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
