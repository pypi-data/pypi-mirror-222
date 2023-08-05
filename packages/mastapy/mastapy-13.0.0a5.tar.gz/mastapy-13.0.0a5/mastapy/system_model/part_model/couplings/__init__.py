"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2558 import BeltDrive
    from ._2559 import BeltDriveType
    from ._2560 import Clutch
    from ._2561 import ClutchHalf
    from ._2562 import ClutchType
    from ._2563 import ConceptCoupling
    from ._2564 import ConceptCouplingHalf
    from ._2565 import Coupling
    from ._2566 import CouplingHalf
    from ._2567 import CrowningSpecification
    from ._2568 import CVT
    from ._2569 import CVTPulley
    from ._2570 import PartToPartShearCoupling
    from ._2571 import PartToPartShearCouplingHalf
    from ._2572 import Pulley
    from ._2573 import RigidConnectorStiffnessType
    from ._2574 import RigidConnectorTiltStiffnessTypes
    from ._2575 import RigidConnectorToothLocation
    from ._2576 import RigidConnectorToothSpacingType
    from ._2577 import RigidConnectorTypes
    from ._2578 import RollingRing
    from ._2579 import RollingRingAssembly
    from ._2580 import ShaftHubConnection
    from ._2581 import SplineLeadRelief
    from ._2582 import SpringDamper
    from ._2583 import SpringDamperHalf
    from ._2584 import Synchroniser
    from ._2585 import SynchroniserCone
    from ._2586 import SynchroniserHalf
    from ._2587 import SynchroniserPart
    from ._2588 import SynchroniserSleeve
    from ._2589 import TorqueConverter
    from ._2590 import TorqueConverterPump
    from ._2591 import TorqueConverterSpeedRatio
    from ._2592 import TorqueConverterTurbine
else:
    import_structure = {
        '_2558': ['BeltDrive'],
        '_2559': ['BeltDriveType'],
        '_2560': ['Clutch'],
        '_2561': ['ClutchHalf'],
        '_2562': ['ClutchType'],
        '_2563': ['ConceptCoupling'],
        '_2564': ['ConceptCouplingHalf'],
        '_2565': ['Coupling'],
        '_2566': ['CouplingHalf'],
        '_2567': ['CrowningSpecification'],
        '_2568': ['CVT'],
        '_2569': ['CVTPulley'],
        '_2570': ['PartToPartShearCoupling'],
        '_2571': ['PartToPartShearCouplingHalf'],
        '_2572': ['Pulley'],
        '_2573': ['RigidConnectorStiffnessType'],
        '_2574': ['RigidConnectorTiltStiffnessTypes'],
        '_2575': ['RigidConnectorToothLocation'],
        '_2576': ['RigidConnectorToothSpacingType'],
        '_2577': ['RigidConnectorTypes'],
        '_2578': ['RollingRing'],
        '_2579': ['RollingRingAssembly'],
        '_2580': ['ShaftHubConnection'],
        '_2581': ['SplineLeadRelief'],
        '_2582': ['SpringDamper'],
        '_2583': ['SpringDamperHalf'],
        '_2584': ['Synchroniser'],
        '_2585': ['SynchroniserCone'],
        '_2586': ['SynchroniserHalf'],
        '_2587': ['SynchroniserPart'],
        '_2588': ['SynchroniserSleeve'],
        '_2589': ['TorqueConverter'],
        '_2590': ['TorqueConverterPump'],
        '_2591': ['TorqueConverterSpeedRatio'],
        '_2592': ['TorqueConverterTurbine'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
