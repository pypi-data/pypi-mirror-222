﻿"""_2561.py

ClutchHalf
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.part_model.couplings import _2566
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ClutchHalf')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchHalf',)


class ClutchHalf(_2566.CouplingHalf):
    """ClutchHalf

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF

    class _Cast_ClutchHalf:
        """Special nested class for casting ClutchHalf to subclasses."""

        def __init__(self, parent: 'ClutchHalf'):
            self._parent = parent

        @property
        def coupling_half(self):
            return self._parent._cast(_2566.CouplingHalf)

        @property
        def mountable_component(self):
            from mastapy.system_model.part_model import _2447
            
            return self._parent._cast(_2447.MountableComponent)

        @property
        def component(self):
            from mastapy.system_model.part_model import _2427
            
            return self._parent._cast(_2427.Component)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2451
            
            return self._parent._cast(_2451.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2190
            
            return self._parent._cast(_2190.DesignEntity)

        @property
        def clutch_half(self) -> 'ClutchHalf':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ClutchHalf.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_mounted_on_shaft_outer(self) -> 'bool':
        """bool: 'IsMountedOnShaftOuter' is the original name of this property."""

        temp = self.wrapped.IsMountedOnShaftOuter

        if temp is None:
            return False

        return temp

    @is_mounted_on_shaft_outer.setter
    def is_mounted_on_shaft_outer(self, value: 'bool'):
        self.wrapped.IsMountedOnShaftOuter = bool(value) if value is not None else False

    @property
    def cast_to(self) -> 'ClutchHalf._Cast_ClutchHalf':
        return self._Cast_ClutchHalf(self)
