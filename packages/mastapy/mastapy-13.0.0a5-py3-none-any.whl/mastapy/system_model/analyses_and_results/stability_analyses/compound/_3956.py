"""_3956.py

PartCompoundStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7512
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'PartCompoundStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3825


__docformat__ = 'restructuredtext en'
__all__ = ('PartCompoundStabilityAnalysis',)


class PartCompoundStabilityAnalysis(_7512.PartCompoundAnalysis):
    """PartCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_STABILITY_ANALYSIS

    class _Cast_PartCompoundStabilityAnalysis:
        """Special nested class for casting PartCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'PartCompoundStabilityAnalysis'):
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
        def abstract_assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3877
            
            return self._parent._cast(_3877.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def abstract_shaft_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3878
            
            return self._parent._cast(_3878.AbstractShaftCompoundStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3879
            
            return self._parent._cast(_3879.AbstractShaftOrHousingCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3881
            
            return self._parent._cast(_3881.AGMAGleasonConicalGearCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3883
            
            return self._parent._cast(_3883.AGMAGleasonConicalGearSetCompoundStabilityAnalysis)

        @property
        def assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3884
            
            return self._parent._cast(_3884.AssemblyCompoundStabilityAnalysis)

        @property
        def bearing_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3885
            
            return self._parent._cast(_3885.BearingCompoundStabilityAnalysis)

        @property
        def belt_drive_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3887
            
            return self._parent._cast(_3887.BeltDriveCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3888
            
            return self._parent._cast(_3888.BevelDifferentialGearCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3890
            
            return self._parent._cast(_3890.BevelDifferentialGearSetCompoundStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3891
            
            return self._parent._cast(_3891.BevelDifferentialPlanetGearCompoundStabilityAnalysis)

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3892
            
            return self._parent._cast(_3892.BevelDifferentialSunGearCompoundStabilityAnalysis)

        @property
        def bevel_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3893
            
            return self._parent._cast(_3893.BevelGearCompoundStabilityAnalysis)

        @property
        def bevel_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3895
            
            return self._parent._cast(_3895.BevelGearSetCompoundStabilityAnalysis)

        @property
        def bolt_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3896
            
            return self._parent._cast(_3896.BoltCompoundStabilityAnalysis)

        @property
        def bolted_joint_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3897
            
            return self._parent._cast(_3897.BoltedJointCompoundStabilityAnalysis)

        @property
        def clutch_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3898
            
            return self._parent._cast(_3898.ClutchCompoundStabilityAnalysis)

        @property
        def clutch_half_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3900
            
            return self._parent._cast(_3900.ClutchHalfCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3902
            
            return self._parent._cast(_3902.ComponentCompoundStabilityAnalysis)

        @property
        def concept_coupling_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3903
            
            return self._parent._cast(_3903.ConceptCouplingCompoundStabilityAnalysis)

        @property
        def concept_coupling_half_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3905
            
            return self._parent._cast(_3905.ConceptCouplingHalfCompoundStabilityAnalysis)

        @property
        def concept_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3906
            
            return self._parent._cast(_3906.ConceptGearCompoundStabilityAnalysis)

        @property
        def concept_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3908
            
            return self._parent._cast(_3908.ConceptGearSetCompoundStabilityAnalysis)

        @property
        def conical_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3909
            
            return self._parent._cast(_3909.ConicalGearCompoundStabilityAnalysis)

        @property
        def conical_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3911
            
            return self._parent._cast(_3911.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def connector_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3913
            
            return self._parent._cast(_3913.ConnectorCompoundStabilityAnalysis)

        @property
        def coupling_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3914
            
            return self._parent._cast(_3914.CouplingCompoundStabilityAnalysis)

        @property
        def coupling_half_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3916
            
            return self._parent._cast(_3916.CouplingHalfCompoundStabilityAnalysis)

        @property
        def cvt_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3918
            
            return self._parent._cast(_3918.CVTCompoundStabilityAnalysis)

        @property
        def cvt_pulley_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3919
            
            return self._parent._cast(_3919.CVTPulleyCompoundStabilityAnalysis)

        @property
        def cycloidal_assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3920
            
            return self._parent._cast(_3920.CycloidalAssemblyCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3922
            
            return self._parent._cast(_3922.CycloidalDiscCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3924
            
            return self._parent._cast(_3924.CylindricalGearCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3926
            
            return self._parent._cast(_3926.CylindricalGearSetCompoundStabilityAnalysis)

        @property
        def cylindrical_planet_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3927
            
            return self._parent._cast(_3927.CylindricalPlanetGearCompoundStabilityAnalysis)

        @property
        def datum_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3928
            
            return self._parent._cast(_3928.DatumCompoundStabilityAnalysis)

        @property
        def external_cad_model_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3929
            
            return self._parent._cast(_3929.ExternalCADModelCompoundStabilityAnalysis)

        @property
        def face_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3930
            
            return self._parent._cast(_3930.FaceGearCompoundStabilityAnalysis)

        @property
        def face_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3932
            
            return self._parent._cast(_3932.FaceGearSetCompoundStabilityAnalysis)

        @property
        def fe_part_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3933
            
            return self._parent._cast(_3933.FEPartCompoundStabilityAnalysis)

        @property
        def flexible_pin_assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3934
            
            return self._parent._cast(_3934.FlexiblePinAssemblyCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3935
            
            return self._parent._cast(_3935.GearCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3937
            
            return self._parent._cast(_3937.GearSetCompoundStabilityAnalysis)

        @property
        def guide_dxf_model_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3938
            
            return self._parent._cast(_3938.GuideDxfModelCompoundStabilityAnalysis)

        @property
        def hypoid_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3939
            
            return self._parent._cast(_3939.HypoidGearCompoundStabilityAnalysis)

        @property
        def hypoid_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3941
            
            return self._parent._cast(_3941.HypoidGearSetCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3943
            
            return self._parent._cast(_3943.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3945
            
            return self._parent._cast(_3945.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3946
            
            return self._parent._cast(_3946.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3948
            
            return self._parent._cast(_3948.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3949
            
            return self._parent._cast(_3949.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3951
            
            return self._parent._cast(_3951.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def mass_disc_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3952
            
            return self._parent._cast(_3952.MassDiscCompoundStabilityAnalysis)

        @property
        def measurement_component_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3953
            
            return self._parent._cast(_3953.MeasurementComponentCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3954
            
            return self._parent._cast(_3954.MountableComponentCompoundStabilityAnalysis)

        @property
        def oil_seal_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3955
            
            return self._parent._cast(_3955.OilSealCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3957
            
            return self._parent._cast(_3957.PartToPartShearCouplingCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3959
            
            return self._parent._cast(_3959.PartToPartShearCouplingHalfCompoundStabilityAnalysis)

        @property
        def planetary_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3961
            
            return self._parent._cast(_3961.PlanetaryGearSetCompoundStabilityAnalysis)

        @property
        def planet_carrier_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3962
            
            return self._parent._cast(_3962.PlanetCarrierCompoundStabilityAnalysis)

        @property
        def point_load_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3963
            
            return self._parent._cast(_3963.PointLoadCompoundStabilityAnalysis)

        @property
        def power_load_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3964
            
            return self._parent._cast(_3964.PowerLoadCompoundStabilityAnalysis)

        @property
        def pulley_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3965
            
            return self._parent._cast(_3965.PulleyCompoundStabilityAnalysis)

        @property
        def ring_pins_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3966
            
            return self._parent._cast(_3966.RingPinsCompoundStabilityAnalysis)

        @property
        def rolling_ring_assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3968
            
            return self._parent._cast(_3968.RollingRingAssemblyCompoundStabilityAnalysis)

        @property
        def rolling_ring_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3969
            
            return self._parent._cast(_3969.RollingRingCompoundStabilityAnalysis)

        @property
        def root_assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3971
            
            return self._parent._cast(_3971.RootAssemblyCompoundStabilityAnalysis)

        @property
        def shaft_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3972
            
            return self._parent._cast(_3972.ShaftCompoundStabilityAnalysis)

        @property
        def shaft_hub_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3973
            
            return self._parent._cast(_3973.ShaftHubConnectionCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3975
            
            return self._parent._cast(_3975.SpecialisedAssemblyCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3976
            
            return self._parent._cast(_3976.SpiralBevelGearCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3978
            
            return self._parent._cast(_3978.SpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def spring_damper_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3979
            
            return self._parent._cast(_3979.SpringDamperCompoundStabilityAnalysis)

        @property
        def spring_damper_half_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3981
            
            return self._parent._cast(_3981.SpringDamperHalfCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3982
            
            return self._parent._cast(_3982.StraightBevelDiffGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3984
            
            return self._parent._cast(_3984.StraightBevelDiffGearSetCompoundStabilityAnalysis)

        @property
        def straight_bevel_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3985
            
            return self._parent._cast(_3985.StraightBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3987
            
            return self._parent._cast(_3987.StraightBevelGearSetCompoundStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3988
            
            return self._parent._cast(_3988.StraightBevelPlanetGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3989
            
            return self._parent._cast(_3989.StraightBevelSunGearCompoundStabilityAnalysis)

        @property
        def synchroniser_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3990
            
            return self._parent._cast(_3990.SynchroniserCompoundStabilityAnalysis)

        @property
        def synchroniser_half_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3991
            
            return self._parent._cast(_3991.SynchroniserHalfCompoundStabilityAnalysis)

        @property
        def synchroniser_part_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3992
            
            return self._parent._cast(_3992.SynchroniserPartCompoundStabilityAnalysis)

        @property
        def synchroniser_sleeve_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3993
            
            return self._parent._cast(_3993.SynchroniserSleeveCompoundStabilityAnalysis)

        @property
        def torque_converter_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3994
            
            return self._parent._cast(_3994.TorqueConverterCompoundStabilityAnalysis)

        @property
        def torque_converter_pump_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3996
            
            return self._parent._cast(_3996.TorqueConverterPumpCompoundStabilityAnalysis)

        @property
        def torque_converter_turbine_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3997
            
            return self._parent._cast(_3997.TorqueConverterTurbineCompoundStabilityAnalysis)

        @property
        def unbalanced_mass_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3998
            
            return self._parent._cast(_3998.UnbalancedMassCompoundStabilityAnalysis)

        @property
        def virtual_component_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3999
            
            return self._parent._cast(_3999.VirtualComponentCompoundStabilityAnalysis)

        @property
        def worm_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4000
            
            return self._parent._cast(_4000.WormGearCompoundStabilityAnalysis)

        @property
        def worm_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4002
            
            return self._parent._cast(_4002.WormGearSetCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4003
            
            return self._parent._cast(_4003.ZerolBevelGearCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4005
            
            return self._parent._cast(_4005.ZerolBevelGearSetCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(self) -> 'PartCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3825.PartStabilityAnalysis]':
        """List[PartStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3825.PartStabilityAnalysis]':
        """List[PartStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis':
        return self._Cast_PartCompoundStabilityAnalysis(self)
