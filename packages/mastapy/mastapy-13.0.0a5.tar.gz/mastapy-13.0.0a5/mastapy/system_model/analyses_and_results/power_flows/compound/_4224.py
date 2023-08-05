"""_4224.py

PartCompoundPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7512
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'PartCompoundPowerFlow')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4092


__docformat__ = 'restructuredtext en'
__all__ = ('PartCompoundPowerFlow',)


class PartCompoundPowerFlow(_7512.PartCompoundAnalysis):
    """PartCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_POWER_FLOW

    class _Cast_PartCompoundPowerFlow:
        """Special nested class for casting PartCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'PartCompoundPowerFlow'):
            self._parent = parent

        @property
        def part_compound_analysis(self):
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
        def abstract_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4145
            
            return self._parent._cast(_4145.AbstractAssemblyCompoundPowerFlow)

        @property
        def abstract_shaft_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4146
            
            return self._parent._cast(_4146.AbstractShaftCompoundPowerFlow)

        @property
        def abstract_shaft_or_housing_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4147
            
            return self._parent._cast(_4147.AbstractShaftOrHousingCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4149
            
            return self._parent._cast(_4149.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4151
            
            return self._parent._cast(_4151.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4152
            
            return self._parent._cast(_4152.AssemblyCompoundPowerFlow)

        @property
        def bearing_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4153
            
            return self._parent._cast(_4153.BearingCompoundPowerFlow)

        @property
        def belt_drive_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4155
            
            return self._parent._cast(_4155.BeltDriveCompoundPowerFlow)

        @property
        def bevel_differential_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4156
            
            return self._parent._cast(_4156.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4158
            
            return self._parent._cast(_4158.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4159
            
            return self._parent._cast(_4159.BevelDifferentialPlanetGearCompoundPowerFlow)

        @property
        def bevel_differential_sun_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4160
            
            return self._parent._cast(_4160.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4161
            
            return self._parent._cast(_4161.BevelGearCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4163
            
            return self._parent._cast(_4163.BevelGearSetCompoundPowerFlow)

        @property
        def bolt_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4164
            
            return self._parent._cast(_4164.BoltCompoundPowerFlow)

        @property
        def bolted_joint_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4165
            
            return self._parent._cast(_4165.BoltedJointCompoundPowerFlow)

        @property
        def clutch_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4166
            
            return self._parent._cast(_4166.ClutchCompoundPowerFlow)

        @property
        def clutch_half_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4168
            
            return self._parent._cast(_4168.ClutchHalfCompoundPowerFlow)

        @property
        def component_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4170
            
            return self._parent._cast(_4170.ComponentCompoundPowerFlow)

        @property
        def concept_coupling_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4171
            
            return self._parent._cast(_4171.ConceptCouplingCompoundPowerFlow)

        @property
        def concept_coupling_half_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4173
            
            return self._parent._cast(_4173.ConceptCouplingHalfCompoundPowerFlow)

        @property
        def concept_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4174
            
            return self._parent._cast(_4174.ConceptGearCompoundPowerFlow)

        @property
        def concept_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4176
            
            return self._parent._cast(_4176.ConceptGearSetCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4177
            
            return self._parent._cast(_4177.ConicalGearCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4179
            
            return self._parent._cast(_4179.ConicalGearSetCompoundPowerFlow)

        @property
        def connector_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4181
            
            return self._parent._cast(_4181.ConnectorCompoundPowerFlow)

        @property
        def coupling_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4182
            
            return self._parent._cast(_4182.CouplingCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4184
            
            return self._parent._cast(_4184.CouplingHalfCompoundPowerFlow)

        @property
        def cvt_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4186
            
            return self._parent._cast(_4186.CVTCompoundPowerFlow)

        @property
        def cvt_pulley_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4187
            
            return self._parent._cast(_4187.CVTPulleyCompoundPowerFlow)

        @property
        def cycloidal_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4188
            
            return self._parent._cast(_4188.CycloidalAssemblyCompoundPowerFlow)

        @property
        def cycloidal_disc_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4190
            
            return self._parent._cast(_4190.CycloidalDiscCompoundPowerFlow)

        @property
        def cylindrical_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4192
            
            return self._parent._cast(_4192.CylindricalGearCompoundPowerFlow)

        @property
        def cylindrical_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4194
            
            return self._parent._cast(_4194.CylindricalGearSetCompoundPowerFlow)

        @property
        def cylindrical_planet_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4195
            
            return self._parent._cast(_4195.CylindricalPlanetGearCompoundPowerFlow)

        @property
        def datum_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4196
            
            return self._parent._cast(_4196.DatumCompoundPowerFlow)

        @property
        def external_cad_model_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4197
            
            return self._parent._cast(_4197.ExternalCADModelCompoundPowerFlow)

        @property
        def face_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4198
            
            return self._parent._cast(_4198.FaceGearCompoundPowerFlow)

        @property
        def face_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4200
            
            return self._parent._cast(_4200.FaceGearSetCompoundPowerFlow)

        @property
        def fe_part_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4201
            
            return self._parent._cast(_4201.FEPartCompoundPowerFlow)

        @property
        def flexible_pin_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4202
            
            return self._parent._cast(_4202.FlexiblePinAssemblyCompoundPowerFlow)

        @property
        def gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4203
            
            return self._parent._cast(_4203.GearCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4205
            
            return self._parent._cast(_4205.GearSetCompoundPowerFlow)

        @property
        def guide_dxf_model_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4206
            
            return self._parent._cast(_4206.GuideDxfModelCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4207
            
            return self._parent._cast(_4207.HypoidGearCompoundPowerFlow)

        @property
        def hypoid_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4209
            
            return self._parent._cast(_4209.HypoidGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4211
            
            return self._parent._cast(_4211.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4213
            
            return self._parent._cast(_4213.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4214
            
            return self._parent._cast(_4214.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4216
            
            return self._parent._cast(_4216.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4217
            
            return self._parent._cast(_4217.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4219
            
            return self._parent._cast(_4219.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow)

        @property
        def mass_disc_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4220
            
            return self._parent._cast(_4220.MassDiscCompoundPowerFlow)

        @property
        def measurement_component_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4221
            
            return self._parent._cast(_4221.MeasurementComponentCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4222
            
            return self._parent._cast(_4222.MountableComponentCompoundPowerFlow)

        @property
        def oil_seal_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4223
            
            return self._parent._cast(_4223.OilSealCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4225
            
            return self._parent._cast(_4225.PartToPartShearCouplingCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_half_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4227
            
            return self._parent._cast(_4227.PartToPartShearCouplingHalfCompoundPowerFlow)

        @property
        def planetary_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4229
            
            return self._parent._cast(_4229.PlanetaryGearSetCompoundPowerFlow)

        @property
        def planet_carrier_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4230
            
            return self._parent._cast(_4230.PlanetCarrierCompoundPowerFlow)

        @property
        def point_load_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4231
            
            return self._parent._cast(_4231.PointLoadCompoundPowerFlow)

        @property
        def power_load_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4232
            
            return self._parent._cast(_4232.PowerLoadCompoundPowerFlow)

        @property
        def pulley_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4233
            
            return self._parent._cast(_4233.PulleyCompoundPowerFlow)

        @property
        def ring_pins_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4234
            
            return self._parent._cast(_4234.RingPinsCompoundPowerFlow)

        @property
        def rolling_ring_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4236
            
            return self._parent._cast(_4236.RollingRingAssemblyCompoundPowerFlow)

        @property
        def rolling_ring_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4237
            
            return self._parent._cast(_4237.RollingRingCompoundPowerFlow)

        @property
        def root_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4239
            
            return self._parent._cast(_4239.RootAssemblyCompoundPowerFlow)

        @property
        def shaft_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4240
            
            return self._parent._cast(_4240.ShaftCompoundPowerFlow)

        @property
        def shaft_hub_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4241
            
            return self._parent._cast(_4241.ShaftHubConnectionCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4243
            
            return self._parent._cast(_4243.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def spiral_bevel_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4244
            
            return self._parent._cast(_4244.SpiralBevelGearCompoundPowerFlow)

        @property
        def spiral_bevel_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4246
            
            return self._parent._cast(_4246.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def spring_damper_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4247
            
            return self._parent._cast(_4247.SpringDamperCompoundPowerFlow)

        @property
        def spring_damper_half_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4249
            
            return self._parent._cast(_4249.SpringDamperHalfCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4250
            
            return self._parent._cast(_4250.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4252
            
            return self._parent._cast(_4252.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4253
            
            return self._parent._cast(_4253.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4255
            
            return self._parent._cast(_4255.StraightBevelGearSetCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4256
            
            return self._parent._cast(_4256.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4257
            
            return self._parent._cast(_4257.StraightBevelSunGearCompoundPowerFlow)

        @property
        def synchroniser_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4258
            
            return self._parent._cast(_4258.SynchroniserCompoundPowerFlow)

        @property
        def synchroniser_half_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4259
            
            return self._parent._cast(_4259.SynchroniserHalfCompoundPowerFlow)

        @property
        def synchroniser_part_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4260
            
            return self._parent._cast(_4260.SynchroniserPartCompoundPowerFlow)

        @property
        def synchroniser_sleeve_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4261
            
            return self._parent._cast(_4261.SynchroniserSleeveCompoundPowerFlow)

        @property
        def torque_converter_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4262
            
            return self._parent._cast(_4262.TorqueConverterCompoundPowerFlow)

        @property
        def torque_converter_pump_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4264
            
            return self._parent._cast(_4264.TorqueConverterPumpCompoundPowerFlow)

        @property
        def torque_converter_turbine_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4265
            
            return self._parent._cast(_4265.TorqueConverterTurbineCompoundPowerFlow)

        @property
        def unbalanced_mass_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4266
            
            return self._parent._cast(_4266.UnbalancedMassCompoundPowerFlow)

        @property
        def virtual_component_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4267
            
            return self._parent._cast(_4267.VirtualComponentCompoundPowerFlow)

        @property
        def worm_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4268
            
            return self._parent._cast(_4268.WormGearCompoundPowerFlow)

        @property
        def worm_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4270
            
            return self._parent._cast(_4270.WormGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4271
            
            return self._parent._cast(_4271.ZerolBevelGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4273
            
            return self._parent._cast(_4273.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def part_compound_power_flow(self) -> 'PartCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4092.PartPowerFlow]':
        """List[PartPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4092.PartPowerFlow]':
        """List[PartPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PartCompoundPowerFlow._Cast_PartCompoundPowerFlow':
        return self._Cast_PartCompoundPowerFlow(self)
