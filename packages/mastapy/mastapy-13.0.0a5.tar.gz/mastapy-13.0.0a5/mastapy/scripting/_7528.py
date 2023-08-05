﻿"""_7528.py

ApiEnumForAttribute
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_API_ENUM_FOR_ATTRIBUTE = python_net_import('SMT.MastaAPIUtility.Scripting', 'ApiEnumForAttribute')


__docformat__ = 'restructuredtext en'
__all__ = ('ApiEnumForAttribute',)


class ApiEnumForAttribute:
    """ApiEnumForAttribute

    This is a mastapy class.
    """

    TYPE = _API_ENUM_FOR_ATTRIBUTE

    class _Cast_ApiEnumForAttribute:
        """Special nested class for casting ApiEnumForAttribute to subclasses."""

        def __init__(self, parent: 'ApiEnumForAttribute'):
            self._parent = parent

        @property
        def api_enum_for_attribute(self) -> 'ApiEnumForAttribute':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ApiEnumForAttribute.TYPE'):
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
    def wrapped_enum(self) -> 'type':
        """type: 'WrappedEnum' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WrappedEnum

        if temp is None:
            return None

        return temp

    @staticmethod
    def get_wrapped_enum_from(api_enum_type: 'type') -> 'type':
        """ 'GetWrappedEnumFrom' is the original name of this method.

        Args:
            api_enum_type (type)

        Returns:
            type
        """

        method_result = ApiEnumForAttribute.TYPE.GetWrappedEnumFrom(api_enum_type)
        return method_result

    @property
    def cast_to(self) -> 'ApiEnumForAttribute._Cast_ApiEnumForAttribute':
        return self._Cast_ApiEnumForAttribute(self)
