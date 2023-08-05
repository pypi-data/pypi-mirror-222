"""_812.py

WheelFinishCutter
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.gear_designs.conical import _1149
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WHEEL_FINISH_CUTTER = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel.Cutters', 'WheelFinishCutter')


__docformat__ = 'restructuredtext en'
__all__ = ('WheelFinishCutter',)


class WheelFinishCutter(_1149.ConicalGearCutter):
    """WheelFinishCutter

    This is a mastapy class.
    """

    TYPE = _WHEEL_FINISH_CUTTER

    class _Cast_WheelFinishCutter:
        """Special nested class for casting WheelFinishCutter to subclasses."""

        def __init__(self, parent: 'WheelFinishCutter'):
            self._parent = parent

        @property
        def conical_gear_cutter(self):
            return self._parent._cast(_1149.ConicalGearCutter)

        @property
        def wheel_finish_cutter(self) -> 'WheelFinishCutter':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WheelFinishCutter.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def point_width(self) -> 'float':
        """float: 'PointWidth' is the original name of this property."""

        temp = self.wrapped.PointWidth

        if temp is None:
            return 0.0

        return temp

    @point_width.setter
    def point_width(self, value: 'float'):
        self.wrapped.PointWidth = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'WheelFinishCutter._Cast_WheelFinishCutter':
        return self._Cast_WheelFinishCutter(self)
