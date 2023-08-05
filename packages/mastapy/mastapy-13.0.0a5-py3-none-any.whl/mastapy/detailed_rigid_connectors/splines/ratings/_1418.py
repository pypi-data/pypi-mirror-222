﻿"""_1418.py

GBT17855SplineJointRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.detailed_rigid_connectors.splines.ratings import _1422
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GBT17855_SPLINE_JOINT_RATING = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines.Ratings', 'GBT17855SplineJointRating')


__docformat__ = 'restructuredtext en'
__all__ = ('GBT17855SplineJointRating',)


class GBT17855SplineJointRating(_1422.SplineJointRating):
    """GBT17855SplineJointRating

    This is a mastapy class.
    """

    TYPE = _GBT17855_SPLINE_JOINT_RATING

    class _Cast_GBT17855SplineJointRating:
        """Special nested class for casting GBT17855SplineJointRating to subclasses."""

        def __init__(self, parent: 'GBT17855SplineJointRating'):
            self._parent = parent

        @property
        def spline_joint_rating(self):
            return self._parent._cast(_1422.SplineJointRating)

        @property
        def shaft_hub_connection_rating(self):
            from mastapy.detailed_rigid_connectors.rating import _1426
            
            return self._parent._cast(_1426.ShaftHubConnectionRating)

        @property
        def gbt17855_spline_joint_rating(self) -> 'GBT17855SplineJointRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GBT17855SplineJointRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def application_factor(self) -> 'float':
        """float: 'ApplicationFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ApplicationFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def backlash_factor(self) -> 'float':
        """float: 'BacklashFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BacklashFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def calculated_compressive_stress(self) -> 'float':
        """float: 'CalculatedCompressiveStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedCompressiveStress

        if temp is None:
            return 0.0

        return temp

    @property
    def calculated_maximum_tooth_shearing_stress(self) -> 'float':
        """float: 'CalculatedMaximumToothShearingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedMaximumToothShearingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def calculated_root_bending_stress(self) -> 'float':
        """float: 'CalculatedRootBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedRootBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def distribution_factor(self) -> 'float':
        """float: 'DistributionFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DistributionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def equivalent_stress(self) -> 'float':
        """float: 'EquivalentStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EquivalentStress

        if temp is None:
            return 0.0

        return temp

    @property
    def face_load_distribution_factor(self) -> 'float':
        """float: 'FaceLoadDistributionFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceLoadDistributionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def k_factor(self) -> 'float':
        """float: 'KFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KFactor

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
    def safety_factor_for_compressive_stress(self) -> 'float':
        """float: 'SafetyFactorForCompressiveStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForCompressiveStress

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_equivalent_stress(self) -> 'float':
        """float: 'SafetyFactorForEquivalentStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForEquivalentStress

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_root_bending_stress(self) -> 'float':
        """float: 'SafetyFactorForRootBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForRootBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_tooth_shearing_stress(self) -> 'float':
        """float: 'SafetyFactorForToothShearingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForToothShearingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_wearing_stress(self) -> 'float':
        """float: 'SafetyFactorForWearingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForWearingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'GBT17855SplineJointRating._Cast_GBT17855SplineJointRating':
        return self._Cast_GBT17855SplineJointRating(self)
