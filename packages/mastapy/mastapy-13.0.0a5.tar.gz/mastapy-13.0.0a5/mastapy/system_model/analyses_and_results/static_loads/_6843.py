"""_6843.py

ElectricMachineHarmonicLoadDataFromMASTA
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.analyses_and_results.static_loads import _6839
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_MASTA = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ElectricMachineHarmonicLoadDataFromMASTA')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineHarmonicLoadDataFromMASTA',)


class ElectricMachineHarmonicLoadDataFromMASTA(_6839.ElectricMachineHarmonicLoadData):
    """ElectricMachineHarmonicLoadDataFromMASTA

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_MASTA

    class _Cast_ElectricMachineHarmonicLoadDataFromMASTA:
        """Special nested class for casting ElectricMachineHarmonicLoadDataFromMASTA to subclasses."""

        def __init__(self, parent: 'ElectricMachineHarmonicLoadDataFromMASTA'):
            self._parent = parent

        @property
        def electric_machine_harmonic_load_data(self):
            return self._parent._cast(_6839.ElectricMachineHarmonicLoadData)

        @property
        def electric_machine_harmonic_load_data_base(self):
            from mastapy.electric_machines.harmonic_load_data import _1368
            
            return self._parent._cast(_1368.ElectricMachineHarmonicLoadDataBase)

        @property
        def speed_dependent_harmonic_load_data(self):
            from mastapy.electric_machines.harmonic_load_data import _1373
            
            return self._parent._cast(_1373.SpeedDependentHarmonicLoadData)

        @property
        def harmonic_load_data_base(self):
            from mastapy.electric_machines.harmonic_load_data import _1370
            
            return self._parent._cast(_1370.HarmonicLoadDataBase)

        @property
        def electric_machine_harmonic_load_data_from_masta(self) -> 'ElectricMachineHarmonicLoadDataFromMASTA':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineHarmonicLoadDataFromMASTA.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElectricMachineHarmonicLoadDataFromMASTA._Cast_ElectricMachineHarmonicLoadDataFromMASTA':
        return self._Cast_ElectricMachineHarmonicLoadDataFromMASTA(self)
