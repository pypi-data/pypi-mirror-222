﻿"""_4875.py

CVTPulleyModalAnalysisAtAStiffness
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4922
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'CVTPulleyModalAnalysisAtAStiffness')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2569


__docformat__ = 'restructuredtext en'
__all__ = ('CVTPulleyModalAnalysisAtAStiffness',)


class CVTPulleyModalAnalysisAtAStiffness(_4922.PulleyModalAnalysisAtAStiffness):
    """CVTPulleyModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_CVTPulleyModalAnalysisAtAStiffness:
        """Special nested class for casting CVTPulleyModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'CVTPulleyModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def pulley_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4922.PulleyModalAnalysisAtAStiffness)

        @property
        def coupling_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4871
            
            return self._parent._cast(_4871.CouplingHalfModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4911
            
            return self._parent._cast(_4911.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4858
            
            return self._parent._cast(_4858.ComponentModalAnalysisAtAStiffness)

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
        def cvt_pulley_modal_analysis_at_a_stiffness(self) -> 'CVTPulleyModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTPulleyModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2569.CVTPulley':
        """CVTPulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness':
        return self._Cast_CVTPulleyModalAnalysisAtAStiffness(self)
