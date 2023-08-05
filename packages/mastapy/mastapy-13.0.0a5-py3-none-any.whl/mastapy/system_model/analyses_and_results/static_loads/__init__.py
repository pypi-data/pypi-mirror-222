"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6771 import LoadCase
    from ._6772 import StaticLoadCase
    from ._6773 import TimeSeriesLoadCase
    from ._6774 import AbstractAssemblyLoadCase
    from ._6775 import AbstractShaftLoadCase
    from ._6776 import AbstractShaftOrHousingLoadCase
    from ._6777 import AbstractShaftToMountableComponentConnectionLoadCase
    from ._6778 import AdditionalAccelerationOptions
    from ._6779 import AdvancedTimeSteppingAnalysisForModulationStaticLoadCase
    from ._6780 import AdvancedTimeSteppingAnalysisForModulationType
    from ._6781 import AGMAGleasonConicalGearLoadCase
    from ._6782 import AGMAGleasonConicalGearMeshLoadCase
    from ._6783 import AGMAGleasonConicalGearSetLoadCase
    from ._6784 import AllRingPinsManufacturingError
    from ._6785 import AnalysisType
    from ._6786 import AssemblyLoadCase
    from ._6787 import BearingLoadCase
    from ._6788 import BeltConnectionLoadCase
    from ._6789 import BeltDriveLoadCase
    from ._6790 import BevelDifferentialGearLoadCase
    from ._6791 import BevelDifferentialGearMeshLoadCase
    from ._6792 import BevelDifferentialGearSetLoadCase
    from ._6793 import BevelDifferentialPlanetGearLoadCase
    from ._6794 import BevelDifferentialSunGearLoadCase
    from ._6795 import BevelGearLoadCase
    from ._6796 import BevelGearMeshLoadCase
    from ._6797 import BevelGearSetLoadCase
    from ._6798 import BoltedJointLoadCase
    from ._6799 import BoltLoadCase
    from ._6800 import ClutchConnectionLoadCase
    from ._6801 import ClutchHalfLoadCase
    from ._6802 import ClutchLoadCase
    from ._6803 import CMSElementFaceGroupWithSelectionOption
    from ._6804 import CoaxialConnectionLoadCase
    from ._6805 import ComponentLoadCase
    from ._6806 import ConceptCouplingConnectionLoadCase
    from ._6807 import ConceptCouplingHalfLoadCase
    from ._6808 import ConceptCouplingLoadCase
    from ._6809 import ConceptGearLoadCase
    from ._6810 import ConceptGearMeshLoadCase
    from ._6811 import ConceptGearSetLoadCase
    from ._6812 import ConicalGearLoadCase
    from ._6813 import ConicalGearManufactureError
    from ._6814 import ConicalGearMeshLoadCase
    from ._6815 import ConicalGearSetHarmonicLoadData
    from ._6816 import ConicalGearSetLoadCase
    from ._6817 import ConnectionLoadCase
    from ._6818 import ConnectorLoadCase
    from ._6819 import CouplingConnectionLoadCase
    from ._6820 import CouplingHalfLoadCase
    from ._6821 import CouplingLoadCase
    from ._6822 import CVTBeltConnectionLoadCase
    from ._6823 import CVTLoadCase
    from ._6824 import CVTPulleyLoadCase
    from ._6825 import CycloidalAssemblyLoadCase
    from ._6826 import CycloidalDiscCentralBearingConnectionLoadCase
    from ._6827 import CycloidalDiscLoadCase
    from ._6828 import CycloidalDiscPlanetaryBearingConnectionLoadCase
    from ._6829 import CylindricalGearLoadCase
    from ._6830 import CylindricalGearManufactureError
    from ._6831 import CylindricalGearMeshLoadCase
    from ._6832 import CylindricalGearSetHarmonicLoadData
    from ._6833 import CylindricalGearSetLoadCase
    from ._6834 import CylindricalPlanetGearLoadCase
    from ._6835 import DataFromMotorPackagePerMeanTorque
    from ._6836 import DataFromMotorPackagePerSpeed
    from ._6837 import DatumLoadCase
    from ._6838 import ElectricMachineDataImportType
    from ._6839 import ElectricMachineHarmonicLoadData
    from ._6840 import ElectricMachineHarmonicLoadDataFromExcel
    from ._6841 import ElectricMachineHarmonicLoadDataFromFlux
    from ._6842 import ElectricMachineHarmonicLoadDataFromJMAG
    from ._6843 import ElectricMachineHarmonicLoadDataFromMASTA
    from ._6844 import ElectricMachineHarmonicLoadDataFromMotorCAD
    from ._6845 import ElectricMachineHarmonicLoadDataFromMotorPackages
    from ._6846 import ElectricMachineHarmonicLoadExcelImportOptions
    from ._6847 import ElectricMachineHarmonicLoadFluxImportOptions
    from ._6848 import ElectricMachineHarmonicLoadImportOptionsBase
    from ._6849 import ElectricMachineHarmonicLoadJMAGImportOptions
    from ._6850 import ElectricMachineHarmonicLoadMotorCADImportOptions
    from ._6851 import ExternalCADModelLoadCase
    from ._6852 import FaceGearLoadCase
    from ._6853 import FaceGearMeshLoadCase
    from ._6854 import FaceGearSetLoadCase
    from ._6855 import FEPartLoadCase
    from ._6856 import FlexiblePinAssemblyLoadCase
    from ._6857 import ForceAndTorqueScalingFactor
    from ._6858 import GearLoadCase
    from ._6859 import GearManufactureError
    from ._6860 import GearMeshLoadCase
    from ._6861 import GearMeshTEOrderType
    from ._6862 import GearSetHarmonicLoadData
    from ._6863 import GearSetLoadCase
    from ._6864 import GuideDxfModelLoadCase
    from ._6865 import HarmonicExcitationType
    from ._6866 import HarmonicLoadDataCSVImport
    from ._6867 import HarmonicLoadDataExcelImport
    from ._6868 import HarmonicLoadDataFluxImport
    from ._6869 import HarmonicLoadDataImportBase
    from ._6870 import HarmonicLoadDataImportFromMotorPackages
    from ._6871 import HarmonicLoadDataJMAGImport
    from ._6872 import HarmonicLoadDataMotorCADImport
    from ._6873 import HypoidGearLoadCase
    from ._6874 import HypoidGearMeshLoadCase
    from ._6875 import HypoidGearSetLoadCase
    from ._6876 import ImportType
    from ._6877 import InformationAtRingPinToDiscContactPointFromGeometry
    from ._6878 import InnerDiameterReference
    from ._6879 import InterMountableComponentConnectionLoadCase
    from ._6880 import KlingelnbergCycloPalloidConicalGearLoadCase
    from ._6881 import KlingelnbergCycloPalloidConicalGearMeshLoadCase
    from ._6882 import KlingelnbergCycloPalloidConicalGearSetLoadCase
    from ._6883 import KlingelnbergCycloPalloidHypoidGearLoadCase
    from ._6884 import KlingelnbergCycloPalloidHypoidGearMeshLoadCase
    from ._6885 import KlingelnbergCycloPalloidHypoidGearSetLoadCase
    from ._6886 import KlingelnbergCycloPalloidSpiralBevelGearLoadCase
    from ._6887 import KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
    from ._6888 import KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
    from ._6889 import MassDiscLoadCase
    from ._6890 import MeasurementComponentLoadCase
    from ._6891 import MeshStiffnessSource
    from ._6892 import MountableComponentLoadCase
    from ._6893 import NamedSpeed
    from ._6894 import OilSealLoadCase
    from ._6895 import ParametricStudyType
    from ._6896 import PartLoadCase
    from ._6897 import PartToPartShearCouplingConnectionLoadCase
    from ._6898 import PartToPartShearCouplingHalfLoadCase
    from ._6899 import PartToPartShearCouplingLoadCase
    from ._6900 import PlanetaryConnectionLoadCase
    from ._6901 import PlanetaryGearSetLoadCase
    from ._6902 import PlanetarySocketManufactureError
    from ._6903 import PlanetCarrierLoadCase
    from ._6904 import PlanetManufactureError
    from ._6905 import PointLoadHarmonicLoadData
    from ._6906 import PointLoadLoadCase
    from ._6907 import PowerLoadLoadCase
    from ._6908 import PulleyLoadCase
    from ._6909 import ResetMicroGeometryOptions
    from ._6910 import RingPinManufacturingError
    from ._6911 import RingPinsLoadCase
    from ._6912 import RingPinsToDiscConnectionLoadCase
    from ._6913 import RollingRingAssemblyLoadCase
    from ._6914 import RollingRingConnectionLoadCase
    from ._6915 import RollingRingLoadCase
    from ._6916 import RootAssemblyLoadCase
    from ._6917 import ShaftHubConnectionLoadCase
    from ._6918 import ShaftLoadCase
    from ._6919 import ShaftToMountableComponentConnectionLoadCase
    from ._6920 import SpecialisedAssemblyLoadCase
    from ._6921 import SpiralBevelGearLoadCase
    from ._6922 import SpiralBevelGearMeshLoadCase
    from ._6923 import SpiralBevelGearSetLoadCase
    from ._6924 import SpringDamperConnectionLoadCase
    from ._6925 import SpringDamperHalfLoadCase
    from ._6926 import SpringDamperLoadCase
    from ._6927 import StraightBevelDiffGearLoadCase
    from ._6928 import StraightBevelDiffGearMeshLoadCase
    from ._6929 import StraightBevelDiffGearSetLoadCase
    from ._6930 import StraightBevelGearLoadCase
    from ._6931 import StraightBevelGearMeshLoadCase
    from ._6932 import StraightBevelGearSetLoadCase
    from ._6933 import StraightBevelPlanetGearLoadCase
    from ._6934 import StraightBevelSunGearLoadCase
    from ._6935 import SynchroniserHalfLoadCase
    from ._6936 import SynchroniserLoadCase
    from ._6937 import SynchroniserPartLoadCase
    from ._6938 import SynchroniserSleeveLoadCase
    from ._6939 import TEExcitationType
    from ._6940 import TorqueConverterConnectionLoadCase
    from ._6941 import TorqueConverterLoadCase
    from ._6942 import TorqueConverterPumpLoadCase
    from ._6943 import TorqueConverterTurbineLoadCase
    from ._6944 import TorqueRippleInputType
    from ._6945 import TorqueSpecificationForSystemDeflection
    from ._6946 import TransmissionEfficiencySettings
    from ._6947 import UnbalancedMassHarmonicLoadData
    from ._6948 import UnbalancedMassLoadCase
    from ._6949 import VirtualComponentLoadCase
    from ._6950 import WormGearLoadCase
    from ._6951 import WormGearMeshLoadCase
    from ._6952 import WormGearSetLoadCase
    from ._6953 import ZerolBevelGearLoadCase
    from ._6954 import ZerolBevelGearMeshLoadCase
    from ._6955 import ZerolBevelGearSetLoadCase
else:
    import_structure = {
        '_6771': ['LoadCase'],
        '_6772': ['StaticLoadCase'],
        '_6773': ['TimeSeriesLoadCase'],
        '_6774': ['AbstractAssemblyLoadCase'],
        '_6775': ['AbstractShaftLoadCase'],
        '_6776': ['AbstractShaftOrHousingLoadCase'],
        '_6777': ['AbstractShaftToMountableComponentConnectionLoadCase'],
        '_6778': ['AdditionalAccelerationOptions'],
        '_6779': ['AdvancedTimeSteppingAnalysisForModulationStaticLoadCase'],
        '_6780': ['AdvancedTimeSteppingAnalysisForModulationType'],
        '_6781': ['AGMAGleasonConicalGearLoadCase'],
        '_6782': ['AGMAGleasonConicalGearMeshLoadCase'],
        '_6783': ['AGMAGleasonConicalGearSetLoadCase'],
        '_6784': ['AllRingPinsManufacturingError'],
        '_6785': ['AnalysisType'],
        '_6786': ['AssemblyLoadCase'],
        '_6787': ['BearingLoadCase'],
        '_6788': ['BeltConnectionLoadCase'],
        '_6789': ['BeltDriveLoadCase'],
        '_6790': ['BevelDifferentialGearLoadCase'],
        '_6791': ['BevelDifferentialGearMeshLoadCase'],
        '_6792': ['BevelDifferentialGearSetLoadCase'],
        '_6793': ['BevelDifferentialPlanetGearLoadCase'],
        '_6794': ['BevelDifferentialSunGearLoadCase'],
        '_6795': ['BevelGearLoadCase'],
        '_6796': ['BevelGearMeshLoadCase'],
        '_6797': ['BevelGearSetLoadCase'],
        '_6798': ['BoltedJointLoadCase'],
        '_6799': ['BoltLoadCase'],
        '_6800': ['ClutchConnectionLoadCase'],
        '_6801': ['ClutchHalfLoadCase'],
        '_6802': ['ClutchLoadCase'],
        '_6803': ['CMSElementFaceGroupWithSelectionOption'],
        '_6804': ['CoaxialConnectionLoadCase'],
        '_6805': ['ComponentLoadCase'],
        '_6806': ['ConceptCouplingConnectionLoadCase'],
        '_6807': ['ConceptCouplingHalfLoadCase'],
        '_6808': ['ConceptCouplingLoadCase'],
        '_6809': ['ConceptGearLoadCase'],
        '_6810': ['ConceptGearMeshLoadCase'],
        '_6811': ['ConceptGearSetLoadCase'],
        '_6812': ['ConicalGearLoadCase'],
        '_6813': ['ConicalGearManufactureError'],
        '_6814': ['ConicalGearMeshLoadCase'],
        '_6815': ['ConicalGearSetHarmonicLoadData'],
        '_6816': ['ConicalGearSetLoadCase'],
        '_6817': ['ConnectionLoadCase'],
        '_6818': ['ConnectorLoadCase'],
        '_6819': ['CouplingConnectionLoadCase'],
        '_6820': ['CouplingHalfLoadCase'],
        '_6821': ['CouplingLoadCase'],
        '_6822': ['CVTBeltConnectionLoadCase'],
        '_6823': ['CVTLoadCase'],
        '_6824': ['CVTPulleyLoadCase'],
        '_6825': ['CycloidalAssemblyLoadCase'],
        '_6826': ['CycloidalDiscCentralBearingConnectionLoadCase'],
        '_6827': ['CycloidalDiscLoadCase'],
        '_6828': ['CycloidalDiscPlanetaryBearingConnectionLoadCase'],
        '_6829': ['CylindricalGearLoadCase'],
        '_6830': ['CylindricalGearManufactureError'],
        '_6831': ['CylindricalGearMeshLoadCase'],
        '_6832': ['CylindricalGearSetHarmonicLoadData'],
        '_6833': ['CylindricalGearSetLoadCase'],
        '_6834': ['CylindricalPlanetGearLoadCase'],
        '_6835': ['DataFromMotorPackagePerMeanTorque'],
        '_6836': ['DataFromMotorPackagePerSpeed'],
        '_6837': ['DatumLoadCase'],
        '_6838': ['ElectricMachineDataImportType'],
        '_6839': ['ElectricMachineHarmonicLoadData'],
        '_6840': ['ElectricMachineHarmonicLoadDataFromExcel'],
        '_6841': ['ElectricMachineHarmonicLoadDataFromFlux'],
        '_6842': ['ElectricMachineHarmonicLoadDataFromJMAG'],
        '_6843': ['ElectricMachineHarmonicLoadDataFromMASTA'],
        '_6844': ['ElectricMachineHarmonicLoadDataFromMotorCAD'],
        '_6845': ['ElectricMachineHarmonicLoadDataFromMotorPackages'],
        '_6846': ['ElectricMachineHarmonicLoadExcelImportOptions'],
        '_6847': ['ElectricMachineHarmonicLoadFluxImportOptions'],
        '_6848': ['ElectricMachineHarmonicLoadImportOptionsBase'],
        '_6849': ['ElectricMachineHarmonicLoadJMAGImportOptions'],
        '_6850': ['ElectricMachineHarmonicLoadMotorCADImportOptions'],
        '_6851': ['ExternalCADModelLoadCase'],
        '_6852': ['FaceGearLoadCase'],
        '_6853': ['FaceGearMeshLoadCase'],
        '_6854': ['FaceGearSetLoadCase'],
        '_6855': ['FEPartLoadCase'],
        '_6856': ['FlexiblePinAssemblyLoadCase'],
        '_6857': ['ForceAndTorqueScalingFactor'],
        '_6858': ['GearLoadCase'],
        '_6859': ['GearManufactureError'],
        '_6860': ['GearMeshLoadCase'],
        '_6861': ['GearMeshTEOrderType'],
        '_6862': ['GearSetHarmonicLoadData'],
        '_6863': ['GearSetLoadCase'],
        '_6864': ['GuideDxfModelLoadCase'],
        '_6865': ['HarmonicExcitationType'],
        '_6866': ['HarmonicLoadDataCSVImport'],
        '_6867': ['HarmonicLoadDataExcelImport'],
        '_6868': ['HarmonicLoadDataFluxImport'],
        '_6869': ['HarmonicLoadDataImportBase'],
        '_6870': ['HarmonicLoadDataImportFromMotorPackages'],
        '_6871': ['HarmonicLoadDataJMAGImport'],
        '_6872': ['HarmonicLoadDataMotorCADImport'],
        '_6873': ['HypoidGearLoadCase'],
        '_6874': ['HypoidGearMeshLoadCase'],
        '_6875': ['HypoidGearSetLoadCase'],
        '_6876': ['ImportType'],
        '_6877': ['InformationAtRingPinToDiscContactPointFromGeometry'],
        '_6878': ['InnerDiameterReference'],
        '_6879': ['InterMountableComponentConnectionLoadCase'],
        '_6880': ['KlingelnbergCycloPalloidConicalGearLoadCase'],
        '_6881': ['KlingelnbergCycloPalloidConicalGearMeshLoadCase'],
        '_6882': ['KlingelnbergCycloPalloidConicalGearSetLoadCase'],
        '_6883': ['KlingelnbergCycloPalloidHypoidGearLoadCase'],
        '_6884': ['KlingelnbergCycloPalloidHypoidGearMeshLoadCase'],
        '_6885': ['KlingelnbergCycloPalloidHypoidGearSetLoadCase'],
        '_6886': ['KlingelnbergCycloPalloidSpiralBevelGearLoadCase'],
        '_6887': ['KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase'],
        '_6888': ['KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase'],
        '_6889': ['MassDiscLoadCase'],
        '_6890': ['MeasurementComponentLoadCase'],
        '_6891': ['MeshStiffnessSource'],
        '_6892': ['MountableComponentLoadCase'],
        '_6893': ['NamedSpeed'],
        '_6894': ['OilSealLoadCase'],
        '_6895': ['ParametricStudyType'],
        '_6896': ['PartLoadCase'],
        '_6897': ['PartToPartShearCouplingConnectionLoadCase'],
        '_6898': ['PartToPartShearCouplingHalfLoadCase'],
        '_6899': ['PartToPartShearCouplingLoadCase'],
        '_6900': ['PlanetaryConnectionLoadCase'],
        '_6901': ['PlanetaryGearSetLoadCase'],
        '_6902': ['PlanetarySocketManufactureError'],
        '_6903': ['PlanetCarrierLoadCase'],
        '_6904': ['PlanetManufactureError'],
        '_6905': ['PointLoadHarmonicLoadData'],
        '_6906': ['PointLoadLoadCase'],
        '_6907': ['PowerLoadLoadCase'],
        '_6908': ['PulleyLoadCase'],
        '_6909': ['ResetMicroGeometryOptions'],
        '_6910': ['RingPinManufacturingError'],
        '_6911': ['RingPinsLoadCase'],
        '_6912': ['RingPinsToDiscConnectionLoadCase'],
        '_6913': ['RollingRingAssemblyLoadCase'],
        '_6914': ['RollingRingConnectionLoadCase'],
        '_6915': ['RollingRingLoadCase'],
        '_6916': ['RootAssemblyLoadCase'],
        '_6917': ['ShaftHubConnectionLoadCase'],
        '_6918': ['ShaftLoadCase'],
        '_6919': ['ShaftToMountableComponentConnectionLoadCase'],
        '_6920': ['SpecialisedAssemblyLoadCase'],
        '_6921': ['SpiralBevelGearLoadCase'],
        '_6922': ['SpiralBevelGearMeshLoadCase'],
        '_6923': ['SpiralBevelGearSetLoadCase'],
        '_6924': ['SpringDamperConnectionLoadCase'],
        '_6925': ['SpringDamperHalfLoadCase'],
        '_6926': ['SpringDamperLoadCase'],
        '_6927': ['StraightBevelDiffGearLoadCase'],
        '_6928': ['StraightBevelDiffGearMeshLoadCase'],
        '_6929': ['StraightBevelDiffGearSetLoadCase'],
        '_6930': ['StraightBevelGearLoadCase'],
        '_6931': ['StraightBevelGearMeshLoadCase'],
        '_6932': ['StraightBevelGearSetLoadCase'],
        '_6933': ['StraightBevelPlanetGearLoadCase'],
        '_6934': ['StraightBevelSunGearLoadCase'],
        '_6935': ['SynchroniserHalfLoadCase'],
        '_6936': ['SynchroniserLoadCase'],
        '_6937': ['SynchroniserPartLoadCase'],
        '_6938': ['SynchroniserSleeveLoadCase'],
        '_6939': ['TEExcitationType'],
        '_6940': ['TorqueConverterConnectionLoadCase'],
        '_6941': ['TorqueConverterLoadCase'],
        '_6942': ['TorqueConverterPumpLoadCase'],
        '_6943': ['TorqueConverterTurbineLoadCase'],
        '_6944': ['TorqueRippleInputType'],
        '_6945': ['TorqueSpecificationForSystemDeflection'],
        '_6946': ['TransmissionEfficiencySettings'],
        '_6947': ['UnbalancedMassHarmonicLoadData'],
        '_6948': ['UnbalancedMassLoadCase'],
        '_6949': ['VirtualComponentLoadCase'],
        '_6950': ['WormGearLoadCase'],
        '_6951': ['WormGearMeshLoadCase'],
        '_6952': ['WormGearSetLoadCase'],
        '_6953': ['ZerolBevelGearLoadCase'],
        '_6954': ['ZerolBevelGearMeshLoadCase'],
        '_6955': ['ZerolBevelGearSetLoadCase'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
