﻿"""_2152.py

RollingBearing
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.bearings.bearing_designs import _2118
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_ROLLING_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'RollingBearing')

if TYPE_CHECKING:
    from mastapy.bearings import (
        _1879, _1857, _1858, _1859,
        _1856, _1882
    )
    from mastapy.bearings.bearing_designs.rolling import (
        _2134, _2138, _2139, _2145,
        _2155, _2133, _2162, _2142,
        _2130, _2154
    )
    from mastapy.materials import _243
    from mastapy.utility import _1573
    from mastapy.bearings.bearing_results.rolling import _1964


__docformat__ = 'restructuredtext en'
__all__ = ('RollingBearing',)


class RollingBearing(_2118.DetailedBearing):
    """RollingBearing

    This is a mastapy class.
    """

    TYPE = _ROLLING_BEARING

    class _Cast_RollingBearing:
        """Special nested class for casting RollingBearing to subclasses."""

        def __init__(self, parent: 'RollingBearing'):
            self._parent = parent

        @property
        def detailed_bearing(self):
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
        def angular_contact_ball_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2122
            
            return self._parent._cast(_2122.AngularContactBallBearing)

        @property
        def angular_contact_thrust_ball_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2123
            
            return self._parent._cast(_2123.AngularContactThrustBallBearing)

        @property
        def asymmetric_spherical_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2124
            
            return self._parent._cast(_2124.AsymmetricSphericalRollerBearing)

        @property
        def axial_thrust_cylindrical_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2125
            
            return self._parent._cast(_2125.AxialThrustCylindricalRollerBearing)

        @property
        def axial_thrust_needle_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2126
            
            return self._parent._cast(_2126.AxialThrustNeedleRollerBearing)

        @property
        def ball_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2127
            
            return self._parent._cast(_2127.BallBearing)

        @property
        def barrel_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2129
            
            return self._parent._cast(_2129.BarrelRollerBearing)

        @property
        def crossed_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2135
            
            return self._parent._cast(_2135.CrossedRollerBearing)

        @property
        def cylindrical_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2136
            
            return self._parent._cast(_2136.CylindricalRollerBearing)

        @property
        def deep_groove_ball_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2137
            
            return self._parent._cast(_2137.DeepGrooveBallBearing)

        @property
        def four_point_contact_ball_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2141
            
            return self._parent._cast(_2141.FourPointContactBallBearing)

        @property
        def multi_point_contact_ball_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2146
            
            return self._parent._cast(_2146.MultiPointContactBallBearing)

        @property
        def needle_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2147
            
            return self._parent._cast(_2147.NeedleRollerBearing)

        @property
        def non_barrel_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2148
            
            return self._parent._cast(_2148.NonBarrelRollerBearing)

        @property
        def roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2149
            
            return self._parent._cast(_2149.RollerBearing)

        @property
        def self_aligning_ball_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2153
            
            return self._parent._cast(_2153.SelfAligningBallBearing)

        @property
        def spherical_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2156
            
            return self._parent._cast(_2156.SphericalRollerBearing)

        @property
        def spherical_roller_thrust_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2157
            
            return self._parent._cast(_2157.SphericalRollerThrustBearing)

        @property
        def taper_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2158
            
            return self._parent._cast(_2158.TaperRollerBearing)

        @property
        def three_point_contact_ball_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2159
            
            return self._parent._cast(_2159.ThreePointContactBallBearing)

        @property
        def thrust_ball_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2160
            
            return self._parent._cast(_2160.ThrustBallBearing)

        @property
        def toroidal_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2161
            
            return self._parent._cast(_2161.ToroidalRollerBearing)

        @property
        def rolling_bearing(self) -> 'RollingBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollingBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def are_the_inner_rings_a_single_piece_of_metal(self) -> 'overridable.Overridable_bool':
        """overridable.Overridable_bool: 'AreTheInnerRingsASinglePieceOfMetal' is the original name of this property."""

        temp = self.wrapped.AreTheInnerRingsASinglePieceOfMetal

        if temp is None:
            return False

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_bool')(temp) if temp is not None else False

    @are_the_inner_rings_a_single_piece_of_metal.setter
    def are_the_inner_rings_a_single_piece_of_metal(self, value: 'overridable.Overridable_bool.implicit_type()'):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else False, is_overridden)
        self.wrapped.AreTheInnerRingsASinglePieceOfMetal = value

    @property
    def are_the_outer_rings_a_single_piece_of_metal(self) -> 'overridable.Overridable_bool':
        """overridable.Overridable_bool: 'AreTheOuterRingsASinglePieceOfMetal' is the original name of this property."""

        temp = self.wrapped.AreTheOuterRingsASinglePieceOfMetal

        if temp is None:
            return False

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_bool')(temp) if temp is not None else False

    @are_the_outer_rings_a_single_piece_of_metal.setter
    def are_the_outer_rings_a_single_piece_of_metal(self, value: 'overridable.Overridable_bool.implicit_type()'):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else False, is_overridden)
        self.wrapped.AreTheOuterRingsASinglePieceOfMetal = value

    @property
    def arrangement(self) -> 'enum_with_selected_value.EnumWithSelectedValue_RollingBearingArrangement':
        """enum_with_selected_value.EnumWithSelectedValue_RollingBearingArrangement: 'Arrangement' is the original name of this property."""

        temp = self.wrapped.Arrangement

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_RollingBearingArrangement.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @arrangement.setter
    def arrangement(self, value: 'enum_with_selected_value.EnumWithSelectedValue_RollingBearingArrangement.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_RollingBearingArrangement.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.Arrangement = value

    @property
    def basic_dynamic_load_rating(self) -> 'float':
        """float: 'BasicDynamicLoadRating' is the original name of this property."""

        temp = self.wrapped.BasicDynamicLoadRating

        if temp is None:
            return 0.0

        return temp

    @basic_dynamic_load_rating.setter
    def basic_dynamic_load_rating(self, value: 'float'):
        self.wrapped.BasicDynamicLoadRating = float(value) if value is not None else 0.0

    @property
    def basic_dynamic_load_rating_calculation(self) -> 'enum_with_selected_value.EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod':
        """enum_with_selected_value.EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod: 'BasicDynamicLoadRatingCalculation' is the original name of this property."""

        temp = self.wrapped.BasicDynamicLoadRatingCalculation

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @basic_dynamic_load_rating_calculation.setter
    def basic_dynamic_load_rating_calculation(self, value: 'enum_with_selected_value.EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.BasicDynamicLoadRatingCalculation = value

    @property
    def basic_dynamic_load_rating_divided_by_correction_factors(self) -> 'float':
        """float: 'BasicDynamicLoadRatingDividedByCorrectionFactors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicDynamicLoadRatingDividedByCorrectionFactors

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_dynamic_load_rating_source(self) -> 'str':
        """str: 'BasicDynamicLoadRatingSource' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicDynamicLoadRatingSource

        if temp is None:
            return ''

        return temp

    @property
    def basic_static_load_rating(self) -> 'float':
        """float: 'BasicStaticLoadRating' is the original name of this property."""

        temp = self.wrapped.BasicStaticLoadRating

        if temp is None:
            return 0.0

        return temp

    @basic_static_load_rating.setter
    def basic_static_load_rating(self, value: 'float'):
        self.wrapped.BasicStaticLoadRating = float(value) if value is not None else 0.0

    @property
    def basic_static_load_rating_calculation(self) -> 'enum_with_selected_value.EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod':
        """enum_with_selected_value.EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod: 'BasicStaticLoadRatingCalculation' is the original name of this property."""

        temp = self.wrapped.BasicStaticLoadRatingCalculation

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @basic_static_load_rating_calculation.setter
    def basic_static_load_rating_calculation(self, value: 'enum_with_selected_value.EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.BasicStaticLoadRatingCalculation = value

    @property
    def basic_static_load_rating_factor(self) -> 'float':
        """float: 'BasicStaticLoadRatingFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicStaticLoadRatingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_static_load_rating_source(self) -> 'str':
        """str: 'BasicStaticLoadRatingSource' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicStaticLoadRatingSource

        if temp is None:
            return ''

        return temp

    @property
    def cage_bridge_angle(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CageBridgeAngle' is the original name of this property."""

        temp = self.wrapped.CageBridgeAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @cage_bridge_angle.setter
    def cage_bridge_angle(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CageBridgeAngle = value

    @property
    def cage_bridge_axial_surface_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CageBridgeAxialSurfaceRadius' is the original name of this property."""

        temp = self.wrapped.CageBridgeAxialSurfaceRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @cage_bridge_axial_surface_radius.setter
    def cage_bridge_axial_surface_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CageBridgeAxialSurfaceRadius = value

    @property
    def cage_bridge_radial_surface_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CageBridgeRadialSurfaceRadius' is the original name of this property."""

        temp = self.wrapped.CageBridgeRadialSurfaceRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @cage_bridge_radial_surface_radius.setter
    def cage_bridge_radial_surface_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CageBridgeRadialSurfaceRadius = value

    @property
    def cage_bridge_shape(self) -> '_2134.CageBridgeShape':
        """CageBridgeShape: 'CageBridgeShape' is the original name of this property."""

        temp = self.wrapped.CageBridgeShape

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bearings.BearingDesigns.Rolling.CageBridgeShape')
        return constructor.new_from_mastapy('mastapy.bearings.bearing_designs.rolling._2134', 'CageBridgeShape')(value) if value is not None else None

    @cage_bridge_shape.setter
    def cage_bridge_shape(self, value: '_2134.CageBridgeShape'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Bearings.BearingDesigns.Rolling.CageBridgeShape')
        self.wrapped.CageBridgeShape = value

    @property
    def cage_bridge_width(self) -> 'float':
        """float: 'CageBridgeWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CageBridgeWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def cage_guiding_ring_width(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CageGuidingRingWidth' is the original name of this property."""

        temp = self.wrapped.CageGuidingRingWidth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @cage_guiding_ring_width.setter
    def cage_guiding_ring_width(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CageGuidingRingWidth = value

    @property
    def cage_mass(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CageMass' is the original name of this property."""

        temp = self.wrapped.CageMass

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @cage_mass.setter
    def cage_mass(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CageMass = value

    @property
    def cage_material(self) -> '_1859.BearingCageMaterial':
        """BearingCageMaterial: 'CageMaterial' is the original name of this property."""

        temp = self.wrapped.CageMaterial

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bearings.BearingCageMaterial')
        return constructor.new_from_mastapy('mastapy.bearings._1859', 'BearingCageMaterial')(value) if value is not None else None

    @cage_material.setter
    def cage_material(self, value: '_1859.BearingCageMaterial'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Bearings.BearingCageMaterial')
        self.wrapped.CageMaterial = value

    @property
    def cage_pitch_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CagePitchRadius' is the original name of this property."""

        temp = self.wrapped.CagePitchRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @cage_pitch_radius.setter
    def cage_pitch_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CagePitchRadius = value

    @property
    def cage_pocket_clearance(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CagePocketClearance' is the original name of this property."""

        temp = self.wrapped.CagePocketClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @cage_pocket_clearance.setter
    def cage_pocket_clearance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CagePocketClearance = value

    @property
    def cage_thickness(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CageThickness' is the original name of this property."""

        temp = self.wrapped.CageThickness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @cage_thickness.setter
    def cage_thickness(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CageThickness = value

    @property
    def cage_to_inner_ring_clearance(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CageToInnerRingClearance' is the original name of this property."""

        temp = self.wrapped.CageToInnerRingClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @cage_to_inner_ring_clearance.setter
    def cage_to_inner_ring_clearance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CageToInnerRingClearance = value

    @property
    def cage_to_outer_ring_clearance(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CageToOuterRingClearance' is the original name of this property."""

        temp = self.wrapped.CageToOuterRingClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @cage_to_outer_ring_clearance.setter
    def cage_to_outer_ring_clearance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CageToOuterRingClearance = value

    @property
    def cage_width(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CageWidth' is the original name of this property."""

        temp = self.wrapped.CageWidth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @cage_width.setter
    def cage_width(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CageWidth = value

    @property
    def catalogue(self) -> '_1856.BearingCatalog':
        """BearingCatalog: 'Catalogue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Catalogue

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bearings.BearingCatalog')
        return constructor.new_from_mastapy('mastapy.bearings._1856', 'BearingCatalog')(value) if value is not None else None

    @property
    def combined_surface_roughness_inner(self) -> 'float':
        """float: 'CombinedSurfaceRoughnessInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CombinedSurfaceRoughnessInner

        if temp is None:
            return 0.0

        return temp

    @property
    def combined_surface_roughness_outer(self) -> 'float':
        """float: 'CombinedSurfaceRoughnessOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CombinedSurfaceRoughnessOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_angle(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ContactAngle' is the original name of this property."""

        temp = self.wrapped.ContactAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @contact_angle.setter
    def contact_angle(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ContactAngle = value

    @property
    def contact_radius_in_rolling_direction_inner(self) -> 'float':
        """float: 'ContactRadiusInRollingDirectionInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactRadiusInRollingDirectionInner

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_radius_in_rolling_direction_outer(self) -> 'float':
        """float: 'ContactRadiusInRollingDirectionOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactRadiusInRollingDirectionOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def designation(self) -> 'str':
        """str: 'Designation' is the original name of this property."""

        temp = self.wrapped.Designation

        if temp is None:
            return ''

        return temp

    @designation.setter
    def designation(self, value: 'str'):
        self.wrapped.Designation = str(value) if value is not None else ''

    @property
    def diameter_series(self) -> 'overridable.Overridable_DiameterSeries':
        """overridable.Overridable_DiameterSeries: 'DiameterSeries' is the original name of this property."""

        temp = self.wrapped.DiameterSeries

        if temp is None:
            return None

        value = overridable.Overridable_DiameterSeries.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @diameter_series.setter
    def diameter_series(self, value: 'overridable.Overridable_DiameterSeries.implicit_type()'):
        wrapper_type = overridable.Overridable_DiameterSeries.wrapper_type()
        enclosed_type = overridable.Overridable_DiameterSeries.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value if value is not None else None, is_overridden)
        self.wrapped.DiameterSeries = value

    @property
    def distance_between_element_centres(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'DistanceBetweenElementCentres' is the original name of this property."""

        temp = self.wrapped.DistanceBetweenElementCentres

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @distance_between_element_centres.setter
    def distance_between_element_centres(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.DistanceBetweenElementCentres = value

    @property
    def dynamic_axial_load_factor_for_high_axial_radial_load_ratios(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'DynamicAxialLoadFactorForHighAxialRadialLoadRatios' is the original name of this property."""

        temp = self.wrapped.DynamicAxialLoadFactorForHighAxialRadialLoadRatios

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @dynamic_axial_load_factor_for_high_axial_radial_load_ratios.setter
    def dynamic_axial_load_factor_for_high_axial_radial_load_ratios(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.DynamicAxialLoadFactorForHighAxialRadialLoadRatios = value

    @property
    def dynamic_axial_load_factor_for_low_axial_radial_load_ratios(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'DynamicAxialLoadFactorForLowAxialRadialLoadRatios' is the original name of this property."""

        temp = self.wrapped.DynamicAxialLoadFactorForLowAxialRadialLoadRatios

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @dynamic_axial_load_factor_for_low_axial_radial_load_ratios.setter
    def dynamic_axial_load_factor_for_low_axial_radial_load_ratios(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.DynamicAxialLoadFactorForLowAxialRadialLoadRatios = value

    @property
    def dynamic_equivalent_load_factors_can_be_specified(self) -> 'bool':
        """bool: 'DynamicEquivalentLoadFactorsCanBeSpecified' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicEquivalentLoadFactorsCanBeSpecified

        if temp is None:
            return False

        return temp

    @property
    def dynamic_radial_load_factor_for_high_axial_radial_load_ratios(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'DynamicRadialLoadFactorForHighAxialRadialLoadRatios' is the original name of this property."""

        temp = self.wrapped.DynamicRadialLoadFactorForHighAxialRadialLoadRatios

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @dynamic_radial_load_factor_for_high_axial_radial_load_ratios.setter
    def dynamic_radial_load_factor_for_high_axial_radial_load_ratios(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.DynamicRadialLoadFactorForHighAxialRadialLoadRatios = value

    @property
    def dynamic_radial_load_factor_for_low_axial_radial_load_ratios(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'DynamicRadialLoadFactorForLowAxialRadialLoadRatios' is the original name of this property."""

        temp = self.wrapped.DynamicRadialLoadFactorForLowAxialRadialLoadRatios

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @dynamic_radial_load_factor_for_low_axial_radial_load_ratios.setter
    def dynamic_radial_load_factor_for_low_axial_radial_load_ratios(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.DynamicRadialLoadFactorForLowAxialRadialLoadRatios = value

    @property
    def element_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ElementDiameter' is the original name of this property."""

        temp = self.wrapped.ElementDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @element_diameter.setter
    def element_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ElementDiameter = value

    @property
    def element_material_reportable(self) -> 'str':
        """str: 'ElementMaterialReportable' is the original name of this property."""

        temp = self.wrapped.ElementMaterialReportable.SelectedItemName

        if temp is None:
            return ''

        return temp

    @element_material_reportable.setter
    def element_material_reportable(self, value: 'str'):
        self.wrapped.ElementMaterialReportable.SetSelectedItem(str(value) if value is not None else '')

    @property
    def element_offset(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ElementOffset' is the original name of this property."""

        temp = self.wrapped.ElementOffset

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @element_offset.setter
    def element_offset(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ElementOffset = value

    @property
    def element_radius(self) -> 'float':
        """float: 'ElementRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def element_surface_roughness_rms(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ElementSurfaceRoughnessRMS' is the original name of this property."""

        temp = self.wrapped.ElementSurfaceRoughnessRMS

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @element_surface_roughness_rms.setter
    def element_surface_roughness_rms(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ElementSurfaceRoughnessRMS = value

    @property
    def element_surface_roughness_ra(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ElementSurfaceRoughnessRa' is the original name of this property."""

        temp = self.wrapped.ElementSurfaceRoughnessRa

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @element_surface_roughness_ra.setter
    def element_surface_roughness_ra(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ElementSurfaceRoughnessRa = value

    @property
    def extra_information(self) -> 'str':
        """str: 'ExtraInformation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExtraInformation

        if temp is None:
            return ''

        return temp

    @property
    def factor_for_basic_dynamic_load_rating_in_ansiabma(self) -> 'float':
        """float: 'FactorForBasicDynamicLoadRatingInANSIABMA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FactorForBasicDynamicLoadRatingInANSIABMA

        if temp is None:
            return 0.0

        return temp

    @property
    def fatigue_load_limit(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'FatigueLoadLimit' is the original name of this property."""

        temp = self.wrapped.FatigueLoadLimit

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @fatigue_load_limit.setter
    def fatigue_load_limit(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.FatigueLoadLimit = value

    @property
    def fatigue_load_limit_calculation_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_FatigueLoadLimitCalculationMethodEnum':
        """enum_with_selected_value.EnumWithSelectedValue_FatigueLoadLimitCalculationMethodEnum: 'FatigueLoadLimitCalculationMethod' is the original name of this property."""

        temp = self.wrapped.FatigueLoadLimitCalculationMethod

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_FatigueLoadLimitCalculationMethodEnum.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @fatigue_load_limit_calculation_method.setter
    def fatigue_load_limit_calculation_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_FatigueLoadLimitCalculationMethodEnum.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_FatigueLoadLimitCalculationMethodEnum.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.FatigueLoadLimitCalculationMethod = value

    @property
    def free_space_between_elements(self) -> 'float':
        """float: 'FreeSpaceBetweenElements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FreeSpaceBetweenElements

        if temp is None:
            return 0.0

        return temp

    @property
    def height_series(self) -> 'overridable.Overridable_HeightSeries':
        """overridable.Overridable_HeightSeries: 'HeightSeries' is the original name of this property."""

        temp = self.wrapped.HeightSeries

        if temp is None:
            return None

        value = overridable.Overridable_HeightSeries.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @height_series.setter
    def height_series(self, value: 'overridable.Overridable_HeightSeries.implicit_type()'):
        wrapper_type = overridable.Overridable_HeightSeries.wrapper_type()
        enclosed_type = overridable.Overridable_HeightSeries.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value if value is not None else None, is_overridden)
        self.wrapped.HeightSeries = value

    @property
    def iso_material_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ISOMaterialFactor' is the original name of this property."""

        temp = self.wrapped.ISOMaterialFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @iso_material_factor.setter
    def iso_material_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ISOMaterialFactor = value

    @property
    def inner_race_hardness_depth(self) -> 'float':
        """float: 'InnerRaceHardnessDepth' is the original name of this property."""

        temp = self.wrapped.InnerRaceHardnessDepth

        if temp is None:
            return 0.0

        return temp

    @inner_race_hardness_depth.setter
    def inner_race_hardness_depth(self, value: 'float'):
        self.wrapped.InnerRaceHardnessDepth = float(value) if value is not None else 0.0

    @property
    def inner_race_material_reportable(self) -> 'str':
        """str: 'InnerRaceMaterialReportable' is the original name of this property."""

        temp = self.wrapped.InnerRaceMaterialReportable.SelectedItemName

        if temp is None:
            return ''

        return temp

    @inner_race_material_reportable.setter
    def inner_race_material_reportable(self, value: 'str'):
        self.wrapped.InnerRaceMaterialReportable.SetSelectedItem(str(value) if value is not None else '')

    @property
    def inner_race_outer_diameter(self) -> 'float':
        """float: 'InnerRaceOuterDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRaceOuterDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_race_type(self) -> 'enum_with_selected_value.EnumWithSelectedValue_RollingBearingRaceType':
        """enum_with_selected_value.EnumWithSelectedValue_RollingBearingRaceType: 'InnerRaceType' is the original name of this property."""

        temp = self.wrapped.InnerRaceType

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_RollingBearingRaceType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @inner_race_type.setter
    def inner_race_type(self, value: 'enum_with_selected_value.EnumWithSelectedValue_RollingBearingRaceType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_RollingBearingRaceType.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.InnerRaceType = value

    @property
    def inner_ring_left_corner_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'InnerRingLeftCornerRadius' is the original name of this property."""

        temp = self.wrapped.InnerRingLeftCornerRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @inner_ring_left_corner_radius.setter
    def inner_ring_left_corner_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.InnerRingLeftCornerRadius = value

    @property
    def inner_ring_right_corner_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'InnerRingRightCornerRadius' is the original name of this property."""

        temp = self.wrapped.InnerRingRightCornerRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @inner_ring_right_corner_radius.setter
    def inner_ring_right_corner_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.InnerRingRightCornerRadius = value

    @property
    def inner_ring_width(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'InnerRingWidth' is the original name of this property."""

        temp = self.wrapped.InnerRingWidth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @inner_ring_width.setter
    def inner_ring_width(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.InnerRingWidth = value

    @property
    def is_full_complement(self) -> 'overridable.Overridable_bool':
        """overridable.Overridable_bool: 'IsFullComplement' is the original name of this property."""

        temp = self.wrapped.IsFullComplement

        if temp is None:
            return False

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_bool')(temp) if temp is not None else False

    @is_full_complement.setter
    def is_full_complement(self, value: 'overridable.Overridable_bool.implicit_type()'):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else False, is_overridden)
        self.wrapped.IsFullComplement = value

    @property
    def kz(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'KZ' is the original name of this property."""

        temp = self.wrapped.KZ

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @kz.setter
    def kz(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.KZ = value

    @property
    def limiting_value_for_axial_load_ratio(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'LimitingValueForAxialLoadRatio' is the original name of this property."""

        temp = self.wrapped.LimitingValueForAxialLoadRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @limiting_value_for_axial_load_ratio.setter
    def limiting_value_for_axial_load_ratio(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.LimitingValueForAxialLoadRatio = value

    @property
    def manufacturer(self) -> 'str':
        """str: 'Manufacturer' is the original name of this property."""

        temp = self.wrapped.Manufacturer

        if temp is None:
            return ''

        return temp

    @manufacturer.setter
    def manufacturer(self, value: 'str'):
        self.wrapped.Manufacturer = str(value) if value is not None else ''

    @property
    def maximum_grease_speed(self) -> 'float':
        """float: 'MaximumGreaseSpeed' is the original name of this property."""

        temp = self.wrapped.MaximumGreaseSpeed

        if temp is None:
            return 0.0

        return temp

    @maximum_grease_speed.setter
    def maximum_grease_speed(self, value: 'float'):
        self.wrapped.MaximumGreaseSpeed = float(value) if value is not None else 0.0

    @property
    def maximum_oil_speed(self) -> 'float':
        """float: 'MaximumOilSpeed' is the original name of this property."""

        temp = self.wrapped.MaximumOilSpeed

        if temp is None:
            return 0.0

        return temp

    @maximum_oil_speed.setter
    def maximum_oil_speed(self, value: 'float'):
        self.wrapped.MaximumOilSpeed = float(value) if value is not None else 0.0

    @property
    def maximum_permissible_contact_stress_for_static_failure_inner(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MaximumPermissibleContactStressForStaticFailureInner' is the original name of this property."""

        temp = self.wrapped.MaximumPermissibleContactStressForStaticFailureInner

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @maximum_permissible_contact_stress_for_static_failure_inner.setter
    def maximum_permissible_contact_stress_for_static_failure_inner(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MaximumPermissibleContactStressForStaticFailureInner = value

    @property
    def maximum_permissible_contact_stress_for_static_failure_outer(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MaximumPermissibleContactStressForStaticFailureOuter' is the original name of this property."""

        temp = self.wrapped.MaximumPermissibleContactStressForStaticFailureOuter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @maximum_permissible_contact_stress_for_static_failure_outer.setter
    def maximum_permissible_contact_stress_for_static_failure_outer(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MaximumPermissibleContactStressForStaticFailureOuter = value

    @property
    def minimum_surface_roughness_rms(self) -> 'float':
        """float: 'MinimumSurfaceRoughnessRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumSurfaceRoughnessRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_surface_roughness_ra(self) -> 'float':
        """float: 'MinimumSurfaceRoughnessRa' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumSurfaceRoughnessRa

        if temp is None:
            return 0.0

        return temp

    @property
    def no_history(self) -> 'str':
        """str: 'NoHistory' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NoHistory

        if temp is None:
            return ''

        return temp

    @property
    def number_of_elements(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'NumberOfElements' is the original name of this property."""

        temp = self.wrapped.NumberOfElements

        if temp is None:
            return 0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_int')(temp) if temp is not None else 0

    @number_of_elements.setter
    def number_of_elements(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.NumberOfElements = value

    @property
    def number_of_rows(self) -> 'int':
        """int: 'NumberOfRows' is the original name of this property."""

        temp = self.wrapped.NumberOfRows

        if temp is None:
            return 0

        return temp

    @number_of_rows.setter
    def number_of_rows(self, value: 'int'):
        self.wrapped.NumberOfRows = int(value) if value is not None else 0

    @property
    def outer_race_hardness_depth(self) -> 'float':
        """float: 'OuterRaceHardnessDepth' is the original name of this property."""

        temp = self.wrapped.OuterRaceHardnessDepth

        if temp is None:
            return 0.0

        return temp

    @outer_race_hardness_depth.setter
    def outer_race_hardness_depth(self, value: 'float'):
        self.wrapped.OuterRaceHardnessDepth = float(value) if value is not None else 0.0

    @property
    def outer_race_inner_diameter(self) -> 'float':
        """float: 'OuterRaceInnerDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRaceInnerDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_race_material_reportable(self) -> 'str':
        """str: 'OuterRaceMaterialReportable' is the original name of this property."""

        temp = self.wrapped.OuterRaceMaterialReportable.SelectedItemName

        if temp is None:
            return ''

        return temp

    @outer_race_material_reportable.setter
    def outer_race_material_reportable(self, value: 'str'):
        self.wrapped.OuterRaceMaterialReportable.SetSelectedItem(str(value) if value is not None else '')

    @property
    def outer_race_type(self) -> 'enum_with_selected_value.EnumWithSelectedValue_RollingBearingRaceType':
        """enum_with_selected_value.EnumWithSelectedValue_RollingBearingRaceType: 'OuterRaceType' is the original name of this property."""

        temp = self.wrapped.OuterRaceType

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_RollingBearingRaceType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @outer_race_type.setter
    def outer_race_type(self, value: 'enum_with_selected_value.EnumWithSelectedValue_RollingBearingRaceType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_RollingBearingRaceType.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.OuterRaceType = value

    @property
    def outer_ring_left_corner_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OuterRingLeftCornerRadius' is the original name of this property."""

        temp = self.wrapped.OuterRingLeftCornerRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @outer_ring_left_corner_radius.setter
    def outer_ring_left_corner_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.OuterRingLeftCornerRadius = value

    @property
    def outer_ring_offset(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OuterRingOffset' is the original name of this property."""

        temp = self.wrapped.OuterRingOffset

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @outer_ring_offset.setter
    def outer_ring_offset(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.OuterRingOffset = value

    @property
    def outer_ring_right_corner_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OuterRingRightCornerRadius' is the original name of this property."""

        temp = self.wrapped.OuterRingRightCornerRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @outer_ring_right_corner_radius.setter
    def outer_ring_right_corner_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.OuterRingRightCornerRadius = value

    @property
    def outer_ring_width(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OuterRingWidth' is the original name of this property."""

        temp = self.wrapped.OuterRingWidth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @outer_ring_width.setter
    def outer_ring_width(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.OuterRingWidth = value

    @property
    def pitch_circle_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'PitchCircleDiameter' is the original name of this property."""

        temp = self.wrapped.PitchCircleDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @pitch_circle_diameter.setter
    def pitch_circle_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.PitchCircleDiameter = value

    @property
    def power_for_maximum_contact_stress_safety_factor(self) -> 'float':
        """float: 'PowerForMaximumContactStressSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerForMaximumContactStressSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def raceway_surface_roughness_rms_inner(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RacewaySurfaceRoughnessRMSInner' is the original name of this property."""

        temp = self.wrapped.RacewaySurfaceRoughnessRMSInner

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @raceway_surface_roughness_rms_inner.setter
    def raceway_surface_roughness_rms_inner(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RacewaySurfaceRoughnessRMSInner = value

    @property
    def raceway_surface_roughness_rms_outer(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RacewaySurfaceRoughnessRMSOuter' is the original name of this property."""

        temp = self.wrapped.RacewaySurfaceRoughnessRMSOuter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @raceway_surface_roughness_rms_outer.setter
    def raceway_surface_roughness_rms_outer(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RacewaySurfaceRoughnessRMSOuter = value

    @property
    def raceway_surface_roughness_ra_inner(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RacewaySurfaceRoughnessRaInner' is the original name of this property."""

        temp = self.wrapped.RacewaySurfaceRoughnessRaInner

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @raceway_surface_roughness_ra_inner.setter
    def raceway_surface_roughness_ra_inner(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RacewaySurfaceRoughnessRaInner = value

    @property
    def raceway_surface_roughness_ra_outer(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RacewaySurfaceRoughnessRaOuter' is the original name of this property."""

        temp = self.wrapped.RacewaySurfaceRoughnessRaOuter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @raceway_surface_roughness_ra_outer.setter
    def raceway_surface_roughness_ra_outer(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RacewaySurfaceRoughnessRaOuter = value

    @property
    def sleeve_type(self) -> '_2155.SleeveType':
        """SleeveType: 'SleeveType' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SleeveType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bearings.BearingDesigns.Rolling.SleeveType')
        return constructor.new_from_mastapy('mastapy.bearings.bearing_designs.rolling._2155', 'SleeveType')(value) if value is not None else None

    @property
    def theoretical_maximum_number_of_elements(self) -> 'float':
        """float: 'TheoreticalMaximumNumberOfElements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TheoreticalMaximumNumberOfElements

        if temp is None:
            return 0.0

        return temp

    @property
    def total_free_space_between_elements(self) -> 'float':
        """float: 'TotalFreeSpaceBetweenElements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalFreeSpaceBetweenElements

        if temp is None:
            return 0.0

        return temp

    @property
    def type_(self) -> 'str':
        """str: 'Type' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Type

        if temp is None:
            return ''

        return temp

    @property
    def type_information(self) -> '_2133.BearingTypeExtraInformation':
        """BearingTypeExtraInformation: 'TypeInformation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TypeInformation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bearings.BearingDesigns.Rolling.BearingTypeExtraInformation')
        return constructor.new_from_mastapy('mastapy.bearings.bearing_designs.rolling._2133', 'BearingTypeExtraInformation')(value) if value is not None else None

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
    def width_series(self) -> 'overridable.Overridable_WidthSeries':
        """overridable.Overridable_WidthSeries: 'WidthSeries' is the original name of this property."""

        temp = self.wrapped.WidthSeries

        if temp is None:
            return None

        value = overridable.Overridable_WidthSeries.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @width_series.setter
    def width_series(self, value: 'overridable.Overridable_WidthSeries.implicit_type()'):
        wrapper_type = overridable.Overridable_WidthSeries.wrapper_type()
        enclosed_type = overridable.Overridable_WidthSeries.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value if value is not None else None, is_overridden)
        self.wrapped.WidthSeries = value

    @property
    def element_material(self) -> '_243.BearingMaterial':
        """BearingMaterial: 'ElementMaterial' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementMaterial

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def geometric_constants(self) -> '_2142.GeometricConstants':
        """GeometricConstants: 'GeometricConstants' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GeometricConstants

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def history(self) -> '_1573.FileHistory':
        """FileHistory: 'History' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.History

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def iso153122018(self) -> '_1964.ISO153122018Results':
        """ISO153122018Results: 'ISO153122018' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO153122018

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_ring_material(self) -> '_243.BearingMaterial':
        """BearingMaterial: 'InnerRingMaterial' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRingMaterial

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_ring_material(self) -> '_243.BearingMaterial':
        """BearingMaterial: 'OuterRingMaterial' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRingMaterial

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def protection(self) -> '_2130.BearingProtection':
        """BearingProtection: 'Protection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Protection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def skf_seal_frictional_moment_constants(self) -> '_2154.SKFSealFrictionalMomentConstants':
        """SKFSealFrictionalMomentConstants: 'SKFSealFrictionalMomentConstants' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SKFSealFrictionalMomentConstants

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def remove_inner_ring_while_keeping_other_geometry_constant(self):
        """ 'RemoveInnerRingWhileKeepingOtherGeometryConstant' is the original name of this method."""

        self.wrapped.RemoveInnerRingWhileKeepingOtherGeometryConstant()

    def remove_outer_ring_while_keeping_other_geometry_constant(self):
        """ 'RemoveOuterRingWhileKeepingOtherGeometryConstant' is the original name of this method."""

        self.wrapped.RemoveOuterRingWhileKeepingOtherGeometryConstant()

    def __copy__(self) -> 'RollingBearing':
        """ 'Copy' is the original name of this method.

        Returns:
            mastapy.bearings.bearing_designs.rolling.RollingBearing
        """

        method_result = self.wrapped.Copy()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def __deepcopy__(self, memo) -> 'RollingBearing':
        """ 'Copy' is the original name of this method.

        Returns:
            mastapy.bearings.bearing_designs.rolling.RollingBearing
        """

        method_result = self.wrapped.Copy()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def link_to_online_catalogue(self):
        """ 'LinkToOnlineCatalogue' is the original name of this method."""

        self.wrapped.LinkToOnlineCatalogue()

    @property
    def cast_to(self) -> 'RollingBearing._Cast_RollingBearing':
        return self._Cast_RollingBearing(self)
