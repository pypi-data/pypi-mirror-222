"""_5334.py

SynchroniserCompoundModalAnalysisAtASpeed
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5319
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'SynchroniserCompoundModalAnalysisAtASpeed')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2584
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5206


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserCompoundModalAnalysisAtASpeed',)


class SynchroniserCompoundModalAnalysisAtASpeed(_5319.SpecialisedAssemblyCompoundModalAnalysisAtASpeed):
    """SynchroniserCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_SynchroniserCompoundModalAnalysisAtASpeed:
        """Special nested class for casting SynchroniserCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'SynchroniserCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5319.SpecialisedAssemblyCompoundModalAnalysisAtASpeed)

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
        def synchroniser_compound_modal_analysis_at_a_speed(self) -> 'SynchroniserCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SynchroniserCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2584.Synchroniser':
        """Synchroniser: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2584.Synchroniser':
        """Synchroniser: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5206.SynchroniserModalAnalysisAtASpeed]':
        """List[SynchroniserModalAnalysisAtASpeed]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5206.SynchroniserModalAnalysisAtASpeed]':
        """List[SynchroniserModalAnalysisAtASpeed]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SynchroniserCompoundModalAnalysisAtASpeed._Cast_SynchroniserCompoundModalAnalysisAtASpeed':
        return self._Cast_SynchroniserCompoundModalAnalysisAtASpeed(self)
