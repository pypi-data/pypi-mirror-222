﻿"""_576.py

Modification
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODIFICATION = python_net_import('SMT.MastaAPI.Gears.MicroGeometry', 'Modification')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1019


__docformat__ = 'restructuredtext en'
__all__ = ('Modification',)


class Modification(_0.APIBase):
    """Modification

    This is a mastapy class.
    """

    TYPE = _MODIFICATION

    class _Cast_Modification:
        """Special nested class for casting Modification to subclasses."""

        def __init__(self, parent: 'Modification'):
            self._parent = parent

        @property
        def bias_modification(self):
            from mastapy.gears.micro_geometry import _566
            
            return self._parent._cast(_566.BiasModification)

        @property
        def lead_modification(self):
            from mastapy.gears.micro_geometry import _569
            
            return self._parent._cast(_569.LeadModification)

        @property
        def profile_modification(self):
            from mastapy.gears.micro_geometry import _579
            
            return self._parent._cast(_579.ProfileModification)

        @property
        def cylindrical_gear_bias_modification(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1089
            
            return self._parent._cast(_1089.CylindricalGearBiasModification)

        @property
        def cylindrical_gear_lead_modification(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1092
            
            return self._parent._cast(_1092.CylindricalGearLeadModification)

        @property
        def cylindrical_gear_lead_modification_at_profile_position(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1093
            
            return self._parent._cast(_1093.CylindricalGearLeadModificationAtProfilePosition)

        @property
        def cylindrical_gear_profile_modification(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1101
            
            return self._parent._cast(_1101.CylindricalGearProfileModification)

        @property
        def cylindrical_gear_profile_modification_at_face_width_position(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1102
            
            return self._parent._cast(_1102.CylindricalGearProfileModificationAtFaceWidthPosition)

        @property
        def cylindrical_gear_triangular_end_modification(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1106
            
            return self._parent._cast(_1106.CylindricalGearTriangularEndModification)

        @property
        def conical_gear_bias_modification(self):
            from mastapy.gears.gear_designs.conical.micro_geometry import _1168
            
            return self._parent._cast(_1168.ConicalGearBiasModification)

        @property
        def conical_gear_lead_modification(self):
            from mastapy.gears.gear_designs.conical.micro_geometry import _1170
            
            return self._parent._cast(_1170.ConicalGearLeadModification)

        @property
        def conical_gear_profile_modification(self):
            from mastapy.gears.gear_designs.conical.micro_geometry import _1171
            
            return self._parent._cast(_1171.ConicalGearProfileModification)

        @property
        def modification(self) -> 'Modification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Modification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def settings(self) -> '_1019.CylindricalGearMicroGeometrySettingsItem':
        """CylindricalGearMicroGeometrySettingsItem: 'Settings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Settings

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
    def cast_to(self) -> 'Modification._Cast_Modification':
        return self._Cast_Modification(self)
