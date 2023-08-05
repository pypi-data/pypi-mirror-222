"""_2767.py

PartSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7513
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'PartSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2451
    from mastapy.math_utility import _1508
    from mastapy.system_model.analyses_and_results.system_deflections import _2807
    from mastapy.system_model.analyses_and_results.power_flows import _4092
    from mastapy.system_model.drawing import _2243


__docformat__ = 'restructuredtext en'
__all__ = ('PartSystemDeflection',)


class PartSystemDeflection(_7513.PartFEAnalysis):
    """PartSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_SYSTEM_DEFLECTION

    class _Cast_PartSystemDeflection:
        """Special nested class for casting PartSystemDeflection to subclasses."""

        def __init__(self, parent: 'PartSystemDeflection'):
            self._parent = parent

        @property
        def part_fe_analysis(self):
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
        def part_system_deflection(self) -> 'PartSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing_showing_axial_forces(self) -> 'Image':
        """Image: 'TwoDDrawingShowingAxialForces' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TwoDDrawingShowingAxialForces

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def two_d_drawing_showing_power_flow(self) -> 'Image':
        """Image: 'TwoDDrawingShowingPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TwoDDrawingShowingPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def component_design(self) -> '_2451.Part':
        """Part: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mass_properties_from_node_model(self) -> '_1508.MassProperties':
        """MassProperties: 'MassPropertiesFromNodeModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassPropertiesFromNodeModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection(self) -> '_2807.SystemDeflection':
        """SystemDeflection: 'SystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4092.PartPowerFlow':
        """PartPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def create_viewable(self) -> '_2243.SystemDeflectionViewable':
        """ 'CreateViewable' is the original name of this method.

        Returns:
            mastapy.system_model.drawing.SystemDeflectionViewable
        """

        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'PartSystemDeflection._Cast_PartSystemDeflection':
        return self._Cast_PartSystemDeflection(self)
