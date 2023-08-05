"""_3101.py

AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3133
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2968


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse',)


class AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse(_3133.ConnectionCompoundSteadyStateSynchronousResponse):
    """AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def connection_compound_steady_state_synchronous_response(self):
            return self._parent._cast(_3133.ConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3122
            
            return self._parent._cast(_3122.CoaxialConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3142
            
            return self._parent._cast(_3142.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3144
            
            return self._parent._cast(_3144.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def planetary_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3181
            
            return self._parent._cast(_3181.PlanetaryConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3195
            
            return self._parent._cast(_3195.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(self) -> 'AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_2968.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse]':
        """List[AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_2968.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse]':
        """List[AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse':
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse(self)
