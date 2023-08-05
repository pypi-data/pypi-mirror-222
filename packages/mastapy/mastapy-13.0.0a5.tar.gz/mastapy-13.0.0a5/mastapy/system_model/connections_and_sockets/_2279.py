"""_2279.py

Socket
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Component')
_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'Socket')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2427, _2428
    from mastapy.system_model.connections_and_sockets import _2255


__docformat__ = 'restructuredtext en'
__all__ = ('Socket',)


class Socket(_0.APIBase):
    """Socket

    This is a mastapy class.
    """

    TYPE = _SOCKET

    class _Cast_Socket:
        """Special nested class for casting Socket to subclasses."""

        def __init__(self, parent: 'Socket'):
            self._parent = parent

        @property
        def bearing_inner_socket(self):
            from mastapy.system_model.connections_and_sockets import _2249
            
            return self._parent._cast(_2249.BearingInnerSocket)

        @property
        def bearing_outer_socket(self):
            from mastapy.system_model.connections_and_sockets import _2250
            
            return self._parent._cast(_2250.BearingOuterSocket)

        @property
        def cvt_pulley_socket(self):
            from mastapy.system_model.connections_and_sockets import _2257
            
            return self._parent._cast(_2257.CVTPulleySocket)

        @property
        def cylindrical_socket(self):
            from mastapy.system_model.connections_and_sockets import _2259
            
            return self._parent._cast(_2259.CylindricalSocket)

        @property
        def electric_machine_stator_socket(self):
            from mastapy.system_model.connections_and_sockets import _2261
            
            return self._parent._cast(_2261.ElectricMachineStatorSocket)

        @property
        def inner_shaft_socket(self):
            from mastapy.system_model.connections_and_sockets import _2262
            
            return self._parent._cast(_2262.InnerShaftSocket)

        @property
        def inner_shaft_socket_base(self):
            from mastapy.system_model.connections_and_sockets import _2263
            
            return self._parent._cast(_2263.InnerShaftSocketBase)

        @property
        def mountable_component_inner_socket(self):
            from mastapy.system_model.connections_and_sockets import _2265
            
            return self._parent._cast(_2265.MountableComponentInnerSocket)

        @property
        def mountable_component_outer_socket(self):
            from mastapy.system_model.connections_and_sockets import _2266
            
            return self._parent._cast(_2266.MountableComponentOuterSocket)

        @property
        def mountable_component_socket(self):
            from mastapy.system_model.connections_and_sockets import _2267
            
            return self._parent._cast(_2267.MountableComponentSocket)

        @property
        def outer_shaft_socket(self):
            from mastapy.system_model.connections_and_sockets import _2268
            
            return self._parent._cast(_2268.OuterShaftSocket)

        @property
        def outer_shaft_socket_base(self):
            from mastapy.system_model.connections_and_sockets import _2269
            
            return self._parent._cast(_2269.OuterShaftSocketBase)

        @property
        def planetary_socket(self):
            from mastapy.system_model.connections_and_sockets import _2271
            
            return self._parent._cast(_2271.PlanetarySocket)

        @property
        def planetary_socket_base(self):
            from mastapy.system_model.connections_and_sockets import _2272
            
            return self._parent._cast(_2272.PlanetarySocketBase)

        @property
        def pulley_socket(self):
            from mastapy.system_model.connections_and_sockets import _2273
            
            return self._parent._cast(_2273.PulleySocket)

        @property
        def rolling_ring_socket(self):
            from mastapy.system_model.connections_and_sockets import _2276
            
            return self._parent._cast(_2276.RollingRingSocket)

        @property
        def shaft_socket(self):
            from mastapy.system_model.connections_and_sockets import _2277
            
            return self._parent._cast(_2277.ShaftSocket)

        @property
        def agma_gleason_conical_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2283
            
            return self._parent._cast(_2283.AGMAGleasonConicalGearTeethSocket)

        @property
        def bevel_differential_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2285
            
            return self._parent._cast(_2285.BevelDifferentialGearTeethSocket)

        @property
        def bevel_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2287
            
            return self._parent._cast(_2287.BevelGearTeethSocket)

        @property
        def concept_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2289
            
            return self._parent._cast(_2289.ConceptGearTeethSocket)

        @property
        def conical_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2291
            
            return self._parent._cast(_2291.ConicalGearTeethSocket)

        @property
        def cylindrical_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2293
            
            return self._parent._cast(_2293.CylindricalGearTeethSocket)

        @property
        def face_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2295
            
            return self._parent._cast(_2295.FaceGearTeethSocket)

        @property
        def gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2297
            
            return self._parent._cast(_2297.GearTeethSocket)

        @property
        def hypoid_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2299
            
            return self._parent._cast(_2299.HypoidGearTeethSocket)

        @property
        def klingelnberg_conical_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2300
            
            return self._parent._cast(_2300.KlingelnbergConicalGearTeethSocket)

        @property
        def klingelnberg_hypoid_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2304
            
            return self._parent._cast(_2304.KlingelnbergHypoidGearTeethSocket)

        @property
        def klingelnberg_spiral_bevel_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2305
            
            return self._parent._cast(_2305.KlingelnbergSpiralBevelGearTeethSocket)

        @property
        def spiral_bevel_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2307
            
            return self._parent._cast(_2307.SpiralBevelGearTeethSocket)

        @property
        def straight_bevel_diff_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2309
            
            return self._parent._cast(_2309.StraightBevelDiffGearTeethSocket)

        @property
        def straight_bevel_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2311
            
            return self._parent._cast(_2311.StraightBevelGearTeethSocket)

        @property
        def worm_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2313
            
            return self._parent._cast(_2313.WormGearTeethSocket)

        @property
        def zerol_bevel_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2315
            
            return self._parent._cast(_2315.ZerolBevelGearTeethSocket)

        @property
        def cycloidal_disc_axial_left_socket(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2316
            
            return self._parent._cast(_2316.CycloidalDiscAxialLeftSocket)

        @property
        def cycloidal_disc_axial_right_socket(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2317
            
            return self._parent._cast(_2317.CycloidalDiscAxialRightSocket)

        @property
        def cycloidal_disc_inner_socket(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2319
            
            return self._parent._cast(_2319.CycloidalDiscInnerSocket)

        @property
        def cycloidal_disc_outer_socket(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2320
            
            return self._parent._cast(_2320.CycloidalDiscOuterSocket)

        @property
        def cycloidal_disc_planetary_bearing_socket(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2322
            
            return self._parent._cast(_2322.CycloidalDiscPlanetaryBearingSocket)

        @property
        def ring_pins_socket(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2323
            
            return self._parent._cast(_2323.RingPinsSocket)

        @property
        def clutch_socket(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2326
            
            return self._parent._cast(_2326.ClutchSocket)

        @property
        def concept_coupling_socket(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2328
            
            return self._parent._cast(_2328.ConceptCouplingSocket)

        @property
        def coupling_socket(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2330
            
            return self._parent._cast(_2330.CouplingSocket)

        @property
        def part_to_part_shear_coupling_socket(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2332
            
            return self._parent._cast(_2332.PartToPartShearCouplingSocket)

        @property
        def spring_damper_socket(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2334
            
            return self._parent._cast(_2334.SpringDamperSocket)

        @property
        def torque_converter_pump_socket(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2336
            
            return self._parent._cast(_2336.TorqueConverterPumpSocket)

        @property
        def torque_converter_turbine_socket(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2337
            
            return self._parent._cast(_2337.TorqueConverterTurbineSocket)

        @property
        def socket(self) -> 'Socket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Socket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def connected_components(self) -> 'List[_2427.Component]':
        """List[Component]: 'ConnectedComponents' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectedComponents

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connections(self) -> 'List[_2255.Connection]':
        """List[Connection]: 'Connections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def owner(self) -> '_2427.Component':
        """Component: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def connect_to(self, component: '_2427.Component') -> '_2428.ComponentsConnectedResult':
        """ 'ConnectTo' is the original name of this method.

        Args:
            component (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.part_model.ComponentsConnectedResult
        """

        method_result = self.wrapped.ConnectTo.Overloads[_COMPONENT](component.wrapped if component else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def connect_to_socket(self, socket: 'Socket') -> '_2428.ComponentsConnectedResult':
        """ 'ConnectTo' is the original name of this method.

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)

        Returns:
            mastapy.system_model.part_model.ComponentsConnectedResult
        """

        method_result = self.wrapped.ConnectTo.Overloads[_SOCKET](socket.wrapped if socket else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def connection_to(self, socket: 'Socket') -> '_2255.Connection':
        """ 'ConnectionTo' is the original name of this method.

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)

        Returns:
            mastapy.system_model.connections_and_sockets.Connection
        """

        method_result = self.wrapped.ConnectionTo(socket.wrapped if socket else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_possible_sockets_to_connect_to(self, component_to_connect_to: '_2427.Component') -> 'List[Socket]':
        """ 'GetPossibleSocketsToConnectTo' is the original name of this method.

        Args:
            component_to_connect_to (mastapy.system_model.part_model.Component)

        Returns:
            List[mastapy.system_model.connections_and_sockets.Socket]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.GetPossibleSocketsToConnectTo(component_to_connect_to.wrapped if component_to_connect_to else None))

    @property
    def cast_to(self) -> 'Socket._Cast_Socket':
        return self._Cast_Socket(self)
