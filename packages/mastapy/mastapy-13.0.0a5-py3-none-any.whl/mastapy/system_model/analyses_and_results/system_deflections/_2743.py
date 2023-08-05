"""_2743.py

GearSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2764
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'GearSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2512
    from mastapy.math_utility.measured_vectors import _1551
    from mastapy.system_model.analyses_and_results.power_flows import _4072


__docformat__ = 'restructuredtext en'
__all__ = ('GearSystemDeflection',)


class GearSystemDeflection(_2764.MountableComponentSystemDeflection):
    """GearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_SYSTEM_DEFLECTION

    class _Cast_GearSystemDeflection:
        """Special nested class for casting GearSystemDeflection to subclasses."""

        def __init__(self, parent: 'GearSystemDeflection'):
            self._parent = parent

        @property
        def mountable_component_system_deflection(self):
            return self._parent._cast(_2764.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2697
            
            return self._parent._cast(_2697.ComponentSystemDeflection)

        @property
        def part_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2767
            
            return self._parent._cast(_2767.PartSystemDeflection)

        @property
        def part_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7513
            
            return self._parent._cast(_7513.PartFEAnalysis)

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
        def agma_gleason_conical_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2673
            
            return self._parent._cast(_2673.AGMAGleasonConicalGearSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2685
            
            return self._parent._cast(_2685.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2686
            
            return self._parent._cast(_2686.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2687
            
            return self._parent._cast(_2687.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2690
            
            return self._parent._cast(_2690.BevelGearSystemDeflection)

        @property
        def concept_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2704
            
            return self._parent._cast(_2704.ConceptGearSystemDeflection)

        @property
        def conical_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2708
            
            return self._parent._cast(_2708.ConicalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2727
            
            return self._parent._cast(_2727.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2728
            
            return self._parent._cast(_2728.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2729
            
            return self._parent._cast(_2729.CylindricalGearSystemDeflectionWithLTCAResults)

        @property
        def cylindrical_planet_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2732
            
            return self._parent._cast(_2732.CylindricalPlanetGearSystemDeflection)

        @property
        def face_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2738
            
            return self._parent._cast(_2738.FaceGearSystemDeflection)

        @property
        def hypoid_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2747
            
            return self._parent._cast(_2747.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2752
            
            return self._parent._cast(_2752.KlingelnbergCycloPalloidConicalGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2755
            
            return self._parent._cast(_2755.KlingelnbergCycloPalloidHypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2758
            
            return self._parent._cast(_2758.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2791
            
            return self._parent._cast(_2791.SpiralBevelGearSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2797
            
            return self._parent._cast(_2797.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2800
            
            return self._parent._cast(_2800.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2801
            
            return self._parent._cast(_2801.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2802
            
            return self._parent._cast(_2802.StraightBevelSunGearSystemDeflection)

        @property
        def worm_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2820
            
            return self._parent._cast(_2820.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2823
            
            return self._parent._cast(_2823.ZerolBevelGearSystemDeflection)

        @property
        def gear_system_deflection(self) -> 'GearSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_loaded(self) -> 'bool':
        """bool: 'IsLoaded' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsLoaded

        if temp is None:
            return False

        return temp

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
    def mesh_point_results_in_wcs(self) -> 'List[_1551.ForceAndDisplacementResults]':
        """List[ForceAndDisplacementResults]: 'MeshPointResultsInWCS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshPointResultsInWCS

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def power_flow_results(self) -> '_4072.GearPowerFlow':
        """GearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearSystemDeflection._Cast_GearSystemDeflection':
        return self._Cast_GearSystemDeflection(self)
