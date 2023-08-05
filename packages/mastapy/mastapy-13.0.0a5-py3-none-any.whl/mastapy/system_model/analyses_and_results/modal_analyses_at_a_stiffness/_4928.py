"""_4928.py

RootAssemblyModalAnalysisAtAStiffness
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4840
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'RootAssemblyModalAnalysisAtAStiffness')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2457
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _2619


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyModalAnalysisAtAStiffness',)


class RootAssemblyModalAnalysisAtAStiffness(_4840.AssemblyModalAnalysisAtAStiffness):
    """RootAssemblyModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_RootAssemblyModalAnalysisAtAStiffness:
        """Special nested class for casting RootAssemblyModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'RootAssemblyModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def assembly_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4840.AssemblyModalAnalysisAtAStiffness)

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
        def root_assembly_modal_analysis_at_a_stiffness(self) -> 'RootAssemblyModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RootAssemblyModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2457.RootAssembly':
        """RootAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def modal_analysis_at_a_stiffness_inputs(self) -> '_2619.ModalAnalysisAtAStiffness':
        """ModalAnalysisAtAStiffness: 'ModalAnalysisAtAStiffnessInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModalAnalysisAtAStiffnessInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'RootAssemblyModalAnalysisAtAStiffness._Cast_RootAssemblyModalAnalysisAtAStiffness':
        return self._Cast_RootAssemblyModalAnalysisAtAStiffness(self)
