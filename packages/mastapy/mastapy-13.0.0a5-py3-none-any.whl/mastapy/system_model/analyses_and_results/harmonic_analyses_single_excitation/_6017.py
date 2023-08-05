"""_6017.py

CouplingHarmonicAnalysisOfSingleExcitation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6077
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'CouplingHarmonicAnalysisOfSingleExcitation')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2565


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHarmonicAnalysisOfSingleExcitation',)


class CouplingHarmonicAnalysisOfSingleExcitation(_6077.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation):
    """CouplingHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _COUPLING_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_CouplingHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CouplingHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'CouplingHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6077.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5978
            
            return self._parent._cast(_5978.AbstractAssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6058
            
            return self._parent._cast(_6058.PartHarmonicAnalysisOfSingleExcitation)

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
        def clutch_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6001
            
            return self._parent._cast(_6001.ClutchHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6006
            
            return self._parent._cast(_6006.ConceptCouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6061
            
            return self._parent._cast(_6061.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def spring_damper_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6083
            
            return self._parent._cast(_6083.SpringDamperHarmonicAnalysisOfSingleExcitation)

        @property
        def torque_converter_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6097
            
            return self._parent._cast(_6097.TorqueConverterHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_harmonic_analysis_of_single_excitation(self) -> 'CouplingHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2565.Coupling':
        """Coupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation':
        return self._Cast_CouplingHarmonicAnalysisOfSingleExcitation(self)
