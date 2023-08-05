﻿"""_2490.py

RollingBearingFromCAD
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.part_model.import_from_cad import _2479
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_BEARING_FROM_CAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD', 'RollingBearingFromCAD')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingBearingFromCAD',)


class RollingBearingFromCAD(_2479.ConnectorFromCAD):
    """RollingBearingFromCAD

    This is a mastapy class.
    """

    TYPE = _ROLLING_BEARING_FROM_CAD

    class _Cast_RollingBearingFromCAD:
        """Special nested class for casting RollingBearingFromCAD to subclasses."""

        def __init__(self, parent: 'RollingBearingFromCAD'):
            self._parent = parent

        @property
        def connector_from_cad(self):
            return self._parent._cast(_2479.ConnectorFromCAD)

        @property
        def mountable_component_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2486
            
            return self._parent._cast(_2486.MountableComponentFromCAD)

        @property
        def component_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2477
            
            return self._parent._cast(_2477.ComponentFromCAD)

        @property
        def rolling_bearing_from_cad(self) -> 'RollingBearingFromCAD':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollingBearingFromCAD.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bore(self) -> 'float':
        """float: 'Bore' is the original name of this property."""

        temp = self.wrapped.Bore

        if temp is None:
            return 0.0

        return temp

    @bore.setter
    def bore(self, value: 'float'):
        self.wrapped.Bore = float(value) if value is not None else 0.0

    @property
    def outer_diameter(self) -> 'float':
        """float: 'OuterDiameter' is the original name of this property."""

        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return temp

    @outer_diameter.setter
    def outer_diameter(self, value: 'float'):
        self.wrapped.OuterDiameter = float(value) if value is not None else 0.0

    @property
    def width(self) -> 'float':
        """float: 'Width' is the original name of this property."""

        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    def width(self, value: 'float'):
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'RollingBearingFromCAD._Cast_RollingBearingFromCAD':
        return self._Cast_RollingBearingFromCAD(self)
