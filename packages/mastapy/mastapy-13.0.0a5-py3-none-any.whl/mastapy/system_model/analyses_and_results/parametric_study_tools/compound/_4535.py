"""_4535.py

SynchroniserHalfCompoundParametricStudyTool
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4536
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'SynchroniserHalfCompoundParametricStudyTool')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2586
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4405


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserHalfCompoundParametricStudyTool',)


class SynchroniserHalfCompoundParametricStudyTool(_4536.SynchroniserPartCompoundParametricStudyTool):
    """SynchroniserHalfCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_SynchroniserHalfCompoundParametricStudyTool:
        """Special nested class for casting SynchroniserHalfCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'SynchroniserHalfCompoundParametricStudyTool'):
            self._parent = parent

        @property
        def synchroniser_part_compound_parametric_study_tool(self):
            return self._parent._cast(_4536.SynchroniserPartCompoundParametricStudyTool)

        @property
        def coupling_half_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4460
            
            return self._parent._cast(_4460.CouplingHalfCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4498
            
            return self._parent._cast(_4498.MountableComponentCompoundParametricStudyTool)

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
        def synchroniser_half_compound_parametric_study_tool(self) -> 'SynchroniserHalfCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SynchroniserHalfCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2586.SynchroniserHalf':
        """SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4405.SynchroniserHalfParametricStudyTool]':
        """List[SynchroniserHalfParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4405.SynchroniserHalfParametricStudyTool]':
        """List[SynchroniserHalfParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SynchroniserHalfCompoundParametricStudyTool._Cast_SynchroniserHalfCompoundParametricStudyTool':
        return self._Cast_SynchroniserHalfCompoundParametricStudyTool(self)
