"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1733 import AdHocCustomTable
    from ._1734 import AxisSettings
    from ._1735 import BlankRow
    from ._1736 import CadPageOrientation
    from ._1737 import CadPageSize
    from ._1738 import CadTableBorderType
    from ._1739 import ChartDefinition
    from ._1740 import SMTChartPointShape
    from ._1741 import CustomChart
    from ._1742 import CustomDrawing
    from ._1743 import CustomGraphic
    from ._1744 import CustomImage
    from ._1745 import CustomReport
    from ._1746 import CustomReportCadDrawing
    from ._1747 import CustomReportChart
    from ._1748 import CustomReportChartItem
    from ._1749 import CustomReportColumn
    from ._1750 import CustomReportColumns
    from ._1751 import CustomReportDefinitionItem
    from ._1752 import CustomReportHorizontalLine
    from ._1753 import CustomReportHtmlItem
    from ._1754 import CustomReportItem
    from ._1755 import CustomReportItemContainer
    from ._1756 import CustomReportItemContainerCollection
    from ._1757 import CustomReportItemContainerCollectionBase
    from ._1758 import CustomReportItemContainerCollectionItem
    from ._1759 import CustomReportKey
    from ._1760 import CustomReportMultiPropertyItem
    from ._1761 import CustomReportMultiPropertyItemBase
    from ._1762 import CustomReportNameableItem
    from ._1763 import CustomReportNamedItem
    from ._1764 import CustomReportPropertyItem
    from ._1765 import CustomReportStatusItem
    from ._1766 import CustomReportTab
    from ._1767 import CustomReportTabs
    from ._1768 import CustomReportText
    from ._1769 import CustomRow
    from ._1770 import CustomSubReport
    from ._1771 import CustomTable
    from ._1772 import DefinitionBooleanCheckOptions
    from ._1773 import DynamicCustomReportItem
    from ._1774 import FontStyle
    from ._1775 import FontWeight
    from ._1776 import HeadingSize
    from ._1777 import SimpleChartDefinition
    from ._1778 import UserTextRow
else:
    import_structure = {
        '_1733': ['AdHocCustomTable'],
        '_1734': ['AxisSettings'],
        '_1735': ['BlankRow'],
        '_1736': ['CadPageOrientation'],
        '_1737': ['CadPageSize'],
        '_1738': ['CadTableBorderType'],
        '_1739': ['ChartDefinition'],
        '_1740': ['SMTChartPointShape'],
        '_1741': ['CustomChart'],
        '_1742': ['CustomDrawing'],
        '_1743': ['CustomGraphic'],
        '_1744': ['CustomImage'],
        '_1745': ['CustomReport'],
        '_1746': ['CustomReportCadDrawing'],
        '_1747': ['CustomReportChart'],
        '_1748': ['CustomReportChartItem'],
        '_1749': ['CustomReportColumn'],
        '_1750': ['CustomReportColumns'],
        '_1751': ['CustomReportDefinitionItem'],
        '_1752': ['CustomReportHorizontalLine'],
        '_1753': ['CustomReportHtmlItem'],
        '_1754': ['CustomReportItem'],
        '_1755': ['CustomReportItemContainer'],
        '_1756': ['CustomReportItemContainerCollection'],
        '_1757': ['CustomReportItemContainerCollectionBase'],
        '_1758': ['CustomReportItemContainerCollectionItem'],
        '_1759': ['CustomReportKey'],
        '_1760': ['CustomReportMultiPropertyItem'],
        '_1761': ['CustomReportMultiPropertyItemBase'],
        '_1762': ['CustomReportNameableItem'],
        '_1763': ['CustomReportNamedItem'],
        '_1764': ['CustomReportPropertyItem'],
        '_1765': ['CustomReportStatusItem'],
        '_1766': ['CustomReportTab'],
        '_1767': ['CustomReportTabs'],
        '_1768': ['CustomReportText'],
        '_1769': ['CustomRow'],
        '_1770': ['CustomSubReport'],
        '_1771': ['CustomTable'],
        '_1772': ['DefinitionBooleanCheckOptions'],
        '_1773': ['DynamicCustomReportItem'],
        '_1774': ['FontStyle'],
        '_1775': ['FontWeight'],
        '_1776': ['HeadingSize'],
        '_1777': ['SimpleChartDefinition'],
        '_1778': ['UserTextRow'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
