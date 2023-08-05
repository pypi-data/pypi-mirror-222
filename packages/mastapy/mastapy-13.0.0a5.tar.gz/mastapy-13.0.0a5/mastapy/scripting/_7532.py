﻿"""_7532.py

MastaPropertyAttribute
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASTA_PROPERTY_ATTRIBUTE = python_net_import('SMT.MastaAPIUtility.Scripting', 'MastaPropertyAttribute')

if TYPE_CHECKING:
    from mastapy.units_and_measurements import _7526


__docformat__ = 'restructuredtext en'
__all__ = ('MastaPropertyAttribute',)


class MastaPropertyAttribute:
    """MastaPropertyAttribute

    This is a mastapy class.
    """

    TYPE = _MASTA_PROPERTY_ATTRIBUTE

    class _Cast_MastaPropertyAttribute:
        """Special nested class for casting MastaPropertyAttribute to subclasses."""

        def __init__(self, parent: 'MastaPropertyAttribute'):
            self._parent = parent

        @property
        def masta_property_attribute(self) -> 'MastaPropertyAttribute':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MastaPropertyAttribute.TYPE'):
        self.wrapped = instance_to_wrap
        if not hasattr(self.wrapped, 'reference_count'):
            self.wrapped.reference_count = 0
        self.wrapped.reference_count += 1
        self._freeze()

    __frozen = False

    def __setattr__(self, attr, value):
        prop = getattr(self.__class__, attr, None)
        if isinstance(prop, property):
            prop.fset(self, value)
        else:
            if self.__frozen and attr not in self.__dict__:
                raise AttributeError((
                    'Attempted to set unknown '
                    'attribute: \'{}\''.format(attr))) from None

            super().__setattr__(attr, value)

    def __delattr__(self, name):
        raise AttributeError(
            'Cannot delete the attributes of a mastapy object.') from None

    def _freeze(self):
        self.__frozen = True

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def description(self) -> 'str':
        """str: 'Description' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Description

        if temp is None:
            return ''

        return temp

    @property
    def symbol(self) -> 'str':
        """str: 'Symbol' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Symbol

        if temp is None:
            return ''

        return temp

    @property
    def measurement(self) -> '_7526.MeasurementType':
        """MeasurementType: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPIUtility.UnitsAndMeasurements.MeasurementType')
        return constructor.new_from_mastapy('mastapy.units_and_measurements._7526', 'MeasurementType')(value) if value is not None else None

    @property
    def cast_to(self) -> 'MastaPropertyAttribute._Cast_MastaPropertyAttribute':
        return self._Cast_MastaPropertyAttribute(self)
