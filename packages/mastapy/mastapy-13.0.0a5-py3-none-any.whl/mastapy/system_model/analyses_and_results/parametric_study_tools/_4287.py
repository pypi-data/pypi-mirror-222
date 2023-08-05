"""_4287.py

BevelDifferentialGearSetParametricStudyTool
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4292
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'BevelDifferentialGearSetParametricStudyTool')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2498
    from mastapy.system_model.analyses_and_results.static_loads import _6792
    from mastapy.system_model.analyses_and_results.system_deflections import _2684
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4286, _4285


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetParametricStudyTool',)


class BevelDifferentialGearSetParametricStudyTool(_4292.BevelGearSetParametricStudyTool):
    """BevelDifferentialGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_PARAMETRIC_STUDY_TOOL

    class _Cast_BevelDifferentialGearSetParametricStudyTool:
        """Special nested class for casting BevelDifferentialGearSetParametricStudyTool to subclasses."""

        def __init__(self, parent: 'BevelDifferentialGearSetParametricStudyTool'):
            self._parent = parent

        @property
        def bevel_gear_set_parametric_study_tool(self):
            return self._parent._cast(_4292.BevelGearSetParametricStudyTool)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4280
            
            return self._parent._cast(_4280.AGMAGleasonConicalGearSetParametricStudyTool)

        @property
        def conical_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4308
            
            return self._parent._cast(_4308.ConicalGearSetParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4341
            
            return self._parent._cast(_4341.GearSetParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4390
            
            return self._parent._cast(_4390.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4274
            
            return self._parent._cast(_4274.AbstractAssemblyParametricStudyTool)

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
        def bevel_differential_gear_set_parametric_study_tool(self) -> 'BevelDifferentialGearSetParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2498.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6792.BevelDifferentialGearSetLoadCase':
        """BevelDifferentialGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2684.BevelDifferentialGearSetSystemDeflection]':
        """List[BevelDifferentialGearSetSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_gears_parametric_study_tool(self) -> 'List[_4286.BevelDifferentialGearParametricStudyTool]':
        """List[BevelDifferentialGearParametricStudyTool]: 'BevelDifferentialGearsParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearsParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_meshes_parametric_study_tool(self) -> 'List[_4285.BevelDifferentialGearMeshParametricStudyTool]':
        """List[BevelDifferentialGearMeshParametricStudyTool]: 'BevelDifferentialMeshesParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialMeshesParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool':
        return self._Cast_BevelDifferentialGearSetParametricStudyTool(self)
