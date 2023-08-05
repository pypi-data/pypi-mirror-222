﻿"""_1085.py

FinishStockSpecification
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.gear_designs.cylindrical import _1064
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FINISH_STOCK_SPECIFICATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ThicknessStockAndBacklash', 'FinishStockSpecification')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import _1086
    from mastapy.gears.gear_designs.cylindrical import _1079


__docformat__ = 'restructuredtext en'
__all__ = ('FinishStockSpecification',)


class FinishStockSpecification(_1064.RelativeValuesSpecification['FinishStockSpecification']):
    """FinishStockSpecification

    This is a mastapy class.
    """

    TYPE = _FINISH_STOCK_SPECIFICATION

    class _Cast_FinishStockSpecification:
        """Special nested class for casting FinishStockSpecification to subclasses."""

        def __init__(self, parent: 'FinishStockSpecification'):
            self._parent = parent

        @property
        def relative_values_specification(self):
            from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import _1085
            
            return self._parent._cast(_1064.RelativeValuesSpecification)

        @property
        def finish_stock_specification(self) -> 'FinishStockSpecification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FinishStockSpecification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def finish_stock_rough_thickness_specification_method(self) -> '_1086.FinishStockType':
        """FinishStockType: 'FinishStockRoughThicknessSpecificationMethod' is the original name of this property."""

        temp = self.wrapped.FinishStockRoughThicknessSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ThicknessStockAndBacklash.FinishStockType')
        return constructor.new_from_mastapy('mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash._1086', 'FinishStockType')(value) if value is not None else None

    @finish_stock_rough_thickness_specification_method.setter
    def finish_stock_rough_thickness_specification_method(self, value: '_1086.FinishStockType'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ThicknessStockAndBacklash.FinishStockType')
        self.wrapped.FinishStockRoughThicknessSpecificationMethod = value

    @property
    def normal(self) -> '_1079.TolerancedValueSpecification[FinishStockSpecification]':
        """TolerancedValueSpecification[FinishStockSpecification]: 'Normal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Normal

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[FinishStockSpecification](temp) if temp is not None else None

    @property
    def tangent_to_reference_circle(self) -> '_1079.TolerancedValueSpecification[FinishStockSpecification]':
        """TolerancedValueSpecification[FinishStockSpecification]: 'TangentToReferenceCircle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TangentToReferenceCircle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[FinishStockSpecification](temp) if temp is not None else None

    @property
    def cast_to(self) -> 'FinishStockSpecification._Cast_FinishStockSpecification':
        return self._Cast_FinishStockSpecification(self)
