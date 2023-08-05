﻿"""_1888.py

BearingConnectionComponent
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_CONNECTION_COMPONENT = python_net_import('SMT.MastaAPI.Bearings.Tolerances', 'BearingConnectionComponent')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingConnectionComponent',)


class BearingConnectionComponent(_0.APIBase):
    """BearingConnectionComponent

    This is a mastapy class.
    """

    TYPE = _BEARING_CONNECTION_COMPONENT

    class _Cast_BearingConnectionComponent:
        """Special nested class for casting BearingConnectionComponent to subclasses."""

        def __init__(self, parent: 'BearingConnectionComponent'):
            self._parent = parent

        @property
        def inner_ring_tolerance(self):
            from mastapy.bearings.tolerances import _1893
            
            return self._parent._cast(_1893.InnerRingTolerance)

        @property
        def inner_support_tolerance(self):
            from mastapy.bearings.tolerances import _1894
            
            return self._parent._cast(_1894.InnerSupportTolerance)

        @property
        def interference_detail(self):
            from mastapy.bearings.tolerances import _1895
            
            return self._parent._cast(_1895.InterferenceDetail)

        @property
        def interference_tolerance(self):
            from mastapy.bearings.tolerances import _1896
            
            return self._parent._cast(_1896.InterferenceTolerance)

        @property
        def mounting_sleeve_diameter_detail(self):
            from mastapy.bearings.tolerances import _1898
            
            return self._parent._cast(_1898.MountingSleeveDiameterDetail)

        @property
        def outer_ring_tolerance(self):
            from mastapy.bearings.tolerances import _1899
            
            return self._parent._cast(_1899.OuterRingTolerance)

        @property
        def outer_support_tolerance(self):
            from mastapy.bearings.tolerances import _1900
            
            return self._parent._cast(_1900.OuterSupportTolerance)

        @property
        def race_detail(self):
            from mastapy.bearings.tolerances import _1901
            
            return self._parent._cast(_1901.RaceDetail)

        @property
        def ring_tolerance(self):
            from mastapy.bearings.tolerances import _1904
            
            return self._parent._cast(_1904.RingTolerance)

        @property
        def support_detail(self):
            from mastapy.bearings.tolerances import _1907
            
            return self._parent._cast(_1907.SupportDetail)

        @property
        def support_tolerance(self):
            from mastapy.bearings.tolerances import _1909
            
            return self._parent._cast(_1909.SupportTolerance)

        @property
        def bearing_connection_component(self) -> 'BearingConnectionComponent':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BearingConnectionComponent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BearingConnectionComponent._Cast_BearingConnectionComponent':
        return self._Cast_BearingConnectionComponent(self)
