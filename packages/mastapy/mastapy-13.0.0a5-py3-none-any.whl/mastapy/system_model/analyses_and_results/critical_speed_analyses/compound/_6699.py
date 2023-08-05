"""_6699.py

FlexiblePinAssemblyCompoundCriticalSpeedAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6740
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'FlexiblePinAssemblyCompoundCriticalSpeedAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2437
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6570


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAssemblyCompoundCriticalSpeedAnalysis',)


class FlexiblePinAssemblyCompoundCriticalSpeedAnalysis(_6740.SpecialisedAssemblyCompoundCriticalSpeedAnalysis):
    """FlexiblePinAssemblyCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_FlexiblePinAssemblyCompoundCriticalSpeedAnalysis:
        """Special nested class for casting FlexiblePinAssemblyCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'FlexiblePinAssemblyCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def specialised_assembly_compound_critical_speed_analysis(self):
            return self._parent._cast(_6740.SpecialisedAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def abstract_assembly_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6642
            
            return self._parent._cast(_6642.AbstractAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6721
            
            return self._parent._cast(_6721.PartCompoundCriticalSpeedAnalysis)

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
        def flexible_pin_assembly_compound_critical_speed_analysis(self) -> 'FlexiblePinAssemblyCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FlexiblePinAssemblyCompoundCriticalSpeedAnalysis.TYPE'):
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
    def assembly_analysis_cases_ready(self) -> 'List[_6570.FlexiblePinAssemblyCriticalSpeedAnalysis]':
        """List[FlexiblePinAssemblyCriticalSpeedAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6570.FlexiblePinAssemblyCriticalSpeedAnalysis]':
        """List[FlexiblePinAssemblyCriticalSpeedAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FlexiblePinAssemblyCompoundCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCompoundCriticalSpeedAnalysis':
        return self._Cast_FlexiblePinAssemblyCompoundCriticalSpeedAnalysis(self)
