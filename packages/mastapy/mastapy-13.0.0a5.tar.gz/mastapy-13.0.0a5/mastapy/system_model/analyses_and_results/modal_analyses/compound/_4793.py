﻿"""_4793.py

RingPinsCompoundModalAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4781
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'RingPinsCompoundModalAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2552
    from mastapy.system_model.analyses_and_results.modal_analyses import _4648


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsCompoundModalAnalysis',)


class RingPinsCompoundModalAnalysis(_4781.MountableComponentCompoundModalAnalysis):
    """RingPinsCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _RING_PINS_COMPOUND_MODAL_ANALYSIS

    class _Cast_RingPinsCompoundModalAnalysis:
        """Special nested class for casting RingPinsCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'RingPinsCompoundModalAnalysis'):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis(self):
            return self._parent._cast(_4781.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4729
            
            return self._parent._cast(_4729.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4783
            
            return self._parent._cast(_4783.PartCompoundModalAnalysis)

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
        def ring_pins_compound_modal_analysis(self) -> 'RingPinsCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RingPinsCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2552.RingPins':
        """RingPins: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4648.RingPinsModalAnalysis]':
        """List[RingPinsModalAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4648.RingPinsModalAnalysis]':
        """List[RingPinsModalAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RingPinsCompoundModalAnalysis._Cast_RingPinsCompoundModalAnalysis':
        return self._Cast_RingPinsCompoundModalAnalysis(self)
