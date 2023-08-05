"""_2600.py

PartDetailSelection
"""
from __future__ import annotations

from typing import (
    TYPE_CHECKING, List, TypeVar, Generic
)

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_DETAIL_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Configurations', 'PartDetailSelection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2451


__docformat__ = 'restructuredtext en'
__all__ = ('PartDetailSelection',)


TPart = TypeVar('TPart', bound='_2451.Part')
TSelectableItem = TypeVar('TSelectableItem')


class PartDetailSelection(_0.APIBase, Generic[TPart, TSelectableItem]):
    """PartDetailSelection

    This is a mastapy class.

    Generic Types:
        TPart
        TSelectableItem
    """

    TYPE = _PART_DETAIL_SELECTION

    class _Cast_PartDetailSelection:
        """Special nested class for casting PartDetailSelection to subclasses."""

        def __init__(self, parent: 'PartDetailSelection'):
            self._parent = parent

        @property
        def active_cylindrical_gear_set_design_selection(self):
            from mastapy.system_model.part_model.gears import _2492
            
            return self._parent._cast(_2492.ActiveCylindricalGearSetDesignSelection)

        @property
        def active_gear_set_design_selection(self):
            from mastapy.system_model.part_model.gears import _2493
            
            return self._parent._cast(_2493.ActiveGearSetDesignSelection)

        @property
        def active_fe_substructure_selection(self):
            from mastapy.system_model.part_model.configurations import _2593
            
            return self._parent._cast(_2593.ActiveFESubstructureSelection)

        @property
        def active_shaft_design_selection(self):
            from mastapy.system_model.part_model.configurations import _2595
            
            return self._parent._cast(_2595.ActiveShaftDesignSelection)

        @property
        def bearing_detail_selection(self):
            from mastapy.system_model.part_model.configurations import _2598
            
            return self._parent._cast(_2598.BearingDetailSelection)

        @property
        def part_detail_selection(self) -> 'PartDetailSelection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartDetailSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def selection(self) -> 'list_with_selected_item.ListWithSelectedItem_TSelectableItem':
        """list_with_selected_item.ListWithSelectedItem_TSelectableItem: 'Selection' is the original name of this property."""

        temp = self.wrapped.Selection

        if temp is None:
            return None

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_TSelectableItem')(temp) if temp is not None else None

    @selection.setter
    def selection(self, value: 'list_with_selected_item.ListWithSelectedItem_TSelectableItem.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_TSelectableItem.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_TSelectableItem.implicit_type()
        value = wrapper_type[enclosed_type](value if value is not None else None)
        self.wrapped.Selection = value

    @property
    def part(self) -> 'TPart':
        """TPart: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_item(self) -> 'TSelectableItem':
        """TSelectableItem: 'SelectedItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SelectedItem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result

    @property
    def cast_to(self) -> 'PartDetailSelection._Cast_PartDetailSelection':
        return self._Cast_PartDetailSelection(self)
