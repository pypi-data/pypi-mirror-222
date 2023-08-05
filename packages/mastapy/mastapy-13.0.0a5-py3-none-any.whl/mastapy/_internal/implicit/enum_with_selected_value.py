﻿"""enum_with_selected_value.py

Implementations of 'EnumWithSelectedValue' in Python.
As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import List

from mastapy._internal import (
    mixins, enum_with_selected_value_runtime, constructor, conversion
)
from mastapy.shafts import _34, _45
from mastapy._internal.python_net import python_net_import
from mastapy.nodal_analysis import (
    _71, _91, _78, _87,
    _53
)
from mastapy.nodal_analysis.varying_input_components import _98
from mastapy.math_utility import (
    _1517, _1500, _1496, _1482,
    _1481, _1485, _1494
)
from mastapy.nodal_analysis.elmer import _172, _168
from mastapy.fe_tools.enums import _1238
from mastapy.materials import _259, _263, _249
from mastapy.gears import _335, _333, _336
from mastapy.gears.rating.cylindrical import _478, _479
from mastapy.gears.micro_geometry import (
    _570, _571, _572, _573
)
from mastapy.gears.manufacturing.cylindrical import (
    _620, _621, _624, _606
)
from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _642, _643, _640
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _655
from mastapy.geometry.two_d.curves import _311
from mastapy.gears.gear_designs.cylindrical import _1075, _1046, _1067
from mastapy.gears.gear_designs.conical import _1153, _1154, _1165
from mastapy.gears.gear_set_pareto_optimiser import _900
from mastapy.utility.model_validation import _1783, _1786
from mastapy.gears.ltca import _824
from mastapy.gears.gear_designs.creation_options import _1142
from mastapy.gears.gear_designs.bevel import _1186, _1175
from mastapy.fe_tools.vfx_tools.vfx_enums import _1235, _1236
from mastapy.electric_machines import _1248
from mastapy.electric_machines.load_cases_and_analyses import _1353
from mastapy.electric_machines.harmonic_load_data import _1372, _1369
from mastapy.bearings.tolerances import (
    _1897, _1910, _1890, _1889,
    _1891
)
from mastapy.detailed_rigid_connectors.splines import (
    _1384, _1407, _1393, _1394,
    _1402, _1408, _1385
)
from mastapy.detailed_rigid_connectors.interference_fits import _1438
from mastapy.utility.report import _1736
from mastapy.bearings import (
    _1871, _1878, _1879, _1857,
    _1858, _1882, _1884, _1864
)
from mastapy.bearings.bearing_results import (
    _1949, _1948, _1950, _1951
)
from mastapy.bearings.bearing_designs.rolling import _2139
from mastapy.materials.efficiency import _290, _298
from mastapy.system_model.part_model import _2458
from mastapy.system_model.drawing.options import _2245
from mastapy.utility.enums import _1811, _1812, _1810
from mastapy.system_model.fe import (
    _2349, _2394, _2371, _2346,
    _2381
)
from mastapy.system_model import (
    _2191, _2206, _2201, _2204
)
from mastapy.nodal_analysis.fe_export_utility import _166, _165
from mastapy.system_model.part_model.couplings import _2573, _2576, _2577
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4327
from mastapy.system_model.analyses_and_results.static_loads import (
    _6785, _6944, _6865, _6906,
    _6945
)
from mastapy.system_model.analyses_and_results.modal_analyses import _4603, _4604
from mastapy.system_model.analyses_and_results.mbd_analyses import (
    _5360, _5412, _5457, _5482
)
from mastapy.system_model.analyses_and_results.harmonic_analyses import (
    _5717, _5735, _5788, _5739
)
from mastapy.bearings.bearing_results.rolling import _1959, _1953
from mastapy.nodal_analysis.nodal_entities import _130
from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2096
from mastapy.math_utility.hertzian_contact import _1564
from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6959

_ARRAY = python_net_import('System', 'Array')
_ENUM_WITH_SELECTED_VALUE = python_net_import('SMT.MastaAPI.Utility.Property', 'EnumWithSelectedValue')


__docformat__ = 'restructuredtext en'
__all__ = (
    'EnumWithSelectedValue_ShaftRatingMethod', 'EnumWithSelectedValue_SurfaceFinishes',
    'EnumWithSelectedValue_IntegrationMethod', 'EnumWithSelectedValue_ValueInputOption',
    'EnumWithSelectedValue_SinglePointSelectionMethod', 'EnumWithSelectedValue_ResultOptionsFor3DVector',
    'EnumWithSelectedValue_ElmerResultType', 'EnumWithSelectedValue_ModeInputType',
    'EnumWithSelectedValue_MaterialPropertyClass', 'EnumWithSelectedValue_LubricantDefinition',
    'EnumWithSelectedValue_LubricantViscosityClassISO', 'EnumWithSelectedValue_MicroGeometryModel',
    'EnumWithSelectedValue_ExtrapolationOptions', 'EnumWithSelectedValue_CylindricalGearRatingMethods',
    'EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod', 'EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod',
    'EnumWithSelectedValue_LocationOfEvaluationLowerLimit', 'EnumWithSelectedValue_LocationOfEvaluationUpperLimit',
    'EnumWithSelectedValue_LocationOfRootReliefEvaluation', 'EnumWithSelectedValue_LocationOfTipReliefEvaluation',
    'EnumWithSelectedValue_CylindricalMftFinishingMethods', 'EnumWithSelectedValue_CylindricalMftRoughingMethods',
    'EnumWithSelectedValue_MicroGeometryDefinitionMethod', 'EnumWithSelectedValue_MicroGeometryDefinitionType',
    'EnumWithSelectedValue_ChartType', 'EnumWithSelectedValue_Flank',
    'EnumWithSelectedValue_ActiveProcessMethod', 'EnumWithSelectedValue_CutterFlankSections',
    'EnumWithSelectedValue_BasicCurveTypes', 'EnumWithSelectedValue_ThicknessType',
    'EnumWithSelectedValue_ConicalMachineSettingCalculationMethods', 'EnumWithSelectedValue_ConicalManufactureMethods',
    'EnumWithSelectedValue_CandidateDisplayChoice', 'EnumWithSelectedValue_Severity',
    'EnumWithSelectedValue_GeometrySpecificationType', 'EnumWithSelectedValue_StatusItemSeverity',
    'EnumWithSelectedValue_LubricationMethods', 'EnumWithSelectedValue_MicropittingCoefficientOfFrictionCalculationMethod',
    'EnumWithSelectedValue_ScuffingCoefficientOfFrictionMethods', 'EnumWithSelectedValue_ContactResultType',
    'EnumWithSelectedValue_StressResultsType', 'EnumWithSelectedValue_CylindricalGearPairCreationOptions_DerivedParameterOption',
    'EnumWithSelectedValue_ToothThicknessSpecificationMethod', 'EnumWithSelectedValue_LoadDistributionFactorMethods',
    'EnumWithSelectedValue_AGMAGleasonConicalGearGeometryMethods', 'EnumWithSelectedValue_ProSolveMpcType',
    'EnumWithSelectedValue_ProSolveSolverType', 'EnumWithSelectedValue_CoilPositionInSlot',
    'EnumWithSelectedValue_ElectricMachineAnalysisPeriod', 'EnumWithSelectedValue_LoadCaseType',
    'EnumWithSelectedValue_HarmonicLoadDataType', 'EnumWithSelectedValue_ForceDisplayOption',
    'EnumWithSelectedValue_ITDesignation', 'EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption',
    'EnumWithSelectedValue_SplineRatingTypes', 'EnumWithSelectedValue_Modules',
    'EnumWithSelectedValue_PressureAngleTypes', 'EnumWithSelectedValue_SplineFitClassType',
    'EnumWithSelectedValue_SplineToleranceClassTypes', 'EnumWithSelectedValue_Table4JointInterfaceTypes',
    'EnumWithSelectedValue_DynamicsResponseScaling', 'EnumWithSelectedValue_CadPageOrientation',
    'EnumWithSelectedValue_FluidFilmTemperatureOptions', 'EnumWithSelectedValue_SupportToleranceLocationDesignation',
    'EnumWithSelectedValue_LoadedBallElementPropertyType', 'EnumWithSelectedValue_RollerBearingProfileTypes',
    'EnumWithSelectedValue_RollingBearingArrangement', 'EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod',
    'EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod', 'EnumWithSelectedValue_FatigueLoadLimitCalculationMethodEnum',
    'EnumWithSelectedValue_RollingBearingRaceType', 'EnumWithSelectedValue_RotationalDirections',
    'EnumWithSelectedValue_BearingEfficiencyRatingMethod', 'EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing',
    'EnumWithSelectedValue_ExcitationAnalysisViewOption', 'EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection',
    'EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection', 'EnumWithSelectedValue_ComponentOrientationOption',
    'EnumWithSelectedValue_Axis', 'EnumWithSelectedValue_AlignmentAxis',
    'EnumWithSelectedValue_DesignEntityId', 'EnumWithSelectedValue_ThermalExpansionOption',
    'EnumWithSelectedValue_FESubstructureType', 'EnumWithSelectedValue_FEExportFormat',
    'EnumWithSelectedValue_ThreeDViewContourOption', 'EnumWithSelectedValue_BoundaryConditionType',
    'EnumWithSelectedValue_BearingNodeOption', 'EnumWithSelectedValue_LinkNodeSource',
    'EnumWithSelectedValue_BearingToleranceClass', 'EnumWithSelectedValue_BearingModel',
    'EnumWithSelectedValue_PreloadType', 'EnumWithSelectedValue_RaceAxialMountingType',
    'EnumWithSelectedValue_RaceRadialMountingType', 'EnumWithSelectedValue_InternalClearanceClass',
    'EnumWithSelectedValue_BearingToleranceDefinitionOptions', 'EnumWithSelectedValue_OilSealLossCalculationMethod',
    'EnumWithSelectedValue_PowerLoadType', 'EnumWithSelectedValue_RigidConnectorStiffnessType',
    'EnumWithSelectedValue_RigidConnectorToothSpacingType', 'EnumWithSelectedValue_RigidConnectorTypes',
    'EnumWithSelectedValue_FitTypes', 'EnumWithSelectedValue_DoeValueSpecificationOption',
    'EnumWithSelectedValue_AnalysisType', 'EnumWithSelectedValue_BarModelExportType',
    'EnumWithSelectedValue_DynamicsResponse3DChartType', 'EnumWithSelectedValue_ComplexPartDisplayOption',
    'EnumWithSelectedValue_DynamicsResponseType', 'EnumWithSelectedValue_BearingStiffnessModel',
    'EnumWithSelectedValue_GearMeshStiffnessModel', 'EnumWithSelectedValue_ShaftAndHousingFlexibilityOption',
    'EnumWithSelectedValue_ExportOutputType', 'EnumWithSelectedValue_HarmonicAnalysisFEExportOptions_ComplexNumberOutput',
    'EnumWithSelectedValue_StiffnessOptionsForHarmonicAnalysis_StepCreation', 'EnumWithSelectedValue_HarmonicAnalysisTorqueInputType',
    'EnumWithSelectedValue_FrictionModelForGyroscopicMoment', 'EnumWithSelectedValue_MeshStiffnessModel',
    'EnumWithSelectedValue_ShearAreaFactorMethod', 'EnumWithSelectedValue_StressConcentrationMethod',
    'EnumWithSelectedValue_BallBearingAnalysisMethod', 'EnumWithSelectedValue_HertzianContactDeflectionCalculationMethod',
    'EnumWithSelectedValue_TorqueRippleInputType', 'EnumWithSelectedValue_HarmonicExcitationType',
    'EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification', 'EnumWithSelectedValue_TorqueSpecificationForSystemDeflection',
    'EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod', 'EnumWithSelectedValue_TorqueConverterLockupRule',
    'EnumWithSelectedValue_DegreeOfFreedom', 'EnumWithSelectedValue_DestinationDesignState'
)


class EnumWithSelectedValue_ShaftRatingMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ShaftRatingMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ShaftRatingMethod' types.
    """
    __qualname__ = 'ShaftRatingMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_34.ShaftRatingMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _34.ShaftRatingMethod

    @classmethod
    def implicit_type(cls) -> '_34.ShaftRatingMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _34.ShaftRatingMethod.type_()

    @property
    def selected_value(self) -> '_34.ShaftRatingMethod':
        """ShaftRatingMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_34.ShaftRatingMethod]':
        """List[ShaftRatingMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_SurfaceFinishes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_SurfaceFinishes

    A specific implementation of 'EnumWithSelectedValue' for 'SurfaceFinishes' types.
    """
    __qualname__ = 'SurfaceFinishes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_45.SurfaceFinishes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _45.SurfaceFinishes

    @classmethod
    def implicit_type(cls) -> '_45.SurfaceFinishes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _45.SurfaceFinishes.type_()

    @property
    def selected_value(self) -> '_45.SurfaceFinishes':
        """SurfaceFinishes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_45.SurfaceFinishes]':
        """List[SurfaceFinishes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_IntegrationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_IntegrationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'IntegrationMethod' types.
    """
    __qualname__ = 'IntegrationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_71.IntegrationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _71.IntegrationMethod

    @classmethod
    def implicit_type(cls) -> '_71.IntegrationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _71.IntegrationMethod.type_()

    @property
    def selected_value(self) -> '_71.IntegrationMethod':
        """IntegrationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_71.IntegrationMethod]':
        """List[IntegrationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ValueInputOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ValueInputOption

    A specific implementation of 'EnumWithSelectedValue' for 'ValueInputOption' types.
    """
    __qualname__ = 'ValueInputOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_91.ValueInputOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _91.ValueInputOption

    @classmethod
    def implicit_type(cls) -> '_91.ValueInputOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _91.ValueInputOption.type_()

    @property
    def selected_value(self) -> '_91.ValueInputOption':
        """ValueInputOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_91.ValueInputOption]':
        """List[ValueInputOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_SinglePointSelectionMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_SinglePointSelectionMethod

    A specific implementation of 'EnumWithSelectedValue' for 'SinglePointSelectionMethod' types.
    """
    __qualname__ = 'SinglePointSelectionMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_98.SinglePointSelectionMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _98.SinglePointSelectionMethod

    @classmethod
    def implicit_type(cls) -> '_98.SinglePointSelectionMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _98.SinglePointSelectionMethod.type_()

    @property
    def selected_value(self) -> '_98.SinglePointSelectionMethod':
        """SinglePointSelectionMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_98.SinglePointSelectionMethod]':
        """List[SinglePointSelectionMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ResultOptionsFor3DVector(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ResultOptionsFor3DVector

    A specific implementation of 'EnumWithSelectedValue' for 'ResultOptionsFor3DVector' types.
    """
    __qualname__ = 'ResultOptionsFor3DVector'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1517.ResultOptionsFor3DVector':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1517.ResultOptionsFor3DVector

    @classmethod
    def implicit_type(cls) -> '_1517.ResultOptionsFor3DVector.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1517.ResultOptionsFor3DVector.type_()

    @property
    def selected_value(self) -> '_1517.ResultOptionsFor3DVector':
        """ResultOptionsFor3DVector: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1517.ResultOptionsFor3DVector]':
        """List[ResultOptionsFor3DVector]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ElmerResultType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ElmerResultType

    A specific implementation of 'EnumWithSelectedValue' for 'ElmerResultType' types.
    """
    __qualname__ = 'ElmerResultType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_172.ElmerResultType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _172.ElmerResultType

    @classmethod
    def implicit_type(cls) -> '_172.ElmerResultType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _172.ElmerResultType.type_()

    @property
    def selected_value(self) -> '_172.ElmerResultType':
        """ElmerResultType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_172.ElmerResultType]':
        """List[ElmerResultType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ModeInputType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ModeInputType

    A specific implementation of 'EnumWithSelectedValue' for 'ModeInputType' types.
    """
    __qualname__ = 'ModeInputType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_78.ModeInputType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _78.ModeInputType

    @classmethod
    def implicit_type(cls) -> '_78.ModeInputType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _78.ModeInputType.type_()

    @property
    def selected_value(self) -> '_78.ModeInputType':
        """ModeInputType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_78.ModeInputType]':
        """List[ModeInputType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_MaterialPropertyClass(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_MaterialPropertyClass

    A specific implementation of 'EnumWithSelectedValue' for 'MaterialPropertyClass' types.
    """
    __qualname__ = 'MaterialPropertyClass'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1238.MaterialPropertyClass':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1238.MaterialPropertyClass

    @classmethod
    def implicit_type(cls) -> '_1238.MaterialPropertyClass.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1238.MaterialPropertyClass.type_()

    @property
    def selected_value(self) -> '_1238.MaterialPropertyClass':
        """MaterialPropertyClass: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1238.MaterialPropertyClass]':
        """List[MaterialPropertyClass]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LubricantDefinition(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LubricantDefinition

    A specific implementation of 'EnumWithSelectedValue' for 'LubricantDefinition' types.
    """
    __qualname__ = 'LubricantDefinition'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_259.LubricantDefinition':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _259.LubricantDefinition

    @classmethod
    def implicit_type(cls) -> '_259.LubricantDefinition.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _259.LubricantDefinition.type_()

    @property
    def selected_value(self) -> '_259.LubricantDefinition':
        """LubricantDefinition: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_259.LubricantDefinition]':
        """List[LubricantDefinition]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LubricantViscosityClassISO(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LubricantViscosityClassISO

    A specific implementation of 'EnumWithSelectedValue' for 'LubricantViscosityClassISO' types.
    """
    __qualname__ = 'LubricantViscosityClassISO'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_263.LubricantViscosityClassISO':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _263.LubricantViscosityClassISO

    @classmethod
    def implicit_type(cls) -> '_263.LubricantViscosityClassISO.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _263.LubricantViscosityClassISO.type_()

    @property
    def selected_value(self) -> '_263.LubricantViscosityClassISO':
        """LubricantViscosityClassISO: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_263.LubricantViscosityClassISO]':
        """List[LubricantViscosityClassISO]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_MicroGeometryModel(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_MicroGeometryModel

    A specific implementation of 'EnumWithSelectedValue' for 'MicroGeometryModel' types.
    """
    __qualname__ = 'MicroGeometryModel'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_335.MicroGeometryModel':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _335.MicroGeometryModel

    @classmethod
    def implicit_type(cls) -> '_335.MicroGeometryModel.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _335.MicroGeometryModel.type_()

    @property
    def selected_value(self) -> '_335.MicroGeometryModel':
        """MicroGeometryModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_335.MicroGeometryModel]':
        """List[MicroGeometryModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ExtrapolationOptions(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ExtrapolationOptions

    A specific implementation of 'EnumWithSelectedValue' for 'ExtrapolationOptions' types.
    """
    __qualname__ = 'ExtrapolationOptions'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1500.ExtrapolationOptions':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1500.ExtrapolationOptions

    @classmethod
    def implicit_type(cls) -> '_1500.ExtrapolationOptions.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1500.ExtrapolationOptions.type_()

    @property
    def selected_value(self) -> '_1500.ExtrapolationOptions':
        """ExtrapolationOptions: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1500.ExtrapolationOptions]':
        """List[ExtrapolationOptions]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CylindricalGearRatingMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CylindricalGearRatingMethods

    A specific implementation of 'EnumWithSelectedValue' for 'CylindricalGearRatingMethods' types.
    """
    __qualname__ = 'CylindricalGearRatingMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_249.CylindricalGearRatingMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _249.CylindricalGearRatingMethods

    @classmethod
    def implicit_type(cls) -> '_249.CylindricalGearRatingMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _249.CylindricalGearRatingMethods.type_()

    @property
    def selected_value(self) -> '_249.CylindricalGearRatingMethods':
        """CylindricalGearRatingMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_249.CylindricalGearRatingMethods]':
        """List[CylindricalGearRatingMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ScuffingFlashTemperatureRatingMethod' types.
    """
    __qualname__ = 'ScuffingFlashTemperatureRatingMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_478.ScuffingFlashTemperatureRatingMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _478.ScuffingFlashTemperatureRatingMethod

    @classmethod
    def implicit_type(cls) -> '_478.ScuffingFlashTemperatureRatingMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _478.ScuffingFlashTemperatureRatingMethod.type_()

    @property
    def selected_value(self) -> '_478.ScuffingFlashTemperatureRatingMethod':
        """ScuffingFlashTemperatureRatingMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_478.ScuffingFlashTemperatureRatingMethod]':
        """List[ScuffingFlashTemperatureRatingMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ScuffingIntegralTemperatureRatingMethod' types.
    """
    __qualname__ = 'ScuffingIntegralTemperatureRatingMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_479.ScuffingIntegralTemperatureRatingMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _479.ScuffingIntegralTemperatureRatingMethod

    @classmethod
    def implicit_type(cls) -> '_479.ScuffingIntegralTemperatureRatingMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _479.ScuffingIntegralTemperatureRatingMethod.type_()

    @property
    def selected_value(self) -> '_479.ScuffingIntegralTemperatureRatingMethod':
        """ScuffingIntegralTemperatureRatingMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_479.ScuffingIntegralTemperatureRatingMethod]':
        """List[ScuffingIntegralTemperatureRatingMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LocationOfEvaluationLowerLimit(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LocationOfEvaluationLowerLimit

    A specific implementation of 'EnumWithSelectedValue' for 'LocationOfEvaluationLowerLimit' types.
    """
    __qualname__ = 'LocationOfEvaluationLowerLimit'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_570.LocationOfEvaluationLowerLimit':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _570.LocationOfEvaluationLowerLimit

    @classmethod
    def implicit_type(cls) -> '_570.LocationOfEvaluationLowerLimit.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _570.LocationOfEvaluationLowerLimit.type_()

    @property
    def selected_value(self) -> '_570.LocationOfEvaluationLowerLimit':
        """LocationOfEvaluationLowerLimit: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_570.LocationOfEvaluationLowerLimit]':
        """List[LocationOfEvaluationLowerLimit]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LocationOfEvaluationUpperLimit(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LocationOfEvaluationUpperLimit

    A specific implementation of 'EnumWithSelectedValue' for 'LocationOfEvaluationUpperLimit' types.
    """
    __qualname__ = 'LocationOfEvaluationUpperLimit'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_571.LocationOfEvaluationUpperLimit':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _571.LocationOfEvaluationUpperLimit

    @classmethod
    def implicit_type(cls) -> '_571.LocationOfEvaluationUpperLimit.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _571.LocationOfEvaluationUpperLimit.type_()

    @property
    def selected_value(self) -> '_571.LocationOfEvaluationUpperLimit':
        """LocationOfEvaluationUpperLimit: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_571.LocationOfEvaluationUpperLimit]':
        """List[LocationOfEvaluationUpperLimit]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LocationOfRootReliefEvaluation(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LocationOfRootReliefEvaluation

    A specific implementation of 'EnumWithSelectedValue' for 'LocationOfRootReliefEvaluation' types.
    """
    __qualname__ = 'LocationOfRootReliefEvaluation'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_572.LocationOfRootReliefEvaluation':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _572.LocationOfRootReliefEvaluation

    @classmethod
    def implicit_type(cls) -> '_572.LocationOfRootReliefEvaluation.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _572.LocationOfRootReliefEvaluation.type_()

    @property
    def selected_value(self) -> '_572.LocationOfRootReliefEvaluation':
        """LocationOfRootReliefEvaluation: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_572.LocationOfRootReliefEvaluation]':
        """List[LocationOfRootReliefEvaluation]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LocationOfTipReliefEvaluation(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LocationOfTipReliefEvaluation

    A specific implementation of 'EnumWithSelectedValue' for 'LocationOfTipReliefEvaluation' types.
    """
    __qualname__ = 'LocationOfTipReliefEvaluation'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_573.LocationOfTipReliefEvaluation':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _573.LocationOfTipReliefEvaluation

    @classmethod
    def implicit_type(cls) -> '_573.LocationOfTipReliefEvaluation.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _573.LocationOfTipReliefEvaluation.type_()

    @property
    def selected_value(self) -> '_573.LocationOfTipReliefEvaluation':
        """LocationOfTipReliefEvaluation: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_573.LocationOfTipReliefEvaluation]':
        """List[LocationOfTipReliefEvaluation]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CylindricalMftFinishingMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CylindricalMftFinishingMethods

    A specific implementation of 'EnumWithSelectedValue' for 'CylindricalMftFinishingMethods' types.
    """
    __qualname__ = 'CylindricalMftFinishingMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_620.CylindricalMftFinishingMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _620.CylindricalMftFinishingMethods

    @classmethod
    def implicit_type(cls) -> '_620.CylindricalMftFinishingMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _620.CylindricalMftFinishingMethods.type_()

    @property
    def selected_value(self) -> '_620.CylindricalMftFinishingMethods':
        """CylindricalMftFinishingMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_620.CylindricalMftFinishingMethods]':
        """List[CylindricalMftFinishingMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CylindricalMftRoughingMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CylindricalMftRoughingMethods

    A specific implementation of 'EnumWithSelectedValue' for 'CylindricalMftRoughingMethods' types.
    """
    __qualname__ = 'CylindricalMftRoughingMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_621.CylindricalMftRoughingMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _621.CylindricalMftRoughingMethods

    @classmethod
    def implicit_type(cls) -> '_621.CylindricalMftRoughingMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _621.CylindricalMftRoughingMethods.type_()

    @property
    def selected_value(self) -> '_621.CylindricalMftRoughingMethods':
        """CylindricalMftRoughingMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_621.CylindricalMftRoughingMethods]':
        """List[CylindricalMftRoughingMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_MicroGeometryDefinitionMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_MicroGeometryDefinitionMethod

    A specific implementation of 'EnumWithSelectedValue' for 'MicroGeometryDefinitionMethod' types.
    """
    __qualname__ = 'MicroGeometryDefinitionMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_642.MicroGeometryDefinitionMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _642.MicroGeometryDefinitionMethod

    @classmethod
    def implicit_type(cls) -> '_642.MicroGeometryDefinitionMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _642.MicroGeometryDefinitionMethod.type_()

    @property
    def selected_value(self) -> '_642.MicroGeometryDefinitionMethod':
        """MicroGeometryDefinitionMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_642.MicroGeometryDefinitionMethod]':
        """List[MicroGeometryDefinitionMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_MicroGeometryDefinitionType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_MicroGeometryDefinitionType

    A specific implementation of 'EnumWithSelectedValue' for 'MicroGeometryDefinitionType' types.
    """
    __qualname__ = 'MicroGeometryDefinitionType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_643.MicroGeometryDefinitionType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _643.MicroGeometryDefinitionType

    @classmethod
    def implicit_type(cls) -> '_643.MicroGeometryDefinitionType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _643.MicroGeometryDefinitionType.type_()

    @property
    def selected_value(self) -> '_643.MicroGeometryDefinitionType':
        """MicroGeometryDefinitionType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_643.MicroGeometryDefinitionType]':
        """List[MicroGeometryDefinitionType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ChartType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ChartType

    A specific implementation of 'EnumWithSelectedValue' for 'ChartType' types.
    """
    __qualname__ = 'ChartType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_640.ChartType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _640.ChartType

    @classmethod
    def implicit_type(cls) -> '_640.ChartType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _640.ChartType.type_()

    @property
    def selected_value(self) -> '_640.ChartType':
        """ChartType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_640.ChartType]':
        """List[ChartType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_Flank(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_Flank

    A specific implementation of 'EnumWithSelectedValue' for 'Flank' types.
    """
    __qualname__ = 'Flank'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_624.Flank':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _624.Flank

    @classmethod
    def implicit_type(cls) -> '_624.Flank.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _624.Flank.type_()

    @property
    def selected_value(self) -> '_624.Flank':
        """Flank: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_624.Flank]':
        """List[Flank]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ActiveProcessMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ActiveProcessMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ActiveProcessMethod' types.
    """
    __qualname__ = 'ActiveProcessMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_655.ActiveProcessMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _655.ActiveProcessMethod

    @classmethod
    def implicit_type(cls) -> '_655.ActiveProcessMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _655.ActiveProcessMethod.type_()

    @property
    def selected_value(self) -> '_655.ActiveProcessMethod':
        """ActiveProcessMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_655.ActiveProcessMethod]':
        """List[ActiveProcessMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CutterFlankSections(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CutterFlankSections

    A specific implementation of 'EnumWithSelectedValue' for 'CutterFlankSections' types.
    """
    __qualname__ = 'CutterFlankSections'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_606.CutterFlankSections':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _606.CutterFlankSections

    @classmethod
    def implicit_type(cls) -> '_606.CutterFlankSections.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _606.CutterFlankSections.type_()

    @property
    def selected_value(self) -> '_606.CutterFlankSections':
        """CutterFlankSections: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_606.CutterFlankSections]':
        """List[CutterFlankSections]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BasicCurveTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BasicCurveTypes

    A specific implementation of 'EnumWithSelectedValue' for 'BasicCurveTypes' types.
    """
    __qualname__ = 'BasicCurveTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_311.BasicCurveTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _311.BasicCurveTypes

    @classmethod
    def implicit_type(cls) -> '_311.BasicCurveTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _311.BasicCurveTypes.type_()

    @property
    def selected_value(self) -> '_311.BasicCurveTypes':
        """BasicCurveTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_311.BasicCurveTypes]':
        """List[BasicCurveTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ThicknessType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ThicknessType

    A specific implementation of 'EnumWithSelectedValue' for 'ThicknessType' types.
    """
    __qualname__ = 'ThicknessType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1075.ThicknessType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1075.ThicknessType

    @classmethod
    def implicit_type(cls) -> '_1075.ThicknessType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1075.ThicknessType.type_()

    @property
    def selected_value(self) -> '_1075.ThicknessType':
        """ThicknessType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1075.ThicknessType]':
        """List[ThicknessType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ConicalMachineSettingCalculationMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ConicalMachineSettingCalculationMethods

    A specific implementation of 'EnumWithSelectedValue' for 'ConicalMachineSettingCalculationMethods' types.
    """
    __qualname__ = 'ConicalMachineSettingCalculationMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1153.ConicalMachineSettingCalculationMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1153.ConicalMachineSettingCalculationMethods

    @classmethod
    def implicit_type(cls) -> '_1153.ConicalMachineSettingCalculationMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1153.ConicalMachineSettingCalculationMethods.type_()

    @property
    def selected_value(self) -> '_1153.ConicalMachineSettingCalculationMethods':
        """ConicalMachineSettingCalculationMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1153.ConicalMachineSettingCalculationMethods]':
        """List[ConicalMachineSettingCalculationMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ConicalManufactureMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ConicalManufactureMethods

    A specific implementation of 'EnumWithSelectedValue' for 'ConicalManufactureMethods' types.
    """
    __qualname__ = 'ConicalManufactureMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1154.ConicalManufactureMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1154.ConicalManufactureMethods

    @classmethod
    def implicit_type(cls) -> '_1154.ConicalManufactureMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1154.ConicalManufactureMethods.type_()

    @property
    def selected_value(self) -> '_1154.ConicalManufactureMethods':
        """ConicalManufactureMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1154.ConicalManufactureMethods]':
        """List[ConicalManufactureMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CandidateDisplayChoice(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CandidateDisplayChoice

    A specific implementation of 'EnumWithSelectedValue' for 'CandidateDisplayChoice' types.
    """
    __qualname__ = 'CandidateDisplayChoice'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_900.CandidateDisplayChoice':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _900.CandidateDisplayChoice

    @classmethod
    def implicit_type(cls) -> '_900.CandidateDisplayChoice.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _900.CandidateDisplayChoice.type_()

    @property
    def selected_value(self) -> '_900.CandidateDisplayChoice':
        """CandidateDisplayChoice: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_900.CandidateDisplayChoice]':
        """List[CandidateDisplayChoice]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_Severity(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_Severity

    A specific implementation of 'EnumWithSelectedValue' for 'Severity' types.
    """
    __qualname__ = 'Severity'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1783.Severity':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1783.Severity

    @classmethod
    def implicit_type(cls) -> '_1783.Severity.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1783.Severity.type_()

    @property
    def selected_value(self) -> '_1783.Severity':
        """Severity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1783.Severity]':
        """List[Severity]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_GeometrySpecificationType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_GeometrySpecificationType

    A specific implementation of 'EnumWithSelectedValue' for 'GeometrySpecificationType' types.
    """
    __qualname__ = 'GeometrySpecificationType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1046.GeometrySpecificationType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1046.GeometrySpecificationType

    @classmethod
    def implicit_type(cls) -> '_1046.GeometrySpecificationType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1046.GeometrySpecificationType.type_()

    @property
    def selected_value(self) -> '_1046.GeometrySpecificationType':
        """GeometrySpecificationType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1046.GeometrySpecificationType]':
        """List[GeometrySpecificationType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_StatusItemSeverity(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_StatusItemSeverity

    A specific implementation of 'EnumWithSelectedValue' for 'StatusItemSeverity' types.
    """
    __qualname__ = 'StatusItemSeverity'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1786.StatusItemSeverity':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1786.StatusItemSeverity

    @classmethod
    def implicit_type(cls) -> '_1786.StatusItemSeverity.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1786.StatusItemSeverity.type_()

    @property
    def selected_value(self) -> '_1786.StatusItemSeverity':
        """StatusItemSeverity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1786.StatusItemSeverity]':
        """List[StatusItemSeverity]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LubricationMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LubricationMethods

    A specific implementation of 'EnumWithSelectedValue' for 'LubricationMethods' types.
    """
    __qualname__ = 'LubricationMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_333.LubricationMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _333.LubricationMethods

    @classmethod
    def implicit_type(cls) -> '_333.LubricationMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _333.LubricationMethods.type_()

    @property
    def selected_value(self) -> '_333.LubricationMethods':
        """LubricationMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_333.LubricationMethods]':
        """List[LubricationMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_MicropittingCoefficientOfFrictionCalculationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_MicropittingCoefficientOfFrictionCalculationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'MicropittingCoefficientOfFrictionCalculationMethod' types.
    """
    __qualname__ = 'MicropittingCoefficientOfFrictionCalculationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_336.MicropittingCoefficientOfFrictionCalculationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _336.MicropittingCoefficientOfFrictionCalculationMethod

    @classmethod
    def implicit_type(cls) -> '_336.MicropittingCoefficientOfFrictionCalculationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _336.MicropittingCoefficientOfFrictionCalculationMethod.type_()

    @property
    def selected_value(self) -> '_336.MicropittingCoefficientOfFrictionCalculationMethod':
        """MicropittingCoefficientOfFrictionCalculationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_336.MicropittingCoefficientOfFrictionCalculationMethod]':
        """List[MicropittingCoefficientOfFrictionCalculationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ScuffingCoefficientOfFrictionMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ScuffingCoefficientOfFrictionMethods

    A specific implementation of 'EnumWithSelectedValue' for 'ScuffingCoefficientOfFrictionMethods' types.
    """
    __qualname__ = 'ScuffingCoefficientOfFrictionMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1067.ScuffingCoefficientOfFrictionMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1067.ScuffingCoefficientOfFrictionMethods

    @classmethod
    def implicit_type(cls) -> '_1067.ScuffingCoefficientOfFrictionMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1067.ScuffingCoefficientOfFrictionMethods.type_()

    @property
    def selected_value(self) -> '_1067.ScuffingCoefficientOfFrictionMethods':
        """ScuffingCoefficientOfFrictionMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1067.ScuffingCoefficientOfFrictionMethods]':
        """List[ScuffingCoefficientOfFrictionMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ContactResultType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ContactResultType

    A specific implementation of 'EnumWithSelectedValue' for 'ContactResultType' types.
    """
    __qualname__ = 'ContactResultType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_824.ContactResultType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _824.ContactResultType

    @classmethod
    def implicit_type(cls) -> '_824.ContactResultType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _824.ContactResultType.type_()

    @property
    def selected_value(self) -> '_824.ContactResultType':
        """ContactResultType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_824.ContactResultType]':
        """List[ContactResultType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_StressResultsType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_StressResultsType

    A specific implementation of 'EnumWithSelectedValue' for 'StressResultsType' types.
    """
    __qualname__ = 'StressResultsType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_87.StressResultsType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _87.StressResultsType

    @classmethod
    def implicit_type(cls) -> '_87.StressResultsType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _87.StressResultsType.type_()

    @property
    def selected_value(self) -> '_87.StressResultsType':
        """StressResultsType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_87.StressResultsType]':
        """List[StressResultsType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CylindricalGearPairCreationOptions_DerivedParameterOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CylindricalGearPairCreationOptions_DerivedParameterOption

    A specific implementation of 'EnumWithSelectedValue' for 'CylindricalGearPairCreationOptions.DerivedParameterOption' types.
    """
    __qualname__ = 'CylindricalGearPairCreationOptions.DerivedParameterOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1142.CylindricalGearPairCreationOptions.DerivedParameterOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1142.CylindricalGearPairCreationOptions.DerivedParameterOption

    @classmethod
    def implicit_type(cls) -> '_1142.CylindricalGearPairCreationOptions.DerivedParameterOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1142.CylindricalGearPairCreationOptions.DerivedParameterOption.type_()

    @property
    def selected_value(self) -> '_1142.CylindricalGearPairCreationOptions.DerivedParameterOption':
        """CylindricalGearPairCreationOptions.DerivedParameterOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1142.CylindricalGearPairCreationOptions.DerivedParameterOption]':
        """List[CylindricalGearPairCreationOptions.DerivedParameterOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ToothThicknessSpecificationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ToothThicknessSpecificationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ToothThicknessSpecificationMethod' types.
    """
    __qualname__ = 'ToothThicknessSpecificationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1186.ToothThicknessSpecificationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1186.ToothThicknessSpecificationMethod

    @classmethod
    def implicit_type(cls) -> '_1186.ToothThicknessSpecificationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1186.ToothThicknessSpecificationMethod.type_()

    @property
    def selected_value(self) -> '_1186.ToothThicknessSpecificationMethod':
        """ToothThicknessSpecificationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1186.ToothThicknessSpecificationMethod]':
        """List[ToothThicknessSpecificationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LoadDistributionFactorMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LoadDistributionFactorMethods

    A specific implementation of 'EnumWithSelectedValue' for 'LoadDistributionFactorMethods' types.
    """
    __qualname__ = 'LoadDistributionFactorMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1165.LoadDistributionFactorMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1165.LoadDistributionFactorMethods

    @classmethod
    def implicit_type(cls) -> '_1165.LoadDistributionFactorMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1165.LoadDistributionFactorMethods.type_()

    @property
    def selected_value(self) -> '_1165.LoadDistributionFactorMethods':
        """LoadDistributionFactorMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1165.LoadDistributionFactorMethods]':
        """List[LoadDistributionFactorMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_AGMAGleasonConicalGearGeometryMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_AGMAGleasonConicalGearGeometryMethods

    A specific implementation of 'EnumWithSelectedValue' for 'AGMAGleasonConicalGearGeometryMethods' types.
    """
    __qualname__ = 'AGMAGleasonConicalGearGeometryMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1175.AGMAGleasonConicalGearGeometryMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1175.AGMAGleasonConicalGearGeometryMethods

    @classmethod
    def implicit_type(cls) -> '_1175.AGMAGleasonConicalGearGeometryMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1175.AGMAGleasonConicalGearGeometryMethods.type_()

    @property
    def selected_value(self) -> '_1175.AGMAGleasonConicalGearGeometryMethods':
        """AGMAGleasonConicalGearGeometryMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1175.AGMAGleasonConicalGearGeometryMethods]':
        """List[AGMAGleasonConicalGearGeometryMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ProSolveMpcType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ProSolveMpcType

    A specific implementation of 'EnumWithSelectedValue' for 'ProSolveMpcType' types.
    """
    __qualname__ = 'ProSolveMpcType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1235.ProSolveMpcType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1235.ProSolveMpcType

    @classmethod
    def implicit_type(cls) -> '_1235.ProSolveMpcType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1235.ProSolveMpcType.type_()

    @property
    def selected_value(self) -> '_1235.ProSolveMpcType':
        """ProSolveMpcType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1235.ProSolveMpcType]':
        """List[ProSolveMpcType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ProSolveSolverType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ProSolveSolverType

    A specific implementation of 'EnumWithSelectedValue' for 'ProSolveSolverType' types.
    """
    __qualname__ = 'ProSolveSolverType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1236.ProSolveSolverType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1236.ProSolveSolverType

    @classmethod
    def implicit_type(cls) -> '_1236.ProSolveSolverType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1236.ProSolveSolverType.type_()

    @property
    def selected_value(self) -> '_1236.ProSolveSolverType':
        """ProSolveSolverType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1236.ProSolveSolverType]':
        """List[ProSolveSolverType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CoilPositionInSlot(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CoilPositionInSlot

    A specific implementation of 'EnumWithSelectedValue' for 'CoilPositionInSlot' types.
    """
    __qualname__ = 'CoilPositionInSlot'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1248.CoilPositionInSlot':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1248.CoilPositionInSlot

    @classmethod
    def implicit_type(cls) -> '_1248.CoilPositionInSlot.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1248.CoilPositionInSlot.type_()

    @property
    def selected_value(self) -> '_1248.CoilPositionInSlot':
        """CoilPositionInSlot: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1248.CoilPositionInSlot]':
        """List[CoilPositionInSlot]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ElectricMachineAnalysisPeriod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ElectricMachineAnalysisPeriod

    A specific implementation of 'EnumWithSelectedValue' for 'ElectricMachineAnalysisPeriod' types.
    """
    __qualname__ = 'ElectricMachineAnalysisPeriod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_168.ElectricMachineAnalysisPeriod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _168.ElectricMachineAnalysisPeriod

    @classmethod
    def implicit_type(cls) -> '_168.ElectricMachineAnalysisPeriod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _168.ElectricMachineAnalysisPeriod.type_()

    @property
    def selected_value(self) -> '_168.ElectricMachineAnalysisPeriod':
        """ElectricMachineAnalysisPeriod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_168.ElectricMachineAnalysisPeriod]':
        """List[ElectricMachineAnalysisPeriod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LoadCaseType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LoadCaseType

    A specific implementation of 'EnumWithSelectedValue' for 'LoadCaseType' types.
    """
    __qualname__ = 'LoadCaseType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1353.LoadCaseType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1353.LoadCaseType

    @classmethod
    def implicit_type(cls) -> '_1353.LoadCaseType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1353.LoadCaseType.type_()

    @property
    def selected_value(self) -> '_1353.LoadCaseType':
        """LoadCaseType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1353.LoadCaseType]':
        """List[LoadCaseType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_HarmonicLoadDataType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_HarmonicLoadDataType

    A specific implementation of 'EnumWithSelectedValue' for 'HarmonicLoadDataType' types.
    """
    __qualname__ = 'HarmonicLoadDataType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1372.HarmonicLoadDataType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1372.HarmonicLoadDataType

    @classmethod
    def implicit_type(cls) -> '_1372.HarmonicLoadDataType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1372.HarmonicLoadDataType.type_()

    @property
    def selected_value(self) -> '_1372.HarmonicLoadDataType':
        """HarmonicLoadDataType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1372.HarmonicLoadDataType]':
        """List[HarmonicLoadDataType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ForceDisplayOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ForceDisplayOption

    A specific implementation of 'EnumWithSelectedValue' for 'ForceDisplayOption' types.
    """
    __qualname__ = 'ForceDisplayOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1369.ForceDisplayOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1369.ForceDisplayOption

    @classmethod
    def implicit_type(cls) -> '_1369.ForceDisplayOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1369.ForceDisplayOption.type_()

    @property
    def selected_value(self) -> '_1369.ForceDisplayOption':
        """ForceDisplayOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1369.ForceDisplayOption]':
        """List[ForceDisplayOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ITDesignation(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ITDesignation

    A specific implementation of 'EnumWithSelectedValue' for 'ITDesignation' types.
    """
    __qualname__ = 'ITDesignation'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1897.ITDesignation':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1897.ITDesignation

    @classmethod
    def implicit_type(cls) -> '_1897.ITDesignation.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1897.ITDesignation.type_()

    @property
    def selected_value(self) -> '_1897.ITDesignation':
        """ITDesignation: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1897.ITDesignation]':
        """List[ITDesignation]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption

    A specific implementation of 'EnumWithSelectedValue' for 'DudleyEffectiveLengthApproximationOption' types.
    """
    __qualname__ = 'DudleyEffectiveLengthApproximationOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1384.DudleyEffectiveLengthApproximationOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1384.DudleyEffectiveLengthApproximationOption

    @classmethod
    def implicit_type(cls) -> '_1384.DudleyEffectiveLengthApproximationOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1384.DudleyEffectiveLengthApproximationOption.type_()

    @property
    def selected_value(self) -> '_1384.DudleyEffectiveLengthApproximationOption':
        """DudleyEffectiveLengthApproximationOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1384.DudleyEffectiveLengthApproximationOption]':
        """List[DudleyEffectiveLengthApproximationOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_SplineRatingTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_SplineRatingTypes

    A specific implementation of 'EnumWithSelectedValue' for 'SplineRatingTypes' types.
    """
    __qualname__ = 'SplineRatingTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1407.SplineRatingTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1407.SplineRatingTypes

    @classmethod
    def implicit_type(cls) -> '_1407.SplineRatingTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1407.SplineRatingTypes.type_()

    @property
    def selected_value(self) -> '_1407.SplineRatingTypes':
        """SplineRatingTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1407.SplineRatingTypes]':
        """List[SplineRatingTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_Modules(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_Modules

    A specific implementation of 'EnumWithSelectedValue' for 'Modules' types.
    """
    __qualname__ = 'Modules'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1393.Modules':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1393.Modules

    @classmethod
    def implicit_type(cls) -> '_1393.Modules.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1393.Modules.type_()

    @property
    def selected_value(self) -> '_1393.Modules':
        """Modules: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1393.Modules]':
        """List[Modules]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_PressureAngleTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_PressureAngleTypes

    A specific implementation of 'EnumWithSelectedValue' for 'PressureAngleTypes' types.
    """
    __qualname__ = 'PressureAngleTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1394.PressureAngleTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1394.PressureAngleTypes

    @classmethod
    def implicit_type(cls) -> '_1394.PressureAngleTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1394.PressureAngleTypes.type_()

    @property
    def selected_value(self) -> '_1394.PressureAngleTypes':
        """PressureAngleTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1394.PressureAngleTypes]':
        """List[PressureAngleTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_SplineFitClassType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_SplineFitClassType

    A specific implementation of 'EnumWithSelectedValue' for 'SplineFitClassType' types.
    """
    __qualname__ = 'SplineFitClassType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1402.SplineFitClassType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1402.SplineFitClassType

    @classmethod
    def implicit_type(cls) -> '_1402.SplineFitClassType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1402.SplineFitClassType.type_()

    @property
    def selected_value(self) -> '_1402.SplineFitClassType':
        """SplineFitClassType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1402.SplineFitClassType]':
        """List[SplineFitClassType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_SplineToleranceClassTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_SplineToleranceClassTypes

    A specific implementation of 'EnumWithSelectedValue' for 'SplineToleranceClassTypes' types.
    """
    __qualname__ = 'SplineToleranceClassTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1408.SplineToleranceClassTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1408.SplineToleranceClassTypes

    @classmethod
    def implicit_type(cls) -> '_1408.SplineToleranceClassTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1408.SplineToleranceClassTypes.type_()

    @property
    def selected_value(self) -> '_1408.SplineToleranceClassTypes':
        """SplineToleranceClassTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1408.SplineToleranceClassTypes]':
        """List[SplineToleranceClassTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_Table4JointInterfaceTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_Table4JointInterfaceTypes

    A specific implementation of 'EnumWithSelectedValue' for 'Table4JointInterfaceTypes' types.
    """
    __qualname__ = 'Table4JointInterfaceTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1438.Table4JointInterfaceTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1438.Table4JointInterfaceTypes

    @classmethod
    def implicit_type(cls) -> '_1438.Table4JointInterfaceTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1438.Table4JointInterfaceTypes.type_()

    @property
    def selected_value(self) -> '_1438.Table4JointInterfaceTypes':
        """Table4JointInterfaceTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1438.Table4JointInterfaceTypes]':
        """List[Table4JointInterfaceTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_DynamicsResponseScaling(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DynamicsResponseScaling

    A specific implementation of 'EnumWithSelectedValue' for 'DynamicsResponseScaling' types.
    """
    __qualname__ = 'DynamicsResponseScaling'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1496.DynamicsResponseScaling':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1496.DynamicsResponseScaling

    @classmethod
    def implicit_type(cls) -> '_1496.DynamicsResponseScaling.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1496.DynamicsResponseScaling.type_()

    @property
    def selected_value(self) -> '_1496.DynamicsResponseScaling':
        """DynamicsResponseScaling: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1496.DynamicsResponseScaling]':
        """List[DynamicsResponseScaling]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CadPageOrientation(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CadPageOrientation

    A specific implementation of 'EnumWithSelectedValue' for 'CadPageOrientation' types.
    """
    __qualname__ = 'CadPageOrientation'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1736.CadPageOrientation':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1736.CadPageOrientation

    @classmethod
    def implicit_type(cls) -> '_1736.CadPageOrientation.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1736.CadPageOrientation.type_()

    @property
    def selected_value(self) -> '_1736.CadPageOrientation':
        """CadPageOrientation: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1736.CadPageOrientation]':
        """List[CadPageOrientation]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_FluidFilmTemperatureOptions(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_FluidFilmTemperatureOptions

    A specific implementation of 'EnumWithSelectedValue' for 'FluidFilmTemperatureOptions' types.
    """
    __qualname__ = 'FluidFilmTemperatureOptions'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1871.FluidFilmTemperatureOptions':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1871.FluidFilmTemperatureOptions

    @classmethod
    def implicit_type(cls) -> '_1871.FluidFilmTemperatureOptions.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1871.FluidFilmTemperatureOptions.type_()

    @property
    def selected_value(self) -> '_1871.FluidFilmTemperatureOptions':
        """FluidFilmTemperatureOptions: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1871.FluidFilmTemperatureOptions]':
        """List[FluidFilmTemperatureOptions]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_SupportToleranceLocationDesignation(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_SupportToleranceLocationDesignation

    A specific implementation of 'EnumWithSelectedValue' for 'SupportToleranceLocationDesignation' types.
    """
    __qualname__ = 'SupportToleranceLocationDesignation'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1910.SupportToleranceLocationDesignation':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1910.SupportToleranceLocationDesignation

    @classmethod
    def implicit_type(cls) -> '_1910.SupportToleranceLocationDesignation.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1910.SupportToleranceLocationDesignation.type_()

    @property
    def selected_value(self) -> '_1910.SupportToleranceLocationDesignation':
        """SupportToleranceLocationDesignation: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1910.SupportToleranceLocationDesignation]':
        """List[SupportToleranceLocationDesignation]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LoadedBallElementPropertyType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LoadedBallElementPropertyType

    A specific implementation of 'EnumWithSelectedValue' for 'LoadedBallElementPropertyType' types.
    """
    __qualname__ = 'LoadedBallElementPropertyType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1949.LoadedBallElementPropertyType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1949.LoadedBallElementPropertyType

    @classmethod
    def implicit_type(cls) -> '_1949.LoadedBallElementPropertyType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1949.LoadedBallElementPropertyType.type_()

    @property
    def selected_value(self) -> '_1949.LoadedBallElementPropertyType':
        """LoadedBallElementPropertyType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1949.LoadedBallElementPropertyType]':
        """List[LoadedBallElementPropertyType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RollerBearingProfileTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RollerBearingProfileTypes

    A specific implementation of 'EnumWithSelectedValue' for 'RollerBearingProfileTypes' types.
    """
    __qualname__ = 'RollerBearingProfileTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1878.RollerBearingProfileTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1878.RollerBearingProfileTypes

    @classmethod
    def implicit_type(cls) -> '_1878.RollerBearingProfileTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1878.RollerBearingProfileTypes.type_()

    @property
    def selected_value(self) -> '_1878.RollerBearingProfileTypes':
        """RollerBearingProfileTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1878.RollerBearingProfileTypes]':
        """List[RollerBearingProfileTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RollingBearingArrangement(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RollingBearingArrangement

    A specific implementation of 'EnumWithSelectedValue' for 'RollingBearingArrangement' types.
    """
    __qualname__ = 'RollingBearingArrangement'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1879.RollingBearingArrangement':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1879.RollingBearingArrangement

    @classmethod
    def implicit_type(cls) -> '_1879.RollingBearingArrangement.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1879.RollingBearingArrangement.type_()

    @property
    def selected_value(self) -> '_1879.RollingBearingArrangement':
        """RollingBearingArrangement: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1879.RollingBearingArrangement]':
        """List[RollingBearingArrangement]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'BasicDynamicLoadRatingCalculationMethod' types.
    """
    __qualname__ = 'BasicDynamicLoadRatingCalculationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1857.BasicDynamicLoadRatingCalculationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1857.BasicDynamicLoadRatingCalculationMethod

    @classmethod
    def implicit_type(cls) -> '_1857.BasicDynamicLoadRatingCalculationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1857.BasicDynamicLoadRatingCalculationMethod.type_()

    @property
    def selected_value(self) -> '_1857.BasicDynamicLoadRatingCalculationMethod':
        """BasicDynamicLoadRatingCalculationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1857.BasicDynamicLoadRatingCalculationMethod]':
        """List[BasicDynamicLoadRatingCalculationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'BasicStaticLoadRatingCalculationMethod' types.
    """
    __qualname__ = 'BasicStaticLoadRatingCalculationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1858.BasicStaticLoadRatingCalculationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1858.BasicStaticLoadRatingCalculationMethod

    @classmethod
    def implicit_type(cls) -> '_1858.BasicStaticLoadRatingCalculationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1858.BasicStaticLoadRatingCalculationMethod.type_()

    @property
    def selected_value(self) -> '_1858.BasicStaticLoadRatingCalculationMethod':
        """BasicStaticLoadRatingCalculationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1858.BasicStaticLoadRatingCalculationMethod]':
        """List[BasicStaticLoadRatingCalculationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_FatigueLoadLimitCalculationMethodEnum(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_FatigueLoadLimitCalculationMethodEnum

    A specific implementation of 'EnumWithSelectedValue' for 'FatigueLoadLimitCalculationMethodEnum' types.
    """
    __qualname__ = 'FatigueLoadLimitCalculationMethodEnum'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2139.FatigueLoadLimitCalculationMethodEnum':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2139.FatigueLoadLimitCalculationMethodEnum

    @classmethod
    def implicit_type(cls) -> '_2139.FatigueLoadLimitCalculationMethodEnum.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2139.FatigueLoadLimitCalculationMethodEnum.type_()

    @property
    def selected_value(self) -> '_2139.FatigueLoadLimitCalculationMethodEnum':
        """FatigueLoadLimitCalculationMethodEnum: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2139.FatigueLoadLimitCalculationMethodEnum]':
        """List[FatigueLoadLimitCalculationMethodEnum]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RollingBearingRaceType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RollingBearingRaceType

    A specific implementation of 'EnumWithSelectedValue' for 'RollingBearingRaceType' types.
    """
    __qualname__ = 'RollingBearingRaceType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1882.RollingBearingRaceType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1882.RollingBearingRaceType

    @classmethod
    def implicit_type(cls) -> '_1882.RollingBearingRaceType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1882.RollingBearingRaceType.type_()

    @property
    def selected_value(self) -> '_1882.RollingBearingRaceType':
        """RollingBearingRaceType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1882.RollingBearingRaceType]':
        """List[RollingBearingRaceType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RotationalDirections(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RotationalDirections

    A specific implementation of 'EnumWithSelectedValue' for 'RotationalDirections' types.
    """
    __qualname__ = 'RotationalDirections'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1884.RotationalDirections':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1884.RotationalDirections

    @classmethod
    def implicit_type(cls) -> '_1884.RotationalDirections.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1884.RotationalDirections.type_()

    @property
    def selected_value(self) -> '_1884.RotationalDirections':
        """RotationalDirections: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1884.RotationalDirections]':
        """List[RotationalDirections]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BearingEfficiencyRatingMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BearingEfficiencyRatingMethod

    A specific implementation of 'EnumWithSelectedValue' for 'BearingEfficiencyRatingMethod' types.
    """
    __qualname__ = 'BearingEfficiencyRatingMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_290.BearingEfficiencyRatingMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _290.BearingEfficiencyRatingMethod

    @classmethod
    def implicit_type(cls) -> '_290.BearingEfficiencyRatingMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _290.BearingEfficiencyRatingMethod.type_()

    @property
    def selected_value(self) -> '_290.BearingEfficiencyRatingMethod':
        """BearingEfficiencyRatingMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_290.BearingEfficiencyRatingMethod]':
        """List[BearingEfficiencyRatingMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing

    A specific implementation of 'EnumWithSelectedValue' for 'ShaftDiameterModificationDueToRollingBearingRing' types.
    """
    __qualname__ = 'ShaftDiameterModificationDueToRollingBearingRing'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2458.ShaftDiameterModificationDueToRollingBearingRing':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2458.ShaftDiameterModificationDueToRollingBearingRing

    @classmethod
    def implicit_type(cls) -> '_2458.ShaftDiameterModificationDueToRollingBearingRing.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2458.ShaftDiameterModificationDueToRollingBearingRing.type_()

    @property
    def selected_value(self) -> '_2458.ShaftDiameterModificationDueToRollingBearingRing':
        """ShaftDiameterModificationDueToRollingBearingRing: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2458.ShaftDiameterModificationDueToRollingBearingRing]':
        """List[ShaftDiameterModificationDueToRollingBearingRing]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ExcitationAnalysisViewOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ExcitationAnalysisViewOption

    A specific implementation of 'EnumWithSelectedValue' for 'ExcitationAnalysisViewOption' types.
    """
    __qualname__ = 'ExcitationAnalysisViewOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2245.ExcitationAnalysisViewOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2245.ExcitationAnalysisViewOption

    @classmethod
    def implicit_type(cls) -> '_2245.ExcitationAnalysisViewOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2245.ExcitationAnalysisViewOption.type_()

    @property
    def selected_value(self) -> '_2245.ExcitationAnalysisViewOption':
        """ExcitationAnalysisViewOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2245.ExcitationAnalysisViewOption]':
        """List[ExcitationAnalysisViewOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection

    A specific implementation of 'EnumWithSelectedValue' for 'ThreeDViewContourOptionFirstSelection' types.
    """
    __qualname__ = 'ThreeDViewContourOptionFirstSelection'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1811.ThreeDViewContourOptionFirstSelection':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1811.ThreeDViewContourOptionFirstSelection

    @classmethod
    def implicit_type(cls) -> '_1811.ThreeDViewContourOptionFirstSelection.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1811.ThreeDViewContourOptionFirstSelection.type_()

    @property
    def selected_value(self) -> '_1811.ThreeDViewContourOptionFirstSelection':
        """ThreeDViewContourOptionFirstSelection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1811.ThreeDViewContourOptionFirstSelection]':
        """List[ThreeDViewContourOptionFirstSelection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection

    A specific implementation of 'EnumWithSelectedValue' for 'ThreeDViewContourOptionSecondSelection' types.
    """
    __qualname__ = 'ThreeDViewContourOptionSecondSelection'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1812.ThreeDViewContourOptionSecondSelection':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1812.ThreeDViewContourOptionSecondSelection

    @classmethod
    def implicit_type(cls) -> '_1812.ThreeDViewContourOptionSecondSelection.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1812.ThreeDViewContourOptionSecondSelection.type_()

    @property
    def selected_value(self) -> '_1812.ThreeDViewContourOptionSecondSelection':
        """ThreeDViewContourOptionSecondSelection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1812.ThreeDViewContourOptionSecondSelection]':
        """List[ThreeDViewContourOptionSecondSelection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ComponentOrientationOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ComponentOrientationOption

    A specific implementation of 'EnumWithSelectedValue' for 'ComponentOrientationOption' types.
    """
    __qualname__ = 'ComponentOrientationOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2349.ComponentOrientationOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2349.ComponentOrientationOption

    @classmethod
    def implicit_type(cls) -> '_2349.ComponentOrientationOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2349.ComponentOrientationOption.type_()

    @property
    def selected_value(self) -> '_2349.ComponentOrientationOption':
        """ComponentOrientationOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2349.ComponentOrientationOption]':
        """List[ComponentOrientationOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_Axis(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_Axis

    A specific implementation of 'EnumWithSelectedValue' for 'Axis' types.
    """
    __qualname__ = 'Axis'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1482.Axis':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1482.Axis

    @classmethod
    def implicit_type(cls) -> '_1482.Axis.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1482.Axis.type_()

    @property
    def selected_value(self) -> '_1482.Axis':
        """Axis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1482.Axis]':
        """List[Axis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_AlignmentAxis(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_AlignmentAxis

    A specific implementation of 'EnumWithSelectedValue' for 'AlignmentAxis' types.
    """
    __qualname__ = 'AlignmentAxis'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1481.AlignmentAxis':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1481.AlignmentAxis

    @classmethod
    def implicit_type(cls) -> '_1481.AlignmentAxis.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1481.AlignmentAxis.type_()

    @property
    def selected_value(self) -> '_1481.AlignmentAxis':
        """AlignmentAxis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1481.AlignmentAxis]':
        """List[AlignmentAxis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_DesignEntityId(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DesignEntityId

    A specific implementation of 'EnumWithSelectedValue' for 'DesignEntityId' types.
    """
    __qualname__ = 'DesignEntityId'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2191.DesignEntityId':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2191.DesignEntityId

    @classmethod
    def implicit_type(cls) -> '_2191.DesignEntityId.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2191.DesignEntityId.type_()

    @property
    def selected_value(self) -> '_2191.DesignEntityId':
        """DesignEntityId: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2191.DesignEntityId]':
        """List[DesignEntityId]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ThermalExpansionOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ThermalExpansionOption

    A specific implementation of 'EnumWithSelectedValue' for 'ThermalExpansionOption' types.
    """
    __qualname__ = 'ThermalExpansionOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2394.ThermalExpansionOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2394.ThermalExpansionOption

    @classmethod
    def implicit_type(cls) -> '_2394.ThermalExpansionOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2394.ThermalExpansionOption.type_()

    @property
    def selected_value(self) -> '_2394.ThermalExpansionOption':
        """ThermalExpansionOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2394.ThermalExpansionOption]':
        """List[ThermalExpansionOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_FESubstructureType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_FESubstructureType

    A specific implementation of 'EnumWithSelectedValue' for 'FESubstructureType' types.
    """
    __qualname__ = 'FESubstructureType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2371.FESubstructureType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2371.FESubstructureType

    @classmethod
    def implicit_type(cls) -> '_2371.FESubstructureType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2371.FESubstructureType.type_()

    @property
    def selected_value(self) -> '_2371.FESubstructureType':
        """FESubstructureType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2371.FESubstructureType]':
        """List[FESubstructureType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_FEExportFormat(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_FEExportFormat

    A specific implementation of 'EnumWithSelectedValue' for 'FEExportFormat' types.
    """
    __qualname__ = 'FEExportFormat'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_166.FEExportFormat':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _166.FEExportFormat

    @classmethod
    def implicit_type(cls) -> '_166.FEExportFormat.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _166.FEExportFormat.type_()

    @property
    def selected_value(self) -> '_166.FEExportFormat':
        """FEExportFormat: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_166.FEExportFormat]':
        """List[FEExportFormat]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ThreeDViewContourOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ThreeDViewContourOption

    A specific implementation of 'EnumWithSelectedValue' for 'ThreeDViewContourOption' types.
    """
    __qualname__ = 'ThreeDViewContourOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1810.ThreeDViewContourOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1810.ThreeDViewContourOption

    @classmethod
    def implicit_type(cls) -> '_1810.ThreeDViewContourOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1810.ThreeDViewContourOption.type_()

    @property
    def selected_value(self) -> '_1810.ThreeDViewContourOption':
        """ThreeDViewContourOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1810.ThreeDViewContourOption]':
        """List[ThreeDViewContourOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BoundaryConditionType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BoundaryConditionType

    A specific implementation of 'EnumWithSelectedValue' for 'BoundaryConditionType' types.
    """
    __qualname__ = 'BoundaryConditionType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_165.BoundaryConditionType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _165.BoundaryConditionType

    @classmethod
    def implicit_type(cls) -> '_165.BoundaryConditionType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _165.BoundaryConditionType.type_()

    @property
    def selected_value(self) -> '_165.BoundaryConditionType':
        """BoundaryConditionType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_165.BoundaryConditionType]':
        """List[BoundaryConditionType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BearingNodeOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BearingNodeOption

    A specific implementation of 'EnumWithSelectedValue' for 'BearingNodeOption' types.
    """
    __qualname__ = 'BearingNodeOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2346.BearingNodeOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2346.BearingNodeOption

    @classmethod
    def implicit_type(cls) -> '_2346.BearingNodeOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2346.BearingNodeOption.type_()

    @property
    def selected_value(self) -> '_2346.BearingNodeOption':
        """BearingNodeOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2346.BearingNodeOption]':
        """List[BearingNodeOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LinkNodeSource(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LinkNodeSource

    A specific implementation of 'EnumWithSelectedValue' for 'LinkNodeSource' types.
    """
    __qualname__ = 'LinkNodeSource'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2381.LinkNodeSource':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2381.LinkNodeSource

    @classmethod
    def implicit_type(cls) -> '_2381.LinkNodeSource.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2381.LinkNodeSource.type_()

    @property
    def selected_value(self) -> '_2381.LinkNodeSource':
        """LinkNodeSource: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2381.LinkNodeSource]':
        """List[LinkNodeSource]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BearingToleranceClass(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BearingToleranceClass

    A specific implementation of 'EnumWithSelectedValue' for 'BearingToleranceClass' types.
    """
    __qualname__ = 'BearingToleranceClass'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1890.BearingToleranceClass':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1890.BearingToleranceClass

    @classmethod
    def implicit_type(cls) -> '_1890.BearingToleranceClass.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1890.BearingToleranceClass.type_()

    @property
    def selected_value(self) -> '_1890.BearingToleranceClass':
        """BearingToleranceClass: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1890.BearingToleranceClass]':
        """List[BearingToleranceClass]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BearingModel(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BearingModel

    A specific implementation of 'EnumWithSelectedValue' for 'BearingModel' types.
    """
    __qualname__ = 'BearingModel'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1864.BearingModel':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1864.BearingModel

    @classmethod
    def implicit_type(cls) -> '_1864.BearingModel.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1864.BearingModel.type_()

    @property
    def selected_value(self) -> '_1864.BearingModel':
        """BearingModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1864.BearingModel]':
        """List[BearingModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_PreloadType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_PreloadType

    A specific implementation of 'EnumWithSelectedValue' for 'PreloadType' types.
    """
    __qualname__ = 'PreloadType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1948.PreloadType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1948.PreloadType

    @classmethod
    def implicit_type(cls) -> '_1948.PreloadType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1948.PreloadType.type_()

    @property
    def selected_value(self) -> '_1948.PreloadType':
        """PreloadType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1948.PreloadType]':
        """List[PreloadType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RaceAxialMountingType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RaceAxialMountingType

    A specific implementation of 'EnumWithSelectedValue' for 'RaceAxialMountingType' types.
    """
    __qualname__ = 'RaceAxialMountingType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1950.RaceAxialMountingType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1950.RaceAxialMountingType

    @classmethod
    def implicit_type(cls) -> '_1950.RaceAxialMountingType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1950.RaceAxialMountingType.type_()

    @property
    def selected_value(self) -> '_1950.RaceAxialMountingType':
        """RaceAxialMountingType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1950.RaceAxialMountingType]':
        """List[RaceAxialMountingType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RaceRadialMountingType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RaceRadialMountingType

    A specific implementation of 'EnumWithSelectedValue' for 'RaceRadialMountingType' types.
    """
    __qualname__ = 'RaceRadialMountingType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1951.RaceRadialMountingType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1951.RaceRadialMountingType

    @classmethod
    def implicit_type(cls) -> '_1951.RaceRadialMountingType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1951.RaceRadialMountingType.type_()

    @property
    def selected_value(self) -> '_1951.RaceRadialMountingType':
        """RaceRadialMountingType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1951.RaceRadialMountingType]':
        """List[RaceRadialMountingType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_InternalClearanceClass(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_InternalClearanceClass

    A specific implementation of 'EnumWithSelectedValue' for 'InternalClearanceClass' types.
    """
    __qualname__ = 'InternalClearanceClass'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1889.InternalClearanceClass':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1889.InternalClearanceClass

    @classmethod
    def implicit_type(cls) -> '_1889.InternalClearanceClass.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1889.InternalClearanceClass.type_()

    @property
    def selected_value(self) -> '_1889.InternalClearanceClass':
        """InternalClearanceClass: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1889.InternalClearanceClass]':
        """List[InternalClearanceClass]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BearingToleranceDefinitionOptions(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BearingToleranceDefinitionOptions

    A specific implementation of 'EnumWithSelectedValue' for 'BearingToleranceDefinitionOptions' types.
    """
    __qualname__ = 'BearingToleranceDefinitionOptions'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1891.BearingToleranceDefinitionOptions':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1891.BearingToleranceDefinitionOptions

    @classmethod
    def implicit_type(cls) -> '_1891.BearingToleranceDefinitionOptions.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1891.BearingToleranceDefinitionOptions.type_()

    @property
    def selected_value(self) -> '_1891.BearingToleranceDefinitionOptions':
        """BearingToleranceDefinitionOptions: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1891.BearingToleranceDefinitionOptions]':
        """List[BearingToleranceDefinitionOptions]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_OilSealLossCalculationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_OilSealLossCalculationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'OilSealLossCalculationMethod' types.
    """
    __qualname__ = 'OilSealLossCalculationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_298.OilSealLossCalculationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _298.OilSealLossCalculationMethod

    @classmethod
    def implicit_type(cls) -> '_298.OilSealLossCalculationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _298.OilSealLossCalculationMethod.type_()

    @property
    def selected_value(self) -> '_298.OilSealLossCalculationMethod':
        """OilSealLossCalculationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_298.OilSealLossCalculationMethod]':
        """List[OilSealLossCalculationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_PowerLoadType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_PowerLoadType

    A specific implementation of 'EnumWithSelectedValue' for 'PowerLoadType' types.
    """
    __qualname__ = 'PowerLoadType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2206.PowerLoadType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2206.PowerLoadType

    @classmethod
    def implicit_type(cls) -> '_2206.PowerLoadType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2206.PowerLoadType.type_()

    @property
    def selected_value(self) -> '_2206.PowerLoadType':
        """PowerLoadType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2206.PowerLoadType]':
        """List[PowerLoadType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RigidConnectorStiffnessType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RigidConnectorStiffnessType

    A specific implementation of 'EnumWithSelectedValue' for 'RigidConnectorStiffnessType' types.
    """
    __qualname__ = 'RigidConnectorStiffnessType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2573.RigidConnectorStiffnessType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2573.RigidConnectorStiffnessType

    @classmethod
    def implicit_type(cls) -> '_2573.RigidConnectorStiffnessType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2573.RigidConnectorStiffnessType.type_()

    @property
    def selected_value(self) -> '_2573.RigidConnectorStiffnessType':
        """RigidConnectorStiffnessType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2573.RigidConnectorStiffnessType]':
        """List[RigidConnectorStiffnessType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RigidConnectorToothSpacingType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RigidConnectorToothSpacingType

    A specific implementation of 'EnumWithSelectedValue' for 'RigidConnectorToothSpacingType' types.
    """
    __qualname__ = 'RigidConnectorToothSpacingType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2576.RigidConnectorToothSpacingType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2576.RigidConnectorToothSpacingType

    @classmethod
    def implicit_type(cls) -> '_2576.RigidConnectorToothSpacingType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2576.RigidConnectorToothSpacingType.type_()

    @property
    def selected_value(self) -> '_2576.RigidConnectorToothSpacingType':
        """RigidConnectorToothSpacingType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2576.RigidConnectorToothSpacingType]':
        """List[RigidConnectorToothSpacingType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RigidConnectorTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RigidConnectorTypes

    A specific implementation of 'EnumWithSelectedValue' for 'RigidConnectorTypes' types.
    """
    __qualname__ = 'RigidConnectorTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2577.RigidConnectorTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2577.RigidConnectorTypes

    @classmethod
    def implicit_type(cls) -> '_2577.RigidConnectorTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2577.RigidConnectorTypes.type_()

    @property
    def selected_value(self) -> '_2577.RigidConnectorTypes':
        """RigidConnectorTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2577.RigidConnectorTypes]':
        """List[RigidConnectorTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_FitTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_FitTypes

    A specific implementation of 'EnumWithSelectedValue' for 'FitTypes' types.
    """
    __qualname__ = 'FitTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1385.FitTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1385.FitTypes

    @classmethod
    def implicit_type(cls) -> '_1385.FitTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1385.FitTypes.type_()

    @property
    def selected_value(self) -> '_1385.FitTypes':
        """FitTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1385.FitTypes]':
        """List[FitTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_DoeValueSpecificationOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DoeValueSpecificationOption

    A specific implementation of 'EnumWithSelectedValue' for 'DoeValueSpecificationOption' types.
    """
    __qualname__ = 'DoeValueSpecificationOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_4327.DoeValueSpecificationOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _4327.DoeValueSpecificationOption

    @classmethod
    def implicit_type(cls) -> '_4327.DoeValueSpecificationOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _4327.DoeValueSpecificationOption.type_()

    @property
    def selected_value(self) -> '_4327.DoeValueSpecificationOption':
        """DoeValueSpecificationOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_4327.DoeValueSpecificationOption]':
        """List[DoeValueSpecificationOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_AnalysisType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_AnalysisType

    A specific implementation of 'EnumWithSelectedValue' for 'AnalysisType' types.
    """
    __qualname__ = 'AnalysisType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6785.AnalysisType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6785.AnalysisType

    @classmethod
    def implicit_type(cls) -> '_6785.AnalysisType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6785.AnalysisType.type_()

    @property
    def selected_value(self) -> '_6785.AnalysisType':
        """AnalysisType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_6785.AnalysisType]':
        """List[AnalysisType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BarModelExportType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BarModelExportType

    A specific implementation of 'EnumWithSelectedValue' for 'BarModelExportType' types.
    """
    __qualname__ = 'BarModelExportType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_53.BarModelExportType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _53.BarModelExportType

    @classmethod
    def implicit_type(cls) -> '_53.BarModelExportType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _53.BarModelExportType.type_()

    @property
    def selected_value(self) -> '_53.BarModelExportType':
        """BarModelExportType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_53.BarModelExportType]':
        """List[BarModelExportType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_DynamicsResponse3DChartType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DynamicsResponse3DChartType

    A specific implementation of 'EnumWithSelectedValue' for 'DynamicsResponse3DChartType' types.
    """
    __qualname__ = 'DynamicsResponse3DChartType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_4603.DynamicsResponse3DChartType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _4603.DynamicsResponse3DChartType

    @classmethod
    def implicit_type(cls) -> '_4603.DynamicsResponse3DChartType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _4603.DynamicsResponse3DChartType.type_()

    @property
    def selected_value(self) -> '_4603.DynamicsResponse3DChartType':
        """DynamicsResponse3DChartType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_4603.DynamicsResponse3DChartType]':
        """List[DynamicsResponse3DChartType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ComplexPartDisplayOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ComplexPartDisplayOption

    A specific implementation of 'EnumWithSelectedValue' for 'ComplexPartDisplayOption' types.
    """
    __qualname__ = 'ComplexPartDisplayOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1485.ComplexPartDisplayOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1485.ComplexPartDisplayOption

    @classmethod
    def implicit_type(cls) -> '_1485.ComplexPartDisplayOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1485.ComplexPartDisplayOption.type_()

    @property
    def selected_value(self) -> '_1485.ComplexPartDisplayOption':
        """ComplexPartDisplayOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1485.ComplexPartDisplayOption]':
        """List[ComplexPartDisplayOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_DynamicsResponseType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DynamicsResponseType

    A specific implementation of 'EnumWithSelectedValue' for 'DynamicsResponseType' types.
    """
    __qualname__ = 'DynamicsResponseType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_4604.DynamicsResponseType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _4604.DynamicsResponseType

    @classmethod
    def implicit_type(cls) -> '_4604.DynamicsResponseType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _4604.DynamicsResponseType.type_()

    @property
    def selected_value(self) -> '_4604.DynamicsResponseType':
        """DynamicsResponseType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_4604.DynamicsResponseType]':
        """List[DynamicsResponseType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BearingStiffnessModel(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BearingStiffnessModel

    A specific implementation of 'EnumWithSelectedValue' for 'BearingStiffnessModel' types.
    """
    __qualname__ = 'BearingStiffnessModel'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5360.BearingStiffnessModel':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5360.BearingStiffnessModel

    @classmethod
    def implicit_type(cls) -> '_5360.BearingStiffnessModel.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5360.BearingStiffnessModel.type_()

    @property
    def selected_value(self) -> '_5360.BearingStiffnessModel':
        """BearingStiffnessModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_5360.BearingStiffnessModel]':
        """List[BearingStiffnessModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_GearMeshStiffnessModel(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_GearMeshStiffnessModel

    A specific implementation of 'EnumWithSelectedValue' for 'GearMeshStiffnessModel' types.
    """
    __qualname__ = 'GearMeshStiffnessModel'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5412.GearMeshStiffnessModel':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5412.GearMeshStiffnessModel

    @classmethod
    def implicit_type(cls) -> '_5412.GearMeshStiffnessModel.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5412.GearMeshStiffnessModel.type_()

    @property
    def selected_value(self) -> '_5412.GearMeshStiffnessModel':
        """GearMeshStiffnessModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_5412.GearMeshStiffnessModel]':
        """List[GearMeshStiffnessModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ShaftAndHousingFlexibilityOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ShaftAndHousingFlexibilityOption

    A specific implementation of 'EnumWithSelectedValue' for 'ShaftAndHousingFlexibilityOption' types.
    """
    __qualname__ = 'ShaftAndHousingFlexibilityOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5457.ShaftAndHousingFlexibilityOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5457.ShaftAndHousingFlexibilityOption

    @classmethod
    def implicit_type(cls) -> '_5457.ShaftAndHousingFlexibilityOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5457.ShaftAndHousingFlexibilityOption.type_()

    @property
    def selected_value(self) -> '_5457.ShaftAndHousingFlexibilityOption':
        """ShaftAndHousingFlexibilityOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_5457.ShaftAndHousingFlexibilityOption]':
        """List[ShaftAndHousingFlexibilityOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ExportOutputType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ExportOutputType

    A specific implementation of 'EnumWithSelectedValue' for 'ExportOutputType' types.
    """
    __qualname__ = 'ExportOutputType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5717.ExportOutputType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5717.ExportOutputType

    @classmethod
    def implicit_type(cls) -> '_5717.ExportOutputType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5717.ExportOutputType.type_()

    @property
    def selected_value(self) -> '_5717.ExportOutputType':
        """ExportOutputType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_5717.ExportOutputType]':
        """List[ExportOutputType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_HarmonicAnalysisFEExportOptions_ComplexNumberOutput(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_HarmonicAnalysisFEExportOptions_ComplexNumberOutput

    A specific implementation of 'EnumWithSelectedValue' for 'HarmonicAnalysisFEExportOptions.ComplexNumberOutput' types.
    """
    __qualname__ = 'HarmonicAnalysisFEExportOptions.ComplexNumberOutput'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5735.HarmonicAnalysisFEExportOptions.ComplexNumberOutput':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5735.HarmonicAnalysisFEExportOptions.ComplexNumberOutput

    @classmethod
    def implicit_type(cls) -> '_5735.HarmonicAnalysisFEExportOptions.ComplexNumberOutput.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5735.HarmonicAnalysisFEExportOptions.ComplexNumberOutput.type_()

    @property
    def selected_value(self) -> '_5735.HarmonicAnalysisFEExportOptions.ComplexNumberOutput':
        """HarmonicAnalysisFEExportOptions.ComplexNumberOutput: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_5735.HarmonicAnalysisFEExportOptions.ComplexNumberOutput]':
        """List[HarmonicAnalysisFEExportOptions.ComplexNumberOutput]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_StiffnessOptionsForHarmonicAnalysis_StepCreation(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_StiffnessOptionsForHarmonicAnalysis_StepCreation

    A specific implementation of 'EnumWithSelectedValue' for 'StiffnessOptionsForHarmonicAnalysis.StepCreation' types.
    """
    __qualname__ = 'StiffnessOptionsForHarmonicAnalysis.StepCreation'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5788.StiffnessOptionsForHarmonicAnalysis.StepCreation':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5788.StiffnessOptionsForHarmonicAnalysis.StepCreation

    @classmethod
    def implicit_type(cls) -> '_5788.StiffnessOptionsForHarmonicAnalysis.StepCreation.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5788.StiffnessOptionsForHarmonicAnalysis.StepCreation.type_()

    @property
    def selected_value(self) -> '_5788.StiffnessOptionsForHarmonicAnalysis.StepCreation':
        """StiffnessOptionsForHarmonicAnalysis.StepCreation: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_5788.StiffnessOptionsForHarmonicAnalysis.StepCreation]':
        """List[StiffnessOptionsForHarmonicAnalysis.StepCreation]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_HarmonicAnalysisTorqueInputType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_HarmonicAnalysisTorqueInputType

    A specific implementation of 'EnumWithSelectedValue' for 'HarmonicAnalysisTorqueInputType' types.
    """
    __qualname__ = 'HarmonicAnalysisTorqueInputType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5739.HarmonicAnalysisTorqueInputType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5739.HarmonicAnalysisTorqueInputType

    @classmethod
    def implicit_type(cls) -> '_5739.HarmonicAnalysisTorqueInputType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5739.HarmonicAnalysisTorqueInputType.type_()

    @property
    def selected_value(self) -> '_5739.HarmonicAnalysisTorqueInputType':
        """HarmonicAnalysisTorqueInputType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_5739.HarmonicAnalysisTorqueInputType]':
        """List[HarmonicAnalysisTorqueInputType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_FrictionModelForGyroscopicMoment(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_FrictionModelForGyroscopicMoment

    A specific implementation of 'EnumWithSelectedValue' for 'FrictionModelForGyroscopicMoment' types.
    """
    __qualname__ = 'FrictionModelForGyroscopicMoment'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1959.FrictionModelForGyroscopicMoment':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1959.FrictionModelForGyroscopicMoment

    @classmethod
    def implicit_type(cls) -> '_1959.FrictionModelForGyroscopicMoment.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1959.FrictionModelForGyroscopicMoment.type_()

    @property
    def selected_value(self) -> '_1959.FrictionModelForGyroscopicMoment':
        """FrictionModelForGyroscopicMoment: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1959.FrictionModelForGyroscopicMoment]':
        """List[FrictionModelForGyroscopicMoment]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_MeshStiffnessModel(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_MeshStiffnessModel

    A specific implementation of 'EnumWithSelectedValue' for 'MeshStiffnessModel' types.
    """
    __qualname__ = 'MeshStiffnessModel'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2201.MeshStiffnessModel':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2201.MeshStiffnessModel

    @classmethod
    def implicit_type(cls) -> '_2201.MeshStiffnessModel.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2201.MeshStiffnessModel.type_()

    @property
    def selected_value(self) -> '_2201.MeshStiffnessModel':
        """MeshStiffnessModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2201.MeshStiffnessModel]':
        """List[MeshStiffnessModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ShearAreaFactorMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ShearAreaFactorMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ShearAreaFactorMethod' types.
    """
    __qualname__ = 'ShearAreaFactorMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_130.ShearAreaFactorMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _130.ShearAreaFactorMethod

    @classmethod
    def implicit_type(cls) -> '_130.ShearAreaFactorMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _130.ShearAreaFactorMethod.type_()

    @property
    def selected_value(self) -> '_130.ShearAreaFactorMethod':
        """ShearAreaFactorMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_130.ShearAreaFactorMethod]':
        """List[ShearAreaFactorMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_StressConcentrationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_StressConcentrationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'StressConcentrationMethod' types.
    """
    __qualname__ = 'StressConcentrationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2096.StressConcentrationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2096.StressConcentrationMethod

    @classmethod
    def implicit_type(cls) -> '_2096.StressConcentrationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2096.StressConcentrationMethod.type_()

    @property
    def selected_value(self) -> '_2096.StressConcentrationMethod':
        """StressConcentrationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2096.StressConcentrationMethod]':
        """List[StressConcentrationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BallBearingAnalysisMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BallBearingAnalysisMethod

    A specific implementation of 'EnumWithSelectedValue' for 'BallBearingAnalysisMethod' types.
    """
    __qualname__ = 'BallBearingAnalysisMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1953.BallBearingAnalysisMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1953.BallBearingAnalysisMethod

    @classmethod
    def implicit_type(cls) -> '_1953.BallBearingAnalysisMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1953.BallBearingAnalysisMethod.type_()

    @property
    def selected_value(self) -> '_1953.BallBearingAnalysisMethod':
        """BallBearingAnalysisMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1953.BallBearingAnalysisMethod]':
        """List[BallBearingAnalysisMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_HertzianContactDeflectionCalculationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_HertzianContactDeflectionCalculationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'HertzianContactDeflectionCalculationMethod' types.
    """
    __qualname__ = 'HertzianContactDeflectionCalculationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1564.HertzianContactDeflectionCalculationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1564.HertzianContactDeflectionCalculationMethod

    @classmethod
    def implicit_type(cls) -> '_1564.HertzianContactDeflectionCalculationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1564.HertzianContactDeflectionCalculationMethod.type_()

    @property
    def selected_value(self) -> '_1564.HertzianContactDeflectionCalculationMethod':
        """HertzianContactDeflectionCalculationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1564.HertzianContactDeflectionCalculationMethod]':
        """List[HertzianContactDeflectionCalculationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_TorqueRippleInputType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_TorqueRippleInputType

    A specific implementation of 'EnumWithSelectedValue' for 'TorqueRippleInputType' types.
    """
    __qualname__ = 'TorqueRippleInputType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6944.TorqueRippleInputType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6944.TorqueRippleInputType

    @classmethod
    def implicit_type(cls) -> '_6944.TorqueRippleInputType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6944.TorqueRippleInputType.type_()

    @property
    def selected_value(self) -> '_6944.TorqueRippleInputType':
        """TorqueRippleInputType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_6944.TorqueRippleInputType]':
        """List[TorqueRippleInputType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_HarmonicExcitationType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_HarmonicExcitationType

    A specific implementation of 'EnumWithSelectedValue' for 'HarmonicExcitationType' types.
    """
    __qualname__ = 'HarmonicExcitationType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6865.HarmonicExcitationType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6865.HarmonicExcitationType

    @classmethod
    def implicit_type(cls) -> '_6865.HarmonicExcitationType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6865.HarmonicExcitationType.type_()

    @property
    def selected_value(self) -> '_6865.HarmonicExcitationType':
        """HarmonicExcitationType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_6865.HarmonicExcitationType]':
        """List[HarmonicExcitationType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification

    A specific implementation of 'EnumWithSelectedValue' for 'PointLoadLoadCase.ForceSpecification' types.
    """
    __qualname__ = 'PointLoadLoadCase.ForceSpecification'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6906.PointLoadLoadCase.ForceSpecification':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6906.PointLoadLoadCase.ForceSpecification

    @classmethod
    def implicit_type(cls) -> '_6906.PointLoadLoadCase.ForceSpecification.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6906.PointLoadLoadCase.ForceSpecification.type_()

    @property
    def selected_value(self) -> '_6906.PointLoadLoadCase.ForceSpecification':
        """PointLoadLoadCase.ForceSpecification: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_6906.PointLoadLoadCase.ForceSpecification]':
        """List[PointLoadLoadCase.ForceSpecification]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_TorqueSpecificationForSystemDeflection(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_TorqueSpecificationForSystemDeflection

    A specific implementation of 'EnumWithSelectedValue' for 'TorqueSpecificationForSystemDeflection' types.
    """
    __qualname__ = 'TorqueSpecificationForSystemDeflection'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6945.TorqueSpecificationForSystemDeflection':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6945.TorqueSpecificationForSystemDeflection

    @classmethod
    def implicit_type(cls) -> '_6945.TorqueSpecificationForSystemDeflection.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6945.TorqueSpecificationForSystemDeflection.type_()

    @property
    def selected_value(self) -> '_6945.TorqueSpecificationForSystemDeflection':
        """TorqueSpecificationForSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_6945.TorqueSpecificationForSystemDeflection]':
        """List[TorqueSpecificationForSystemDeflection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'PowerLoadInputTorqueSpecificationMethod' types.
    """
    __qualname__ = 'PowerLoadInputTorqueSpecificationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2204.PowerLoadInputTorqueSpecificationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2204.PowerLoadInputTorqueSpecificationMethod

    @classmethod
    def implicit_type(cls) -> '_2204.PowerLoadInputTorqueSpecificationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2204.PowerLoadInputTorqueSpecificationMethod.type_()

    @property
    def selected_value(self) -> '_2204.PowerLoadInputTorqueSpecificationMethod':
        """PowerLoadInputTorqueSpecificationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2204.PowerLoadInputTorqueSpecificationMethod]':
        """List[PowerLoadInputTorqueSpecificationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_TorqueConverterLockupRule(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_TorqueConverterLockupRule

    A specific implementation of 'EnumWithSelectedValue' for 'TorqueConverterLockupRule' types.
    """
    __qualname__ = 'TorqueConverterLockupRule'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5482.TorqueConverterLockupRule':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5482.TorqueConverterLockupRule

    @classmethod
    def implicit_type(cls) -> '_5482.TorqueConverterLockupRule.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5482.TorqueConverterLockupRule.type_()

    @property
    def selected_value(self) -> '_5482.TorqueConverterLockupRule':
        """TorqueConverterLockupRule: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_5482.TorqueConverterLockupRule]':
        """List[TorqueConverterLockupRule]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_DegreeOfFreedom(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DegreeOfFreedom

    A specific implementation of 'EnumWithSelectedValue' for 'DegreeOfFreedom' types.
    """
    __qualname__ = 'DegreeOfFreedom'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1494.DegreeOfFreedom':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1494.DegreeOfFreedom

    @classmethod
    def implicit_type(cls) -> '_1494.DegreeOfFreedom.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1494.DegreeOfFreedom.type_()

    @property
    def selected_value(self) -> '_1494.DegreeOfFreedom':
        """DegreeOfFreedom: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1494.DegreeOfFreedom]':
        """List[DegreeOfFreedom]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_DestinationDesignState(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DestinationDesignState

    A specific implementation of 'EnumWithSelectedValue' for 'DestinationDesignState' types.
    """
    __qualname__ = 'DestinationDesignState'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6959.DestinationDesignState':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6959.DestinationDesignState

    @classmethod
    def implicit_type(cls) -> '_6959.DestinationDesignState.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6959.DestinationDesignState.type_()

    @property
    def selected_value(self) -> '_6959.DestinationDesignState':
        """DestinationDesignState: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_6959.DestinationDesignState]':
        """List[DestinationDesignState]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None
