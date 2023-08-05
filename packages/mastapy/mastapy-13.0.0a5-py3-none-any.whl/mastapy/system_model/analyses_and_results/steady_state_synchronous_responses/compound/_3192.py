"""_3192.py

RootAssemblyCompoundSteadyStateSynchronousResponse
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3105
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'RootAssemblyCompoundSteadyStateSynchronousResponse')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3060


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyCompoundSteadyStateSynchronousResponse',)


class RootAssemblyCompoundSteadyStateSynchronousResponse(_3105.AssemblyCompoundSteadyStateSynchronousResponse):
    """RootAssemblyCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_RootAssemblyCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting RootAssemblyCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'RootAssemblyCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def assembly_compound_steady_state_synchronous_response(self):
            return self._parent._cast(_3105.AssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3098
            
            return self._parent._cast(_3098.AbstractAssemblyCompoundSteadyStateSynchronousResponse)

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
        def root_assembly_compound_steady_state_synchronous_response(self) -> 'RootAssemblyCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RootAssemblyCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3060.RootAssemblySteadyStateSynchronousResponse]':
        """List[RootAssemblySteadyStateSynchronousResponse]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3060.RootAssemblySteadyStateSynchronousResponse]':
        """List[RootAssemblySteadyStateSynchronousResponse]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RootAssemblyCompoundSteadyStateSynchronousResponse._Cast_RootAssemblyCompoundSteadyStateSynchronousResponse':
        return self._Cast_RootAssemblyCompoundSteadyStateSynchronousResponse(self)
