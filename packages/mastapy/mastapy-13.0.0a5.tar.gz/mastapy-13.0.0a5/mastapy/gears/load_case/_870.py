"""_870.py

GearLoadCaseBase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.analysis import _1214
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_LOAD_CASE_BASE = python_net_import('SMT.MastaAPI.Gears.LoadCase', 'GearLoadCaseBase')


__docformat__ = 'restructuredtext en'
__all__ = ('GearLoadCaseBase',)


class GearLoadCaseBase(_1214.GearDesignAnalysis):
    """GearLoadCaseBase

    This is a mastapy class.
    """

    TYPE = _GEAR_LOAD_CASE_BASE

    class _Cast_GearLoadCaseBase:
        """Special nested class for casting GearLoadCaseBase to subclasses."""

        def __init__(self, parent: 'GearLoadCaseBase'):
            self._parent = parent

        @property
        def gear_design_analysis(self):
            return self._parent._cast(_1214.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearAnalysis)

        @property
        def worm_gear_load_case(self):
            from mastapy.gears.load_case.worm import _873
            
            return self._parent._cast(_873.WormGearLoadCase)

        @property
        def face_gear_load_case(self):
            from mastapy.gears.load_case.face import _876
            
            return self._parent._cast(_876.FaceGearLoadCase)

        @property
        def cylindrical_gear_load_case(self):
            from mastapy.gears.load_case.cylindrical import _879
            
            return self._parent._cast(_879.CylindricalGearLoadCase)

        @property
        def conical_gear_load_case(self):
            from mastapy.gears.load_case.conical import _882
            
            return self._parent._cast(_882.ConicalGearLoadCase)

        @property
        def concept_gear_load_case(self):
            from mastapy.gears.load_case.concept import _885
            
            return self._parent._cast(_885.ConceptGearLoadCase)

        @property
        def bevel_load_case(self):
            from mastapy.gears.load_case.bevel import _888
            
            return self._parent._cast(_888.BevelLoadCase)

        @property
        def gear_load_case_base(self) -> 'GearLoadCaseBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearLoadCaseBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duration(self) -> 'float':
        """float: 'Duration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Duration

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_temperature(self) -> 'float':
        """float: 'GearTemperature' is the original name of this property."""

        temp = self.wrapped.GearTemperature

        if temp is None:
            return 0.0

        return temp

    @gear_temperature.setter
    def gear_temperature(self, value: 'float'):
        self.wrapped.GearTemperature = float(value) if value is not None else 0.0

    @property
    def sump_temperature(self) -> 'float':
        """float: 'SumpTemperature' is the original name of this property."""

        temp = self.wrapped.SumpTemperature

        if temp is None:
            return 0.0

        return temp

    @sump_temperature.setter
    def sump_temperature(self, value: 'float'):
        self.wrapped.SumpTemperature = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'GearLoadCaseBase._Cast_GearLoadCaseBase':
        return self._Cast_GearLoadCaseBase(self)
