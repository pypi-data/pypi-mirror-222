"""_7072.py

RootAssemblyAdvancedTimeSteppingAnalysisForModulation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6983
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'RootAssemblyAdvancedTimeSteppingAnalysisForModulation')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _2605
    from mastapy.system_model.part_model import _2457
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5846
    from mastapy.system_model.analyses_and_results.system_deflections import _2782


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyAdvancedTimeSteppingAnalysisForModulation',)


class RootAssemblyAdvancedTimeSteppingAnalysisForModulation(_6983.AssemblyAdvancedTimeSteppingAnalysisForModulation):
    """RootAssemblyAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_RootAssemblyAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting RootAssemblyAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'RootAssemblyAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def assembly_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_6983.AssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6973
            
            return self._parent._cast(_6973.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7057
            
            return self._parent._cast(_7057.PartAdvancedTimeSteppingAnalysisForModulation)

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
        def root_assembly_advanced_time_stepping_analysis_for_modulation(self) -> 'RootAssemblyAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RootAssemblyAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def advanced_time_stepping_analysis_for_modulation_inputs(self) -> '_2605.AdvancedTimeSteppingAnalysisForModulation':
        """AdvancedTimeSteppingAnalysisForModulation: 'AdvancedTimeSteppingAnalysisForModulationInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdvancedTimeSteppingAnalysisForModulationInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def results(self) -> '_5846.RootAssemblyHarmonicAnalysisResultsPropertyAccessor':
        """RootAssemblyHarmonicAnalysisResultsPropertyAccessor: 'Results' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Results

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2782.RootAssemblySystemDeflection':
        """RootAssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'RootAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_RootAssemblyAdvancedTimeSteppingAnalysisForModulation(self)
