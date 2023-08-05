"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1823 import EnumWithSelectedValue
    from ._1825 import DeletableCollectionMember
    from ._1826 import DutyCyclePropertySummary
    from ._1827 import DutyCyclePropertySummaryForce
    from ._1828 import DutyCyclePropertySummaryPercentage
    from ._1829 import DutyCyclePropertySummarySmallAngle
    from ._1830 import DutyCyclePropertySummaryStress
    from ._1831 import EnumWithBoolean
    from ._1832 import NamedRangeWithOverridableMinAndMax
    from ._1833 import TypedObjectsWithOption
else:
    import_structure = {
        '_1823': ['EnumWithSelectedValue'],
        '_1825': ['DeletableCollectionMember'],
        '_1826': ['DutyCyclePropertySummary'],
        '_1827': ['DutyCyclePropertySummaryForce'],
        '_1828': ['DutyCyclePropertySummaryPercentage'],
        '_1829': ['DutyCyclePropertySummarySmallAngle'],
        '_1830': ['DutyCyclePropertySummaryStress'],
        '_1831': ['EnumWithBoolean'],
        '_1832': ['NamedRangeWithOverridableMinAndMax'],
        '_1833': ['TypedObjectsWithOption'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
