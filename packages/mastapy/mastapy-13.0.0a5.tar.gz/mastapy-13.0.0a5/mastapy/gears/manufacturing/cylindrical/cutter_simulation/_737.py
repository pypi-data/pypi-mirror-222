"""_737.py

HobSimulationCalculator
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _740
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HOB_SIMULATION_CALCULATOR = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation', 'HobSimulationCalculator')

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _722


__docformat__ = 'restructuredtext en'
__all__ = ('HobSimulationCalculator',)


class HobSimulationCalculator(_740.RackSimulationCalculator):
    """HobSimulationCalculator

    This is a mastapy class.
    """

    TYPE = _HOB_SIMULATION_CALCULATOR

    class _Cast_HobSimulationCalculator:
        """Special nested class for casting HobSimulationCalculator to subclasses."""

        def __init__(self, parent: 'HobSimulationCalculator'):
            self._parent = parent

        @property
        def rack_simulation_calculator(self):
            return self._parent._cast(_740.RackSimulationCalculator)

        @property
        def cutter_simulation_calc(self):
            from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _728
            
            return self._parent._cast(_728.CutterSimulationCalc)

        @property
        def hob_simulation_calculator(self) -> 'HobSimulationCalculator':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HobSimulationCalculator.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hob(self) -> '_722.CylindricalGearHobShape':
        """CylindricalGearHobShape: 'Hob' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Hob

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'HobSimulationCalculator._Cast_HobSimulationCalculator':
        return self._Cast_HobSimulationCalculator(self)
