﻿"""_6867.py

HarmonicLoadDataExcelImport
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.analyses_and_results.static_loads import _6869, _6846
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_LOAD_DATA_EXCEL_IMPORT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'HarmonicLoadDataExcelImport')

if TYPE_CHECKING:
    from mastapy.utility.units_and_measurements import _1601
    from mastapy.system_model.analyses_and_results.static_loads import _6893


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicLoadDataExcelImport',)


class HarmonicLoadDataExcelImport(_6869.HarmonicLoadDataImportBase['_6846.ElectricMachineHarmonicLoadExcelImportOptions']):
    """HarmonicLoadDataExcelImport

    This is a mastapy class.
    """

    TYPE = _HARMONIC_LOAD_DATA_EXCEL_IMPORT

    class _Cast_HarmonicLoadDataExcelImport:
        """Special nested class for casting HarmonicLoadDataExcelImport to subclasses."""

        def __init__(self, parent: 'HarmonicLoadDataExcelImport'):
            self._parent = parent

        @property
        def harmonic_load_data_import_base(self):
            return self._parent._cast(_6869.HarmonicLoadDataImportBase)

        @property
        def harmonic_load_data_excel_import(self) -> 'HarmonicLoadDataExcelImport':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HarmonicLoadDataExcelImport.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def column_index_of_first_data_point(self) -> 'int':
        """int: 'ColumnIndexOfFirstDataPoint' is the original name of this property."""

        temp = self.wrapped.ColumnIndexOfFirstDataPoint

        if temp is None:
            return 0

        return temp

    @column_index_of_first_data_point.setter
    def column_index_of_first_data_point(self, value: 'int'):
        self.wrapped.ColumnIndexOfFirstDataPoint = int(value) if value is not None else 0

    @property
    def column_index_of_first_speed_point(self) -> 'int':
        """int: 'ColumnIndexOfFirstSpeedPoint' is the original name of this property."""

        temp = self.wrapped.ColumnIndexOfFirstSpeedPoint

        if temp is None:
            return 0

        return temp

    @column_index_of_first_speed_point.setter
    def column_index_of_first_speed_point(self, value: 'int'):
        self.wrapped.ColumnIndexOfFirstSpeedPoint = int(value) if value is not None else 0

    @property
    def excitation_order_as_rotational_order_of_shaft(self) -> 'float':
        """float: 'ExcitationOrderAsRotationalOrderOfShaft' is the original name of this property."""

        temp = self.wrapped.ExcitationOrderAsRotationalOrderOfShaft

        if temp is None:
            return 0.0

        return temp

    @excitation_order_as_rotational_order_of_shaft.setter
    def excitation_order_as_rotational_order_of_shaft(self, value: 'float'):
        self.wrapped.ExcitationOrderAsRotationalOrderOfShaft = float(value) if value is not None else 0.0

    @property
    def number_of_speeds(self) -> 'int':
        """int: 'NumberOfSpeeds' is the original name of this property."""

        temp = self.wrapped.NumberOfSpeeds

        if temp is None:
            return 0

        return temp

    @number_of_speeds.setter
    def number_of_speeds(self, value: 'int'):
        self.wrapped.NumberOfSpeeds = int(value) if value is not None else 0

    @property
    def read_speeds_from_excel_sheet(self) -> 'bool':
        """bool: 'ReadSpeedsFromExcelSheet' is the original name of this property."""

        temp = self.wrapped.ReadSpeedsFromExcelSheet

        if temp is None:
            return False

        return temp

    @read_speeds_from_excel_sheet.setter
    def read_speeds_from_excel_sheet(self, value: 'bool'):
        self.wrapped.ReadSpeedsFromExcelSheet = bool(value) if value is not None else False

    @property
    def row_index_of_first_data_point(self) -> 'int':
        """int: 'RowIndexOfFirstDataPoint' is the original name of this property."""

        temp = self.wrapped.RowIndexOfFirstDataPoint

        if temp is None:
            return 0

        return temp

    @row_index_of_first_data_point.setter
    def row_index_of_first_data_point(self, value: 'int'):
        self.wrapped.RowIndexOfFirstDataPoint = int(value) if value is not None else 0

    @property
    def row_index_of_first_speed_point(self) -> 'int':
        """int: 'RowIndexOfFirstSpeedPoint' is the original name of this property."""

        temp = self.wrapped.RowIndexOfFirstSpeedPoint

        if temp is None:
            return 0

        return temp

    @row_index_of_first_speed_point.setter
    def row_index_of_first_speed_point(self, value: 'int'):
        self.wrapped.RowIndexOfFirstSpeedPoint = int(value) if value is not None else 0

    @property
    def row_index_of_last_data_point(self) -> 'int':
        """int: 'RowIndexOfLastDataPoint' is the original name of this property."""

        temp = self.wrapped.RowIndexOfLastDataPoint

        if temp is None:
            return 0

        return temp

    @row_index_of_last_data_point.setter
    def row_index_of_last_data_point(self, value: 'int'):
        self.wrapped.RowIndexOfLastDataPoint = int(value) if value is not None else 0

    @property
    def sheet_for_first_set_of_data(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'SheetForFirstSetOfData' is the original name of this property."""

        temp = self.wrapped.SheetForFirstSetOfData

        if temp is None:
            return ''

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_str')(temp) if temp is not None else ''

    @sheet_for_first_set_of_data.setter
    def sheet_for_first_set_of_data(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.SheetForFirstSetOfData = value

    @property
    def sheet_with_speed_data(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'SheetWithSpeedData' is the original name of this property."""

        temp = self.wrapped.SheetWithSpeedData

        if temp is None:
            return ''

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_str')(temp) if temp is not None else ''

    @sheet_with_speed_data.setter
    def sheet_with_speed_data(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.SheetWithSpeedData = value

    @property
    def speed_units(self) -> 'list_with_selected_item.ListWithSelectedItem_Unit':
        """list_with_selected_item.ListWithSelectedItem_Unit: 'SpeedUnits' is the original name of this property."""

        temp = self.wrapped.SpeedUnits

        if temp is None:
            return None

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_Unit')(temp) if temp is not None else None

    @speed_units.setter
    def speed_units(self, value: 'list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.SpeedUnits = value

    @property
    def units_for_data_being_imported(self) -> 'list_with_selected_item.ListWithSelectedItem_Unit':
        """list_with_selected_item.ListWithSelectedItem_Unit: 'UnitsForDataBeingImported' is the original name of this property."""

        temp = self.wrapped.UnitsForDataBeingImported

        if temp is None:
            return None

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_Unit')(temp) if temp is not None else None

    @units_for_data_being_imported.setter
    def units_for_data_being_imported(self, value: 'list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.UnitsForDataBeingImported = value

    @property
    def speeds(self) -> 'List[_6893.NamedSpeed]':
        """List[NamedSpeed]: 'Speeds' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Speeds

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def select_excel_file(self):
        """ 'SelectExcelFile' is the original name of this method."""

        self.wrapped.SelectExcelFile()

    @property
    def cast_to(self) -> 'HarmonicLoadDataExcelImport._Cast_HarmonicLoadDataExcelImport':
        return self._Cast_HarmonicLoadDataExcelImport(self)
