﻿"""_5874.py

ComponentCompoundHarmonicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5928
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'ComponentCompoundHarmonicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5678


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentCompoundHarmonicAnalysis',)


class ComponentCompoundHarmonicAnalysis(_5928.PartCompoundHarmonicAnalysis):
    """ComponentCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_ComponentCompoundHarmonicAnalysis:
        """Special nested class for casting ComponentCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'ComponentCompoundHarmonicAnalysis'):
            self._parent = parent

        @property
        def part_compound_harmonic_analysis(self):
            return self._parent._cast(_5928.PartCompoundHarmonicAnalysis)

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
        def abstract_shaft_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5850
            
            return self._parent._cast(_5850.AbstractShaftCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5851
            
            return self._parent._cast(_5851.AbstractShaftOrHousingCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5853
            
            return self._parent._cast(_5853.AGMAGleasonConicalGearCompoundHarmonicAnalysis)

        @property
        def bearing_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5857
            
            return self._parent._cast(_5857.BearingCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5860
            
            return self._parent._cast(_5860.BevelDifferentialGearCompoundHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5863
            
            return self._parent._cast(_5863.BevelDifferentialPlanetGearCompoundHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5864
            
            return self._parent._cast(_5864.BevelDifferentialSunGearCompoundHarmonicAnalysis)

        @property
        def bevel_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5865
            
            return self._parent._cast(_5865.BevelGearCompoundHarmonicAnalysis)

        @property
        def bolt_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5868
            
            return self._parent._cast(_5868.BoltCompoundHarmonicAnalysis)

        @property
        def clutch_half_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5872
            
            return self._parent._cast(_5872.ClutchHalfCompoundHarmonicAnalysis)

        @property
        def concept_coupling_half_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5877
            
            return self._parent._cast(_5877.ConceptCouplingHalfCompoundHarmonicAnalysis)

        @property
        def concept_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5878
            
            return self._parent._cast(_5878.ConceptGearCompoundHarmonicAnalysis)

        @property
        def conical_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5881
            
            return self._parent._cast(_5881.ConicalGearCompoundHarmonicAnalysis)

        @property
        def connector_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5885
            
            return self._parent._cast(_5885.ConnectorCompoundHarmonicAnalysis)

        @property
        def coupling_half_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5888
            
            return self._parent._cast(_5888.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def cvt_pulley_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5891
            
            return self._parent._cast(_5891.CVTPulleyCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5894
            
            return self._parent._cast(_5894.CycloidalDiscCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5896
            
            return self._parent._cast(_5896.CylindricalGearCompoundHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5899
            
            return self._parent._cast(_5899.CylindricalPlanetGearCompoundHarmonicAnalysis)

        @property
        def datum_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5900
            
            return self._parent._cast(_5900.DatumCompoundHarmonicAnalysis)

        @property
        def external_cad_model_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5901
            
            return self._parent._cast(_5901.ExternalCADModelCompoundHarmonicAnalysis)

        @property
        def face_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5902
            
            return self._parent._cast(_5902.FaceGearCompoundHarmonicAnalysis)

        @property
        def fe_part_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5905
            
            return self._parent._cast(_5905.FEPartCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5907
            
            return self._parent._cast(_5907.GearCompoundHarmonicAnalysis)

        @property
        def guide_dxf_model_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5910
            
            return self._parent._cast(_5910.GuideDxfModelCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5911
            
            return self._parent._cast(_5911.HypoidGearCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5915
            
            return self._parent._cast(_5915.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5918
            
            return self._parent._cast(_5918.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5921
            
            return self._parent._cast(_5921.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis)

        @property
        def mass_disc_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5924
            
            return self._parent._cast(_5924.MassDiscCompoundHarmonicAnalysis)

        @property
        def measurement_component_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5925
            
            return self._parent._cast(_5925.MeasurementComponentCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5926
            
            return self._parent._cast(_5926.MountableComponentCompoundHarmonicAnalysis)

        @property
        def oil_seal_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5927
            
            return self._parent._cast(_5927.OilSealCompoundHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5931
            
            return self._parent._cast(_5931.PartToPartShearCouplingHalfCompoundHarmonicAnalysis)

        @property
        def planet_carrier_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5934
            
            return self._parent._cast(_5934.PlanetCarrierCompoundHarmonicAnalysis)

        @property
        def point_load_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5935
            
            return self._parent._cast(_5935.PointLoadCompoundHarmonicAnalysis)

        @property
        def power_load_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5936
            
            return self._parent._cast(_5936.PowerLoadCompoundHarmonicAnalysis)

        @property
        def pulley_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5937
            
            return self._parent._cast(_5937.PulleyCompoundHarmonicAnalysis)

        @property
        def ring_pins_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5938
            
            return self._parent._cast(_5938.RingPinsCompoundHarmonicAnalysis)

        @property
        def rolling_ring_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5941
            
            return self._parent._cast(_5941.RollingRingCompoundHarmonicAnalysis)

        @property
        def shaft_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5944
            
            return self._parent._cast(_5944.ShaftCompoundHarmonicAnalysis)

        @property
        def shaft_hub_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5945
            
            return self._parent._cast(_5945.ShaftHubConnectionCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5948
            
            return self._parent._cast(_5948.SpiralBevelGearCompoundHarmonicAnalysis)

        @property
        def spring_damper_half_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5953
            
            return self._parent._cast(_5953.SpringDamperHalfCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5954
            
            return self._parent._cast(_5954.StraightBevelDiffGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5957
            
            return self._parent._cast(_5957.StraightBevelGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5960
            
            return self._parent._cast(_5960.StraightBevelPlanetGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5961
            
            return self._parent._cast(_5961.StraightBevelSunGearCompoundHarmonicAnalysis)

        @property
        def synchroniser_half_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5963
            
            return self._parent._cast(_5963.SynchroniserHalfCompoundHarmonicAnalysis)

        @property
        def synchroniser_part_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5964
            
            return self._parent._cast(_5964.SynchroniserPartCompoundHarmonicAnalysis)

        @property
        def synchroniser_sleeve_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5965
            
            return self._parent._cast(_5965.SynchroniserSleeveCompoundHarmonicAnalysis)

        @property
        def torque_converter_pump_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5968
            
            return self._parent._cast(_5968.TorqueConverterPumpCompoundHarmonicAnalysis)

        @property
        def torque_converter_turbine_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5969
            
            return self._parent._cast(_5969.TorqueConverterTurbineCompoundHarmonicAnalysis)

        @property
        def unbalanced_mass_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5970
            
            return self._parent._cast(_5970.UnbalancedMassCompoundHarmonicAnalysis)

        @property
        def virtual_component_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5971
            
            return self._parent._cast(_5971.VirtualComponentCompoundHarmonicAnalysis)

        @property
        def worm_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5972
            
            return self._parent._cast(_5972.WormGearCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5975
            
            return self._parent._cast(_5975.ZerolBevelGearCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(self) -> 'ComponentCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ComponentCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_5678.ComponentHarmonicAnalysis]':
        """List[ComponentHarmonicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_5678.ComponentHarmonicAnalysis]':
        """List[ComponentHarmonicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis':
        return self._Cast_ComponentCompoundHarmonicAnalysis(self)
