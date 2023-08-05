"""_3489.py

AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3521
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2248


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed',)


class AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed(_3521.ConnectionSteadyStateSynchronousResponseAtASpeed):
    """AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def connection_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3521.ConnectionSteadyStateSynchronousResponseAtASpeed)

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
        def coaxial_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3510
            
            return self._parent._cast(_3510.CoaxialConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3530
            
            return self._parent._cast(_3530.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3531
            
            return self._parent._cast(_3531.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def planetary_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3569
            
            return self._parent._cast(_3569.PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3583
            
            return self._parent._cast(_3583.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(self) -> 'AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed.TYPE'):
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
    def cast_to(self) -> 'AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed(self)
