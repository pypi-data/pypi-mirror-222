﻿"""_690.py

WormGrindingLeadCalculation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _691
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_LEAD_CALCULATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'WormGrindingLeadCalculation')

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1854
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _657


__docformat__ = 'restructuredtext en'
__all__ = ('WormGrindingLeadCalculation',)


class WormGrindingLeadCalculation(_691.WormGrindingProcessCalculation):
    """WormGrindingLeadCalculation

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_LEAD_CALCULATION

    class _Cast_WormGrindingLeadCalculation:
        """Special nested class for casting WormGrindingLeadCalculation to subclasses."""

        def __init__(self, parent: 'WormGrindingLeadCalculation'):
            self._parent = parent

        @property
        def worm_grinding_process_calculation(self):
            return self._parent._cast(_691.WormGrindingProcessCalculation)

        @property
        def process_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _677
            
            return self._parent._cast(_677.ProcessCalculation)

        @property
        def worm_grinding_lead_calculation(self) -> 'WormGrindingLeadCalculation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGrindingLeadCalculation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def left_flank_lead_modification_chart(self) -> '_1854.TwoDChartDefinition':
        """TwoDChartDefinition: 'LeftFlankLeadModificationChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlankLeadModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def number_of_lead_bands(self) -> 'int':
        """int: 'NumberOfLeadBands' is the original name of this property."""

        temp = self.wrapped.NumberOfLeadBands

        if temp is None:
            return 0

        return temp

    @number_of_lead_bands.setter
    def number_of_lead_bands(self, value: 'int'):
        self.wrapped.NumberOfLeadBands = int(value) if value is not None else 0

    @property
    def radius_for_lead_modification_calculation(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RadiusForLeadModificationCalculation' is the original name of this property."""

        temp = self.wrapped.RadiusForLeadModificationCalculation

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @radius_for_lead_modification_calculation.setter
    def radius_for_lead_modification_calculation(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RadiusForLeadModificationCalculation = value

    @property
    def right_flank_lead_modification_chart(self) -> '_1854.TwoDChartDefinition':
        """TwoDChartDefinition: 'RightFlankLeadModificationChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlankLeadModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def left_flank(self) -> '_657.CalculateLeadDeviationAccuracy':
        """CalculateLeadDeviationAccuracy: 'LeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_flank(self) -> '_657.CalculateLeadDeviationAccuracy':
        """CalculateLeadDeviationAccuracy: 'RightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'WormGrindingLeadCalculation._Cast_WormGrindingLeadCalculation':
        return self._Cast_WormGrindingLeadCalculation(self)
