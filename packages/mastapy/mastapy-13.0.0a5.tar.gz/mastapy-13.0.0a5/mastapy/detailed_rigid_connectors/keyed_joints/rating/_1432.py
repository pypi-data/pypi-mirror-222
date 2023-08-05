﻿"""_1432.py

KeywayRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.detailed_rigid_connectors.interference_fits.rating import _1439
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KEYWAY_RATING = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.KeyedJoints.Rating', 'KeywayRating')

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.keyed_joints import _1427
    from mastapy.detailed_rigid_connectors.keyed_joints.rating import _1431


__docformat__ = 'restructuredtext en'
__all__ = ('KeywayRating',)


class KeywayRating(_1439.InterferenceFitRating):
    """KeywayRating

    This is a mastapy class.
    """

    TYPE = _KEYWAY_RATING

    class _Cast_KeywayRating:
        """Special nested class for casting KeywayRating to subclasses."""

        def __init__(self, parent: 'KeywayRating'):
            self._parent = parent

        @property
        def interference_fit_rating(self):
            return self._parent._cast(_1439.InterferenceFitRating)

        @property
        def shaft_hub_connection_rating(self):
            from mastapy.detailed_rigid_connectors.rating import _1426
            
            return self._parent._cast(_1426.ShaftHubConnectionRating)

        @property
        def keyway_rating(self) -> 'KeywayRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KeywayRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def application_factor(self) -> 'float':
        """float: 'ApplicationFactor' is the original name of this property."""

        temp = self.wrapped.ApplicationFactor

        if temp is None:
            return 0.0

        return temp

    @application_factor.setter
    def application_factor(self, value: 'float'):
        self.wrapped.ApplicationFactor = float(value) if value is not None else 0.0

    @property
    def circumferential_force(self) -> 'float':
        """float: 'CircumferentialForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CircumferentialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def extreme_force(self) -> 'float':
        """float: 'ExtremeForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExtremeForce

        if temp is None:
            return 0.0

        return temp

    @property
    def extreme_load_carrying_factor(self) -> 'float':
        """float: 'ExtremeLoadCarryingFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExtremeLoadCarryingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def frictional_engagement_factor_extreme_load(self) -> 'float':
        """float: 'FrictionalEngagementFactorExtremeLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrictionalEngagementFactorExtremeLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def frictional_engagement_factor_rated_load(self) -> 'float':
        """float: 'FrictionalEngagementFactorRatedLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrictionalEngagementFactorRatedLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def frictional_torque(self) -> 'float':
        """float: 'FrictionalTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrictionalTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_component_extreme_safety_factor(self) -> 'float':
        """float: 'InnerComponentExtremeSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerComponentExtremeSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_component_rated_safety_factor(self) -> 'float':
        """float: 'InnerComponentRatedSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerComponentRatedSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def key_extreme_safety_factor(self) -> 'float':
        """float: 'KeyExtremeSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KeyExtremeSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def key_rated_safety_factor(self) -> 'float':
        """float: 'KeyRatedSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KeyRatedSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def load_distribution_factor(self) -> 'float':
        """float: 'LoadDistributionFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadDistributionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def load_distribution_factor_single_key(self) -> 'float':
        """float: 'LoadDistributionFactorSingleKey' is the original name of this property."""

        temp = self.wrapped.LoadDistributionFactorSingleKey

        if temp is None:
            return 0.0

        return temp

    @load_distribution_factor_single_key.setter
    def load_distribution_factor_single_key(self, value: 'float'):
        self.wrapped.LoadDistributionFactorSingleKey = float(value) if value is not None else 0.0

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
    def number_of_torque_peaks(self) -> 'float':
        """float: 'NumberOfTorquePeaks' is the original name of this property."""

        temp = self.wrapped.NumberOfTorquePeaks

        if temp is None:
            return 0.0

        return temp

    @number_of_torque_peaks.setter
    def number_of_torque_peaks(self, value: 'float'):
        self.wrapped.NumberOfTorquePeaks = float(value) if value is not None else 0.0

    @property
    def number_of_torque_reversals(self) -> 'float':
        """float: 'NumberOfTorqueReversals' is the original name of this property."""

        temp = self.wrapped.NumberOfTorqueReversals

        if temp is None:
            return 0.0

        return temp

    @number_of_torque_reversals.setter
    def number_of_torque_reversals(self, value: 'float'):
        self.wrapped.NumberOfTorqueReversals = float(value) if value is not None else 0.0

    @property
    def outer_component_extreme_safety_factor(self) -> 'float':
        """float: 'OuterComponentExtremeSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterComponentExtremeSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_component_rated_safety_factor(self) -> 'float':
        """float: 'OuterComponentRatedSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterComponentRatedSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def rated_force(self) -> 'float':
        """float: 'RatedForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatedForce

        if temp is None:
            return 0.0

        return temp

    @property
    def rated_load_carrying_factor(self) -> 'float':
        """float: 'RatedLoadCarryingFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatedLoadCarryingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_peak_factor(self) -> 'float':
        """float: 'TorquePeakFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorquePeakFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_reversal_factor(self) -> 'float':
        """float: 'TorqueReversalFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueReversalFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def keyed_joint_design(self) -> '_1427.KeyedJointDesign':
        """KeyedJointDesign: 'KeyedJointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KeyedJointDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def keyway_half_ratings(self) -> 'List[_1431.KeywayHalfRating]':
        """List[KeywayHalfRating]: 'KeywayHalfRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KeywayHalfRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KeywayRating._Cast_KeywayRating':
        return self._Cast_KeywayRating(self)
