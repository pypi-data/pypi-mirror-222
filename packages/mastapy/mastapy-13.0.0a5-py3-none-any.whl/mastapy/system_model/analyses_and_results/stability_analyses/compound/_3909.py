"""_3909.py

ConicalGearCompoundStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3935
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'ConicalGearCompoundStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3779


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearCompoundStabilityAnalysis',)


class ConicalGearCompoundStabilityAnalysis(_3935.GearCompoundStabilityAnalysis):
    """ConicalGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_COMPOUND_STABILITY_ANALYSIS

    class _Cast_ConicalGearCompoundStabilityAnalysis:
        """Special nested class for casting ConicalGearCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'ConicalGearCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def gear_compound_stability_analysis(self):
            return self._parent._cast(_3935.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3954
            
            return self._parent._cast(_3954.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3902
            
            return self._parent._cast(_3902.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3956
            
            return self._parent._cast(_3956.PartCompoundStabilityAnalysis)

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
        def agma_gleason_conical_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3881
            
            return self._parent._cast(_3881.AGMAGleasonConicalGearCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3888
            
            return self._parent._cast(_3888.BevelDifferentialGearCompoundStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3891
            
            return self._parent._cast(_3891.BevelDifferentialPlanetGearCompoundStabilityAnalysis)

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3892
            
            return self._parent._cast(_3892.BevelDifferentialSunGearCompoundStabilityAnalysis)

        @property
        def bevel_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3893
            
            return self._parent._cast(_3893.BevelGearCompoundStabilityAnalysis)

        @property
        def hypoid_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3939
            
            return self._parent._cast(_3939.HypoidGearCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3943
            
            return self._parent._cast(_3943.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3946
            
            return self._parent._cast(_3946.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3949
            
            return self._parent._cast(_3949.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3976
            
            return self._parent._cast(_3976.SpiralBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3982
            
            return self._parent._cast(_3982.StraightBevelDiffGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3985
            
            return self._parent._cast(_3985.StraightBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3988
            
            return self._parent._cast(_3988.StraightBevelPlanetGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3989
            
            return self._parent._cast(_3989.StraightBevelSunGearCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4003
            
            return self._parent._cast(_4003.ZerolBevelGearCompoundStabilityAnalysis)

        @property
        def conical_gear_compound_stability_analysis(self) -> 'ConicalGearCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self) -> 'List[ConicalGearCompoundStabilityAnalysis]':
        """List[ConicalGearCompoundStabilityAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3779.ConicalGearStabilityAnalysis]':
        """List[ConicalGearStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3779.ConicalGearStabilityAnalysis]':
        """List[ConicalGearStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis':
        return self._Cast_ConicalGearCompoundStabilityAnalysis(self)
