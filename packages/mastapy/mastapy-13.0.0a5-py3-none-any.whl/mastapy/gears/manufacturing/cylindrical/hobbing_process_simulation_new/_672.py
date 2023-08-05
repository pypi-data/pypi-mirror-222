"""_672.py

HobbingProcessTotalModificationCalculation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _663
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HOBBING_PROCESS_TOTAL_MODIFICATION_CALCULATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'HobbingProcessTotalModificationCalculation')

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1852


__docformat__ = 'restructuredtext en'
__all__ = ('HobbingProcessTotalModificationCalculation',)


class HobbingProcessTotalModificationCalculation(_663.HobbingProcessCalculation):
    """HobbingProcessTotalModificationCalculation

    This is a mastapy class.
    """

    TYPE = _HOBBING_PROCESS_TOTAL_MODIFICATION_CALCULATION

    class _Cast_HobbingProcessTotalModificationCalculation:
        """Special nested class for casting HobbingProcessTotalModificationCalculation to subclasses."""

        def __init__(self, parent: 'HobbingProcessTotalModificationCalculation'):
            self._parent = parent

        @property
        def hobbing_process_calculation(self):
            return self._parent._cast(_663.HobbingProcessCalculation)

        @property
        def process_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _677
            
            return self._parent._cast(_677.ProcessCalculation)

        @property
        def hobbing_process_total_modification_calculation(self) -> 'HobbingProcessTotalModificationCalculation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HobbingProcessTotalModificationCalculation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def lead_range_max(self) -> 'float':
        """float: 'LeadRangeMax' is the original name of this property."""

        temp = self.wrapped.LeadRangeMax

        if temp is None:
            return 0.0

        return temp

    @lead_range_max.setter
    def lead_range_max(self, value: 'float'):
        self.wrapped.LeadRangeMax = float(value) if value is not None else 0.0

    @property
    def lead_range_min(self) -> 'float':
        """float: 'LeadRangeMin' is the original name of this property."""

        temp = self.wrapped.LeadRangeMin

        if temp is None:
            return 0.0

        return temp

    @lead_range_min.setter
    def lead_range_min(self, value: 'float'):
        self.wrapped.LeadRangeMin = float(value) if value is not None else 0.0

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
    def total_errors_chart_left_flank(self) -> '_1852.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'TotalErrorsChartLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalErrorsChartLeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def total_errors_chart_right_flank(self) -> '_1852.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'TotalErrorsChartRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalErrorsChartRightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'HobbingProcessTotalModificationCalculation._Cast_HobbingProcessTotalModificationCalculation':
        return self._Cast_HobbingProcessTotalModificationCalculation(self)
