"""_5656.py

AGMAGleasonConicalGearHarmonicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5685
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'AGMAGleasonConicalGearHarmonicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2495
    from mastapy.system_model.analyses_and_results.system_deflections import _2673


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearHarmonicAnalysis',)


class AGMAGleasonConicalGearHarmonicAnalysis(_5685.ConicalGearHarmonicAnalysis):
    """AGMAGleasonConicalGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_HARMONIC_ANALYSIS

    class _Cast_AGMAGleasonConicalGearHarmonicAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearHarmonicAnalysis'):
            self._parent = parent

        @property
        def conical_gear_harmonic_analysis(self):
            return self._parent._cast(_5685.ConicalGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5725
            
            return self._parent._cast(_5725.GearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5756
            
            return self._parent._cast(_5756.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5678
            
            return self._parent._cast(_5678.ComponentHarmonicAnalysis)

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
        def bevel_differential_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5663
            
            return self._parent._cast(_5663.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5666
            
            return self._parent._cast(_5666.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5667
            
            return self._parent._cast(_5667.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5668
            
            return self._parent._cast(_5668.BevelGearHarmonicAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5741
            
            return self._parent._cast(_5741.HypoidGearHarmonicAnalysis)

        @property
        def spiral_bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5782
            
            return self._parent._cast(_5782.SpiralBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5789
            
            return self._parent._cast(_5789.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5792
            
            return self._parent._cast(_5792.StraightBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5795
            
            return self._parent._cast(_5795.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5796
            
            return self._parent._cast(_5796.StraightBevelSunGearHarmonicAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5811
            
            return self._parent._cast(_5811.ZerolBevelGearHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(self) -> 'AGMAGleasonConicalGearHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2495.AGMAGleasonConicalGear':
        """AGMAGleasonConicalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2673.AGMAGleasonConicalGearSystemDeflection':
        """AGMAGleasonConicalGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis':
        return self._Cast_AGMAGleasonConicalGearHarmonicAnalysis(self)
