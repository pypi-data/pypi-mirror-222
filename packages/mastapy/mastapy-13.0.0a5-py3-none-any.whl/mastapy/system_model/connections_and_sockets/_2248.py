"""_2248.py

AbstractShaftToMountableComponentConnection
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets import _2255
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'AbstractShaftToMountableComponentConnection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2447, _2418


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftToMountableComponentConnection',)


class AbstractShaftToMountableComponentConnection(_2255.Connection):
    """AbstractShaftToMountableComponentConnection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION

    class _Cast_AbstractShaftToMountableComponentConnection:
        """Special nested class for casting AbstractShaftToMountableComponentConnection to subclasses."""

        def __init__(self, parent: 'AbstractShaftToMountableComponentConnection'):
            self._parent = parent

        @property
        def connection(self):
            return self._parent._cast(_2255.Connection)

        @property
        def design_entity(self):
            from mastapy.system_model import _2190
            
            return self._parent._cast(_2190.DesignEntity)

        @property
        def coaxial_connection(self):
            from mastapy.system_model.connections_and_sockets import _2252
            
            return self._parent._cast(_2252.CoaxialConnection)

        @property
        def planetary_connection(self):
            from mastapy.system_model.connections_and_sockets import _2270
            
            return self._parent._cast(_2270.PlanetaryConnection)

        @property
        def shaft_to_mountable_component_connection(self):
            from mastapy.system_model.connections_and_sockets import _2278
            
            return self._parent._cast(_2278.ShaftToMountableComponentConnection)

        @property
        def cycloidal_disc_central_bearing_connection(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2318
            
            return self._parent._cast(_2318.CycloidalDiscCentralBearingConnection)

        @property
        def cycloidal_disc_planetary_bearing_connection(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2321
            
            return self._parent._cast(_2321.CycloidalDiscPlanetaryBearingConnection)

        @property
        def abstract_shaft_to_mountable_component_connection(self) -> 'AbstractShaftToMountableComponentConnection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftToMountableComponentConnection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mountable_component(self) -> '_2447.MountableComponent':
        """MountableComponent: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft(self) -> '_2418.AbstractShaft':
        """AbstractShaft: 'Shaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shaft

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection':
        return self._Cast_AbstractShaftToMountableComponentConnection(self)
