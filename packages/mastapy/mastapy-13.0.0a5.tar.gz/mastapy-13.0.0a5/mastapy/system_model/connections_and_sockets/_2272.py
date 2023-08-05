"""_2272.py

PlanetarySocketBase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets import _2259
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_SOCKET_BASE = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'PlanetarySocketBase')

if TYPE_CHECKING:
    from mastapy.gears import _338


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetarySocketBase',)


class PlanetarySocketBase(_2259.CylindricalSocket):
    """PlanetarySocketBase

    This is a mastapy class.
    """

    TYPE = _PLANETARY_SOCKET_BASE

    class _Cast_PlanetarySocketBase:
        """Special nested class for casting PlanetarySocketBase to subclasses."""

        def __init__(self, parent: 'PlanetarySocketBase'):
            self._parent = parent

        @property
        def cylindrical_socket(self):
            return self._parent._cast(_2259.CylindricalSocket)

        @property
        def socket(self):
            from mastapy.system_model.connections_and_sockets import _2279
            
            return self._parent._cast(_2279.Socket)

        @property
        def planetary_socket(self):
            from mastapy.system_model.connections_and_sockets import _2271
            
            return self._parent._cast(_2271.PlanetarySocket)

        @property
        def cycloidal_disc_planetary_bearing_socket(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2322
            
            return self._parent._cast(_2322.CycloidalDiscPlanetaryBearingSocket)

        @property
        def planetary_socket_base(self) -> 'PlanetarySocketBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetarySocketBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def draw_on_lower_half_of_2d(self) -> 'bool':
        """bool: 'DrawOnLowerHalfOf2D' is the original name of this property."""

        temp = self.wrapped.DrawOnLowerHalfOf2D

        if temp is None:
            return False

        return temp

    @draw_on_lower_half_of_2d.setter
    def draw_on_lower_half_of_2d(self, value: 'bool'):
        self.wrapped.DrawOnLowerHalfOf2D = bool(value) if value is not None else False

    @property
    def draw_on_upper_half_of_2d(self) -> 'bool':
        """bool: 'DrawOnUpperHalfOf2D' is the original name of this property."""

        temp = self.wrapped.DrawOnUpperHalfOf2D

        if temp is None:
            return False

        return temp

    @draw_on_upper_half_of_2d.setter
    def draw_on_upper_half_of_2d(self, value: 'bool'):
        self.wrapped.DrawOnUpperHalfOf2D = bool(value) if value is not None else False

    @property
    def editable_name(self) -> 'str':
        """str: 'EditableName' is the original name of this property."""

        temp = self.wrapped.EditableName

        if temp is None:
            return ''

        return temp

    @editable_name.setter
    def editable_name(self, value: 'str'):
        self.wrapped.EditableName = str(value) if value is not None else ''

    @property
    def planetary_load_sharing_factor(self) -> 'float':
        """float: 'PlanetaryLoadSharingFactor' is the original name of this property."""

        temp = self.wrapped.PlanetaryLoadSharingFactor

        if temp is None:
            return 0.0

        return temp

    @planetary_load_sharing_factor.setter
    def planetary_load_sharing_factor(self, value: 'float'):
        self.wrapped.PlanetaryLoadSharingFactor = float(value) if value is not None else 0.0

    @property
    def width(self) -> 'float':
        """float: 'Width' is the original name of this property."""

        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    def width(self, value: 'float'):
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def planetary_details(self) -> '_338.PlanetaryDetail':
        """PlanetaryDetail: 'PlanetaryDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetaryDetails

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PlanetarySocketBase._Cast_PlanetarySocketBase':
        return self._Cast_PlanetarySocketBase(self)
