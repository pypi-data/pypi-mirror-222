"""_6133.py

ComponentCompoundHarmonicAnalysisOfSingleExcitation
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6187
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'ComponentCompoundHarmonicAnalysisOfSingleExcitation')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6003


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentCompoundHarmonicAnalysisOfSingleExcitation',)


class ComponentCompoundHarmonicAnalysisOfSingleExcitation(_6187.PartCompoundHarmonicAnalysisOfSingleExcitation):
    """ComponentCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ComponentCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'ComponentCompoundHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def part_compound_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6187.PartCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7512
            
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
        def abstract_shaft_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6109
            
            return self._parent._cast(_6109.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6110
            
            return self._parent._cast(_6110.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6112
            
            return self._parent._cast(_6112.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bearing_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6116
            
            return self._parent._cast(_6116.BearingCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6119
            
            return self._parent._cast(_6119.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6122
            
            return self._parent._cast(_6122.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6123
            
            return self._parent._cast(_6123.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6124
            
            return self._parent._cast(_6124.BevelGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bolt_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6127
            
            return self._parent._cast(_6127.BoltCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_half_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6131
            
            return self._parent._cast(_6131.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_half_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6136
            
            return self._parent._cast(_6136.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6137
            
            return self._parent._cast(_6137.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def conical_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6140
            
            return self._parent._cast(_6140.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def connector_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6144
            
            return self._parent._cast(_6144.ConnectorCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_half_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6147
            
            return self._parent._cast(_6147.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_pulley_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6150
            
            return self._parent._cast(_6150.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_disc_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6153
            
            return self._parent._cast(_6153.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6155
            
            return self._parent._cast(_6155.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6158
            
            return self._parent._cast(_6158.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def datum_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6159
            
            return self._parent._cast(_6159.DatumCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def external_cad_model_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6160
            
            return self._parent._cast(_6160.ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6161
            
            return self._parent._cast(_6161.FaceGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def fe_part_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6164
            
            return self._parent._cast(_6164.FEPartCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6166
            
            return self._parent._cast(_6166.GearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def guide_dxf_model_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6169
            
            return self._parent._cast(_6169.GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6170
            
            return self._parent._cast(_6170.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6174
            
            return self._parent._cast(_6174.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6177
            
            return self._parent._cast(_6177.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6180
            
            return self._parent._cast(_6180.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def mass_disc_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6183
            
            return self._parent._cast(_6183.MassDiscCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def measurement_component_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6184
            
            return self._parent._cast(_6184.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6185
            
            return self._parent._cast(_6185.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def oil_seal_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6186
            
            return self._parent._cast(_6186.OilSealCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6190
            
            return self._parent._cast(_6190.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def planet_carrier_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6193
            
            return self._parent._cast(_6193.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def point_load_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6194
            
            return self._parent._cast(_6194.PointLoadCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def power_load_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6195
            
            return self._parent._cast(_6195.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def pulley_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6196
            
            return self._parent._cast(_6196.PulleyCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def ring_pins_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6197
            
            return self._parent._cast(_6197.RingPinsCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6200
            
            return self._parent._cast(_6200.RollingRingCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6203
            
            return self._parent._cast(_6203.ShaftCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_hub_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6204
            
            return self._parent._cast(_6204.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6207
            
            return self._parent._cast(_6207.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def spring_damper_half_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6212
            
            return self._parent._cast(_6212.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6213
            
            return self._parent._cast(_6213.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6216
            
            return self._parent._cast(_6216.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6219
            
            return self._parent._cast(_6219.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6220
            
            return self._parent._cast(_6220.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_half_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6222
            
            return self._parent._cast(_6222.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_part_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6223
            
            return self._parent._cast(_6223.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_sleeve_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6224
            
            return self._parent._cast(_6224.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def torque_converter_pump_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6227
            
            return self._parent._cast(_6227.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def torque_converter_turbine_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6228
            
            return self._parent._cast(_6228.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def unbalanced_mass_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6229
            
            return self._parent._cast(_6229.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def virtual_component_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6230
            
            return self._parent._cast(_6230.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6231
            
            return self._parent._cast(_6231.WormGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6234
            
            return self._parent._cast(_6234.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def component_compound_harmonic_analysis_of_single_excitation(self) -> 'ComponentCompoundHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ComponentCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_6003.ComponentHarmonicAnalysisOfSingleExcitation]':
        """List[ComponentHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_6003.ComponentHarmonicAnalysisOfSingleExcitation]':
        """List[ComponentHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation':
        return self._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation(self)
