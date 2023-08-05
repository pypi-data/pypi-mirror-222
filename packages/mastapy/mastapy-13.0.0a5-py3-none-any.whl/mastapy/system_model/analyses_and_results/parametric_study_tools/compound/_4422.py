"""_4422.py

AbstractShaftCompoundParametricStudyTool
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4423
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'AbstractShaftCompoundParametricStudyTool')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4276


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftCompoundParametricStudyTool',)


class AbstractShaftCompoundParametricStudyTool(_4423.AbstractShaftOrHousingCompoundParametricStudyTool):
    """AbstractShaftCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_AbstractShaftCompoundParametricStudyTool:
        """Special nested class for casting AbstractShaftCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'AbstractShaftCompoundParametricStudyTool'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_parametric_study_tool(self):
            return self._parent._cast(_4423.AbstractShaftOrHousingCompoundParametricStudyTool)

        @property
        def component_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4446
            
            return self._parent._cast(_4446.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4500
            
            return self._parent._cast(_4500.PartCompoundParametricStudyTool)

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
        def cycloidal_disc_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4466
            
            return self._parent._cast(_4466.CycloidalDiscCompoundParametricStudyTool)

        @property
        def shaft_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4516
            
            return self._parent._cast(_4516.ShaftCompoundParametricStudyTool)

        @property
        def abstract_shaft_compound_parametric_study_tool(self) -> 'AbstractShaftCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4276.AbstractShaftParametricStudyTool]':
        """List[AbstractShaftParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4276.AbstractShaftParametricStudyTool]':
        """List[AbstractShaftParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftCompoundParametricStudyTool._Cast_AbstractShaftCompoundParametricStudyTool':
        return self._Cast_AbstractShaftCompoundParametricStudyTool(self)
