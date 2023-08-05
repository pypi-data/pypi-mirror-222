"""_5144.py

ExternalCADModelModalAnalysisAtASpeed
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5117
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'ExternalCADModelModalAnalysisAtASpeed')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2435
    from mastapy.system_model.analyses_and_results.static_loads import _6851


__docformat__ = 'restructuredtext en'
__all__ = ('ExternalCADModelModalAnalysisAtASpeed',)


class ExternalCADModelModalAnalysisAtASpeed(_5117.ComponentModalAnalysisAtASpeed):
    """ExternalCADModelModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_ExternalCADModelModalAnalysisAtASpeed:
        """Special nested class for casting ExternalCADModelModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'ExternalCADModelModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def component_modal_analysis_at_a_speed(self):
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
        def external_cad_model_modal_analysis_at_a_speed(self) -> 'ExternalCADModelModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ExternalCADModelModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2435.ExternalCADModel':
        """ExternalCADModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6851.ExternalCADModelLoadCase':
        """ExternalCADModelLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ExternalCADModelModalAnalysisAtASpeed._Cast_ExternalCADModelModalAnalysisAtASpeed':
        return self._Cast_ExternalCADModelModalAnalysisAtASpeed(self)
