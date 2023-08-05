"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1441 import ContactSpecification
    from ._1442 import CrowningSpecificationMethod
    from ._1443 import CycloidalAssemblyDesign
    from ._1444 import CycloidalDiscDesign
    from ._1445 import CycloidalDiscDesignExporter
    from ._1446 import CycloidalDiscMaterial
    from ._1447 import CycloidalDiscMaterialDatabase
    from ._1448 import CycloidalDiscModificationsSpecification
    from ._1449 import DirectionOfMeasuredModifications
    from ._1450 import GeometryToExport
    from ._1451 import NamedDiscPhase
    from ._1452 import RingPinsDesign
    from ._1453 import RingPinsMaterial
    from ._1454 import RingPinsMaterialDatabase
else:
    import_structure = {
        '_1441': ['ContactSpecification'],
        '_1442': ['CrowningSpecificationMethod'],
        '_1443': ['CycloidalAssemblyDesign'],
        '_1444': ['CycloidalDiscDesign'],
        '_1445': ['CycloidalDiscDesignExporter'],
        '_1446': ['CycloidalDiscMaterial'],
        '_1447': ['CycloidalDiscMaterialDatabase'],
        '_1448': ['CycloidalDiscModificationsSpecification'],
        '_1449': ['DirectionOfMeasuredModifications'],
        '_1450': ['GeometryToExport'],
        '_1451': ['NamedDiscPhase'],
        '_1452': ['RingPinsDesign'],
        '_1453': ['RingPinsMaterial'],
        '_1454': ['RingPinsMaterialDatabase'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
