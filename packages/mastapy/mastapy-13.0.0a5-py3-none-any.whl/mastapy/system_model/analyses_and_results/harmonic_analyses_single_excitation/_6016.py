"""_6016.py

CouplingHalfHarmonicAnalysisOfSingleExcitation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6056
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'CouplingHalfHarmonicAnalysisOfSingleExcitation')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2566


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHalfHarmonicAnalysisOfSingleExcitation',)


class CouplingHalfHarmonicAnalysisOfSingleExcitation(_6056.MountableComponentHarmonicAnalysisOfSingleExcitation):
    """CouplingHalfHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CouplingHalfHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'CouplingHalfHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6056.MountableComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def component_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6003
            
            return self._parent._cast(_6003.ComponentHarmonicAnalysisOfSingleExcitation)

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
        def clutch_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6000
            
            return self._parent._cast(_6000.ClutchHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6005
            
            return self._parent._cast(_6005.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_pulley_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6020
            
            return self._parent._cast(_6020.CVTPulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6060
            
            return self._parent._cast(_6060.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def pulley_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6067
            
            return self._parent._cast(_6067.PulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6072
            
            return self._parent._cast(_6072.RollingRingHarmonicAnalysisOfSingleExcitation)

        @property
        def spring_damper_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6082
            
            return self._parent._cast(_6082.SpringDamperHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6092
            
            return self._parent._cast(_6092.SynchroniserHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_part_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6094
            
            return self._parent._cast(_6094.SynchroniserPartHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_sleeve_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6095
            
            return self._parent._cast(_6095.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation)

        @property
        def torque_converter_pump_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6098
            
            return self._parent._cast(_6098.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation)

        @property
        def torque_converter_turbine_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6099
            
            return self._parent._cast(_6099.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(self) -> 'CouplingHalfHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingHalfHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2566.CouplingHalf':
        """CouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation':
        return self._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation(self)
