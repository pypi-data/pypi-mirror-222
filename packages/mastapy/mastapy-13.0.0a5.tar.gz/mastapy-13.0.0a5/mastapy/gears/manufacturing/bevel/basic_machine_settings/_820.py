﻿"""_820.py

BasicConicalGearMachineSettingsGenerated
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel.basic_machine_settings import _818
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BASIC_CONICAL_GEAR_MACHINE_SETTINGS_GENERATED = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel.BasicMachineSettings', 'BasicConicalGearMachineSettingsGenerated')


__docformat__ = 'restructuredtext en'
__all__ = ('BasicConicalGearMachineSettingsGenerated',)


class BasicConicalGearMachineSettingsGenerated(_818.BasicConicalGearMachineSettings):
    """BasicConicalGearMachineSettingsGenerated

    This is a mastapy class.
    """

    TYPE = _BASIC_CONICAL_GEAR_MACHINE_SETTINGS_GENERATED

    class _Cast_BasicConicalGearMachineSettingsGenerated:
        """Special nested class for casting BasicConicalGearMachineSettingsGenerated to subclasses."""

        def __init__(self, parent: 'BasicConicalGearMachineSettingsGenerated'):
            self._parent = parent

        @property
        def basic_conical_gear_machine_settings(self):
            return self._parent._cast(_818.BasicConicalGearMachineSettings)

        @property
        def basic_conical_gear_machine_settings_generated(self) -> 'BasicConicalGearMachineSettingsGenerated':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BasicConicalGearMachineSettingsGenerated.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def basic_cradle_angle(self) -> 'float':
        """float: 'BasicCradleAngle' is the original name of this property."""

        temp = self.wrapped.BasicCradleAngle

        if temp is None:
            return 0.0

        return temp

    @basic_cradle_angle.setter
    def basic_cradle_angle(self, value: 'float'):
        self.wrapped.BasicCradleAngle = float(value) if value is not None else 0.0

    @property
    def blank_offset(self) -> 'float':
        """float: 'BlankOffset' is the original name of this property."""

        temp = self.wrapped.BlankOffset

        if temp is None:
            return 0.0

        return temp

    @blank_offset.setter
    def blank_offset(self, value: 'float'):
        self.wrapped.BlankOffset = float(value) if value is not None else 0.0

    @property
    def modified_roll_coefficient_c(self) -> 'float':
        """float: 'ModifiedRollCoefficientC' is the original name of this property."""

        temp = self.wrapped.ModifiedRollCoefficientC

        if temp is None:
            return 0.0

        return temp

    @modified_roll_coefficient_c.setter
    def modified_roll_coefficient_c(self, value: 'float'):
        self.wrapped.ModifiedRollCoefficientC = float(value) if value is not None else 0.0

    @property
    def modified_roll_coefficient_d(self) -> 'float':
        """float: 'ModifiedRollCoefficientD' is the original name of this property."""

        temp = self.wrapped.ModifiedRollCoefficientD

        if temp is None:
            return 0.0

        return temp

    @modified_roll_coefficient_d.setter
    def modified_roll_coefficient_d(self, value: 'float'):
        self.wrapped.ModifiedRollCoefficientD = float(value) if value is not None else 0.0

    @property
    def radial_setting(self) -> 'float':
        """float: 'RadialSetting' is the original name of this property."""

        temp = self.wrapped.RadialSetting

        if temp is None:
            return 0.0

        return temp

    @radial_setting.setter
    def radial_setting(self, value: 'float'):
        self.wrapped.RadialSetting = float(value) if value is not None else 0.0

    @property
    def ratio_of_roll(self) -> 'float':
        """float: 'RatioOfRoll' is the original name of this property."""

        temp = self.wrapped.RatioOfRoll

        if temp is None:
            return 0.0

        return temp

    @ratio_of_roll.setter
    def ratio_of_roll(self, value: 'float'):
        self.wrapped.RatioOfRoll = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'BasicConicalGearMachineSettingsGenerated._Cast_BasicConicalGearMachineSettingsGenerated':
        return self._Cast_BasicConicalGearMachineSettingsGenerated(self)
