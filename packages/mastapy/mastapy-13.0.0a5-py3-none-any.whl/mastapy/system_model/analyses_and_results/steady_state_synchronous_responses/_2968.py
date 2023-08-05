"""_2968.py

AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3000
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2248


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse',)


class AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse(_3000.ConnectionSteadyStateSynchronousResponse):
    """AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def connection_steady_state_synchronous_response(self):
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
        def coaxial_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2989
            
            return self._parent._cast(_2989.CoaxialConnectionSteadyStateSynchronousResponse)

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3009
            
            return self._parent._cast(_3009.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse)

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3010
            
            return self._parent._cast(_3010.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse)

        @property
        def planetary_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3049
            
            return self._parent._cast(_3049.PlanetaryConnectionSteadyStateSynchronousResponse)

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3063
            
            return self._parent._cast(_3063.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse)

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response(self) -> 'AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2248.AbstractShaftToMountableComponentConnection':
        """AbstractShaftToMountableComponentConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse':
        return self._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse(self)
