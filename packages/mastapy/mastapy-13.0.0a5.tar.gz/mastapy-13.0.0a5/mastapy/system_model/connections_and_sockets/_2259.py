"""_2259.py

CylindricalSocket
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.connections_and_sockets import _2279
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'CylindricalSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalSocket',)


class CylindricalSocket(_2279.Socket):
    """CylindricalSocket

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_SOCKET

    class _Cast_CylindricalSocket:
        """Special nested class for casting CylindricalSocket to subclasses."""

        def __init__(self, parent: 'CylindricalSocket'):
            self._parent = parent

        @property
        def socket(self):
            return self._parent._cast(_2279.Socket)

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
        def cylindrical_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2293
            
            return self._parent._cast(_2293.CylindricalGearTeethSocket)

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
        def cylindrical_socket(self) -> 'CylindricalSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalSocket._Cast_CylindricalSocket':
        return self._Cast_CylindricalSocket(self)
