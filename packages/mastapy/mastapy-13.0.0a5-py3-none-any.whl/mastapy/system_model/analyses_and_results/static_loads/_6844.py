"""_6844.py

ElectricMachineHarmonicLoadDataFromMotorCAD
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.analyses_and_results.static_loads import _6845, _6850
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_MOTOR_CAD = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ElectricMachineHarmonicLoadDataFromMotorCAD')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineHarmonicLoadDataFromMotorCAD',)


class ElectricMachineHarmonicLoadDataFromMotorCAD(_6845.ElectricMachineHarmonicLoadDataFromMotorPackages['_6850.ElectricMachineHarmonicLoadMotorCADImportOptions']):
    """ElectricMachineHarmonicLoadDataFromMotorCAD

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_MOTOR_CAD

    class _Cast_ElectricMachineHarmonicLoadDataFromMotorCAD:
        """Special nested class for casting ElectricMachineHarmonicLoadDataFromMotorCAD to subclasses."""

        def __init__(self, parent: 'ElectricMachineHarmonicLoadDataFromMotorCAD'):
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
        def electric_machine_harmonic_load_data_from_motor_cad(self) -> 'ElectricMachineHarmonicLoadDataFromMotorCAD':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineHarmonicLoadDataFromMotorCAD.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElectricMachineHarmonicLoadDataFromMotorCAD._Cast_ElectricMachineHarmonicLoadDataFromMotorCAD':
        return self._Cast_ElectricMachineHarmonicLoadDataFromMotorCAD(self)
