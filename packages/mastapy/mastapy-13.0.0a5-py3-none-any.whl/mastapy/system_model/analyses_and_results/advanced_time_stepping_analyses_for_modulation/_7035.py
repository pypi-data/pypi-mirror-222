"""_7035.py

GearAdvancedTimeSteppingAnalysisForModulation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7055
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'GearAdvancedTimeSteppingAnalysisForModulation')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2512
    from mastapy.system_model.analyses_and_results.system_deflections import _2743


__docformat__ = 'restructuredtext en'
__all__ = ('GearAdvancedTimeSteppingAnalysisForModulation',)


class GearAdvancedTimeSteppingAnalysisForModulation(_7055.MountableComponentAdvancedTimeSteppingAnalysisForModulation):
    """GearAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_GearAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting GearAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'GearAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7055.MountableComponentAdvancedTimeSteppingAnalysisForModulation)

        @property
        def component_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7002
            
            return self._parent._cast(_7002.ComponentAdvancedTimeSteppingAnalysisForModulation)

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
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6980
            
            return self._parent._cast(_6980.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6988
            
            return self._parent._cast(_6988.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_planet_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6991
            
            return self._parent._cast(_6991.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_sun_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6992
            
            return self._parent._cast(_6992.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6993
            
            return self._parent._cast(_6993.BevelGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7006
            
            return self._parent._cast(_7006.ConceptGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7009
            
            return self._parent._cast(_7009.ConicalGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cylindrical_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7024
            
            return self._parent._cast(_7024.CylindricalGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cylindrical_planet_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7027
            
            return self._parent._cast(_7027.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def face_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7030
            
            return self._parent._cast(_7030.FaceGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def hypoid_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7040
            
            return self._parent._cast(_7040.HypoidGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7044
            
            return self._parent._cast(_7044.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7047
            
            return self._parent._cast(_7047.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7050
            
            return self._parent._cast(_7050.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7077
            
            return self._parent._cast(_7077.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_diff_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7083
            
            return self._parent._cast(_7083.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7086
            
            return self._parent._cast(_7086.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_planet_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7089
            
            return self._parent._cast(_7089.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_sun_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7090
            
            return self._parent._cast(_7090.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def worm_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7101
            
            return self._parent._cast(_7101.WormGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def zerol_bevel_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7104
            
            return self._parent._cast(_7104.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(self) -> 'GearAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2512.Gear':
        """Gear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2743.GearSystemDeflection':
        """GearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearAdvancedTimeSteppingAnalysisForModulation._Cast_GearAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_GearAdvancedTimeSteppingAnalysisForModulation(self)
