﻿"""_727.py

RackShape
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _720
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RACK_SHAPE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters.Tangibles', 'RackShape')

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters import _709


__docformat__ = 'restructuredtext en'
__all__ = ('RackShape',)


class RackShape(_720.CutterShapeDefinition):
    """RackShape

    This is a mastapy class.
    """

    TYPE = _RACK_SHAPE

    class _Cast_RackShape:
        """Special nested class for casting RackShape to subclasses."""

        def __init__(self, parent: 'RackShape'):
            self._parent = parent

        @property
        def cutter_shape_definition(self):
            return self._parent._cast(_720.CutterShapeDefinition)

        @property
        def cylindrical_gear_hob_shape(self):
            from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _722
            
            return self._parent._cast(_722.CylindricalGearHobShape)

        @property
        def cylindrical_gear_worm_grinder_shape(self):
            from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _725
            
            return self._parent._cast(_725.CylindricalGearWormGrinderShape)

        @property
        def rack_shape(self) -> 'RackShape':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RackShape.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def actual_protuberance(self) -> 'float':
        """float: 'ActualProtuberance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActualProtuberance

        if temp is None:
            return 0.0

        return temp

    @property
    def addendum(self) -> 'float':
        """float: 'Addendum' is the original name of this property."""

        temp = self.wrapped.Addendum

        if temp is None:
            return 0.0

        return temp

    @addendum.setter
    def addendum(self, value: 'float'):
        self.wrapped.Addendum = float(value) if value is not None else 0.0

    @property
    def addendum_form(self) -> 'float':
        """float: 'AddendumForm' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AddendumForm

        if temp is None:
            return 0.0

        return temp

    @property
    def dedendum(self) -> 'float':
        """float: 'Dedendum' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Dedendum

        if temp is None:
            return 0.0

        return temp

    @property
    def edge_height(self) -> 'float':
        """float: 'EdgeHeight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EdgeHeight

        if temp is None:
            return 0.0

        return temp

    @property
    def edge_radius(self) -> 'float':
        """float: 'EdgeRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EdgeRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def flat_root_width(self) -> 'float':
        """float: 'FlatRootWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlatRootWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def flat_tip_width(self) -> 'float':
        """float: 'FlatTipWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlatTipWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def has_semi_topping_blade(self) -> 'bool':
        """bool: 'HasSemiToppingBlade' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HasSemiToppingBlade

        if temp is None:
            return False

        return temp

    @property
    def hob_whole_depth(self) -> 'float':
        """float: 'HobWholeDepth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HobWholeDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def main_blade_pressure_angle_nearest_hob_root(self) -> 'float':
        """float: 'MainBladePressureAngleNearestHobRoot' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MainBladePressureAngleNearestHobRoot

        if temp is None:
            return 0.0

        return temp

    @property
    def main_blade_pressure_angle_nearest_hob_tip(self) -> 'float':
        """float: 'MainBladePressureAngleNearestHobTip' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MainBladePressureAngleNearestHobTip

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_edge_radius(self) -> 'float':
        """float: 'MaximumEdgeRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumEdgeRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_protuberance_blade_pressure_angle(self) -> 'float':
        """float: 'MaximumProtuberanceBladePressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumProtuberanceBladePressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_protuberance_blade_pressure_angle(self) -> 'float':
        """float: 'MinimumProtuberanceBladePressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumProtuberanceBladePressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_protuberance_height(self) -> 'float':
        """float: 'MinimumProtuberanceHeight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumProtuberanceHeight

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_thickness(self) -> 'float':
        """float: 'NormalThickness' is the original name of this property."""

        temp = self.wrapped.NormalThickness

        if temp is None:
            return 0.0

        return temp

    @normal_thickness.setter
    def normal_thickness(self, value: 'float'):
        self.wrapped.NormalThickness = float(value) if value is not None else 0.0

    @property
    def protuberance(self) -> 'float':
        """float: 'Protuberance' is the original name of this property."""

        temp = self.wrapped.Protuberance

        if temp is None:
            return 0.0

        return temp

    @protuberance.setter
    def protuberance(self, value: 'float'):
        self.wrapped.Protuberance = float(value) if value is not None else 0.0

    @property
    def protuberance_height(self) -> 'float':
        """float: 'ProtuberanceHeight' is the original name of this property."""

        temp = self.wrapped.ProtuberanceHeight

        if temp is None:
            return 0.0

        return temp

    @protuberance_height.setter
    def protuberance_height(self, value: 'float'):
        self.wrapped.ProtuberanceHeight = float(value) if value is not None else 0.0

    @property
    def protuberance_length(self) -> 'float':
        """float: 'ProtuberanceLength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProtuberanceLength

        if temp is None:
            return 0.0

        return temp

    @property
    def protuberance_pressure_angle(self) -> 'float':
        """float: 'ProtuberancePressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProtuberancePressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def protuberance_relative_to_main_blade_pressure_angle_nearest_hob_tip(self) -> 'float':
        """float: 'ProtuberanceRelativeToMainBladePressureAngleNearestHobTip' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProtuberanceRelativeToMainBladePressureAngleNearestHobTip

        if temp is None:
            return 0.0

        return temp

    @property
    def semi_topping_height(self) -> 'float':
        """float: 'SemiToppingHeight' is the original name of this property."""

        temp = self.wrapped.SemiToppingHeight

        if temp is None:
            return 0.0

        return temp

    @semi_topping_height.setter
    def semi_topping_height(self, value: 'float'):
        self.wrapped.SemiToppingHeight = float(value) if value is not None else 0.0

    @property
    def semi_topping_pressure_angle(self) -> 'float':
        """float: 'SemiToppingPressureAngle' is the original name of this property."""

        temp = self.wrapped.SemiToppingPressureAngle

        if temp is None:
            return 0.0

        return temp

    @semi_topping_pressure_angle.setter
    def semi_topping_pressure_angle(self, value: 'float'):
        self.wrapped.SemiToppingPressureAngle = float(value) if value is not None else 0.0

    @property
    def semi_topping_start(self) -> 'float':
        """float: 'SemiToppingStart' is the original name of this property."""

        temp = self.wrapped.SemiToppingStart

        if temp is None:
            return 0.0

        return temp

    @semi_topping_start.setter
    def semi_topping_start(self, value: 'float'):
        self.wrapped.SemiToppingStart = float(value) if value is not None else 0.0

    @property
    def design(self) -> '_709.CylindricalGearRackDesign':
        """CylindricalGearRackDesign: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'RackShape._Cast_RackShape':
        return self._Cast_RackShape(self)
