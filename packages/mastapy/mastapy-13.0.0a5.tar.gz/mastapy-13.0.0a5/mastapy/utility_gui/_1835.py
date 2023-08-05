﻿"""_1835.py

ColumnInputOptions
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COLUMN_INPUT_OPTIONS = python_net_import('SMT.MastaAPI.UtilityGUI', 'ColumnInputOptions')

if TYPE_CHECKING:
    from mastapy.utility.file_access_helpers import _1806
    from mastapy.utility.units_and_measurements import _1601


__docformat__ = 'restructuredtext en'
__all__ = ('ColumnInputOptions',)


class ColumnInputOptions(_0.APIBase):
    """ColumnInputOptions

    This is a mastapy class.
    """

    TYPE = _COLUMN_INPUT_OPTIONS

    class _Cast_ColumnInputOptions:
        """Special nested class for casting ColumnInputOptions to subclasses."""

        def __init__(self, parent: 'ColumnInputOptions'):
            self._parent = parent

        @property
        def boost_pressure_input_options(self):
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2537
            
            return self._parent._cast(_2537.BoostPressureInputOptions)

        @property
        def input_power_input_options(self):
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2538
            
            return self._parent._cast(_2538.InputPowerInputOptions)

        @property
        def pressure_ratio_input_options(self):
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2539
            
            return self._parent._cast(_2539.PressureRatioInputOptions)

        @property
        def rotor_speed_input_options(self):
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2542
            
            return self._parent._cast(_2542.RotorSpeedInputOptions)

        @property
        def boost_pressure_load_case_input_options(self):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6957
            
            return self._parent._cast(_6957.BoostPressureLoadCaseInputOptions)

        @property
        def design_state_options(self):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6958
            
            return self._parent._cast(_6958.DesignStateOptions)

        @property
        def force_input_options(self):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6960
            
            return self._parent._cast(_6960.ForceInputOptions)

        @property
        def gear_ratio_input_options(self):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6961
            
            return self._parent._cast(_6961.GearRatioInputOptions)

        @property
        def load_case_name_options(self):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6962
            
            return self._parent._cast(_6962.LoadCaseNameOptions)

        @property
        def moment_input_options(self):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6963
            
            return self._parent._cast(_6963.MomentInputOptions)

        @property
        def point_load_input_options(self):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6965
            
            return self._parent._cast(_6965.PointLoadInputOptions)

        @property
        def power_load_input_options(self):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6966
            
            return self._parent._cast(_6966.PowerLoadInputOptions)

        @property
        def ramp_or_steady_state_input_options(self):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6967
            
            return self._parent._cast(_6967.RampOrSteadyStateInputOptions)

        @property
        def speed_input_options(self):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6968
            
            return self._parent._cast(_6968.SpeedInputOptions)

        @property
        def time_step_input_options(self):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6970
            
            return self._parent._cast(_6970.TimeStepInputOptions)

        @property
        def torque_input_options(self):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6971
            
            return self._parent._cast(_6971.TorqueInputOptions)

        @property
        def column_input_options(self) -> 'ColumnInputOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ColumnInputOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def column(self) -> 'list_with_selected_item.ListWithSelectedItem_ColumnTitle':
        """list_with_selected_item.ListWithSelectedItem_ColumnTitle: 'Column' is the original name of this property."""

        temp = self.wrapped.Column

        if temp is None:
            return None

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_ColumnTitle')(temp) if temp is not None else None

    @column.setter
    def column(self, value: 'list_with_selected_item.ListWithSelectedItem_ColumnTitle.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_ColumnTitle.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_ColumnTitle.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.Column = value

    @property
    def unit(self) -> 'list_with_selected_item.ListWithSelectedItem_Unit':
        """list_with_selected_item.ListWithSelectedItem_Unit: 'Unit' is the original name of this property."""

        temp = self.wrapped.Unit

        if temp is None:
            return None

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_Unit')(temp) if temp is not None else None

    @unit.setter
    def unit(self, value: 'list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.Unit = value

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
    def cast_to(self) -> 'ColumnInputOptions._Cast_ColumnInputOptions':
        return self._Cast_ColumnInputOptions(self)
