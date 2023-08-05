"""_3136.py

CouplingConnectionCompoundSteadyStateSynchronousResponse
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3163
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'CouplingConnectionCompoundSteadyStateSynchronousResponse')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3002


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionCompoundSteadyStateSynchronousResponse',)


class CouplingConnectionCompoundSteadyStateSynchronousResponse(_3163.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse):
    """CouplingConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_CouplingConnectionCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting CouplingConnectionCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'CouplingConnectionCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(self):
            return self._parent._cast(_3163.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3133
            
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
        def clutch_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3120
            
            return self._parent._cast(_3120.ClutchConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def concept_coupling_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3125
            
            return self._parent._cast(_3125.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3179
            
            return self._parent._cast(_3179.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def spring_damper_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3201
            
            return self._parent._cast(_3201.SpringDamperConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def torque_converter_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3216
            
            return self._parent._cast(_3216.TorqueConverterConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def coupling_connection_compound_steady_state_synchronous_response(self) -> 'CouplingConnectionCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_3002.CouplingConnectionSteadyStateSynchronousResponse]':
        """List[CouplingConnectionSteadyStateSynchronousResponse]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3002.CouplingConnectionSteadyStateSynchronousResponse]':
        """List[CouplingConnectionSteadyStateSynchronousResponse]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponse':
        return self._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponse(self)
