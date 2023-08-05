"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1788 import GearMeshForTE
    from ._1789 import GearOrderForTE
    from ._1790 import GearPositions
    from ._1791 import HarmonicOrderForTE
    from ._1792 import LabelOnlyOrder
    from ._1793 import OrderForTE
    from ._1794 import OrderSelector
    from ._1795 import OrderWithRadius
    from ._1796 import RollingBearingOrder
    from ._1797 import ShaftOrderForTE
    from ._1798 import UserDefinedOrderForTE
else:
    import_structure = {
        '_1788': ['GearMeshForTE'],
        '_1789': ['GearOrderForTE'],
        '_1790': ['GearPositions'],
        '_1791': ['HarmonicOrderForTE'],
        '_1792': ['LabelOnlyOrder'],
        '_1793': ['OrderForTE'],
        '_1794': ['OrderSelector'],
        '_1795': ['OrderWithRadius'],
        '_1796': ['RollingBearingOrder'],
        '_1797': ['ShaftOrderForTE'],
        '_1798': ['UserDefinedOrderForTE'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
