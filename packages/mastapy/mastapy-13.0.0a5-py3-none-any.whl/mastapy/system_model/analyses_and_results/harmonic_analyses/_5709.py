﻿"""_5709.py

ElectricMachineRotorYMomentPeriodicExcitationDetail
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5705
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_ROTOR_Y_MOMENT_PERIODIC_EXCITATION_DETAIL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'ElectricMachineRotorYMomentPeriodicExcitationDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineRotorYMomentPeriodicExcitationDetail',)


class ElectricMachineRotorYMomentPeriodicExcitationDetail(_5705.ElectricMachinePeriodicExcitationDetail):
    """ElectricMachineRotorYMomentPeriodicExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_ROTOR_Y_MOMENT_PERIODIC_EXCITATION_DETAIL

    class _Cast_ElectricMachineRotorYMomentPeriodicExcitationDetail:
        """Special nested class for casting ElectricMachineRotorYMomentPeriodicExcitationDetail to subclasses."""

        def __init__(self, parent: 'ElectricMachineRotorYMomentPeriodicExcitationDetail'):
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
        def electric_machine_rotor_y_moment_periodic_excitation_detail(self) -> 'ElectricMachineRotorYMomentPeriodicExcitationDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineRotorYMomentPeriodicExcitationDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElectricMachineRotorYMomentPeriodicExcitationDetail._Cast_ElectricMachineRotorYMomentPeriodicExcitationDetail':
        return self._Cast_ElectricMachineRotorYMomentPeriodicExcitationDetail(self)
