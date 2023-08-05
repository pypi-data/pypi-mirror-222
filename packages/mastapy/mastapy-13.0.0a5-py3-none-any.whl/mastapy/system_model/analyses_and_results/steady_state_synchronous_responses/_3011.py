"""_3011.py

CycloidalDiscSteadyStateSynchronousResponse
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2967
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'CycloidalDiscSteadyStateSynchronousResponse')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2551
    from mastapy.system_model.analyses_and_results.static_loads import _6827


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscSteadyStateSynchronousResponse',)


class CycloidalDiscSteadyStateSynchronousResponse(_2967.AbstractShaftSteadyStateSynchronousResponse):
    """CycloidalDiscSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_CycloidalDiscSteadyStateSynchronousResponse:
        """Special nested class for casting CycloidalDiscSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'CycloidalDiscSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def abstract_shaft_steady_state_synchronous_response(self):
            return self._parent._cast(_2967.AbstractShaftSteadyStateSynchronousResponse)

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2966
            
            return self._parent._cast(_2966.AbstractShaftOrHousingSteadyStateSynchronousResponse)

        @property
        def component_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2990
            
            return self._parent._cast(_2990.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3045
            
            return self._parent._cast(_3045.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7514
            
            return self._parent._cast(_7514.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7511
            
            return self._parent._cast(_7511.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2639
            
            return self._parent._cast(_2639.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2635
            
            return self._parent._cast(_2635.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def cycloidal_disc_steady_state_synchronous_response(self) -> 'CycloidalDiscSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2551.CycloidalDisc':
        """CycloidalDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6827.CycloidalDiscLoadCase':
        """CycloidalDiscLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse':
        return self._Cast_CycloidalDiscSteadyStateSynchronousResponse(self)
