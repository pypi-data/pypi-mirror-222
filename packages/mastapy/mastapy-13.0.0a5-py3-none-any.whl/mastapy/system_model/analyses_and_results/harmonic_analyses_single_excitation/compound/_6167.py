"""_6167.py

GearMeshCompoundHarmonicAnalysisOfSingleExcitation
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6173
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'GearMeshCompoundHarmonicAnalysisOfSingleExcitation')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6037


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshCompoundHarmonicAnalysisOfSingleExcitation',)


class GearMeshCompoundHarmonicAnalysisOfSingleExcitation(_6173.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation):
    """GearMeshCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting GearMeshCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'GearMeshCompoundHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6173.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6143
            
            return self._parent._cast(_6143.ConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6113
            
            return self._parent._cast(_6113.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6120
            
            return self._parent._cast(_6120.BevelDifferentialGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6125
            
            return self._parent._cast(_6125.BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6138
            
            return self._parent._cast(_6138.ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6141
            
            return self._parent._cast(_6141.ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6156
            
            return self._parent._cast(_6156.CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6162
            
            return self._parent._cast(_6162.FaceGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6171
            
            return self._parent._cast(_6171.HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6175
            
            return self._parent._cast(_6175.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6178
            
            return self._parent._cast(_6178.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6181
            
            return self._parent._cast(_6181.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6208
            
            return self._parent._cast(_6208.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6214
            
            return self._parent._cast(_6214.StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6217
            
            return self._parent._cast(_6217.StraightBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6232
            
            return self._parent._cast(_6232.WormGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6235
            
            return self._parent._cast(_6235.ZerolBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_mesh_compound_harmonic_analysis_of_single_excitation(self) -> 'GearMeshCompoundHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_6037.GearMeshHarmonicAnalysisOfSingleExcitation]':
        """List[GearMeshHarmonicAnalysisOfSingleExcitation]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6037.GearMeshHarmonicAnalysisOfSingleExcitation]':
        """List[GearMeshHarmonicAnalysisOfSingleExcitation]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation':
        return self._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation(self)
