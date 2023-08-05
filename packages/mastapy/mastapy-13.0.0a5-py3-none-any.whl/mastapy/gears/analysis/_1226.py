﻿"""_1226.py

GearSetImplementationAnalysisDutyCycle
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.analysis import _1225
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_IMPLEMENTATION_ANALYSIS_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Gears.Analysis', 'GearSetImplementationAnalysisDutyCycle')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetImplementationAnalysisDutyCycle',)


class GearSetImplementationAnalysisDutyCycle(_1225.GearSetImplementationAnalysisAbstract):
    """GearSetImplementationAnalysisDutyCycle

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_IMPLEMENTATION_ANALYSIS_DUTY_CYCLE

    class _Cast_GearSetImplementationAnalysisDutyCycle:
        """Special nested class for casting GearSetImplementationAnalysisDutyCycle to subclasses."""

        def __init__(self, parent: 'GearSetImplementationAnalysisDutyCycle'):
            self._parent = parent

        @property
        def gear_set_implementation_analysis_abstract(self):
            return self._parent._cast(_1225.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_design_analysis(self):
            from mastapy.gears.analysis import _1222
            
            return self._parent._cast(_1222.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1213
            
            return self._parent._cast(_1213.AbstractGearSetAnalysis)

        @property
        def cylindrical_manufactured_gear_set_duty_cycle(self):
            from mastapy.gears.manufacturing.cylindrical import _617
            
            return self._parent._cast(_617.CylindricalManufacturedGearSetDutyCycle)

        @property
        def cylindrical_gear_set_micro_geometry_duty_cycle(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1104
            
            return self._parent._cast(_1104.CylindricalGearSetMicroGeometryDutyCycle)

        @property
        def gear_set_implementation_analysis_duty_cycle(self) -> 'GearSetImplementationAnalysisDutyCycle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetImplementationAnalysisDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duty_cycle_name(self) -> 'str':
        """str: 'DutyCycleName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DutyCycleName

        if temp is None:
            return ''

        return temp

    @property
    def cast_to(self) -> 'GearSetImplementationAnalysisDutyCycle._Cast_GearSetImplementationAnalysisDutyCycle':
        return self._Cast_GearSetImplementationAnalysisDutyCycle(self)
