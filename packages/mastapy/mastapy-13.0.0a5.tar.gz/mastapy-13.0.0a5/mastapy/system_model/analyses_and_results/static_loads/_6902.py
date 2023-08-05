﻿"""_6902.py

PlanetarySocketManufactureError
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_SOCKET_MANUFACTURE_ERROR = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PlanetarySocketManufactureError')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6904


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetarySocketManufactureError',)


class PlanetarySocketManufactureError(_0.APIBase):
    """PlanetarySocketManufactureError

    This is a mastapy class.
    """

    TYPE = _PLANETARY_SOCKET_MANUFACTURE_ERROR

    class _Cast_PlanetarySocketManufactureError:
        """Special nested class for casting PlanetarySocketManufactureError to subclasses."""

        def __init__(self, parent: 'PlanetarySocketManufactureError'):
            self._parent = parent

        @property
        def planetary_socket_manufacture_error(self) -> 'PlanetarySocketManufactureError':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetarySocketManufactureError.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def socket_name(self) -> 'str':
        """str: 'SocketName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketName

        if temp is None:
            return ''

        return temp

    @property
    def planet_manufacture_errors(self) -> 'List[_6904.PlanetManufactureError]':
        """List[PlanetManufactureError]: 'PlanetManufactureErrors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetManufactureErrors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PlanetarySocketManufactureError._Cast_PlanetarySocketManufactureError':
        return self._Cast_PlanetarySocketManufactureError(self)
