"""_4500.py

PartCompoundParametricStudyTool
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7512
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'PartCompoundParametricStudyTool')

if TYPE_CHECKING:
    from mastapy.utility_gui import _1838
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4371


__docformat__ = 'restructuredtext en'
__all__ = ('PartCompoundParametricStudyTool',)


class PartCompoundParametricStudyTool(_7512.PartCompoundAnalysis):
    """PartCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_PartCompoundParametricStudyTool:
        """Special nested class for casting PartCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'PartCompoundParametricStudyTool'):
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
        def abstract_assembly_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4421
            
            return self._parent._cast(_4421.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def abstract_shaft_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4422
            
            return self._parent._cast(_4422.AbstractShaftCompoundParametricStudyTool)

        @property
        def abstract_shaft_or_housing_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4423
            
            return self._parent._cast(_4423.AbstractShaftOrHousingCompoundParametricStudyTool)

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4425
            
            return self._parent._cast(_4425.AGMAGleasonConicalGearCompoundParametricStudyTool)

        @property
        def agma_gleason_conical_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4427
            
            return self._parent._cast(_4427.AGMAGleasonConicalGearSetCompoundParametricStudyTool)

        @property
        def assembly_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4428
            
            return self._parent._cast(_4428.AssemblyCompoundParametricStudyTool)

        @property
        def bearing_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4429
            
            return self._parent._cast(_4429.BearingCompoundParametricStudyTool)

        @property
        def belt_drive_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4431
            
            return self._parent._cast(_4431.BeltDriveCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4432
            
            return self._parent._cast(_4432.BevelDifferentialGearCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4434
            
            return self._parent._cast(_4434.BevelDifferentialGearSetCompoundParametricStudyTool)

        @property
        def bevel_differential_planet_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4435
            
            return self._parent._cast(_4435.BevelDifferentialPlanetGearCompoundParametricStudyTool)

        @property
        def bevel_differential_sun_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4436
            
            return self._parent._cast(_4436.BevelDifferentialSunGearCompoundParametricStudyTool)

        @property
        def bevel_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4437
            
            return self._parent._cast(_4437.BevelGearCompoundParametricStudyTool)

        @property
        def bevel_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4439
            
            return self._parent._cast(_4439.BevelGearSetCompoundParametricStudyTool)

        @property
        def bolt_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4440
            
            return self._parent._cast(_4440.BoltCompoundParametricStudyTool)

        @property
        def bolted_joint_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4441
            
            return self._parent._cast(_4441.BoltedJointCompoundParametricStudyTool)

        @property
        def clutch_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4442
            
            return self._parent._cast(_4442.ClutchCompoundParametricStudyTool)

        @property
        def clutch_half_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4444
            
            return self._parent._cast(_4444.ClutchHalfCompoundParametricStudyTool)

        @property
        def component_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4446
            
            return self._parent._cast(_4446.ComponentCompoundParametricStudyTool)

        @property
        def concept_coupling_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4447
            
            return self._parent._cast(_4447.ConceptCouplingCompoundParametricStudyTool)

        @property
        def concept_coupling_half_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4449
            
            return self._parent._cast(_4449.ConceptCouplingHalfCompoundParametricStudyTool)

        @property
        def concept_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4450
            
            return self._parent._cast(_4450.ConceptGearCompoundParametricStudyTool)

        @property
        def concept_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4452
            
            return self._parent._cast(_4452.ConceptGearSetCompoundParametricStudyTool)

        @property
        def conical_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4453
            
            return self._parent._cast(_4453.ConicalGearCompoundParametricStudyTool)

        @property
        def conical_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4455
            
            return self._parent._cast(_4455.ConicalGearSetCompoundParametricStudyTool)

        @property
        def connector_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4457
            
            return self._parent._cast(_4457.ConnectorCompoundParametricStudyTool)

        @property
        def coupling_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4458
            
            return self._parent._cast(_4458.CouplingCompoundParametricStudyTool)

        @property
        def coupling_half_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4460
            
            return self._parent._cast(_4460.CouplingHalfCompoundParametricStudyTool)

        @property
        def cvt_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4462
            
            return self._parent._cast(_4462.CVTCompoundParametricStudyTool)

        @property
        def cvt_pulley_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4463
            
            return self._parent._cast(_4463.CVTPulleyCompoundParametricStudyTool)

        @property
        def cycloidal_assembly_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4464
            
            return self._parent._cast(_4464.CycloidalAssemblyCompoundParametricStudyTool)

        @property
        def cycloidal_disc_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4466
            
            return self._parent._cast(_4466.CycloidalDiscCompoundParametricStudyTool)

        @property
        def cylindrical_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4468
            
            return self._parent._cast(_4468.CylindricalGearCompoundParametricStudyTool)

        @property
        def cylindrical_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4470
            
            return self._parent._cast(_4470.CylindricalGearSetCompoundParametricStudyTool)

        @property
        def cylindrical_planet_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4471
            
            return self._parent._cast(_4471.CylindricalPlanetGearCompoundParametricStudyTool)

        @property
        def datum_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4472
            
            return self._parent._cast(_4472.DatumCompoundParametricStudyTool)

        @property
        def external_cad_model_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4473
            
            return self._parent._cast(_4473.ExternalCADModelCompoundParametricStudyTool)

        @property
        def face_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4474
            
            return self._parent._cast(_4474.FaceGearCompoundParametricStudyTool)

        @property
        def face_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4476
            
            return self._parent._cast(_4476.FaceGearSetCompoundParametricStudyTool)

        @property
        def fe_part_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4477
            
            return self._parent._cast(_4477.FEPartCompoundParametricStudyTool)

        @property
        def flexible_pin_assembly_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4478
            
            return self._parent._cast(_4478.FlexiblePinAssemblyCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4479
            
            return self._parent._cast(_4479.GearCompoundParametricStudyTool)

        @property
        def gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4481
            
            return self._parent._cast(_4481.GearSetCompoundParametricStudyTool)

        @property
        def guide_dxf_model_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4482
            
            return self._parent._cast(_4482.GuideDxfModelCompoundParametricStudyTool)

        @property
        def hypoid_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4483
            
            return self._parent._cast(_4483.HypoidGearCompoundParametricStudyTool)

        @property
        def hypoid_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4485
            
            return self._parent._cast(_4485.HypoidGearSetCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4487
            
            return self._parent._cast(_4487.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4489
            
            return self._parent._cast(_4489.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4490
            
            return self._parent._cast(_4490.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4492
            
            return self._parent._cast(_4492.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4493
            
            return self._parent._cast(_4493.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4495
            
            return self._parent._cast(_4495.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool)

        @property
        def mass_disc_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4496
            
            return self._parent._cast(_4496.MassDiscCompoundParametricStudyTool)

        @property
        def measurement_component_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4497
            
            return self._parent._cast(_4497.MeasurementComponentCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4498
            
            return self._parent._cast(_4498.MountableComponentCompoundParametricStudyTool)

        @property
        def oil_seal_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4499
            
            return self._parent._cast(_4499.OilSealCompoundParametricStudyTool)

        @property
        def part_to_part_shear_coupling_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4501
            
            return self._parent._cast(_4501.PartToPartShearCouplingCompoundParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4503
            
            return self._parent._cast(_4503.PartToPartShearCouplingHalfCompoundParametricStudyTool)

        @property
        def planetary_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4505
            
            return self._parent._cast(_4505.PlanetaryGearSetCompoundParametricStudyTool)

        @property
        def planet_carrier_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4506
            
            return self._parent._cast(_4506.PlanetCarrierCompoundParametricStudyTool)

        @property
        def point_load_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4507
            
            return self._parent._cast(_4507.PointLoadCompoundParametricStudyTool)

        @property
        def power_load_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4508
            
            return self._parent._cast(_4508.PowerLoadCompoundParametricStudyTool)

        @property
        def pulley_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4509
            
            return self._parent._cast(_4509.PulleyCompoundParametricStudyTool)

        @property
        def ring_pins_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4510
            
            return self._parent._cast(_4510.RingPinsCompoundParametricStudyTool)

        @property
        def rolling_ring_assembly_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4512
            
            return self._parent._cast(_4512.RollingRingAssemblyCompoundParametricStudyTool)

        @property
        def rolling_ring_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4513
            
            return self._parent._cast(_4513.RollingRingCompoundParametricStudyTool)

        @property
        def root_assembly_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4515
            
            return self._parent._cast(_4515.RootAssemblyCompoundParametricStudyTool)

        @property
        def shaft_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4516
            
            return self._parent._cast(_4516.ShaftCompoundParametricStudyTool)

        @property
        def shaft_hub_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4517
            
            return self._parent._cast(_4517.ShaftHubConnectionCompoundParametricStudyTool)

        @property
        def specialised_assembly_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4519
            
            return self._parent._cast(_4519.SpecialisedAssemblyCompoundParametricStudyTool)

        @property
        def spiral_bevel_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4520
            
            return self._parent._cast(_4520.SpiralBevelGearCompoundParametricStudyTool)

        @property
        def spiral_bevel_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4522
            
            return self._parent._cast(_4522.SpiralBevelGearSetCompoundParametricStudyTool)

        @property
        def spring_damper_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4523
            
            return self._parent._cast(_4523.SpringDamperCompoundParametricStudyTool)

        @property
        def spring_damper_half_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4525
            
            return self._parent._cast(_4525.SpringDamperHalfCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4526
            
            return self._parent._cast(_4526.StraightBevelDiffGearCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4528
            
            return self._parent._cast(_4528.StraightBevelDiffGearSetCompoundParametricStudyTool)

        @property
        def straight_bevel_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4529
            
            return self._parent._cast(_4529.StraightBevelGearCompoundParametricStudyTool)

        @property
        def straight_bevel_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4531
            
            return self._parent._cast(_4531.StraightBevelGearSetCompoundParametricStudyTool)

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4532
            
            return self._parent._cast(_4532.StraightBevelPlanetGearCompoundParametricStudyTool)

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4533
            
            return self._parent._cast(_4533.StraightBevelSunGearCompoundParametricStudyTool)

        @property
        def synchroniser_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4534
            
            return self._parent._cast(_4534.SynchroniserCompoundParametricStudyTool)

        @property
        def synchroniser_half_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4535
            
            return self._parent._cast(_4535.SynchroniserHalfCompoundParametricStudyTool)

        @property
        def synchroniser_part_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4536
            
            return self._parent._cast(_4536.SynchroniserPartCompoundParametricStudyTool)

        @property
        def synchroniser_sleeve_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4537
            
            return self._parent._cast(_4537.SynchroniserSleeveCompoundParametricStudyTool)

        @property
        def torque_converter_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4538
            
            return self._parent._cast(_4538.TorqueConverterCompoundParametricStudyTool)

        @property
        def torque_converter_pump_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4540
            
            return self._parent._cast(_4540.TorqueConverterPumpCompoundParametricStudyTool)

        @property
        def torque_converter_turbine_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4541
            
            return self._parent._cast(_4541.TorqueConverterTurbineCompoundParametricStudyTool)

        @property
        def unbalanced_mass_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4542
            
            return self._parent._cast(_4542.UnbalancedMassCompoundParametricStudyTool)

        @property
        def virtual_component_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4543
            
            return self._parent._cast(_4543.VirtualComponentCompoundParametricStudyTool)

        @property
        def worm_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4544
            
            return self._parent._cast(_4544.WormGearCompoundParametricStudyTool)

        @property
        def worm_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4546
            
            return self._parent._cast(_4546.WormGearSetCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4547
            
            return self._parent._cast(_4547.ZerolBevelGearCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4549
            
            return self._parent._cast(_4549.ZerolBevelGearSetCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(self) -> 'PartCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def data_logger(self) -> '_1838.DataLoggerWithCharts':
        """DataLoggerWithCharts: 'DataLogger' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DataLogger

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases(self) -> 'List[_4371.PartParametricStudyTool]':
        """List[PartParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4371.PartParametricStudyTool]':
        """List[PartParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool':
        return self._Cast_PartCompoundParametricStudyTool(self)
