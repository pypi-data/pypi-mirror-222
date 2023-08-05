"""_1072.py

StandardRack
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.gear_designs.cylindrical import _1005
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STANDARD_RACK = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'StandardRack')


__docformat__ = 'restructuredtext en'
__all__ = ('StandardRack',)


class StandardRack(_1005.CylindricalGearBasicRack):
    """StandardRack

    This is a mastapy class.
    """

    TYPE = _STANDARD_RACK

    class _Cast_StandardRack:
        """Special nested class for casting StandardRack to subclasses."""

        def __init__(self, parent: 'StandardRack'):
            self._parent = parent

        @property
        def cylindrical_gear_basic_rack(self):
            return self._parent._cast(_1005.CylindricalGearBasicRack)

        @property
        def cylindrical_gear_abstract_rack(self):
            from mastapy.gears.gear_designs.cylindrical import _1003
            
            return self._parent._cast(_1003.CylindricalGearAbstractRack)

        @property
        def standard_rack(self) -> 'StandardRack':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StandardRack.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'StandardRack._Cast_StandardRack':
        return self._Cast_StandardRack(self)
