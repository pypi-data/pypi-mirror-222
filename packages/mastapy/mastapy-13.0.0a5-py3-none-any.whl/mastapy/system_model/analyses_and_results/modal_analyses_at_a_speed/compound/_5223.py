"""_5223.py

AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5246
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'AbstractShaftOrHousingCompoundModalAnalysisAtASpeed')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5094


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftOrHousingCompoundModalAnalysisAtASpeed',)


class AbstractShaftOrHousingCompoundModalAnalysisAtASpeed(_5246.ComponentCompoundModalAnalysisAtASpeed):
    """AbstractShaftOrHousingCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed:
        """Special nested class for casting AbstractShaftOrHousingCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'AbstractShaftOrHousingCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def component_compound_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5246.ComponentCompoundModalAnalysisAtASpeed)

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
        def abstract_shaft_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5222
            
            return self._parent._cast(_5222.AbstractShaftCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5266
            
            return self._parent._cast(_5266.CycloidalDiscCompoundModalAnalysisAtASpeed)

        @property
        def fe_part_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5277
            
            return self._parent._cast(_5277.FEPartCompoundModalAnalysisAtASpeed)

        @property
        def shaft_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5316
            
            return self._parent._cast(_5316.ShaftCompoundModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_speed(self) -> 'AbstractShaftOrHousingCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftOrHousingCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_5094.AbstractShaftOrHousingModalAnalysisAtASpeed]':
        """List[AbstractShaftOrHousingModalAnalysisAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_5094.AbstractShaftOrHousingModalAnalysisAtASpeed]':
        """List[AbstractShaftOrHousingModalAnalysisAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed':
        return self._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed(self)
