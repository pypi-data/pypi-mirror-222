"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2325 import ClutchConnection
    from ._2326 import ClutchSocket
    from ._2327 import ConceptCouplingConnection
    from ._2328 import ConceptCouplingSocket
    from ._2329 import CouplingConnection
    from ._2330 import CouplingSocket
    from ._2331 import PartToPartShearCouplingConnection
    from ._2332 import PartToPartShearCouplingSocket
    from ._2333 import SpringDamperConnection
    from ._2334 import SpringDamperSocket
    from ._2335 import TorqueConverterConnection
    from ._2336 import TorqueConverterPumpSocket
    from ._2337 import TorqueConverterTurbineSocket
else:
    import_structure = {
        '_2325': ['ClutchConnection'],
        '_2326': ['ClutchSocket'],
        '_2327': ['ConceptCouplingConnection'],
        '_2328': ['ConceptCouplingSocket'],
        '_2329': ['CouplingConnection'],
        '_2330': ['CouplingSocket'],
        '_2331': ['PartToPartShearCouplingConnection'],
        '_2332': ['PartToPartShearCouplingSocket'],
        '_2333': ['SpringDamperConnection'],
        '_2334': ['SpringDamperSocket'],
        '_2335': ['TorqueConverterConnection'],
        '_2336': ['TorqueConverterPumpSocket'],
        '_2337': ['TorqueConverterTurbineSocket'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
