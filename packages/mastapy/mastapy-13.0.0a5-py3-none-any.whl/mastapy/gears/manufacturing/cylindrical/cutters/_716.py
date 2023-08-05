"""_716.py

MutableCommon
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.manufacturing.cylindrical.cutters import _700
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MUTABLE_COMMON = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'MutableCommon')

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _606


__docformat__ = 'restructuredtext en'
__all__ = ('MutableCommon',)


class MutableCommon(_700.CurveInLinkedList):
    """MutableCommon

    This is a mastapy class.
    """

    TYPE = _MUTABLE_COMMON

    class _Cast_MutableCommon:
        """Special nested class for casting MutableCommon to subclasses."""

        def __init__(self, parent: 'MutableCommon'):
            self._parent = parent

        @property
        def curve_in_linked_list(self):
            return self._parent._cast(_700.CurveInLinkedList)

        @property
        def mutable_curve(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _717
            
            return self._parent._cast(_717.MutableCurve)

        @property
        def mutable_fillet(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _718
            
            return self._parent._cast(_718.MutableFillet)

        @property
        def mutable_common(self) -> 'MutableCommon':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MutableCommon.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def protuberance(self) -> 'float':
        """float: 'Protuberance' is the original name of this property."""

        temp = self.wrapped.Protuberance

        if temp is None:
            return 0.0

        return temp

    @protuberance.setter
    def protuberance(self, value: 'float'):
        self.wrapped.Protuberance = float(value) if value is not None else 0.0

    @property
    def radius(self) -> 'float':
        """float: 'Radius' is the original name of this property."""

        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @radius.setter
    def radius(self, value: 'float'):
        self.wrapped.Radius = float(value) if value is not None else 0.0

    @property
    def section(self) -> 'enum_with_selected_value.EnumWithSelectedValue_CutterFlankSections':
        """enum_with_selected_value.EnumWithSelectedValue_CutterFlankSections: 'Section' is the original name of this property."""

        temp = self.wrapped.Section

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_CutterFlankSections.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @section.setter
    def section(self, value: 'enum_with_selected_value.EnumWithSelectedValue_CutterFlankSections.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_CutterFlankSections.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.Section = value

    def remove(self):
        """ 'Remove' is the original name of this method."""

        self.wrapped.Remove()

    def split(self):
        """ 'Split' is the original name of this method."""

        self.wrapped.Split()

    @property
    def cast_to(self) -> 'MutableCommon._Cast_MutableCommon':
        return self._Cast_MutableCommon(self)
