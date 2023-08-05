﻿"""_1383.py

DIN5480SplineJointDesign
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.detailed_rigid_connectors.splines import _1410
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DIN5480_SPLINE_JOINT_DESIGN = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines', 'DIN5480SplineJointDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('DIN5480SplineJointDesign',)


class DIN5480SplineJointDesign(_1410.StandardSplineJointDesign):
    """DIN5480SplineJointDesign

    This is a mastapy class.
    """

    TYPE = _DIN5480_SPLINE_JOINT_DESIGN

    class _Cast_DIN5480SplineJointDesign:
        """Special nested class for casting DIN5480SplineJointDesign to subclasses."""

        def __init__(self, parent: 'DIN5480SplineJointDesign'):
            self._parent = parent

        @property
        def standard_spline_joint_design(self):
            return self._parent._cast(_1410.StandardSplineJointDesign)

        @property
        def spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1405
            
            return self._parent._cast(_1405.SplineJointDesign)

        @property
        def detailed_rigid_connector_design(self):
            from mastapy.detailed_rigid_connectors import _1377
            
            return self._parent._cast(_1377.DetailedRigidConnectorDesign)

        @property
        def din5480_spline_joint_design(self) -> 'DIN5480SplineJointDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DIN5480SplineJointDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def addendum_modification_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'AddendumModificationFactor' is the original name of this property."""

        temp = self.wrapped.AddendumModificationFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @addendum_modification_factor.setter
    def addendum_modification_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AddendumModificationFactor = value

    @property
    def base_diameter(self) -> 'float':
        """float: 'BaseDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BaseDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_form_clearance(self) -> 'float':
        """float: 'MinimumFormClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumFormClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def nominal_space_width(self) -> 'float':
        """float: 'NominalSpaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalSpaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def nominal_tooth_thickness(self) -> 'float':
        """float: 'NominalToothThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalToothThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_diameter(self) -> 'float':
        """float: 'PitchDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_diameter(self) -> 'float':
        """float: 'ReferenceDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReferenceDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'DIN5480SplineJointDesign._Cast_DIN5480SplineJointDesign':
        return self._Cast_DIN5480SplineJointDesign(self)
