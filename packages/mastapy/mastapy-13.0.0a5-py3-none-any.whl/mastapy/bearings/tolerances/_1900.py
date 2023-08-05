﻿"""_1900.py

OuterSupportTolerance
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.bearings.tolerances import _1909
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OUTER_SUPPORT_TOLERANCE = python_net_import('SMT.MastaAPI.Bearings.Tolerances', 'OuterSupportTolerance')


__docformat__ = 'restructuredtext en'
__all__ = ('OuterSupportTolerance',)


class OuterSupportTolerance(_1909.SupportTolerance):
    """OuterSupportTolerance

    This is a mastapy class.
    """

    TYPE = _OUTER_SUPPORT_TOLERANCE

    class _Cast_OuterSupportTolerance:
        """Special nested class for casting OuterSupportTolerance to subclasses."""

        def __init__(self, parent: 'OuterSupportTolerance'):
            self._parent = parent

        @property
        def support_tolerance(self):
            return self._parent._cast(_1909.SupportTolerance)

        @property
        def interference_tolerance(self):
            from mastapy.bearings.tolerances import _1896
            
            return self._parent._cast(_1896.InterferenceTolerance)

        @property
        def bearing_connection_component(self):
            from mastapy.bearings.tolerances import _1888
            
            return self._parent._cast(_1888.BearingConnectionComponent)

        @property
        def outer_support_tolerance(self) -> 'OuterSupportTolerance':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OuterSupportTolerance.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'OuterSupportTolerance._Cast_OuterSupportTolerance':
        return self._Cast_OuterSupportTolerance(self)
