"""_7002.py

ComponentAdvancedTimeSteppingAnalysisForModulation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7057
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'ComponentAdvancedTimeSteppingAnalysisForModulation')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2427
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5835
    from mastapy.system_model.analyses_and_results.system_deflections import _2697


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentAdvancedTimeSteppingAnalysisForModulation',)


class ComponentAdvancedTimeSteppingAnalysisForModulation(_7057.PartAdvancedTimeSteppingAnalysisForModulation):
    """ComponentAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _COMPONENT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_ComponentAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ComponentAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'ComponentAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def part_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7057.PartAdvancedTimeSteppingAnalysisForModulation)

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
        def bearing_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6985
            
            return self._parent._cast(_6985.BearingAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6988
            
            return self._parent._cast(_6988.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation)

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
        def bolt_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6996
            
            return self._parent._cast(_6996.BoltAdvancedTimeSteppingAnalysisForModulation)

        @property
        def clutch_half_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7000
            
            return self._parent._cast(_7000.ClutchHalfAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_coupling_half_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7005
            
            return self._parent._cast(_7005.ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7006
            
            return self._parent._cast(_7006.ConceptGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7009
            
            return self._parent._cast(_7009.ConicalGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def connector_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7013
            
            return self._parent._cast(_7013.ConnectorAdvancedTimeSteppingAnalysisForModulation)

        @property
        def coupling_half_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7016
            
            return self._parent._cast(_7016.CouplingHalfAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cvt_pulley_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7019
            
            return self._parent._cast(_7019.CVTPulleyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cycloidal_disc_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7021
            
            return self._parent._cast(_7021.CycloidalDiscAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cylindrical_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7024
            
            return self._parent._cast(_7024.CylindricalGearAdvancedTimeSteppingAnalysisForModulation)

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
        def fe_part_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7033
            
            return self._parent._cast(_7033.FEPartAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7035
            
            return self._parent._cast(_7035.GearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def guide_dxf_model_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7038
            
            return self._parent._cast(_7038.GuideDxfModelAdvancedTimeSteppingAnalysisForModulation)

        @property
        def hypoid_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7040
            
            return self._parent._cast(_7040.HypoidGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7044
            
            return self._parent._cast(_7044.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7047
            
            return self._parent._cast(_7047.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7050
            
            return self._parent._cast(_7050.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation)

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
        def part_to_part_shear_coupling_half_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7060
            
            return self._parent._cast(_7060.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation)

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
        def shaft_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7073
            
            return self._parent._cast(_7073.ShaftAdvancedTimeSteppingAnalysisForModulation)

        @property
        def shaft_hub_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7074
            
            return self._parent._cast(_7074.ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7077
            
            return self._parent._cast(_7077.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spring_damper_half_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7082
            
            return self._parent._cast(_7082.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_diff_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7083
            
            return self._parent._cast(_7083.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7086
            
            return self._parent._cast(_7086.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_planet_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7089
            
            return self._parent._cast(_7089.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_sun_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7090
            
            return self._parent._cast(_7090.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation)

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
        def zerol_bevel_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7104
            
            return self._parent._cast(_7104.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def component_advanced_time_stepping_analysis_for_modulation(self) -> 'ComponentAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ComponentAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def magnitude_of_rotation(self) -> 'float':
        """float: 'MagnitudeOfRotation' is the original name of this property."""

        temp = self.wrapped.MagnitudeOfRotation

        if temp is None:
            return 0.0

        return temp

    @magnitude_of_rotation.setter
    def magnitude_of_rotation(self, value: 'float'):
        self.wrapped.MagnitudeOfRotation = float(value) if value is not None else 0.0

    @property
    def component_design(self) -> '_2427.Component':
        """Component: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def results(self) -> '_5835.HarmonicAnalysisResultsPropertyAccessor':
        """HarmonicAnalysisResultsPropertyAccessor: 'Results' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Results

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2697.ComponentSystemDeflection':
        """ComponentSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ComponentAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_ComponentAdvancedTimeSteppingAnalysisForModulation(self)
