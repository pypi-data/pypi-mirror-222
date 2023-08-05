"""_2987.py

ClutchHalfSteadyStateSynchronousResponse
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3003
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'ClutchHalfSteadyStateSynchronousResponse')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2561
    from mastapy.system_model.analyses_and_results.static_loads import _6801


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchHalfSteadyStateSynchronousResponse',)


class ClutchHalfSteadyStateSynchronousResponse(_3003.CouplingHalfSteadyStateSynchronousResponse):
    """ClutchHalfSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_ClutchHalfSteadyStateSynchronousResponse:
        """Special nested class for casting ClutchHalfSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'ClutchHalfSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def coupling_half_steady_state_synchronous_response(self):
            return self._parent._cast(_3003.CouplingHalfSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3043
            
            return self._parent._cast(_3043.MountableComponentSteadyStateSynchronousResponse)

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
        def clutch_half_steady_state_synchronous_response(self) -> 'ClutchHalfSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ClutchHalfSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2561.ClutchHalf':
        """ClutchHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6801.ClutchHalfLoadCase':
        """ClutchHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ClutchHalfSteadyStateSynchronousResponse._Cast_ClutchHalfSteadyStateSynchronousResponse':
        return self._Cast_ClutchHalfSteadyStateSynchronousResponse(self)
