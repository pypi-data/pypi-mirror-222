﻿"""_706.py

CylindricalGearHobDesign
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.manufacturing.cylindrical.cutters import _709
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_HOB_DESIGN = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'CylindricalGearHobDesign')

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _628
    from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _722, _727


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearHobDesign',)


class CylindricalGearHobDesign(_709.CylindricalGearRackDesign):
    """CylindricalGearHobDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_HOB_DESIGN

    class _Cast_CylindricalGearHobDesign:
        """Special nested class for casting CylindricalGearHobDesign to subclasses."""

        def __init__(self, parent: 'CylindricalGearHobDesign'):
            self._parent = parent

        @property
        def cylindrical_gear_rack_design(self):
            return self._parent._cast(_709.CylindricalGearRackDesign)

        @property
        def cylindrical_gear_real_cutter_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _710
            
            return self._parent._cast(_710.CylindricalGearRealCutterDesign)

        @property
        def cylindrical_gear_abstract_cutter_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _703
            
            return self._parent._cast(_703.CylindricalGearAbstractCutterDesign)

        @property
        def named_database_item(self):
            from mastapy.utility.databases import _1818
            
            return self._parent._cast(_1818.NamedDatabaseItem)

        @property
        def cylindrical_gear_hob_design(self) -> 'CylindricalGearHobDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearHobDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def addendum_tolerance(self) -> 'float':
        """float: 'AddendumTolerance' is the original name of this property."""

        temp = self.wrapped.AddendumTolerance

        if temp is None:
            return 0.0

        return temp

    @addendum_tolerance.setter
    def addendum_tolerance(self, value: 'float'):
        self.wrapped.AddendumTolerance = float(value) if value is not None else 0.0

    @property
    def blade_control_distance(self) -> 'float':
        """float: 'BladeControlDistance' is the original name of this property."""

        temp = self.wrapped.BladeControlDistance

        if temp is None:
            return 0.0

        return temp

    @blade_control_distance.setter
    def blade_control_distance(self, value: 'float'):
        self.wrapped.BladeControlDistance = float(value) if value is not None else 0.0

    @property
    def blade_relief(self) -> 'float':
        """float: 'BladeRelief' is the original name of this property."""

        temp = self.wrapped.BladeRelief

        if temp is None:
            return 0.0

        return temp

    @blade_relief.setter
    def blade_relief(self, value: 'float'):
        self.wrapped.BladeRelief = float(value) if value is not None else 0.0

    @property
    def edge_height(self) -> 'float':
        """float: 'EdgeHeight' is the original name of this property."""

        temp = self.wrapped.EdgeHeight

        if temp is None:
            return 0.0

        return temp

    @edge_height.setter
    def edge_height(self, value: 'float'):
        self.wrapped.EdgeHeight = float(value) if value is not None else 0.0

    @property
    def edge_radius_tolerance(self) -> 'float':
        """float: 'EdgeRadiusTolerance' is the original name of this property."""

        temp = self.wrapped.EdgeRadiusTolerance

        if temp is None:
            return 0.0

        return temp

    @edge_radius_tolerance.setter
    def edge_radius_tolerance(self, value: 'float'):
        self.wrapped.EdgeRadiusTolerance = float(value) if value is not None else 0.0

    @property
    def flat_tip_width(self) -> 'float':
        """float: 'FlatTipWidth' is the original name of this property."""

        temp = self.wrapped.FlatTipWidth

        if temp is None:
            return 0.0

        return temp

    @flat_tip_width.setter
    def flat_tip_width(self, value: 'float'):
        self.wrapped.FlatTipWidth = float(value) if value is not None else 0.0

    @property
    def has_protuberance(self) -> 'bool':
        """bool: 'HasProtuberance' is the original name of this property."""

        temp = self.wrapped.HasProtuberance

        if temp is None:
            return False

        return temp

    @has_protuberance.setter
    def has_protuberance(self, value: 'bool'):
        self.wrapped.HasProtuberance = bool(value) if value is not None else False

    @property
    def has_semi_topping_blade(self) -> 'bool':
        """bool: 'HasSemiToppingBlade' is the original name of this property."""

        temp = self.wrapped.HasSemiToppingBlade

        if temp is None:
            return False

        return temp

    @has_semi_topping_blade.setter
    def has_semi_topping_blade(self, value: 'bool'):
        self.wrapped.HasSemiToppingBlade = bool(value) if value is not None else False

    @property
    def hob_edge_type(self) -> '_628.HobEdgeTypes':
        """HobEdgeTypes: 'HobEdgeType' is the original name of this property."""

        temp = self.wrapped.HobEdgeType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobEdgeTypes')
        return constructor.new_from_mastapy('mastapy.gears.manufacturing.cylindrical._628', 'HobEdgeTypes')(value) if value is not None else None

    @hob_edge_type.setter
    def hob_edge_type(self, value: '_628.HobEdgeTypes'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobEdgeTypes')
        self.wrapped.HobEdgeType = value

    @property
    def normal_thickness_tolerance(self) -> 'float':
        """float: 'NormalThicknessTolerance' is the original name of this property."""

        temp = self.wrapped.NormalThicknessTolerance

        if temp is None:
            return 0.0

        return temp

    @normal_thickness_tolerance.setter
    def normal_thickness_tolerance(self, value: 'float'):
        self.wrapped.NormalThicknessTolerance = float(value) if value is not None else 0.0

    @property
    def number_of_gashes(self) -> 'int':
        """int: 'NumberOfGashes' is the original name of this property."""

        temp = self.wrapped.NumberOfGashes

        if temp is None:
            return 0

        return temp

    @number_of_gashes.setter
    def number_of_gashes(self, value: 'int'):
        self.wrapped.NumberOfGashes = int(value) if value is not None else 0

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
    def protuberance_angle(self) -> 'float':
        """float: 'ProtuberanceAngle' is the original name of this property."""

        temp = self.wrapped.ProtuberanceAngle

        if temp is None:
            return 0.0

        return temp

    @protuberance_angle.setter
    def protuberance_angle(self, value: 'float'):
        self.wrapped.ProtuberanceAngle = float(value) if value is not None else 0.0

    @property
    def protuberance_factor(self) -> 'float':
        """float: 'ProtuberanceFactor' is the original name of this property."""

        temp = self.wrapped.ProtuberanceFactor

        if temp is None:
            return 0.0

        return temp

    @protuberance_factor.setter
    def protuberance_factor(self, value: 'float'):
        self.wrapped.ProtuberanceFactor = float(value) if value is not None else 0.0

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
    def protuberance_height_relative_to_edge_height(self) -> 'float':
        """float: 'ProtuberanceHeightRelativeToEdgeHeight' is the original name of this property."""

        temp = self.wrapped.ProtuberanceHeightRelativeToEdgeHeight

        if temp is None:
            return 0.0

        return temp

    @protuberance_height_relative_to_edge_height.setter
    def protuberance_height_relative_to_edge_height(self, value: 'float'):
        self.wrapped.ProtuberanceHeightRelativeToEdgeHeight = float(value) if value is not None else 0.0

    @property
    def protuberance_height_tolerance(self) -> 'float':
        """float: 'ProtuberanceHeightTolerance' is the original name of this property."""

        temp = self.wrapped.ProtuberanceHeightTolerance

        if temp is None:
            return 0.0

        return temp

    @protuberance_height_tolerance.setter
    def protuberance_height_tolerance(self, value: 'float'):
        self.wrapped.ProtuberanceHeightTolerance = float(value) if value is not None else 0.0

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
    def protuberance_tolerance(self) -> 'float':
        """float: 'ProtuberanceTolerance' is the original name of this property."""

        temp = self.wrapped.ProtuberanceTolerance

        if temp is None:
            return 0.0

        return temp

    @protuberance_tolerance.setter
    def protuberance_tolerance(self, value: 'float'):
        self.wrapped.ProtuberanceTolerance = float(value) if value is not None else 0.0

    @property
    def semi_topping_blade_height_tolerance(self) -> 'float':
        """float: 'SemiToppingBladeHeightTolerance' is the original name of this property."""

        temp = self.wrapped.SemiToppingBladeHeightTolerance

        if temp is None:
            return 0.0

        return temp

    @semi_topping_blade_height_tolerance.setter
    def semi_topping_blade_height_tolerance(self, value: 'float'):
        self.wrapped.SemiToppingBladeHeightTolerance = float(value) if value is not None else 0.0

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
    def semi_topping_pressure_angle_tolerance(self) -> 'float':
        """float: 'SemiToppingPressureAngleTolerance' is the original name of this property."""

        temp = self.wrapped.SemiToppingPressureAngleTolerance

        if temp is None:
            return 0.0

        return temp

    @semi_topping_pressure_angle_tolerance.setter
    def semi_topping_pressure_angle_tolerance(self, value: 'float'):
        self.wrapped.SemiToppingPressureAngleTolerance = float(value) if value is not None else 0.0

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
    def tip_control_distance(self) -> 'float':
        """float: 'TipControlDistance' is the original name of this property."""

        temp = self.wrapped.TipControlDistance

        if temp is None:
            return 0.0

        return temp

    @tip_control_distance.setter
    def tip_control_distance(self, value: 'float'):
        self.wrapped.TipControlDistance = float(value) if value is not None else 0.0

    @property
    def maximum_hob_material_shape(self) -> '_722.CylindricalGearHobShape':
        """CylindricalGearHobShape: 'MaximumHobMaterialShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumHobMaterialShape

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def minimum_hob_material_shape(self) -> '_722.CylindricalGearHobShape':
        """CylindricalGearHobShape: 'MinimumHobMaterialShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumHobMaterialShape

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def nominal_hob_shape(self) -> '_722.CylindricalGearHobShape':
        """CylindricalGearHobShape: 'NominalHobShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalHobShape

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def nominal_rack_shape(self) -> '_727.RackShape':
        """RackShape: 'NominalRackShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalRackShape

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalGearHobDesign._Cast_CylindricalGearHobDesign':
        return self._Cast_CylindricalGearHobDesign(self)
