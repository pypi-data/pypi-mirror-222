﻿"""_6870.py

HarmonicLoadDataImportFromMotorPackages
"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.implicit import list_with_selected_item, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6869
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_LOAD_DATA_IMPORT_FROM_MOTOR_PACKAGES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'HarmonicLoadDataImportFromMotorPackages')

if TYPE_CHECKING:
    from mastapy.electric_machines.harmonic_load_data import _1372
    from mastapy.system_model.analyses_and_results.static_loads import _6848


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicLoadDataImportFromMotorPackages',)


T = TypeVar('T', bound='_6848.ElectricMachineHarmonicLoadImportOptionsBase')


class HarmonicLoadDataImportFromMotorPackages(_6869.HarmonicLoadDataImportBase[T]):
    """HarmonicLoadDataImportFromMotorPackages

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _HARMONIC_LOAD_DATA_IMPORT_FROM_MOTOR_PACKAGES

    class _Cast_HarmonicLoadDataImportFromMotorPackages:
        """Special nested class for casting HarmonicLoadDataImportFromMotorPackages to subclasses."""

        def __init__(self, parent: 'HarmonicLoadDataImportFromMotorPackages'):
            self._parent = parent

        @property
        def harmonic_load_data_import_base(self):
            return self._parent._cast(_6869.HarmonicLoadDataImportBase)

        @property
        def harmonic_load_data_csv_import(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6866
            
            return self._parent._cast(_6866.HarmonicLoadDataCSVImport)

        @property
        def harmonic_load_data_flux_import(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6868
            
            return self._parent._cast(_6868.HarmonicLoadDataFluxImport)

        @property
        def harmonic_load_data_jmag_import(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6871
            
            return self._parent._cast(_6871.HarmonicLoadDataJMAGImport)

        @property
        def harmonic_load_data_motor_cad_import(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6872
            
            return self._parent._cast(_6872.HarmonicLoadDataMotorCADImport)

        @property
        def harmonic_load_data_import_from_motor_packages(self) -> 'HarmonicLoadDataImportFromMotorPackages':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HarmonicLoadDataImportFromMotorPackages.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_slice_number(self) -> 'list_with_selected_item.ListWithSelectedItem_int':
        """list_with_selected_item.ListWithSelectedItem_int: 'AxialSliceNumber' is the original name of this property."""

        temp = self.wrapped.AxialSliceNumber

        if temp is None:
            return 0

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_int')(temp) if temp is not None else 0

    @axial_slice_number.setter
    def axial_slice_number(self, value: 'list_with_selected_item.ListWithSelectedItem_int.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_int.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_int.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0)
        self.wrapped.AxialSliceNumber = value

    @property
    def data_type(self) -> 'enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType':
        """enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType: 'DataType' is the original name of this property."""

        temp = self.wrapped.DataType

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @data_type.setter
    def data_type(self, value: 'enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DataType = value

    @property
    def speed(self) -> 'list_with_selected_item.ListWithSelectedItem_float':
        """list_with_selected_item.ListWithSelectedItem_float: 'Speed' is the original name of this property."""

        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_float')(temp) if temp is not None else 0.0

    @speed.setter
    def speed(self, value: 'list_with_selected_item.ListWithSelectedItem_float.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_float.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0)
        self.wrapped.Speed = value

    @property
    def cast_to(self) -> 'HarmonicLoadDataImportFromMotorPackages._Cast_HarmonicLoadDataImportFromMotorPackages':
        return self._Cast_HarmonicLoadDataImportFromMotorPackages(self)
