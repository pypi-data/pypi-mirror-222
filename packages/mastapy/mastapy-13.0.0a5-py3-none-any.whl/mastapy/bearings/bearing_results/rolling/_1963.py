"""_1963.py

ISO14179SettingsPerBearingType
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal.python_net import python_net_import
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.utility import _1577
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_ISO14179_SETTINGS_PER_BEARING_TYPE = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'ISO14179SettingsPerBearingType')

if TYPE_CHECKING:
    from mastapy.bearings import _1883
    from mastapy.bearings.bearing_results.rolling import _1961


__docformat__ = 'restructuredtext en'
__all__ = ('ISO14179SettingsPerBearingType',)


class ISO14179SettingsPerBearingType(_1577.IndependentReportablePropertiesBase['ISO14179SettingsPerBearingType']):
    """ISO14179SettingsPerBearingType

    This is a mastapy class.
    """

    TYPE = _ISO14179_SETTINGS_PER_BEARING_TYPE

    class _Cast_ISO14179SettingsPerBearingType:
        """Special nested class for casting ISO14179SettingsPerBearingType to subclasses."""

        def __init__(self, parent: 'ISO14179SettingsPerBearingType'):
            self._parent = parent

        @property
        def independent_reportable_properties_base(self):
            from mastapy.bearings.bearing_results.rolling import _1963
            
            return self._parent._cast(_1577.IndependentReportablePropertiesBase)

        @property
        def iso14179_settings_per_bearing_type(self) -> 'ISO14179SettingsPerBearingType':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISO14179SettingsPerBearingType.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def iso14179_settings_database(self) -> 'str':
        """str: 'ISO14179SettingsDatabase' is the original name of this property."""

        temp = self.wrapped.ISO14179SettingsDatabase.SelectedItemName

        if temp is None:
            return ''

        return temp

    @iso14179_settings_database.setter
    def iso14179_settings_database(self, value: 'str'):
        self.wrapped.ISO14179SettingsDatabase.SetSelectedItem(str(value) if value is not None else '')

    @property
    def rolling_bearing_type(self) -> '_1883.RollingBearingType':
        """RollingBearingType: 'RollingBearingType' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingBearingType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bearings.RollingBearingType')
        return constructor.new_from_mastapy('mastapy.bearings._1883', 'RollingBearingType')(value) if value is not None else None

    @property
    def iso14179_settings(self) -> '_1961.ISO14179Settings':
        """ISO14179Settings: 'ISO14179Settings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO14179Settings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ISO14179SettingsPerBearingType._Cast_ISO14179SettingsPerBearingType':
        return self._Cast_ISO14179SettingsPerBearingType(self)
