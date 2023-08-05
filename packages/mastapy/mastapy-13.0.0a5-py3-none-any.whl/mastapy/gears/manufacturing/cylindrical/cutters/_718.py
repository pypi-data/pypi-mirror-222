"""_718.py

MutableFillet
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutters import _716
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MUTABLE_FILLET = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'MutableFillet')


__docformat__ = 'restructuredtext en'
__all__ = ('MutableFillet',)


class MutableFillet(_716.MutableCommon):
    """MutableFillet

    This is a mastapy class.
    """

    TYPE = _MUTABLE_FILLET

    class _Cast_MutableFillet:
        """Special nested class for casting MutableFillet to subclasses."""

        def __init__(self, parent: 'MutableFillet'):
            self._parent = parent

        @property
        def mutable_common(self):
            return self._parent._cast(_716.MutableCommon)

        @property
        def curve_in_linked_list(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _700
            
            return self._parent._cast(_700.CurveInLinkedList)

        @property
        def mutable_fillet(self) -> 'MutableFillet':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MutableFillet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def radius(self) -> 'float':
        """float: 'Radius' is the original name of this property."""

        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @radius.setter
    def radius(self, value: 'float'):
        self.wrapped.Radius = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'MutableFillet._Cast_MutableFillet':
        return self._Cast_MutableFillet(self)
