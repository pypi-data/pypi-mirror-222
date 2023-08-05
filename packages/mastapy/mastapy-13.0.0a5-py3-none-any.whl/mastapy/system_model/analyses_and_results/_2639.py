"""_2639.py

PartAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results import _2635
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'PartAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PartAnalysis',)


class PartAnalysis(_2635.DesignEntitySingleContextAnalysis):
    """PartAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_ANALYSIS

    class _Cast_PartAnalysis:
        """Special nested class for casting PartAnalysis to subclasses."""

        def __init__(self, parent: 'PartAnalysis'):
            self._parent = parent

        @property
        def design_entity_single_context_analysis(self):
            return self._parent._cast(_2635.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def abstract_assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2667
            
            return self._parent._cast(_2667.AbstractAssemblySystemDeflection)

        @property
        def abstract_shaft_or_housing_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2668
            
            return self._parent._cast(_2668.AbstractShaftOrHousingSystemDeflection)

        @property
        def abstract_shaft_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2669
            
            return self._parent._cast(_2669.AbstractShaftSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2672
            
            return self._parent._cast(_2672.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2673
            
            return self._parent._cast(_2673.AGMAGleasonConicalGearSystemDeflection)

        @property
        def assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2674
            
            return self._parent._cast(_2674.AssemblySystemDeflection)

        @property
        def bearing_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2680
            
            return self._parent._cast(_2680.BearingSystemDeflection)

        @property
        def belt_drive_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2682
            
            return self._parent._cast(_2682.BeltDriveSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2684
            
            return self._parent._cast(_2684.BevelDifferentialGearSetSystemDeflection)

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
        def bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2689
            
            return self._parent._cast(_2689.BevelGearSetSystemDeflection)

        @property
        def bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2690
            
            return self._parent._cast(_2690.BevelGearSystemDeflection)

        @property
        def bolted_joint_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2691
            
            return self._parent._cast(_2691.BoltedJointSystemDeflection)

        @property
        def bolt_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2692
            
            return self._parent._cast(_2692.BoltSystemDeflection)

        @property
        def clutch_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2694
            
            return self._parent._cast(_2694.ClutchHalfSystemDeflection)

        @property
        def clutch_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2695
            
            return self._parent._cast(_2695.ClutchSystemDeflection)

        @property
        def component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2697
            
            return self._parent._cast(_2697.ComponentSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2700
            
            return self._parent._cast(_2700.ConceptCouplingHalfSystemDeflection)

        @property
        def concept_coupling_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2701
            
            return self._parent._cast(_2701.ConceptCouplingSystemDeflection)

        @property
        def concept_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2703
            
            return self._parent._cast(_2703.ConceptGearSetSystemDeflection)

        @property
        def concept_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2704
            
            return self._parent._cast(_2704.ConceptGearSystemDeflection)

        @property
        def conical_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2707
            
            return self._parent._cast(_2707.ConicalGearSetSystemDeflection)

        @property
        def conical_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2708
            
            return self._parent._cast(_2708.ConicalGearSystemDeflection)

        @property
        def connector_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2710
            
            return self._parent._cast(_2710.ConnectorSystemDeflection)

        @property
        def coupling_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2712
            
            return self._parent._cast(_2712.CouplingHalfSystemDeflection)

        @property
        def coupling_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2713
            
            return self._parent._cast(_2713.CouplingSystemDeflection)

        @property
        def cvt_pulley_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2715
            
            return self._parent._cast(_2715.CVTPulleySystemDeflection)

        @property
        def cvt_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2716
            
            return self._parent._cast(_2716.CVTSystemDeflection)

        @property
        def cycloidal_assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2717
            
            return self._parent._cast(_2717.CycloidalAssemblySystemDeflection)

        @property
        def cycloidal_disc_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2720
            
            return self._parent._cast(_2720.CycloidalDiscSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2724
            
            return self._parent._cast(_2724.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2725
            
            return self._parent._cast(_2725.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2726
            
            return self._parent._cast(_2726.CylindricalGearSetSystemDeflectionWithLTCAResults)

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
        def datum_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2733
            
            return self._parent._cast(_2733.DatumSystemDeflection)

        @property
        def external_cad_model_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2734
            
            return self._parent._cast(_2734.ExternalCADModelSystemDeflection)

        @property
        def face_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2737
            
            return self._parent._cast(_2737.FaceGearSetSystemDeflection)

        @property
        def face_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2738
            
            return self._parent._cast(_2738.FaceGearSystemDeflection)

        @property
        def fe_part_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2739
            
            return self._parent._cast(_2739.FEPartSystemDeflection)

        @property
        def flexible_pin_assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2740
            
            return self._parent._cast(_2740.FlexiblePinAssemblySystemDeflection)

        @property
        def gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2742
            
            return self._parent._cast(_2742.GearSetSystemDeflection)

        @property
        def gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2743
            
            return self._parent._cast(_2743.GearSystemDeflection)

        @property
        def guide_dxf_model_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2744
            
            return self._parent._cast(_2744.GuideDxfModelSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2746
            
            return self._parent._cast(_2746.HypoidGearSetSystemDeflection)

        @property
        def hypoid_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2747
            
            return self._parent._cast(_2747.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2751
            
            return self._parent._cast(_2751.KlingelnbergCycloPalloidConicalGearSetSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2752
            
            return self._parent._cast(_2752.KlingelnbergCycloPalloidConicalGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2754
            
            return self._parent._cast(_2754.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2755
            
            return self._parent._cast(_2755.KlingelnbergCycloPalloidHypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2757
            
            return self._parent._cast(_2757.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2758
            
            return self._parent._cast(_2758.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection)

        @property
        def mass_disc_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2761
            
            return self._parent._cast(_2761.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2762
            
            return self._parent._cast(_2762.MeasurementComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2764
            
            return self._parent._cast(_2764.MountableComponentSystemDeflection)

        @property
        def oil_seal_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2766
            
            return self._parent._cast(_2766.OilSealSystemDeflection)

        @property
        def part_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2767
            
            return self._parent._cast(_2767.PartSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2769
            
            return self._parent._cast(_2769.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def part_to_part_shear_coupling_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2770
            
            return self._parent._cast(_2770.PartToPartShearCouplingSystemDeflection)

        @property
        def planet_carrier_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2772
            
            return self._parent._cast(_2772.PlanetCarrierSystemDeflection)

        @property
        def point_load_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2773
            
            return self._parent._cast(_2773.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2774
            
            return self._parent._cast(_2774.PowerLoadSystemDeflection)

        @property
        def pulley_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2775
            
            return self._parent._cast(_2775.PulleySystemDeflection)

        @property
        def ring_pins_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2776
            
            return self._parent._cast(_2776.RingPinsSystemDeflection)

        @property
        def rolling_ring_assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2779
            
            return self._parent._cast(_2779.RollingRingAssemblySystemDeflection)

        @property
        def rolling_ring_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2781
            
            return self._parent._cast(_2781.RollingRingSystemDeflection)

        @property
        def root_assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2782
            
            return self._parent._cast(_2782.RootAssemblySystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2783
            
            return self._parent._cast(_2783.ShaftHubConnectionSystemDeflection)

        @property
        def shaft_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2786
            
            return self._parent._cast(_2786.ShaftSystemDeflection)

        @property
        def specialised_assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2788
            
            return self._parent._cast(_2788.SpecialisedAssemblySystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2790
            
            return self._parent._cast(_2790.SpiralBevelGearSetSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2791
            
            return self._parent._cast(_2791.SpiralBevelGearSystemDeflection)

        @property
        def spring_damper_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2793
            
            return self._parent._cast(_2793.SpringDamperHalfSystemDeflection)

        @property
        def spring_damper_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2794
            
            return self._parent._cast(_2794.SpringDamperSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2796
            
            return self._parent._cast(_2796.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2797
            
            return self._parent._cast(_2797.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2799
            
            return self._parent._cast(_2799.StraightBevelGearSetSystemDeflection)

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
        def synchroniser_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2803
            
            return self._parent._cast(_2803.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2804
            
            return self._parent._cast(_2804.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2805
            
            return self._parent._cast(_2805.SynchroniserSleeveSystemDeflection)

        @property
        def synchroniser_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2806
            
            return self._parent._cast(_2806.SynchroniserSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2811
            
            return self._parent._cast(_2811.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2812
            
            return self._parent._cast(_2812.TorqueConverterSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2813
            
            return self._parent._cast(_2813.TorqueConverterTurbineSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2816
            
            return self._parent._cast(_2816.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2817
            
            return self._parent._cast(_2817.VirtualComponentSystemDeflection)

        @property
        def worm_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2819
            
            return self._parent._cast(_2819.WormGearSetSystemDeflection)

        @property
        def worm_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2820
            
            return self._parent._cast(_2820.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2822
            
            return self._parent._cast(_2822.ZerolBevelGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2823
            
            return self._parent._cast(_2823.ZerolBevelGearSystemDeflection)

        @property
        def abstract_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2965
            
            return self._parent._cast(_2965.AbstractAssemblySteadyStateSynchronousResponse)

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2966
            
            return self._parent._cast(_2966.AbstractShaftOrHousingSteadyStateSynchronousResponse)

        @property
        def abstract_shaft_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2967
            
            return self._parent._cast(_2967.AbstractShaftSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2970
            
            return self._parent._cast(_2970.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2971
            
            return self._parent._cast(_2971.AGMAGleasonConicalGearSteadyStateSynchronousResponse)

        @property
        def assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2972
            
            return self._parent._cast(_2972.AssemblySteadyStateSynchronousResponse)

        @property
        def bearing_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2973
            
            return self._parent._cast(_2973.BearingSteadyStateSynchronousResponse)

        @property
        def belt_drive_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2975
            
            return self._parent._cast(_2975.BeltDriveSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2977
            
            return self._parent._cast(_2977.BevelDifferentialGearSetSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2978
            
            return self._parent._cast(_2978.BevelDifferentialGearSteadyStateSynchronousResponse)

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2979
            
            return self._parent._cast(_2979.BevelDifferentialPlanetGearSteadyStateSynchronousResponse)

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2980
            
            return self._parent._cast(_2980.BevelDifferentialSunGearSteadyStateSynchronousResponse)

        @property
        def bevel_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2982
            
            return self._parent._cast(_2982.BevelGearSetSteadyStateSynchronousResponse)

        @property
        def bevel_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2983
            
            return self._parent._cast(_2983.BevelGearSteadyStateSynchronousResponse)

        @property
        def bolted_joint_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2984
            
            return self._parent._cast(_2984.BoltedJointSteadyStateSynchronousResponse)

        @property
        def bolt_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2985
            
            return self._parent._cast(_2985.BoltSteadyStateSynchronousResponse)

        @property
        def clutch_half_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2987
            
            return self._parent._cast(_2987.ClutchHalfSteadyStateSynchronousResponse)

        @property
        def clutch_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2988
            
            return self._parent._cast(_2988.ClutchSteadyStateSynchronousResponse)

        @property
        def component_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2990
            
            return self._parent._cast(_2990.ComponentSteadyStateSynchronousResponse)

        @property
        def concept_coupling_half_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2992
            
            return self._parent._cast(_2992.ConceptCouplingHalfSteadyStateSynchronousResponse)

        @property
        def concept_coupling_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2993
            
            return self._parent._cast(_2993.ConceptCouplingSteadyStateSynchronousResponse)

        @property
        def concept_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2995
            
            return self._parent._cast(_2995.ConceptGearSetSteadyStateSynchronousResponse)

        @property
        def concept_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2996
            
            return self._parent._cast(_2996.ConceptGearSteadyStateSynchronousResponse)

        @property
        def conical_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2998
            
            return self._parent._cast(_2998.ConicalGearSetSteadyStateSynchronousResponse)

        @property
        def conical_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2999
            
            return self._parent._cast(_2999.ConicalGearSteadyStateSynchronousResponse)

        @property
        def connector_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3001
            
            return self._parent._cast(_3001.ConnectorSteadyStateSynchronousResponse)

        @property
        def coupling_half_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3003
            
            return self._parent._cast(_3003.CouplingHalfSteadyStateSynchronousResponse)

        @property
        def coupling_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3004
            
            return self._parent._cast(_3004.CouplingSteadyStateSynchronousResponse)

        @property
        def cvt_pulley_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3006
            
            return self._parent._cast(_3006.CVTPulleySteadyStateSynchronousResponse)

        @property
        def cvt_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3007
            
            return self._parent._cast(_3007.CVTSteadyStateSynchronousResponse)

        @property
        def cycloidal_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3008
            
            return self._parent._cast(_3008.CycloidalAssemblySteadyStateSynchronousResponse)

        @property
        def cycloidal_disc_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3011
            
            return self._parent._cast(_3011.CycloidalDiscSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3013
            
            return self._parent._cast(_3013.CylindricalGearSetSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3014
            
            return self._parent._cast(_3014.CylindricalGearSteadyStateSynchronousResponse)

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3015
            
            return self._parent._cast(_3015.CylindricalPlanetGearSteadyStateSynchronousResponse)

        @property
        def datum_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3016
            
            return self._parent._cast(_3016.DatumSteadyStateSynchronousResponse)

        @property
        def external_cad_model_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3018
            
            return self._parent._cast(_3018.ExternalCADModelSteadyStateSynchronousResponse)

        @property
        def face_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3020
            
            return self._parent._cast(_3020.FaceGearSetSteadyStateSynchronousResponse)

        @property
        def face_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3021
            
            return self._parent._cast(_3021.FaceGearSteadyStateSynchronousResponse)

        @property
        def fe_part_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3022
            
            return self._parent._cast(_3022.FEPartSteadyStateSynchronousResponse)

        @property
        def flexible_pin_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3023
            
            return self._parent._cast(_3023.FlexiblePinAssemblySteadyStateSynchronousResponse)

        @property
        def gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3025
            
            return self._parent._cast(_3025.GearSetSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3026
            
            return self._parent._cast(_3026.GearSteadyStateSynchronousResponse)

        @property
        def guide_dxf_model_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3027
            
            return self._parent._cast(_3027.GuideDxfModelSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3029
            
            return self._parent._cast(_3029.HypoidGearSetSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3030
            
            return self._parent._cast(_3030.HypoidGearSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3033
            
            return self._parent._cast(_3033.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3034
            
            return self._parent._cast(_3034.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3036
            
            return self._parent._cast(_3036.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3037
            
            return self._parent._cast(_3037.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3039
            
            return self._parent._cast(_3039.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3040
            
            return self._parent._cast(_3040.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse)

        @property
        def mass_disc_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3041
            
            return self._parent._cast(_3041.MassDiscSteadyStateSynchronousResponse)

        @property
        def measurement_component_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3042
            
            return self._parent._cast(_3042.MeasurementComponentSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3043
            
            return self._parent._cast(_3043.MountableComponentSteadyStateSynchronousResponse)

        @property
        def oil_seal_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3044
            
            return self._parent._cast(_3044.OilSealSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3045
            
            return self._parent._cast(_3045.PartSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3047
            
            return self._parent._cast(_3047.PartToPartShearCouplingHalfSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3048
            
            return self._parent._cast(_3048.PartToPartShearCouplingSteadyStateSynchronousResponse)

        @property
        def planetary_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3050
            
            return self._parent._cast(_3050.PlanetaryGearSetSteadyStateSynchronousResponse)

        @property
        def planet_carrier_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3051
            
            return self._parent._cast(_3051.PlanetCarrierSteadyStateSynchronousResponse)

        @property
        def point_load_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3052
            
            return self._parent._cast(_3052.PointLoadSteadyStateSynchronousResponse)

        @property
        def power_load_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3053
            
            return self._parent._cast(_3053.PowerLoadSteadyStateSynchronousResponse)

        @property
        def pulley_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3054
            
            return self._parent._cast(_3054.PulleySteadyStateSynchronousResponse)

        @property
        def ring_pins_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3055
            
            return self._parent._cast(_3055.RingPinsSteadyStateSynchronousResponse)

        @property
        def rolling_ring_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3057
            
            return self._parent._cast(_3057.RollingRingAssemblySteadyStateSynchronousResponse)

        @property
        def rolling_ring_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3059
            
            return self._parent._cast(_3059.RollingRingSteadyStateSynchronousResponse)

        @property
        def root_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3060
            
            return self._parent._cast(_3060.RootAssemblySteadyStateSynchronousResponse)

        @property
        def shaft_hub_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3061
            
            return self._parent._cast(_3061.ShaftHubConnectionSteadyStateSynchronousResponse)

        @property
        def shaft_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3062
            
            return self._parent._cast(_3062.ShaftSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3064
            
            return self._parent._cast(_3064.SpecialisedAssemblySteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3066
            
            return self._parent._cast(_3066.SpiralBevelGearSetSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3067
            
            return self._parent._cast(_3067.SpiralBevelGearSteadyStateSynchronousResponse)

        @property
        def spring_damper_half_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3069
            
            return self._parent._cast(_3069.SpringDamperHalfSteadyStateSynchronousResponse)

        @property
        def spring_damper_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3070
            
            return self._parent._cast(_3070.SpringDamperSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3075
            
            return self._parent._cast(_3075.StraightBevelDiffGearSetSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3076
            
            return self._parent._cast(_3076.StraightBevelDiffGearSteadyStateSynchronousResponse)

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3078
            
            return self._parent._cast(_3078.StraightBevelGearSetSteadyStateSynchronousResponse)

        @property
        def straight_bevel_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3079
            
            return self._parent._cast(_3079.StraightBevelGearSteadyStateSynchronousResponse)

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3080
            
            return self._parent._cast(_3080.StraightBevelPlanetGearSteadyStateSynchronousResponse)

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3081
            
            return self._parent._cast(_3081.StraightBevelSunGearSteadyStateSynchronousResponse)

        @property
        def synchroniser_half_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3082
            
            return self._parent._cast(_3082.SynchroniserHalfSteadyStateSynchronousResponse)

        @property
        def synchroniser_part_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3083
            
            return self._parent._cast(_3083.SynchroniserPartSteadyStateSynchronousResponse)

        @property
        def synchroniser_sleeve_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3084
            
            return self._parent._cast(_3084.SynchroniserSleeveSteadyStateSynchronousResponse)

        @property
        def synchroniser_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3085
            
            return self._parent._cast(_3085.SynchroniserSteadyStateSynchronousResponse)

        @property
        def torque_converter_pump_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3087
            
            return self._parent._cast(_3087.TorqueConverterPumpSteadyStateSynchronousResponse)

        @property
        def torque_converter_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3088
            
            return self._parent._cast(_3088.TorqueConverterSteadyStateSynchronousResponse)

        @property
        def torque_converter_turbine_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3089
            
            return self._parent._cast(_3089.TorqueConverterTurbineSteadyStateSynchronousResponse)

        @property
        def unbalanced_mass_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3090
            
            return self._parent._cast(_3090.UnbalancedMassSteadyStateSynchronousResponse)

        @property
        def virtual_component_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3091
            
            return self._parent._cast(_3091.VirtualComponentSteadyStateSynchronousResponse)

        @property
        def worm_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3093
            
            return self._parent._cast(_3093.WormGearSetSteadyStateSynchronousResponse)

        @property
        def worm_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3094
            
            return self._parent._cast(_3094.WormGearSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3096
            
            return self._parent._cast(_3096.ZerolBevelGearSetSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3097
            
            return self._parent._cast(_3097.ZerolBevelGearSteadyStateSynchronousResponse)

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3227
            
            return self._parent._cast(_3227.AbstractAssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3228
            
            return self._parent._cast(_3228.AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft)

        @property
        def abstract_shaft_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3229
            
            return self._parent._cast(_3229.AbstractShaftSteadyStateSynchronousResponseOnAShaft)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3232
            
            return self._parent._cast(_3232.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3233
            
            return self._parent._cast(_3233.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def assembly_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3234
            
            return self._parent._cast(_3234.AssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def bearing_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3235
            
            return self._parent._cast(_3235.BearingSteadyStateSynchronousResponseOnAShaft)

        @property
        def belt_drive_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3237
            
            return self._parent._cast(_3237.BeltDriveSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3239
            
            return self._parent._cast(_3239.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft)

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
        def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3244
            
            return self._parent._cast(_3244.BevelGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3245
            
            return self._parent._cast(_3245.BevelGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def bolted_joint_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3246
            
            return self._parent._cast(_3246.BoltedJointSteadyStateSynchronousResponseOnAShaft)

        @property
        def bolt_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3247
            
            return self._parent._cast(_3247.BoltSteadyStateSynchronousResponseOnAShaft)

        @property
        def clutch_half_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3249
            
            return self._parent._cast(_3249.ClutchHalfSteadyStateSynchronousResponseOnAShaft)

        @property
        def clutch_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3250
            
            return self._parent._cast(_3250.ClutchSteadyStateSynchronousResponseOnAShaft)

        @property
        def component_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3252
            
            return self._parent._cast(_3252.ComponentSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_coupling_half_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3254
            
            return self._parent._cast(_3254.ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_coupling_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3255
            
            return self._parent._cast(_3255.ConceptCouplingSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3257
            
            return self._parent._cast(_3257.ConceptGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3258
            
            return self._parent._cast(_3258.ConceptGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3260
            
            return self._parent._cast(_3260.ConicalGearSetSteadyStateSynchronousResponseOnAShaft)

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
        def coupling_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3266
            
            return self._parent._cast(_3266.CouplingSteadyStateSynchronousResponseOnAShaft)

        @property
        def cvt_pulley_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3268
            
            return self._parent._cast(_3268.CVTPulleySteadyStateSynchronousResponseOnAShaft)

        @property
        def cvt_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3269
            
            return self._parent._cast(_3269.CVTSteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3270
            
            return self._parent._cast(_3270.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_disc_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3273
            
            return self._parent._cast(_3273.CycloidalDiscSteadyStateSynchronousResponseOnAShaft)

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3275
            
            return self._parent._cast(_3275.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def cylindrical_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3276
            
            return self._parent._cast(_3276.CylindricalGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3277
            
            return self._parent._cast(_3277.CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def datum_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3278
            
            return self._parent._cast(_3278.DatumSteadyStateSynchronousResponseOnAShaft)

        @property
        def external_cad_model_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3279
            
            return self._parent._cast(_3279.ExternalCADModelSteadyStateSynchronousResponseOnAShaft)

        @property
        def face_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3281
            
            return self._parent._cast(_3281.FaceGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def face_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3282
            
            return self._parent._cast(_3282.FaceGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def fe_part_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3283
            
            return self._parent._cast(_3283.FEPartSteadyStateSynchronousResponseOnAShaft)

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3284
            
            return self._parent._cast(_3284.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3286
            
            return self._parent._cast(_3286.GearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3287
            
            return self._parent._cast(_3287.GearSteadyStateSynchronousResponseOnAShaft)

        @property
        def guide_dxf_model_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3288
            
            return self._parent._cast(_3288.GuideDxfModelSteadyStateSynchronousResponseOnAShaft)

        @property
        def hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3290
            
            return self._parent._cast(_3290.HypoidGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def hypoid_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3291
            
            return self._parent._cast(_3291.HypoidGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3294
            
            return self._parent._cast(_3294.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3295
            
            return self._parent._cast(_3295.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3297
            
            return self._parent._cast(_3297.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3298
            
            return self._parent._cast(_3298.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3300
            
            return self._parent._cast(_3300.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft)

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
        def mountable_component_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3304
            
            return self._parent._cast(_3304.MountableComponentSteadyStateSynchronousResponseOnAShaft)

        @property
        def oil_seal_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3305
            
            return self._parent._cast(_3305.OilSealSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3306
            
            return self._parent._cast(_3306.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3308
            
            return self._parent._cast(_3308.PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3309
            
            return self._parent._cast(_3309.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft)

        @property
        def planetary_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3311
            
            return self._parent._cast(_3311.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft)

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
        def rolling_ring_assembly_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3318
            
            return self._parent._cast(_3318.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def rolling_ring_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3320
            
            return self._parent._cast(_3320.RollingRingSteadyStateSynchronousResponseOnAShaft)

        @property
        def root_assembly_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3321
            
            return self._parent._cast(_3321.RootAssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def shaft_hub_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3322
            
            return self._parent._cast(_3322.ShaftHubConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def shaft_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3323
            
            return self._parent._cast(_3323.ShaftSteadyStateSynchronousResponseOnAShaft)

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3325
            
            return self._parent._cast(_3325.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3327
            
            return self._parent._cast(_3327.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3328
            
            return self._parent._cast(_3328.SpiralBevelGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def spring_damper_half_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3330
            
            return self._parent._cast(_3330.SpringDamperHalfSteadyStateSynchronousResponseOnAShaft)

        @property
        def spring_damper_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3331
            
            return self._parent._cast(_3331.SpringDamperSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3334
            
            return self._parent._cast(_3334.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3335
            
            return self._parent._cast(_3335.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3337
            
            return self._parent._cast(_3337.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft)

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
        def synchroniser_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3344
            
            return self._parent._cast(_3344.SynchroniserSteadyStateSynchronousResponseOnAShaft)

        @property
        def torque_converter_pump_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3346
            
            return self._parent._cast(_3346.TorqueConverterPumpSteadyStateSynchronousResponseOnAShaft)

        @property
        def torque_converter_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3347
            
            return self._parent._cast(_3347.TorqueConverterSteadyStateSynchronousResponseOnAShaft)

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
        def worm_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3352
            
            return self._parent._cast(_3352.WormGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def worm_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3353
            
            return self._parent._cast(_3353.WormGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3355
            
            return self._parent._cast(_3355.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3356
            
            return self._parent._cast(_3356.ZerolBevelGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3486
            
            return self._parent._cast(_3486.AbstractAssemblySteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3487
            
            return self._parent._cast(_3487.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_shaft_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3488
            
            return self._parent._cast(_3488.AbstractShaftSteadyStateSynchronousResponseAtASpeed)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3491
            
            return self._parent._cast(_3491.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3492
            
            return self._parent._cast(_3492.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3493
            
            return self._parent._cast(_3493.AssemblySteadyStateSynchronousResponseAtASpeed)

        @property
        def bearing_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3494
            
            return self._parent._cast(_3494.BearingSteadyStateSynchronousResponseAtASpeed)

        @property
        def belt_drive_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3496
            
            return self._parent._cast(_3496.BeltDriveSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3498
            
            return self._parent._cast(_3498.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3499
            
            return self._parent._cast(_3499.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3500
            
            return self._parent._cast(_3500.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3501
            
            return self._parent._cast(_3501.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3503
            
            return self._parent._cast(_3503.BevelGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3504
            
            return self._parent._cast(_3504.BevelGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def bolted_joint_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3505
            
            return self._parent._cast(_3505.BoltedJointSteadyStateSynchronousResponseAtASpeed)

        @property
        def bolt_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3506
            
            return self._parent._cast(_3506.BoltSteadyStateSynchronousResponseAtASpeed)

        @property
        def clutch_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3508
            
            return self._parent._cast(_3508.ClutchHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def clutch_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3509
            
            return self._parent._cast(_3509.ClutchSteadyStateSynchronousResponseAtASpeed)

        @property
        def component_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3511
            
            return self._parent._cast(_3511.ComponentSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_coupling_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3513
            
            return self._parent._cast(_3513.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_coupling_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3514
            
            return self._parent._cast(_3514.ConceptCouplingSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3516
            
            return self._parent._cast(_3516.ConceptGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3517
            
            return self._parent._cast(_3517.ConceptGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def conical_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3519
            
            return self._parent._cast(_3519.ConicalGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3520
            
            return self._parent._cast(_3520.ConicalGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def connector_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3522
            
            return self._parent._cast(_3522.ConnectorSteadyStateSynchronousResponseAtASpeed)

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3524
            
            return self._parent._cast(_3524.CouplingHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def coupling_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3525
            
            return self._parent._cast(_3525.CouplingSteadyStateSynchronousResponseAtASpeed)

        @property
        def cvt_pulley_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3527
            
            return self._parent._cast(_3527.CVTPulleySteadyStateSynchronousResponseAtASpeed)

        @property
        def cvt_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3528
            
            return self._parent._cast(_3528.CVTSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3529
            
            return self._parent._cast(_3529.CycloidalAssemblySteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_disc_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3532
            
            return self._parent._cast(_3532.CycloidalDiscSteadyStateSynchronousResponseAtASpeed)

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3534
            
            return self._parent._cast(_3534.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def cylindrical_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3535
            
            return self._parent._cast(_3535.CylindricalGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3536
            
            return self._parent._cast(_3536.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def datum_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3537
            
            return self._parent._cast(_3537.DatumSteadyStateSynchronousResponseAtASpeed)

        @property
        def external_cad_model_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3538
            
            return self._parent._cast(_3538.ExternalCADModelSteadyStateSynchronousResponseAtASpeed)

        @property
        def face_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3540
            
            return self._parent._cast(_3540.FaceGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def face_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3541
            
            return self._parent._cast(_3541.FaceGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def fe_part_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3542
            
            return self._parent._cast(_3542.FEPartSteadyStateSynchronousResponseAtASpeed)

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3543
            
            return self._parent._cast(_3543.FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed)

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3545
            
            return self._parent._cast(_3545.GearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3546
            
            return self._parent._cast(_3546.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def guide_dxf_model_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3547
            
            return self._parent._cast(_3547.GuideDxfModelSteadyStateSynchronousResponseAtASpeed)

        @property
        def hypoid_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3549
            
            return self._parent._cast(_3549.HypoidGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def hypoid_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3550
            
            return self._parent._cast(_3550.HypoidGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3553
            
            return self._parent._cast(_3553.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3554
            
            return self._parent._cast(_3554.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3556
            
            return self._parent._cast(_3556.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3557
            
            return self._parent._cast(_3557.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3559
            
            return self._parent._cast(_3559.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3560
            
            return self._parent._cast(_3560.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def mass_disc_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3561
            
            return self._parent._cast(_3561.MassDiscSteadyStateSynchronousResponseAtASpeed)

        @property
        def measurement_component_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3562
            
            return self._parent._cast(_3562.MeasurementComponentSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3563
            
            return self._parent._cast(_3563.MountableComponentSteadyStateSynchronousResponseAtASpeed)

        @property
        def oil_seal_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3564
            
            return self._parent._cast(_3564.OilSealSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3565
            
            return self._parent._cast(_3565.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3567
            
            return self._parent._cast(_3567.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3568
            
            return self._parent._cast(_3568.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed)

        @property
        def planetary_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3570
            
            return self._parent._cast(_3570.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def planet_carrier_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3571
            
            return self._parent._cast(_3571.PlanetCarrierSteadyStateSynchronousResponseAtASpeed)

        @property
        def point_load_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3572
            
            return self._parent._cast(_3572.PointLoadSteadyStateSynchronousResponseAtASpeed)

        @property
        def power_load_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3573
            
            return self._parent._cast(_3573.PowerLoadSteadyStateSynchronousResponseAtASpeed)

        @property
        def pulley_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3574
            
            return self._parent._cast(_3574.PulleySteadyStateSynchronousResponseAtASpeed)

        @property
        def ring_pins_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3575
            
            return self._parent._cast(_3575.RingPinsSteadyStateSynchronousResponseAtASpeed)

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3577
            
            return self._parent._cast(_3577.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed)

        @property
        def rolling_ring_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3579
            
            return self._parent._cast(_3579.RollingRingSteadyStateSynchronousResponseAtASpeed)

        @property
        def root_assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3580
            
            return self._parent._cast(_3580.RootAssemblySteadyStateSynchronousResponseAtASpeed)

        @property
        def shaft_hub_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3581
            
            return self._parent._cast(_3581.ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def shaft_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3582
            
            return self._parent._cast(_3582.ShaftSteadyStateSynchronousResponseAtASpeed)

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3584
            
            return self._parent._cast(_3584.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed)

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3586
            
            return self._parent._cast(_3586.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3587
            
            return self._parent._cast(_3587.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def spring_damper_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3589
            
            return self._parent._cast(_3589.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def spring_damper_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3590
            
            return self._parent._cast(_3590.SpringDamperSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3593
            
            return self._parent._cast(_3593.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3594
            
            return self._parent._cast(_3594.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3596
            
            return self._parent._cast(_3596.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3597
            
            return self._parent._cast(_3597.StraightBevelGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3598
            
            return self._parent._cast(_3598.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3599
            
            return self._parent._cast(_3599.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3600
            
            return self._parent._cast(_3600.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_part_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3601
            
            return self._parent._cast(_3601.SynchroniserPartSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3602
            
            return self._parent._cast(_3602.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3603
            
            return self._parent._cast(_3603.SynchroniserSteadyStateSynchronousResponseAtASpeed)

        @property
        def torque_converter_pump_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3605
            
            return self._parent._cast(_3605.TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed)

        @property
        def torque_converter_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3606
            
            return self._parent._cast(_3606.TorqueConverterSteadyStateSynchronousResponseAtASpeed)

        @property
        def torque_converter_turbine_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3607
            
            return self._parent._cast(_3607.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed)

        @property
        def unbalanced_mass_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3608
            
            return self._parent._cast(_3608.UnbalancedMassSteadyStateSynchronousResponseAtASpeed)

        @property
        def virtual_component_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3609
            
            return self._parent._cast(_3609.VirtualComponentSteadyStateSynchronousResponseAtASpeed)

        @property
        def worm_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3611
            
            return self._parent._cast(_3611.WormGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def worm_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3612
            
            return self._parent._cast(_3612.WormGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3614
            
            return self._parent._cast(_3614.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3615
            
            return self._parent._cast(_3615.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3745
            
            return self._parent._cast(_3745.AbstractAssemblyStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3746
            
            return self._parent._cast(_3746.AbstractShaftOrHousingStabilityAnalysis)

        @property
        def abstract_shaft_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3747
            
            return self._parent._cast(_3747.AbstractShaftStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3750
            
            return self._parent._cast(_3750.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3751
            
            return self._parent._cast(_3751.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3752
            
            return self._parent._cast(_3752.AssemblyStabilityAnalysis)

        @property
        def bearing_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3753
            
            return self._parent._cast(_3753.BearingStabilityAnalysis)

        @property
        def belt_drive_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3755
            
            return self._parent._cast(_3755.BeltDriveStabilityAnalysis)

        @property
        def bevel_differential_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3757
            
            return self._parent._cast(_3757.BevelDifferentialGearSetStabilityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3758
            
            return self._parent._cast(_3758.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3759
            
            return self._parent._cast(_3759.BevelDifferentialPlanetGearStabilityAnalysis)

        @property
        def bevel_differential_sun_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3760
            
            return self._parent._cast(_3760.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def bevel_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3762
            
            return self._parent._cast(_3762.BevelGearSetStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3763
            
            return self._parent._cast(_3763.BevelGearStabilityAnalysis)

        @property
        def bolted_joint_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3764
            
            return self._parent._cast(_3764.BoltedJointStabilityAnalysis)

        @property
        def bolt_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3765
            
            return self._parent._cast(_3765.BoltStabilityAnalysis)

        @property
        def clutch_half_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3767
            
            return self._parent._cast(_3767.ClutchHalfStabilityAnalysis)

        @property
        def clutch_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3768
            
            return self._parent._cast(_3768.ClutchStabilityAnalysis)

        @property
        def component_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3770
            
            return self._parent._cast(_3770.ComponentStabilityAnalysis)

        @property
        def concept_coupling_half_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3772
            
            return self._parent._cast(_3772.ConceptCouplingHalfStabilityAnalysis)

        @property
        def concept_coupling_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3773
            
            return self._parent._cast(_3773.ConceptCouplingStabilityAnalysis)

        @property
        def concept_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3775
            
            return self._parent._cast(_3775.ConceptGearSetStabilityAnalysis)

        @property
        def concept_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3776
            
            return self._parent._cast(_3776.ConceptGearStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3778
            
            return self._parent._cast(_3778.ConicalGearSetStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3779
            
            return self._parent._cast(_3779.ConicalGearStabilityAnalysis)

        @property
        def connector_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3781
            
            return self._parent._cast(_3781.ConnectorStabilityAnalysis)

        @property
        def coupling_half_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3783
            
            return self._parent._cast(_3783.CouplingHalfStabilityAnalysis)

        @property
        def coupling_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3784
            
            return self._parent._cast(_3784.CouplingStabilityAnalysis)

        @property
        def cvt_pulley_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3787
            
            return self._parent._cast(_3787.CVTPulleyStabilityAnalysis)

        @property
        def cvt_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3788
            
            return self._parent._cast(_3788.CVTStabilityAnalysis)

        @property
        def cycloidal_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3789
            
            return self._parent._cast(_3789.CycloidalAssemblyStabilityAnalysis)

        @property
        def cycloidal_disc_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3792
            
            return self._parent._cast(_3792.CycloidalDiscStabilityAnalysis)

        @property
        def cylindrical_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3794
            
            return self._parent._cast(_3794.CylindricalGearSetStabilityAnalysis)

        @property
        def cylindrical_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3795
            
            return self._parent._cast(_3795.CylindricalGearStabilityAnalysis)

        @property
        def cylindrical_planet_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3796
            
            return self._parent._cast(_3796.CylindricalPlanetGearStabilityAnalysis)

        @property
        def datum_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3797
            
            return self._parent._cast(_3797.DatumStabilityAnalysis)

        @property
        def external_cad_model_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3798
            
            return self._parent._cast(_3798.ExternalCADModelStabilityAnalysis)

        @property
        def face_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3800
            
            return self._parent._cast(_3800.FaceGearSetStabilityAnalysis)

        @property
        def face_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3801
            
            return self._parent._cast(_3801.FaceGearStabilityAnalysis)

        @property
        def fe_part_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3802
            
            return self._parent._cast(_3802.FEPartStabilityAnalysis)

        @property
        def flexible_pin_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3803
            
            return self._parent._cast(_3803.FlexiblePinAssemblyStabilityAnalysis)

        @property
        def gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3805
            
            return self._parent._cast(_3805.GearSetStabilityAnalysis)

        @property
        def gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3806
            
            return self._parent._cast(_3806.GearStabilityAnalysis)

        @property
        def guide_dxf_model_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3807
            
            return self._parent._cast(_3807.GuideDxfModelStabilityAnalysis)

        @property
        def hypoid_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3809
            
            return self._parent._cast(_3809.HypoidGearSetStabilityAnalysis)

        @property
        def hypoid_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3810
            
            return self._parent._cast(_3810.HypoidGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3813
            
            return self._parent._cast(_3813.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3814
            
            return self._parent._cast(_3814.KlingelnbergCycloPalloidConicalGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3816
            
            return self._parent._cast(_3816.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3817
            
            return self._parent._cast(_3817.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3819
            
            return self._parent._cast(_3819.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3820
            
            return self._parent._cast(_3820.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis)

        @property
        def mass_disc_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3821
            
            return self._parent._cast(_3821.MassDiscStabilityAnalysis)

        @property
        def measurement_component_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3822
            
            return self._parent._cast(_3822.MeasurementComponentStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3823
            
            return self._parent._cast(_3823.MountableComponentStabilityAnalysis)

        @property
        def oil_seal_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3824
            
            return self._parent._cast(_3824.OilSealStabilityAnalysis)

        @property
        def part_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3825
            
            return self._parent._cast(_3825.PartStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3827
            
            return self._parent._cast(_3827.PartToPartShearCouplingHalfStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3828
            
            return self._parent._cast(_3828.PartToPartShearCouplingStabilityAnalysis)

        @property
        def planetary_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3830
            
            return self._parent._cast(_3830.PlanetaryGearSetStabilityAnalysis)

        @property
        def planet_carrier_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3831
            
            return self._parent._cast(_3831.PlanetCarrierStabilityAnalysis)

        @property
        def point_load_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3832
            
            return self._parent._cast(_3832.PointLoadStabilityAnalysis)

        @property
        def power_load_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3833
            
            return self._parent._cast(_3833.PowerLoadStabilityAnalysis)

        @property
        def pulley_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3834
            
            return self._parent._cast(_3834.PulleyStabilityAnalysis)

        @property
        def ring_pins_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3835
            
            return self._parent._cast(_3835.RingPinsStabilityAnalysis)

        @property
        def rolling_ring_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3837
            
            return self._parent._cast(_3837.RollingRingAssemblyStabilityAnalysis)

        @property
        def rolling_ring_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3839
            
            return self._parent._cast(_3839.RollingRingStabilityAnalysis)

        @property
        def root_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3840
            
            return self._parent._cast(_3840.RootAssemblyStabilityAnalysis)

        @property
        def shaft_hub_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3841
            
            return self._parent._cast(_3841.ShaftHubConnectionStabilityAnalysis)

        @property
        def shaft_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3842
            
            return self._parent._cast(_3842.ShaftStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3844
            
            return self._parent._cast(_3844.SpecialisedAssemblyStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3846
            
            return self._parent._cast(_3846.SpiralBevelGearSetStabilityAnalysis)

        @property
        def spiral_bevel_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3847
            
            return self._parent._cast(_3847.SpiralBevelGearStabilityAnalysis)

        @property
        def spring_damper_half_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3849
            
            return self._parent._cast(_3849.SpringDamperHalfStabilityAnalysis)

        @property
        def spring_damper_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3850
            
            return self._parent._cast(_3850.SpringDamperStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3854
            
            return self._parent._cast(_3854.StraightBevelDiffGearSetStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3855
            
            return self._parent._cast(_3855.StraightBevelDiffGearStabilityAnalysis)

        @property
        def straight_bevel_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3857
            
            return self._parent._cast(_3857.StraightBevelGearSetStabilityAnalysis)

        @property
        def straight_bevel_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3858
            
            return self._parent._cast(_3858.StraightBevelGearStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3859
            
            return self._parent._cast(_3859.StraightBevelPlanetGearStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3860
            
            return self._parent._cast(_3860.StraightBevelSunGearStabilityAnalysis)

        @property
        def synchroniser_half_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3861
            
            return self._parent._cast(_3861.SynchroniserHalfStabilityAnalysis)

        @property
        def synchroniser_part_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3862
            
            return self._parent._cast(_3862.SynchroniserPartStabilityAnalysis)

        @property
        def synchroniser_sleeve_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3863
            
            return self._parent._cast(_3863.SynchroniserSleeveStabilityAnalysis)

        @property
        def synchroniser_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3864
            
            return self._parent._cast(_3864.SynchroniserStabilityAnalysis)

        @property
        def torque_converter_pump_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3866
            
            return self._parent._cast(_3866.TorqueConverterPumpStabilityAnalysis)

        @property
        def torque_converter_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3867
            
            return self._parent._cast(_3867.TorqueConverterStabilityAnalysis)

        @property
        def torque_converter_turbine_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3868
            
            return self._parent._cast(_3868.TorqueConverterTurbineStabilityAnalysis)

        @property
        def unbalanced_mass_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3869
            
            return self._parent._cast(_3869.UnbalancedMassStabilityAnalysis)

        @property
        def virtual_component_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3870
            
            return self._parent._cast(_3870.VirtualComponentStabilityAnalysis)

        @property
        def worm_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3872
            
            return self._parent._cast(_3872.WormGearSetStabilityAnalysis)

        @property
        def worm_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3873
            
            return self._parent._cast(_3873.WormGearStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3875
            
            return self._parent._cast(_3875.ZerolBevelGearSetStabilityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3876
            
            return self._parent._cast(_3876.ZerolBevelGearStabilityAnalysis)

        @property
        def abstract_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4012
            
            return self._parent._cast(_4012.AbstractAssemblyPowerFlow)

        @property
        def abstract_shaft_or_housing_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4013
            
            return self._parent._cast(_4013.AbstractShaftOrHousingPowerFlow)

        @property
        def abstract_shaft_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4014
            
            return self._parent._cast(_4014.AbstractShaftPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4017
            
            return self._parent._cast(_4017.AGMAGleasonConicalGearPowerFlow)

        @property
        def agma_gleason_conical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4018
            
            return self._parent._cast(_4018.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4019
            
            return self._parent._cast(_4019.AssemblyPowerFlow)

        @property
        def bearing_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4020
            
            return self._parent._cast(_4020.BearingPowerFlow)

        @property
        def belt_drive_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4022
            
            return self._parent._cast(_4022.BeltDrivePowerFlow)

        @property
        def bevel_differential_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4024
            
            return self._parent._cast(_4024.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4025
            
            return self._parent._cast(_4025.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4026
            
            return self._parent._cast(_4026.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4027
            
            return self._parent._cast(_4027.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4029
            
            return self._parent._cast(_4029.BevelGearPowerFlow)

        @property
        def bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4030
            
            return self._parent._cast(_4030.BevelGearSetPowerFlow)

        @property
        def bolted_joint_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4031
            
            return self._parent._cast(_4031.BoltedJointPowerFlow)

        @property
        def bolt_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4032
            
            return self._parent._cast(_4032.BoltPowerFlow)

        @property
        def clutch_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4034
            
            return self._parent._cast(_4034.ClutchHalfPowerFlow)

        @property
        def clutch_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4035
            
            return self._parent._cast(_4035.ClutchPowerFlow)

        @property
        def component_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4037
            
            return self._parent._cast(_4037.ComponentPowerFlow)

        @property
        def concept_coupling_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4039
            
            return self._parent._cast(_4039.ConceptCouplingHalfPowerFlow)

        @property
        def concept_coupling_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4040
            
            return self._parent._cast(_4040.ConceptCouplingPowerFlow)

        @property
        def concept_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4042
            
            return self._parent._cast(_4042.ConceptGearPowerFlow)

        @property
        def concept_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4043
            
            return self._parent._cast(_4043.ConceptGearSetPowerFlow)

        @property
        def conical_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4045
            
            return self._parent._cast(_4045.ConicalGearPowerFlow)

        @property
        def conical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4046
            
            return self._parent._cast(_4046.ConicalGearSetPowerFlow)

        @property
        def connector_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4048
            
            return self._parent._cast(_4048.ConnectorPowerFlow)

        @property
        def coupling_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4050
            
            return self._parent._cast(_4050.CouplingHalfPowerFlow)

        @property
        def coupling_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4051
            
            return self._parent._cast(_4051.CouplingPowerFlow)

        @property
        def cvt_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4053
            
            return self._parent._cast(_4053.CVTPowerFlow)

        @property
        def cvt_pulley_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4054
            
            return self._parent._cast(_4054.CVTPulleyPowerFlow)

        @property
        def cycloidal_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4055
            
            return self._parent._cast(_4055.CycloidalAssemblyPowerFlow)

        @property
        def cycloidal_disc_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4058
            
            return self._parent._cast(_4058.CycloidalDiscPowerFlow)

        @property
        def cylindrical_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4061
            
            return self._parent._cast(_4061.CylindricalGearPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4062
            
            return self._parent._cast(_4062.CylindricalGearSetPowerFlow)

        @property
        def cylindrical_planet_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4063
            
            return self._parent._cast(_4063.CylindricalPlanetGearPowerFlow)

        @property
        def datum_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4064
            
            return self._parent._cast(_4064.DatumPowerFlow)

        @property
        def external_cad_model_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4065
            
            return self._parent._cast(_4065.ExternalCADModelPowerFlow)

        @property
        def face_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4067
            
            return self._parent._cast(_4067.FaceGearPowerFlow)

        @property
        def face_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4068
            
            return self._parent._cast(_4068.FaceGearSetPowerFlow)

        @property
        def fe_part_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4069
            
            return self._parent._cast(_4069.FEPartPowerFlow)

        @property
        def flexible_pin_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4070
            
            return self._parent._cast(_4070.FlexiblePinAssemblyPowerFlow)

        @property
        def gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4072
            
            return self._parent._cast(_4072.GearPowerFlow)

        @property
        def gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4073
            
            return self._parent._cast(_4073.GearSetPowerFlow)

        @property
        def guide_dxf_model_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4074
            
            return self._parent._cast(_4074.GuideDxfModelPowerFlow)

        @property
        def hypoid_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4076
            
            return self._parent._cast(_4076.HypoidGearPowerFlow)

        @property
        def hypoid_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4077
            
            return self._parent._cast(_4077.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4080
            
            return self._parent._cast(_4080.KlingelnbergCycloPalloidConicalGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4081
            
            return self._parent._cast(_4081.KlingelnbergCycloPalloidConicalGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4083
            
            return self._parent._cast(_4083.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4084
            
            return self._parent._cast(_4084.KlingelnbergCycloPalloidHypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4086
            
            return self._parent._cast(_4086.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4087
            
            return self._parent._cast(_4087.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow)

        @property
        def mass_disc_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4088
            
            return self._parent._cast(_4088.MassDiscPowerFlow)

        @property
        def measurement_component_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4089
            
            return self._parent._cast(_4089.MeasurementComponentPowerFlow)

        @property
        def mountable_component_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4090
            
            return self._parent._cast(_4090.MountableComponentPowerFlow)

        @property
        def oil_seal_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4091
            
            return self._parent._cast(_4091.OilSealPowerFlow)

        @property
        def part_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4092
            
            return self._parent._cast(_4092.PartPowerFlow)

        @property
        def part_to_part_shear_coupling_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4094
            
            return self._parent._cast(_4094.PartToPartShearCouplingHalfPowerFlow)

        @property
        def part_to_part_shear_coupling_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4095
            
            return self._parent._cast(_4095.PartToPartShearCouplingPowerFlow)

        @property
        def planetary_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4097
            
            return self._parent._cast(_4097.PlanetaryGearSetPowerFlow)

        @property
        def planet_carrier_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4098
            
            return self._parent._cast(_4098.PlanetCarrierPowerFlow)

        @property
        def point_load_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4099
            
            return self._parent._cast(_4099.PointLoadPowerFlow)

        @property
        def power_load_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4102
            
            return self._parent._cast(_4102.PowerLoadPowerFlow)

        @property
        def pulley_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4103
            
            return self._parent._cast(_4103.PulleyPowerFlow)

        @property
        def ring_pins_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4104
            
            return self._parent._cast(_4104.RingPinsPowerFlow)

        @property
        def rolling_ring_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4106
            
            return self._parent._cast(_4106.RollingRingAssemblyPowerFlow)

        @property
        def rolling_ring_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4108
            
            return self._parent._cast(_4108.RollingRingPowerFlow)

        @property
        def root_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4109
            
            return self._parent._cast(_4109.RootAssemblyPowerFlow)

        @property
        def shaft_hub_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4110
            
            return self._parent._cast(_4110.ShaftHubConnectionPowerFlow)

        @property
        def shaft_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4111
            
            return self._parent._cast(_4111.ShaftPowerFlow)

        @property
        def specialised_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4113
            
            return self._parent._cast(_4113.SpecialisedAssemblyPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4115
            
            return self._parent._cast(_4115.SpiralBevelGearPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4116
            
            return self._parent._cast(_4116.SpiralBevelGearSetPowerFlow)

        @property
        def spring_damper_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4118
            
            return self._parent._cast(_4118.SpringDamperHalfPowerFlow)

        @property
        def spring_damper_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4119
            
            return self._parent._cast(_4119.SpringDamperPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4121
            
            return self._parent._cast(_4121.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4122
            
            return self._parent._cast(_4122.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4124
            
            return self._parent._cast(_4124.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4125
            
            return self._parent._cast(_4125.StraightBevelGearSetPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4126
            
            return self._parent._cast(_4126.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4127
            
            return self._parent._cast(_4127.StraightBevelSunGearPowerFlow)

        @property
        def synchroniser_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4128
            
            return self._parent._cast(_4128.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_part_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4129
            
            return self._parent._cast(_4129.SynchroniserPartPowerFlow)

        @property
        def synchroniser_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4130
            
            return self._parent._cast(_4130.SynchroniserPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4131
            
            return self._parent._cast(_4131.SynchroniserSleevePowerFlow)

        @property
        def torque_converter_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4134
            
            return self._parent._cast(_4134.TorqueConverterPowerFlow)

        @property
        def torque_converter_pump_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4135
            
            return self._parent._cast(_4135.TorqueConverterPumpPowerFlow)

        @property
        def torque_converter_turbine_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4136
            
            return self._parent._cast(_4136.TorqueConverterTurbinePowerFlow)

        @property
        def unbalanced_mass_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4137
            
            return self._parent._cast(_4137.UnbalancedMassPowerFlow)

        @property
        def virtual_component_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4138
            
            return self._parent._cast(_4138.VirtualComponentPowerFlow)

        @property
        def worm_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4140
            
            return self._parent._cast(_4140.WormGearPowerFlow)

        @property
        def worm_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4141
            
            return self._parent._cast(_4141.WormGearSetPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4143
            
            return self._parent._cast(_4143.ZerolBevelGearPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4144
            
            return self._parent._cast(_4144.ZerolBevelGearSetPowerFlow)

        @property
        def abstract_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4274
            
            return self._parent._cast(_4274.AbstractAssemblyParametricStudyTool)

        @property
        def abstract_shaft_or_housing_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4275
            
            return self._parent._cast(_4275.AbstractShaftOrHousingParametricStudyTool)

        @property
        def abstract_shaft_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4276
            
            return self._parent._cast(_4276.AbstractShaftParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4279
            
            return self._parent._cast(_4279.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4280
            
            return self._parent._cast(_4280.AGMAGleasonConicalGearSetParametricStudyTool)

        @property
        def assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4281
            
            return self._parent._cast(_4281.AssemblyParametricStudyTool)

        @property
        def bearing_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4282
            
            return self._parent._cast(_4282.BearingParametricStudyTool)

        @property
        def belt_drive_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4284
            
            return self._parent._cast(_4284.BeltDriveParametricStudyTool)

        @property
        def bevel_differential_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4286
            
            return self._parent._cast(_4286.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_differential_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4287
            
            return self._parent._cast(_4287.BevelDifferentialGearSetParametricStudyTool)

        @property
        def bevel_differential_planet_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4288
            
            return self._parent._cast(_4288.BevelDifferentialPlanetGearParametricStudyTool)

        @property
        def bevel_differential_sun_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4289
            
            return self._parent._cast(_4289.BevelDifferentialSunGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4291
            
            return self._parent._cast(_4291.BevelGearParametricStudyTool)

        @property
        def bevel_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4292
            
            return self._parent._cast(_4292.BevelGearSetParametricStudyTool)

        @property
        def bolted_joint_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4293
            
            return self._parent._cast(_4293.BoltedJointParametricStudyTool)

        @property
        def bolt_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4294
            
            return self._parent._cast(_4294.BoltParametricStudyTool)

        @property
        def clutch_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4296
            
            return self._parent._cast(_4296.ClutchHalfParametricStudyTool)

        @property
        def clutch_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4297
            
            return self._parent._cast(_4297.ClutchParametricStudyTool)

        @property
        def component_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4299
            
            return self._parent._cast(_4299.ComponentParametricStudyTool)

        @property
        def concept_coupling_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4301
            
            return self._parent._cast(_4301.ConceptCouplingHalfParametricStudyTool)

        @property
        def concept_coupling_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4302
            
            return self._parent._cast(_4302.ConceptCouplingParametricStudyTool)

        @property
        def concept_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4304
            
            return self._parent._cast(_4304.ConceptGearParametricStudyTool)

        @property
        def concept_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4305
            
            return self._parent._cast(_4305.ConceptGearSetParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4307
            
            return self._parent._cast(_4307.ConicalGearParametricStudyTool)

        @property
        def conical_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4308
            
            return self._parent._cast(_4308.ConicalGearSetParametricStudyTool)

        @property
        def connector_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4310
            
            return self._parent._cast(_4310.ConnectorParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4312
            
            return self._parent._cast(_4312.CouplingHalfParametricStudyTool)

        @property
        def coupling_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4313
            
            return self._parent._cast(_4313.CouplingParametricStudyTool)

        @property
        def cvt_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4315
            
            return self._parent._cast(_4315.CVTParametricStudyTool)

        @property
        def cvt_pulley_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4316
            
            return self._parent._cast(_4316.CVTPulleyParametricStudyTool)

        @property
        def cycloidal_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4317
            
            return self._parent._cast(_4317.CycloidalAssemblyParametricStudyTool)

        @property
        def cycloidal_disc_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4319
            
            return self._parent._cast(_4319.CycloidalDiscParametricStudyTool)

        @property
        def cylindrical_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4322
            
            return self._parent._cast(_4322.CylindricalGearParametricStudyTool)

        @property
        def cylindrical_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4323
            
            return self._parent._cast(_4323.CylindricalGearSetParametricStudyTool)

        @property
        def cylindrical_planet_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4324
            
            return self._parent._cast(_4324.CylindricalPlanetGearParametricStudyTool)

        @property
        def datum_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4325
            
            return self._parent._cast(_4325.DatumParametricStudyTool)

        @property
        def external_cad_model_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4333
            
            return self._parent._cast(_4333.ExternalCADModelParametricStudyTool)

        @property
        def face_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4335
            
            return self._parent._cast(_4335.FaceGearParametricStudyTool)

        @property
        def face_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4336
            
            return self._parent._cast(_4336.FaceGearSetParametricStudyTool)

        @property
        def fe_part_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4337
            
            return self._parent._cast(_4337.FEPartParametricStudyTool)

        @property
        def flexible_pin_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4338
            
            return self._parent._cast(_4338.FlexiblePinAssemblyParametricStudyTool)

        @property
        def gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4340
            
            return self._parent._cast(_4340.GearParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4341
            
            return self._parent._cast(_4341.GearSetParametricStudyTool)

        @property
        def guide_dxf_model_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4342
            
            return self._parent._cast(_4342.GuideDxfModelParametricStudyTool)

        @property
        def hypoid_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4344
            
            return self._parent._cast(_4344.HypoidGearParametricStudyTool)

        @property
        def hypoid_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4345
            
            return self._parent._cast(_4345.HypoidGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4348
            
            return self._parent._cast(_4348.KlingelnbergCycloPalloidConicalGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4349
            
            return self._parent._cast(_4349.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4351
            
            return self._parent._cast(_4351.KlingelnbergCycloPalloidHypoidGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4352
            
            return self._parent._cast(_4352.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4354
            
            return self._parent._cast(_4354.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4355
            
            return self._parent._cast(_4355.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool)

        @property
        def mass_disc_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4356
            
            return self._parent._cast(_4356.MassDiscParametricStudyTool)

        @property
        def measurement_component_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4357
            
            return self._parent._cast(_4357.MeasurementComponentParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4359
            
            return self._parent._cast(_4359.MountableComponentParametricStudyTool)

        @property
        def oil_seal_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4360
            
            return self._parent._cast(_4360.OilSealParametricStudyTool)

        @property
        def part_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4371
            
            return self._parent._cast(_4371.PartParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4373
            
            return self._parent._cast(_4373.PartToPartShearCouplingHalfParametricStudyTool)

        @property
        def part_to_part_shear_coupling_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4374
            
            return self._parent._cast(_4374.PartToPartShearCouplingParametricStudyTool)

        @property
        def planetary_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4376
            
            return self._parent._cast(_4376.PlanetaryGearSetParametricStudyTool)

        @property
        def planet_carrier_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4377
            
            return self._parent._cast(_4377.PlanetCarrierParametricStudyTool)

        @property
        def point_load_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4378
            
            return self._parent._cast(_4378.PointLoadParametricStudyTool)

        @property
        def power_load_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4379
            
            return self._parent._cast(_4379.PowerLoadParametricStudyTool)

        @property
        def pulley_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4380
            
            return self._parent._cast(_4380.PulleyParametricStudyTool)

        @property
        def ring_pins_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4381
            
            return self._parent._cast(_4381.RingPinsParametricStudyTool)

        @property
        def rolling_ring_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4383
            
            return self._parent._cast(_4383.RollingRingAssemblyParametricStudyTool)

        @property
        def rolling_ring_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4385
            
            return self._parent._cast(_4385.RollingRingParametricStudyTool)

        @property
        def root_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4386
            
            return self._parent._cast(_4386.RootAssemblyParametricStudyTool)

        @property
        def shaft_hub_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4387
            
            return self._parent._cast(_4387.ShaftHubConnectionParametricStudyTool)

        @property
        def shaft_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4388
            
            return self._parent._cast(_4388.ShaftParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4390
            
            return self._parent._cast(_4390.SpecialisedAssemblyParametricStudyTool)

        @property
        def spiral_bevel_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4392
            
            return self._parent._cast(_4392.SpiralBevelGearParametricStudyTool)

        @property
        def spiral_bevel_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4393
            
            return self._parent._cast(_4393.SpiralBevelGearSetParametricStudyTool)

        @property
        def spring_damper_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4395
            
            return self._parent._cast(_4395.SpringDamperHalfParametricStudyTool)

        @property
        def spring_damper_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4396
            
            return self._parent._cast(_4396.SpringDamperParametricStudyTool)

        @property
        def straight_bevel_diff_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4398
            
            return self._parent._cast(_4398.StraightBevelDiffGearParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4399
            
            return self._parent._cast(_4399.StraightBevelDiffGearSetParametricStudyTool)

        @property
        def straight_bevel_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4401
            
            return self._parent._cast(_4401.StraightBevelGearParametricStudyTool)

        @property
        def straight_bevel_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4402
            
            return self._parent._cast(_4402.StraightBevelGearSetParametricStudyTool)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4403
            
            return self._parent._cast(_4403.StraightBevelPlanetGearParametricStudyTool)

        @property
        def straight_bevel_sun_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4404
            
            return self._parent._cast(_4404.StraightBevelSunGearParametricStudyTool)

        @property
        def synchroniser_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4405
            
            return self._parent._cast(_4405.SynchroniserHalfParametricStudyTool)

        @property
        def synchroniser_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4406
            
            return self._parent._cast(_4406.SynchroniserParametricStudyTool)

        @property
        def synchroniser_part_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4407
            
            return self._parent._cast(_4407.SynchroniserPartParametricStudyTool)

        @property
        def synchroniser_sleeve_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4408
            
            return self._parent._cast(_4408.SynchroniserSleeveParametricStudyTool)

        @property
        def torque_converter_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4410
            
            return self._parent._cast(_4410.TorqueConverterParametricStudyTool)

        @property
        def torque_converter_pump_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4411
            
            return self._parent._cast(_4411.TorqueConverterPumpParametricStudyTool)

        @property
        def torque_converter_turbine_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4412
            
            return self._parent._cast(_4412.TorqueConverterTurbineParametricStudyTool)

        @property
        def unbalanced_mass_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4413
            
            return self._parent._cast(_4413.UnbalancedMassParametricStudyTool)

        @property
        def virtual_component_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4414
            
            return self._parent._cast(_4414.VirtualComponentParametricStudyTool)

        @property
        def worm_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4416
            
            return self._parent._cast(_4416.WormGearParametricStudyTool)

        @property
        def worm_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4417
            
            return self._parent._cast(_4417.WormGearSetParametricStudyTool)

        @property
        def zerol_bevel_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4419
            
            return self._parent._cast(_4419.ZerolBevelGearParametricStudyTool)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4420
            
            return self._parent._cast(_4420.ZerolBevelGearSetParametricStudyTool)

        @property
        def abstract_assembly_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4550
            
            return self._parent._cast(_4550.AbstractAssemblyModalAnalysis)

        @property
        def abstract_shaft_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4551
            
            return self._parent._cast(_4551.AbstractShaftModalAnalysis)

        @property
        def abstract_shaft_or_housing_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4552
            
            return self._parent._cast(_4552.AbstractShaftOrHousingModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4555
            
            return self._parent._cast(_4555.AGMAGleasonConicalGearModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4556
            
            return self._parent._cast(_4556.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def assembly_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4557
            
            return self._parent._cast(_4557.AssemblyModalAnalysis)

        @property
        def bearing_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4558
            
            return self._parent._cast(_4558.BearingModalAnalysis)

        @property
        def belt_drive_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4560
            
            return self._parent._cast(_4560.BeltDriveModalAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4562
            
            return self._parent._cast(_4562.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4563
            
            return self._parent._cast(_4563.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4564
            
            return self._parent._cast(_4564.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4565
            
            return self._parent._cast(_4565.BevelDifferentialSunGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4567
            
            return self._parent._cast(_4567.BevelGearModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4568
            
            return self._parent._cast(_4568.BevelGearSetModalAnalysis)

        @property
        def bolted_joint_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4569
            
            return self._parent._cast(_4569.BoltedJointModalAnalysis)

        @property
        def bolt_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4570
            
            return self._parent._cast(_4570.BoltModalAnalysis)

        @property
        def clutch_half_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4572
            
            return self._parent._cast(_4572.ClutchHalfModalAnalysis)

        @property
        def clutch_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4573
            
            return self._parent._cast(_4573.ClutchModalAnalysis)

        @property
        def component_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4575
            
            return self._parent._cast(_4575.ComponentModalAnalysis)

        @property
        def concept_coupling_half_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4577
            
            return self._parent._cast(_4577.ConceptCouplingHalfModalAnalysis)

        @property
        def concept_coupling_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4578
            
            return self._parent._cast(_4578.ConceptCouplingModalAnalysis)

        @property
        def concept_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4580
            
            return self._parent._cast(_4580.ConceptGearModalAnalysis)

        @property
        def concept_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4581
            
            return self._parent._cast(_4581.ConceptGearSetModalAnalysis)

        @property
        def conical_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4583
            
            return self._parent._cast(_4583.ConicalGearModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4584
            
            return self._parent._cast(_4584.ConicalGearSetModalAnalysis)

        @property
        def connector_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4586
            
            return self._parent._cast(_4586.ConnectorModalAnalysis)

        @property
        def coupling_half_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4589
            
            return self._parent._cast(_4589.CouplingHalfModalAnalysis)

        @property
        def coupling_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4590
            
            return self._parent._cast(_4590.CouplingModalAnalysis)

        @property
        def cvt_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4592
            
            return self._parent._cast(_4592.CVTModalAnalysis)

        @property
        def cvt_pulley_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593
            
            return self._parent._cast(_4593.CVTPulleyModalAnalysis)

        @property
        def cycloidal_assembly_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4594
            
            return self._parent._cast(_4594.CycloidalAssemblyModalAnalysis)

        @property
        def cycloidal_disc_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4596
            
            return self._parent._cast(_4596.CycloidalDiscModalAnalysis)

        @property
        def cylindrical_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4599
            
            return self._parent._cast(_4599.CylindricalGearModalAnalysis)

        @property
        def cylindrical_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4600
            
            return self._parent._cast(_4600.CylindricalGearSetModalAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4601
            
            return self._parent._cast(_4601.CylindricalPlanetGearModalAnalysis)

        @property
        def datum_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4602
            
            return self._parent._cast(_4602.DatumModalAnalysis)

        @property
        def external_cad_model_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605
            
            return self._parent._cast(_4605.ExternalCADModelModalAnalysis)

        @property
        def face_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4607
            
            return self._parent._cast(_4607.FaceGearModalAnalysis)

        @property
        def face_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4608
            
            return self._parent._cast(_4608.FaceGearSetModalAnalysis)

        @property
        def fe_part_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4609
            
            return self._parent._cast(_4609.FEPartModalAnalysis)

        @property
        def flexible_pin_assembly_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4610
            
            return self._parent._cast(_4610.FlexiblePinAssemblyModalAnalysis)

        @property
        def gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4613
            
            return self._parent._cast(_4613.GearModalAnalysis)

        @property
        def gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4614
            
            return self._parent._cast(_4614.GearSetModalAnalysis)

        @property
        def guide_dxf_model_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4615
            
            return self._parent._cast(_4615.GuideDxfModelModalAnalysis)

        @property
        def hypoid_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4617
            
            return self._parent._cast(_4617.HypoidGearModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618
            
            return self._parent._cast(_4618.HypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4621
            
            return self._parent._cast(_4621.KlingelnbergCycloPalloidConicalGearModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4622
            
            return self._parent._cast(_4622.KlingelnbergCycloPalloidConicalGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4624
            
            return self._parent._cast(_4624.KlingelnbergCycloPalloidHypoidGearModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4625
            
            return self._parent._cast(_4625.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4627
            
            return self._parent._cast(_4627.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4628
            
            return self._parent._cast(_4628.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis)

        @property
        def mass_disc_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4629
            
            return self._parent._cast(_4629.MassDiscModalAnalysis)

        @property
        def measurement_component_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4630
            
            return self._parent._cast(_4630.MeasurementComponentModalAnalysis)

        @property
        def mountable_component_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4634
            
            return self._parent._cast(_4634.MountableComponentModalAnalysis)

        @property
        def oil_seal_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636
            
            return self._parent._cast(_4636.OilSealModalAnalysis)

        @property
        def part_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4638
            
            return self._parent._cast(_4638.PartModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4640
            
            return self._parent._cast(_4640.PartToPartShearCouplingHalfModalAnalysis)

        @property
        def part_to_part_shear_coupling_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4641
            
            return self._parent._cast(_4641.PartToPartShearCouplingModalAnalysis)

        @property
        def planetary_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4643
            
            return self._parent._cast(_4643.PlanetaryGearSetModalAnalysis)

        @property
        def planet_carrier_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644
            
            return self._parent._cast(_4644.PlanetCarrierModalAnalysis)

        @property
        def point_load_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4645
            
            return self._parent._cast(_4645.PointLoadModalAnalysis)

        @property
        def power_load_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646
            
            return self._parent._cast(_4646.PowerLoadModalAnalysis)

        @property
        def pulley_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4647
            
            return self._parent._cast(_4647.PulleyModalAnalysis)

        @property
        def ring_pins_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4648
            
            return self._parent._cast(_4648.RingPinsModalAnalysis)

        @property
        def rolling_ring_assembly_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4650
            
            return self._parent._cast(_4650.RollingRingAssemblyModalAnalysis)

        @property
        def rolling_ring_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4652
            
            return self._parent._cast(_4652.RollingRingModalAnalysis)

        @property
        def root_assembly_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4653
            
            return self._parent._cast(_4653.RootAssemblyModalAnalysis)

        @property
        def shaft_hub_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4654
            
            return self._parent._cast(_4654.ShaftHubConnectionModalAnalysis)

        @property
        def shaft_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4655
            
            return self._parent._cast(_4655.ShaftModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658
            
            return self._parent._cast(_4658.SpecialisedAssemblyModalAnalysis)

        @property
        def spiral_bevel_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660
            
            return self._parent._cast(_4660.SpiralBevelGearModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661
            
            return self._parent._cast(_4661.SpiralBevelGearSetModalAnalysis)

        @property
        def spring_damper_half_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4663
            
            return self._parent._cast(_4663.SpringDamperHalfModalAnalysis)

        @property
        def spring_damper_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4664
            
            return self._parent._cast(_4664.SpringDamperModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4666
            
            return self._parent._cast(_4666.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4667
            
            return self._parent._cast(_4667.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4669
            
            return self._parent._cast(_4669.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670
            
            return self._parent._cast(_4670.StraightBevelGearSetModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4671
            
            return self._parent._cast(_4671.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4672
            
            return self._parent._cast(_4672.StraightBevelSunGearModalAnalysis)

        @property
        def synchroniser_half_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4673
            
            return self._parent._cast(_4673.SynchroniserHalfModalAnalysis)

        @property
        def synchroniser_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4674
            
            return self._parent._cast(_4674.SynchroniserModalAnalysis)

        @property
        def synchroniser_part_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4675
            
            return self._parent._cast(_4675.SynchroniserPartModalAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4676
            
            return self._parent._cast(_4676.SynchroniserSleeveModalAnalysis)

        @property
        def torque_converter_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4678
            
            return self._parent._cast(_4678.TorqueConverterModalAnalysis)

        @property
        def torque_converter_pump_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679
            
            return self._parent._cast(_4679.TorqueConverterPumpModalAnalysis)

        @property
        def torque_converter_turbine_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4680
            
            return self._parent._cast(_4680.TorqueConverterTurbineModalAnalysis)

        @property
        def unbalanced_mass_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681
            
            return self._parent._cast(_4681.UnbalancedMassModalAnalysis)

        @property
        def virtual_component_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4682
            
            return self._parent._cast(_4682.VirtualComponentModalAnalysis)

        @property
        def worm_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4687
            
            return self._parent._cast(_4687.WormGearModalAnalysis)

        @property
        def worm_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4688
            
            return self._parent._cast(_4688.WormGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690
            
            return self._parent._cast(_4690.ZerolBevelGearModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4691
            
            return self._parent._cast(_4691.ZerolBevelGearSetModalAnalysis)

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4833
            
            return self._parent._cast(_4833.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4834
            
            return self._parent._cast(_4834.AbstractShaftModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4835
            
            return self._parent._cast(_4835.AbstractShaftOrHousingModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4838
            
            return self._parent._cast(_4838.AGMAGleasonConicalGearModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4839
            
            return self._parent._cast(_4839.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness)

        @property
        def assembly_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4840
            
            return self._parent._cast(_4840.AssemblyModalAnalysisAtAStiffness)

        @property
        def bearing_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4841
            
            return self._parent._cast(_4841.BearingModalAnalysisAtAStiffness)

        @property
        def belt_drive_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4843
            
            return self._parent._cast(_4843.BeltDriveModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4845
            
            return self._parent._cast(_4845.BevelDifferentialGearModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4846
            
            return self._parent._cast(_4846.BevelDifferentialGearSetModalAnalysisAtAStiffness)

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4847
            
            return self._parent._cast(_4847.BevelDifferentialPlanetGearModalAnalysisAtAStiffness)

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4848
            
            return self._parent._cast(_4848.BevelDifferentialSunGearModalAnalysisAtAStiffness)

        @property
        def bevel_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4850
            
            return self._parent._cast(_4850.BevelGearModalAnalysisAtAStiffness)

        @property
        def bevel_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4851
            
            return self._parent._cast(_4851.BevelGearSetModalAnalysisAtAStiffness)

        @property
        def bolted_joint_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4852
            
            return self._parent._cast(_4852.BoltedJointModalAnalysisAtAStiffness)

        @property
        def bolt_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4853
            
            return self._parent._cast(_4853.BoltModalAnalysisAtAStiffness)

        @property
        def clutch_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4855
            
            return self._parent._cast(_4855.ClutchHalfModalAnalysisAtAStiffness)

        @property
        def clutch_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4856
            
            return self._parent._cast(_4856.ClutchModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4858
            
            return self._parent._cast(_4858.ComponentModalAnalysisAtAStiffness)

        @property
        def concept_coupling_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4860
            
            return self._parent._cast(_4860.ConceptCouplingHalfModalAnalysisAtAStiffness)

        @property
        def concept_coupling_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4861
            
            return self._parent._cast(_4861.ConceptCouplingModalAnalysisAtAStiffness)

        @property
        def concept_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4863
            
            return self._parent._cast(_4863.ConceptGearModalAnalysisAtAStiffness)

        @property
        def concept_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4864
            
            return self._parent._cast(_4864.ConceptGearSetModalAnalysisAtAStiffness)

        @property
        def conical_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4866
            
            return self._parent._cast(_4866.ConicalGearModalAnalysisAtAStiffness)

        @property
        def conical_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4867
            
            return self._parent._cast(_4867.ConicalGearSetModalAnalysisAtAStiffness)

        @property
        def connector_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4869
            
            return self._parent._cast(_4869.ConnectorModalAnalysisAtAStiffness)

        @property
        def coupling_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4871
            
            return self._parent._cast(_4871.CouplingHalfModalAnalysisAtAStiffness)

        @property
        def coupling_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4872
            
            return self._parent._cast(_4872.CouplingModalAnalysisAtAStiffness)

        @property
        def cvt_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4874
            
            return self._parent._cast(_4874.CVTModalAnalysisAtAStiffness)

        @property
        def cvt_pulley_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4875
            
            return self._parent._cast(_4875.CVTPulleyModalAnalysisAtAStiffness)

        @property
        def cycloidal_assembly_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4876
            
            return self._parent._cast(_4876.CycloidalAssemblyModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4878
            
            return self._parent._cast(_4878.CycloidalDiscModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4881
            
            return self._parent._cast(_4881.CylindricalGearModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4882
            
            return self._parent._cast(_4882.CylindricalGearSetModalAnalysisAtAStiffness)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4883
            
            return self._parent._cast(_4883.CylindricalPlanetGearModalAnalysisAtAStiffness)

        @property
        def datum_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4884
            
            return self._parent._cast(_4884.DatumModalAnalysisAtAStiffness)

        @property
        def external_cad_model_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4886
            
            return self._parent._cast(_4886.ExternalCADModelModalAnalysisAtAStiffness)

        @property
        def face_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4888
            
            return self._parent._cast(_4888.FaceGearModalAnalysisAtAStiffness)

        @property
        def face_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4889
            
            return self._parent._cast(_4889.FaceGearSetModalAnalysisAtAStiffness)

        @property
        def fe_part_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4890
            
            return self._parent._cast(_4890.FEPartModalAnalysisAtAStiffness)

        @property
        def flexible_pin_assembly_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4891
            
            return self._parent._cast(_4891.FlexiblePinAssemblyModalAnalysisAtAStiffness)

        @property
        def gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4893
            
            return self._parent._cast(_4893.GearModalAnalysisAtAStiffness)

        @property
        def gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4894
            
            return self._parent._cast(_4894.GearSetModalAnalysisAtAStiffness)

        @property
        def guide_dxf_model_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4895
            
            return self._parent._cast(_4895.GuideDxfModelModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4897
            
            return self._parent._cast(_4897.HypoidGearModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4898
            
            return self._parent._cast(_4898.HypoidGearSetModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4901
            
            return self._parent._cast(_4901.KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4902
            
            return self._parent._cast(_4902.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4904
            
            return self._parent._cast(_4904.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4905
            
            return self._parent._cast(_4905.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4907
            
            return self._parent._cast(_4907.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4908
            
            return self._parent._cast(_4908.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness)

        @property
        def mass_disc_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4909
            
            return self._parent._cast(_4909.MassDiscModalAnalysisAtAStiffness)

        @property
        def measurement_component_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4910
            
            return self._parent._cast(_4910.MeasurementComponentModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4911
            
            return self._parent._cast(_4911.MountableComponentModalAnalysisAtAStiffness)

        @property
        def oil_seal_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4912
            
            return self._parent._cast(_4912.OilSealModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4913
            
            return self._parent._cast(_4913.PartModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4915
            
            return self._parent._cast(_4915.PartToPartShearCouplingHalfModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4916
            
            return self._parent._cast(_4916.PartToPartShearCouplingModalAnalysisAtAStiffness)

        @property
        def planetary_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4918
            
            return self._parent._cast(_4918.PlanetaryGearSetModalAnalysisAtAStiffness)

        @property
        def planet_carrier_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4919
            
            return self._parent._cast(_4919.PlanetCarrierModalAnalysisAtAStiffness)

        @property
        def point_load_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4920
            
            return self._parent._cast(_4920.PointLoadModalAnalysisAtAStiffness)

        @property
        def power_load_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4921
            
            return self._parent._cast(_4921.PowerLoadModalAnalysisAtAStiffness)

        @property
        def pulley_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4922
            
            return self._parent._cast(_4922.PulleyModalAnalysisAtAStiffness)

        @property
        def ring_pins_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4923
            
            return self._parent._cast(_4923.RingPinsModalAnalysisAtAStiffness)

        @property
        def rolling_ring_assembly_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4925
            
            return self._parent._cast(_4925.RollingRingAssemblyModalAnalysisAtAStiffness)

        @property
        def rolling_ring_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4927
            
            return self._parent._cast(_4927.RollingRingModalAnalysisAtAStiffness)

        @property
        def root_assembly_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4928
            
            return self._parent._cast(_4928.RootAssemblyModalAnalysisAtAStiffness)

        @property
        def shaft_hub_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4929
            
            return self._parent._cast(_4929.ShaftHubConnectionModalAnalysisAtAStiffness)

        @property
        def shaft_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4930
            
            return self._parent._cast(_4930.ShaftModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4932
            
            return self._parent._cast(_4932.SpecialisedAssemblyModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4934
            
            return self._parent._cast(_4934.SpiralBevelGearModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4935
            
            return self._parent._cast(_4935.SpiralBevelGearSetModalAnalysisAtAStiffness)

        @property
        def spring_damper_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4937
            
            return self._parent._cast(_4937.SpringDamperHalfModalAnalysisAtAStiffness)

        @property
        def spring_damper_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4938
            
            return self._parent._cast(_4938.SpringDamperModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4940
            
            return self._parent._cast(_4940.StraightBevelDiffGearModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4941
            
            return self._parent._cast(_4941.StraightBevelDiffGearSetModalAnalysisAtAStiffness)

        @property
        def straight_bevel_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4943
            
            return self._parent._cast(_4943.StraightBevelGearModalAnalysisAtAStiffness)

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4944
            
            return self._parent._cast(_4944.StraightBevelGearSetModalAnalysisAtAStiffness)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4945
            
            return self._parent._cast(_4945.StraightBevelPlanetGearModalAnalysisAtAStiffness)

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4946
            
            return self._parent._cast(_4946.StraightBevelSunGearModalAnalysisAtAStiffness)

        @property
        def synchroniser_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4947
            
            return self._parent._cast(_4947.SynchroniserHalfModalAnalysisAtAStiffness)

        @property
        def synchroniser_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4948
            
            return self._parent._cast(_4948.SynchroniserModalAnalysisAtAStiffness)

        @property
        def synchroniser_part_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4949
            
            return self._parent._cast(_4949.SynchroniserPartModalAnalysisAtAStiffness)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4950
            
            return self._parent._cast(_4950.SynchroniserSleeveModalAnalysisAtAStiffness)

        @property
        def torque_converter_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4952
            
            return self._parent._cast(_4952.TorqueConverterModalAnalysisAtAStiffness)

        @property
        def torque_converter_pump_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4953
            
            return self._parent._cast(_4953.TorqueConverterPumpModalAnalysisAtAStiffness)

        @property
        def torque_converter_turbine_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4954
            
            return self._parent._cast(_4954.TorqueConverterTurbineModalAnalysisAtAStiffness)

        @property
        def unbalanced_mass_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4955
            
            return self._parent._cast(_4955.UnbalancedMassModalAnalysisAtAStiffness)

        @property
        def virtual_component_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4956
            
            return self._parent._cast(_4956.VirtualComponentModalAnalysisAtAStiffness)

        @property
        def worm_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4958
            
            return self._parent._cast(_4958.WormGearModalAnalysisAtAStiffness)

        @property
        def worm_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4959
            
            return self._parent._cast(_4959.WormGearSetModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4961
            
            return self._parent._cast(_4961.ZerolBevelGearModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4962
            
            return self._parent._cast(_4962.ZerolBevelGearSetModalAnalysisAtAStiffness)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5092
            
            return self._parent._cast(_5092.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_shaft_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5093
            
            return self._parent._cast(_5093.AbstractShaftModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5094
            
            return self._parent._cast(_5094.AbstractShaftOrHousingModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5097
            
            return self._parent._cast(_5097.AGMAGleasonConicalGearModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5098
            
            return self._parent._cast(_5098.AGMAGleasonConicalGearSetModalAnalysisAtASpeed)

        @property
        def assembly_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5099
            
            return self._parent._cast(_5099.AssemblyModalAnalysisAtASpeed)

        @property
        def bearing_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5100
            
            return self._parent._cast(_5100.BearingModalAnalysisAtASpeed)

        @property
        def belt_drive_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5102
            
            return self._parent._cast(_5102.BeltDriveModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5104
            
            return self._parent._cast(_5104.BevelDifferentialGearModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5105
            
            return self._parent._cast(_5105.BevelDifferentialGearSetModalAnalysisAtASpeed)

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5106
            
            return self._parent._cast(_5106.BevelDifferentialPlanetGearModalAnalysisAtASpeed)

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5107
            
            return self._parent._cast(_5107.BevelDifferentialSunGearModalAnalysisAtASpeed)

        @property
        def bevel_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5109
            
            return self._parent._cast(_5109.BevelGearModalAnalysisAtASpeed)

        @property
        def bevel_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5110
            
            return self._parent._cast(_5110.BevelGearSetModalAnalysisAtASpeed)

        @property
        def bolted_joint_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5111
            
            return self._parent._cast(_5111.BoltedJointModalAnalysisAtASpeed)

        @property
        def bolt_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5112
            
            return self._parent._cast(_5112.BoltModalAnalysisAtASpeed)

        @property
        def clutch_half_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5114
            
            return self._parent._cast(_5114.ClutchHalfModalAnalysisAtASpeed)

        @property
        def clutch_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5115
            
            return self._parent._cast(_5115.ClutchModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5117
            
            return self._parent._cast(_5117.ComponentModalAnalysisAtASpeed)

        @property
        def concept_coupling_half_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5119
            
            return self._parent._cast(_5119.ConceptCouplingHalfModalAnalysisAtASpeed)

        @property
        def concept_coupling_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5120
            
            return self._parent._cast(_5120.ConceptCouplingModalAnalysisAtASpeed)

        @property
        def concept_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5122
            
            return self._parent._cast(_5122.ConceptGearModalAnalysisAtASpeed)

        @property
        def concept_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5123
            
            return self._parent._cast(_5123.ConceptGearSetModalAnalysisAtASpeed)

        @property
        def conical_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5125
            
            return self._parent._cast(_5125.ConicalGearModalAnalysisAtASpeed)

        @property
        def conical_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5126
            
            return self._parent._cast(_5126.ConicalGearSetModalAnalysisAtASpeed)

        @property
        def connector_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5128
            
            return self._parent._cast(_5128.ConnectorModalAnalysisAtASpeed)

        @property
        def coupling_half_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5130
            
            return self._parent._cast(_5130.CouplingHalfModalAnalysisAtASpeed)

        @property
        def coupling_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5131
            
            return self._parent._cast(_5131.CouplingModalAnalysisAtASpeed)

        @property
        def cvt_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5133
            
            return self._parent._cast(_5133.CVTModalAnalysisAtASpeed)

        @property
        def cvt_pulley_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5134
            
            return self._parent._cast(_5134.CVTPulleyModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5135
            
            return self._parent._cast(_5135.CycloidalAssemblyModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5137
            
            return self._parent._cast(_5137.CycloidalDiscModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5140
            
            return self._parent._cast(_5140.CylindricalGearModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5141
            
            return self._parent._cast(_5141.CylindricalGearSetModalAnalysisAtASpeed)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5142
            
            return self._parent._cast(_5142.CylindricalPlanetGearModalAnalysisAtASpeed)

        @property
        def datum_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5143
            
            return self._parent._cast(_5143.DatumModalAnalysisAtASpeed)

        @property
        def external_cad_model_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5144
            
            return self._parent._cast(_5144.ExternalCADModelModalAnalysisAtASpeed)

        @property
        def face_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5146
            
            return self._parent._cast(_5146.FaceGearModalAnalysisAtASpeed)

        @property
        def face_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5147
            
            return self._parent._cast(_5147.FaceGearSetModalAnalysisAtASpeed)

        @property
        def fe_part_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5148
            
            return self._parent._cast(_5148.FEPartModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5149
            
            return self._parent._cast(_5149.FlexiblePinAssemblyModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5151
            
            return self._parent._cast(_5151.GearModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5152
            
            return self._parent._cast(_5152.GearSetModalAnalysisAtASpeed)

        @property
        def guide_dxf_model_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5153
            
            return self._parent._cast(_5153.GuideDxfModelModalAnalysisAtASpeed)

        @property
        def hypoid_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5155
            
            return self._parent._cast(_5155.HypoidGearModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5156
            
            return self._parent._cast(_5156.HypoidGearSetModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5159
            
            return self._parent._cast(_5159.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5160
            
            return self._parent._cast(_5160.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5162
            
            return self._parent._cast(_5162.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5163
            
            return self._parent._cast(_5163.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5165
            
            return self._parent._cast(_5165.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5166
            
            return self._parent._cast(_5166.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed)

        @property
        def mass_disc_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5167
            
            return self._parent._cast(_5167.MassDiscModalAnalysisAtASpeed)

        @property
        def measurement_component_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5168
            
            return self._parent._cast(_5168.MeasurementComponentModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5169
            
            return self._parent._cast(_5169.MountableComponentModalAnalysisAtASpeed)

        @property
        def oil_seal_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5170
            
            return self._parent._cast(_5170.OilSealModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5171
            
            return self._parent._cast(_5171.PartModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_half_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5173
            
            return self._parent._cast(_5173.PartToPartShearCouplingHalfModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5174
            
            return self._parent._cast(_5174.PartToPartShearCouplingModalAnalysisAtASpeed)

        @property
        def planetary_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5176
            
            return self._parent._cast(_5176.PlanetaryGearSetModalAnalysisAtASpeed)

        @property
        def planet_carrier_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5177
            
            return self._parent._cast(_5177.PlanetCarrierModalAnalysisAtASpeed)

        @property
        def point_load_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5178
            
            return self._parent._cast(_5178.PointLoadModalAnalysisAtASpeed)

        @property
        def power_load_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5179
            
            return self._parent._cast(_5179.PowerLoadModalAnalysisAtASpeed)

        @property
        def pulley_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5180
            
            return self._parent._cast(_5180.PulleyModalAnalysisAtASpeed)

        @property
        def ring_pins_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5181
            
            return self._parent._cast(_5181.RingPinsModalAnalysisAtASpeed)

        @property
        def rolling_ring_assembly_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5183
            
            return self._parent._cast(_5183.RollingRingAssemblyModalAnalysisAtASpeed)

        @property
        def rolling_ring_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5185
            
            return self._parent._cast(_5185.RollingRingModalAnalysisAtASpeed)

        @property
        def root_assembly_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5186
            
            return self._parent._cast(_5186.RootAssemblyModalAnalysisAtASpeed)

        @property
        def shaft_hub_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5187
            
            return self._parent._cast(_5187.ShaftHubConnectionModalAnalysisAtASpeed)

        @property
        def shaft_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5188
            
            return self._parent._cast(_5188.ShaftModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5190
            
            return self._parent._cast(_5190.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5192
            
            return self._parent._cast(_5192.SpiralBevelGearModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5193
            
            return self._parent._cast(_5193.SpiralBevelGearSetModalAnalysisAtASpeed)

        @property
        def spring_damper_half_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5195
            
            return self._parent._cast(_5195.SpringDamperHalfModalAnalysisAtASpeed)

        @property
        def spring_damper_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5196
            
            return self._parent._cast(_5196.SpringDamperModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5198
            
            return self._parent._cast(_5198.StraightBevelDiffGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5199
            
            return self._parent._cast(_5199.StraightBevelDiffGearSetModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5201
            
            return self._parent._cast(_5201.StraightBevelGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5202
            
            return self._parent._cast(_5202.StraightBevelGearSetModalAnalysisAtASpeed)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5203
            
            return self._parent._cast(_5203.StraightBevelPlanetGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5204
            
            return self._parent._cast(_5204.StraightBevelSunGearModalAnalysisAtASpeed)

        @property
        def synchroniser_half_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5205
            
            return self._parent._cast(_5205.SynchroniserHalfModalAnalysisAtASpeed)

        @property
        def synchroniser_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5206
            
            return self._parent._cast(_5206.SynchroniserModalAnalysisAtASpeed)

        @property
        def synchroniser_part_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5207
            
            return self._parent._cast(_5207.SynchroniserPartModalAnalysisAtASpeed)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5208
            
            return self._parent._cast(_5208.SynchroniserSleeveModalAnalysisAtASpeed)

        @property
        def torque_converter_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5210
            
            return self._parent._cast(_5210.TorqueConverterModalAnalysisAtASpeed)

        @property
        def torque_converter_pump_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5211
            
            return self._parent._cast(_5211.TorqueConverterPumpModalAnalysisAtASpeed)

        @property
        def torque_converter_turbine_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5212
            
            return self._parent._cast(_5212.TorqueConverterTurbineModalAnalysisAtASpeed)

        @property
        def unbalanced_mass_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5213
            
            return self._parent._cast(_5213.UnbalancedMassModalAnalysisAtASpeed)

        @property
        def virtual_component_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5214
            
            return self._parent._cast(_5214.VirtualComponentModalAnalysisAtASpeed)

        @property
        def worm_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5216
            
            return self._parent._cast(_5216.WormGearModalAnalysisAtASpeed)

        @property
        def worm_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5217
            
            return self._parent._cast(_5217.WormGearSetModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5219
            
            return self._parent._cast(_5219.ZerolBevelGearModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5220
            
            return self._parent._cast(_5220.ZerolBevelGearSetModalAnalysisAtASpeed)

        @property
        def abstract_assembly_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5350
            
            return self._parent._cast(_5350.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5351
            
            return self._parent._cast(_5351.AbstractShaftMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_or_housing_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5352
            
            return self._parent._cast(_5352.AbstractShaftOrHousingMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5355
            
            return self._parent._cast(_5355.AGMAGleasonConicalGearMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5356
            
            return self._parent._cast(_5356.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def assembly_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5358
            
            return self._parent._cast(_5358.AssemblyMultibodyDynamicsAnalysis)

        @property
        def bearing_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5359
            
            return self._parent._cast(_5359.BearingMultibodyDynamicsAnalysis)

        @property
        def belt_drive_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5362
            
            return self._parent._cast(_5362.BeltDriveMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5364
            
            return self._parent._cast(_5364.BevelDifferentialGearMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5365
            
            return self._parent._cast(_5365.BevelDifferentialGearSetMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_planet_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5366
            
            return self._parent._cast(_5366.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_sun_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5367
            
            return self._parent._cast(_5367.BevelDifferentialSunGearMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5369
            
            return self._parent._cast(_5369.BevelGearMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5370
            
            return self._parent._cast(_5370.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5371
            
            return self._parent._cast(_5371.BoltedJointMultibodyDynamicsAnalysis)

        @property
        def bolt_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5372
            
            return self._parent._cast(_5372.BoltMultibodyDynamicsAnalysis)

        @property
        def clutch_half_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5374
            
            return self._parent._cast(_5374.ClutchHalfMultibodyDynamicsAnalysis)

        @property
        def clutch_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5375
            
            return self._parent._cast(_5375.ClutchMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5378
            
            return self._parent._cast(_5378.ComponentMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5380
            
            return self._parent._cast(_5380.ConceptCouplingHalfMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5381
            
            return self._parent._cast(_5381.ConceptCouplingMultibodyDynamicsAnalysis)

        @property
        def concept_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5383
            
            return self._parent._cast(_5383.ConceptGearMultibodyDynamicsAnalysis)

        @property
        def concept_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5384
            
            return self._parent._cast(_5384.ConceptGearSetMultibodyDynamicsAnalysis)

        @property
        def conical_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5386
            
            return self._parent._cast(_5386.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5387
            
            return self._parent._cast(_5387.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def connector_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5389
            
            return self._parent._cast(_5389.ConnectorMultibodyDynamicsAnalysis)

        @property
        def coupling_half_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5391
            
            return self._parent._cast(_5391.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def coupling_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5392
            
            return self._parent._cast(_5392.CouplingMultibodyDynamicsAnalysis)

        @property
        def cvt_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5394
            
            return self._parent._cast(_5394.CVTMultibodyDynamicsAnalysis)

        @property
        def cvt_pulley_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5395
            
            return self._parent._cast(_5395.CVTPulleyMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5396
            
            return self._parent._cast(_5396.CycloidalAssemblyMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5398
            
            return self._parent._cast(_5398.CycloidalDiscMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5401
            
            return self._parent._cast(_5401.CylindricalGearMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5402
            
            return self._parent._cast(_5402.CylindricalGearSetMultibodyDynamicsAnalysis)

        @property
        def cylindrical_planet_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403
            
            return self._parent._cast(_5403.CylindricalPlanetGearMultibodyDynamicsAnalysis)

        @property
        def datum_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404
            
            return self._parent._cast(_5404.DatumMultibodyDynamicsAnalysis)

        @property
        def external_cad_model_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5405
            
            return self._parent._cast(_5405.ExternalCADModelMultibodyDynamicsAnalysis)

        @property
        def face_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5407
            
            return self._parent._cast(_5407.FaceGearMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5408
            
            return self._parent._cast(_5408.FaceGearSetMultibodyDynamicsAnalysis)

        @property
        def fe_part_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5409
            
            return self._parent._cast(_5409.FEPartMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410
            
            return self._parent._cast(_5410.FlexiblePinAssemblyMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5413
            
            return self._parent._cast(_5413.GearMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414
            
            return self._parent._cast(_5414.GearSetMultibodyDynamicsAnalysis)

        @property
        def guide_dxf_model_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5415
            
            return self._parent._cast(_5415.GuideDxfModelMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5417
            
            return self._parent._cast(_5417.HypoidGearMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5418
            
            return self._parent._cast(_5418.HypoidGearSetMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425
            
            return self._parent._cast(_5425.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5426
            
            return self._parent._cast(_5426.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428
            
            return self._parent._cast(_5428.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5429
            
            return self._parent._cast(_5429.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5431
            
            return self._parent._cast(_5431.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5432
            
            return self._parent._cast(_5432.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def mass_disc_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5433
            
            return self._parent._cast(_5433.MassDiscMultibodyDynamicsAnalysis)

        @property
        def measurement_component_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437
            
            return self._parent._cast(_5437.MeasurementComponentMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5438
            
            return self._parent._cast(_5438.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def oil_seal_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439
            
            return self._parent._cast(_5439.OilSealMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5440
            
            return self._parent._cast(_5440.PartMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5442
            
            return self._parent._cast(_5442.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5443
            
            return self._parent._cast(_5443.PartToPartShearCouplingMultibodyDynamicsAnalysis)

        @property
        def planetary_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5445
            
            return self._parent._cast(_5445.PlanetaryGearSetMultibodyDynamicsAnalysis)

        @property
        def planet_carrier_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5446
            
            return self._parent._cast(_5446.PlanetCarrierMultibodyDynamicsAnalysis)

        @property
        def point_load_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5447
            
            return self._parent._cast(_5447.PointLoadMultibodyDynamicsAnalysis)

        @property
        def power_load_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5448
            
            return self._parent._cast(_5448.PowerLoadMultibodyDynamicsAnalysis)

        @property
        def pulley_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5449
            
            return self._parent._cast(_5449.PulleyMultibodyDynamicsAnalysis)

        @property
        def ring_pins_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5450
            
            return self._parent._cast(_5450.RingPinsMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_assembly_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5452
            
            return self._parent._cast(_5452.RollingRingAssemblyMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5454
            
            return self._parent._cast(_5454.RollingRingMultibodyDynamicsAnalysis)

        @property
        def root_assembly_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5455
            
            return self._parent._cast(_5455.RootAssemblyMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5458
            
            return self._parent._cast(_5458.ShaftHubConnectionMultibodyDynamicsAnalysis)

        @property
        def shaft_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5459
            
            return self._parent._cast(_5459.ShaftMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5462
            
            return self._parent._cast(_5462.SpecialisedAssemblyMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464
            
            return self._parent._cast(_5464.SpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5465
            
            return self._parent._cast(_5465.SpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def spring_damper_half_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467
            
            return self._parent._cast(_5467.SpringDamperHalfMultibodyDynamicsAnalysis)

        @property
        def spring_damper_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5468
            
            return self._parent._cast(_5468.SpringDamperMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5470
            
            return self._parent._cast(_5470.StraightBevelDiffGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5471
            
            return self._parent._cast(_5471.StraightBevelDiffGearSetMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5473
            
            return self._parent._cast(_5473.StraightBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5474
            
            return self._parent._cast(_5474.StraightBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_planet_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475
            
            return self._parent._cast(_5475.StraightBevelPlanetGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_sun_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5476
            
            return self._parent._cast(_5476.StraightBevelSunGearMultibodyDynamicsAnalysis)

        @property
        def synchroniser_half_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5477
            
            return self._parent._cast(_5477.SynchroniserHalfMultibodyDynamicsAnalysis)

        @property
        def synchroniser_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5478
            
            return self._parent._cast(_5478.SynchroniserMultibodyDynamicsAnalysis)

        @property
        def synchroniser_part_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5479
            
            return self._parent._cast(_5479.SynchroniserPartMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5480
            
            return self._parent._cast(_5480.SynchroniserSleeveMultibodyDynamicsAnalysis)

        @property
        def torque_converter_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5483
            
            return self._parent._cast(_5483.TorqueConverterMultibodyDynamicsAnalysis)

        @property
        def torque_converter_pump_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5484
            
            return self._parent._cast(_5484.TorqueConverterPumpMultibodyDynamicsAnalysis)

        @property
        def torque_converter_turbine_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5486
            
            return self._parent._cast(_5486.TorqueConverterTurbineMultibodyDynamicsAnalysis)

        @property
        def unbalanced_mass_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5487
            
            return self._parent._cast(_5487.UnbalancedMassMultibodyDynamicsAnalysis)

        @property
        def virtual_component_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488
            
            return self._parent._cast(_5488.VirtualComponentMultibodyDynamicsAnalysis)

        @property
        def worm_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491
            
            return self._parent._cast(_5491.WormGearMultibodyDynamicsAnalysis)

        @property
        def worm_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5492
            
            return self._parent._cast(_5492.WormGearSetMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5494
            
            return self._parent._cast(_5494.ZerolBevelGearMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5495
            
            return self._parent._cast(_5495.ZerolBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5651
            
            return self._parent._cast(_5651.AbstractAssemblyHarmonicAnalysis)

        @property
        def abstract_shaft_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5653
            
            return self._parent._cast(_5653.AbstractShaftHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5654
            
            return self._parent._cast(_5654.AbstractShaftOrHousingHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5656
            
            return self._parent._cast(_5656.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5658
            
            return self._parent._cast(_5658.AGMAGleasonConicalGearSetHarmonicAnalysis)

        @property
        def assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5659
            
            return self._parent._cast(_5659.AssemblyHarmonicAnalysis)

        @property
        def bearing_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5660
            
            return self._parent._cast(_5660.BearingHarmonicAnalysis)

        @property
        def belt_drive_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5662
            
            return self._parent._cast(_5662.BeltDriveHarmonicAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5663
            
            return self._parent._cast(_5663.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5665
            
            return self._parent._cast(_5665.BevelDifferentialGearSetHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5666
            
            return self._parent._cast(_5666.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5667
            
            return self._parent._cast(_5667.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5668
            
            return self._parent._cast(_5668.BevelGearHarmonicAnalysis)

        @property
        def bevel_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5670
            
            return self._parent._cast(_5670.BevelGearSetHarmonicAnalysis)

        @property
        def bolted_joint_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5671
            
            return self._parent._cast(_5671.BoltedJointHarmonicAnalysis)

        @property
        def bolt_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5672
            
            return self._parent._cast(_5672.BoltHarmonicAnalysis)

        @property
        def clutch_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5674
            
            return self._parent._cast(_5674.ClutchHalfHarmonicAnalysis)

        @property
        def clutch_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5675
            
            return self._parent._cast(_5675.ClutchHarmonicAnalysis)

        @property
        def component_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5678
            
            return self._parent._cast(_5678.ComponentHarmonicAnalysis)

        @property
        def concept_coupling_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5680
            
            return self._parent._cast(_5680.ConceptCouplingHalfHarmonicAnalysis)

        @property
        def concept_coupling_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5681
            
            return self._parent._cast(_5681.ConceptCouplingHarmonicAnalysis)

        @property
        def concept_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5682
            
            return self._parent._cast(_5682.ConceptGearHarmonicAnalysis)

        @property
        def concept_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5684
            
            return self._parent._cast(_5684.ConceptGearSetHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5685
            
            return self._parent._cast(_5685.ConicalGearHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5687
            
            return self._parent._cast(_5687.ConicalGearSetHarmonicAnalysis)

        @property
        def connector_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5689
            
            return self._parent._cast(_5689.ConnectorHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5691
            
            return self._parent._cast(_5691.CouplingHalfHarmonicAnalysis)

        @property
        def coupling_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5692
            
            return self._parent._cast(_5692.CouplingHarmonicAnalysis)

        @property
        def cvt_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5694
            
            return self._parent._cast(_5694.CVTHarmonicAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5695
            
            return self._parent._cast(_5695.CVTPulleyHarmonicAnalysis)

        @property
        def cycloidal_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5696
            
            return self._parent._cast(_5696.CycloidalAssemblyHarmonicAnalysis)

        @property
        def cycloidal_disc_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5698
            
            return self._parent._cast(_5698.CycloidalDiscHarmonicAnalysis)

        @property
        def cylindrical_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5700
            
            return self._parent._cast(_5700.CylindricalGearHarmonicAnalysis)

        @property
        def cylindrical_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5702
            
            return self._parent._cast(_5702.CylindricalGearSetHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5703
            
            return self._parent._cast(_5703.CylindricalPlanetGearHarmonicAnalysis)

        @property
        def datum_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5704
            
            return self._parent._cast(_5704.DatumHarmonicAnalysis)

        @property
        def external_cad_model_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5718
            
            return self._parent._cast(_5718.ExternalCADModelHarmonicAnalysis)

        @property
        def face_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5719
            
            return self._parent._cast(_5719.FaceGearHarmonicAnalysis)

        @property
        def face_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5721
            
            return self._parent._cast(_5721.FaceGearSetHarmonicAnalysis)

        @property
        def fe_part_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5722
            
            return self._parent._cast(_5722.FEPartHarmonicAnalysis)

        @property
        def flexible_pin_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5723
            
            return self._parent._cast(_5723.FlexiblePinAssemblyHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5725
            
            return self._parent._cast(_5725.GearHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5730
            
            return self._parent._cast(_5730.GearSetHarmonicAnalysis)

        @property
        def guide_dxf_model_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5732
            
            return self._parent._cast(_5732.GuideDxfModelHarmonicAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5741
            
            return self._parent._cast(_5741.HypoidGearHarmonicAnalysis)

        @property
        def hypoid_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5743
            
            return self._parent._cast(_5743.HypoidGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5745
            
            return self._parent._cast(_5745.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5747
            
            return self._parent._cast(_5747.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5748
            
            return self._parent._cast(_5748.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5750
            
            return self._parent._cast(_5750.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5751
            
            return self._parent._cast(_5751.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5753
            
            return self._parent._cast(_5753.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis)

        @property
        def mass_disc_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5754
            
            return self._parent._cast(_5754.MassDiscHarmonicAnalysis)

        @property
        def measurement_component_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5755
            
            return self._parent._cast(_5755.MeasurementComponentHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5756
            
            return self._parent._cast(_5756.MountableComponentHarmonicAnalysis)

        @property
        def oil_seal_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5757
            
            return self._parent._cast(_5757.OilSealHarmonicAnalysis)

        @property
        def part_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5758
            
            return self._parent._cast(_5758.PartHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5760
            
            return self._parent._cast(_5760.PartToPartShearCouplingHalfHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5761
            
            return self._parent._cast(_5761.PartToPartShearCouplingHarmonicAnalysis)

        @property
        def planetary_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5764
            
            return self._parent._cast(_5764.PlanetaryGearSetHarmonicAnalysis)

        @property
        def planet_carrier_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5765
            
            return self._parent._cast(_5765.PlanetCarrierHarmonicAnalysis)

        @property
        def point_load_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5766
            
            return self._parent._cast(_5766.PointLoadHarmonicAnalysis)

        @property
        def power_load_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5767
            
            return self._parent._cast(_5767.PowerLoadHarmonicAnalysis)

        @property
        def pulley_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5768
            
            return self._parent._cast(_5768.PulleyHarmonicAnalysis)

        @property
        def ring_pins_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5770
            
            return self._parent._cast(_5770.RingPinsHarmonicAnalysis)

        @property
        def rolling_ring_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5772
            
            return self._parent._cast(_5772.RollingRingAssemblyHarmonicAnalysis)

        @property
        def rolling_ring_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5774
            
            return self._parent._cast(_5774.RollingRingHarmonicAnalysis)

        @property
        def root_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5775
            
            return self._parent._cast(_5775.RootAssemblyHarmonicAnalysis)

        @property
        def shaft_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5776
            
            return self._parent._cast(_5776.ShaftHarmonicAnalysis)

        @property
        def shaft_hub_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5777
            
            return self._parent._cast(_5777.ShaftHubConnectionHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5780
            
            return self._parent._cast(_5780.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def spiral_bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5782
            
            return self._parent._cast(_5782.SpiralBevelGearHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5784
            
            return self._parent._cast(_5784.SpiralBevelGearSetHarmonicAnalysis)

        @property
        def spring_damper_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5786
            
            return self._parent._cast(_5786.SpringDamperHalfHarmonicAnalysis)

        @property
        def spring_damper_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5787
            
            return self._parent._cast(_5787.SpringDamperHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5789
            
            return self._parent._cast(_5789.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5791
            
            return self._parent._cast(_5791.StraightBevelDiffGearSetHarmonicAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5792
            
            return self._parent._cast(_5792.StraightBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5794
            
            return self._parent._cast(_5794.StraightBevelGearSetHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5795
            
            return self._parent._cast(_5795.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5796
            
            return self._parent._cast(_5796.StraightBevelSunGearHarmonicAnalysis)

        @property
        def synchroniser_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5797
            
            return self._parent._cast(_5797.SynchroniserHalfHarmonicAnalysis)

        @property
        def synchroniser_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5798
            
            return self._parent._cast(_5798.SynchroniserHarmonicAnalysis)

        @property
        def synchroniser_part_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5799
            
            return self._parent._cast(_5799.SynchroniserPartHarmonicAnalysis)

        @property
        def synchroniser_sleeve_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5800
            
            return self._parent._cast(_5800.SynchroniserSleeveHarmonicAnalysis)

        @property
        def torque_converter_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5802
            
            return self._parent._cast(_5802.TorqueConverterHarmonicAnalysis)

        @property
        def torque_converter_pump_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5803
            
            return self._parent._cast(_5803.TorqueConverterPumpHarmonicAnalysis)

        @property
        def torque_converter_turbine_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5804
            
            return self._parent._cast(_5804.TorqueConverterTurbineHarmonicAnalysis)

        @property
        def unbalanced_mass_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5806
            
            return self._parent._cast(_5806.UnbalancedMassHarmonicAnalysis)

        @property
        def virtual_component_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5807
            
            return self._parent._cast(_5807.VirtualComponentHarmonicAnalysis)

        @property
        def worm_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5808
            
            return self._parent._cast(_5808.WormGearHarmonicAnalysis)

        @property
        def worm_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5810
            
            return self._parent._cast(_5810.WormGearSetHarmonicAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5811
            
            return self._parent._cast(_5811.ZerolBevelGearHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5813
            
            return self._parent._cast(_5813.ZerolBevelGearSetHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5978
            
            return self._parent._cast(_5978.AbstractAssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_shaft_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5979
            
            return self._parent._cast(_5979.AbstractShaftHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_shaft_or_housing_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5980
            
            return self._parent._cast(_5980.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation)

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5982
            
            return self._parent._cast(_5982.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5984
            
            return self._parent._cast(_5984.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5985
            
            return self._parent._cast(_5985.AssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def bearing_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5986
            
            return self._parent._cast(_5986.BearingHarmonicAnalysisOfSingleExcitation)

        @property
        def belt_drive_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5988
            
            return self._parent._cast(_5988.BeltDriveHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5989
            
            return self._parent._cast(_5989.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5991
            
            return self._parent._cast(_5991.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_planet_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5992
            
            return self._parent._cast(_5992.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_sun_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5993
            
            return self._parent._cast(_5993.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5994
            
            return self._parent._cast(_5994.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5996
            
            return self._parent._cast(_5996.BevelGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def bolted_joint_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5997
            
            return self._parent._cast(_5997.BoltedJointHarmonicAnalysisOfSingleExcitation)

        @property
        def bolt_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5998
            
            return self._parent._cast(_5998.BoltHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6000
            
            return self._parent._cast(_6000.ClutchHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6001
            
            return self._parent._cast(_6001.ClutchHarmonicAnalysisOfSingleExcitation)

        @property
        def component_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6003
            
            return self._parent._cast(_6003.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6005
            
            return self._parent._cast(_6005.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6006
            
            return self._parent._cast(_6006.ConceptCouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6007
            
            return self._parent._cast(_6007.ConceptGearHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6009
            
            return self._parent._cast(_6009.ConceptGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6010
            
            return self._parent._cast(_6010.ConicalGearHarmonicAnalysisOfSingleExcitation)

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6012
            
            return self._parent._cast(_6012.ConicalGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def connector_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6014
            
            return self._parent._cast(_6014.ConnectorHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6016
            
            return self._parent._cast(_6016.CouplingHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6017
            
            return self._parent._cast(_6017.CouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6019
            
            return self._parent._cast(_6019.CVTHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_pulley_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6020
            
            return self._parent._cast(_6020.CVTPulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6021
            
            return self._parent._cast(_6021.CycloidalAssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_disc_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6023
            
            return self._parent._cast(_6023.CycloidalDiscHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6025
            
            return self._parent._cast(_6025.CylindricalGearHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6027
            
            return self._parent._cast(_6027.CylindricalGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_planet_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6028
            
            return self._parent._cast(_6028.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation)

        @property
        def datum_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6029
            
            return self._parent._cast(_6029.DatumHarmonicAnalysisOfSingleExcitation)

        @property
        def external_cad_model_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6030
            
            return self._parent._cast(_6030.ExternalCADModelHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6031
            
            return self._parent._cast(_6031.FaceGearHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6033
            
            return self._parent._cast(_6033.FaceGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def fe_part_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6034
            
            return self._parent._cast(_6034.FEPartHarmonicAnalysisOfSingleExcitation)

        @property
        def flexible_pin_assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6035
            
            return self._parent._cast(_6035.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6036
            
            return self._parent._cast(_6036.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6038
            
            return self._parent._cast(_6038.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def guide_dxf_model_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6039
            
            return self._parent._cast(_6039.GuideDxfModelHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6041
            
            return self._parent._cast(_6041.HypoidGearHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6043
            
            return self._parent._cast(_6043.HypoidGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6045
            
            return self._parent._cast(_6045.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6047
            
            return self._parent._cast(_6047.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6048
            
            return self._parent._cast(_6048.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6050
            
            return self._parent._cast(_6050.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6051
            
            return self._parent._cast(_6051.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6053
            
            return self._parent._cast(_6053.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def mass_disc_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6054
            
            return self._parent._cast(_6054.MassDiscHarmonicAnalysisOfSingleExcitation)

        @property
        def measurement_component_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6055
            
            return self._parent._cast(_6055.MeasurementComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6056
            
            return self._parent._cast(_6056.MountableComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def oil_seal_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6057
            
            return self._parent._cast(_6057.OilSealHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6058
            
            return self._parent._cast(_6058.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6060
            
            return self._parent._cast(_6060.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6061
            
            return self._parent._cast(_6061.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def planetary_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6063
            
            return self._parent._cast(_6063.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def planet_carrier_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6064
            
            return self._parent._cast(_6064.PlanetCarrierHarmonicAnalysisOfSingleExcitation)

        @property
        def point_load_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6065
            
            return self._parent._cast(_6065.PointLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def power_load_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6066
            
            return self._parent._cast(_6066.PowerLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def pulley_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6067
            
            return self._parent._cast(_6067.PulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def ring_pins_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6068
            
            return self._parent._cast(_6068.RingPinsHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6070
            
            return self._parent._cast(_6070.RollingRingAssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6072
            
            return self._parent._cast(_6072.RollingRingHarmonicAnalysisOfSingleExcitation)

        @property
        def root_assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6073
            
            return self._parent._cast(_6073.RootAssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6074
            
            return self._parent._cast(_6074.ShaftHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_hub_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6075
            
            return self._parent._cast(_6075.ShaftHubConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6077
            
            return self._parent._cast(_6077.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def spiral_bevel_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6078
            
            return self._parent._cast(_6078.SpiralBevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6080
            
            return self._parent._cast(_6080.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def spring_damper_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6082
            
            return self._parent._cast(_6082.SpringDamperHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def spring_damper_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6083
            
            return self._parent._cast(_6083.SpringDamperHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_diff_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6084
            
            return self._parent._cast(_6084.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6086
            
            return self._parent._cast(_6086.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6087
            
            return self._parent._cast(_6087.StraightBevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6089
            
            return self._parent._cast(_6089.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_planet_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6090
            
            return self._parent._cast(_6090.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_sun_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6091
            
            return self._parent._cast(_6091.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6092
            
            return self._parent._cast(_6092.SynchroniserHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6093
            
            return self._parent._cast(_6093.SynchroniserHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_part_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6094
            
            return self._parent._cast(_6094.SynchroniserPartHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_sleeve_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6095
            
            return self._parent._cast(_6095.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation)

        @property
        def torque_converter_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6097
            
            return self._parent._cast(_6097.TorqueConverterHarmonicAnalysisOfSingleExcitation)

        @property
        def torque_converter_pump_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6098
            
            return self._parent._cast(_6098.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation)

        @property
        def torque_converter_turbine_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6099
            
            return self._parent._cast(_6099.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation)

        @property
        def unbalanced_mass_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6100
            
            return self._parent._cast(_6100.UnbalancedMassHarmonicAnalysisOfSingleExcitation)

        @property
        def virtual_component_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6101
            
            return self._parent._cast(_6101.VirtualComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6102
            
            return self._parent._cast(_6102.WormGearHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6104
            
            return self._parent._cast(_6104.WormGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6105
            
            return self._parent._cast(_6105.ZerolBevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6107
            
            return self._parent._cast(_6107.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_assembly_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6246
            
            return self._parent._cast(_6246.AbstractAssemblyDynamicAnalysis)

        @property
        def abstract_shaft_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6247
            
            return self._parent._cast(_6247.AbstractShaftDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6248
            
            return self._parent._cast(_6248.AbstractShaftOrHousingDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6250
            
            return self._parent._cast(_6250.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6252
            
            return self._parent._cast(_6252.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def assembly_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6253
            
            return self._parent._cast(_6253.AssemblyDynamicAnalysis)

        @property
        def bearing_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6254
            
            return self._parent._cast(_6254.BearingDynamicAnalysis)

        @property
        def belt_drive_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6256
            
            return self._parent._cast(_6256.BeltDriveDynamicAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6257
            
            return self._parent._cast(_6257.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6259
            
            return self._parent._cast(_6259.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6260
            
            return self._parent._cast(_6260.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6261
            
            return self._parent._cast(_6261.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6262
            
            return self._parent._cast(_6262.BevelGearDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6264
            
            return self._parent._cast(_6264.BevelGearSetDynamicAnalysis)

        @property
        def bolt_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6265
            
            return self._parent._cast(_6265.BoltDynamicAnalysis)

        @property
        def bolted_joint_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6266
            
            return self._parent._cast(_6266.BoltedJointDynamicAnalysis)

        @property
        def clutch_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6268
            
            return self._parent._cast(_6268.ClutchDynamicAnalysis)

        @property
        def clutch_half_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6269
            
            return self._parent._cast(_6269.ClutchHalfDynamicAnalysis)

        @property
        def component_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6271
            
            return self._parent._cast(_6271.ComponentDynamicAnalysis)

        @property
        def concept_coupling_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6273
            
            return self._parent._cast(_6273.ConceptCouplingDynamicAnalysis)

        @property
        def concept_coupling_half_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6274
            
            return self._parent._cast(_6274.ConceptCouplingHalfDynamicAnalysis)

        @property
        def concept_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6275
            
            return self._parent._cast(_6275.ConceptGearDynamicAnalysis)

        @property
        def concept_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6277
            
            return self._parent._cast(_6277.ConceptGearSetDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6278
            
            return self._parent._cast(_6278.ConicalGearDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6280
            
            return self._parent._cast(_6280.ConicalGearSetDynamicAnalysis)

        @property
        def connector_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6282
            
            return self._parent._cast(_6282.ConnectorDynamicAnalysis)

        @property
        def coupling_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6284
            
            return self._parent._cast(_6284.CouplingDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6285
            
            return self._parent._cast(_6285.CouplingHalfDynamicAnalysis)

        @property
        def cvt_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6287
            
            return self._parent._cast(_6287.CVTDynamicAnalysis)

        @property
        def cvt_pulley_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6288
            
            return self._parent._cast(_6288.CVTPulleyDynamicAnalysis)

        @property
        def cycloidal_assembly_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6289
            
            return self._parent._cast(_6289.CycloidalAssemblyDynamicAnalysis)

        @property
        def cycloidal_disc_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6291
            
            return self._parent._cast(_6291.CycloidalDiscDynamicAnalysis)

        @property
        def cylindrical_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6293
            
            return self._parent._cast(_6293.CylindricalGearDynamicAnalysis)

        @property
        def cylindrical_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6295
            
            return self._parent._cast(_6295.CylindricalGearSetDynamicAnalysis)

        @property
        def cylindrical_planet_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6296
            
            return self._parent._cast(_6296.CylindricalPlanetGearDynamicAnalysis)

        @property
        def datum_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6297
            
            return self._parent._cast(_6297.DatumDynamicAnalysis)

        @property
        def external_cad_model_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299
            
            return self._parent._cast(_6299.ExternalCADModelDynamicAnalysis)

        @property
        def face_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6300
            
            return self._parent._cast(_6300.FaceGearDynamicAnalysis)

        @property
        def face_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302
            
            return self._parent._cast(_6302.FaceGearSetDynamicAnalysis)

        @property
        def fe_part_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303
            
            return self._parent._cast(_6303.FEPartDynamicAnalysis)

        @property
        def flexible_pin_assembly_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304
            
            return self._parent._cast(_6304.FlexiblePinAssemblyDynamicAnalysis)

        @property
        def gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6305
            
            return self._parent._cast(_6305.GearDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307
            
            return self._parent._cast(_6307.GearSetDynamicAnalysis)

        @property
        def guide_dxf_model_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308
            
            return self._parent._cast(_6308.GuideDxfModelDynamicAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309
            
            return self._parent._cast(_6309.HypoidGearDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311
            
            return self._parent._cast(_6311.HypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6313
            
            return self._parent._cast(_6313.KlingelnbergCycloPalloidConicalGearDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6315
            
            return self._parent._cast(_6315.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316
            
            return self._parent._cast(_6316.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6318
            
            return self._parent._cast(_6318.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6319
            
            return self._parent._cast(_6319.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321
            
            return self._parent._cast(_6321.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis)

        @property
        def mass_disc_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6322
            
            return self._parent._cast(_6322.MassDiscDynamicAnalysis)

        @property
        def measurement_component_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323
            
            return self._parent._cast(_6323.MeasurementComponentDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6324
            
            return self._parent._cast(_6324.MountableComponentDynamicAnalysis)

        @property
        def oil_seal_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6325
            
            return self._parent._cast(_6325.OilSealDynamicAnalysis)

        @property
        def part_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6326
            
            return self._parent._cast(_6326.PartDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328
            
            return self._parent._cast(_6328.PartToPartShearCouplingDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6329
            
            return self._parent._cast(_6329.PartToPartShearCouplingHalfDynamicAnalysis)

        @property
        def planetary_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6331
            
            return self._parent._cast(_6331.PlanetaryGearSetDynamicAnalysis)

        @property
        def planet_carrier_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6332
            
            return self._parent._cast(_6332.PlanetCarrierDynamicAnalysis)

        @property
        def point_load_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6333
            
            return self._parent._cast(_6333.PointLoadDynamicAnalysis)

        @property
        def power_load_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334
            
            return self._parent._cast(_6334.PowerLoadDynamicAnalysis)

        @property
        def pulley_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335
            
            return self._parent._cast(_6335.PulleyDynamicAnalysis)

        @property
        def ring_pins_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6336
            
            return self._parent._cast(_6336.RingPinsDynamicAnalysis)

        @property
        def rolling_ring_assembly_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338
            
            return self._parent._cast(_6338.RollingRingAssemblyDynamicAnalysis)

        @property
        def rolling_ring_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6340
            
            return self._parent._cast(_6340.RollingRingDynamicAnalysis)

        @property
        def root_assembly_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6341
            
            return self._parent._cast(_6341.RootAssemblyDynamicAnalysis)

        @property
        def shaft_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342
            
            return self._parent._cast(_6342.ShaftDynamicAnalysis)

        @property
        def shaft_hub_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6343
            
            return self._parent._cast(_6343.ShaftHubConnectionDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6345
            
            return self._parent._cast(_6345.SpecialisedAssemblyDynamicAnalysis)

        @property
        def spiral_bevel_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346
            
            return self._parent._cast(_6346.SpiralBevelGearDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6348
            
            return self._parent._cast(_6348.SpiralBevelGearSetDynamicAnalysis)

        @property
        def spring_damper_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350
            
            return self._parent._cast(_6350.SpringDamperDynamicAnalysis)

        @property
        def spring_damper_half_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6351
            
            return self._parent._cast(_6351.SpringDamperHalfDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352
            
            return self._parent._cast(_6352.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354
            
            return self._parent._cast(_6354.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355
            
            return self._parent._cast(_6355.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357
            
            return self._parent._cast(_6357.StraightBevelGearSetDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358
            
            return self._parent._cast(_6358.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6359
            
            return self._parent._cast(_6359.StraightBevelSunGearDynamicAnalysis)

        @property
        def synchroniser_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360
            
            return self._parent._cast(_6360.SynchroniserDynamicAnalysis)

        @property
        def synchroniser_half_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6361
            
            return self._parent._cast(_6361.SynchroniserHalfDynamicAnalysis)

        @property
        def synchroniser_part_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6362
            
            return self._parent._cast(_6362.SynchroniserPartDynamicAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363
            
            return self._parent._cast(_6363.SynchroniserSleeveDynamicAnalysis)

        @property
        def torque_converter_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6365
            
            return self._parent._cast(_6365.TorqueConverterDynamicAnalysis)

        @property
        def torque_converter_pump_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366
            
            return self._parent._cast(_6366.TorqueConverterPumpDynamicAnalysis)

        @property
        def torque_converter_turbine_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6367
            
            return self._parent._cast(_6367.TorqueConverterTurbineDynamicAnalysis)

        @property
        def unbalanced_mass_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6368
            
            return self._parent._cast(_6368.UnbalancedMassDynamicAnalysis)

        @property
        def virtual_component_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6369
            
            return self._parent._cast(_6369.VirtualComponentDynamicAnalysis)

        @property
        def worm_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6370
            
            return self._parent._cast(_6370.WormGearDynamicAnalysis)

        @property
        def worm_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6372
            
            return self._parent._cast(_6372.WormGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6373
            
            return self._parent._cast(_6373.ZerolBevelGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6375
            
            return self._parent._cast(_6375.ZerolBevelGearSetDynamicAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6511
            
            return self._parent._cast(_6511.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_shaft_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6512
            
            return self._parent._cast(_6512.AbstractShaftCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6513
            
            return self._parent._cast(_6513.AbstractShaftOrHousingCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6515
            
            return self._parent._cast(_6515.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6517
            
            return self._parent._cast(_6517.AGMAGleasonConicalGearSetCriticalSpeedAnalysis)

        @property
        def assembly_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6518
            
            return self._parent._cast(_6518.AssemblyCriticalSpeedAnalysis)

        @property
        def bearing_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6519
            
            return self._parent._cast(_6519.BearingCriticalSpeedAnalysis)

        @property
        def belt_drive_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6521
            
            return self._parent._cast(_6521.BeltDriveCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6522
            
            return self._parent._cast(_6522.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6524
            
            return self._parent._cast(_6524.BevelDifferentialGearSetCriticalSpeedAnalysis)

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6525
            
            return self._parent._cast(_6525.BevelDifferentialPlanetGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6526
            
            return self._parent._cast(_6526.BevelDifferentialSunGearCriticalSpeedAnalysis)

        @property
        def bevel_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6527
            
            return self._parent._cast(_6527.BevelGearCriticalSpeedAnalysis)

        @property
        def bevel_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6529
            
            return self._parent._cast(_6529.BevelGearSetCriticalSpeedAnalysis)

        @property
        def bolt_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6530
            
            return self._parent._cast(_6530.BoltCriticalSpeedAnalysis)

        @property
        def bolted_joint_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6531
            
            return self._parent._cast(_6531.BoltedJointCriticalSpeedAnalysis)

        @property
        def clutch_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6533
            
            return self._parent._cast(_6533.ClutchCriticalSpeedAnalysis)

        @property
        def clutch_half_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6534
            
            return self._parent._cast(_6534.ClutchHalfCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6536
            
            return self._parent._cast(_6536.ComponentCriticalSpeedAnalysis)

        @property
        def concept_coupling_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6538
            
            return self._parent._cast(_6538.ConceptCouplingCriticalSpeedAnalysis)

        @property
        def concept_coupling_half_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6539
            
            return self._parent._cast(_6539.ConceptCouplingHalfCriticalSpeedAnalysis)

        @property
        def concept_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6540
            
            return self._parent._cast(_6540.ConceptGearCriticalSpeedAnalysis)

        @property
        def concept_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6542
            
            return self._parent._cast(_6542.ConceptGearSetCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6543
            
            return self._parent._cast(_6543.ConicalGearCriticalSpeedAnalysis)

        @property
        def conical_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6545
            
            return self._parent._cast(_6545.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def connector_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6547
            
            return self._parent._cast(_6547.ConnectorCriticalSpeedAnalysis)

        @property
        def coupling_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6549
            
            return self._parent._cast(_6549.CouplingCriticalSpeedAnalysis)

        @property
        def coupling_half_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6550
            
            return self._parent._cast(_6550.CouplingHalfCriticalSpeedAnalysis)

        @property
        def cvt_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6554
            
            return self._parent._cast(_6554.CVTCriticalSpeedAnalysis)

        @property
        def cvt_pulley_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6555
            
            return self._parent._cast(_6555.CVTPulleyCriticalSpeedAnalysis)

        @property
        def cycloidal_assembly_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6556
            
            return self._parent._cast(_6556.CycloidalAssemblyCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6558
            
            return self._parent._cast(_6558.CycloidalDiscCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6560
            
            return self._parent._cast(_6560.CylindricalGearCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6562
            
            return self._parent._cast(_6562.CylindricalGearSetCriticalSpeedAnalysis)

        @property
        def cylindrical_planet_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6563
            
            return self._parent._cast(_6563.CylindricalPlanetGearCriticalSpeedAnalysis)

        @property
        def datum_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6564
            
            return self._parent._cast(_6564.DatumCriticalSpeedAnalysis)

        @property
        def external_cad_model_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6565
            
            return self._parent._cast(_6565.ExternalCADModelCriticalSpeedAnalysis)

        @property
        def face_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6566
            
            return self._parent._cast(_6566.FaceGearCriticalSpeedAnalysis)

        @property
        def face_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6568
            
            return self._parent._cast(_6568.FaceGearSetCriticalSpeedAnalysis)

        @property
        def fe_part_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6569
            
            return self._parent._cast(_6569.FEPartCriticalSpeedAnalysis)

        @property
        def flexible_pin_assembly_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6570
            
            return self._parent._cast(_6570.FlexiblePinAssemblyCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6571
            
            return self._parent._cast(_6571.GearCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6573
            
            return self._parent._cast(_6573.GearSetCriticalSpeedAnalysis)

        @property
        def guide_dxf_model_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6574
            
            return self._parent._cast(_6574.GuideDxfModelCriticalSpeedAnalysis)

        @property
        def hypoid_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6575
            
            return self._parent._cast(_6575.HypoidGearCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6577
            
            return self._parent._cast(_6577.HypoidGearSetCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6579
            
            return self._parent._cast(_6579.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6581
            
            return self._parent._cast(_6581.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6582
            
            return self._parent._cast(_6582.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6584
            
            return self._parent._cast(_6584.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6585
            
            return self._parent._cast(_6585.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6587
            
            return self._parent._cast(_6587.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis)

        @property
        def mass_disc_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6588
            
            return self._parent._cast(_6588.MassDiscCriticalSpeedAnalysis)

        @property
        def measurement_component_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6589
            
            return self._parent._cast(_6589.MeasurementComponentCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6590
            
            return self._parent._cast(_6590.MountableComponentCriticalSpeedAnalysis)

        @property
        def oil_seal_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6591
            
            return self._parent._cast(_6591.OilSealCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6592
            
            return self._parent._cast(_6592.PartCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6594
            
            return self._parent._cast(_6594.PartToPartShearCouplingCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_half_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6595
            
            return self._parent._cast(_6595.PartToPartShearCouplingHalfCriticalSpeedAnalysis)

        @property
        def planetary_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6597
            
            return self._parent._cast(_6597.PlanetaryGearSetCriticalSpeedAnalysis)

        @property
        def planet_carrier_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6598
            
            return self._parent._cast(_6598.PlanetCarrierCriticalSpeedAnalysis)

        @property
        def point_load_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6599
            
            return self._parent._cast(_6599.PointLoadCriticalSpeedAnalysis)

        @property
        def power_load_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6600
            
            return self._parent._cast(_6600.PowerLoadCriticalSpeedAnalysis)

        @property
        def pulley_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6601
            
            return self._parent._cast(_6601.PulleyCriticalSpeedAnalysis)

        @property
        def ring_pins_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6602
            
            return self._parent._cast(_6602.RingPinsCriticalSpeedAnalysis)

        @property
        def rolling_ring_assembly_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6604
            
            return self._parent._cast(_6604.RollingRingAssemblyCriticalSpeedAnalysis)

        @property
        def rolling_ring_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6606
            
            return self._parent._cast(_6606.RollingRingCriticalSpeedAnalysis)

        @property
        def root_assembly_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6607
            
            return self._parent._cast(_6607.RootAssemblyCriticalSpeedAnalysis)

        @property
        def shaft_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6608
            
            return self._parent._cast(_6608.ShaftCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6609
            
            return self._parent._cast(_6609.ShaftHubConnectionCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6611
            
            return self._parent._cast(_6611.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6612
            
            return self._parent._cast(_6612.SpiralBevelGearCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6614
            
            return self._parent._cast(_6614.SpiralBevelGearSetCriticalSpeedAnalysis)

        @property
        def spring_damper_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6616
            
            return self._parent._cast(_6616.SpringDamperCriticalSpeedAnalysis)

        @property
        def spring_damper_half_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6617
            
            return self._parent._cast(_6617.SpringDamperHalfCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6618
            
            return self._parent._cast(_6618.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6620
            
            return self._parent._cast(_6620.StraightBevelDiffGearSetCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6621
            
            return self._parent._cast(_6621.StraightBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6623
            
            return self._parent._cast(_6623.StraightBevelGearSetCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6624
            
            return self._parent._cast(_6624.StraightBevelPlanetGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6625
            
            return self._parent._cast(_6625.StraightBevelSunGearCriticalSpeedAnalysis)

        @property
        def synchroniser_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6626
            
            return self._parent._cast(_6626.SynchroniserCriticalSpeedAnalysis)

        @property
        def synchroniser_half_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6627
            
            return self._parent._cast(_6627.SynchroniserHalfCriticalSpeedAnalysis)

        @property
        def synchroniser_part_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6628
            
            return self._parent._cast(_6628.SynchroniserPartCriticalSpeedAnalysis)

        @property
        def synchroniser_sleeve_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6629
            
            return self._parent._cast(_6629.SynchroniserSleeveCriticalSpeedAnalysis)

        @property
        def torque_converter_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6631
            
            return self._parent._cast(_6631.TorqueConverterCriticalSpeedAnalysis)

        @property
        def torque_converter_pump_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6632
            
            return self._parent._cast(_6632.TorqueConverterPumpCriticalSpeedAnalysis)

        @property
        def torque_converter_turbine_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6633
            
            return self._parent._cast(_6633.TorqueConverterTurbineCriticalSpeedAnalysis)

        @property
        def unbalanced_mass_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6634
            
            return self._parent._cast(_6634.UnbalancedMassCriticalSpeedAnalysis)

        @property
        def virtual_component_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6635
            
            return self._parent._cast(_6635.VirtualComponentCriticalSpeedAnalysis)

        @property
        def worm_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6636
            
            return self._parent._cast(_6636.WormGearCriticalSpeedAnalysis)

        @property
        def worm_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6638
            
            return self._parent._cast(_6638.WormGearSetCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6639
            
            return self._parent._cast(_6639.ZerolBevelGearCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6641
            
            return self._parent._cast(_6641.ZerolBevelGearSetCriticalSpeedAnalysis)

        @property
        def abstract_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6774
            
            return self._parent._cast(_6774.AbstractAssemblyLoadCase)

        @property
        def abstract_shaft_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6775
            
            return self._parent._cast(_6775.AbstractShaftLoadCase)

        @property
        def abstract_shaft_or_housing_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6776
            
            return self._parent._cast(_6776.AbstractShaftOrHousingLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6781
            
            return self._parent._cast(_6781.AGMAGleasonConicalGearLoadCase)

        @property
        def agma_gleason_conical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6783
            
            return self._parent._cast(_6783.AGMAGleasonConicalGearSetLoadCase)

        @property
        def assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6786
            
            return self._parent._cast(_6786.AssemblyLoadCase)

        @property
        def bearing_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6787
            
            return self._parent._cast(_6787.BearingLoadCase)

        @property
        def belt_drive_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6789
            
            return self._parent._cast(_6789.BeltDriveLoadCase)

        @property
        def bevel_differential_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6790
            
            return self._parent._cast(_6790.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6792
            
            return self._parent._cast(_6792.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6793
            
            return self._parent._cast(_6793.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6794
            
            return self._parent._cast(_6794.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6795
            
            return self._parent._cast(_6795.BevelGearLoadCase)

        @property
        def bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6797
            
            return self._parent._cast(_6797.BevelGearSetLoadCase)

        @property
        def bolted_joint_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6798
            
            return self._parent._cast(_6798.BoltedJointLoadCase)

        @property
        def bolt_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6799
            
            return self._parent._cast(_6799.BoltLoadCase)

        @property
        def clutch_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6801
            
            return self._parent._cast(_6801.ClutchHalfLoadCase)

        @property
        def clutch_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6802
            
            return self._parent._cast(_6802.ClutchLoadCase)

        @property
        def component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6805
            
            return self._parent._cast(_6805.ComponentLoadCase)

        @property
        def concept_coupling_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6807
            
            return self._parent._cast(_6807.ConceptCouplingHalfLoadCase)

        @property
        def concept_coupling_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6808
            
            return self._parent._cast(_6808.ConceptCouplingLoadCase)

        @property
        def concept_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6809
            
            return self._parent._cast(_6809.ConceptGearLoadCase)

        @property
        def concept_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6811
            
            return self._parent._cast(_6811.ConceptGearSetLoadCase)

        @property
        def conical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6812
            
            return self._parent._cast(_6812.ConicalGearLoadCase)

        @property
        def conical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6816
            
            return self._parent._cast(_6816.ConicalGearSetLoadCase)

        @property
        def connector_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6818
            
            return self._parent._cast(_6818.ConnectorLoadCase)

        @property
        def coupling_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6820
            
            return self._parent._cast(_6820.CouplingHalfLoadCase)

        @property
        def coupling_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6821
            
            return self._parent._cast(_6821.CouplingLoadCase)

        @property
        def cvt_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6823
            
            return self._parent._cast(_6823.CVTLoadCase)

        @property
        def cvt_pulley_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6824
            
            return self._parent._cast(_6824.CVTPulleyLoadCase)

        @property
        def cycloidal_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6825
            
            return self._parent._cast(_6825.CycloidalAssemblyLoadCase)

        @property
        def cycloidal_disc_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6827
            
            return self._parent._cast(_6827.CycloidalDiscLoadCase)

        @property
        def cylindrical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6829
            
            return self._parent._cast(_6829.CylindricalGearLoadCase)

        @property
        def cylindrical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6833
            
            return self._parent._cast(_6833.CylindricalGearSetLoadCase)

        @property
        def cylindrical_planet_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6834
            
            return self._parent._cast(_6834.CylindricalPlanetGearLoadCase)

        @property
        def datum_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6837
            
            return self._parent._cast(_6837.DatumLoadCase)

        @property
        def external_cad_model_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6851
            
            return self._parent._cast(_6851.ExternalCADModelLoadCase)

        @property
        def face_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6852
            
            return self._parent._cast(_6852.FaceGearLoadCase)

        @property
        def face_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6854
            
            return self._parent._cast(_6854.FaceGearSetLoadCase)

        @property
        def fe_part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6855
            
            return self._parent._cast(_6855.FEPartLoadCase)

        @property
        def flexible_pin_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6856
            
            return self._parent._cast(_6856.FlexiblePinAssemblyLoadCase)

        @property
        def gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6858
            
            return self._parent._cast(_6858.GearLoadCase)

        @property
        def gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6863
            
            return self._parent._cast(_6863.GearSetLoadCase)

        @property
        def guide_dxf_model_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6864
            
            return self._parent._cast(_6864.GuideDxfModelLoadCase)

        @property
        def hypoid_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6873
            
            return self._parent._cast(_6873.HypoidGearLoadCase)

        @property
        def hypoid_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6875
            
            return self._parent._cast(_6875.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6880
            
            return self._parent._cast(_6880.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6882
            
            return self._parent._cast(_6882.KlingelnbergCycloPalloidConicalGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6883
            
            return self._parent._cast(_6883.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6885
            
            return self._parent._cast(_6885.KlingelnbergCycloPalloidHypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6886
            
            return self._parent._cast(_6886.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6888
            
            return self._parent._cast(_6888.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)

        @property
        def mass_disc_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6889
            
            return self._parent._cast(_6889.MassDiscLoadCase)

        @property
        def measurement_component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6890
            
            return self._parent._cast(_6890.MeasurementComponentLoadCase)

        @property
        def mountable_component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6892
            
            return self._parent._cast(_6892.MountableComponentLoadCase)

        @property
        def oil_seal_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6894
            
            return self._parent._cast(_6894.OilSealLoadCase)

        @property
        def part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6896
            
            return self._parent._cast(_6896.PartLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6898
            
            return self._parent._cast(_6898.PartToPartShearCouplingHalfLoadCase)

        @property
        def part_to_part_shear_coupling_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6899
            
            return self._parent._cast(_6899.PartToPartShearCouplingLoadCase)

        @property
        def planetary_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6901
            
            return self._parent._cast(_6901.PlanetaryGearSetLoadCase)

        @property
        def planet_carrier_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6903
            
            return self._parent._cast(_6903.PlanetCarrierLoadCase)

        @property
        def point_load_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6906
            
            return self._parent._cast(_6906.PointLoadLoadCase)

        @property
        def power_load_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6907
            
            return self._parent._cast(_6907.PowerLoadLoadCase)

        @property
        def pulley_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6908
            
            return self._parent._cast(_6908.PulleyLoadCase)

        @property
        def ring_pins_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6911
            
            return self._parent._cast(_6911.RingPinsLoadCase)

        @property
        def rolling_ring_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6913
            
            return self._parent._cast(_6913.RollingRingAssemblyLoadCase)

        @property
        def rolling_ring_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6915
            
            return self._parent._cast(_6915.RollingRingLoadCase)

        @property
        def root_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6916
            
            return self._parent._cast(_6916.RootAssemblyLoadCase)

        @property
        def shaft_hub_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6917
            
            return self._parent._cast(_6917.ShaftHubConnectionLoadCase)

        @property
        def shaft_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6918
            
            return self._parent._cast(_6918.ShaftLoadCase)

        @property
        def specialised_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6920
            
            return self._parent._cast(_6920.SpecialisedAssemblyLoadCase)

        @property
        def spiral_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6921
            
            return self._parent._cast(_6921.SpiralBevelGearLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6923
            
            return self._parent._cast(_6923.SpiralBevelGearSetLoadCase)

        @property
        def spring_damper_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6925
            
            return self._parent._cast(_6925.SpringDamperHalfLoadCase)

        @property
        def spring_damper_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6926
            
            return self._parent._cast(_6926.SpringDamperLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6927
            
            return self._parent._cast(_6927.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6929
            
            return self._parent._cast(_6929.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6930
            
            return self._parent._cast(_6930.StraightBevelGearLoadCase)

        @property
        def straight_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6932
            
            return self._parent._cast(_6932.StraightBevelGearSetLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6933
            
            return self._parent._cast(_6933.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6934
            
            return self._parent._cast(_6934.StraightBevelSunGearLoadCase)

        @property
        def synchroniser_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6935
            
            return self._parent._cast(_6935.SynchroniserHalfLoadCase)

        @property
        def synchroniser_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6936
            
            return self._parent._cast(_6936.SynchroniserLoadCase)

        @property
        def synchroniser_part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6937
            
            return self._parent._cast(_6937.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6938
            
            return self._parent._cast(_6938.SynchroniserSleeveLoadCase)

        @property
        def torque_converter_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6941
            
            return self._parent._cast(_6941.TorqueConverterLoadCase)

        @property
        def torque_converter_pump_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6942
            
            return self._parent._cast(_6942.TorqueConverterPumpLoadCase)

        @property
        def torque_converter_turbine_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6943
            
            return self._parent._cast(_6943.TorqueConverterTurbineLoadCase)

        @property
        def unbalanced_mass_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6948
            
            return self._parent._cast(_6948.UnbalancedMassLoadCase)

        @property
        def virtual_component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6949
            
            return self._parent._cast(_6949.VirtualComponentLoadCase)

        @property
        def worm_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6950
            
            return self._parent._cast(_6950.WormGearLoadCase)

        @property
        def worm_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6952
            
            return self._parent._cast(_6952.WormGearSetLoadCase)

        @property
        def zerol_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6953
            
            return self._parent._cast(_6953.ZerolBevelGearLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6955
            
            return self._parent._cast(_6955.ZerolBevelGearSetLoadCase)

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6973
            
            return self._parent._cast(_6973.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_shaft_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6974
            
            return self._parent._cast(_6974.AbstractShaftAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_shaft_or_housing_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6975
            
            return self._parent._cast(_6975.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation)

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6980
            
            return self._parent._cast(_6980.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6982
            
            return self._parent._cast(_6982.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6983
            
            return self._parent._cast(_6983.AssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bearing_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6985
            
            return self._parent._cast(_6985.BearingAdvancedTimeSteppingAnalysisForModulation)

        @property
        def belt_drive_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6987
            
            return self._parent._cast(_6987.BeltDriveAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6988
            
            return self._parent._cast(_6988.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6990
            
            return self._parent._cast(_6990.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation)

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
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6995
            
            return self._parent._cast(_6995.BevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bolt_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6996
            
            return self._parent._cast(_6996.BoltAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bolted_joint_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6997
            
            return self._parent._cast(_6997.BoltedJointAdvancedTimeSteppingAnalysisForModulation)

        @property
        def clutch_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6998
            
            return self._parent._cast(_6998.ClutchAdvancedTimeSteppingAnalysisForModulation)

        @property
        def clutch_half_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7000
            
            return self._parent._cast(_7000.ClutchHalfAdvancedTimeSteppingAnalysisForModulation)

        @property
        def component_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7002
            
            return self._parent._cast(_7002.ComponentAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_coupling_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7003
            
            return self._parent._cast(_7003.ConceptCouplingAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_coupling_half_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7005
            
            return self._parent._cast(_7005.ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7006
            
            return self._parent._cast(_7006.ConceptGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7008
            
            return self._parent._cast(_7008.ConceptGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7009
            
            return self._parent._cast(_7009.ConicalGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7011
            
            return self._parent._cast(_7011.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def connector_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7013
            
            return self._parent._cast(_7013.ConnectorAdvancedTimeSteppingAnalysisForModulation)

        @property
        def coupling_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7014
            
            return self._parent._cast(_7014.CouplingAdvancedTimeSteppingAnalysisForModulation)

        @property
        def coupling_half_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7016
            
            return self._parent._cast(_7016.CouplingHalfAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cvt_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7017
            
            return self._parent._cast(_7017.CVTAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cvt_pulley_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7019
            
            return self._parent._cast(_7019.CVTPulleyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cycloidal_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7020
            
            return self._parent._cast(_7020.CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cycloidal_disc_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7021
            
            return self._parent._cast(_7021.CycloidalDiscAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cylindrical_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7024
            
            return self._parent._cast(_7024.CylindricalGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cylindrical_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7026
            
            return self._parent._cast(_7026.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cylindrical_planet_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7027
            
            return self._parent._cast(_7027.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def datum_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7028
            
            return self._parent._cast(_7028.DatumAdvancedTimeSteppingAnalysisForModulation)

        @property
        def external_cad_model_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7029
            
            return self._parent._cast(_7029.ExternalCADModelAdvancedTimeSteppingAnalysisForModulation)

        @property
        def face_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7030
            
            return self._parent._cast(_7030.FaceGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def face_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7032
            
            return self._parent._cast(_7032.FaceGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def fe_part_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7033
            
            return self._parent._cast(_7033.FEPartAdvancedTimeSteppingAnalysisForModulation)

        @property
        def flexible_pin_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7034
            
            return self._parent._cast(_7034.FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7035
            
            return self._parent._cast(_7035.GearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7037
            
            return self._parent._cast(_7037.GearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def guide_dxf_model_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7038
            
            return self._parent._cast(_7038.GuideDxfModelAdvancedTimeSteppingAnalysisForModulation)

        @property
        def hypoid_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7040
            
            return self._parent._cast(_7040.HypoidGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7042
            
            return self._parent._cast(_7042.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7044
            
            return self._parent._cast(_7044.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7046
            
            return self._parent._cast(_7046.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7047
            
            return self._parent._cast(_7047.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7049
            
            return self._parent._cast(_7049.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7050
            
            return self._parent._cast(_7050.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7052
            
            return self._parent._cast(_7052.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def mass_disc_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7053
            
            return self._parent._cast(_7053.MassDiscAdvancedTimeSteppingAnalysisForModulation)

        @property
        def measurement_component_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7054
            
            return self._parent._cast(_7054.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation)

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7055
            
            return self._parent._cast(_7055.MountableComponentAdvancedTimeSteppingAnalysisForModulation)

        @property
        def oil_seal_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7056
            
            return self._parent._cast(_7056.OilSealAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7057
            
            return self._parent._cast(_7057.PartAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_to_part_shear_coupling_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7058
            
            return self._parent._cast(_7058.PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_to_part_shear_coupling_half_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7060
            
            return self._parent._cast(_7060.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation)

        @property
        def planetary_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7062
            
            return self._parent._cast(_7062.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def planet_carrier_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7063
            
            return self._parent._cast(_7063.PlanetCarrierAdvancedTimeSteppingAnalysisForModulation)

        @property
        def point_load_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7064
            
            return self._parent._cast(_7064.PointLoadAdvancedTimeSteppingAnalysisForModulation)

        @property
        def power_load_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7065
            
            return self._parent._cast(_7065.PowerLoadAdvancedTimeSteppingAnalysisForModulation)

        @property
        def pulley_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7066
            
            return self._parent._cast(_7066.PulleyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def ring_pins_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7067
            
            return self._parent._cast(_7067.RingPinsAdvancedTimeSteppingAnalysisForModulation)

        @property
        def rolling_ring_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7069
            
            return self._parent._cast(_7069.RollingRingAdvancedTimeSteppingAnalysisForModulation)

        @property
        def rolling_ring_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7070
            
            return self._parent._cast(_7070.RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def root_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7072
            
            return self._parent._cast(_7072.RootAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def shaft_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7073
            
            return self._parent._cast(_7073.ShaftAdvancedTimeSteppingAnalysisForModulation)

        @property
        def shaft_hub_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7074
            
            return self._parent._cast(_7074.ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7076
            
            return self._parent._cast(_7076.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7077
            
            return self._parent._cast(_7077.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7079
            
            return self._parent._cast(_7079.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spring_damper_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7080
            
            return self._parent._cast(_7080.SpringDamperAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spring_damper_half_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7082
            
            return self._parent._cast(_7082.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_diff_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7083
            
            return self._parent._cast(_7083.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_diff_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7085
            
            return self._parent._cast(_7085.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7086
            
            return self._parent._cast(_7086.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7088
            
            return self._parent._cast(_7088.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_planet_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7089
            
            return self._parent._cast(_7089.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_sun_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7090
            
            return self._parent._cast(_7090.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def synchroniser_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7091
            
            return self._parent._cast(_7091.SynchroniserAdvancedTimeSteppingAnalysisForModulation)

        @property
        def synchroniser_half_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7092
            
            return self._parent._cast(_7092.SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation)

        @property
        def synchroniser_part_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7093
            
            return self._parent._cast(_7093.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation)

        @property
        def synchroniser_sleeve_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7094
            
            return self._parent._cast(_7094.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation)

        @property
        def torque_converter_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7095
            
            return self._parent._cast(_7095.TorqueConverterAdvancedTimeSteppingAnalysisForModulation)

        @property
        def torque_converter_pump_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7097
            
            return self._parent._cast(_7097.TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation)

        @property
        def torque_converter_turbine_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7098
            
            return self._parent._cast(_7098.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation)

        @property
        def unbalanced_mass_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7099
            
            return self._parent._cast(_7099.UnbalancedMassAdvancedTimeSteppingAnalysisForModulation)

        @property
        def virtual_component_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7100
            
            return self._parent._cast(_7100.VirtualComponentAdvancedTimeSteppingAnalysisForModulation)

        @property
        def worm_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7101
            
            return self._parent._cast(_7101.WormGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def worm_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7103
            
            return self._parent._cast(_7103.WormGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def zerol_bevel_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7104
            
            return self._parent._cast(_7104.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def zerol_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7106
            
            return self._parent._cast(_7106.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_assembly_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7236
            
            return self._parent._cast(_7236.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def abstract_shaft_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7237
            
            return self._parent._cast(_7237.AbstractShaftAdvancedSystemDeflection)

        @property
        def abstract_shaft_or_housing_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7238
            
            return self._parent._cast(_7238.AbstractShaftOrHousingAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7243
            
            return self._parent._cast(_7243.AGMAGleasonConicalGearAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7245
            
            return self._parent._cast(_7245.AGMAGleasonConicalGearSetAdvancedSystemDeflection)

        @property
        def assembly_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7246
            
            return self._parent._cast(_7246.AssemblyAdvancedSystemDeflection)

        @property
        def bearing_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7247
            
            return self._parent._cast(_7247.BearingAdvancedSystemDeflection)

        @property
        def belt_drive_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7249
            
            return self._parent._cast(_7249.BeltDriveAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7250
            
            return self._parent._cast(_7250.BevelDifferentialGearAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7252
            
            return self._parent._cast(_7252.BevelDifferentialGearSetAdvancedSystemDeflection)

        @property
        def bevel_differential_planet_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7253
            
            return self._parent._cast(_7253.BevelDifferentialPlanetGearAdvancedSystemDeflection)

        @property
        def bevel_differential_sun_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7254
            
            return self._parent._cast(_7254.BevelDifferentialSunGearAdvancedSystemDeflection)

        @property
        def bevel_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7255
            
            return self._parent._cast(_7255.BevelGearAdvancedSystemDeflection)

        @property
        def bevel_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7257
            
            return self._parent._cast(_7257.BevelGearSetAdvancedSystemDeflection)

        @property
        def bolt_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7258
            
            return self._parent._cast(_7258.BoltAdvancedSystemDeflection)

        @property
        def bolted_joint_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7259
            
            return self._parent._cast(_7259.BoltedJointAdvancedSystemDeflection)

        @property
        def clutch_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7260
            
            return self._parent._cast(_7260.ClutchAdvancedSystemDeflection)

        @property
        def clutch_half_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7262
            
            return self._parent._cast(_7262.ClutchHalfAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7264
            
            return self._parent._cast(_7264.ComponentAdvancedSystemDeflection)

        @property
        def concept_coupling_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7265
            
            return self._parent._cast(_7265.ConceptCouplingAdvancedSystemDeflection)

        @property
        def concept_coupling_half_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7267
            
            return self._parent._cast(_7267.ConceptCouplingHalfAdvancedSystemDeflection)

        @property
        def concept_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7268
            
            return self._parent._cast(_7268.ConceptGearAdvancedSystemDeflection)

        @property
        def concept_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7270
            
            return self._parent._cast(_7270.ConceptGearSetAdvancedSystemDeflection)

        @property
        def conical_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7271
            
            return self._parent._cast(_7271.ConicalGearAdvancedSystemDeflection)

        @property
        def conical_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7273
            
            return self._parent._cast(_7273.ConicalGearSetAdvancedSystemDeflection)

        @property
        def connector_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7275
            
            return self._parent._cast(_7275.ConnectorAdvancedSystemDeflection)

        @property
        def coupling_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7277
            
            return self._parent._cast(_7277.CouplingAdvancedSystemDeflection)

        @property
        def coupling_half_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7279
            
            return self._parent._cast(_7279.CouplingHalfAdvancedSystemDeflection)

        @property
        def cvt_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7280
            
            return self._parent._cast(_7280.CVTAdvancedSystemDeflection)

        @property
        def cvt_pulley_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7282
            
            return self._parent._cast(_7282.CVTPulleyAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7283
            
            return self._parent._cast(_7283.CycloidalAssemblyAdvancedSystemDeflection)

        @property
        def cycloidal_disc_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7284
            
            return self._parent._cast(_7284.CycloidalDiscAdvancedSystemDeflection)

        @property
        def cylindrical_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7287
            
            return self._parent._cast(_7287.CylindricalGearAdvancedSystemDeflection)

        @property
        def cylindrical_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7289
            
            return self._parent._cast(_7289.CylindricalGearSetAdvancedSystemDeflection)

        @property
        def cylindrical_planet_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7291
            
            return self._parent._cast(_7291.CylindricalPlanetGearAdvancedSystemDeflection)

        @property
        def datum_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7292
            
            return self._parent._cast(_7292.DatumAdvancedSystemDeflection)

        @property
        def external_cad_model_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7293
            
            return self._parent._cast(_7293.ExternalCADModelAdvancedSystemDeflection)

        @property
        def face_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7294
            
            return self._parent._cast(_7294.FaceGearAdvancedSystemDeflection)

        @property
        def face_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7296
            
            return self._parent._cast(_7296.FaceGearSetAdvancedSystemDeflection)

        @property
        def fe_part_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7297
            
            return self._parent._cast(_7297.FEPartAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7298
            
            return self._parent._cast(_7298.FlexiblePinAssemblyAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7299
            
            return self._parent._cast(_7299.GearAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7301
            
            return self._parent._cast(_7301.GearSetAdvancedSystemDeflection)

        @property
        def guide_dxf_model_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7302
            
            return self._parent._cast(_7302.GuideDxfModelAdvancedSystemDeflection)

        @property
        def hypoid_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7303
            
            return self._parent._cast(_7303.HypoidGearAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7305
            
            return self._parent._cast(_7305.HypoidGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7307
            
            return self._parent._cast(_7307.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7309
            
            return self._parent._cast(_7309.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7310
            
            return self._parent._cast(_7310.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7312
            
            return self._parent._cast(_7312.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7313
            
            return self._parent._cast(_7313.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7315
            
            return self._parent._cast(_7315.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def mass_disc_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7317
            
            return self._parent._cast(_7317.MassDiscAdvancedSystemDeflection)

        @property
        def measurement_component_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7318
            
            return self._parent._cast(_7318.MeasurementComponentAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7319
            
            return self._parent._cast(_7319.MountableComponentAdvancedSystemDeflection)

        @property
        def oil_seal_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7320
            
            return self._parent._cast(_7320.OilSealAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7321
            
            return self._parent._cast(_7321.PartAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7322
            
            return self._parent._cast(_7322.PartToPartShearCouplingAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7324
            
            return self._parent._cast(_7324.PartToPartShearCouplingHalfAdvancedSystemDeflection)

        @property
        def planetary_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7326
            
            return self._parent._cast(_7326.PlanetaryGearSetAdvancedSystemDeflection)

        @property
        def planet_carrier_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7327
            
            return self._parent._cast(_7327.PlanetCarrierAdvancedSystemDeflection)

        @property
        def point_load_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7328
            
            return self._parent._cast(_7328.PointLoadAdvancedSystemDeflection)

        @property
        def power_load_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7329
            
            return self._parent._cast(_7329.PowerLoadAdvancedSystemDeflection)

        @property
        def pulley_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7330
            
            return self._parent._cast(_7330.PulleyAdvancedSystemDeflection)

        @property
        def ring_pins_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7331
            
            return self._parent._cast(_7331.RingPinsAdvancedSystemDeflection)

        @property
        def rolling_ring_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7333
            
            return self._parent._cast(_7333.RollingRingAdvancedSystemDeflection)

        @property
        def rolling_ring_assembly_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7334
            
            return self._parent._cast(_7334.RollingRingAssemblyAdvancedSystemDeflection)

        @property
        def root_assembly_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7336
            
            return self._parent._cast(_7336.RootAssemblyAdvancedSystemDeflection)

        @property
        def shaft_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7337
            
            return self._parent._cast(_7337.ShaftAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7338
            
            return self._parent._cast(_7338.ShaftHubConnectionAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7340
            
            return self._parent._cast(_7340.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7341
            
            return self._parent._cast(_7341.SpiralBevelGearAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7343
            
            return self._parent._cast(_7343.SpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def spring_damper_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7344
            
            return self._parent._cast(_7344.SpringDamperAdvancedSystemDeflection)

        @property
        def spring_damper_half_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7346
            
            return self._parent._cast(_7346.SpringDamperHalfAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7347
            
            return self._parent._cast(_7347.StraightBevelDiffGearAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7349
            
            return self._parent._cast(_7349.StraightBevelDiffGearSetAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7350
            
            return self._parent._cast(_7350.StraightBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7352
            
            return self._parent._cast(_7352.StraightBevelGearSetAdvancedSystemDeflection)

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7353
            
            return self._parent._cast(_7353.StraightBevelPlanetGearAdvancedSystemDeflection)

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7354
            
            return self._parent._cast(_7354.StraightBevelSunGearAdvancedSystemDeflection)

        @property
        def synchroniser_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7355
            
            return self._parent._cast(_7355.SynchroniserAdvancedSystemDeflection)

        @property
        def synchroniser_half_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7356
            
            return self._parent._cast(_7356.SynchroniserHalfAdvancedSystemDeflection)

        @property
        def synchroniser_part_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7357
            
            return self._parent._cast(_7357.SynchroniserPartAdvancedSystemDeflection)

        @property
        def synchroniser_sleeve_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7358
            
            return self._parent._cast(_7358.SynchroniserSleeveAdvancedSystemDeflection)

        @property
        def torque_converter_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7359
            
            return self._parent._cast(_7359.TorqueConverterAdvancedSystemDeflection)

        @property
        def torque_converter_pump_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7361
            
            return self._parent._cast(_7361.TorqueConverterPumpAdvancedSystemDeflection)

        @property
        def torque_converter_turbine_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7362
            
            return self._parent._cast(_7362.TorqueConverterTurbineAdvancedSystemDeflection)

        @property
        def unbalanced_mass_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7364
            
            return self._parent._cast(_7364.UnbalancedMassAdvancedSystemDeflection)

        @property
        def virtual_component_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7365
            
            return self._parent._cast(_7365.VirtualComponentAdvancedSystemDeflection)

        @property
        def worm_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7366
            
            return self._parent._cast(_7366.WormGearAdvancedSystemDeflection)

        @property
        def worm_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7368
            
            return self._parent._cast(_7368.WormGearSetAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7369
            
            return self._parent._cast(_7369.ZerolBevelGearAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7371
            
            return self._parent._cast(_7371.ZerolBevelGearSetAdvancedSystemDeflection)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7511
            
            return self._parent._cast(_7511.PartAnalysisCase)

        @property
        def part_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7513
            
            return self._parent._cast(_7513.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7514
            
            return self._parent._cast(_7514.PartStaticLoadAnalysisCase)

        @property
        def part_time_series_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7515
            
            return self._parent._cast(_7515.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis(self) -> 'PartAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetary_original(self) -> 'PartAnalysis':
        """PartAnalysis: 'PlanetaryOriginal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetaryOriginal

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PartAnalysis._Cast_PartAnalysis':
        return self._Cast_PartAnalysis(self)
