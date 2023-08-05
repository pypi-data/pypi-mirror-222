"""_4471.py

CylindricalPlanetGearCompoundParametricStudyTool
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4468
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'CylindricalPlanetGearCompoundParametricStudyTool')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4324


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalPlanetGearCompoundParametricStudyTool',)


class CylindricalPlanetGearCompoundParametricStudyTool(_4468.CylindricalGearCompoundParametricStudyTool):
    """CylindricalPlanetGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_CylindricalPlanetGearCompoundParametricStudyTool:
        """Special nested class for casting CylindricalPlanetGearCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'CylindricalPlanetGearCompoundParametricStudyTool'):
            self._parent = parent

        @property
        def cylindrical_gear_compound_parametric_study_tool(self):
            return self._parent._cast(_4468.CylindricalGearCompoundParametricStudyTool)

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
        def cylindrical_planet_gear_compound_parametric_study_tool(self) -> 'CylindricalPlanetGearCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalPlanetGearCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(self) -> 'List[_4324.CylindricalPlanetGearParametricStudyTool]':
        """List[CylindricalPlanetGearParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4324.CylindricalPlanetGearParametricStudyTool]':
        """List[CylindricalPlanetGearParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool':
        return self._Cast_CylindricalPlanetGearCompoundParametricStudyTool(self)
