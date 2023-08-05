"""_6700.py

GearCompoundCriticalSpeedAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6719
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'GearCompoundCriticalSpeedAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6571


__docformat__ = 'restructuredtext en'
__all__ = ('GearCompoundCriticalSpeedAnalysis',)


class GearCompoundCriticalSpeedAnalysis(_6719.MountableComponentCompoundCriticalSpeedAnalysis):
    """GearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_GearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting GearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'GearCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def mountable_component_compound_critical_speed_analysis(self):
            return self._parent._cast(_6719.MountableComponentCompoundCriticalSpeedAnalysis)

        @property
        def component_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6667
            
            return self._parent._cast(_6667.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6721
            
            return self._parent._cast(_6721.PartCompoundCriticalSpeedAnalysis)

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
        def agma_gleason_conical_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6646
            
            return self._parent._cast(_6646.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6653
            
            return self._parent._cast(_6653.BevelDifferentialGearCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_planet_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6656
            
            return self._parent._cast(_6656.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_sun_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6657
            
            return self._parent._cast(_6657.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis)

        @property
        def bevel_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6658
            
            return self._parent._cast(_6658.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def concept_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6671
            
            return self._parent._cast(_6671.ConceptGearCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6674
            
            return self._parent._cast(_6674.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6689
            
            return self._parent._cast(_6689.CylindricalGearCompoundCriticalSpeedAnalysis)

        @property
        def cylindrical_planet_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6692
            
            return self._parent._cast(_6692.CylindricalPlanetGearCompoundCriticalSpeedAnalysis)

        @property
        def face_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6695
            
            return self._parent._cast(_6695.FaceGearCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6704
            
            return self._parent._cast(_6704.HypoidGearCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6708
            
            return self._parent._cast(_6708.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6711
            
            return self._parent._cast(_6711.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6714
            
            return self._parent._cast(_6714.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6741
            
            return self._parent._cast(_6741.SpiralBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6747
            
            return self._parent._cast(_6747.StraightBevelDiffGearCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6750
            
            return self._parent._cast(_6750.StraightBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6753
            
            return self._parent._cast(_6753.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_sun_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6754
            
            return self._parent._cast(_6754.StraightBevelSunGearCompoundCriticalSpeedAnalysis)

        @property
        def worm_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6765
            
            return self._parent._cast(_6765.WormGearCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6768
            
            return self._parent._cast(_6768.ZerolBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(self) -> 'GearCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_6571.GearCriticalSpeedAnalysis]':
        """List[GearCriticalSpeedAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_6571.GearCriticalSpeedAnalysis]':
        """List[GearCriticalSpeedAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis':
        return self._Cast_GearCompoundCriticalSpeedAnalysis(self)
