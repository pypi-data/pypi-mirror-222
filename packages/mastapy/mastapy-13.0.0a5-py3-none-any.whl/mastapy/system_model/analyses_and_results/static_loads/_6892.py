"""_6892.py

MountableComponentLoadCase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6805
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'MountableComponentLoadCase')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2447


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponentLoadCase',)


class MountableComponentLoadCase(_6805.ComponentLoadCase):
    """MountableComponentLoadCase

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_LOAD_CASE

    class _Cast_MountableComponentLoadCase:
        """Special nested class for casting MountableComponentLoadCase to subclasses."""

        def __init__(self, parent: 'MountableComponentLoadCase'):
            self._parent = parent

        @property
        def component_load_case(self):
            return self._parent._cast(_6805.ComponentLoadCase)

        @property
        def part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6896
            
            return self._parent._cast(_6896.PartLoadCase)

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
        def agma_gleason_conical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6781
            
            return self._parent._cast(_6781.AGMAGleasonConicalGearLoadCase)

        @property
        def bearing_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6787
            
            return self._parent._cast(_6787.BearingLoadCase)

        @property
        def bevel_differential_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6790
            
            return self._parent._cast(_6790.BevelDifferentialGearLoadCase)

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
        def clutch_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6801
            
            return self._parent._cast(_6801.ClutchHalfLoadCase)

        @property
        def concept_coupling_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6807
            
            return self._parent._cast(_6807.ConceptCouplingHalfLoadCase)

        @property
        def concept_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6809
            
            return self._parent._cast(_6809.ConceptGearLoadCase)

        @property
        def conical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6812
            
            return self._parent._cast(_6812.ConicalGearLoadCase)

        @property
        def connector_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6818
            
            return self._parent._cast(_6818.ConnectorLoadCase)

        @property
        def coupling_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6820
            
            return self._parent._cast(_6820.CouplingHalfLoadCase)

        @property
        def cvt_pulley_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6824
            
            return self._parent._cast(_6824.CVTPulleyLoadCase)

        @property
        def cylindrical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6829
            
            return self._parent._cast(_6829.CylindricalGearLoadCase)

        @property
        def cylindrical_planet_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6834
            
            return self._parent._cast(_6834.CylindricalPlanetGearLoadCase)

        @property
        def face_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6852
            
            return self._parent._cast(_6852.FaceGearLoadCase)

        @property
        def gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6858
            
            return self._parent._cast(_6858.GearLoadCase)

        @property
        def hypoid_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6873
            
            return self._parent._cast(_6873.HypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6880
            
            return self._parent._cast(_6880.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6883
            
            return self._parent._cast(_6883.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6886
            
            return self._parent._cast(_6886.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)

        @property
        def mass_disc_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6889
            
            return self._parent._cast(_6889.MassDiscLoadCase)

        @property
        def measurement_component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6890
            
            return self._parent._cast(_6890.MeasurementComponentLoadCase)

        @property
        def oil_seal_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6894
            
            return self._parent._cast(_6894.OilSealLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6898
            
            return self._parent._cast(_6898.PartToPartShearCouplingHalfLoadCase)

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
        def rolling_ring_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6915
            
            return self._parent._cast(_6915.RollingRingLoadCase)

        @property
        def shaft_hub_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6917
            
            return self._parent._cast(_6917.ShaftHubConnectionLoadCase)

        @property
        def spiral_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6921
            
            return self._parent._cast(_6921.SpiralBevelGearLoadCase)

        @property
        def spring_damper_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6925
            
            return self._parent._cast(_6925.SpringDamperHalfLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6927
            
            return self._parent._cast(_6927.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6930
            
            return self._parent._cast(_6930.StraightBevelGearLoadCase)

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
        def synchroniser_part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6937
            
            return self._parent._cast(_6937.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6938
            
            return self._parent._cast(_6938.SynchroniserSleeveLoadCase)

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
        def zerol_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6953
            
            return self._parent._cast(_6953.ZerolBevelGearLoadCase)

        @property
        def mountable_component_load_case(self) -> 'MountableComponentLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MountableComponentLoadCase.TYPE'):
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
    def cast_to(self) -> 'MountableComponentLoadCase._Cast_MountableComponentLoadCase':
        return self._Cast_MountableComponentLoadCase(self)
