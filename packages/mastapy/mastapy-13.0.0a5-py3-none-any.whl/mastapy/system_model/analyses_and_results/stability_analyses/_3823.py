"""_3823.py

MountableComponentStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3770
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'MountableComponentStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2447


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponentStabilityAnalysis',)


class MountableComponentStabilityAnalysis(_3770.ComponentStabilityAnalysis):
    """MountableComponentStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_STABILITY_ANALYSIS

    class _Cast_MountableComponentStabilityAnalysis:
        """Special nested class for casting MountableComponentStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'MountableComponentStabilityAnalysis'):
            self._parent = parent

        @property
        def component_stability_analysis(self):
            return self._parent._cast(_3770.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3825
            
            return self._parent._cast(_3825.PartStabilityAnalysis)

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
        def agma_gleason_conical_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3751
            
            return self._parent._cast(_3751.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def bearing_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3753
            
            return self._parent._cast(_3753.BearingStabilityAnalysis)

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
        def bevel_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3763
            
            return self._parent._cast(_3763.BevelGearStabilityAnalysis)

        @property
        def clutch_half_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3767
            
            return self._parent._cast(_3767.ClutchHalfStabilityAnalysis)

        @property
        def concept_coupling_half_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3772
            
            return self._parent._cast(_3772.ConceptCouplingHalfStabilityAnalysis)

        @property
        def concept_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3776
            
            return self._parent._cast(_3776.ConceptGearStabilityAnalysis)

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
        def cvt_pulley_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3787
            
            return self._parent._cast(_3787.CVTPulleyStabilityAnalysis)

        @property
        def cylindrical_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3795
            
            return self._parent._cast(_3795.CylindricalGearStabilityAnalysis)

        @property
        def cylindrical_planet_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3796
            
            return self._parent._cast(_3796.CylindricalPlanetGearStabilityAnalysis)

        @property
        def face_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3801
            
            return self._parent._cast(_3801.FaceGearStabilityAnalysis)

        @property
        def gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3806
            
            return self._parent._cast(_3806.GearStabilityAnalysis)

        @property
        def hypoid_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3810
            
            return self._parent._cast(_3810.HypoidGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3814
            
            return self._parent._cast(_3814.KlingelnbergCycloPalloidConicalGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3817
            
            return self._parent._cast(_3817.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis)

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
        def oil_seal_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3824
            
            return self._parent._cast(_3824.OilSealStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3827
            
            return self._parent._cast(_3827.PartToPartShearCouplingHalfStabilityAnalysis)

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
        def rolling_ring_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3839
            
            return self._parent._cast(_3839.RollingRingStabilityAnalysis)

        @property
        def shaft_hub_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3841
            
            return self._parent._cast(_3841.ShaftHubConnectionStabilityAnalysis)

        @property
        def spiral_bevel_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3847
            
            return self._parent._cast(_3847.SpiralBevelGearStabilityAnalysis)

        @property
        def spring_damper_half_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3849
            
            return self._parent._cast(_3849.SpringDamperHalfStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3855
            
            return self._parent._cast(_3855.StraightBevelDiffGearStabilityAnalysis)

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
        def torque_converter_pump_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3866
            
            return self._parent._cast(_3866.TorqueConverterPumpStabilityAnalysis)

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
        def worm_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3873
            
            return self._parent._cast(_3873.WormGearStabilityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3876
            
            return self._parent._cast(_3876.ZerolBevelGearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(self) -> 'MountableComponentStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MountableComponentStabilityAnalysis.TYPE'):
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
    def cast_to(self) -> 'MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis':
        return self._Cast_MountableComponentStabilityAnalysis(self)
