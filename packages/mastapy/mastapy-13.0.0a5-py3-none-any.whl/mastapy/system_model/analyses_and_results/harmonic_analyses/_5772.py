"""_5772.py

RollingRingAssemblyHarmonicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5780
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'RollingRingAssemblyHarmonicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2579
    from mastapy.system_model.analyses_and_results.static_loads import _6913
    from mastapy.system_model.analyses_and_results.system_deflections import _2779


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingAssemblyHarmonicAnalysis',)


class RollingRingAssemblyHarmonicAnalysis(_5780.SpecialisedAssemblyHarmonicAnalysis):
    """RollingRingAssemblyHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_HARMONIC_ANALYSIS

    class _Cast_RollingRingAssemblyHarmonicAnalysis:
        """Special nested class for casting RollingRingAssemblyHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'RollingRingAssemblyHarmonicAnalysis'):
            self._parent = parent

        @property
        def specialised_assembly_harmonic_analysis(self):
            return self._parent._cast(_5780.SpecialisedAssemblyHarmonicAnalysis)

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
        def rolling_ring_assembly_harmonic_analysis(self) -> 'RollingRingAssemblyHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollingRingAssemblyHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def assembly_load_case(self) -> '_6913.RollingRingAssemblyLoadCase':
        """RollingRingAssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2779.RollingRingAssemblySystemDeflection':
        """RollingRingAssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis':
        return self._Cast_RollingRingAssemblyHarmonicAnalysis(self)
