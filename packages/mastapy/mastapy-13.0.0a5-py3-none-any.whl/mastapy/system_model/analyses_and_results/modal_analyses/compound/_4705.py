"""_4705.py

AbstractShaftCompoundModalAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4706
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'AbstractShaftCompoundModalAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4551


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftCompoundModalAnalysis',)


class AbstractShaftCompoundModalAnalysis(_4706.AbstractShaftOrHousingCompoundModalAnalysis):
    """AbstractShaftCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_MODAL_ANALYSIS

    class _Cast_AbstractShaftCompoundModalAnalysis:
        """Special nested class for casting AbstractShaftCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractShaftCompoundModalAnalysis'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_modal_analysis(self):
            return self._parent._cast(_4706.AbstractShaftOrHousingCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4729
            
            return self._parent._cast(_4729.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4783
            
            return self._parent._cast(_4783.PartCompoundModalAnalysis)

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
        def cycloidal_disc_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4749
            
            return self._parent._cast(_4749.CycloidalDiscCompoundModalAnalysis)

        @property
        def shaft_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4799
            
            return self._parent._cast(_4799.ShaftCompoundModalAnalysis)

        @property
        def abstract_shaft_compound_modal_analysis(self) -> 'AbstractShaftCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4551.AbstractShaftModalAnalysis]':
        """List[AbstractShaftModalAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4551.AbstractShaftModalAnalysis]':
        """List[AbstractShaftModalAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis':
        return self._Cast_AbstractShaftCompoundModalAnalysis(self)
