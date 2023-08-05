"""_4526.py

StraightBevelDiffGearCompoundParametricStudyTool
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4437
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'StraightBevelDiffGearCompoundParametricStudyTool')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4398


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearCompoundParametricStudyTool',)


class StraightBevelDiffGearCompoundParametricStudyTool(_4437.BevelGearCompoundParametricStudyTool):
    """StraightBevelDiffGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_StraightBevelDiffGearCompoundParametricStudyTool:
        """Special nested class for casting StraightBevelDiffGearCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'StraightBevelDiffGearCompoundParametricStudyTool'):
            self._parent = parent

        @property
        def bevel_gear_compound_parametric_study_tool(self):
            return self._parent._cast(_4437.BevelGearCompoundParametricStudyTool)

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4425
            
            return self._parent._cast(_4425.AGMAGleasonConicalGearCompoundParametricStudyTool)

        @property
        def conical_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4453
            
            return self._parent._cast(_4453.ConicalGearCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4479
            
            return self._parent._cast(_4479.GearCompoundParametricStudyTool)

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
        def straight_bevel_planet_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4532
            
            return self._parent._cast(_4532.StraightBevelPlanetGearCompoundParametricStudyTool)

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4533
            
            return self._parent._cast(_4533.StraightBevelSunGearCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(self) -> 'StraightBevelDiffGearCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2527.StraightBevelDiffGear':
        """StraightBevelDiffGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4398.StraightBevelDiffGearParametricStudyTool]':
        """List[StraightBevelDiffGearParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4398.StraightBevelDiffGearParametricStudyTool]':
        """List[StraightBevelDiffGearParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelDiffGearCompoundParametricStudyTool._Cast_StraightBevelDiffGearCompoundParametricStudyTool':
        return self._Cast_StraightBevelDiffGearCompoundParametricStudyTool(self)
