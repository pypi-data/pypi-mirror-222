"""_1373.py

SpeedDependentHarmonicLoadData
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.electric_machines.harmonic_load_data import _1370
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPEED_DEPENDENT_HARMONIC_LOAD_DATA = python_net_import('SMT.MastaAPI.ElectricMachines.HarmonicLoadData', 'SpeedDependentHarmonicLoadData')


__docformat__ = 'restructuredtext en'
__all__ = ('SpeedDependentHarmonicLoadData',)


class SpeedDependentHarmonicLoadData(_1370.HarmonicLoadDataBase):
    """SpeedDependentHarmonicLoadData

    This is a mastapy class.
    """

    TYPE = _SPEED_DEPENDENT_HARMONIC_LOAD_DATA

    class _Cast_SpeedDependentHarmonicLoadData:
        """Special nested class for casting SpeedDependentHarmonicLoadData to subclasses."""

        def __init__(self, parent: 'SpeedDependentHarmonicLoadData'):
            self._parent = parent

        @property
        def harmonic_load_data_base(self):
            return self._parent._cast(_1370.HarmonicLoadDataBase)

        @property
        def dynamic_force_results(self):
            from mastapy.electric_machines.results import _1312
            
            return self._parent._cast(_1312.DynamicForceResults)

        @property
        def electric_machine_harmonic_load_data_base(self):
            from mastapy.electric_machines.harmonic_load_data import _1368
            
            return self._parent._cast(_1368.ElectricMachineHarmonicLoadDataBase)

        @property
        def electric_machine_harmonic_load_data(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6839
            
            return self._parent._cast(_6839.ElectricMachineHarmonicLoadData)

        @property
        def electric_machine_harmonic_load_data_from_excel(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6840
            
            return self._parent._cast(_6840.ElectricMachineHarmonicLoadDataFromExcel)

        @property
        def electric_machine_harmonic_load_data_from_flux(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6841
            
            return self._parent._cast(_6841.ElectricMachineHarmonicLoadDataFromFlux)

        @property
        def electric_machine_harmonic_load_data_from_jmag(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6842
            
            return self._parent._cast(_6842.ElectricMachineHarmonicLoadDataFromJMAG)

        @property
        def electric_machine_harmonic_load_data_from_masta(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6843
            
            return self._parent._cast(_6843.ElectricMachineHarmonicLoadDataFromMASTA)

        @property
        def electric_machine_harmonic_load_data_from_motor_cad(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6844
            
            return self._parent._cast(_6844.ElectricMachineHarmonicLoadDataFromMotorCAD)

        @property
        def electric_machine_harmonic_load_data_from_motor_packages(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6845
            
            return self._parent._cast(_6845.ElectricMachineHarmonicLoadDataFromMotorPackages)

        @property
        def point_load_harmonic_load_data(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6905
            
            return self._parent._cast(_6905.PointLoadHarmonicLoadData)

        @property
        def unbalanced_mass_harmonic_load_data(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6947
            
            return self._parent._cast(_6947.UnbalancedMassHarmonicLoadData)

        @property
        def speed_dependent_harmonic_load_data(self) -> 'SpeedDependentHarmonicLoadData':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpeedDependentHarmonicLoadData.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def selected_speed(self) -> 'list_with_selected_item.ListWithSelectedItem_float':
        """list_with_selected_item.ListWithSelectedItem_float: 'SelectedSpeed' is the original name of this property."""

        temp = self.wrapped.SelectedSpeed

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_float')(temp) if temp is not None else 0.0

    @selected_speed.setter
    def selected_speed(self, value: 'list_with_selected_item.ListWithSelectedItem_float.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_float.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0)
        self.wrapped.SelectedSpeed = value

    @property
    def show_all_speeds(self) -> 'bool':
        """bool: 'ShowAllSpeeds' is the original name of this property."""

        temp = self.wrapped.ShowAllSpeeds

        if temp is None:
            return False

        return temp

    @show_all_speeds.setter
    def show_all_speeds(self, value: 'bool'):
        self.wrapped.ShowAllSpeeds = bool(value) if value is not None else False

    @property
    def cast_to(self) -> 'SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData':
        return self._Cast_SpeedDependentHarmonicLoadData(self)
