"""_4403.py

StraightBevelPlanetGearParametricStudyTool
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4398
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'StraightBevelPlanetGearParametricStudyTool')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2531


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelPlanetGearParametricStudyTool',)


class StraightBevelPlanetGearParametricStudyTool(_4398.StraightBevelDiffGearParametricStudyTool):
    """StraightBevelPlanetGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_PARAMETRIC_STUDY_TOOL

    class _Cast_StraightBevelPlanetGearParametricStudyTool:
        """Special nested class for casting StraightBevelPlanetGearParametricStudyTool to subclasses."""

        def __init__(self, parent: 'StraightBevelPlanetGearParametricStudyTool'):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_parametric_study_tool(self):
            return self._parent._cast(_4398.StraightBevelDiffGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4291
            
            return self._parent._cast(_4291.BevelGearParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4279
            
            return self._parent._cast(_4279.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4307
            
            return self._parent._cast(_4307.ConicalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4340
            
            return self._parent._cast(_4340.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4359
            
            return self._parent._cast(_4359.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4299
            
            return self._parent._cast(_4299.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4371
            
            return self._parent._cast(_4371.PartParametricStudyTool)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7511
            
            return self._parent._cast(_7511.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2639
            
            return self._parent._cast(_2639.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2635
            
            return self._parent._cast(_2635.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(self) -> 'StraightBevelPlanetGearParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelPlanetGearParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2531.StraightBevelPlanetGear':
        """StraightBevelPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool':
        return self._Cast_StraightBevelPlanetGearParametricStudyTool(self)
