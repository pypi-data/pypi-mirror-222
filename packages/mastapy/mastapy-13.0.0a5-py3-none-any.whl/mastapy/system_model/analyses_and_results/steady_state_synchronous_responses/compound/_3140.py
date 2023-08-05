"""_3140.py

CVTPulleyCompoundSteadyStateSynchronousResponse
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3186
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'CVTPulleyCompoundSteadyStateSynchronousResponse')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3006


__docformat__ = 'restructuredtext en'
__all__ = ('CVTPulleyCompoundSteadyStateSynchronousResponse',)


class CVTPulleyCompoundSteadyStateSynchronousResponse(_3186.PulleyCompoundSteadyStateSynchronousResponse):
    """CVTPulleyCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_CVTPulleyCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting CVTPulleyCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'CVTPulleyCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def pulley_compound_steady_state_synchronous_response(self):
            return self._parent._cast(_3186.PulleyCompoundSteadyStateSynchronousResponse)

        @property
        def coupling_half_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3137
            
            return self._parent._cast(_3137.CouplingHalfCompoundSteadyStateSynchronousResponse)

        @property
        def mountable_component_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3175
            
            return self._parent._cast(_3175.MountableComponentCompoundSteadyStateSynchronousResponse)

        @property
        def component_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3123
            
            return self._parent._cast(_3123.ComponentCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3177
            
            return self._parent._cast(_3177.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7512
            
            return self._parent._cast(_7512.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_steady_state_synchronous_response(self) -> 'CVTPulleyCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTPulleyCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(self) -> 'List[_3006.CVTPulleySteadyStateSynchronousResponse]':
        """List[CVTPulleySteadyStateSynchronousResponse]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3006.CVTPulleySteadyStateSynchronousResponse]':
        """List[CVTPulleySteadyStateSynchronousResponse]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CVTPulleyCompoundSteadyStateSynchronousResponse._Cast_CVTPulleyCompoundSteadyStateSynchronousResponse':
        return self._Cast_CVTPulleyCompoundSteadyStateSynchronousResponse(self)
