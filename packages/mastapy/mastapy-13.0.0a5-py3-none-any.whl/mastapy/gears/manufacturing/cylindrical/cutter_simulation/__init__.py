"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._728 import CutterSimulationCalc
    from ._729 import CylindricalCutterSimulatableGear
    from ._730 import CylindricalGearSpecification
    from ._731 import CylindricalManufacturedRealGearInMesh
    from ._732 import CylindricalManufacturedVirtualGearInMesh
    from ._733 import FinishCutterSimulation
    from ._734 import FinishStockPoint
    from ._735 import FormWheelGrindingSimulationCalculator
    from ._736 import GearCutterSimulation
    from ._737 import HobSimulationCalculator
    from ._738 import ManufacturingOperationConstraints
    from ._739 import ManufacturingProcessControls
    from ._740 import RackSimulationCalculator
    from ._741 import RoughCutterSimulation
    from ._742 import ShaperSimulationCalculator
    from ._743 import ShavingSimulationCalculator
    from ._744 import VirtualSimulationCalculator
    from ._745 import WormGrinderSimulationCalculator
else:
    import_structure = {
        '_728': ['CutterSimulationCalc'],
        '_729': ['CylindricalCutterSimulatableGear'],
        '_730': ['CylindricalGearSpecification'],
        '_731': ['CylindricalManufacturedRealGearInMesh'],
        '_732': ['CylindricalManufacturedVirtualGearInMesh'],
        '_733': ['FinishCutterSimulation'],
        '_734': ['FinishStockPoint'],
        '_735': ['FormWheelGrindingSimulationCalculator'],
        '_736': ['GearCutterSimulation'],
        '_737': ['HobSimulationCalculator'],
        '_738': ['ManufacturingOperationConstraints'],
        '_739': ['ManufacturingProcessControls'],
        '_740': ['RackSimulationCalculator'],
        '_741': ['RoughCutterSimulation'],
        '_742': ['ShaperSimulationCalculator'],
        '_743': ['ShavingSimulationCalculator'],
        '_744': ['VirtualSimulationCalculator'],
        '_745': ['WormGrinderSimulationCalculator'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
