"""_5293.py

KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5287
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2522
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5165


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed',)


class KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed(_5287.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed):
    """KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5287.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5253
            
            return self._parent._cast(_5253.ConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5279
            
            return self._parent._cast(_5279.GearCompoundModalAnalysisAtASpeed)

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5298
            
            return self._parent._cast(_5298.MountableComponentCompoundModalAnalysisAtASpeed)

        @property
        def component_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5246
            
            return self._parent._cast(_5246.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5300
            
            return self._parent._cast(_5300.PartCompoundModalAnalysisAtASpeed)

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
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_speed(self) -> 'KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2522.KlingelnbergCycloPalloidSpiralBevelGear':
        """KlingelnbergCycloPalloidSpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5165.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5165.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed':
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed(self)
