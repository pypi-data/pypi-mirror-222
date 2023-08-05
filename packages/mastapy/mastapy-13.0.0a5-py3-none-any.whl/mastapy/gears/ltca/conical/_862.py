﻿"""_862.py

ConicalGearContactStiffness
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.ltca import _832
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_CONTACT_STIFFNESS = python_net_import('SMT.MastaAPI.Gears.LTCA.Conical', 'ConicalGearContactStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearContactStiffness',)


class ConicalGearContactStiffness(_832.GearContactStiffness):
    """ConicalGearContactStiffness

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_CONTACT_STIFFNESS

    class _Cast_ConicalGearContactStiffness:
        """Special nested class for casting ConicalGearContactStiffness to subclasses."""

        def __init__(self, parent: 'ConicalGearContactStiffness'):
            self._parent = parent

        @property
        def gear_contact_stiffness(self):
            return self._parent._cast(_832.GearContactStiffness)

        @property
        def gear_stiffness(self):
            from mastapy.gears.ltca import _844
            
            return self._parent._cast(_844.GearStiffness)

        @property
        def fe_stiffness(self):
            from mastapy.nodal_analysis import _66
            
            return self._parent._cast(_66.FEStiffness)

        @property
        def conical_gear_contact_stiffness(self) -> 'ConicalGearContactStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearContactStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalGearContactStiffness._Cast_ConicalGearContactStiffness':
        return self._Cast_ConicalGearContactStiffness(self)
