"""_5315.py

RootAssemblyCompoundModalAnalysisAtASpeed
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5228
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'RootAssemblyCompoundModalAnalysisAtASpeed')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5186


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyCompoundModalAnalysisAtASpeed',)


class RootAssemblyCompoundModalAnalysisAtASpeed(_5228.AssemblyCompoundModalAnalysisAtASpeed):
    """RootAssemblyCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_RootAssemblyCompoundModalAnalysisAtASpeed:
        """Special nested class for casting RootAssemblyCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'RootAssemblyCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def assembly_compound_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5228.AssemblyCompoundModalAnalysisAtASpeed)

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5221
            
            return self._parent._cast(_5221.AbstractAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5300
            
            return self._parent._cast(_5300.PartCompoundModalAnalysisAtASpeed)

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
        def root_assembly_compound_modal_analysis_at_a_speed(self) -> 'RootAssemblyCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RootAssemblyCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5186.RootAssemblyModalAnalysisAtASpeed]':
        """List[RootAssemblyModalAnalysisAtASpeed]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5186.RootAssemblyModalAnalysisAtASpeed]':
        """List[RootAssemblyModalAnalysisAtASpeed]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RootAssemblyCompoundModalAnalysisAtASpeed._Cast_RootAssemblyCompoundModalAnalysisAtASpeed':
        return self._Cast_RootAssemblyCompoundModalAnalysisAtASpeed(self)
