"""_3758.py

BevelDifferentialGearStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3763
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'BevelDifferentialGearStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2497
    from mastapy.system_model.analyses_and_results.static_loads import _6790


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearStabilityAnalysis',)


class BevelDifferentialGearStabilityAnalysis(_3763.BevelGearStabilityAnalysis):
    """BevelDifferentialGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_STABILITY_ANALYSIS

    class _Cast_BevelDifferentialGearStabilityAnalysis:
        """Special nested class for casting BevelDifferentialGearStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'BevelDifferentialGearStabilityAnalysis'):
            self._parent = parent

        @property
        def bevel_gear_stability_analysis(self):
            return self._parent._cast(_3763.BevelGearStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3751
            
            return self._parent._cast(_3751.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3779
            
            return self._parent._cast(_3779.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3806
            
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
        def bevel_differential_planet_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3759
            
            return self._parent._cast(_3759.BevelDifferentialPlanetGearStabilityAnalysis)

        @property
        def bevel_differential_sun_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3760
            
            return self._parent._cast(_3760.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(self) -> 'BevelDifferentialGearStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2497.BevelDifferentialGear':
        """BevelDifferentialGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6790.BevelDifferentialGearLoadCase':
        """BevelDifferentialGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BevelDifferentialGearStabilityAnalysis._Cast_BevelDifferentialGearStabilityAnalysis':
        return self._Cast_BevelDifferentialGearStabilityAnalysis(self)
