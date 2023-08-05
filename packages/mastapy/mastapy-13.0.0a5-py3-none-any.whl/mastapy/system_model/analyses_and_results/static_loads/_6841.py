"""_6841.py

ElectricMachineHarmonicLoadDataFromFlux
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.analyses_and_results.static_loads import _6845, _6847
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_FLUX = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ElectricMachineHarmonicLoadDataFromFlux')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineHarmonicLoadDataFromFlux',)


class ElectricMachineHarmonicLoadDataFromFlux(_6845.ElectricMachineHarmonicLoadDataFromMotorPackages['_6847.ElectricMachineHarmonicLoadFluxImportOptions']):
    """ElectricMachineHarmonicLoadDataFromFlux

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_FLUX

    class _Cast_ElectricMachineHarmonicLoadDataFromFlux:
        """Special nested class for casting ElectricMachineHarmonicLoadDataFromFlux to subclasses."""

        def __init__(self, parent: 'ElectricMachineHarmonicLoadDataFromFlux'):
            self._parent = parent

        @property
        def electric_machine_harmonic_load_data_from_motor_packages(self):
            return self._parent._cast(_6845.ElectricMachineHarmonicLoadDataFromMotorPackages)

        @property
        def electric_machine_harmonic_load_data(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6839
            
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
        def electric_machine_harmonic_load_data_from_flux(self) -> 'ElectricMachineHarmonicLoadDataFromFlux':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineHarmonicLoadDataFromFlux.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElectricMachineHarmonicLoadDataFromFlux._Cast_ElectricMachineHarmonicLoadDataFromFlux':
        return self._Cast_ElectricMachineHarmonicLoadDataFromFlux(self)
