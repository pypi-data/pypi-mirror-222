"""_4638.py

PartModalAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7514
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'PartModalAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2451
    from mastapy.system_model.analyses_and_results.modal_analyses import _2617
    from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4702, _4700, _4703
    from mastapy.system_model.analyses_and_results.system_deflections import _2767
    from mastapy.system_model.drawing import _2234


__docformat__ = 'restructuredtext en'
__all__ = ('PartModalAnalysis',)


class PartModalAnalysis(_7514.PartStaticLoadAnalysisCase):
    """PartModalAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_MODAL_ANALYSIS

    class _Cast_PartModalAnalysis:
        """Special nested class for casting PartModalAnalysis to subclasses."""

        def __init__(self, parent: 'PartModalAnalysis'):
            self._parent = parent

        @property
        def part_static_load_analysis_case(self):
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
        def part_modal_analysis(self) -> 'PartModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def modal_analysis(self) -> '_2617.ModalAnalysis':
        """ModalAnalysis: 'ModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excited_modes_summary(self) -> 'List[_4702.SingleExcitationResultsModalAnalysis]':
        """List[SingleExcitationResultsModalAnalysis]: 'ExcitedModesSummary' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitedModesSummary

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_mesh_excitation_details(self) -> 'List[_4700.RigidlyConnectedDesignEntityGroupModalAnalysis]':
        """List[RigidlyConnectedDesignEntityGroupModalAnalysis]: 'GearMeshExcitationDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshExcitationDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def results_for_modes(self) -> 'List[_4703.SingleModeResults]':
        """List[SingleModeResults]: 'ResultsForModes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultsForModes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shaft_excitation_details(self) -> 'List[_4700.RigidlyConnectedDesignEntityGroupModalAnalysis]':
        """List[RigidlyConnectedDesignEntityGroupModalAnalysis]: 'ShaftExcitationDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftExcitationDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def system_deflection_results(self) -> '_2767.PartSystemDeflection':
        """PartSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def create_viewable(self) -> '_2234.ModalAnalysisViewable':
        """ 'CreateViewable' is the original name of this method.

        Returns:
            mastapy.system_model.drawing.ModalAnalysisViewable
        """

        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'PartModalAnalysis._Cast_PartModalAnalysis':
        return self._Cast_PartModalAnalysis(self)
