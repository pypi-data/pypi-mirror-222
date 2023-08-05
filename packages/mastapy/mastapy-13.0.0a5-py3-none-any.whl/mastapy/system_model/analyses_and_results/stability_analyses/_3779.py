"""_3779.py

ConicalGearStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3806
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'ConicalGearStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2505


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearStabilityAnalysis',)


class ConicalGearStabilityAnalysis(_3806.GearStabilityAnalysis):
    """ConicalGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_STABILITY_ANALYSIS

    class _Cast_ConicalGearStabilityAnalysis:
        """Special nested class for casting ConicalGearStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'ConicalGearStabilityAnalysis'):
            self._parent = parent

        @property
        def gear_stability_analysis(self):
            return self._parent._cast(_3806.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3823
            
            return self._parent._cast(_3823.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3770
            
            return self._parent._cast(_3770.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3825
            
            return self._parent._cast(_3825.PartStabilityAnalysis)

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
        def agma_gleason_conical_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3751
            
            return self._parent._cast(_3751.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3758
            
            return self._parent._cast(_3758.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3759
            
            return self._parent._cast(_3759.BevelDifferentialPlanetGearStabilityAnalysis)

        @property
        def bevel_differential_sun_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3760
            
            return self._parent._cast(_3760.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3763
            
            return self._parent._cast(_3763.BevelGearStabilityAnalysis)

        @property
        def hypoid_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3810
            
            return self._parent._cast(_3810.HypoidGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3814
            
            return self._parent._cast(_3814.KlingelnbergCycloPalloidConicalGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3817
            
            return self._parent._cast(_3817.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3820
            
            return self._parent._cast(_3820.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis)

        @property
        def spiral_bevel_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3847
            
            return self._parent._cast(_3847.SpiralBevelGearStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3855
            
            return self._parent._cast(_3855.StraightBevelDiffGearStabilityAnalysis)

        @property
        def straight_bevel_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3858
            
            return self._parent._cast(_3858.StraightBevelGearStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3859
            
            return self._parent._cast(_3859.StraightBevelPlanetGearStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3860
            
            return self._parent._cast(_3860.StraightBevelSunGearStabilityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3876
            
            return self._parent._cast(_3876.ZerolBevelGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(self) -> 'ConicalGearStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2505.ConicalGear':
        """ConicalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[ConicalGearStabilityAnalysis]':
        """List[ConicalGearStabilityAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis':
        return self._Cast_ConicalGearStabilityAnalysis(self)
