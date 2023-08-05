﻿"""_225.py

CMSModel
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CMS_MODEL = python_net_import('SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis', 'CMSModel')

if TYPE_CHECKING:
    from mastapy.nodal_analysis.component_mode_synthesis import _232, _227, _223
    from mastapy.nodal_analysis.dev_tools_analyses import _183
    from mastapy.utility import _1569


__docformat__ = 'restructuredtext en'
__all__ = ('CMSModel',)


class CMSModel(_0.APIBase):
    """CMSModel

    This is a mastapy class.
    """

    TYPE = _CMS_MODEL

    class _Cast_CMSModel:
        """Special nested class for casting CMSModel to subclasses."""

        def __init__(self, parent: 'CMSModel'):
            self._parent = parent

        @property
        def cms_model(self) -> 'CMSModel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CMSModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def estimated_memory_required_for_displacement_expansion(self) -> 'str':
        """str: 'EstimatedMemoryRequiredForDisplacementExpansion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EstimatedMemoryRequiredForDisplacementExpansion

        if temp is None:
            return ''

        return temp

    @property
    def estimated_memory_required_for_stiffness_and_mass_matrices(self) -> 'str':
        """str: 'EstimatedMemoryRequiredForStiffnessAndMassMatrices' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EstimatedMemoryRequiredForStiffnessAndMassMatrices

        if temp is None:
            return ''

        return temp

    @property
    def estimated_total_memory_required_for_results(self) -> 'str':
        """str: 'EstimatedTotalMemoryRequiredForResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EstimatedTotalMemoryRequiredForResults

        if temp is None:
            return ''

        return temp

    @property
    def has_condensation_result(self) -> 'bool':
        """bool: 'HasCondensationResult' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HasCondensationResult

        if temp is None:
            return False

        return temp

    @property
    def memory_required_for_displacement_expansion(self) -> 'str':
        """str: 'MemoryRequiredForDisplacementExpansion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MemoryRequiredForDisplacementExpansion

        if temp is None:
            return ''

        return temp

    @property
    def memory_required_for_stiffness_and_mass_matrices(self) -> 'str':
        """str: 'MemoryRequiredForStiffnessAndMassMatrices' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MemoryRequiredForStiffnessAndMassMatrices

        if temp is None:
            return ''

        return temp

    @property
    def software_used_for_reduction(self) -> '_232.SoftwareUsedForReductionType':
        """SoftwareUsedForReductionType: 'SoftwareUsedForReduction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SoftwareUsedForReduction

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis.SoftwareUsedForReductionType')
        return constructor.new_from_mastapy('mastapy.nodal_analysis.component_mode_synthesis._232', 'SoftwareUsedForReductionType')(value) if value is not None else None

    @property
    def total_memory_required_for_mesh(self) -> 'str':
        """str: 'TotalMemoryRequiredForMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalMemoryRequiredForMesh

        if temp is None:
            return ''

        return temp

    @property
    def total_memory_required_for_results(self) -> 'str':
        """str: 'TotalMemoryRequiredForResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalMemoryRequiredForResults

        if temp is None:
            return ''

        return temp

    @property
    def fe_model(self) -> '_183.FEModel':
        """FEModel: 'FEModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FEModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def reduction_information(self) -> '_1569.AnalysisRunInformation':
        """AnalysisRunInformation: 'ReductionInformation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReductionInformation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def reduction_options(self) -> '_227.CMSOptions':
        """CMSOptions: 'ReductionOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReductionOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def element_face_groups(self) -> 'List[_223.CMSElementFaceGroup]':
        """List[CMSElementFaceGroup]: 'ElementFaceGroups' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementFaceGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

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

    def save_surface_mesh_as_stl(self, file_path: 'str'):
        """ 'SaveSurfaceMeshAsStl' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.SaveSurfaceMeshAsStl(file_path if file_path else '')

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
    def cast_to(self) -> 'CMSModel._Cast_CMSModel':
        return self._Cast_CMSModel(self)
