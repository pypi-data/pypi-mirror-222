"""_4790.py

PointLoadCompoundModalAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4826
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'PointLoadCompoundModalAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.modal_analyses import _4645


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoadCompoundModalAnalysis',)


class PointLoadCompoundModalAnalysis(_4826.VirtualComponentCompoundModalAnalysis):
    """PointLoadCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_COMPOUND_MODAL_ANALYSIS

    class _Cast_PointLoadCompoundModalAnalysis:
        """Special nested class for casting PointLoadCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'PointLoadCompoundModalAnalysis'):
            self._parent = parent

        @property
        def virtual_component_compound_modal_analysis(self):
            return self._parent._cast(_4826.VirtualComponentCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4781
            
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
        def point_load_compound_modal_analysis(self) -> 'PointLoadCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PointLoadCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2454.PointLoad':
        """PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4645.PointLoadModalAnalysis]':
        """List[PointLoadModalAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4645.PointLoadModalAnalysis]':
        """List[PointLoadModalAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PointLoadCompoundModalAnalysis._Cast_PointLoadCompoundModalAnalysis':
        return self._Cast_PointLoadCompoundModalAnalysis(self)
