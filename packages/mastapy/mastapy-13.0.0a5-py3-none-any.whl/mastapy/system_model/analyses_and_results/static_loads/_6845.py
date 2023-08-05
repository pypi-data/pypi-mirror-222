"""_6845.py

ElectricMachineHarmonicLoadDataFromMotorPackages
"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy.system_model.analyses_and_results.static_loads import _6839
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_MOTOR_PACKAGES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ElectricMachineHarmonicLoadDataFromMotorPackages')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6848


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineHarmonicLoadDataFromMotorPackages',)


T = TypeVar('T', bound='_6848.ElectricMachineHarmonicLoadImportOptionsBase')


class ElectricMachineHarmonicLoadDataFromMotorPackages(_6839.ElectricMachineHarmonicLoadData, Generic[T]):
    """ElectricMachineHarmonicLoadDataFromMotorPackages

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_MOTOR_PACKAGES

    class _Cast_ElectricMachineHarmonicLoadDataFromMotorPackages:
        """Special nested class for casting ElectricMachineHarmonicLoadDataFromMotorPackages to subclasses."""

        def __init__(self, parent: 'ElectricMachineHarmonicLoadDataFromMotorPackages'):
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
        def electric_machine_harmonic_load_data_from_flux(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6841
            
            return self._parent._cast(_6841.ElectricMachineHarmonicLoadDataFromFlux)

        @property
        def electric_machine_harmonic_load_data_from_jmag(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6842
            
            return self._parent._cast(_6842.ElectricMachineHarmonicLoadDataFromJMAG)

        @property
        def electric_machine_harmonic_load_data_from_motor_cad(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6844
            
            return self._parent._cast(_6844.ElectricMachineHarmonicLoadDataFromMotorCAD)

        @property
        def electric_machine_harmonic_load_data_from_motor_packages(self) -> 'ElectricMachineHarmonicLoadDataFromMotorPackages':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineHarmonicLoadDataFromMotorPackages.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElectricMachineHarmonicLoadDataFromMotorPackages._Cast_ElectricMachineHarmonicLoadDataFromMotorPackages':
        return self._Cast_ElectricMachineHarmonicLoadDataFromMotorPackages(self)
