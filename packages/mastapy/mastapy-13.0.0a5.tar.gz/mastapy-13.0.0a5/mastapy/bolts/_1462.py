﻿"""_1462.py

BoltSection
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_SECTION = python_net_import('SMT.MastaAPI.Bolts', 'BoltSection')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltSection',)


class BoltSection(_0.APIBase):
    """BoltSection

    This is a mastapy class.
    """

    TYPE = _BOLT_SECTION

    class _Cast_BoltSection:
        """Special nested class for casting BoltSection to subclasses."""

        def __init__(self, parent: 'BoltSection'):
            self._parent = parent

        @property
        def bolt_section(self) -> 'BoltSection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BoltSection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diameter(self) -> 'float':
        """float: 'Diameter' is the original name of this property."""

        temp = self.wrapped.Diameter

        if temp is None:
            return 0.0

        return temp

    @diameter.setter
    def diameter(self, value: 'float'):
        self.wrapped.Diameter = float(value) if value is not None else 0.0

    @property
    def inner_diameter(self) -> 'float':
        """float: 'InnerDiameter' is the original name of this property."""

        temp = self.wrapped.InnerDiameter

        if temp is None:
            return 0.0

        return temp

    @inner_diameter.setter
    def inner_diameter(self, value: 'float'):
        self.wrapped.InnerDiameter = float(value) if value is not None else 0.0

    @property
    def length(self) -> 'float':
        """float: 'Length' is the original name of this property."""

        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    def length(self, value: 'float'):
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'BoltSection._Cast_BoltSection':
        return self._Cast_BoltSection(self)
