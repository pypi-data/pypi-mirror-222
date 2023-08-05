﻿"""_697.py

WormGrindingProcessSimulationNew
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _683, _696
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_PROCESS_SIMULATION_NEW = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'WormGrindingProcessSimulationNew')

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _689, _692, _690, _693,
        _694, _695, _699
    )


__docformat__ = 'restructuredtext en'
__all__ = ('WormGrindingProcessSimulationNew',)


class WormGrindingProcessSimulationNew(_683.ProcessSimulationNew['_696.WormGrindingProcessSimulationInput']):
    """WormGrindingProcessSimulationNew

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_PROCESS_SIMULATION_NEW

    class _Cast_WormGrindingProcessSimulationNew:
        """Special nested class for casting WormGrindingProcessSimulationNew to subclasses."""

        def __init__(self, parent: 'WormGrindingProcessSimulationNew'):
            self._parent = parent

        @property
        def process_simulation_new(self):
            return self._parent._cast(_683.ProcessSimulationNew)

        @property
        def worm_grinding_process_simulation_new(self) -> 'WormGrindingProcessSimulationNew':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGrindingProcessSimulationNew.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def worm_grinding_cutter_calculation(self) -> '_689.WormGrindingCutterCalculation':
        """WormGrindingCutterCalculation: 'WormGrindingCutterCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGrindingCutterCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_grinding_process_gear_shape_calculation(self) -> '_692.WormGrindingProcessGearShape':
        """WormGrindingProcessGearShape: 'WormGrindingProcessGearShapeCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGrindingProcessGearShapeCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_grinding_process_lead_calculation(self) -> '_690.WormGrindingLeadCalculation':
        """WormGrindingLeadCalculation: 'WormGrindingProcessLeadCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGrindingProcessLeadCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_grinding_process_mark_on_shaft_calculation(self) -> '_693.WormGrindingProcessMarkOnShaft':
        """WormGrindingProcessMarkOnShaft: 'WormGrindingProcessMarkOnShaftCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGrindingProcessMarkOnShaftCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_grinding_process_pitch_calculation(self) -> '_694.WormGrindingProcessPitchCalculation':
        """WormGrindingProcessPitchCalculation: 'WormGrindingProcessPitchCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGrindingProcessPitchCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_grinding_process_profile_calculation(self) -> '_695.WormGrindingProcessProfileCalculation':
        """WormGrindingProcessProfileCalculation: 'WormGrindingProcessProfileCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGrindingProcessProfileCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_grinding_process_total_modification_calculation(self) -> '_699.WormGrindingProcessTotalModificationCalculation':
        """WormGrindingProcessTotalModificationCalculation: 'WormGrindingProcessTotalModificationCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGrindingProcessTotalModificationCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'WormGrindingProcessSimulationNew._Cast_WormGrindingProcessSimulationNew':
        return self._Cast_WormGrindingProcessSimulationNew(self)
