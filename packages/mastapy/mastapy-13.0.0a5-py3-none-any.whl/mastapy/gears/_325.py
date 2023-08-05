"""_325.py

GearNURBSSurface
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears import _318
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_NURBS_SURFACE = python_net_import('SMT.MastaAPI.Gears', 'GearNURBSSurface')


__docformat__ = 'restructuredtext en'
__all__ = ('GearNURBSSurface',)


class GearNURBSSurface(_318.ConicalGearToothSurface):
    """GearNURBSSurface

    This is a mastapy class.
    """

    TYPE = _GEAR_NURBS_SURFACE

    class _Cast_GearNURBSSurface:
        """Special nested class for casting GearNURBSSurface to subclasses."""

        def __init__(self, parent: 'GearNURBSSurface'):
            self._parent = parent

        @property
        def conical_gear_tooth_surface(self):
            return self._parent._cast(_318.ConicalGearToothSurface)

        @property
        def gear_nurbs_surface(self) -> 'GearNURBSSurface':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearNURBSSurface.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearNURBSSurface._Cast_GearNURBSSurface':
        return self._Cast_GearNURBSSurface(self)
