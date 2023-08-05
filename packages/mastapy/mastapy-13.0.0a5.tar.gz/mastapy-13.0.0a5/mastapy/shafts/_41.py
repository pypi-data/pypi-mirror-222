﻿"""_41.py

ShaftSurfaceFinishSection
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.shafts import _21
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SURFACE_FINISH_SECTION = python_net_import('SMT.MastaAPI.Shafts', 'ShaftSurfaceFinishSection')

if TYPE_CHECKING:
    from mastapy.shafts import _42


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftSurfaceFinishSection',)


class ShaftSurfaceFinishSection(_21.ShaftFeature):
    """ShaftSurfaceFinishSection

    This is a mastapy class.
    """

    TYPE = _SHAFT_SURFACE_FINISH_SECTION

    class _Cast_ShaftSurfaceFinishSection:
        """Special nested class for casting ShaftSurfaceFinishSection to subclasses."""

        def __init__(self, parent: 'ShaftSurfaceFinishSection'):
            self._parent = parent

        @property
        def shaft_feature(self):
            return self._parent._cast(_21.ShaftFeature)

        @property
        def shaft_surface_finish_section(self) -> 'ShaftSurfaceFinishSection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftSurfaceFinishSection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length(self) -> 'float':
        """float: 'Length' is the original name of this property."""

        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    def length(self, value: 'float'):
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def surface_roughness(self) -> '_42.ShaftSurfaceRoughness':
        """ShaftSurfaceRoughness: 'SurfaceRoughness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SurfaceRoughness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def add_new_surface_finish_section(self):
        """ 'AddNewSurfaceFinishSection' is the original name of this method."""

        self.wrapped.AddNewSurfaceFinishSection()

    @property
    def cast_to(self) -> 'ShaftSurfaceFinishSection._Cast_ShaftSurfaceFinishSection':
        return self._Cast_ShaftSurfaceFinishSection(self)
