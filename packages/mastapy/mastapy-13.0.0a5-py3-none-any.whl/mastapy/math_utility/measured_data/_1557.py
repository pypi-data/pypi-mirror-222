"""_1557.py

LookupTableBase
"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.implicit import enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.utility import _1577
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOOKUP_TABLE_BASE = python_net_import('SMT.MastaAPI.MathUtility.MeasuredData', 'LookupTableBase')

if TYPE_CHECKING:
    from mastapy.math_utility import _1500


__docformat__ = 'restructuredtext en'
__all__ = ('LookupTableBase',)


T = TypeVar('T', bound='LookupTableBase')


class LookupTableBase(_1577.IndependentReportablePropertiesBase[T]):
    """LookupTableBase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _LOOKUP_TABLE_BASE

    class _Cast_LookupTableBase:
        """Special nested class for casting LookupTableBase to subclasses."""

        def __init__(self, parent: 'LookupTableBase'):
            self._parent = parent

        @property
        def independent_reportable_properties_base(self):
            return self._parent._cast(_1577.IndependentReportablePropertiesBase)

        @property
        def onedimensional_function_lookup_table(self):
            from mastapy.math_utility.measured_data import _1558
            
            return self._parent._cast(_1558.OnedimensionalFunctionLookupTable)

        @property
        def twodimensional_function_lookup_table(self):
            from mastapy.math_utility.measured_data import _1559
            
            return self._parent._cast(_1559.TwodimensionalFunctionLookupTable)

        @property
        def lookup_table_base(self) -> 'LookupTableBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LookupTableBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def extrapolation_option(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions':
        """enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions: 'ExtrapolationOption' is the original name of this property."""

        temp = self.wrapped.ExtrapolationOption

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @extrapolation_option.setter
    def extrapolation_option(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ExtrapolationOption = value

    @property
    def cast_to(self) -> 'LookupTableBase._Cast_LookupTableBase':
        return self._Cast_LookupTableBase(self)
