"""_6872.py

HarmonicLoadDataMotorCADImport
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6870, _6850
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_LOAD_DATA_MOTOR_CAD_IMPORT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'HarmonicLoadDataMotorCADImport')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicLoadDataMotorCADImport',)


class HarmonicLoadDataMotorCADImport(_6870.HarmonicLoadDataImportFromMotorPackages['_6850.ElectricMachineHarmonicLoadMotorCADImportOptions']):
    """HarmonicLoadDataMotorCADImport

    This is a mastapy class.
    """

    TYPE = _HARMONIC_LOAD_DATA_MOTOR_CAD_IMPORT

    class _Cast_HarmonicLoadDataMotorCADImport:
        """Special nested class for casting HarmonicLoadDataMotorCADImport to subclasses."""

        def __init__(self, parent: 'HarmonicLoadDataMotorCADImport'):
            self._parent = parent

        @property
        def harmonic_load_data_import_from_motor_packages(self):
            return self._parent._cast(_6870.HarmonicLoadDataImportFromMotorPackages)

        @property
        def harmonic_load_data_import_base(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6869
            
            return self._parent._cast(_6869.HarmonicLoadDataImportBase)

        @property
        def harmonic_load_data_motor_cad_import(self) -> 'HarmonicLoadDataMotorCADImport':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HarmonicLoadDataMotorCADImport.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def derive_rotor_forces_from_stator_loads(self) -> 'bool':
        """bool: 'DeriveRotorForcesFromStatorLoads' is the original name of this property."""

        temp = self.wrapped.DeriveRotorForcesFromStatorLoads

        if temp is None:
            return False

        return temp

    @derive_rotor_forces_from_stator_loads.setter
    def derive_rotor_forces_from_stator_loads(self, value: 'bool'):
        self.wrapped.DeriveRotorForcesFromStatorLoads = bool(value) if value is not None else False

    def select_motor_cad_file(self):
        """ 'SelectMotorCADFile' is the original name of this method."""

        self.wrapped.SelectMotorCADFile()

    @property
    def cast_to(self) -> 'HarmonicLoadDataMotorCADImport._Cast_HarmonicLoadDataMotorCADImport':
        return self._Cast_HarmonicLoadDataMotorCADImport(self)
