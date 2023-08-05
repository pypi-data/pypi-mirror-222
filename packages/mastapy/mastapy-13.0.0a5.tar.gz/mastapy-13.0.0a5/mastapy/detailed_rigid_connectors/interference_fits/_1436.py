﻿"""_1436.py

InterferenceFitHalfDesign
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.detailed_rigid_connectors import _1378
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTERFERENCE_FIT_HALF_DESIGN = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.InterferenceFits', 'InterferenceFitHalfDesign')

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.interference_fits import _1437
    from mastapy.bearings.tolerances import _1909


__docformat__ = 'restructuredtext en'
__all__ = ('InterferenceFitHalfDesign',)


class InterferenceFitHalfDesign(_1378.DetailedRigidConnectorHalfDesign):
    """InterferenceFitHalfDesign

    This is a mastapy class.
    """

    TYPE = _INTERFERENCE_FIT_HALF_DESIGN

    class _Cast_InterferenceFitHalfDesign:
        """Special nested class for casting InterferenceFitHalfDesign to subclasses."""

        def __init__(self, parent: 'InterferenceFitHalfDesign'):
            self._parent = parent

        @property
        def detailed_rigid_connector_half_design(self):
            return self._parent._cast(_1378.DetailedRigidConnectorHalfDesign)

        @property
        def keyway_joint_half_design(self):
            from mastapy.detailed_rigid_connectors.keyed_joints import _1429
            
            return self._parent._cast(_1429.KeywayJointHalfDesign)

        @property
        def interference_fit_half_design(self) -> 'InterferenceFitHalfDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InterferenceFitHalfDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_joint_diameter(self) -> 'float':
        """float: 'AverageJointDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageJointDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def average_surface_roughness(self) -> 'float':
        """float: 'AverageSurfaceRoughness' is the original name of this property."""

        temp = self.wrapped.AverageSurfaceRoughness

        if temp is None:
            return 0.0

        return temp

    @average_surface_roughness.setter
    def average_surface_roughness(self, value: 'float'):
        self.wrapped.AverageSurfaceRoughness = float(value) if value is not None else 0.0

    @property
    def designation(self) -> 'str':
        """str: 'Designation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Designation

        if temp is None:
            return ''

        return temp

    @property
    def diameter_ratio(self) -> 'float':
        """float: 'DiameterRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DiameterRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def joint_pressure_for_fully_plastic_part(self) -> 'float':
        """float: 'JointPressureForFullyPlasticPart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.JointPressureForFullyPlasticPart

        if temp is None:
            return 0.0

        return temp

    @property
    def lower_deviation(self) -> 'float':
        """float: 'LowerDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LowerDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def nominal_joint_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'NominalJointDiameter' is the original name of this property."""

        temp = self.wrapped.NominalJointDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @nominal_joint_diameter.setter
    def nominal_joint_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NominalJointDiameter = value

    @property
    def permissible_joint_pressure_for_fully_elastic_part(self) -> 'float':
        """float: 'PermissibleJointPressureForFullyElasticPart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleJointPressureForFullyElasticPart

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_relative_interference_for_fully_elastic_part(self) -> 'float':
        """float: 'PermissibleRelativeInterferenceForFullyElasticPart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleRelativeInterferenceForFullyElasticPart

        if temp is None:
            return 0.0

        return temp

    @property
    def required_safety_against_plastic_strain(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RequiredSafetyAgainstPlasticStrain' is the original name of this property."""

        temp = self.wrapped.RequiredSafetyAgainstPlasticStrain

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @required_safety_against_plastic_strain.setter
    def required_safety_against_plastic_strain(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RequiredSafetyAgainstPlasticStrain = value

    @property
    def stress_region(self) -> '_1437.StressRegions':
        """StressRegions: 'StressRegion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StressRegion

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.DetailedRigidConnectors.InterferenceFits.StressRegions')
        return constructor.new_from_mastapy('mastapy.detailed_rigid_connectors.interference_fits._1437', 'StressRegions')(value) if value is not None else None

    @property
    def upper_deviation(self) -> 'float':
        """float: 'UpperDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UpperDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def tolerance(self) -> '_1909.SupportTolerance':
        """SupportTolerance: 'Tolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Tolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'InterferenceFitHalfDesign._Cast_InterferenceFitHalfDesign':
        return self._Cast_InterferenceFitHalfDesign(self)
