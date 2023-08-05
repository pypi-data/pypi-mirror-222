"""_6013.py

ConnectionHarmonicAnalysisOfSingleExcitation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7507
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'ConnectionHarmonicAnalysisOfSingleExcitation')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2255
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6040


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionHarmonicAnalysisOfSingleExcitation',)


class ConnectionHarmonicAnalysisOfSingleExcitation(_7507.ConnectionStaticLoadAnalysisCase):
    """ConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_ConnectionHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'ConnectionHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def connection_static_load_analysis_case(self):
            return self._parent._cast(_7507.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7504
            
            return self._parent._cast(_7504.ConnectionAnalysisCase)

        @property
        def connection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2631
            
            return self._parent._cast(_2631.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2635
            
            return self._parent._cast(_2635.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5981
            
            return self._parent._cast(_5981.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5983
            
            return self._parent._cast(_5983.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def belt_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5987
            
            return self._parent._cast(_5987.BeltConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5990
            
            return self._parent._cast(_5990.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5995
            
            return self._parent._cast(_5995.BevelGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5999
            
            return self._parent._cast(_5999.ClutchConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def coaxial_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6002
            
            return self._parent._cast(_6002.CoaxialConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6004
            
            return self._parent._cast(_6004.ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6008
            
            return self._parent._cast(_6008.ConceptGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def conical_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6011
            
            return self._parent._cast(_6011.ConicalGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6015
            
            return self._parent._cast(_6015.CouplingConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_belt_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6018
            
            return self._parent._cast(_6018.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6022
            
            return self._parent._cast(_6022.CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_disc_planetary_bearing_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6024
            
            return self._parent._cast(_6024.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6026
            
            return self._parent._cast(_6026.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6032
            
            return self._parent._cast(_6032.FaceGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6037
            
            return self._parent._cast(_6037.GearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6042
            
            return self._parent._cast(_6042.HypoidGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6044
            
            return self._parent._cast(_6044.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6046
            
            return self._parent._cast(_6046.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6049
            
            return self._parent._cast(_6049.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6052
            
            return self._parent._cast(_6052.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6059
            
            return self._parent._cast(_6059.PartToPartShearCouplingConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def planetary_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6062
            
            return self._parent._cast(_6062.PlanetaryConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def ring_pins_to_disc_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6069
            
            return self._parent._cast(_6069.RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6071
            
            return self._parent._cast(_6071.RollingRingConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6076
            
            return self._parent._cast(_6076.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6079
            
            return self._parent._cast(_6079.SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def spring_damper_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6081
            
            return self._parent._cast(_6081.SpringDamperConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6085
            
            return self._parent._cast(_6085.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6088
            
            return self._parent._cast(_6088.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def torque_converter_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6096
            
            return self._parent._cast(_6096.TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6103
            
            return self._parent._cast(_6103.WormGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6106
            
            return self._parent._cast(_6106.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def connection_harmonic_analysis_of_single_excitation(self) -> 'ConnectionHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2255.Connection':
        """Connection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2255.Connection':
        """Connection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def harmonic_analysis_of_single_excitation(self) -> '_6040.HarmonicAnalysisOfSingleExcitation':
        """HarmonicAnalysisOfSingleExcitation: 'HarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConnectionHarmonicAnalysisOfSingleExcitation':
        return self._Cast_ConnectionHarmonicAnalysisOfSingleExcitation(self)
