"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._995 import AddendumModificationDistributionRule
    from ._996 import BacklashSpecification
    from ._997 import BasicRackProfiles
    from ._998 import CaseHardeningProperties
    from ._999 import CreateNewSuitableCutterOption
    from ._1000 import CrossedAxisCylindricalGearPair
    from ._1001 import CrossedAxisCylindricalGearPairLineContact
    from ._1002 import CrossedAxisCylindricalGearPairPointContact
    from ._1003 import CylindricalGearAbstractRack
    from ._1004 import CylindricalGearAbstractRackFlank
    from ._1005 import CylindricalGearBasicRack
    from ._1006 import CylindricalGearBasicRackFlank
    from ._1007 import CylindricalGearCuttingOptions
    from ._1008 import CylindricalGearDefaults
    from ._1009 import CylindricalGearDesign
    from ._1010 import CylindricalGearDesignConstraint
    from ._1011 import CylindricalGearDesignConstraints
    from ._1012 import CylindricalGearDesignConstraintsDatabase
    from ._1013 import CylindricalGearDesignConstraintSettings
    from ._1014 import CylindricalGearFlankDesign
    from ._1015 import CylindricalGearMeshDesign
    from ._1016 import CylindricalGearMeshFlankDesign
    from ._1017 import CylindricalGearMicroGeometrySettings
    from ._1018 import CylindricalGearMicroGeometrySettingsDatabase
    from ._1019 import CylindricalGearMicroGeometrySettingsItem
    from ._1020 import CylindricalGearPinionTypeCutter
    from ._1021 import CylindricalGearPinionTypeCutterFlank
    from ._1022 import CylindricalGearProfileMeasurement
    from ._1023 import CylindricalGearProfileMeasurementType
    from ._1024 import CylindricalGearProfileModifications
    from ._1025 import CylindricalGearSetDesign
    from ._1026 import CylindricalGearSetFlankDesign
    from ._1027 import CylindricalGearSetMacroGeometryOptimiser
    from ._1028 import CylindricalGearSetManufacturingConfigurationSelection
    from ._1029 import CylindricalGearSetMicroGeometrySettings
    from ._1030 import CylindricalGearTableMGItemDetail
    from ._1031 import CylindricalGearTableWithMGCharts
    from ._1032 import CylindricalGearToothThicknessSpecification
    from ._1033 import CylindricalMeshAngularBacklash
    from ._1034 import CylindricalMeshedGear
    from ._1035 import CylindricalMeshedGearFlank
    from ._1036 import CylindricalMeshLinearBacklashSpecification
    from ._1037 import CylindricalPlanetaryGearSetDesign
    from ._1038 import CylindricalPlanetGearDesign
    from ._1039 import DIN3967AllowanceSeries
    from ._1040 import DIN3967ToleranceSeries
    from ._1041 import DoubleAxisScaleAndRange
    from ._1042 import FinishToothThicknessDesignSpecification
    from ._1043 import GearFitSystems
    from ._1044 import GearManufacturingConfigSetupViewModel
    from ._1045 import GearSetManufacturingConfigurationSetup
    from ._1046 import GeometrySpecificationType
    from ._1047 import HardenedMaterialProperties
    from ._1048 import HardnessProfileCalculationMethod
    from ._1049 import HeatTreatmentType
    from ._1050 import ISO6336Geometry
    from ._1051 import ISO6336GeometryBase
    from ._1052 import ISO6336GeometryForShapedGears
    from ._1053 import ISO6336GeometryManufactured
    from ._1054 import LinearBacklashSpecification
    from ._1055 import LTCALoadCaseModifiableSettings
    from ._1056 import LTCASettings
    from ._1057 import MicroGeometryConvention
    from ._1058 import MicroGeometryProfileConvention
    from ._1059 import Micropitting
    from ._1060 import NamedPlanetAssemblyIndex
    from ._1061 import NamedPlanetSideBandAmplitudeFactor
    from ._1062 import ReadonlyToothThicknessSpecification
    from ._1063 import RelativeMeasurementViewModel
    from ._1064 import RelativeValuesSpecification
    from ._1065 import RootStressSurfaceChartOption
    from ._1066 import Scuffing
    from ._1067 import ScuffingCoefficientOfFrictionMethods
    from ._1068 import ScuffingTemperatureMethodsAGMA
    from ._1069 import ScuffingTemperatureMethodsISO
    from ._1070 import ShaperEdgeTypes
    from ._1071 import SpurGearLoadSharingCodes
    from ._1072 import StandardRack
    from ._1073 import StandardRackFlank
    from ._1074 import SurfaceRoughness
    from ._1075 import ThicknessType
    from ._1076 import TiffAnalysisSettings
    from ._1077 import TipAlterationCoefficientMethod
    from ._1078 import TolerancedMetalMeasurements
    from ._1079 import TolerancedValueSpecification
    from ._1080 import ToothFlankFractureAnalysisSettings
    from ._1081 import ToothThicknessSpecification
    from ._1082 import ToothThicknessSpecificationBase
    from ._1083 import TypeOfMechanismHousing
    from ._1084 import Usage
else:
    import_structure = {
        '_995': ['AddendumModificationDistributionRule'],
        '_996': ['BacklashSpecification'],
        '_997': ['BasicRackProfiles'],
        '_998': ['CaseHardeningProperties'],
        '_999': ['CreateNewSuitableCutterOption'],
        '_1000': ['CrossedAxisCylindricalGearPair'],
        '_1001': ['CrossedAxisCylindricalGearPairLineContact'],
        '_1002': ['CrossedAxisCylindricalGearPairPointContact'],
        '_1003': ['CylindricalGearAbstractRack'],
        '_1004': ['CylindricalGearAbstractRackFlank'],
        '_1005': ['CylindricalGearBasicRack'],
        '_1006': ['CylindricalGearBasicRackFlank'],
        '_1007': ['CylindricalGearCuttingOptions'],
        '_1008': ['CylindricalGearDefaults'],
        '_1009': ['CylindricalGearDesign'],
        '_1010': ['CylindricalGearDesignConstraint'],
        '_1011': ['CylindricalGearDesignConstraints'],
        '_1012': ['CylindricalGearDesignConstraintsDatabase'],
        '_1013': ['CylindricalGearDesignConstraintSettings'],
        '_1014': ['CylindricalGearFlankDesign'],
        '_1015': ['CylindricalGearMeshDesign'],
        '_1016': ['CylindricalGearMeshFlankDesign'],
        '_1017': ['CylindricalGearMicroGeometrySettings'],
        '_1018': ['CylindricalGearMicroGeometrySettingsDatabase'],
        '_1019': ['CylindricalGearMicroGeometrySettingsItem'],
        '_1020': ['CylindricalGearPinionTypeCutter'],
        '_1021': ['CylindricalGearPinionTypeCutterFlank'],
        '_1022': ['CylindricalGearProfileMeasurement'],
        '_1023': ['CylindricalGearProfileMeasurementType'],
        '_1024': ['CylindricalGearProfileModifications'],
        '_1025': ['CylindricalGearSetDesign'],
        '_1026': ['CylindricalGearSetFlankDesign'],
        '_1027': ['CylindricalGearSetMacroGeometryOptimiser'],
        '_1028': ['CylindricalGearSetManufacturingConfigurationSelection'],
        '_1029': ['CylindricalGearSetMicroGeometrySettings'],
        '_1030': ['CylindricalGearTableMGItemDetail'],
        '_1031': ['CylindricalGearTableWithMGCharts'],
        '_1032': ['CylindricalGearToothThicknessSpecification'],
        '_1033': ['CylindricalMeshAngularBacklash'],
        '_1034': ['CylindricalMeshedGear'],
        '_1035': ['CylindricalMeshedGearFlank'],
        '_1036': ['CylindricalMeshLinearBacklashSpecification'],
        '_1037': ['CylindricalPlanetaryGearSetDesign'],
        '_1038': ['CylindricalPlanetGearDesign'],
        '_1039': ['DIN3967AllowanceSeries'],
        '_1040': ['DIN3967ToleranceSeries'],
        '_1041': ['DoubleAxisScaleAndRange'],
        '_1042': ['FinishToothThicknessDesignSpecification'],
        '_1043': ['GearFitSystems'],
        '_1044': ['GearManufacturingConfigSetupViewModel'],
        '_1045': ['GearSetManufacturingConfigurationSetup'],
        '_1046': ['GeometrySpecificationType'],
        '_1047': ['HardenedMaterialProperties'],
        '_1048': ['HardnessProfileCalculationMethod'],
        '_1049': ['HeatTreatmentType'],
        '_1050': ['ISO6336Geometry'],
        '_1051': ['ISO6336GeometryBase'],
        '_1052': ['ISO6336GeometryForShapedGears'],
        '_1053': ['ISO6336GeometryManufactured'],
        '_1054': ['LinearBacklashSpecification'],
        '_1055': ['LTCALoadCaseModifiableSettings'],
        '_1056': ['LTCASettings'],
        '_1057': ['MicroGeometryConvention'],
        '_1058': ['MicroGeometryProfileConvention'],
        '_1059': ['Micropitting'],
        '_1060': ['NamedPlanetAssemblyIndex'],
        '_1061': ['NamedPlanetSideBandAmplitudeFactor'],
        '_1062': ['ReadonlyToothThicknessSpecification'],
        '_1063': ['RelativeMeasurementViewModel'],
        '_1064': ['RelativeValuesSpecification'],
        '_1065': ['RootStressSurfaceChartOption'],
        '_1066': ['Scuffing'],
        '_1067': ['ScuffingCoefficientOfFrictionMethods'],
        '_1068': ['ScuffingTemperatureMethodsAGMA'],
        '_1069': ['ScuffingTemperatureMethodsISO'],
        '_1070': ['ShaperEdgeTypes'],
        '_1071': ['SpurGearLoadSharingCodes'],
        '_1072': ['StandardRack'],
        '_1073': ['StandardRackFlank'],
        '_1074': ['SurfaceRoughness'],
        '_1075': ['ThicknessType'],
        '_1076': ['TiffAnalysisSettings'],
        '_1077': ['TipAlterationCoefficientMethod'],
        '_1078': ['TolerancedMetalMeasurements'],
        '_1079': ['TolerancedValueSpecification'],
        '_1080': ['ToothFlankFractureAnalysisSettings'],
        '_1081': ['ToothThicknessSpecification'],
        '_1082': ['ToothThicknessSpecificationBase'],
        '_1083': ['TypeOfMechanismHousing'],
        '_1084': ['Usage'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
