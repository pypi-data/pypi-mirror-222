"""_1031.py

CylindricalGearTableWithMGCharts
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.utility.report import _1771
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_TABLE_WITH_MG_CHARTS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearTableWithMGCharts')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1030


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearTableWithMGCharts',)


class CylindricalGearTableWithMGCharts(_1771.CustomTable):
    """CylindricalGearTableWithMGCharts

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_TABLE_WITH_MG_CHARTS

    class _Cast_CylindricalGearTableWithMGCharts:
        """Special nested class for casting CylindricalGearTableWithMGCharts to subclasses."""

        def __init__(self, parent: 'CylindricalGearTableWithMGCharts'):
            self._parent = parent

        @property
        def custom_table(self):
            return self._parent._cast(_1771.CustomTable)

        @property
        def custom_report_multi_property_item(self):
            from mastapy.utility.report import _1760, _1769
            
            return self._parent._cast(_1760.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(self):
            from mastapy.utility.report import _1761
            
            return self._parent._cast(_1761.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(self):
            from mastapy.utility.report import _1762
            
            return self._parent._cast(_1762.CustomReportNameableItem)

        @property
        def custom_report_item(self):
            from mastapy.utility.report import _1754
            
            return self._parent._cast(_1754.CustomReportItem)

        @property
        def cylindrical_gear_table_with_mg_charts(self) -> 'CylindricalGearTableWithMGCharts':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearTableWithMGCharts.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def chart_height(self) -> 'int':
        """int: 'ChartHeight' is the original name of this property."""

        temp = self.wrapped.ChartHeight

        if temp is None:
            return 0

        return temp

    @chart_height.setter
    def chart_height(self, value: 'int'):
        self.wrapped.ChartHeight = int(value) if value is not None else 0

    @property
    def chart_width(self) -> 'int':
        """int: 'ChartWidth' is the original name of this property."""

        temp = self.wrapped.ChartWidth

        if temp is None:
            return 0

        return temp

    @chart_width.setter
    def chart_width(self, value: 'int'):
        self.wrapped.ChartWidth = int(value) if value is not None else 0

    @property
    def item_detail(self) -> '_1030.CylindricalGearTableMGItemDetail':
        """CylindricalGearTableMGItemDetail: 'ItemDetail' is the original name of this property."""

        temp = self.wrapped.ItemDetail

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CylindricalGearTableMGItemDetail')
        return constructor.new_from_mastapy('mastapy.gears.gear_designs.cylindrical._1030', 'CylindricalGearTableMGItemDetail')(value) if value is not None else None

    @item_detail.setter
    def item_detail(self, value: '_1030.CylindricalGearTableMGItemDetail'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CylindricalGearTableMGItemDetail')
        self.wrapped.ItemDetail = value

    @property
    def cast_to(self) -> 'CylindricalGearTableWithMGCharts._Cast_CylindricalGearTableWithMGCharts':
        return self._Cast_CylindricalGearTableWithMGCharts(self)
