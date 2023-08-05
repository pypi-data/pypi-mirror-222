﻿"""_2568.py

CVT
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.part_model.couplings import _2558
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'CVT')


__docformat__ = 'restructuredtext en'
__all__ = ('CVT',)


class CVT(_2558.BeltDrive):
    """CVT

    This is a mastapy class.
    """

    TYPE = _CVT

    class _Cast_CVT:
        """Special nested class for casting CVT to subclasses."""

        def __init__(self, parent: 'CVT'):
            self._parent = parent

        @property
        def belt_drive(self):
            return self._parent._cast(_2558.BeltDrive)

        @property
        def specialised_assembly(self):
            from mastapy.system_model.part_model import _2459
            
            return self._parent._cast(_2459.SpecialisedAssembly)

        @property
        def abstract_assembly(self):
            from mastapy.system_model.part_model import _2417
            
            return self._parent._cast(_2417.AbstractAssembly)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2451
            
            return self._parent._cast(_2451.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2190
            
            return self._parent._cast(_2190.DesignEntity)

        @property
        def cvt(self) -> 'CVT':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVT.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def belt_loss_constant(self) -> 'float':
        """float: 'BeltLossConstant' is the original name of this property."""

        temp = self.wrapped.BeltLossConstant

        if temp is None:
            return 0.0

        return temp

    @belt_loss_constant.setter
    def belt_loss_constant(self, value: 'float'):
        self.wrapped.BeltLossConstant = float(value) if value is not None else 0.0

    @property
    def coefficient_of_static_friction_with_lubrication(self) -> 'float':
        """float: 'CoefficientOfStaticFrictionWithLubrication' is the original name of this property."""

        temp = self.wrapped.CoefficientOfStaticFrictionWithLubrication

        if temp is None:
            return 0.0

        return temp

    @coefficient_of_static_friction_with_lubrication.setter
    def coefficient_of_static_friction_with_lubrication(self, value: 'float'):
        self.wrapped.CoefficientOfStaticFrictionWithLubrication = float(value) if value is not None else 0.0

    @property
    def contact_stiffness_for_unit_length(self) -> 'float':
        """float: 'ContactStiffnessForUnitLength' is the original name of this property."""

        temp = self.wrapped.ContactStiffnessForUnitLength

        if temp is None:
            return 0.0

        return temp

    @contact_stiffness_for_unit_length.setter
    def contact_stiffness_for_unit_length(self, value: 'float'):
        self.wrapped.ContactStiffnessForUnitLength = float(value) if value is not None else 0.0

    @property
    def cross_sectional_area_of_the_pump_outlet(self) -> 'float':
        """float: 'CrossSectionalAreaOfThePumpOutlet' is the original name of this property."""

        temp = self.wrapped.CrossSectionalAreaOfThePumpOutlet

        if temp is None:
            return 0.0

        return temp

    @cross_sectional_area_of_the_pump_outlet.setter
    def cross_sectional_area_of_the_pump_outlet(self, value: 'float'):
        self.wrapped.CrossSectionalAreaOfThePumpOutlet = float(value) if value is not None else 0.0

    @property
    def pulley_sheave_angle(self) -> 'float':
        """float: 'PulleySheaveAngle' is the original name of this property."""

        temp = self.wrapped.PulleySheaveAngle

        if temp is None:
            return 0.0

        return temp

    @pulley_sheave_angle.setter
    def pulley_sheave_angle(self, value: 'float'):
        self.wrapped.PulleySheaveAngle = float(value) if value is not None else 0.0

    @property
    def pump_displacement_per_revolution(self) -> 'float':
        """float: 'PumpDisplacementPerRevolution' is the original name of this property."""

        temp = self.wrapped.PumpDisplacementPerRevolution

        if temp is None:
            return 0.0

        return temp

    @pump_displacement_per_revolution.setter
    def pump_displacement_per_revolution(self, value: 'float'):
        self.wrapped.PumpDisplacementPerRevolution = float(value) if value is not None else 0.0

    @property
    def pump_pressure_loss_constant(self) -> 'float':
        """float: 'PumpPressureLossConstant' is the original name of this property."""

        temp = self.wrapped.PumpPressureLossConstant

        if temp is None:
            return 0.0

        return temp

    @pump_pressure_loss_constant.setter
    def pump_pressure_loss_constant(self, value: 'float'):
        self.wrapped.PumpPressureLossConstant = float(value) if value is not None else 0.0

    @property
    def pump_speed_factor(self) -> 'float':
        """float: 'PumpSpeedFactor' is the original name of this property."""

        temp = self.wrapped.PumpSpeedFactor

        if temp is None:
            return 0.0

        return temp

    @pump_speed_factor.setter
    def pump_speed_factor(self, value: 'float'):
        self.wrapped.PumpSpeedFactor = float(value) if value is not None else 0.0

    @property
    def pump_speed_loss_constant(self) -> 'float':
        """float: 'PumpSpeedLossConstant' is the original name of this property."""

        temp = self.wrapped.PumpSpeedLossConstant

        if temp is None:
            return 0.0

        return temp

    @pump_speed_loss_constant.setter
    def pump_speed_loss_constant(self, value: 'float'):
        self.wrapped.PumpSpeedLossConstant = float(value) if value is not None else 0.0

    @property
    def tangential_stiffness(self) -> 'float':
        """float: 'TangentialStiffness' is the original name of this property."""

        temp = self.wrapped.TangentialStiffness

        if temp is None:
            return 0.0

        return temp

    @tangential_stiffness.setter
    def tangential_stiffness(self, value: 'float'):
        self.wrapped.TangentialStiffness = float(value) if value is not None else 0.0

    @property
    def use_improved_model(self) -> 'bool':
        """bool: 'UseImprovedModel' is the original name of this property."""

        temp = self.wrapped.UseImprovedModel

        if temp is None:
            return False

        return temp

    @use_improved_model.setter
    def use_improved_model(self, value: 'bool'):
        self.wrapped.UseImprovedModel = bool(value) if value is not None else False

    @property
    def cast_to(self) -> 'CVT._Cast_CVT':
        return self._Cast_CVT(self)
