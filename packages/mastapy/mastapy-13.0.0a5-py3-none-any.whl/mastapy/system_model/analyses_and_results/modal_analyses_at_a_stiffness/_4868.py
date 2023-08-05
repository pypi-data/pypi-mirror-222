"""_4868.py

ConnectionModalAnalysisAtAStiffness
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7507
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'ConnectionModalAnalysisAtAStiffness')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2255
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _2619


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionModalAnalysisAtAStiffness',)


class ConnectionModalAnalysisAtAStiffness(_7507.ConnectionStaticLoadAnalysisCase):
    """ConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_ConnectionModalAnalysisAtAStiffness:
        """Special nested class for casting ConnectionModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'ConnectionModalAnalysisAtAStiffness'):
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
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4836
            
            return self._parent._cast(_4836.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4837
            
            return self._parent._cast(_4837.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def belt_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4842
            
            return self._parent._cast(_4842.BeltConnectionModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4844
            
            return self._parent._cast(_4844.BevelDifferentialGearMeshModalAnalysisAtAStiffness)

        @property
        def bevel_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4849
            
            return self._parent._cast(_4849.BevelGearMeshModalAnalysisAtAStiffness)

        @property
        def clutch_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4854
            
            return self._parent._cast(_4854.ClutchConnectionModalAnalysisAtAStiffness)

        @property
        def coaxial_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4857
            
            return self._parent._cast(_4857.CoaxialConnectionModalAnalysisAtAStiffness)

        @property
        def concept_coupling_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4859
            
            return self._parent._cast(_4859.ConceptCouplingConnectionModalAnalysisAtAStiffness)

        @property
        def concept_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4862
            
            return self._parent._cast(_4862.ConceptGearMeshModalAnalysisAtAStiffness)

        @property
        def conical_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4865
            
            return self._parent._cast(_4865.ConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def coupling_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4870
            
            return self._parent._cast(_4870.CouplingConnectionModalAnalysisAtAStiffness)

        @property
        def cvt_belt_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4873
            
            return self._parent._cast(_4873.CVTBeltConnectionModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4877
            
            return self._parent._cast(_4877.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4879
            
            return self._parent._cast(_4879.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4880
            
            return self._parent._cast(_4880.CylindricalGearMeshModalAnalysisAtAStiffness)

        @property
        def face_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4887
            
            return self._parent._cast(_4887.FaceGearMeshModalAnalysisAtAStiffness)

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4892
            
            return self._parent._cast(_4892.GearMeshModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4896
            
            return self._parent._cast(_4896.HypoidGearMeshModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4899
            
            return self._parent._cast(_4899.InterMountableComponentConnectionModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4900
            
            return self._parent._cast(_4900.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4903
            
            return self._parent._cast(_4903.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4906
            
            return self._parent._cast(_4906.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4914
            
            return self._parent._cast(_4914.PartToPartShearCouplingConnectionModalAnalysisAtAStiffness)

        @property
        def planetary_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4917
            
            return self._parent._cast(_4917.PlanetaryConnectionModalAnalysisAtAStiffness)

        @property
        def ring_pins_to_disc_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4924
            
            return self._parent._cast(_4924.RingPinsToDiscConnectionModalAnalysisAtAStiffness)

        @property
        def rolling_ring_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4926
            
            return self._parent._cast(_4926.RollingRingConnectionModalAnalysisAtAStiffness)

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4931
            
            return self._parent._cast(_4931.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4933
            
            return self._parent._cast(_4933.SpiralBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def spring_damper_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4936
            
            return self._parent._cast(_4936.SpringDamperConnectionModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4939
            
            return self._parent._cast(_4939.StraightBevelDiffGearMeshModalAnalysisAtAStiffness)

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4942
            
            return self._parent._cast(_4942.StraightBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def torque_converter_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4951
            
            return self._parent._cast(_4951.TorqueConverterConnectionModalAnalysisAtAStiffness)

        @property
        def worm_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4957
            
            return self._parent._cast(_4957.WormGearMeshModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4960
            
            return self._parent._cast(_4960.ZerolBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def connection_modal_analysis_at_a_stiffness(self) -> 'ConnectionModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionModalAnalysisAtAStiffness.TYPE'):
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
    def modal_analysis_at_a_stiffness(self) -> '_2619.ModalAnalysisAtAStiffness':
        """ModalAnalysisAtAStiffness: 'ModalAnalysisAtAStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModalAnalysisAtAStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness':
        return self._Cast_ConnectionModalAnalysisAtAStiffness(self)
