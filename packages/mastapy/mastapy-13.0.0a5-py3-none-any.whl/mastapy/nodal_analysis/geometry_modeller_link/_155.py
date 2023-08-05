﻿"""_155.py

GeometryModellerDesignInformation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEOMETRY_MODELLER_DESIGN_INFORMATION = python_net_import('SMT.MastaAPI.NodalAnalysis.GeometryModellerLink', 'GeometryModellerDesignInformation')


__docformat__ = 'restructuredtext en'
__all__ = ('GeometryModellerDesignInformation',)


class GeometryModellerDesignInformation(_0.APIBase):
    """GeometryModellerDesignInformation

    This is a mastapy class.
    """

    TYPE = _GEOMETRY_MODELLER_DESIGN_INFORMATION

    class _Cast_GeometryModellerDesignInformation:
        """Special nested class for casting GeometryModellerDesignInformation to subclasses."""

        def __init__(self, parent: 'GeometryModellerDesignInformation'):
            self._parent = parent

        @property
        def geometry_modeller_design_information(self) -> 'GeometryModellerDesignInformation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GeometryModellerDesignInformation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def file_name(self) -> 'str':
        """str: 'FileName' is the original name of this property."""

        temp = self.wrapped.FileName

        if temp is None:
            return ''

        return temp

    @file_name.setter
    def file_name(self, value: 'str'):
        self.wrapped.FileName = str(value) if value is not None else ''

    @property
    def tab_name(self) -> 'str':
        """str: 'TabName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TabName

        if temp is None:
            return ''

        return temp

    @property
    def main_part_moniker(self) -> 'str':
        """str: 'MainPartMoniker' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MainPartMoniker

        if temp is None:
            return ''

        return temp

    @property
    def cast_to(self) -> 'GeometryModellerDesignInformation._Cast_GeometryModellerDesignInformation':
        return self._Cast_GeometryModellerDesignInformation(self)
