"""_806.py

PinionMachineSettingsSMT
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.manufacturing.bevel import _803
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PINION_MACHINE_SETTINGS_SMT = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'PinionMachineSettingsSMT')


__docformat__ = 'restructuredtext en'
__all__ = ('PinionMachineSettingsSMT',)


class PinionMachineSettingsSMT(_803.PinionFinishMachineSettings):
    """PinionMachineSettingsSMT

    This is a mastapy class.
    """

    TYPE = _PINION_MACHINE_SETTINGS_SMT

    class _Cast_PinionMachineSettingsSMT:
        """Special nested class for casting PinionMachineSettingsSMT to subclasses."""

        def __init__(self, parent: 'PinionMachineSettingsSMT'):
            self._parent = parent

        @property
        def pinion_finish_machine_settings(self):
            return self._parent._cast(_803.PinionFinishMachineSettings)

        @property
        def conical_gear_tooth_surface(self):
            from mastapy.gears import _318
            
            return self._parent._cast(_318.ConicalGearToothSurface)

        @property
        def pinion_machine_settings_smt(self) -> 'PinionMachineSettingsSMT':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PinionMachineSettingsSMT.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PinionMachineSettingsSMT._Cast_PinionMachineSettingsSMT':
        return self._Cast_PinionMachineSettingsSMT(self)
