"""_7090.py

StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7083
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2532
    from mastapy.system_model.analyses_and_results.system_deflections import _2802


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation',)


class StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation(_7083.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation):
    """StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7083.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6993
            
            return self._parent._cast(_6993.BevelGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6980
            
            return self._parent._cast(_6980.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7009
            
            return self._parent._cast(_7009.ConicalGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7035
            
            return self._parent._cast(_7035.GearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7055
            
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
        def straight_bevel_sun_gear_advanced_time_stepping_analysis_for_modulation(self) -> 'StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2532.StraightBevelSunGear':
        """StraightBevelSunGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2802.StraightBevelSunGearSystemDeflection':
        """StraightBevelSunGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation(self)
