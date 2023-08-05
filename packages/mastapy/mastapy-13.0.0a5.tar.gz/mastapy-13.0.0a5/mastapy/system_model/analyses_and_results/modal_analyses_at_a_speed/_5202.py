﻿"""_5202.py

StraightBevelGearSetModalAnalysisAtASpeed
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5110
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'StraightBevelGearSetModalAnalysisAtASpeed')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2530
    from mastapy.system_model.analyses_and_results.static_loads import _6932
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5201, _5200


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetModalAnalysisAtASpeed',)


class StraightBevelGearSetModalAnalysisAtASpeed(_5110.BevelGearSetModalAnalysisAtASpeed):
    """StraightBevelGearSetModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_StraightBevelGearSetModalAnalysisAtASpeed:
        """Special nested class for casting StraightBevelGearSetModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'StraightBevelGearSetModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def bevel_gear_set_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5110.BevelGearSetModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5098
            
            return self._parent._cast(_5098.AGMAGleasonConicalGearSetModalAnalysisAtASpeed)

        @property
        def conical_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5126
            
            return self._parent._cast(_5126.ConicalGearSetModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5152
            
            return self._parent._cast(_5152.GearSetModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5190
            
            return self._parent._cast(_5190.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5092
            
            return self._parent._cast(_5092.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5171
            
            return self._parent._cast(_5171.PartModalAnalysisAtASpeed)

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
        def straight_bevel_gear_set_modal_analysis_at_a_speed(self) -> 'StraightBevelGearSetModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2530.StraightBevelGearSet':
        """StraightBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6932.StraightBevelGearSetLoadCase':
        """StraightBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def straight_bevel_gears_modal_analysis_at_a_speed(self) -> 'List[_5201.StraightBevelGearModalAnalysisAtASpeed]':
        """List[StraightBevelGearModalAnalysisAtASpeed]: 'StraightBevelGearsModalAnalysisAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearsModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_meshes_modal_analysis_at_a_speed(self) -> 'List[_5200.StraightBevelGearMeshModalAnalysisAtASpeed]':
        """List[StraightBevelGearMeshModalAnalysisAtASpeed]: 'StraightBevelMeshesModalAnalysisAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelMeshesModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelGearSetModalAnalysisAtASpeed._Cast_StraightBevelGearSetModalAnalysisAtASpeed':
        return self._Cast_StraightBevelGearSetModalAnalysisAtASpeed(self)
