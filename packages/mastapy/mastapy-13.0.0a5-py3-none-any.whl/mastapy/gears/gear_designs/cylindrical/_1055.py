﻿"""_1055.py

LTCALoadCaseModifiableSettings
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.utility import _1577
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LTCA_LOAD_CASE_MODIFIABLE_SETTINGS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'LTCALoadCaseModifiableSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('LTCALoadCaseModifiableSettings',)


class LTCALoadCaseModifiableSettings(_1577.IndependentReportablePropertiesBase['LTCALoadCaseModifiableSettings']):
    """LTCALoadCaseModifiableSettings

    This is a mastapy class.
    """

    TYPE = _LTCA_LOAD_CASE_MODIFIABLE_SETTINGS

    class _Cast_LTCALoadCaseModifiableSettings:
        """Special nested class for casting LTCALoadCaseModifiableSettings to subclasses."""

        def __init__(self, parent: 'LTCALoadCaseModifiableSettings'):
            self._parent = parent

        @property
        def independent_reportable_properties_base(self):
            from mastapy.gears.gear_designs.cylindrical import _1055
            
            return self._parent._cast(_1577.IndependentReportablePropertiesBase)

        @property
        def ltca_load_case_modifiable_settings(self) -> 'LTCALoadCaseModifiableSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LTCALoadCaseModifiableSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def apply_application_and_dynamic_factor(self) -> 'bool':
        """bool: 'ApplyApplicationAndDynamicFactor' is the original name of this property."""

        temp = self.wrapped.ApplyApplicationAndDynamicFactor

        if temp is None:
            return False

        return temp

    @apply_application_and_dynamic_factor.setter
    def apply_application_and_dynamic_factor(self, value: 'bool'):
        self.wrapped.ApplyApplicationAndDynamicFactor = bool(value) if value is not None else False

    @property
    def include_change_in_contact_point_due_to_micro_geometry(self) -> 'bool':
        """bool: 'IncludeChangeInContactPointDueToMicroGeometry' is the original name of this property."""

        temp = self.wrapped.IncludeChangeInContactPointDueToMicroGeometry

        if temp is None:
            return False

        return temp

    @include_change_in_contact_point_due_to_micro_geometry.setter
    def include_change_in_contact_point_due_to_micro_geometry(self, value: 'bool'):
        self.wrapped.IncludeChangeInContactPointDueToMicroGeometry = bool(value) if value is not None else False

    @property
    def use_jacobian_advanced_ltca_solver(self) -> 'bool':
        """bool: 'UseJacobianAdvancedLTCASolver' is the original name of this property."""

        temp = self.wrapped.UseJacobianAdvancedLTCASolver

        if temp is None:
            return False

        return temp

    @use_jacobian_advanced_ltca_solver.setter
    def use_jacobian_advanced_ltca_solver(self, value: 'bool'):
        self.wrapped.UseJacobianAdvancedLTCASolver = bool(value) if value is not None else False

    @property
    def cast_to(self) -> 'LTCALoadCaseModifiableSettings._Cast_LTCALoadCaseModifiableSettings':
        return self._Cast_LTCALoadCaseModifiableSettings(self)
