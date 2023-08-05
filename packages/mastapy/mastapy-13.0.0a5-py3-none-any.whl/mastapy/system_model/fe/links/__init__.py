"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2401 import FELink
    from ._2402 import ElectricMachineStatorFELink
    from ._2403 import FELinkWithSelection
    from ._2404 import GearMeshFELink
    from ._2405 import GearWithDuplicatedMeshesFELink
    from ._2406 import MultiAngleConnectionFELink
    from ._2407 import MultiNodeConnectorFELink
    from ._2408 import MultiNodeFELink
    from ._2409 import PlanetaryConnectorMultiNodeFELink
    from ._2410 import PlanetBasedFELink
    from ._2411 import PlanetCarrierFELink
    from ._2412 import PointLoadFELink
    from ._2413 import RollingRingConnectionFELink
    from ._2414 import ShaftHubConnectionFELink
    from ._2415 import SingleNodeFELink
else:
    import_structure = {
        '_2401': ['FELink'],
        '_2402': ['ElectricMachineStatorFELink'],
        '_2403': ['FELinkWithSelection'],
        '_2404': ['GearMeshFELink'],
        '_2405': ['GearWithDuplicatedMeshesFELink'],
        '_2406': ['MultiAngleConnectionFELink'],
        '_2407': ['MultiNodeConnectorFELink'],
        '_2408': ['MultiNodeFELink'],
        '_2409': ['PlanetaryConnectorMultiNodeFELink'],
        '_2410': ['PlanetBasedFELink'],
        '_2411': ['PlanetCarrierFELink'],
        '_2412': ['PointLoadFELink'],
        '_2413': ['RollingRingConnectionFELink'],
        '_2414': ['ShaftHubConnectionFELink'],
        '_2415': ['SingleNodeFELink'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
