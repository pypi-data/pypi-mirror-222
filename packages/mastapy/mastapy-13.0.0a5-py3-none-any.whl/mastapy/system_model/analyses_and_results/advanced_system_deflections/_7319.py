"""_7319.py

MountableComponentAdvancedSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7264
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'MountableComponentAdvancedSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2447


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponentAdvancedSystemDeflection',)


class MountableComponentAdvancedSystemDeflection(_7264.ComponentAdvancedSystemDeflection):
    """MountableComponentAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_MountableComponentAdvancedSystemDeflection:
        """Special nested class for casting MountableComponentAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'MountableComponentAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def component_advanced_system_deflection(self):
            return self._parent._cast(_7264.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7321
            
            return self._parent._cast(_7321.PartAdvancedSystemDeflection)

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
        def agma_gleason_conical_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7243
            
            return self._parent._cast(_7243.AGMAGleasonConicalGearAdvancedSystemDeflection)

        @property
        def bearing_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7247
            
            return self._parent._cast(_7247.BearingAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7250
            
            return self._parent._cast(_7250.BevelDifferentialGearAdvancedSystemDeflection)

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
        def clutch_half_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7262
            
            return self._parent._cast(_7262.ClutchHalfAdvancedSystemDeflection)

        @property
        def concept_coupling_half_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7267
            
            return self._parent._cast(_7267.ConceptCouplingHalfAdvancedSystemDeflection)

        @property
        def concept_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7268
            
            return self._parent._cast(_7268.ConceptGearAdvancedSystemDeflection)

        @property
        def conical_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7271
            
            return self._parent._cast(_7271.ConicalGearAdvancedSystemDeflection)

        @property
        def connector_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7275
            
            return self._parent._cast(_7275.ConnectorAdvancedSystemDeflection)

        @property
        def coupling_half_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7279
            
            return self._parent._cast(_7279.CouplingHalfAdvancedSystemDeflection)

        @property
        def cvt_pulley_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7282
            
            return self._parent._cast(_7282.CVTPulleyAdvancedSystemDeflection)

        @property
        def cylindrical_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7287
            
            return self._parent._cast(_7287.CylindricalGearAdvancedSystemDeflection)

        @property
        def cylindrical_planet_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7291
            
            return self._parent._cast(_7291.CylindricalPlanetGearAdvancedSystemDeflection)

        @property
        def face_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7294
            
            return self._parent._cast(_7294.FaceGearAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7299
            
            return self._parent._cast(_7299.GearAdvancedSystemDeflection)

        @property
        def hypoid_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7303
            
            return self._parent._cast(_7303.HypoidGearAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7307
            
            return self._parent._cast(_7307.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7310
            
            return self._parent._cast(_7310.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7313
            
            return self._parent._cast(_7313.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection)

        @property
        def mass_disc_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7317
            
            return self._parent._cast(_7317.MassDiscAdvancedSystemDeflection)

        @property
        def measurement_component_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7318
            
            return self._parent._cast(_7318.MeasurementComponentAdvancedSystemDeflection)

        @property
        def oil_seal_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7320
            
            return self._parent._cast(_7320.OilSealAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7324
            
            return self._parent._cast(_7324.PartToPartShearCouplingHalfAdvancedSystemDeflection)

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
        def shaft_hub_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7338
            
            return self._parent._cast(_7338.ShaftHubConnectionAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7341
            
            return self._parent._cast(_7341.SpiralBevelGearAdvancedSystemDeflection)

        @property
        def spring_damper_half_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7346
            
            return self._parent._cast(_7346.SpringDamperHalfAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7347
            
            return self._parent._cast(_7347.StraightBevelDiffGearAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7350
            
            return self._parent._cast(_7350.StraightBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7353
            
            return self._parent._cast(_7353.StraightBevelPlanetGearAdvancedSystemDeflection)

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7354
            
            return self._parent._cast(_7354.StraightBevelSunGearAdvancedSystemDeflection)

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
        def zerol_bevel_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7369
            
            return self._parent._cast(_7369.ZerolBevelGearAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(self) -> 'MountableComponentAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MountableComponentAdvancedSystemDeflection.TYPE'):
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
    def cast_to(self) -> 'MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection':
        return self._Cast_MountableComponentAdvancedSystemDeflection(self)
