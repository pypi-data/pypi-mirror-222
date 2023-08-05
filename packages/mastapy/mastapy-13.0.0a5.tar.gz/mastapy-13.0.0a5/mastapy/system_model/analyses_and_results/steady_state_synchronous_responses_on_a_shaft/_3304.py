"""_3304.py

MountableComponentSteadyStateSynchronousResponseOnAShaft
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3252
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'MountableComponentSteadyStateSynchronousResponseOnAShaft')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2447


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponentSteadyStateSynchronousResponseOnAShaft',)


class MountableComponentSteadyStateSynchronousResponseOnAShaft(_3252.ComponentSteadyStateSynchronousResponseOnAShaft):
    """MountableComponentSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting MountableComponentSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'MountableComponentSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def component_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3252.ComponentSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3306
            
            return self._parent._cast(_3306.PartSteadyStateSynchronousResponseOnAShaft)

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
        def agma_gleason_conical_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3233
            
            return self._parent._cast(_3233.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def bearing_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3235
            
            return self._parent._cast(_3235.BearingSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_differential_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3240
            
            return self._parent._cast(_3240.BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3241
            
            return self._parent._cast(_3241.BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3242
            
            return self._parent._cast(_3242.BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3245
            
            return self._parent._cast(_3245.BevelGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def clutch_half_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3249
            
            return self._parent._cast(_3249.ClutchHalfSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_coupling_half_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3254
            
            return self._parent._cast(_3254.ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3258
            
            return self._parent._cast(_3258.ConceptGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def conical_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3261
            
            return self._parent._cast(_3261.ConicalGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def connector_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3263
            
            return self._parent._cast(_3263.ConnectorSteadyStateSynchronousResponseOnAShaft)

        @property
        def coupling_half_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3265
            
            return self._parent._cast(_3265.CouplingHalfSteadyStateSynchronousResponseOnAShaft)

        @property
        def cvt_pulley_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3268
            
            return self._parent._cast(_3268.CVTPulleySteadyStateSynchronousResponseOnAShaft)

        @property
        def cylindrical_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3276
            
            return self._parent._cast(_3276.CylindricalGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3277
            
            return self._parent._cast(_3277.CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def face_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3282
            
            return self._parent._cast(_3282.FaceGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3287
            
            return self._parent._cast(_3287.GearSteadyStateSynchronousResponseOnAShaft)

        @property
        def hypoid_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3291
            
            return self._parent._cast(_3291.HypoidGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3295
            
            return self._parent._cast(_3295.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3298
            
            return self._parent._cast(_3298.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3301
            
            return self._parent._cast(_3301.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def mass_disc_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3302
            
            return self._parent._cast(_3302.MassDiscSteadyStateSynchronousResponseOnAShaft)

        @property
        def measurement_component_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3303
            
            return self._parent._cast(_3303.MeasurementComponentSteadyStateSynchronousResponseOnAShaft)

        @property
        def oil_seal_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3305
            
            return self._parent._cast(_3305.OilSealSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3308
            
            return self._parent._cast(_3308.PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft)

        @property
        def planet_carrier_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3312
            
            return self._parent._cast(_3312.PlanetCarrierSteadyStateSynchronousResponseOnAShaft)

        @property
        def point_load_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3313
            
            return self._parent._cast(_3313.PointLoadSteadyStateSynchronousResponseOnAShaft)

        @property
        def power_load_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3314
            
            return self._parent._cast(_3314.PowerLoadSteadyStateSynchronousResponseOnAShaft)

        @property
        def pulley_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3315
            
            return self._parent._cast(_3315.PulleySteadyStateSynchronousResponseOnAShaft)

        @property
        def ring_pins_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3316
            
            return self._parent._cast(_3316.RingPinsSteadyStateSynchronousResponseOnAShaft)

        @property
        def rolling_ring_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3320
            
            return self._parent._cast(_3320.RollingRingSteadyStateSynchronousResponseOnAShaft)

        @property
        def shaft_hub_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3322
            
            return self._parent._cast(_3322.ShaftHubConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3328
            
            return self._parent._cast(_3328.SpiralBevelGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def spring_damper_half_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3330
            
            return self._parent._cast(_3330.SpringDamperHalfSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3335
            
            return self._parent._cast(_3335.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3338
            
            return self._parent._cast(_3338.StraightBevelGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3339
            
            return self._parent._cast(_3339.StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3340
            
            return self._parent._cast(_3340.StraightBevelSunGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def synchroniser_half_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3341
            
            return self._parent._cast(_3341.SynchroniserHalfSteadyStateSynchronousResponseOnAShaft)

        @property
        def synchroniser_part_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3342
            
            return self._parent._cast(_3342.SynchroniserPartSteadyStateSynchronousResponseOnAShaft)

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3343
            
            return self._parent._cast(_3343.SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft)

        @property
        def torque_converter_pump_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3346
            
            return self._parent._cast(_3346.TorqueConverterPumpSteadyStateSynchronousResponseOnAShaft)

        @property
        def torque_converter_turbine_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3348
            
            return self._parent._cast(_3348.TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft)

        @property
        def unbalanced_mass_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3349
            
            return self._parent._cast(_3349.UnbalancedMassSteadyStateSynchronousResponseOnAShaft)

        @property
        def virtual_component_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3350
            
            return self._parent._cast(_3350.VirtualComponentSteadyStateSynchronousResponseOnAShaft)

        @property
        def worm_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3353
            
            return self._parent._cast(_3353.WormGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3356
            
            return self._parent._cast(_3356.ZerolBevelGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(self) -> 'MountableComponentSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MountableComponentSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2447.MountableComponent':
        """MountableComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft(self)
