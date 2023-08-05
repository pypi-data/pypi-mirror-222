"""_5346.py

WormGearSetCompoundModalAnalysisAtASpeed
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5281
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'WormGearSetCompoundModalAnalysisAtASpeed')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5217
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5344, _5345


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetCompoundModalAnalysisAtASpeed',)


class WormGearSetCompoundModalAnalysisAtASpeed(_5281.GearSetCompoundModalAnalysisAtASpeed):
    """WormGearSetCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_WormGearSetCompoundModalAnalysisAtASpeed:
        """Special nested class for casting WormGearSetCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'WormGearSetCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def gear_set_compound_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5281.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5319
            
            return self._parent._cast(_5319.SpecialisedAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5221
            
            return self._parent._cast(_5221.AbstractAssemblyCompoundModalAnalysisAtASpeed)

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
        def worm_gear_set_compound_modal_analysis_at_a_speed(self) -> 'WormGearSetCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGearSetCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2534.WormGearSet':
        """WormGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2534.WormGearSet':
        """WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5217.WormGearSetModalAnalysisAtASpeed]':
        """List[WormGearSetModalAnalysisAtASpeed]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gears_compound_modal_analysis_at_a_speed(self) -> 'List[_5344.WormGearCompoundModalAnalysisAtASpeed]':
        """List[WormGearCompoundModalAnalysisAtASpeed]: 'WormGearsCompoundModalAnalysisAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearsCompoundModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_meshes_compound_modal_analysis_at_a_speed(self) -> 'List[_5345.WormGearMeshCompoundModalAnalysisAtASpeed]':
        """List[WormGearMeshCompoundModalAnalysisAtASpeed]: 'WormMeshesCompoundModalAnalysisAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormMeshesCompoundModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5217.WormGearSetModalAnalysisAtASpeed]':
        """List[WormGearSetModalAnalysisAtASpeed]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'WormGearSetCompoundModalAnalysisAtASpeed._Cast_WormGearSetCompoundModalAnalysisAtASpeed':
        return self._Cast_WormGearSetCompoundModalAnalysisAtASpeed(self)
