"""_3068.py

SpringDamperConnectionSteadyStateSynchronousResponse
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3002
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'SpringDamperConnectionSteadyStateSynchronousResponse')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2333
    from mastapy.system_model.analyses_and_results.static_loads import _6924


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperConnectionSteadyStateSynchronousResponse',)


class SpringDamperConnectionSteadyStateSynchronousResponse(_3002.CouplingConnectionSteadyStateSynchronousResponse):
    """SpringDamperConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_SpringDamperConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting SpringDamperConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'SpringDamperConnectionSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def coupling_connection_steady_state_synchronous_response(self):
            return self._parent._cast(_3002.CouplingConnectionSteadyStateSynchronousResponse)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3031
            
            return self._parent._cast(_3031.InterMountableComponentConnectionSteadyStateSynchronousResponse)

        @property
        def connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3000
            
            return self._parent._cast(_3000.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7504
            
            return self._parent._cast(_7504.ConnectionAnalysisCase)

        @property
        def connection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2631
            
            return self._parent._cast(_2631.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2635
            
            return self._parent._cast(_2635.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def spring_damper_connection_steady_state_synchronous_response(self) -> 'SpringDamperConnectionSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpringDamperConnectionSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2333.SpringDamperConnection':
        """SpringDamperConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6924.SpringDamperConnectionLoadCase':
        """SpringDamperConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SpringDamperConnectionSteadyStateSynchronousResponse._Cast_SpringDamperConnectionSteadyStateSynchronousResponse':
        return self._Cast_SpringDamperConnectionSteadyStateSynchronousResponse(self)
