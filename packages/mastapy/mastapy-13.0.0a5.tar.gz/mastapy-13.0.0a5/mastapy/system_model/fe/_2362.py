"""_2362.py

FEPartDRIVASurfaceSelection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_DRIVA_SURFACE_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.FE', 'FEPartDRIVASurfaceSelection')

if TYPE_CHECKING:
    from mastapy.system_model.fe import _2366
    from mastapy.nodal_analysis.component_mode_synthesis import _223


__docformat__ = 'restructuredtext en'
__all__ = ('FEPartDRIVASurfaceSelection',)


class FEPartDRIVASurfaceSelection(_0.APIBase):
    """FEPartDRIVASurfaceSelection

    This is a mastapy class.
    """

    TYPE = _FE_PART_DRIVA_SURFACE_SELECTION

    class _Cast_FEPartDRIVASurfaceSelection:
        """Special nested class for casting FEPartDRIVASurfaceSelection to subclasses."""

        def __init__(self, parent: 'FEPartDRIVASurfaceSelection'):
            self._parent = parent

        @property
        def fe_part_driva_surface_selection(self) -> 'FEPartDRIVASurfaceSelection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEPartDRIVASurfaceSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fe_substructures(self) -> 'list_with_selected_item.ListWithSelectedItem_FESubstructure':
        """list_with_selected_item.ListWithSelectedItem_FESubstructure: 'FESubstructures' is the original name of this property."""

        temp = self.wrapped.FESubstructures

        if temp is None:
            return None

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_FESubstructure')(temp) if temp is not None else None

    @fe_substructures.setter
    def fe_substructures(self, value: 'list_with_selected_item.ListWithSelectedItem_FESubstructure.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_FESubstructure.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_FESubstructure.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.FESubstructures = value

    @property
    def is_included(self) -> 'bool':
        """bool: 'IsIncluded' is the original name of this property."""

        temp = self.wrapped.IsIncluded

        if temp is None:
            return False

        return temp

    @is_included.setter
    def is_included(self, value: 'bool'):
        self.wrapped.IsIncluded = bool(value) if value is not None else False

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
    def surfaces(self) -> 'list_with_selected_item.ListWithSelectedItem_CMSElementFaceGroup':
        """list_with_selected_item.ListWithSelectedItem_CMSElementFaceGroup: 'Surfaces' is the original name of this property."""

        temp = self.wrapped.Surfaces

        if temp is None:
            return None

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_CMSElementFaceGroup')(temp) if temp is not None else None

    @surfaces.setter
    def surfaces(self, value: 'list_with_selected_item.ListWithSelectedItem_CMSElementFaceGroup.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_CMSElementFaceGroup.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_CMSElementFaceGroup.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.Surfaces = value

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
    def cast_to(self) -> 'FEPartDRIVASurfaceSelection._Cast_FEPartDRIVASurfaceSelection':
        return self._Cast_FEPartDRIVASurfaceSelection(self)
