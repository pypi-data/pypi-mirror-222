"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._639 import CalculationError
    from ._640 import ChartType
    from ._641 import GearPointCalculationError
    from ._642 import MicroGeometryDefinitionMethod
    from ._643 import MicroGeometryDefinitionType
    from ._644 import PlungeShaverCalculation
    from ._645 import PlungeShaverCalculationInputs
    from ._646 import PlungeShaverGeneration
    from ._647 import PlungeShaverInputsAndMicroGeometry
    from ._648 import PlungeShaverOutputs
    from ._649 import PlungeShaverSettings
    from ._650 import PointOfInterest
    from ._651 import RealPlungeShaverOutputs
    from ._652 import ShaverPointCalculationError
    from ._653 import ShaverPointOfInterest
    from ._654 import VirtualPlungeShaverOutputs
else:
    import_structure = {
        '_639': ['CalculationError'],
        '_640': ['ChartType'],
        '_641': ['GearPointCalculationError'],
        '_642': ['MicroGeometryDefinitionMethod'],
        '_643': ['MicroGeometryDefinitionType'],
        '_644': ['PlungeShaverCalculation'],
        '_645': ['PlungeShaverCalculationInputs'],
        '_646': ['PlungeShaverGeneration'],
        '_647': ['PlungeShaverInputsAndMicroGeometry'],
        '_648': ['PlungeShaverOutputs'],
        '_649': ['PlungeShaverSettings'],
        '_650': ['PointOfInterest'],
        '_651': ['RealPlungeShaverOutputs'],
        '_652': ['ShaverPointCalculationError'],
        '_653': ['ShaverPointOfInterest'],
        '_654': ['VirtualPlungeShaverOutputs'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
