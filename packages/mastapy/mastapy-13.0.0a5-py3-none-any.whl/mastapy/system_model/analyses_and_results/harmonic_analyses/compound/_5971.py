"""_5971.py

VirtualComponentCompoundHarmonicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5926
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'VirtualComponentCompoundHarmonicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5807


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualComponentCompoundHarmonicAnalysis',)


class VirtualComponentCompoundHarmonicAnalysis(_5926.MountableComponentCompoundHarmonicAnalysis):
    """VirtualComponentCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_VirtualComponentCompoundHarmonicAnalysis:
        """Special nested class for casting VirtualComponentCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'VirtualComponentCompoundHarmonicAnalysis'):
            self._parent = parent

        @property
        def mountable_component_compound_harmonic_analysis(self):
            return self._parent._cast(_5926.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5874
            
            return self._parent._cast(_5874.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5928
            
            return self._parent._cast(_5928.PartCompoundHarmonicAnalysis)

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
        def mass_disc_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5924
            
            return self._parent._cast(_5924.MassDiscCompoundHarmonicAnalysis)

        @property
        def measurement_component_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5925
            
            return self._parent._cast(_5925.MeasurementComponentCompoundHarmonicAnalysis)

        @property
        def point_load_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5935
            
            return self._parent._cast(_5935.PointLoadCompoundHarmonicAnalysis)

        @property
        def power_load_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5936
            
            return self._parent._cast(_5936.PowerLoadCompoundHarmonicAnalysis)

        @property
        def unbalanced_mass_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5970
            
            return self._parent._cast(_5970.UnbalancedMassCompoundHarmonicAnalysis)

        @property
        def virtual_component_compound_harmonic_analysis(self) -> 'VirtualComponentCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VirtualComponentCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_5807.VirtualComponentHarmonicAnalysis]':
        """List[VirtualComponentHarmonicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_5807.VirtualComponentHarmonicAnalysis]':
        """List[VirtualComponentHarmonicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis':
        return self._Cast_VirtualComponentCompoundHarmonicAnalysis(self)
