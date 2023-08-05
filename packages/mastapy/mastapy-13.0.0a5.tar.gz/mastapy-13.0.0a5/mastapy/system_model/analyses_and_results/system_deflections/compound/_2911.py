"""_2911.py

MountableComponentCompoundSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2858
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'MountableComponentCompoundSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2764


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponentCompoundSystemDeflection',)


class MountableComponentCompoundSystemDeflection(_2858.ComponentCompoundSystemDeflection):
    """MountableComponentCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_MountableComponentCompoundSystemDeflection:
        """Special nested class for casting MountableComponentCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'MountableComponentCompoundSystemDeflection'):
            self._parent = parent

        @property
        def component_compound_system_deflection(self):
            return self._parent._cast(_2858.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2913
            
            return self._parent._cast(_2913.PartCompoundSystemDeflection)

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
        def agma_gleason_conical_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2837
            
            return self._parent._cast(_2837.AGMAGleasonConicalGearCompoundSystemDeflection)

        @property
        def bearing_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2841
            
            return self._parent._cast(_2841.BearingCompoundSystemDeflection)

        @property
        def bevel_differential_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2844
            
            return self._parent._cast(_2844.BevelDifferentialGearCompoundSystemDeflection)

        @property
        def bevel_differential_planet_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2847
            
            return self._parent._cast(_2847.BevelDifferentialPlanetGearCompoundSystemDeflection)

        @property
        def bevel_differential_sun_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2848
            
            return self._parent._cast(_2848.BevelDifferentialSunGearCompoundSystemDeflection)

        @property
        def bevel_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2849
            
            return self._parent._cast(_2849.BevelGearCompoundSystemDeflection)

        @property
        def clutch_half_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2856
            
            return self._parent._cast(_2856.ClutchHalfCompoundSystemDeflection)

        @property
        def concept_coupling_half_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2861
            
            return self._parent._cast(_2861.ConceptCouplingHalfCompoundSystemDeflection)

        @property
        def concept_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2862
            
            return self._parent._cast(_2862.ConceptGearCompoundSystemDeflection)

        @property
        def conical_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2865
            
            return self._parent._cast(_2865.ConicalGearCompoundSystemDeflection)

        @property
        def connector_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2869
            
            return self._parent._cast(_2869.ConnectorCompoundSystemDeflection)

        @property
        def coupling_half_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2872
            
            return self._parent._cast(_2872.CouplingHalfCompoundSystemDeflection)

        @property
        def cvt_pulley_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2875
            
            return self._parent._cast(_2875.CVTPulleyCompoundSystemDeflection)

        @property
        def cylindrical_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2880
            
            return self._parent._cast(_2880.CylindricalGearCompoundSystemDeflection)

        @property
        def cylindrical_planet_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2883
            
            return self._parent._cast(_2883.CylindricalPlanetGearCompoundSystemDeflection)

        @property
        def face_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2887
            
            return self._parent._cast(_2887.FaceGearCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2892
            
            return self._parent._cast(_2892.GearCompoundSystemDeflection)

        @property
        def hypoid_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2896
            
            return self._parent._cast(_2896.HypoidGearCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2900
            
            return self._parent._cast(_2900.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2903
            
            return self._parent._cast(_2903.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2906
            
            return self._parent._cast(_2906.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection)

        @property
        def mass_disc_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2909
            
            return self._parent._cast(_2909.MassDiscCompoundSystemDeflection)

        @property
        def measurement_component_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2910
            
            return self._parent._cast(_2910.MeasurementComponentCompoundSystemDeflection)

        @property
        def oil_seal_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2912
            
            return self._parent._cast(_2912.OilSealCompoundSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2916
            
            return self._parent._cast(_2916.PartToPartShearCouplingHalfCompoundSystemDeflection)

        @property
        def planet_carrier_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2919
            
            return self._parent._cast(_2919.PlanetCarrierCompoundSystemDeflection)

        @property
        def point_load_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2920
            
            return self._parent._cast(_2920.PointLoadCompoundSystemDeflection)

        @property
        def power_load_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2921
            
            return self._parent._cast(_2921.PowerLoadCompoundSystemDeflection)

        @property
        def pulley_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2922
            
            return self._parent._cast(_2922.PulleyCompoundSystemDeflection)

        @property
        def ring_pins_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2923
            
            return self._parent._cast(_2923.RingPinsCompoundSystemDeflection)

        @property
        def rolling_ring_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2926
            
            return self._parent._cast(_2926.RollingRingCompoundSystemDeflection)

        @property
        def shaft_hub_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2931
            
            return self._parent._cast(_2931.ShaftHubConnectionCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2934
            
            return self._parent._cast(_2934.SpiralBevelGearCompoundSystemDeflection)

        @property
        def spring_damper_half_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2939
            
            return self._parent._cast(_2939.SpringDamperHalfCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2940
            
            return self._parent._cast(_2940.StraightBevelDiffGearCompoundSystemDeflection)

        @property
        def straight_bevel_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2943
            
            return self._parent._cast(_2943.StraightBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_planet_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2946
            
            return self._parent._cast(_2946.StraightBevelPlanetGearCompoundSystemDeflection)

        @property
        def straight_bevel_sun_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2947
            
            return self._parent._cast(_2947.StraightBevelSunGearCompoundSystemDeflection)

        @property
        def synchroniser_half_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2949
            
            return self._parent._cast(_2949.SynchroniserHalfCompoundSystemDeflection)

        @property
        def synchroniser_part_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2950
            
            return self._parent._cast(_2950.SynchroniserPartCompoundSystemDeflection)

        @property
        def synchroniser_sleeve_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2951
            
            return self._parent._cast(_2951.SynchroniserSleeveCompoundSystemDeflection)

        @property
        def torque_converter_pump_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2954
            
            return self._parent._cast(_2954.TorqueConverterPumpCompoundSystemDeflection)

        @property
        def torque_converter_turbine_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2955
            
            return self._parent._cast(_2955.TorqueConverterTurbineCompoundSystemDeflection)

        @property
        def unbalanced_mass_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2956
            
            return self._parent._cast(_2956.UnbalancedMassCompoundSystemDeflection)

        @property
        def virtual_component_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2957
            
            return self._parent._cast(_2957.VirtualComponentCompoundSystemDeflection)

        @property
        def worm_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2958
            
            return self._parent._cast(_2958.WormGearCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2961
            
            return self._parent._cast(_2961.ZerolBevelGearCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(self) -> 'MountableComponentCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MountableComponentCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_2764.MountableComponentSystemDeflection]':
        """List[MountableComponentSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_2764.MountableComponentSystemDeflection]':
        """List[MountableComponentSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection':
        return self._Cast_MountableComponentCompoundSystemDeflection(self)
