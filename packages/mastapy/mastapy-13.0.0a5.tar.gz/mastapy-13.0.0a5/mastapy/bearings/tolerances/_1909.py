"""_1909.py

SupportTolerance
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal.implicit import enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.bearings.tolerances import _1896
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SUPPORT_TOLERANCE = python_net_import('SMT.MastaAPI.Bearings.Tolerances', 'SupportTolerance')

if TYPE_CHECKING:
    from mastapy.bearings.tolerances import _1897, _1910


__docformat__ = 'restructuredtext en'
__all__ = ('SupportTolerance',)


class SupportTolerance(_1896.InterferenceTolerance):
    """SupportTolerance

    This is a mastapy class.
    """

    TYPE = _SUPPORT_TOLERANCE

    class _Cast_SupportTolerance:
        """Special nested class for casting SupportTolerance to subclasses."""

        def __init__(self, parent: 'SupportTolerance'):
            self._parent = parent

        @property
        def interference_tolerance(self):
            return self._parent._cast(_1896.InterferenceTolerance)

        @property
        def bearing_connection_component(self):
            from mastapy.bearings.tolerances import _1888
            
            return self._parent._cast(_1888.BearingConnectionComponent)

        @property
        def inner_support_tolerance(self):
            from mastapy.bearings.tolerances import _1894
            
            return self._parent._cast(_1894.InnerSupportTolerance)

        @property
        def outer_support_tolerance(self):
            from mastapy.bearings.tolerances import _1900
            
            return self._parent._cast(_1900.OuterSupportTolerance)

        @property
        def support_tolerance(self) -> 'SupportTolerance':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SupportTolerance.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def tolerance_band_designation(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ITDesignation':
        """enum_with_selected_value.EnumWithSelectedValue_ITDesignation: 'ToleranceBandDesignation' is the original name of this property."""

        temp = self.wrapped.ToleranceBandDesignation

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_ITDesignation.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @tolerance_band_designation.setter
    def tolerance_band_designation(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ITDesignation.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ITDesignation.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ToleranceBandDesignation = value

    @property
    def tolerance_deviation_class(self) -> 'enum_with_selected_value.EnumWithSelectedValue_SupportToleranceLocationDesignation':
        """enum_with_selected_value.EnumWithSelectedValue_SupportToleranceLocationDesignation: 'ToleranceDeviationClass' is the original name of this property."""

        temp = self.wrapped.ToleranceDeviationClass

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_SupportToleranceLocationDesignation.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @tolerance_deviation_class.setter
    def tolerance_deviation_class(self, value: 'enum_with_selected_value.EnumWithSelectedValue_SupportToleranceLocationDesignation.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_SupportToleranceLocationDesignation.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ToleranceDeviationClass = value

    @property
    def cast_to(self) -> 'SupportTolerance._Cast_SupportTolerance':
        return self._Cast_SupportTolerance(self)
