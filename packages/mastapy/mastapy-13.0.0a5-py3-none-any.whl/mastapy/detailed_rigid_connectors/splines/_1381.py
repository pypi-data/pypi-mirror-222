﻿"""_1381.py

DetailedSplineJointSettings
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DETAILED_SPLINE_JOINT_SETTINGS = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines', 'DetailedSplineJointSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('DetailedSplineJointSettings',)


class DetailedSplineJointSettings(_0.APIBase):
    """DetailedSplineJointSettings

    This is a mastapy class.
    """

    TYPE = _DETAILED_SPLINE_JOINT_SETTINGS

    class _Cast_DetailedSplineJointSettings:
        """Special nested class for casting DetailedSplineJointSettings to subclasses."""

        def __init__(self, parent: 'DetailedSplineJointSettings'):
            self._parent = parent

        @property
        def detailed_spline_joint_settings(self) -> 'DetailedSplineJointSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DetailedSplineJointSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def required_safety_factor_for_compressive_stress(self) -> 'float':
        """float: 'RequiredSafetyFactorForCompressiveStress' is the original name of this property."""

        temp = self.wrapped.RequiredSafetyFactorForCompressiveStress

        if temp is None:
            return 0.0

        return temp

    @required_safety_factor_for_compressive_stress.setter
    def required_safety_factor_for_compressive_stress(self, value: 'float'):
        self.wrapped.RequiredSafetyFactorForCompressiveStress = float(value) if value is not None else 0.0

    @property
    def required_safety_factor_for_ring_bursting(self) -> 'float':
        """float: 'RequiredSafetyFactorForRingBursting' is the original name of this property."""

        temp = self.wrapped.RequiredSafetyFactorForRingBursting

        if temp is None:
            return 0.0

        return temp

    @required_safety_factor_for_ring_bursting.setter
    def required_safety_factor_for_ring_bursting(self, value: 'float'):
        self.wrapped.RequiredSafetyFactorForRingBursting = float(value) if value is not None else 0.0

    @property
    def required_safety_factor_for_root_bending_stress(self) -> 'float':
        """float: 'RequiredSafetyFactorForRootBendingStress' is the original name of this property."""

        temp = self.wrapped.RequiredSafetyFactorForRootBendingStress

        if temp is None:
            return 0.0

        return temp

    @required_safety_factor_for_root_bending_stress.setter
    def required_safety_factor_for_root_bending_stress(self, value: 'float'):
        self.wrapped.RequiredSafetyFactorForRootBendingStress = float(value) if value is not None else 0.0

    @property
    def required_safety_factor_for_tooth_shearing_stress(self) -> 'float':
        """float: 'RequiredSafetyFactorForToothShearingStress' is the original name of this property."""

        temp = self.wrapped.RequiredSafetyFactorForToothShearingStress

        if temp is None:
            return 0.0

        return temp

    @required_safety_factor_for_tooth_shearing_stress.setter
    def required_safety_factor_for_tooth_shearing_stress(self, value: 'float'):
        self.wrapped.RequiredSafetyFactorForToothShearingStress = float(value) if value is not None else 0.0

    @property
    def required_safety_factor_for_torsional_failure(self) -> 'float':
        """float: 'RequiredSafetyFactorForTorsionalFailure' is the original name of this property."""

        temp = self.wrapped.RequiredSafetyFactorForTorsionalFailure

        if temp is None:
            return 0.0

        return temp

    @required_safety_factor_for_torsional_failure.setter
    def required_safety_factor_for_torsional_failure(self, value: 'float'):
        self.wrapped.RequiredSafetyFactorForTorsionalFailure = float(value) if value is not None else 0.0

    @property
    def required_safety_factor_for_wear_and_fretting(self) -> 'float':
        """float: 'RequiredSafetyFactorForWearAndFretting' is the original name of this property."""

        temp = self.wrapped.RequiredSafetyFactorForWearAndFretting

        if temp is None:
            return 0.0

        return temp

    @required_safety_factor_for_wear_and_fretting.setter
    def required_safety_factor_for_wear_and_fretting(self, value: 'float'):
        self.wrapped.RequiredSafetyFactorForWearAndFretting = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'DetailedSplineJointSettings._Cast_DetailedSplineJointSettings':
        return self._Cast_DetailedSplineJointSettings(self)
