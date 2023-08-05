﻿"""_5707.py

ElectricMachineRotorXMomentPeriodicExcitationDetail
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5705
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_ROTOR_X_MOMENT_PERIODIC_EXCITATION_DETAIL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'ElectricMachineRotorXMomentPeriodicExcitationDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineRotorXMomentPeriodicExcitationDetail',)


class ElectricMachineRotorXMomentPeriodicExcitationDetail(_5705.ElectricMachinePeriodicExcitationDetail):
    """ElectricMachineRotorXMomentPeriodicExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_ROTOR_X_MOMENT_PERIODIC_EXCITATION_DETAIL

    class _Cast_ElectricMachineRotorXMomentPeriodicExcitationDetail:
        """Special nested class for casting ElectricMachineRotorXMomentPeriodicExcitationDetail to subclasses."""

        def __init__(self, parent: 'ElectricMachineRotorXMomentPeriodicExcitationDetail'):
            self._parent = parent

        @property
        def electric_machine_periodic_excitation_detail(self):
            return self._parent._cast(_5705.ElectricMachinePeriodicExcitationDetail)

        @property
        def periodic_excitation_with_reference_shaft(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5762
            
            return self._parent._cast(_5762.PeriodicExcitationWithReferenceShaft)

        @property
        def abstract_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5652
            
            return self._parent._cast(_5652.AbstractPeriodicExcitationDetail)

        @property
        def electric_machine_rotor_x_moment_periodic_excitation_detail(self) -> 'ElectricMachineRotorXMomentPeriodicExcitationDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineRotorXMomentPeriodicExcitationDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElectricMachineRotorXMomentPeriodicExcitationDetail._Cast_ElectricMachineRotorXMomentPeriodicExcitationDetail':
        return self._Cast_ElectricMachineRotorXMomentPeriodicExcitationDetail(self)
