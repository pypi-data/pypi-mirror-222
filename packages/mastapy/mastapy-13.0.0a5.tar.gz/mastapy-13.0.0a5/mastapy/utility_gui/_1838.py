"""_1838.py

DataLoggerWithCharts
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.math_utility.convergence import _1566
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA_LOGGER_WITH_CHARTS = python_net_import('SMT.MastaAPI.UtilityGUI', 'DataLoggerWithCharts')

if TYPE_CHECKING:
    from mastapy.utility_gui import _1837


__docformat__ = 'restructuredtext en'
__all__ = ('DataLoggerWithCharts',)


class DataLoggerWithCharts(_1566.DataLogger):
    """DataLoggerWithCharts

    This is a mastapy class.
    """

    TYPE = _DATA_LOGGER_WITH_CHARTS

    class _Cast_DataLoggerWithCharts:
        """Special nested class for casting DataLoggerWithCharts to subclasses."""

        def __init__(self, parent: 'DataLoggerWithCharts'):
            self._parent = parent

        @property
        def data_logger(self):
            return self._parent._cast(_1566.DataLogger)

        @property
        def data_logger_with_charts(self) -> 'DataLoggerWithCharts':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DataLoggerWithCharts.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def logged_items(self) -> 'List[_1837.DataLoggerItem]':
        """List[DataLoggerItem]: 'LoggedItems' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoggedItems

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'DataLoggerWithCharts._Cast_DataLoggerWithCharts':
        return self._Cast_DataLoggerWithCharts(self)
