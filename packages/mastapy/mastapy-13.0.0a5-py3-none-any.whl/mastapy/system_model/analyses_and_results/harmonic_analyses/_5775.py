"""_5775.py

RootAssemblyHarmonicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5659
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'RootAssemblyHarmonicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2457
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5737, _2614
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5846
    from mastapy.system_model.analyses_and_results.system_deflections import _2782


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyHarmonicAnalysis',)


class RootAssemblyHarmonicAnalysis(_5659.AssemblyHarmonicAnalysis):
    """RootAssemblyHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_HARMONIC_ANALYSIS

    class _Cast_RootAssemblyHarmonicAnalysis:
        """Special nested class for casting RootAssemblyHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'RootAssemblyHarmonicAnalysis'):
            self._parent = parent

        @property
        def assembly_harmonic_analysis(self):
            return self._parent._cast(_5659.AssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5651
            
            return self._parent._cast(_5651.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5758
            
            return self._parent._cast(_5758.PartHarmonicAnalysis)

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
        def root_assembly_harmonic_analysis(self) -> 'RootAssemblyHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RootAssemblyHarmonicAnalysis.TYPE'):
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
    def export(self) -> '_5737.HarmonicAnalysisRootAssemblyExportOptions':
        """HarmonicAnalysisRootAssemblyExportOptions: 'Export' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Export

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def harmonic_analysis_inputs(self) -> '_2614.HarmonicAnalysis':
        """HarmonicAnalysis: 'HarmonicAnalysisInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicAnalysisInputs

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
    def cast_to(self) -> 'RootAssemblyHarmonicAnalysis._Cast_RootAssemblyHarmonicAnalysis':
        return self._Cast_RootAssemblyHarmonicAnalysis(self)
