"""_1742.py

CustomDrawing
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.utility.report import _1743
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_DRAWING = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomDrawing')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomDrawing',)


class CustomDrawing(_1743.CustomGraphic):
    """CustomDrawing

    This is a mastapy class.
    """

    TYPE = _CUSTOM_DRAWING

    class _Cast_CustomDrawing:
        """Special nested class for casting CustomDrawing to subclasses."""

        def __init__(self, parent: 'CustomDrawing'):
            self._parent = parent

        @property
        def custom_graphic(self):
            return self._parent._cast(_1743.CustomGraphic)

        @property
        def custom_report_definition_item(self):
            from mastapy.utility.report import _1751
            
            return self._parent._cast(_1751.CustomReportDefinitionItem)

        @property
        def custom_report_nameable_item(self):
            from mastapy.utility.report import _1762
            
            return self._parent._cast(_1762.CustomReportNameableItem)

        @property
        def custom_report_item(self):
            from mastapy.utility.report import _1754
            
            return self._parent._cast(_1754.CustomReportItem)

        @property
        def custom_drawing(self) -> 'CustomDrawing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomDrawing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def show_editor(self) -> 'bool':
        """bool: 'ShowEditor' is the original name of this property."""

        temp = self.wrapped.ShowEditor

        if temp is None:
            return False

        return temp

    @show_editor.setter
    def show_editor(self, value: 'bool'):
        self.wrapped.ShowEditor = bool(value) if value is not None else False

    @property
    def cast_to(self) -> 'CustomDrawing._Cast_CustomDrawing':
        return self._Cast_CustomDrawing(self)
