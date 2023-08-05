"""_1270.py

InteriorPermanentMagnetMachine
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.electric_machines import _1278
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTERIOR_PERMANENT_MAGNET_MACHINE = python_net_import('SMT.MastaAPI.ElectricMachines', 'InteriorPermanentMagnetMachine')

if TYPE_CHECKING:
    from mastapy.electric_machines import _1269


__docformat__ = 'restructuredtext en'
__all__ = ('InteriorPermanentMagnetMachine',)


class InteriorPermanentMagnetMachine(_1278.NonCADElectricMachineDetail):
    """InteriorPermanentMagnetMachine

    This is a mastapy class.
    """

    TYPE = _INTERIOR_PERMANENT_MAGNET_MACHINE

    class _Cast_InteriorPermanentMagnetMachine:
        """Special nested class for casting InteriorPermanentMagnetMachine to subclasses."""

        def __init__(self, parent: 'InteriorPermanentMagnetMachine'):
            self._parent = parent

        @property
        def non_cad_electric_machine_detail(self):
            return self._parent._cast(_1278.NonCADElectricMachineDetail)

        @property
        def electric_machine_detail(self):
            from mastapy.electric_machines import _1256
            
            return self._parent._cast(_1256.ElectricMachineDetail)

        @property
        def interior_permanent_magnet_machine(self) -> 'InteriorPermanentMagnetMachine':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InteriorPermanentMagnetMachine.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotor(self) -> '_1269.InteriorPermanentMagnetAndSynchronousReluctanceRotor':
        """InteriorPermanentMagnetAndSynchronousReluctanceRotor: 'Rotor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rotor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'InteriorPermanentMagnetMachine._Cast_InteriorPermanentMagnetMachine':
        return self._Cast_InteriorPermanentMagnetMachine(self)
