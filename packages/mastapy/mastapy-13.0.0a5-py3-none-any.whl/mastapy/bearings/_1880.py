"""_1880.py

RollingBearingDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Optional, List

from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.utility.databases import _1820
from mastapy.bearings import _1881
from mastapy.bearings.bearing_designs.rolling import _2152
from mastapy._internal.cast_exception import CastException

_ROLLING_BEARING_TYPE = python_net_import('SMT.MastaAPI.Bearings', 'RollingBearingType')
_BEARING_CATALOG = python_net_import('SMT.MastaAPI.Bearings', 'BearingCatalog')
_HYBRID_STEEL_ALL = python_net_import('SMT.MastaAPI.Bearings', 'HybridSteelAll')
_ROLLING_BEARING_DATABASE = python_net_import('SMT.MastaAPI.Bearings', 'RollingBearingDatabase')
_STRING = python_net_import('System', 'String')
_INT_32 = python_net_import('System', 'Int32')
_RANGE = python_net_import('SMT.MastaAPI.MathUtility', 'Range')

if TYPE_CHECKING:
    from mastapy.bearings import _1883, _1856, _1872
    from mastapy.math_utility import _1479


__docformat__ = 'restructuredtext en'
__all__ = ('RollingBearingDatabase',)


class RollingBearingDatabase(_1820.SQLDatabase['_1881.RollingBearingKey', '_2152.RollingBearing']):
    """RollingBearingDatabase

    This is a mastapy class.
    """

    TYPE = _ROLLING_BEARING_DATABASE

    class _Cast_RollingBearingDatabase:
        """Special nested class for casting RollingBearingDatabase to subclasses."""

        def __init__(self, parent: 'RollingBearingDatabase'):
            self._parent = parent

        @property
        def sql_database(self):
            return self._parent._cast(_1820.SQLDatabase)

        @property
        def database(self):
            from mastapy.utility.databases import _1813
            
            return self._parent._cast(_1813.Database)

        @property
        def rolling_bearing_database(self) -> 'RollingBearingDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollingBearingDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def add_to_database(self, bearing: '_2152.RollingBearing'):
        """ 'AddToDatabase' is the original name of this method.

        Args:
            bearing (mastapy.bearings.bearing_designs.rolling.RollingBearing)
        """

        self.wrapped.AddToDatabase(bearing.wrapped if bearing else None)

    def create_bearing(self, type_: '_1883.RollingBearingType', designation: Optional['str'] = 'None') -> '_2152.RollingBearing':
        """ 'CreateBearing' is the original name of this method.

        Args:
            type_ (mastapy.bearings.RollingBearingType)
            designation (str, optional)

        Returns:
            mastapy.bearings.bearing_designs.rolling.RollingBearing
        """

        type_ = conversion.mp_to_pn_enum(type_, 'SMT.MastaAPI.Bearings.RollingBearingType')
        designation = str(designation)
        method_result = self.wrapped.CreateBearing.Overloads[_ROLLING_BEARING_TYPE, _STRING](type_, designation if designation else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def create_bearing_with_type_name(self, type_: 'str', designation: Optional['str'] = 'None') -> '_2152.RollingBearing':
        """ 'CreateBearing' is the original name of this method.

        Args:
            type_ (str)
            designation (str, optional)

        Returns:
            mastapy.bearings.bearing_designs.rolling.RollingBearing
        """

        type_ = str(type_)
        designation = str(designation)
        method_result = self.wrapped.CreateBearing.Overloads[_STRING, _STRING](type_ if type_ else '', designation if designation else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def create_key(self, type_: '_1883.RollingBearingType', designation: Optional['str'] = 'None') -> '_1881.RollingBearingKey':
        """ 'CreateKey' is the original name of this method.

        Args:
            type_ (mastapy.bearings.RollingBearingType)
            designation (str, optional)

        Returns:
            mastapy.bearings.RollingBearingKey
        """

        type_ = conversion.mp_to_pn_enum(type_, 'SMT.MastaAPI.Bearings.RollingBearingType')
        designation = str(designation)
        method_result = self.wrapped.CreateKey.Overloads[_ROLLING_BEARING_TYPE, _STRING](type_, designation if designation else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def create_key_with_type_name(self, type_: 'str', designation: Optional['str'] = 'None') -> '_1881.RollingBearingKey':
        """ 'CreateKey' is the original name of this method.

        Args:
            type_ (str)
            designation (str, optional)

        Returns:
            mastapy.bearings.RollingBearingKey
        """

        type_ = str(type_)
        designation = str(designation)
        method_result = self.wrapped.CreateKey.Overloads[_STRING, _STRING](type_ if type_ else '', designation if designation else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def remove_from_database(self, bearing: '_2152.RollingBearing'):
        """ 'RemoveFromDatabase' is the original name of this method.

        Args:
            bearing (mastapy.bearings.bearing_designs.rolling.RollingBearing)
        """

        self.wrapped.RemoveFromDatabase(bearing.wrapped if bearing else None)

    def search_for_rolling_bearing_with_catalog(self, catalog: '_1856.BearingCatalog') -> 'List[_2152.RollingBearing]':
        """ 'SearchForRollingBearing' is the original name of this method.

        Args:
            catalog (mastapy.bearings.BearingCatalog)

        Returns:
            List[mastapy.bearings.bearing_designs.rolling.RollingBearing]
        """

        catalog = conversion.mp_to_pn_enum(catalog, 'SMT.MastaAPI.Bearings.BearingCatalog')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.SearchForRollingBearing.Overloads[_BEARING_CATALOG](catalog))

    def search_for_rolling_bearing_with_name_and_catalog(self, designation: 'str', catalog: '_1856.BearingCatalog') -> '_2152.RollingBearing':
        """ 'SearchForRollingBearing' is the original name of this method.

        Args:
            designation (str)
            catalog (mastapy.bearings.BearingCatalog)

        Returns:
            mastapy.bearings.bearing_designs.rolling.RollingBearing
        """

        designation = str(designation)
        catalog = conversion.mp_to_pn_enum(catalog, 'SMT.MastaAPI.Bearings.BearingCatalog')
        method_result = self.wrapped.SearchForRollingBearing.Overloads[_STRING, _BEARING_CATALOG](designation if designation else '', catalog)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def search_for_rolling_bearing_with_name_catalog_and_type(self, designation: 'str', catalog: '_1856.BearingCatalog', type_: '_1883.RollingBearingType') -> 'List[_2152.RollingBearing]':
        """ 'SearchForRollingBearing' is the original name of this method.

        Args:
            designation (str)
            catalog (mastapy.bearings.BearingCatalog)
            type_ (mastapy.bearings.RollingBearingType)

        Returns:
            List[mastapy.bearings.bearing_designs.rolling.RollingBearing]
        """

        designation = str(designation)
        catalog = conversion.mp_to_pn_enum(catalog, 'SMT.MastaAPI.Bearings.BearingCatalog')
        type_ = conversion.mp_to_pn_enum(type_, 'SMT.MastaAPI.Bearings.RollingBearingType')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.SearchForRollingBearing.Overloads[_STRING, _BEARING_CATALOG, _ROLLING_BEARING_TYPE](designation if designation else '', catalog, type_))

    def search_for_rolling_bearing(self, designation: 'str', catalog: '_1856.BearingCatalog', type_: '_1883.RollingBearingType', bore_range: '_1479.Range', outer_diameter_range: '_1479.Range', width_range: '_1479.Range', dynamic_capacity_range: '_1479.Range', number_of_rows: 'int', material_type: '_1872.HybridSteelAll') -> 'List[_2152.RollingBearing]':
        """ 'SearchForRollingBearing' is the original name of this method.

        Args:
            designation (str)
            catalog (mastapy.bearings.BearingCatalog)
            type_ (mastapy.bearings.RollingBearingType)
            bore_range (mastapy.math_utility.Range)
            outer_diameter_range (mastapy.math_utility.Range)
            width_range (mastapy.math_utility.Range)
            dynamic_capacity_range (mastapy.math_utility.Range)
            number_of_rows (int)
            material_type (mastapy.bearings.HybridSteelAll)

        Returns:
            List[mastapy.bearings.bearing_designs.rolling.RollingBearing]
        """

        designation = str(designation)
        catalog = conversion.mp_to_pn_enum(catalog, 'SMT.MastaAPI.Bearings.BearingCatalog')
        type_ = conversion.mp_to_pn_enum(type_, 'SMT.MastaAPI.Bearings.RollingBearingType')
        number_of_rows = int(number_of_rows)
        material_type = conversion.mp_to_pn_enum(material_type, 'SMT.MastaAPI.Bearings.HybridSteelAll')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.SearchForRollingBearing.Overloads[_STRING, _BEARING_CATALOG, _ROLLING_BEARING_TYPE, _RANGE, _RANGE, _RANGE, _RANGE, _INT_32, _HYBRID_STEEL_ALL](designation if designation else '', catalog, type_, bore_range.wrapped if bore_range else None, outer_diameter_range.wrapped if outer_diameter_range else None, width_range.wrapped if width_range else None, dynamic_capacity_range.wrapped if dynamic_capacity_range else None, number_of_rows if number_of_rows else 0, material_type))

    @property
    def cast_to(self) -> 'RollingBearingDatabase._Cast_RollingBearingDatabase':
        return self._Cast_RollingBearingDatabase(self)
