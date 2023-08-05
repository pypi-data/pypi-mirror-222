"""_5715.py

ElectricMachineStatorToothTangentialLoadsExcitationDetail
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5712
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_STATOR_TOOTH_TANGENTIAL_LOADS_EXCITATION_DETAIL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'ElectricMachineStatorToothTangentialLoadsExcitationDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineStatorToothTangentialLoadsExcitationDetail',)


class ElectricMachineStatorToothTangentialLoadsExcitationDetail(_5712.ElectricMachineStatorToothLoadsExcitationDetail):
    """ElectricMachineStatorToothTangentialLoadsExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_STATOR_TOOTH_TANGENTIAL_LOADS_EXCITATION_DETAIL

    class _Cast_ElectricMachineStatorToothTangentialLoadsExcitationDetail:
        """Special nested class for casting ElectricMachineStatorToothTangentialLoadsExcitationDetail to subclasses."""

        def __init__(self, parent: 'ElectricMachineStatorToothTangentialLoadsExcitationDetail'):
            self._parent = parent

        @property
        def electric_machine_stator_tooth_loads_excitation_detail(self):
            return self._parent._cast(_5712.ElectricMachineStatorToothLoadsExcitationDetail)

        @property
        def electric_machine_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5705
            
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
        def electric_machine_stator_tooth_tangential_loads_excitation_detail(self) -> 'ElectricMachineStatorToothTangentialLoadsExcitationDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineStatorToothTangentialLoadsExcitationDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElectricMachineStatorToothTangentialLoadsExcitationDetail._Cast_ElectricMachineStatorToothTangentialLoadsExcitationDetail':
        return self._Cast_ElectricMachineStatorToothTangentialLoadsExcitationDetail(self)
