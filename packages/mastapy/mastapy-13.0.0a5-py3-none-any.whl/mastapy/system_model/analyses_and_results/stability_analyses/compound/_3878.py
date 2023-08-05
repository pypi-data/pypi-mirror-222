"""_3878.py

AbstractShaftCompoundStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3879
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'AbstractShaftCompoundStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3747


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftCompoundStabilityAnalysis',)


class AbstractShaftCompoundStabilityAnalysis(_3879.AbstractShaftOrHousingCompoundStabilityAnalysis):
    """AbstractShaftCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_STABILITY_ANALYSIS

    class _Cast_AbstractShaftCompoundStabilityAnalysis:
        """Special nested class for casting AbstractShaftCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractShaftCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_stability_analysis(self):
            return self._parent._cast(_3879.AbstractShaftOrHousingCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3902
            
            return self._parent._cast(_3902.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3956
            
            return self._parent._cast(_3956.PartCompoundStabilityAnalysis)

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
        def cycloidal_disc_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3922
            
            return self._parent._cast(_3922.CycloidalDiscCompoundStabilityAnalysis)

        @property
        def shaft_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3972
            
            return self._parent._cast(_3972.ShaftCompoundStabilityAnalysis)

        @property
        def abstract_shaft_compound_stability_analysis(self) -> 'AbstractShaftCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3747.AbstractShaftStabilityAnalysis]':
        """List[AbstractShaftStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3747.AbstractShaftStabilityAnalysis]':
        """List[AbstractShaftStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis':
        return self._Cast_AbstractShaftCompoundStabilityAnalysis(self)
