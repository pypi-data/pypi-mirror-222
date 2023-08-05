﻿"""_666.py

HobbingProcessMarkOnShaft
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _663
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HOBBING_PROCESS_MARK_ON_SHAFT = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'HobbingProcessMarkOnShaft')

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1852


__docformat__ = 'restructuredtext en'
__all__ = ('HobbingProcessMarkOnShaft',)


class HobbingProcessMarkOnShaft(_663.HobbingProcessCalculation):
    """HobbingProcessMarkOnShaft

    This is a mastapy class.
    """

    TYPE = _HOBBING_PROCESS_MARK_ON_SHAFT

    class _Cast_HobbingProcessMarkOnShaft:
        """Special nested class for casting HobbingProcessMarkOnShaft to subclasses."""

        def __init__(self, parent: 'HobbingProcessMarkOnShaft'):
            self._parent = parent

        @property
        def hobbing_process_calculation(self):
            return self._parent._cast(_663.HobbingProcessCalculation)

        @property
        def process_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _677
            
            return self._parent._cast(_677.ProcessCalculation)

        @property
        def hobbing_process_mark_on_shaft(self) -> 'HobbingProcessMarkOnShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HobbingProcessMarkOnShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_profile_bands(self) -> 'int':
        """int: 'NumberOfProfileBands' is the original name of this property."""

        temp = self.wrapped.NumberOfProfileBands

        if temp is None:
            return 0

        return temp

    @number_of_profile_bands.setter
    def number_of_profile_bands(self, value: 'int'):
        self.wrapped.NumberOfProfileBands = int(value) if value is not None else 0

    @property
    def number_of_transverse_plane(self) -> 'int':
        """int: 'NumberOfTransversePlane' is the original name of this property."""

        temp = self.wrapped.NumberOfTransversePlane

        if temp is None:
            return 0

        return temp

    @number_of_transverse_plane.setter
    def number_of_transverse_plane(self, value: 'int'):
        self.wrapped.NumberOfTransversePlane = int(value) if value is not None else 0

    @property
    def shaft_diameter(self) -> 'float':
        """float: 'ShaftDiameter' is the original name of this property."""

        temp = self.wrapped.ShaftDiameter

        if temp is None:
            return 0.0

        return temp

    @shaft_diameter.setter
    def shaft_diameter(self, value: 'float'):
        self.wrapped.ShaftDiameter = float(value) if value is not None else 0.0

    @property
    def shaft_mark_chart(self) -> '_1852.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'ShaftMarkChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftMarkChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'HobbingProcessMarkOnShaft._Cast_HobbingProcessMarkOnShaft':
        return self._Cast_HobbingProcessMarkOnShaft(self)
