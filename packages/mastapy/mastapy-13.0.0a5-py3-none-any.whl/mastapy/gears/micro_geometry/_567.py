﻿"""_567.py

FlankMicroGeometry
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from PIL.Image import Image

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLANK_MICRO_GEOMETRY = python_net_import('SMT.MastaAPI.Gears.MicroGeometry', 'FlankMicroGeometry')

if TYPE_CHECKING:
    from mastapy.gears import _334
    from mastapy.gears.gear_designs import _944
    from mastapy.utility.scripting import _1732


__docformat__ = 'restructuredtext en'
__all__ = ('FlankMicroGeometry',)


class FlankMicroGeometry(_0.APIBase):
    """FlankMicroGeometry

    This is a mastapy class.
    """

    TYPE = _FLANK_MICRO_GEOMETRY

    class _Cast_FlankMicroGeometry:
        """Special nested class for casting FlankMicroGeometry to subclasses."""

        def __init__(self, parent: 'FlankMicroGeometry'):
            self._parent = parent

        @property
        def cylindrical_gear_flank_micro_geometry(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1091
            
            return self._parent._cast(_1091.CylindricalGearFlankMicroGeometry)

        @property
        def conical_gear_flank_micro_geometry(self):
            from mastapy.gears.gear_designs.conical.micro_geometry import _1169
            
            return self._parent._cast(_1169.ConicalGearFlankMicroGeometry)

        @property
        def flank_micro_geometry(self) -> 'FlankMicroGeometry':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FlankMicroGeometry.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def micro_geometry_input_type(self) -> '_334.MicroGeometryInputTypes':
        """MicroGeometryInputTypes: 'MicroGeometryInputType' is the original name of this property."""

        temp = self.wrapped.MicroGeometryInputType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.MicroGeometryInputTypes')
        return constructor.new_from_mastapy('mastapy.gears._334', 'MicroGeometryInputTypes')(value) if value is not None else None

    @micro_geometry_input_type.setter
    def micro_geometry_input_type(self, value: '_334.MicroGeometryInputTypes'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.MicroGeometryInputTypes')
        self.wrapped.MicroGeometryInputType = value

    @property
    def modification_chart(self) -> 'Image':
        """Image: 'ModificationChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModificationChart

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def gear_design(self) -> '_944.GearDesign':
        """GearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def user_specified_data(self) -> '_1732.UserSpecifiedData':
        """UserSpecifiedData: 'UserSpecifiedData' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UserSpecifiedData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'FlankMicroGeometry._Cast_FlankMicroGeometry':
        return self._Cast_FlankMicroGeometry(self)
