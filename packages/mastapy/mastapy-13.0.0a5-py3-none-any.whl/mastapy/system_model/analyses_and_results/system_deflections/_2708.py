"""_2708.py

ConicalGearSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2743
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ConicalGearSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2505
    from mastapy.gears.ltca.conical import _864
    from mastapy.system_model.analyses_and_results.power_flows import _4045


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearSystemDeflection',)


class ConicalGearSystemDeflection(_2743.GearSystemDeflection):
    """ConicalGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SYSTEM_DEFLECTION

    class _Cast_ConicalGearSystemDeflection:
        """Special nested class for casting ConicalGearSystemDeflection to subclasses."""

        def __init__(self, parent: 'ConicalGearSystemDeflection'):
            self._parent = parent

        @property
        def gear_system_deflection(self):
            return self._parent._cast(_2743.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2764
            
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
        def zerol_bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2823
            
            return self._parent._cast(_2823.ZerolBevelGearSystemDeflection)

        @property
        def conical_gear_system_deflection(self) -> 'ConicalGearSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearSystemDeflection.TYPE'):
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
    def conical_gear_ltca_results(self) -> '_864.ConicalGearLoadDistributionAnalysis':
        """ConicalGearLoadDistributionAnalysis: 'ConicalGearLTCAResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearLTCAResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[ConicalGearSystemDeflection]':
        """List[ConicalGearSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def power_flow_results(self) -> '_4045.ConicalGearPowerFlow':
        """ConicalGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection':
        return self._Cast_ConicalGearSystemDeflection(self)
