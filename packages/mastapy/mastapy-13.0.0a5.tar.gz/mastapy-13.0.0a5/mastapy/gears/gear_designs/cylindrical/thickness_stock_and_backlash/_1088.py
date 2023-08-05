"""_1088.py

NoValueSpecification
"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.cylindrical import _1079
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NO_VALUE_SPECIFICATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ThicknessStockAndBacklash', 'NoValueSpecification')


__docformat__ = 'restructuredtext en'
__all__ = ('NoValueSpecification',)


T = TypeVar('T')


class NoValueSpecification(_1079.TolerancedValueSpecification[T]):
    """NoValueSpecification

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _NO_VALUE_SPECIFICATION

    class _Cast_NoValueSpecification:
        """Special nested class for casting NoValueSpecification to subclasses."""

        def __init__(self, parent: 'NoValueSpecification'):
            self._parent = parent

        @property
        def toleranced_value_specification(self):
            return self._parent._cast(_1079.TolerancedValueSpecification)

        @property
        def relative_measurement_view_model(self):
            from mastapy.gears.gear_designs.cylindrical import _1063
            
            return self._parent._cast(_1063.RelativeMeasurementViewModel)

        @property
        def no_value_specification(self) -> 'NoValueSpecification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NoValueSpecification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'NoValueSpecification._Cast_NoValueSpecification':
        return self._Cast_NoValueSpecification(self)
