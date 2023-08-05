"""_3017.py

DynamicModelForSteadyStateSynchronousResponse
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.analyses_and_results.dynamic_analyses import _2608
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_MODEL_FOR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'DynamicModelForSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicModelForSteadyStateSynchronousResponse',)


class DynamicModelForSteadyStateSynchronousResponse(_2608.DynamicAnalysis):
    """DynamicModelForSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_MODEL_FOR_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_DynamicModelForSteadyStateSynchronousResponse:
        """Special nested class for casting DynamicModelForSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'DynamicModelForSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def dynamic_analysis(self):
            return self._parent._cast(_2608.DynamicAnalysis)

        @property
        def fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
            return self._parent._cast(_7510.FEAnalysis)

        @property
        def static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7516
            
            return self._parent._cast(_7516.StaticLoadAnalysisCase)

        @property
        def analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7501
            
            return self._parent._cast(_7501.AnalysisCase)

        @property
        def context(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.Context)

        @property
        def dynamic_model_for_steady_state_synchronous_response(self) -> 'DynamicModelForSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DynamicModelForSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'DynamicModelForSteadyStateSynchronousResponse._Cast_DynamicModelForSteadyStateSynchronousResponse':
        return self._Cast_DynamicModelForSteadyStateSynchronousResponse(self)
