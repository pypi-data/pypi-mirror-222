﻿"""_6969.py

TimeSeriesImporter
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TIME_SERIES_IMPORTER = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition', 'TimeSeriesImporter')

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1854
    from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
        _6959, _6958, _6961, _6962,
        _6970, _6957, _6964, _6960,
        _6963, _6968, _6971
    )
    from mastapy.system_model.analyses_and_results.static_loads import _6876
    from mastapy.utility.file_access_helpers import _1806


__docformat__ = 'restructuredtext en'
__all__ = ('TimeSeriesImporter',)


class TimeSeriesImporter(_0.APIBase):
    """TimeSeriesImporter

    This is a mastapy class.
    """

    TYPE = _TIME_SERIES_IMPORTER

    class _Cast_TimeSeriesImporter:
        """Special nested class for casting TimeSeriesImporter to subclasses."""

        def __init__(self, parent: 'TimeSeriesImporter'):
            self._parent = parent

        @property
        def time_series_importer(self) -> 'TimeSeriesImporter':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TimeSeriesImporter.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def boost_pressure_chart(self) -> '_1854.TwoDChartDefinition':
        """TwoDChartDefinition: 'BoostPressureChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoostPressureChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def create_load_cases_for_parametric_study_tool(self) -> 'bool':
        """bool: 'CreateLoadCasesForParametricStudyTool' is the original name of this property."""

        temp = self.wrapped.CreateLoadCasesForParametricStudyTool

        if temp is None:
            return False

        return temp

    @create_load_cases_for_parametric_study_tool.setter
    def create_load_cases_for_parametric_study_tool(self, value: 'bool'):
        self.wrapped.CreateLoadCasesForParametricStudyTool = bool(value) if value is not None else False

    @property
    def design_state_name(self) -> 'str':
        """str: 'DesignStateName' is the original name of this property."""

        temp = self.wrapped.DesignStateName

        if temp is None:
            return ''

        return temp

    @design_state_name.setter
    def design_state_name(self, value: 'str'):
        self.wrapped.DesignStateName = str(value) if value is not None else ''

    @property
    def destination_design_state_column(self) -> 'enum_with_selected_value.EnumWithSelectedValue_DestinationDesignState':
        """enum_with_selected_value.EnumWithSelectedValue_DestinationDesignState: 'DestinationDesignStateColumn' is the original name of this property."""

        temp = self.wrapped.DestinationDesignStateColumn

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_DestinationDesignState.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @destination_design_state_column.setter
    def destination_design_state_column(self, value: 'enum_with_selected_value.EnumWithSelectedValue_DestinationDesignState.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_DestinationDesignState.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DestinationDesignStateColumn = value

    @property
    def duty_cycle_duration(self) -> 'float':
        """float: 'DutyCycleDuration' is the original name of this property."""

        temp = self.wrapped.DutyCycleDuration

        if temp is None:
            return 0.0

        return temp

    @duty_cycle_duration.setter
    def duty_cycle_duration(self, value: 'float'):
        self.wrapped.DutyCycleDuration = float(value) if value is not None else 0.0

    @property
    def force_chart(self) -> '_1854.TwoDChartDefinition':
        """TwoDChartDefinition: 'ForceChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_ratios(self) -> 'str':
        """str: 'GearRatios' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearRatios

        if temp is None:
            return ''

        return temp

    @property
    def import_type(self) -> '_6876.ImportType':
        """ImportType: 'ImportType' is the original name of this property."""

        temp = self.wrapped.ImportType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.ImportType')
        return constructor.new_from_mastapy('mastapy.system_model.analyses_and_results.static_loads._6876', 'ImportType')(value) if value is not None else None

    @import_type.setter
    def import_type(self, value: '_6876.ImportType'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.ImportType')
        self.wrapped.ImportType = value

    @property
    def moment_chart(self) -> '_1854.TwoDChartDefinition':
        """TwoDChartDefinition: 'MomentChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MomentChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def number_of_boost_pressure_inputs(self) -> 'int':
        """int: 'NumberOfBoostPressureInputs' is the original name of this property."""

        temp = self.wrapped.NumberOfBoostPressureInputs

        if temp is None:
            return 0

        return temp

    @number_of_boost_pressure_inputs.setter
    def number_of_boost_pressure_inputs(self, value: 'int'):
        self.wrapped.NumberOfBoostPressureInputs = int(value) if value is not None else 0

    @property
    def number_of_cycle_repeats(self) -> 'float':
        """float: 'NumberOfCycleRepeats' is the original name of this property."""

        temp = self.wrapped.NumberOfCycleRepeats

        if temp is None:
            return 0.0

        return temp

    @number_of_cycle_repeats.setter
    def number_of_cycle_repeats(self, value: 'float'):
        self.wrapped.NumberOfCycleRepeats = float(value) if value is not None else 0.0

    @property
    def number_of_data_files(self) -> 'int':
        """int: 'NumberOfDataFiles' is the original name of this property."""

        temp = self.wrapped.NumberOfDataFiles

        if temp is None:
            return 0

        return temp

    @number_of_data_files.setter
    def number_of_data_files(self, value: 'int'):
        self.wrapped.NumberOfDataFiles = int(value) if value is not None else 0

    @property
    def number_of_extra_points_for_ramp_sections(self) -> 'int':
        """int: 'NumberOfExtraPointsForRampSections' is the original name of this property."""

        temp = self.wrapped.NumberOfExtraPointsForRampSections

        if temp is None:
            return 0

        return temp

    @number_of_extra_points_for_ramp_sections.setter
    def number_of_extra_points_for_ramp_sections(self, value: 'int'):
        self.wrapped.NumberOfExtraPointsForRampSections = int(value) if value is not None else 0

    @property
    def number_of_force_inputs(self) -> 'int':
        """int: 'NumberOfForceInputs' is the original name of this property."""

        temp = self.wrapped.NumberOfForceInputs

        if temp is None:
            return 0

        return temp

    @number_of_force_inputs.setter
    def number_of_force_inputs(self, value: 'int'):
        self.wrapped.NumberOfForceInputs = int(value) if value is not None else 0

    @property
    def number_of_moment_inputs(self) -> 'int':
        """int: 'NumberOfMomentInputs' is the original name of this property."""

        temp = self.wrapped.NumberOfMomentInputs

        if temp is None:
            return 0

        return temp

    @number_of_moment_inputs.setter
    def number_of_moment_inputs(self, value: 'int'):
        self.wrapped.NumberOfMomentInputs = int(value) if value is not None else 0

    @property
    def number_of_speed_inputs(self) -> 'int':
        """int: 'NumberOfSpeedInputs' is the original name of this property."""

        temp = self.wrapped.NumberOfSpeedInputs

        if temp is None:
            return 0

        return temp

    @number_of_speed_inputs.setter
    def number_of_speed_inputs(self, value: 'int'):
        self.wrapped.NumberOfSpeedInputs = int(value) if value is not None else 0

    @property
    def number_of_torque_inputs(self) -> 'int':
        """int: 'NumberOfTorqueInputs' is the original name of this property."""

        temp = self.wrapped.NumberOfTorqueInputs

        if temp is None:
            return 0

        return temp

    @number_of_torque_inputs.setter
    def number_of_torque_inputs(self, value: 'int'):
        self.wrapped.NumberOfTorqueInputs = int(value) if value is not None else 0

    @property
    def specify_load_case_names(self) -> 'bool':
        """bool: 'SpecifyLoadCaseNames' is the original name of this property."""

        temp = self.wrapped.SpecifyLoadCaseNames

        if temp is None:
            return False

        return temp

    @specify_load_case_names.setter
    def specify_load_case_names(self, value: 'bool'):
        self.wrapped.SpecifyLoadCaseNames = bool(value) if value is not None else False

    @property
    def speed_chart(self) -> '_1854.TwoDChartDefinition':
        """TwoDChartDefinition: 'SpeedChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpeedChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def torque_chart(self) -> '_1854.TwoDChartDefinition':
        """TwoDChartDefinition: 'TorqueChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_state_options(self) -> '_6958.DesignStateOptions':
        """DesignStateOptions: 'DesignStateOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DesignStateOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_ratio_options(self) -> '_6961.GearRatioInputOptions':
        """GearRatioInputOptions: 'GearRatioOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearRatioOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def load_case_name_inputs(self) -> '_6962.LoadCaseNameOptions':
        """LoadCaseNameOptions: 'LoadCaseNameInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCaseNameInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def time_step_input(self) -> '_6970.TimeStepInputOptions':
        """TimeStepInputOptions: 'TimeStepInput' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeStepInput

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def boost_pressure_inputs(self) -> 'List[_6957.BoostPressureLoadCaseInputOptions]':
        """List[BoostPressureLoadCaseInputOptions]: 'BoostPressureInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoostPressureInputs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def file_inputs(self) -> 'List[_6964.MultiTimeSeriesDataInputFileOptions]':
        """List[MultiTimeSeriesDataInputFileOptions]: 'FileInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FileInputs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def force_inputs(self) -> 'List[_6960.ForceInputOptions]':
        """List[ForceInputOptions]: 'ForceInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceInputs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def moment_inputs(self) -> 'List[_6963.MomentInputOptions]':
        """List[MomentInputOptions]: 'MomentInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MomentInputs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def speed_inputs(self) -> 'List[_6968.SpeedInputOptions]':
        """List[SpeedInputOptions]: 'SpeedInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpeedInputs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def torque_inputs(self) -> 'List[_6971.TorqueInputOptions]':
        """List[TorqueInputOptions]: 'TorqueInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueInputs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def columns(self) -> 'List[_1806.ColumnTitle]':
        """List[ColumnTitle]: 'Columns' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Columns

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def create_load_cases(self):
        """ 'CreateLoadCases' is the original name of this method."""

        self.wrapped.CreateLoadCases()

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result

    @property
    def cast_to(self) -> 'TimeSeriesImporter._Cast_TimeSeriesImporter':
        return self._Cast_TimeSeriesImporter(self)
