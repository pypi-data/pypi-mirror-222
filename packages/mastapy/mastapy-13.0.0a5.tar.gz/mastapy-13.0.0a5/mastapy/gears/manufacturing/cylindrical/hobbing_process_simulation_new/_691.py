"""_691.py

WormGrindingProcessCalculation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _677
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_PROCESS_CALCULATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'WormGrindingProcessCalculation')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGrindingProcessCalculation',)


class WormGrindingProcessCalculation(_677.ProcessCalculation):
    """WormGrindingProcessCalculation

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_PROCESS_CALCULATION

    class _Cast_WormGrindingProcessCalculation:
        """Special nested class for casting WormGrindingProcessCalculation to subclasses."""

        def __init__(self, parent: 'WormGrindingProcessCalculation'):
            self._parent = parent

        @property
        def process_calculation(self):
            return self._parent._cast(_677.ProcessCalculation)

        @property
        def worm_grinding_cutter_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _689
            
            return self._parent._cast(_689.WormGrindingCutterCalculation)

        @property
        def worm_grinding_lead_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _690
            
            return self._parent._cast(_690.WormGrindingLeadCalculation)

        @property
        def worm_grinding_process_gear_shape(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _692
            
            return self._parent._cast(_692.WormGrindingProcessGearShape)

        @property
        def worm_grinding_process_mark_on_shaft(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _693
            
            return self._parent._cast(_693.WormGrindingProcessMarkOnShaft)

        @property
        def worm_grinding_process_pitch_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _694
            
            return self._parent._cast(_694.WormGrindingProcessPitchCalculation)

        @property
        def worm_grinding_process_profile_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _695
            
            return self._parent._cast(_695.WormGrindingProcessProfileCalculation)

        @property
        def worm_grinding_process_total_modification_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _699
            
            return self._parent._cast(_699.WormGrindingProcessTotalModificationCalculation)

        @property
        def worm_grinding_process_calculation(self) -> 'WormGrindingProcessCalculation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGrindingProcessCalculation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation':
        return self._Cast_WormGrindingProcessCalculation(self)
