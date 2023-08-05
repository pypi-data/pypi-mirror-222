"""_7451.py

PartCompoundAdvancedSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7512
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'PartCompoundAdvancedSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7321


__docformat__ = 'restructuredtext en'
__all__ = ('PartCompoundAdvancedSystemDeflection',)


class PartCompoundAdvancedSystemDeflection(_7512.PartCompoundAnalysis):
    """PartCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_PartCompoundAdvancedSystemDeflection:
        """Special nested class for casting PartCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'PartCompoundAdvancedSystemDeflection'):
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
        def abstract_assembly_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7372
            
            return self._parent._cast(_7372.AbstractAssemblyCompoundAdvancedSystemDeflection)

        @property
        def abstract_shaft_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7373
            
            return self._parent._cast(_7373.AbstractShaftCompoundAdvancedSystemDeflection)

        @property
        def abstract_shaft_or_housing_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7374
            
            return self._parent._cast(_7374.AbstractShaftOrHousingCompoundAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7376
            
            return self._parent._cast(_7376.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7378
            
            return self._parent._cast(_7378.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection)

        @property
        def assembly_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7379
            
            return self._parent._cast(_7379.AssemblyCompoundAdvancedSystemDeflection)

        @property
        def bearing_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7380
            
            return self._parent._cast(_7380.BearingCompoundAdvancedSystemDeflection)

        @property
        def belt_drive_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7382
            
            return self._parent._cast(_7382.BeltDriveCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7383
            
            return self._parent._cast(_7383.BevelDifferentialGearCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7385
            
            return self._parent._cast(_7385.BevelDifferentialGearSetCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_planet_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7386
            
            return self._parent._cast(_7386.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_sun_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7387
            
            return self._parent._cast(_7387.BevelDifferentialSunGearCompoundAdvancedSystemDeflection)

        @property
        def bevel_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7388
            
            return self._parent._cast(_7388.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def bevel_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7390
            
            return self._parent._cast(_7390.BevelGearSetCompoundAdvancedSystemDeflection)

        @property
        def bolt_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7391
            
            return self._parent._cast(_7391.BoltCompoundAdvancedSystemDeflection)

        @property
        def bolted_joint_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7392
            
            return self._parent._cast(_7392.BoltedJointCompoundAdvancedSystemDeflection)

        @property
        def clutch_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7393
            
            return self._parent._cast(_7393.ClutchCompoundAdvancedSystemDeflection)

        @property
        def clutch_half_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7395
            
            return self._parent._cast(_7395.ClutchHalfCompoundAdvancedSystemDeflection)

        @property
        def component_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7397
            
            return self._parent._cast(_7397.ComponentCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7398
            
            return self._parent._cast(_7398.ConceptCouplingCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_half_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7400
            
            return self._parent._cast(_7400.ConceptCouplingHalfCompoundAdvancedSystemDeflection)

        @property
        def concept_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7401
            
            return self._parent._cast(_7401.ConceptGearCompoundAdvancedSystemDeflection)

        @property
        def concept_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7403
            
            return self._parent._cast(_7403.ConceptGearSetCompoundAdvancedSystemDeflection)

        @property
        def conical_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7404
            
            return self._parent._cast(_7404.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def conical_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7406
            
            return self._parent._cast(_7406.ConicalGearSetCompoundAdvancedSystemDeflection)

        @property
        def connector_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7408
            
            return self._parent._cast(_7408.ConnectorCompoundAdvancedSystemDeflection)

        @property
        def coupling_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7409
            
            return self._parent._cast(_7409.CouplingCompoundAdvancedSystemDeflection)

        @property
        def coupling_half_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7411
            
            return self._parent._cast(_7411.CouplingHalfCompoundAdvancedSystemDeflection)

        @property
        def cvt_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7413
            
            return self._parent._cast(_7413.CVTCompoundAdvancedSystemDeflection)

        @property
        def cvt_pulley_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7414
            
            return self._parent._cast(_7414.CVTPulleyCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7415
            
            return self._parent._cast(_7415.CycloidalAssemblyCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_disc_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7417
            
            return self._parent._cast(_7417.CycloidalDiscCompoundAdvancedSystemDeflection)

        @property
        def cylindrical_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7419
            
            return self._parent._cast(_7419.CylindricalGearCompoundAdvancedSystemDeflection)

        @property
        def cylindrical_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7421
            
            return self._parent._cast(_7421.CylindricalGearSetCompoundAdvancedSystemDeflection)

        @property
        def cylindrical_planet_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7422
            
            return self._parent._cast(_7422.CylindricalPlanetGearCompoundAdvancedSystemDeflection)

        @property
        def datum_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7423
            
            return self._parent._cast(_7423.DatumCompoundAdvancedSystemDeflection)

        @property
        def external_cad_model_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7424
            
            return self._parent._cast(_7424.ExternalCADModelCompoundAdvancedSystemDeflection)

        @property
        def face_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7425
            
            return self._parent._cast(_7425.FaceGearCompoundAdvancedSystemDeflection)

        @property
        def face_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7427
            
            return self._parent._cast(_7427.FaceGearSetCompoundAdvancedSystemDeflection)

        @property
        def fe_part_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7428
            
            return self._parent._cast(_7428.FEPartCompoundAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7429
            
            return self._parent._cast(_7429.FlexiblePinAssemblyCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7430
            
            return self._parent._cast(_7430.GearCompoundAdvancedSystemDeflection)

        @property
        def gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7432
            
            return self._parent._cast(_7432.GearSetCompoundAdvancedSystemDeflection)

        @property
        def guide_dxf_model_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7433
            
            return self._parent._cast(_7433.GuideDxfModelCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7434
            
            return self._parent._cast(_7434.HypoidGearCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7436
            
            return self._parent._cast(_7436.HypoidGearSetCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7438
            
            return self._parent._cast(_7438.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7440
            
            return self._parent._cast(_7440.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7441
            
            return self._parent._cast(_7441.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7443
            
            return self._parent._cast(_7443.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7444
            
            return self._parent._cast(_7444.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7446
            
            return self._parent._cast(_7446.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection)

        @property
        def mass_disc_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7447
            
            return self._parent._cast(_7447.MassDiscCompoundAdvancedSystemDeflection)

        @property
        def measurement_component_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7448
            
            return self._parent._cast(_7448.MeasurementComponentCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7449
            
            return self._parent._cast(_7449.MountableComponentCompoundAdvancedSystemDeflection)

        @property
        def oil_seal_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7450
            
            return self._parent._cast(_7450.OilSealCompoundAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7452
            
            return self._parent._cast(_7452.PartToPartShearCouplingCompoundAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7454
            
            return self._parent._cast(_7454.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection)

        @property
        def planetary_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7456
            
            return self._parent._cast(_7456.PlanetaryGearSetCompoundAdvancedSystemDeflection)

        @property
        def planet_carrier_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7457
            
            return self._parent._cast(_7457.PlanetCarrierCompoundAdvancedSystemDeflection)

        @property
        def point_load_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7458
            
            return self._parent._cast(_7458.PointLoadCompoundAdvancedSystemDeflection)

        @property
        def power_load_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7459
            
            return self._parent._cast(_7459.PowerLoadCompoundAdvancedSystemDeflection)

        @property
        def pulley_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7460
            
            return self._parent._cast(_7460.PulleyCompoundAdvancedSystemDeflection)

        @property
        def ring_pins_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7461
            
            return self._parent._cast(_7461.RingPinsCompoundAdvancedSystemDeflection)

        @property
        def rolling_ring_assembly_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7463
            
            return self._parent._cast(_7463.RollingRingAssemblyCompoundAdvancedSystemDeflection)

        @property
        def rolling_ring_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7464
            
            return self._parent._cast(_7464.RollingRingCompoundAdvancedSystemDeflection)

        @property
        def root_assembly_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7466
            
            return self._parent._cast(_7466.RootAssemblyCompoundAdvancedSystemDeflection)

        @property
        def shaft_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7467
            
            return self._parent._cast(_7467.ShaftCompoundAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7468
            
            return self._parent._cast(_7468.ShaftHubConnectionCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7470
            
            return self._parent._cast(_7470.SpecialisedAssemblyCompoundAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7471
            
            return self._parent._cast(_7471.SpiralBevelGearCompoundAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7473
            
            return self._parent._cast(_7473.SpiralBevelGearSetCompoundAdvancedSystemDeflection)

        @property
        def spring_damper_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7474
            
            return self._parent._cast(_7474.SpringDamperCompoundAdvancedSystemDeflection)

        @property
        def spring_damper_half_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7476
            
            return self._parent._cast(_7476.SpringDamperHalfCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7477
            
            return self._parent._cast(_7477.StraightBevelDiffGearCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7479
            
            return self._parent._cast(_7479.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7480
            
            return self._parent._cast(_7480.StraightBevelGearCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7482
            
            return self._parent._cast(_7482.StraightBevelGearSetCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_planet_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7483
            
            return self._parent._cast(_7483.StraightBevelPlanetGearCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_sun_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7484
            
            return self._parent._cast(_7484.StraightBevelSunGearCompoundAdvancedSystemDeflection)

        @property
        def synchroniser_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7485
            
            return self._parent._cast(_7485.SynchroniserCompoundAdvancedSystemDeflection)

        @property
        def synchroniser_half_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7486
            
            return self._parent._cast(_7486.SynchroniserHalfCompoundAdvancedSystemDeflection)

        @property
        def synchroniser_part_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7487
            
            return self._parent._cast(_7487.SynchroniserPartCompoundAdvancedSystemDeflection)

        @property
        def synchroniser_sleeve_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7488
            
            return self._parent._cast(_7488.SynchroniserSleeveCompoundAdvancedSystemDeflection)

        @property
        def torque_converter_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7489
            
            return self._parent._cast(_7489.TorqueConverterCompoundAdvancedSystemDeflection)

        @property
        def torque_converter_pump_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7491
            
            return self._parent._cast(_7491.TorqueConverterPumpCompoundAdvancedSystemDeflection)

        @property
        def torque_converter_turbine_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7492
            
            return self._parent._cast(_7492.TorqueConverterTurbineCompoundAdvancedSystemDeflection)

        @property
        def unbalanced_mass_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7493
            
            return self._parent._cast(_7493.UnbalancedMassCompoundAdvancedSystemDeflection)

        @property
        def virtual_component_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7494
            
            return self._parent._cast(_7494.VirtualComponentCompoundAdvancedSystemDeflection)

        @property
        def worm_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7495
            
            return self._parent._cast(_7495.WormGearCompoundAdvancedSystemDeflection)

        @property
        def worm_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7497
            
            return self._parent._cast(_7497.WormGearSetCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7498
            
            return self._parent._cast(_7498.ZerolBevelGearCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7500
            
            return self._parent._cast(_7500.ZerolBevelGearSetCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(self) -> 'PartCompoundAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_7321.PartAdvancedSystemDeflection]':
        """List[PartAdvancedSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_7321.PartAdvancedSystemDeflection]':
        """List[PartAdvancedSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection':
        return self._Cast_PartCompoundAdvancedSystemDeflection(self)
