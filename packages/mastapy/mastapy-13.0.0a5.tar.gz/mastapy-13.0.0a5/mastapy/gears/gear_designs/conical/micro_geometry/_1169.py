﻿"""_1169.py

ConicalGearFlankMicroGeometry
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.micro_geometry import _567
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_FLANK_MICRO_GEOMETRY = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Conical.MicroGeometry', 'ConicalGearFlankMicroGeometry')

if TYPE_CHECKING:
    from mastapy.gears import _334
    from mastapy.gears.gear_designs.conical.micro_geometry import _1168, _1170, _1171
    from mastapy.gears.gear_designs.conical import _1150


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearFlankMicroGeometry',)


class ConicalGearFlankMicroGeometry(_567.FlankMicroGeometry):
    """ConicalGearFlankMicroGeometry

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_FLANK_MICRO_GEOMETRY

    class _Cast_ConicalGearFlankMicroGeometry:
        """Special nested class for casting ConicalGearFlankMicroGeometry to subclasses."""

        def __init__(self, parent: 'ConicalGearFlankMicroGeometry'):
            self._parent = parent

        @property
        def flank_micro_geometry(self):
            return self._parent._cast(_567.FlankMicroGeometry)

        @property
        def conical_gear_flank_micro_geometry(self) -> 'ConicalGearFlankMicroGeometry':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearFlankMicroGeometry.TYPE'):
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
    def bias(self) -> '_1168.ConicalGearBiasModification':
        """ConicalGearBiasModification: 'Bias' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bias

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def lead_relief(self) -> '_1170.ConicalGearLeadModification':
        """ConicalGearLeadModification: 'LeadRelief' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadRelief

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_relief(self) -> '_1171.ConicalGearProfileModification':
        """ConicalGearProfileModification: 'ProfileRelief' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileRelief

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design(self) -> '_1150.ConicalGearDesign':
        """ConicalGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalGearFlankMicroGeometry._Cast_ConicalGearFlankMicroGeometry':
        return self._Cast_ConicalGearFlankMicroGeometry(self)
