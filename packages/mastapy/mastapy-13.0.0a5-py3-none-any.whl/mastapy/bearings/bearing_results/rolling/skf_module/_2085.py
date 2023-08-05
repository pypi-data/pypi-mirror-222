"""_2085.py

SKFModuleResults
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SKF_MODULE_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'SKFModuleResults')

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling.skf_module import (
        _2063, _2065, _2066, _2067,
        _2068, _2070, _2074, _2078,
        _2086, _2087
    )


__docformat__ = 'restructuredtext en'
__all__ = ('SKFModuleResults',)


class SKFModuleResults(_0.APIBase):
    """SKFModuleResults

    This is a mastapy class.
    """

    TYPE = _SKF_MODULE_RESULTS

    class _Cast_SKFModuleResults:
        """Special nested class for casting SKFModuleResults to subclasses."""

        def __init__(self, parent: 'SKFModuleResults'):
            self._parent = parent

        @property
        def skf_module_results(self) -> 'SKFModuleResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SKFModuleResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def adjusted_speed(self) -> '_2063.AdjustedSpeed':
        """AdjustedSpeed: 'AdjustedSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdjustedSpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_loads(self) -> '_2065.BearingLoads':
        """BearingLoads: 'BearingLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingLoads

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_rating_life(self) -> '_2066.BearingRatingLife':
        """BearingRatingLife: 'BearingRatingLife' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingRatingLife

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def dynamic_axial_load_carrying_capacity(self) -> '_2067.DynamicAxialLoadCarryingCapacity':
        """DynamicAxialLoadCarryingCapacity: 'DynamicAxialLoadCarryingCapacity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicAxialLoadCarryingCapacity

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def frequencies(self) -> '_2068.Frequencies':
        """Frequencies: 'Frequencies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Frequencies

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def friction(self) -> '_2070.Friction':
        """Friction: 'Friction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Friction

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def grease_life_and_relubrication_interval(self) -> '_2074.GreaseLifeAndRelubricationInterval':
        """GreaseLifeAndRelubricationInterval: 'GreaseLifeAndRelubricationInterval' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GreaseLifeAndRelubricationInterval

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def minimum_load(self) -> '_2078.MinimumLoad':
        """MinimumLoad: 'MinimumLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumLoad

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def static_safety_factors(self) -> '_2086.StaticSafetyFactors':
        """StaticSafetyFactors: 'StaticSafetyFactors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticSafetyFactors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def viscosities(self) -> '_2087.Viscosities':
        """Viscosities: 'Viscosities' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Viscosities

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def cast_to(self) -> 'SKFModuleResults._Cast_SKFModuleResults':
        return self._Cast_SKFModuleResults(self)
