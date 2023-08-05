﻿"""_2507.py

CylindricalGear
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.part_model.gears import _2512
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'CylindricalGear')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1009
    from mastapy.system_model.connections_and_sockets.gears import _2292


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGear',)


class CylindricalGear(_2512.Gear):
    """CylindricalGear

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR

    class _Cast_CylindricalGear:
        """Special nested class for casting CylindricalGear to subclasses."""

        def __init__(self, parent: 'CylindricalGear'):
            self._parent = parent

        @property
        def gear(self):
            return self._parent._cast(_2512.Gear)

        @property
        def mountable_component(self):
            from mastapy.system_model.part_model import _2447
            
            return self._parent._cast(_2447.MountableComponent)

        @property
        def component(self):
            from mastapy.system_model.part_model import _2427
            
            return self._parent._cast(_2427.Component)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2451
            
            return self._parent._cast(_2451.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2190
            
            return self._parent._cast(_2190.DesignEntity)

        @property
        def cylindrical_planet_gear(self):
            from mastapy.system_model.part_model.gears import _2509
            
            return self._parent._cast(_2509.CylindricalPlanetGear)

        @property
        def cylindrical_gear(self) -> 'CylindricalGear':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def centre_of_estimated_micro_geometry_range(self) -> 'float':
        """float: 'CentreOfEstimatedMicroGeometryRange' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CentreOfEstimatedMicroGeometryRange

        if temp is None:
            return 0.0

        return temp

    @property
    def clearance_to_maximum_tip_diameter(self) -> 'float':
        """float: 'ClearanceToMaximumTipDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClearanceToMaximumTipDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def clocking_angle_error(self) -> 'float':
        """float: 'ClockingAngleError' is the original name of this property."""

        temp = self.wrapped.ClockingAngleError

        if temp is None:
            return 0.0

        return temp

    @clocking_angle_error.setter
    def clocking_angle_error(self, value: 'float'):
        self.wrapped.ClockingAngleError = float(value) if value is not None else 0.0

    @property
    def estimated_crowning(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'EstimatedCrowning' is the original name of this property."""

        temp = self.wrapped.EstimatedCrowning

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @estimated_crowning.setter
    def estimated_crowning(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.EstimatedCrowning = value

    @property
    def extra_backlash(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ExtraBacklash' is the original name of this property."""

        temp = self.wrapped.ExtraBacklash

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @extra_backlash.setter
    def extra_backlash(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ExtraBacklash = value

    @property
    def has_concept_synchroniser(self) -> 'bool':
        """bool: 'HasConceptSynchroniser' is the original name of this property."""

        temp = self.wrapped.HasConceptSynchroniser

        if temp is None:
            return False

        return temp

    @has_concept_synchroniser.setter
    def has_concept_synchroniser(self, value: 'bool'):
        self.wrapped.HasConceptSynchroniser = bool(value) if value is not None else False

    @property
    def is_position_fixed_for_centre_distance_modification(self) -> 'bool':
        """bool: 'IsPositionFixedForCentreDistanceModification' is the original name of this property."""

        temp = self.wrapped.IsPositionFixedForCentreDistanceModification

        if temp is None:
            return False

        return temp

    @is_position_fixed_for_centre_distance_modification.setter
    def is_position_fixed_for_centre_distance_modification(self, value: 'bool'):
        self.wrapped.IsPositionFixedForCentreDistanceModification = bool(value) if value is not None else False

    @property
    def left_limit_of_estimated_micro_geometry_range(self) -> 'float':
        """float: 'LeftLimitOfEstimatedMicroGeometryRange' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftLimitOfEstimatedMicroGeometryRange

        if temp is None:
            return 0.0

        return temp

    @property
    def linear_relief(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'LinearRelief' is the original name of this property."""

        temp = self.wrapped.LinearRelief

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @linear_relief.setter
    def linear_relief(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.LinearRelief = value

    @property
    def maximum_tip_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MaximumTipDiameter' is the original name of this property."""

        temp = self.wrapped.MaximumTipDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @maximum_tip_diameter.setter
    def maximum_tip_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MaximumTipDiameter = value

    @property
    def minimum_root_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MinimumRootDiameter' is the original name of this property."""

        temp = self.wrapped.MinimumRootDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @minimum_root_diameter.setter
    def minimum_root_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MinimumRootDiameter = value

    @property
    def reference_axis_angle_about_local_z_axis_from_y_axis(self) -> 'float':
        """float: 'ReferenceAxisAngleAboutLocalZAxisFromYAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReferenceAxisAngleAboutLocalZAxisFromYAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def right_limit_of_estimated_micro_geometry_range(self) -> 'float':
        """float: 'RightLimitOfEstimatedMicroGeometryRange' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightLimitOfEstimatedMicroGeometryRange

        if temp is None:
            return 0.0

        return temp

    @property
    def active_gear_design(self) -> '_1009.CylindricalGearDesign':
        """CylindricalGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_design(self) -> '_1009.CylindricalGearDesign':
        """CylindricalGearDesign: 'CylindricalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_meshes(self) -> 'List[_2292.CylindricalGearMesh]':
        """List[CylindricalGearMesh]: 'CylindricalMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def make_carrier_assembly(self, number_of_radial_bearings: 'int', add_left_thrust_bearing: 'bool', add_right_thrust_bearing: 'bool', gear_bore: 'float', carrier_bore: 'float', carrier_width: 'float', gear_offset: Optional['float'] = 0.0, left_bearing_indent: Optional['float'] = 0.0, right_bearing_indent: Optional['float'] = 0.0, thrust_pad_clearance: Optional['float'] = 0.0, adding_bearing: Optional['bool'] = True, left_thurst_pad_contact_diameter: Optional['Optional[float]'] = None, right_thurst_pad_contact_diameter: Optional['Optional[float]'] = None):
        """ 'MakeCarrierAssembly' is the original name of this method.

        Args:
            number_of_radial_bearings (int)
            add_left_thrust_bearing (bool)
            add_right_thrust_bearing (bool)
            gear_bore (float)
            carrier_bore (float)
            carrier_width (float)
            gear_offset (float, optional)
            left_bearing_indent (float, optional)
            right_bearing_indent (float, optional)
            thrust_pad_clearance (float, optional)
            adding_bearing (bool, optional)
            left_thurst_pad_contact_diameter (Optional[float], optional)
            right_thurst_pad_contact_diameter (Optional[float], optional)
        """

        number_of_radial_bearings = int(number_of_radial_bearings)
        add_left_thrust_bearing = bool(add_left_thrust_bearing)
        add_right_thrust_bearing = bool(add_right_thrust_bearing)
        gear_bore = float(gear_bore)
        carrier_bore = float(carrier_bore)
        carrier_width = float(carrier_width)
        gear_offset = float(gear_offset)
        left_bearing_indent = float(left_bearing_indent)
        right_bearing_indent = float(right_bearing_indent)
        thrust_pad_clearance = float(thrust_pad_clearance)
        adding_bearing = bool(adding_bearing)
        self.wrapped.MakeCarrierAssembly(number_of_radial_bearings if number_of_radial_bearings else 0, add_left_thrust_bearing if add_left_thrust_bearing else False, add_right_thrust_bearing if add_right_thrust_bearing else False, gear_bore if gear_bore else 0.0, carrier_bore if carrier_bore else 0.0, carrier_width if carrier_width else 0.0, gear_offset if gear_offset else 0.0, left_bearing_indent if left_bearing_indent else 0.0, right_bearing_indent if right_bearing_indent else 0.0, thrust_pad_clearance if thrust_pad_clearance else 0.0, adding_bearing if adding_bearing else False, left_thurst_pad_contact_diameter, right_thurst_pad_contact_diameter)

    @property
    def cast_to(self) -> 'CylindricalGear._Cast_CylindricalGear':
        return self._Cast_CylindricalGear(self)
