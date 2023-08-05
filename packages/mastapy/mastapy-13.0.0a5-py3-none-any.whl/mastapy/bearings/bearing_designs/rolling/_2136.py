"""_2136.py

CylindricalRollerBearing
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.bearings.bearing_designs.rolling import _2148
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_ROLLER_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'CylindricalRollerBearing')

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import _1929


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalRollerBearing',)


class CylindricalRollerBearing(_2148.NonBarrelRollerBearing):
    """CylindricalRollerBearing

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_ROLLER_BEARING

    class _Cast_CylindricalRollerBearing:
        """Special nested class for casting CylindricalRollerBearing to subclasses."""

        def __init__(self, parent: 'CylindricalRollerBearing'):
            self._parent = parent

        @property
        def non_barrel_roller_bearing(self):
            return self._parent._cast(_2148.NonBarrelRollerBearing)

        @property
        def roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2149
            
            return self._parent._cast(_2149.RollerBearing)

        @property
        def rolling_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2152
            
            return self._parent._cast(_2152.RollingBearing)

        @property
        def detailed_bearing(self):
            from mastapy.bearings.bearing_designs import _2118
            
            return self._parent._cast(_2118.DetailedBearing)

        @property
        def non_linear_bearing(self):
            from mastapy.bearings.bearing_designs import _2121
            
            return self._parent._cast(_2121.NonLinearBearing)

        @property
        def bearing_design(self):
            from mastapy.bearings.bearing_designs import _2117
            
            return self._parent._cast(_2117.BearingDesign)

        @property
        def needle_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2147
            
            return self._parent._cast(_2147.NeedleRollerBearing)

        @property
        def cylindrical_roller_bearing(self) -> 'CylindricalRollerBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalRollerBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_axial_load_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'AllowableAxialLoadFactor' is the original name of this property."""

        temp = self.wrapped.AllowableAxialLoadFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @allowable_axial_load_factor.setter
    def allowable_axial_load_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AllowableAxialLoadFactor = value

    @property
    def capacity_lubrication_factor_for_permissible_axial_load_grease(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CapacityLubricationFactorForPermissibleAxialLoadGrease' is the original name of this property."""

        temp = self.wrapped.CapacityLubricationFactorForPermissibleAxialLoadGrease

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @capacity_lubrication_factor_for_permissible_axial_load_grease.setter
    def capacity_lubrication_factor_for_permissible_axial_load_grease(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CapacityLubricationFactorForPermissibleAxialLoadGrease = value

    @property
    def capacity_lubrication_factor_for_permissible_axial_load_oil(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CapacityLubricationFactorForPermissibleAxialLoadOil' is the original name of this property."""

        temp = self.wrapped.CapacityLubricationFactorForPermissibleAxialLoadOil

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @capacity_lubrication_factor_for_permissible_axial_load_oil.setter
    def capacity_lubrication_factor_for_permissible_axial_load_oil(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CapacityLubricationFactorForPermissibleAxialLoadOil = value

    @property
    def diameter_exponent_factor_for_permissible_axial_load(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'DiameterExponentFactorForPermissibleAxialLoad' is the original name of this property."""

        temp = self.wrapped.DiameterExponentFactorForPermissibleAxialLoad

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @diameter_exponent_factor_for_permissible_axial_load.setter
    def diameter_exponent_factor_for_permissible_axial_load(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.DiameterExponentFactorForPermissibleAxialLoad = value

    @property
    def diameter_scaling_factor_for_permissible_axial_load(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'DiameterScalingFactorForPermissibleAxialLoad' is the original name of this property."""

        temp = self.wrapped.DiameterScalingFactorForPermissibleAxialLoad

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @diameter_scaling_factor_for_permissible_axial_load.setter
    def diameter_scaling_factor_for_permissible_axial_load(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.DiameterScalingFactorForPermissibleAxialLoad = value

    @property
    def permissible_axial_load_default_calculation_method(self) -> '_1929.CylindricalRollerMaxAxialLoadMethod':
        """CylindricalRollerMaxAxialLoadMethod: 'PermissibleAxialLoadDefaultCalculationMethod' is the original name of this property."""

        temp = self.wrapped.PermissibleAxialLoadDefaultCalculationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bearings.BearingResults.CylindricalRollerMaxAxialLoadMethod')
        return constructor.new_from_mastapy('mastapy.bearings.bearing_results._1929', 'CylindricalRollerMaxAxialLoadMethod')(value) if value is not None else None

    @permissible_axial_load_default_calculation_method.setter
    def permissible_axial_load_default_calculation_method(self, value: '_1929.CylindricalRollerMaxAxialLoadMethod'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Bearings.BearingResults.CylindricalRollerMaxAxialLoadMethod')
        self.wrapped.PermissibleAxialLoadDefaultCalculationMethod = value

    @property
    def permissible_axial_load_dimension_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'PermissibleAxialLoadDimensionFactor' is the original name of this property."""

        temp = self.wrapped.PermissibleAxialLoadDimensionFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @permissible_axial_load_dimension_factor.setter
    def permissible_axial_load_dimension_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.PermissibleAxialLoadDimensionFactor = value

    @property
    def permissible_axial_load_internal_dimension_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'PermissibleAxialLoadInternalDimensionFactor' is the original name of this property."""

        temp = self.wrapped.PermissibleAxialLoadInternalDimensionFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @permissible_axial_load_internal_dimension_factor.setter
    def permissible_axial_load_internal_dimension_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.PermissibleAxialLoadInternalDimensionFactor = value

    @property
    def radial_load_lubrication_factor_for_permissible_axial_load_grease(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RadialLoadLubricationFactorForPermissibleAxialLoadGrease' is the original name of this property."""

        temp = self.wrapped.RadialLoadLubricationFactorForPermissibleAxialLoadGrease

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @radial_load_lubrication_factor_for_permissible_axial_load_grease.setter
    def radial_load_lubrication_factor_for_permissible_axial_load_grease(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RadialLoadLubricationFactorForPermissibleAxialLoadGrease = value

    @property
    def radial_load_lubrication_factor_for_permissible_axial_load_oil(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RadialLoadLubricationFactorForPermissibleAxialLoadOil' is the original name of this property."""

        temp = self.wrapped.RadialLoadLubricationFactorForPermissibleAxialLoadOil

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @radial_load_lubrication_factor_for_permissible_axial_load_oil.setter
    def radial_load_lubrication_factor_for_permissible_axial_load_oil(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RadialLoadLubricationFactorForPermissibleAxialLoadOil = value

    @property
    def reference_rotation_speed(self) -> 'float':
        """float: 'ReferenceRotationSpeed' is the original name of this property."""

        temp = self.wrapped.ReferenceRotationSpeed

        if temp is None:
            return 0.0

        return temp

    @reference_rotation_speed.setter
    def reference_rotation_speed(self, value: 'float'):
        self.wrapped.ReferenceRotationSpeed = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'CylindricalRollerBearing._Cast_CylindricalRollerBearing':
        return self._Cast_CylindricalRollerBearing(self)
