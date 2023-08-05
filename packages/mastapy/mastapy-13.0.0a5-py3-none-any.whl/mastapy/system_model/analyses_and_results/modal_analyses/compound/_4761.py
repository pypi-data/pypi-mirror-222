"""_4761.py

FlexiblePinAssemblyCompoundModalAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4802
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'FlexiblePinAssemblyCompoundModalAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2437
    from mastapy.system_model.analyses_and_results.modal_analyses import _4610


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAssemblyCompoundModalAnalysis',)


class FlexiblePinAssemblyCompoundModalAnalysis(_4802.SpecialisedAssemblyCompoundModalAnalysis):
    """FlexiblePinAssemblyCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_COMPOUND_MODAL_ANALYSIS

    class _Cast_FlexiblePinAssemblyCompoundModalAnalysis:
        """Special nested class for casting FlexiblePinAssemblyCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'FlexiblePinAssemblyCompoundModalAnalysis'):
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
        def flexible_pin_assembly_compound_modal_analysis(self) -> 'FlexiblePinAssemblyCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FlexiblePinAssemblyCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2437.FlexiblePinAssembly':
        """FlexiblePinAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2437.FlexiblePinAssembly':
        """FlexiblePinAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4610.FlexiblePinAssemblyModalAnalysis]':
        """List[FlexiblePinAssemblyModalAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4610.FlexiblePinAssemblyModalAnalysis]':
        """List[FlexiblePinAssemblyModalAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FlexiblePinAssemblyCompoundModalAnalysis._Cast_FlexiblePinAssemblyCompoundModalAnalysis':
        return self._Cast_FlexiblePinAssemblyCompoundModalAnalysis(self)
