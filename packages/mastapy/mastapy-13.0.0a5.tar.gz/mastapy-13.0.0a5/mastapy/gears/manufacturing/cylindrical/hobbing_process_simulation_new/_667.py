"""_667.py

HobbingProcessPitchCalculation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _663
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HOBBING_PROCESS_PITCH_CALCULATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'HobbingProcessPitchCalculation')

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1854
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _658


__docformat__ = 'restructuredtext en'
__all__ = ('HobbingProcessPitchCalculation',)


class HobbingProcessPitchCalculation(_663.HobbingProcessCalculation):
    """HobbingProcessPitchCalculation

    This is a mastapy class.
    """

    TYPE = _HOBBING_PROCESS_PITCH_CALCULATION

    class _Cast_HobbingProcessPitchCalculation:
        """Special nested class for casting HobbingProcessPitchCalculation to subclasses."""

        def __init__(self, parent: 'HobbingProcessPitchCalculation'):
            self._parent = parent

        @property
        def hobbing_process_calculation(self):
            return self._parent._cast(_663.HobbingProcessCalculation)

        @property
        def process_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _677
            
            return self._parent._cast(_677.ProcessCalculation)

        @property
        def hobbing_process_pitch_calculation(self) -> 'HobbingProcessPitchCalculation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HobbingProcessPitchCalculation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pitch_modification_chart(self) -> '_1854.TwoDChartDefinition':
        """TwoDChartDefinition: 'PitchModificationChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PitchModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def result_z_plane(self) -> 'float':
        """float: 'ResultZPlane' is the original name of this property."""

        temp = self.wrapped.ResultZPlane

        if temp is None:
            return 0.0

        return temp

    @result_z_plane.setter
    def result_z_plane(self, value: 'float'):
        self.wrapped.ResultZPlane = float(value) if value is not None else 0.0

    @property
    def left_flank(self) -> '_658.CalculatePitchDeviationAccuracy':
        """CalculatePitchDeviationAccuracy: 'LeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_flank(self) -> '_658.CalculatePitchDeviationAccuracy':
        """CalculatePitchDeviationAccuracy: 'RightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'HobbingProcessPitchCalculation._Cast_HobbingProcessPitchCalculation':
        return self._Cast_HobbingProcessPitchCalculation(self)
