"""_1744.py

CustomImage
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.report import _1743
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_IMAGE = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomImage')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomImage',)


class CustomImage(_1743.CustomGraphic):
    """CustomImage

    This is a mastapy class.
    """

    TYPE = _CUSTOM_IMAGE

    class _Cast_CustomImage:
        """Special nested class for casting CustomImage to subclasses."""

        def __init__(self, parent: 'CustomImage'):
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
        def loaded_bearing_chart_reporter(self):
            from mastapy.bearings.bearing_results import _1934
            
            return self._parent._cast(_1934.LoadedBearingChartReporter)

        @property
        def custom_image(self) -> 'CustomImage':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomImage.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CustomImage._Cast_CustomImage':
        return self._Cast_CustomImage(self)
