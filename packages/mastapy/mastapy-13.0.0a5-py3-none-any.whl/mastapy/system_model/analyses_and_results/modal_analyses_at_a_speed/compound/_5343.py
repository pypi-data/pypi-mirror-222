"""_5343.py

VirtualComponentCompoundModalAnalysisAtASpeed
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5298
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'VirtualComponentCompoundModalAnalysisAtASpeed')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5214


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualComponentCompoundModalAnalysisAtASpeed',)


class VirtualComponentCompoundModalAnalysisAtASpeed(_5298.MountableComponentCompoundModalAnalysisAtASpeed):
    """VirtualComponentCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_VirtualComponentCompoundModalAnalysisAtASpeed:
        """Special nested class for casting VirtualComponentCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'VirtualComponentCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(self):
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
        def mass_disc_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5296
            
            return self._parent._cast(_5296.MassDiscCompoundModalAnalysisAtASpeed)

        @property
        def measurement_component_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5297
            
            return self._parent._cast(_5297.MeasurementComponentCompoundModalAnalysisAtASpeed)

        @property
        def point_load_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5307
            
            return self._parent._cast(_5307.PointLoadCompoundModalAnalysisAtASpeed)

        @property
        def power_load_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5308
            
            return self._parent._cast(_5308.PowerLoadCompoundModalAnalysisAtASpeed)

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5342
            
            return self._parent._cast(_5342.UnbalancedMassCompoundModalAnalysisAtASpeed)

        @property
        def virtual_component_compound_modal_analysis_at_a_speed(self) -> 'VirtualComponentCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VirtualComponentCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_5214.VirtualComponentModalAnalysisAtASpeed]':
        """List[VirtualComponentModalAnalysisAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_5214.VirtualComponentModalAnalysisAtASpeed]':
        """List[VirtualComponentModalAnalysisAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'VirtualComponentCompoundModalAnalysisAtASpeed._Cast_VirtualComponentCompoundModalAnalysisAtASpeed':
        return self._Cast_VirtualComponentCompoundModalAnalysisAtASpeed(self)
