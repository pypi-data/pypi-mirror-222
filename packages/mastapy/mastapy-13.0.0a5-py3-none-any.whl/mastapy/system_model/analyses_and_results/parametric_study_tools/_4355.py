"""_4355.py

KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4349
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2523
    from mastapy.system_model.analyses_and_results.static_loads import _6888
    from mastapy.system_model.analyses_and_results.system_deflections import _2757
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4354, _4353


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool',)


class KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool(_4349.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool):
    """KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_PARAMETRIC_STUDY_TOOL

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_parametric_study_tool(self):
            return self._parent._cast(_4349.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool)

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
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_parametric_study_tool(self) -> 'KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2523.KlingelnbergCycloPalloidSpiralBevelGearSet':
        """KlingelnbergCycloPalloidSpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6888.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase':
        """KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2757.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_parametric_study_tool(self) -> 'List[_4354.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool]: 'KlingelnbergCycloPalloidSpiralBevelGearsParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_parametric_study_tool(self) -> 'List[_4353.KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool]: 'KlingelnbergCycloPalloidSpiralBevelMeshesParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool':
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool(self)
