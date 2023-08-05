﻿"""_807.py

PinionRoughMachineSetting
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PINION_ROUGH_MACHINE_SETTING = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'PinionRoughMachineSetting')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1152
    from mastapy.gears.manufacturing.bevel import _785


__docformat__ = 'restructuredtext en'
__all__ = ('PinionRoughMachineSetting',)


class PinionRoughMachineSetting(_0.APIBase):
    """PinionRoughMachineSetting

    This is a mastapy class.
    """

    TYPE = _PINION_ROUGH_MACHINE_SETTING

    class _Cast_PinionRoughMachineSetting:
        """Special nested class for casting PinionRoughMachineSetting to subclasses."""

        def __init__(self, parent: 'PinionRoughMachineSetting'):
            self._parent = parent

        @property
        def pinion_rough_machine_setting(self) -> 'PinionRoughMachineSetting':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PinionRoughMachineSetting.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def absolute_increment_in_machine_centre_to_back(self) -> 'float':
        """float: 'AbsoluteIncrementInMachineCentreToBack' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AbsoluteIncrementInMachineCentreToBack

        if temp is None:
            return 0.0

        return temp

    @property
    def blank_offset(self) -> 'float':
        """float: 'BlankOffset' is the original name of this property."""

        temp = self.wrapped.BlankOffset

        if temp is None:
            return 0.0

        return temp

    @blank_offset.setter
    def blank_offset(self, value: 'float'):
        self.wrapped.BlankOffset = float(value) if value is not None else 0.0

    @property
    def cone_distance_of_reference_point(self) -> 'float':
        """float: 'ConeDistanceOfReferencePoint' is the original name of this property."""

        temp = self.wrapped.ConeDistanceOfReferencePoint

        if temp is None:
            return 0.0

        return temp

    @cone_distance_of_reference_point.setter
    def cone_distance_of_reference_point(self, value: 'float'):
        self.wrapped.ConeDistanceOfReferencePoint = float(value) if value is not None else 0.0

    @property
    def height_of_reference_point(self) -> 'float':
        """float: 'HeightOfReferencePoint' is the original name of this property."""

        temp = self.wrapped.HeightOfReferencePoint

        if temp is None:
            return 0.0

        return temp

    @height_of_reference_point.setter
    def height_of_reference_point(self, value: 'float'):
        self.wrapped.HeightOfReferencePoint = float(value) if value is not None else 0.0

    @property
    def increment_of_pinion_workpiece_mounting_distance(self) -> 'float':
        """float: 'IncrementOfPinionWorkpieceMountingDistance' is the original name of this property."""

        temp = self.wrapped.IncrementOfPinionWorkpieceMountingDistance

        if temp is None:
            return 0.0

        return temp

    @increment_of_pinion_workpiece_mounting_distance.setter
    def increment_of_pinion_workpiece_mounting_distance(self, value: 'float'):
        self.wrapped.IncrementOfPinionWorkpieceMountingDistance = float(value) if value is not None else 0.0

    @property
    def minimum_allowed_finish_stock(self) -> 'float':
        """float: 'MinimumAllowedFinishStock' is the original name of this property."""

        temp = self.wrapped.MinimumAllowedFinishStock

        if temp is None:
            return 0.0

        return temp

    @minimum_allowed_finish_stock.setter
    def minimum_allowed_finish_stock(self, value: 'float'):
        self.wrapped.MinimumAllowedFinishStock = float(value) if value is not None else 0.0

    @property
    def spiral_angle_at_reference_point(self) -> 'float':
        """float: 'SpiralAngleAtReferencePoint' is the original name of this property."""

        temp = self.wrapped.SpiralAngleAtReferencePoint

        if temp is None:
            return 0.0

        return temp

    @spiral_angle_at_reference_point.setter
    def spiral_angle_at_reference_point(self, value: 'float'):
        self.wrapped.SpiralAngleAtReferencePoint = float(value) if value is not None else 0.0

    @property
    def gear_set(self) -> '_1152.ConicalGearSetDesign':
        """ConicalGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_config(self) -> '_785.ConicalPinionManufacturingConfig':
        """ConicalPinionManufacturingConfig: 'PinionConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionConfig

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PinionRoughMachineSetting._Cast_PinionRoughMachineSetting':
        return self._Cast_PinionRoughMachineSetting(self)
