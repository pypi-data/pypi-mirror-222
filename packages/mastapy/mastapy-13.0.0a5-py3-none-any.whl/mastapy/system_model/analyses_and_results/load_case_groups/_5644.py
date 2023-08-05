﻿"""_5644.py

TimeSeriesLoadCaseGroup
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.load_case_groups import _5632
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TIME_SERIES_LOAD_CASE_GROUP = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups', 'TimeSeriesLoadCaseGroup')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6773, _6785
    from mastapy.system_model.analyses_and_results import _2657, _2601


__docformat__ = 'restructuredtext en'
__all__ = ('TimeSeriesLoadCaseGroup',)


class TimeSeriesLoadCaseGroup(_5632.AbstractLoadCaseGroup):
    """TimeSeriesLoadCaseGroup

    This is a mastapy class.
    """

    TYPE = _TIME_SERIES_LOAD_CASE_GROUP

    class _Cast_TimeSeriesLoadCaseGroup:
        """Special nested class for casting TimeSeriesLoadCaseGroup to subclasses."""

        def __init__(self, parent: 'TimeSeriesLoadCaseGroup'):
            self._parent = parent

        @property
        def abstract_load_case_group(self):
            return self._parent._cast(_5632.AbstractLoadCaseGroup)

        @property
        def time_series_load_case_group(self) -> 'TimeSeriesLoadCaseGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TimeSeriesLoadCaseGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_cases(self) -> 'List[_6773.TimeSeriesLoadCase]':
        """List[TimeSeriesLoadCase]: 'LoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def compound_multibody_dynamics_analysis(self) -> '_2657.CompoundMultibodyDynamicsAnalysis':
        """CompoundMultibodyDynamicsAnalysis: 'CompoundMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundMultibodyDynamicsAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def delete(self):
        """ 'Delete' is the original name of this method."""

        self.wrapped.Delete()

    def analysis_of(self, analysis_type: '_6785.AnalysisType') -> '_2601.CompoundAnalysis':
        """ 'AnalysisOf' is the original name of this method.

        Args:
            analysis_type (mastapy.system_model.analyses_and_results.static_loads.AnalysisType)

        Returns:
            mastapy.system_model.analyses_and_results.CompoundAnalysis
        """

        analysis_type = conversion.mp_to_pn_enum(analysis_type, 'SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.AnalysisType')
        method_result = self.wrapped.AnalysisOf(analysis_type)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'TimeSeriesLoadCaseGroup._Cast_TimeSeriesLoadCaseGroup':
        return self._Cast_TimeSeriesLoadCaseGroup(self)
