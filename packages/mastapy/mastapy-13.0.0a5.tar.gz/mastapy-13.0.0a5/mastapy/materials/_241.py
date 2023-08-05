﻿"""_241.py

AirProperties
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AIR_PROPERTIES = python_net_import('SMT.MastaAPI.Materials', 'AirProperties')


__docformat__ = 'restructuredtext en'
__all__ = ('AirProperties',)


class AirProperties(_0.APIBase):
    """AirProperties

    This is a mastapy class.
    """

    TYPE = _AIR_PROPERTIES

    class _Cast_AirProperties:
        """Special nested class for casting AirProperties to subclasses."""

        def __init__(self, parent: 'AirProperties'):
            self._parent = parent

        @property
        def air_properties(self) -> 'AirProperties':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AirProperties.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def adiabatic_index(self) -> 'float':
        """float: 'AdiabaticIndex' is the original name of this property."""

        temp = self.wrapped.AdiabaticIndex

        if temp is None:
            return 0.0

        return temp

    @adiabatic_index.setter
    def adiabatic_index(self, value: 'float'):
        self.wrapped.AdiabaticIndex = float(value) if value is not None else 0.0

    @property
    def pressure(self) -> 'float':
        """float: 'Pressure' is the original name of this property."""

        temp = self.wrapped.Pressure

        if temp is None:
            return 0.0

        return temp

    @pressure.setter
    def pressure(self, value: 'float'):
        self.wrapped.Pressure = float(value) if value is not None else 0.0

    @property
    def specific_gas_constant(self) -> 'float':
        """float: 'SpecificGasConstant' is the original name of this property."""

        temp = self.wrapped.SpecificGasConstant

        if temp is None:
            return 0.0

        return temp

    @specific_gas_constant.setter
    def specific_gas_constant(self, value: 'float'):
        self.wrapped.SpecificGasConstant = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'AirProperties._Cast_AirProperties':
        return self._Cast_AirProperties(self)
