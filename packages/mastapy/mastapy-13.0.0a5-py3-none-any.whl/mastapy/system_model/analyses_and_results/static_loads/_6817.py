"""_6817.py

ConnectionLoadCase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results import _2631
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConnectionLoadCase')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2255
    from mastapy.system_model.analyses_and_results.static_loads import _6772, _6773


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionLoadCase',)


class ConnectionLoadCase(_2631.ConnectionAnalysis):
    """ConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _CONNECTION_LOAD_CASE

    class _Cast_ConnectionLoadCase:
        """Special nested class for casting ConnectionLoadCase to subclasses."""

        def __init__(self, parent: 'ConnectionLoadCase'):
            self._parent = parent

        @property
        def connection_analysis(self):
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
        def abstract_shaft_to_mountable_component_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6777
            
            return self._parent._cast(_6777.AbstractShaftToMountableComponentConnectionLoadCase)

        @property
        def agma_gleason_conical_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6782
            
            return self._parent._cast(_6782.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def belt_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6788
            
            return self._parent._cast(_6788.BeltConnectionLoadCase)

        @property
        def bevel_differential_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6791
            
            return self._parent._cast(_6791.BevelDifferentialGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6796
            
            return self._parent._cast(_6796.BevelGearMeshLoadCase)

        @property
        def clutch_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6800
            
            return self._parent._cast(_6800.ClutchConnectionLoadCase)

        @property
        def coaxial_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6804
            
            return self._parent._cast(_6804.CoaxialConnectionLoadCase)

        @property
        def concept_coupling_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6806
            
            return self._parent._cast(_6806.ConceptCouplingConnectionLoadCase)

        @property
        def concept_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6810
            
            return self._parent._cast(_6810.ConceptGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6814
            
            return self._parent._cast(_6814.ConicalGearMeshLoadCase)

        @property
        def coupling_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6819
            
            return self._parent._cast(_6819.CouplingConnectionLoadCase)

        @property
        def cvt_belt_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6822
            
            return self._parent._cast(_6822.CVTBeltConnectionLoadCase)

        @property
        def cycloidal_disc_central_bearing_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6826
            
            return self._parent._cast(_6826.CycloidalDiscCentralBearingConnectionLoadCase)

        @property
        def cycloidal_disc_planetary_bearing_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6828
            
            return self._parent._cast(_6828.CycloidalDiscPlanetaryBearingConnectionLoadCase)

        @property
        def cylindrical_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6831
            
            return self._parent._cast(_6831.CylindricalGearMeshLoadCase)

        @property
        def face_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6853
            
            return self._parent._cast(_6853.FaceGearMeshLoadCase)

        @property
        def gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6860
            
            return self._parent._cast(_6860.GearMeshLoadCase)

        @property
        def hypoid_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6874
            
            return self._parent._cast(_6874.HypoidGearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6879
            
            return self._parent._cast(_6879.InterMountableComponentConnectionLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6881
            
            return self._parent._cast(_6881.KlingelnbergCycloPalloidConicalGearMeshLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6884
            
            return self._parent._cast(_6884.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6887
            
            return self._parent._cast(_6887.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)

        @property
        def part_to_part_shear_coupling_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6897
            
            return self._parent._cast(_6897.PartToPartShearCouplingConnectionLoadCase)

        @property
        def planetary_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6900
            
            return self._parent._cast(_6900.PlanetaryConnectionLoadCase)

        @property
        def ring_pins_to_disc_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6912
            
            return self._parent._cast(_6912.RingPinsToDiscConnectionLoadCase)

        @property
        def rolling_ring_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6914
            
            return self._parent._cast(_6914.RollingRingConnectionLoadCase)

        @property
        def shaft_to_mountable_component_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6919
            
            return self._parent._cast(_6919.ShaftToMountableComponentConnectionLoadCase)

        @property
        def spiral_bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6922
            
            return self._parent._cast(_6922.SpiralBevelGearMeshLoadCase)

        @property
        def spring_damper_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6924
            
            return self._parent._cast(_6924.SpringDamperConnectionLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6928
            
            return self._parent._cast(_6928.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6931
            
            return self._parent._cast(_6931.StraightBevelGearMeshLoadCase)

        @property
        def torque_converter_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6940
            
            return self._parent._cast(_6940.TorqueConverterConnectionLoadCase)

        @property
        def worm_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6951
            
            return self._parent._cast(_6951.WormGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6954
            
            return self._parent._cast(_6954.ZerolBevelGearMeshLoadCase)

        @property
        def connection_load_case(self) -> 'ConnectionLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionLoadCase.TYPE'):
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
    def static_load_case(self) -> '_6772.StaticLoadCase':
        """StaticLoadCase: 'StaticLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def time_series_load_case(self) -> '_6773.TimeSeriesLoadCase':
        """TimeSeriesLoadCase: 'TimeSeriesLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeSeriesLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConnectionLoadCase._Cast_ConnectionLoadCase':
        return self._Cast_ConnectionLoadCase(self)
