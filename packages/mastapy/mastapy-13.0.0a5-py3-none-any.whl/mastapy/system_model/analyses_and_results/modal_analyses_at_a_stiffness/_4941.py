"""_4941.py

StraightBevelDiffGearSetModalAnalysisAtAStiffness
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4851
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'StraightBevelDiffGearSetModalAnalysisAtAStiffness')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2528
    from mastapy.system_model.analyses_and_results.static_loads import _6929
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4940, _4939


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetModalAnalysisAtAStiffness',)


class StraightBevelDiffGearSetModalAnalysisAtAStiffness(_4851.BevelGearSetModalAnalysisAtAStiffness):
    """StraightBevelDiffGearSetModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_StraightBevelDiffGearSetModalAnalysisAtAStiffness:
        """Special nested class for casting StraightBevelDiffGearSetModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'StraightBevelDiffGearSetModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def bevel_gear_set_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4851.BevelGearSetModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4839
            
            return self._parent._cast(_4839.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness)

        @property
        def conical_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4867
            
            return self._parent._cast(_4867.ConicalGearSetModalAnalysisAtAStiffness)

        @property
        def gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4894
            
            return self._parent._cast(_4894.GearSetModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4932
            
            return self._parent._cast(_4932.SpecialisedAssemblyModalAnalysisAtAStiffness)

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4833
            
            return self._parent._cast(_4833.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4913
            
            return self._parent._cast(_4913.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7514
            
            return self._parent._cast(_7514.PartStaticLoadAnalysisCase)

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
        def straight_bevel_diff_gear_set_modal_analysis_at_a_stiffness(self) -> 'StraightBevelDiffGearSetModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2528.StraightBevelDiffGearSet':
        """StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6929.StraightBevelDiffGearSetLoadCase':
        """StraightBevelDiffGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def straight_bevel_diff_gears_modal_analysis_at_a_stiffness(self) -> 'List[_4940.StraightBevelDiffGearModalAnalysisAtAStiffness]':
        """List[StraightBevelDiffGearModalAnalysisAtAStiffness]: 'StraightBevelDiffGearsModalAnalysisAtAStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearsModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_meshes_modal_analysis_at_a_stiffness(self) -> 'List[_4939.StraightBevelDiffGearMeshModalAnalysisAtAStiffness]':
        """List[StraightBevelDiffGearMeshModalAnalysisAtAStiffness]: 'StraightBevelDiffMeshesModalAnalysisAtAStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffMeshesModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelDiffGearSetModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearSetModalAnalysisAtAStiffness':
        return self._Cast_StraightBevelDiffGearSetModalAnalysisAtAStiffness(self)
