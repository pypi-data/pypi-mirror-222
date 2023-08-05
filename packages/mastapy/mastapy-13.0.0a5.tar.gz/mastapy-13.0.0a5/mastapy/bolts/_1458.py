﻿"""_1458.py

BoltGeometry
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy.utility.databases import _1818
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_GEOMETRY = python_net_import('SMT.MastaAPI.Bolts', 'BoltGeometry')

if TYPE_CHECKING:
    from mastapy.bolts import (
        _1462, _1463, _1474, _1464,
        _1469, _1476
    )


__docformat__ = 'restructuredtext en'
__all__ = ('BoltGeometry',)


class BoltGeometry(_1818.NamedDatabaseItem):
    """BoltGeometry

    This is a mastapy class.
    """

    TYPE = _BOLT_GEOMETRY

    class _Cast_BoltGeometry:
        """Special nested class for casting BoltGeometry to subclasses."""

        def __init__(self, parent: 'BoltGeometry'):
            self._parent = parent

        @property
        def named_database_item(self):
            return self._parent._cast(_1818.NamedDatabaseItem)

        @property
        def bolt_geometry(self) -> 'BoltGeometry':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BoltGeometry.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bolt_diameter(self) -> 'float':
        """float: 'BoltDiameter' is the original name of this property."""

        temp = self.wrapped.BoltDiameter

        if temp is None:
            return 0.0

        return temp

    @bolt_diameter.setter
    def bolt_diameter(self, value: 'float'):
        self.wrapped.BoltDiameter = float(value) if value is not None else 0.0

    @property
    def bolt_inner_diameter(self) -> 'float':
        """float: 'BoltInnerDiameter' is the original name of this property."""

        temp = self.wrapped.BoltInnerDiameter

        if temp is None:
            return 0.0

        return temp

    @bolt_inner_diameter.setter
    def bolt_inner_diameter(self, value: 'float'):
        self.wrapped.BoltInnerDiameter = float(value) if value is not None else 0.0

    @property
    def bolt_length(self) -> 'float':
        """float: 'BoltLength' is the original name of this property."""

        temp = self.wrapped.BoltLength

        if temp is None:
            return 0.0

        return temp

    @bolt_length.setter
    def bolt_length(self, value: 'float'):
        self.wrapped.BoltLength = float(value) if value is not None else 0.0

    @property
    def bolt_name(self) -> 'str':
        """str: 'BoltName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoltName

        if temp is None:
            return ''

        return temp

    @property
    def bolt_sections(self) -> 'List[_1462.BoltSection]':
        """List[BoltSection]: 'BoltSections' is the original name of this property."""

        temp = self.wrapped.BoltSections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @bolt_sections.setter
    def bolt_sections(self, value: 'List[_1462.BoltSection]'):
        value = conversion.mp_to_pn_objects_in_list(value)
        self.wrapped.BoltSections = value

    @property
    def bolt_shank_type(self) -> '_1463.BoltShankType':
        """BoltShankType: 'BoltShankType' is the original name of this property."""

        temp = self.wrapped.BoltShankType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bolts.BoltShankType')
        return constructor.new_from_mastapy('mastapy.bolts._1463', 'BoltShankType')(value) if value is not None else None

    @bolt_shank_type.setter
    def bolt_shank_type(self, value: '_1463.BoltShankType'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Bolts.BoltShankType')
        self.wrapped.BoltShankType = value

    @property
    def bolt_thread_pitch_diameter(self) -> 'float':
        """float: 'BoltThreadPitchDiameter' is the original name of this property."""

        temp = self.wrapped.BoltThreadPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @bolt_thread_pitch_diameter.setter
    def bolt_thread_pitch_diameter(self, value: 'float'):
        self.wrapped.BoltThreadPitchDiameter = float(value) if value is not None else 0.0

    @property
    def has_cross_sections_of_different_diameters(self) -> 'bool':
        """bool: 'HasCrossSectionsOfDifferentDiameters' is the original name of this property."""

        temp = self.wrapped.HasCrossSectionsOfDifferentDiameters

        if temp is None:
            return False

        return temp

    @has_cross_sections_of_different_diameters.setter
    def has_cross_sections_of_different_diameters(self, value: 'bool'):
        self.wrapped.HasCrossSectionsOfDifferentDiameters = bool(value) if value is not None else False

    @property
    def hole_chamfer_width(self) -> 'float':
        """float: 'HoleChamferWidth' is the original name of this property."""

        temp = self.wrapped.HoleChamferWidth

        if temp is None:
            return 0.0

        return temp

    @hole_chamfer_width.setter
    def hole_chamfer_width(self, value: 'float'):
        self.wrapped.HoleChamferWidth = float(value) if value is not None else 0.0

    @property
    def hole_diameter_of_clamped_parts(self) -> 'float':
        """float: 'HoleDiameterOfClampedParts' is the original name of this property."""

        temp = self.wrapped.HoleDiameterOfClampedParts

        if temp is None:
            return 0.0

        return temp

    @hole_diameter_of_clamped_parts.setter
    def hole_diameter_of_clamped_parts(self, value: 'float'):
        self.wrapped.HoleDiameterOfClampedParts = float(value) if value is not None else 0.0

    @property
    def is_threaded_to_head(self) -> 'bool':
        """bool: 'IsThreadedToHead' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsThreadedToHead

        if temp is None:
            return False

        return temp

    @property
    def minor_diameter_of_bolt_thread(self) -> 'float':
        """float: 'MinorDiameterOfBoltThread' is the original name of this property."""

        temp = self.wrapped.MinorDiameterOfBoltThread

        if temp is None:
            return 0.0

        return temp

    @minor_diameter_of_bolt_thread.setter
    def minor_diameter_of_bolt_thread(self, value: 'float'):
        self.wrapped.MinorDiameterOfBoltThread = float(value) if value is not None else 0.0

    @property
    def nut_thread_minor_diameter(self) -> 'float':
        """float: 'NutThreadMinorDiameter' is the original name of this property."""

        temp = self.wrapped.NutThreadMinorDiameter

        if temp is None:
            return 0.0

        return temp

    @nut_thread_minor_diameter.setter
    def nut_thread_minor_diameter(self, value: 'float'):
        self.wrapped.NutThreadMinorDiameter = float(value) if value is not None else 0.0

    @property
    def nut_thread_pitch_diameter(self) -> 'float':
        """float: 'NutThreadPitchDiameter' is the original name of this property."""

        temp = self.wrapped.NutThreadPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @nut_thread_pitch_diameter.setter
    def nut_thread_pitch_diameter(self, value: 'float'):
        self.wrapped.NutThreadPitchDiameter = float(value) if value is not None else 0.0

    @property
    def outside_diameter_of_clamped_parts(self) -> 'float':
        """float: 'OutsideDiameterOfClampedParts' is the original name of this property."""

        temp = self.wrapped.OutsideDiameterOfClampedParts

        if temp is None:
            return 0.0

        return temp

    @outside_diameter_of_clamped_parts.setter
    def outside_diameter_of_clamped_parts(self, value: 'float'):
        self.wrapped.OutsideDiameterOfClampedParts = float(value) if value is not None else 0.0

    @property
    def pitch_of_thread(self) -> 'float':
        """float: 'PitchOfThread' is the original name of this property."""

        temp = self.wrapped.PitchOfThread

        if temp is None:
            return 0.0

        return temp

    @pitch_of_thread.setter
    def pitch_of_thread(self, value: 'float'):
        self.wrapped.PitchOfThread = float(value) if value is not None else 0.0

    @property
    def shank_diameter(self) -> 'float':
        """float: 'ShankDiameter' is the original name of this property."""

        temp = self.wrapped.ShankDiameter

        if temp is None:
            return 0.0

        return temp

    @shank_diameter.setter
    def shank_diameter(self, value: 'float'):
        self.wrapped.ShankDiameter = float(value) if value is not None else 0.0

    @property
    def shank_inner_diameter(self) -> 'float':
        """float: 'ShankInnerDiameter' is the original name of this property."""

        temp = self.wrapped.ShankInnerDiameter

        if temp is None:
            return 0.0

        return temp

    @shank_inner_diameter.setter
    def shank_inner_diameter(self, value: 'float'):
        self.wrapped.ShankInnerDiameter = float(value) if value is not None else 0.0

    @property
    def shank_length(self) -> 'float':
        """float: 'ShankLength' is the original name of this property."""

        temp = self.wrapped.ShankLength

        if temp is None:
            return 0.0

        return temp

    @shank_length.setter
    def shank_length(self, value: 'float'):
        self.wrapped.ShankLength = float(value) if value is not None else 0.0

    @property
    def standard_size(self) -> '_1474.StandardSizes':
        """StandardSizes: 'StandardSize' is the original name of this property."""

        temp = self.wrapped.StandardSize

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bolts.StandardSizes')
        return constructor.new_from_mastapy('mastapy.bolts._1474', 'StandardSizes')(value) if value is not None else None

    @standard_size.setter
    def standard_size(self, value: '_1474.StandardSizes'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Bolts.StandardSizes')
        self.wrapped.StandardSize = value

    @property
    def tapped_thread_minor_diameter(self) -> 'float':
        """float: 'TappedThreadMinorDiameter' is the original name of this property."""

        temp = self.wrapped.TappedThreadMinorDiameter

        if temp is None:
            return 0.0

        return temp

    @tapped_thread_minor_diameter.setter
    def tapped_thread_minor_diameter(self, value: 'float'):
        self.wrapped.TappedThreadMinorDiameter = float(value) if value is not None else 0.0

    @property
    def tapped_thread_pitch_diameter(self) -> 'float':
        """float: 'TappedThreadPitchDiameter' is the original name of this property."""

        temp = self.wrapped.TappedThreadPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @tapped_thread_pitch_diameter.setter
    def tapped_thread_pitch_diameter(self, value: 'float'):
        self.wrapped.TappedThreadPitchDiameter = float(value) if value is not None else 0.0

    @property
    def type_of_bolted_joint(self) -> '_1464.BoltTypes':
        """BoltTypes: 'TypeOfBoltedJoint' is the original name of this property."""

        temp = self.wrapped.TypeOfBoltedJoint

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bolts.BoltTypes')
        return constructor.new_from_mastapy('mastapy.bolts._1464', 'BoltTypes')(value) if value is not None else None

    @type_of_bolted_joint.setter
    def type_of_bolted_joint(self, value: '_1464.BoltTypes'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Bolts.BoltTypes')
        self.wrapped.TypeOfBoltedJoint = value

    @property
    def type_of_head_cap(self) -> '_1469.HeadCapTypes':
        """HeadCapTypes: 'TypeOfHeadCap' is the original name of this property."""

        temp = self.wrapped.TypeOfHeadCap

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bolts.HeadCapTypes')
        return constructor.new_from_mastapy('mastapy.bolts._1469', 'HeadCapTypes')(value) if value is not None else None

    @type_of_head_cap.setter
    def type_of_head_cap(self, value: '_1469.HeadCapTypes'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Bolts.HeadCapTypes')
        self.wrapped.TypeOfHeadCap = value

    @property
    def type_of_thread(self) -> '_1476.ThreadTypes':
        """ThreadTypes: 'TypeOfThread' is the original name of this property."""

        temp = self.wrapped.TypeOfThread

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bolts.ThreadTypes')
        return constructor.new_from_mastapy('mastapy.bolts._1476', 'ThreadTypes')(value) if value is not None else None

    @type_of_thread.setter
    def type_of_thread(self, value: '_1476.ThreadTypes'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Bolts.ThreadTypes')
        self.wrapped.TypeOfThread = value

    @property
    def width_across_flats(self) -> 'float':
        """float: 'WidthAcrossFlats' is the original name of this property."""

        temp = self.wrapped.WidthAcrossFlats

        if temp is None:
            return 0.0

        return temp

    @width_across_flats.setter
    def width_across_flats(self, value: 'float'):
        self.wrapped.WidthAcrossFlats = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'BoltGeometry._Cast_BoltGeometry':
        return self._Cast_BoltGeometry(self)
