﻿"""_1087.py

NominalValueSpecification
"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical import _1079
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NOMINAL_VALUE_SPECIFICATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ThicknessStockAndBacklash', 'NominalValueSpecification')


__docformat__ = 'restructuredtext en'
__all__ = ('NominalValueSpecification',)


T = TypeVar('T')


class NominalValueSpecification(_1079.TolerancedValueSpecification[T]):
    """NominalValueSpecification

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _NOMINAL_VALUE_SPECIFICATION

    class _Cast_NominalValueSpecification:
        """Special nested class for casting NominalValueSpecification to subclasses."""

        def __init__(self, parent: 'NominalValueSpecification'):
            self._parent = parent

        @property
        def toleranced_value_specification(self):
            return self._parent._cast(_1079.TolerancedValueSpecification)

        @property
        def relative_measurement_view_model(self):
            from mastapy.gears.gear_designs.cylindrical import _1063
            
            return self._parent._cast(_1063.RelativeMeasurementViewModel)

        @property
        def nominal_value_specification(self) -> 'NominalValueSpecification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NominalValueSpecification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Design' is the original name of this property."""

        temp = self.wrapped.Design

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @design.setter
    def design(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Design = value

    @property
    def cast_to(self) -> 'NominalValueSpecification._Cast_NominalValueSpecification':
        return self._Cast_NominalValueSpecification(self)
