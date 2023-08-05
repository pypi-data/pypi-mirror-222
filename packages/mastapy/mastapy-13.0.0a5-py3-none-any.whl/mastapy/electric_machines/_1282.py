"""_1282.py

PermanentMagnetRotor
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.electric_machines import _1285
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PERMANENT_MAGNET_ROTOR = python_net_import('SMT.MastaAPI.ElectricMachines', 'PermanentMagnetRotor')


__docformat__ = 'restructuredtext en'
__all__ = ('PermanentMagnetRotor',)


class PermanentMagnetRotor(_1285.Rotor):
    """PermanentMagnetRotor

    This is a mastapy class.
    """

    TYPE = _PERMANENT_MAGNET_ROTOR

    class _Cast_PermanentMagnetRotor:
        """Special nested class for casting PermanentMagnetRotor to subclasses."""

        def __init__(self, parent: 'PermanentMagnetRotor'):
            self._parent = parent

        @property
        def rotor(self):
            return self._parent._cast(_1285.Rotor)

        @property
        def interior_permanent_magnet_and_synchronous_reluctance_rotor(self):
            from mastapy.electric_machines import _1269
            
            return self._parent._cast(_1269.InteriorPermanentMagnetAndSynchronousReluctanceRotor)

        @property
        def surface_permanent_magnet_rotor(self):
            from mastapy.electric_machines import _1296
            
            return self._parent._cast(_1296.SurfacePermanentMagnetRotor)

        @property
        def permanent_magnet_rotor(self) -> 'PermanentMagnetRotor':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PermanentMagnetRotor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PermanentMagnetRotor._Cast_PermanentMagnetRotor':
        return self._Cast_PermanentMagnetRotor(self)
