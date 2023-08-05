"""_6434.py

GearCompoundDynamicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6453
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'GearCompoundDynamicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6305


__docformat__ = 'restructuredtext en'
__all__ = ('GearCompoundDynamicAnalysis',)


class GearCompoundDynamicAnalysis(_6453.MountableComponentCompoundDynamicAnalysis):
    """GearCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_GearCompoundDynamicAnalysis:
        """Special nested class for casting GearCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'GearCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def mountable_component_compound_dynamic_analysis(self):
            return self._parent._cast(_6453.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6401
            
            return self._parent._cast(_6401.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6455
            
            return self._parent._cast(_6455.PartCompoundDynamicAnalysis)

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
        def agma_gleason_conical_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6380
            
            return self._parent._cast(_6380.AGMAGleasonConicalGearCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6387
            
            return self._parent._cast(_6387.BevelDifferentialGearCompoundDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6390
            
            return self._parent._cast(_6390.BevelDifferentialPlanetGearCompoundDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6391
            
            return self._parent._cast(_6391.BevelDifferentialSunGearCompoundDynamicAnalysis)

        @property
        def bevel_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6392
            
            return self._parent._cast(_6392.BevelGearCompoundDynamicAnalysis)

        @property
        def concept_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6405
            
            return self._parent._cast(_6405.ConceptGearCompoundDynamicAnalysis)

        @property
        def conical_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6408
            
            return self._parent._cast(_6408.ConicalGearCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6423
            
            return self._parent._cast(_6423.CylindricalGearCompoundDynamicAnalysis)

        @property
        def cylindrical_planet_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6426
            
            return self._parent._cast(_6426.CylindricalPlanetGearCompoundDynamicAnalysis)

        @property
        def face_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6429
            
            return self._parent._cast(_6429.FaceGearCompoundDynamicAnalysis)

        @property
        def hypoid_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6438
            
            return self._parent._cast(_6438.HypoidGearCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6442
            
            return self._parent._cast(_6442.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6445
            
            return self._parent._cast(_6445.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6448
            
            return self._parent._cast(_6448.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6475
            
            return self._parent._cast(_6475.SpiralBevelGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6481
            
            return self._parent._cast(_6481.StraightBevelDiffGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6484
            
            return self._parent._cast(_6484.StraightBevelGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6487
            
            return self._parent._cast(_6487.StraightBevelPlanetGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6488
            
            return self._parent._cast(_6488.StraightBevelSunGearCompoundDynamicAnalysis)

        @property
        def worm_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6499
            
            return self._parent._cast(_6499.WormGearCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6502
            
            return self._parent._cast(_6502.ZerolBevelGearCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(self) -> 'GearCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_6305.GearDynamicAnalysis]':
        """List[GearDynamicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_6305.GearDynamicAnalysis]':
        """List[GearDynamicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis':
        return self._Cast_GearCompoundDynamicAnalysis(self)
