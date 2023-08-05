"""_4423.py

AbstractShaftOrHousingCompoundParametricStudyTool
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4446
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'AbstractShaftOrHousingCompoundParametricStudyTool')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4275


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftOrHousingCompoundParametricStudyTool',)


class AbstractShaftOrHousingCompoundParametricStudyTool(_4446.ComponentCompoundParametricStudyTool):
    """AbstractShaftOrHousingCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_AbstractShaftOrHousingCompoundParametricStudyTool:
        """Special nested class for casting AbstractShaftOrHousingCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'AbstractShaftOrHousingCompoundParametricStudyTool'):
            self._parent = parent

        @property
        def component_compound_parametric_study_tool(self):
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
        def abstract_shaft_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4422
            
            return self._parent._cast(_4422.AbstractShaftCompoundParametricStudyTool)

        @property
        def cycloidal_disc_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4466
            
            return self._parent._cast(_4466.CycloidalDiscCompoundParametricStudyTool)

        @property
        def fe_part_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4477
            
            return self._parent._cast(_4477.FEPartCompoundParametricStudyTool)

        @property
        def shaft_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4516
            
            return self._parent._cast(_4516.ShaftCompoundParametricStudyTool)

        @property
        def abstract_shaft_or_housing_compound_parametric_study_tool(self) -> 'AbstractShaftOrHousingCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftOrHousingCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4275.AbstractShaftOrHousingParametricStudyTool]':
        """List[AbstractShaftOrHousingParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4275.AbstractShaftOrHousingParametricStudyTool]':
        """List[AbstractShaftOrHousingParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool':
        return self._Cast_AbstractShaftOrHousingCompoundParametricStudyTool(self)
