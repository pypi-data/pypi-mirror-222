"""_4795.py

RollingRingAssemblyCompoundModalAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4802
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'RollingRingAssemblyCompoundModalAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2579
    from mastapy.system_model.analyses_and_results.modal_analyses import _4650


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingAssemblyCompoundModalAnalysis',)


class RollingRingAssemblyCompoundModalAnalysis(_4802.SpecialisedAssemblyCompoundModalAnalysis):
    """RollingRingAssemblyCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_COMPOUND_MODAL_ANALYSIS

    class _Cast_RollingRingAssemblyCompoundModalAnalysis:
        """Special nested class for casting RollingRingAssemblyCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'RollingRingAssemblyCompoundModalAnalysis'):
            self._parent = parent

        @property
        def specialised_assembly_compound_modal_analysis(self):
            return self._parent._cast(_4802.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4704
            
            return self._parent._cast(_4704.AbstractAssemblyCompoundModalAnalysis)

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
        def rolling_ring_assembly_compound_modal_analysis(self) -> 'RollingRingAssemblyCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollingRingAssemblyCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2579.RollingRingAssembly':
        """RollingRingAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2579.RollingRingAssembly':
        """RollingRingAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4650.RollingRingAssemblyModalAnalysis]':
        """List[RollingRingAssemblyModalAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4650.RollingRingAssemblyModalAnalysis]':
        """List[RollingRingAssemblyModalAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RollingRingAssemblyCompoundModalAnalysis._Cast_RollingRingAssemblyCompoundModalAnalysis':
        return self._Cast_RollingRingAssemblyCompoundModalAnalysis(self)
