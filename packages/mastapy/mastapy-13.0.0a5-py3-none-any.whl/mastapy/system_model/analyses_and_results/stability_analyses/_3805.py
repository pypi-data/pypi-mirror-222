"""_3805.py

GearSetStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3844
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'GearSetStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2514


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetStabilityAnalysis',)


class GearSetStabilityAnalysis(_3844.SpecialisedAssemblyStabilityAnalysis):
    """GearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_STABILITY_ANALYSIS

    class _Cast_GearSetStabilityAnalysis:
        """Special nested class for casting GearSetStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'GearSetStabilityAnalysis'):
            self._parent = parent

        @property
        def specialised_assembly_stability_analysis(self):
            return self._parent._cast(_3844.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3745
            
            return self._parent._cast(_3745.AbstractAssemblyStabilityAnalysis)

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
        def agma_gleason_conical_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3750
            
            return self._parent._cast(_3750.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def bevel_differential_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3757
            
            return self._parent._cast(_3757.BevelDifferentialGearSetStabilityAnalysis)

        @property
        def bevel_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3762
            
            return self._parent._cast(_3762.BevelGearSetStabilityAnalysis)

        @property
        def concept_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3775
            
            return self._parent._cast(_3775.ConceptGearSetStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3778
            
            return self._parent._cast(_3778.ConicalGearSetStabilityAnalysis)

        @property
        def cylindrical_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3794
            
            return self._parent._cast(_3794.CylindricalGearSetStabilityAnalysis)

        @property
        def face_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3800
            
            return self._parent._cast(_3800.FaceGearSetStabilityAnalysis)

        @property
        def hypoid_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3809
            
            return self._parent._cast(_3809.HypoidGearSetStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3813
            
            return self._parent._cast(_3813.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3816
            
            return self._parent._cast(_3816.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3819
            
            return self._parent._cast(_3819.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis)

        @property
        def planetary_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3830
            
            return self._parent._cast(_3830.PlanetaryGearSetStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3846
            
            return self._parent._cast(_3846.SpiralBevelGearSetStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3854
            
            return self._parent._cast(_3854.StraightBevelDiffGearSetStabilityAnalysis)

        @property
        def straight_bevel_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3857
            
            return self._parent._cast(_3857.StraightBevelGearSetStabilityAnalysis)

        @property
        def worm_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3872
            
            return self._parent._cast(_3872.WormGearSetStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3875
            
            return self._parent._cast(_3875.ZerolBevelGearSetStabilityAnalysis)

        @property
        def gear_set_stability_analysis(self) -> 'GearSetStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2514.GearSet':
        """GearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis':
        return self._Cast_GearSetStabilityAnalysis(self)
