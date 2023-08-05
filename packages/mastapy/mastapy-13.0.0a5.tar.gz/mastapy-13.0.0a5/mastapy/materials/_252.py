﻿"""_252.py

FatigueSafetyFactorItemBase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.materials import _278
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FATIGUE_SAFETY_FACTOR_ITEM_BASE = python_net_import('SMT.MastaAPI.Materials', 'FatigueSafetyFactorItemBase')


__docformat__ = 'restructuredtext en'
__all__ = ('FatigueSafetyFactorItemBase',)


class FatigueSafetyFactorItemBase(_278.SafetyFactorItem):
    """FatigueSafetyFactorItemBase

    This is a mastapy class.
    """

    TYPE = _FATIGUE_SAFETY_FACTOR_ITEM_BASE

    class _Cast_FatigueSafetyFactorItemBase:
        """Special nested class for casting FatigueSafetyFactorItemBase to subclasses."""

        def __init__(self, parent: 'FatigueSafetyFactorItemBase'):
            self._parent = parent

        @property
        def safety_factor_item(self):
            return self._parent._cast(_278.SafetyFactorItem)

        @property
        def composite_fatigue_safety_factor_item(self):
            from mastapy.materials import _248
            
            return self._parent._cast(_248.CompositeFatigueSafetyFactorItem)

        @property
        def fatigue_safety_factor_item(self):
            from mastapy.materials import _251
            
            return self._parent._cast(_251.FatigueSafetyFactorItem)

        @property
        def fatigue_safety_factor_item_base(self) -> 'FatigueSafetyFactorItemBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FatigueSafetyFactorItemBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'FatigueSafetyFactorItemBase._Cast_FatigueSafetyFactorItemBase':
        return self._Cast_FatigueSafetyFactorItemBase(self)
