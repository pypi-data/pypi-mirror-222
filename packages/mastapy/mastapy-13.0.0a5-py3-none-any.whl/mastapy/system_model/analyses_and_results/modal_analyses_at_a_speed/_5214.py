"""_5214.py

VirtualComponentModalAnalysisAtASpeed
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5169
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'VirtualComponentModalAnalysisAtASpeed')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualComponentModalAnalysisAtASpeed',)


class VirtualComponentModalAnalysisAtASpeed(_5169.MountableComponentModalAnalysisAtASpeed):
    """VirtualComponentModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_VirtualComponentModalAnalysisAtASpeed:
        """Special nested class for casting VirtualComponentModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'VirtualComponentModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def mountable_component_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5169.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5117
            
            return self._parent._cast(_5117.ComponentModalAnalysisAtASpeed)

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
        def mass_disc_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5167
            
            return self._parent._cast(_5167.MassDiscModalAnalysisAtASpeed)

        @property
        def measurement_component_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5168
            
            return self._parent._cast(_5168.MeasurementComponentModalAnalysisAtASpeed)

        @property
        def point_load_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5178
            
            return self._parent._cast(_5178.PointLoadModalAnalysisAtASpeed)

        @property
        def power_load_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5179
            
            return self._parent._cast(_5179.PowerLoadModalAnalysisAtASpeed)

        @property
        def unbalanced_mass_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5213
            
            return self._parent._cast(_5213.UnbalancedMassModalAnalysisAtASpeed)

        @property
        def virtual_component_modal_analysis_at_a_speed(self) -> 'VirtualComponentModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VirtualComponentModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2462.VirtualComponent':
        """VirtualComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed':
        return self._Cast_VirtualComponentModalAnalysisAtASpeed(self)
