"""_1935.py

LoadedBearingDutyCycle
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_BEARING_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Bearings.BearingResults', 'LoadedBearingDutyCycle')

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs import _2117
    from mastapy.utility.property import _1827
    from mastapy.bearings import _1862
    from mastapy.bearings.bearing_results import _1936


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedBearingDutyCycle',)


class LoadedBearingDutyCycle(_0.APIBase):
    """LoadedBearingDutyCycle

    This is a mastapy class.
    """

    TYPE = _LOADED_BEARING_DUTY_CYCLE

    class _Cast_LoadedBearingDutyCycle:
        """Special nested class for casting LoadedBearingDutyCycle to subclasses."""

        def __init__(self, parent: 'LoadedBearingDutyCycle'):
            self._parent = parent

        @property
        def loaded_non_linear_bearing_duty_cycle_results(self):
            from mastapy.bearings.bearing_results import _1943
            
            return self._parent._cast(_1943.LoadedNonLinearBearingDutyCycleResults)

        @property
        def loaded_rolling_bearing_duty_cycle(self):
            from mastapy.bearings.bearing_results import _1946
            
            return self._parent._cast(_1946.LoadedRollingBearingDutyCycle)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_duty_cycle(self):
            from mastapy.bearings.bearing_results.rolling import _1979
            
            return self._parent._cast(_1979.LoadedAxialThrustCylindricalRollerBearingDutyCycle)

        @property
        def loaded_ball_bearing_duty_cycle(self):
            from mastapy.bearings.bearing_results.rolling import _1986
            
            return self._parent._cast(_1986.LoadedBallBearingDutyCycle)

        @property
        def loaded_cylindrical_roller_bearing_duty_cycle(self):
            from mastapy.bearings.bearing_results.rolling import _1994
            
            return self._parent._cast(_1994.LoadedCylindricalRollerBearingDutyCycle)

        @property
        def loaded_non_barrel_roller_bearing_duty_cycle(self):
            from mastapy.bearings.bearing_results.rolling import _2010
            
            return self._parent._cast(_2010.LoadedNonBarrelRollerBearingDutyCycle)

        @property
        def loaded_taper_roller_bearing_duty_cycle(self):
            from mastapy.bearings.bearing_results.rolling import _2033
            
            return self._parent._cast(_2033.LoadedTaperRollerBearingDutyCycle)

        @property
        def loaded_bearing_duty_cycle(self) -> 'LoadedBearingDutyCycle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedBearingDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duration(self) -> 'float':
        """float: 'Duration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Duration

        if temp is None:
            return 0.0

        return temp

    @property
    def duty_cycle_name(self) -> 'str':
        """str: 'DutyCycleName' is the original name of this property."""

        temp = self.wrapped.DutyCycleName

        if temp is None:
            return ''

        return temp

    @duty_cycle_name.setter
    def duty_cycle_name(self, value: 'str'):
        self.wrapped.DutyCycleName = str(value) if value is not None else ''

    @property
    def bearing_design(self) -> '_2117.BearingDesign':
        """BearingDesign: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def radial_load_summary(self) -> '_1827.DutyCyclePropertySummaryForce[_1862.BearingLoadCaseResultsLightweight]':
        """DutyCyclePropertySummaryForce[BearingLoadCaseResultsLightweight]: 'RadialLoadSummary' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadialLoadSummary

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1862.BearingLoadCaseResultsLightweight](temp) if temp is not None else None

    @property
    def z_thrust_reaction_summary(self) -> '_1827.DutyCyclePropertySummaryForce[_1862.BearingLoadCaseResultsLightweight]':
        """DutyCyclePropertySummaryForce[BearingLoadCaseResultsLightweight]: 'ZThrustReactionSummary' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZThrustReactionSummary

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1862.BearingLoadCaseResultsLightweight](temp) if temp is not None else None

    @property
    def bearing_load_case_results(self) -> 'List[_1936.LoadedBearingResults]':
        """List[LoadedBearingResults]: 'BearingLoadCaseResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingLoadCaseResults

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
    def cast_to(self) -> 'LoadedBearingDutyCycle._Cast_LoadedBearingDutyCycle':
        return self._Cast_LoadedBearingDutyCycle(self)
