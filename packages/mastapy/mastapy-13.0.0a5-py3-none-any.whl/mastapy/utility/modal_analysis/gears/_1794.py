﻿"""_1794.py

OrderSelector
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.modal_analysis.gears import _1793
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ORDER_SELECTOR = python_net_import('SMT.MastaAPI.Utility.ModalAnalysis.Gears', 'OrderSelector')


__docformat__ = 'restructuredtext en'
__all__ = ('OrderSelector',)


class OrderSelector(_1793.OrderForTE):
    """OrderSelector

    This is a mastapy class.
    """

    TYPE = _ORDER_SELECTOR

    class _Cast_OrderSelector:
        """Special nested class for casting OrderSelector to subclasses."""

        def __init__(self, parent: 'OrderSelector'):
            self._parent = parent

        @property
        def order_for_te(self):
            return self._parent._cast(_1793.OrderForTE)

        @property
        def order_selector(self) -> 'OrderSelector':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OrderSelector.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'OrderSelector._Cast_OrderSelector':
        return self._Cast_OrderSelector(self)
