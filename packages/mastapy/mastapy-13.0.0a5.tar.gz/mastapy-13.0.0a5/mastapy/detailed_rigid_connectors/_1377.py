﻿"""_1377.py

DetailedRigidConnectorDesign
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DETAILED_RIGID_CONNECTOR_DESIGN = python_net_import('SMT.MastaAPI.DetailedRigidConnectors', 'DetailedRigidConnectorDesign')

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors import _1378


__docformat__ = 'restructuredtext en'
__all__ = ('DetailedRigidConnectorDesign',)


class DetailedRigidConnectorDesign(_0.APIBase):
    """DetailedRigidConnectorDesign

    This is a mastapy class.
    """

    TYPE = _DETAILED_RIGID_CONNECTOR_DESIGN

    class _Cast_DetailedRigidConnectorDesign:
        """Special nested class for casting DetailedRigidConnectorDesign to subclasses."""

        def __init__(self, parent: 'DetailedRigidConnectorDesign'):
            self._parent = parent

        @property
        def custom_spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1380
            
            return self._parent._cast(_1380.CustomSplineJointDesign)

        @property
        def din5480_spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1383
            
            return self._parent._cast(_1383.DIN5480SplineJointDesign)

        @property
        def gbt3478_spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1387
            
            return self._parent._cast(_1387.GBT3478SplineJointDesign)

        @property
        def iso4156_spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1390
            
            return self._parent._cast(_1390.ISO4156SplineJointDesign)

        @property
        def jisb1603_spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1391
            
            return self._parent._cast(_1391.JISB1603SplineJointDesign)

        @property
        def sae_spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1398
            
            return self._parent._cast(_1398.SAESplineJointDesign)

        @property
        def spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1405
            
            return self._parent._cast(_1405.SplineJointDesign)

        @property
        def standard_spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1410
            
            return self._parent._cast(_1410.StandardSplineJointDesign)

        @property
        def keyed_joint_design(self):
            from mastapy.detailed_rigid_connectors.keyed_joints import _1427
            
            return self._parent._cast(_1427.KeyedJointDesign)

        @property
        def interference_fit_design(self):
            from mastapy.detailed_rigid_connectors.interference_fits import _1435
            
            return self._parent._cast(_1435.InterferenceFitDesign)

        @property
        def detailed_rigid_connector_design(self) -> 'DetailedRigidConnectorDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DetailedRigidConnectorDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_spline_drawing(self) -> 'Image':
        """Image: 'TwoDSplineDrawing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TwoDSplineDrawing

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def length_of_engagement(self) -> 'float':
        """float: 'LengthOfEngagement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LengthOfEngagement

        if temp is None:
            return 0.0

        return temp

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
    def halves(self) -> 'List[_1378.DetailedRigidConnectorHalfDesign]':
        """List[DetailedRigidConnectorHalfDesign]: 'Halves' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Halves

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
    def cast_to(self) -> 'DetailedRigidConnectorDesign._Cast_DetailedRigidConnectorDesign':
        return self._Cast_DetailedRigidConnectorDesign(self)
