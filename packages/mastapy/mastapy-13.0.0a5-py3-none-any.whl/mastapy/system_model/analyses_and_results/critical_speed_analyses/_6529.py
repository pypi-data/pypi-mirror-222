"""_6529.py

BevelGearSetCriticalSpeedAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6517
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'BevelGearSetCriticalSpeedAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2502


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearSetCriticalSpeedAnalysis',)


class BevelGearSetCriticalSpeedAnalysis(_6517.AGMAGleasonConicalGearSetCriticalSpeedAnalysis):
    """BevelGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_CRITICAL_SPEED_ANALYSIS

    class _Cast_BevelGearSetCriticalSpeedAnalysis:
        """Special nested class for casting BevelGearSetCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'BevelGearSetCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_critical_speed_analysis(self):
            return self._parent._cast(_6517.AGMAGleasonConicalGearSetCriticalSpeedAnalysis)

        @property
        def conical_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6545
            
            return self._parent._cast(_6545.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6573
            
            return self._parent._cast(_6573.GearSetCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6611
            
            return self._parent._cast(_6611.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6511
            
            return self._parent._cast(_6511.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6592
            
            return self._parent._cast(_6592.PartCriticalSpeedAnalysis)

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
        def bevel_differential_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6524
            
            return self._parent._cast(_6524.BevelDifferentialGearSetCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6614
            
            return self._parent._cast(_6614.SpiralBevelGearSetCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6620
            
            return self._parent._cast(_6620.StraightBevelDiffGearSetCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6623
            
            return self._parent._cast(_6623.StraightBevelGearSetCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6641
            
            return self._parent._cast(_6641.ZerolBevelGearSetCriticalSpeedAnalysis)

        @property
        def bevel_gear_set_critical_speed_analysis(self) -> 'BevelGearSetCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearSetCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2502.BevelGearSet':
        """BevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BevelGearSetCriticalSpeedAnalysis._Cast_BevelGearSetCriticalSpeedAnalysis':
        return self._Cast_BevelGearSetCriticalSpeedAnalysis(self)
