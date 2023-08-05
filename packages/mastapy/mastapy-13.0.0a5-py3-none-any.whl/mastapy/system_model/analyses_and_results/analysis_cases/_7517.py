"""_7517.py

TimeSeriesLoadAnalysisCase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7501
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TIME_SERIES_LOAD_ANALYSIS_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases', 'TimeSeriesLoadAnalysisCase')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6773


__docformat__ = 'restructuredtext en'
__all__ = ('TimeSeriesLoadAnalysisCase',)


class TimeSeriesLoadAnalysisCase(_7501.AnalysisCase):
    """TimeSeriesLoadAnalysisCase

    This is a mastapy class.
    """

    TYPE = _TIME_SERIES_LOAD_ANALYSIS_CASE

    class _Cast_TimeSeriesLoadAnalysisCase:
        """Special nested class for casting TimeSeriesLoadAnalysisCase to subclasses."""

        def __init__(self, parent: 'TimeSeriesLoadAnalysisCase'):
            self._parent = parent

        @property
        def analysis_case(self):
            return self._parent._cast(_7501.AnalysisCase)

        @property
        def context(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.Context)

        @property
        def multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _2621
            
            return self._parent._cast(_2621.MultibodyDynamicsAnalysis)

        @property
        def time_series_load_analysis_case(self) -> 'TimeSeriesLoadAnalysisCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TimeSeriesLoadAnalysisCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_case(self) -> '_6773.TimeSeriesLoadCase':
        """TimeSeriesLoadCase: 'LoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'TimeSeriesLoadAnalysisCase._Cast_TimeSeriesLoadAnalysisCase':
        return self._Cast_TimeSeriesLoadAnalysisCase(self)
