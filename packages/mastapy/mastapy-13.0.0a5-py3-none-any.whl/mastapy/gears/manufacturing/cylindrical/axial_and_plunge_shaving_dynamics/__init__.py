"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._746 import ActiveProfileRangeCalculationSource
    from ._747 import AxialShaverRedressing
    from ._748 import ConventionalShavingDynamics
    from ._749 import ConventionalShavingDynamicsCalculationForDesignedGears
    from ._750 import ConventionalShavingDynamicsCalculationForHobbedGears
    from ._751 import ConventionalShavingDynamicsViewModel
    from ._752 import PlungeShaverDynamics
    from ._753 import PlungeShaverDynamicSettings
    from ._754 import PlungeShaverRedressing
    from ._755 import PlungeShavingDynamicsCalculationForDesignedGears
    from ._756 import PlungeShavingDynamicsCalculationForHobbedGears
    from ._757 import PlungeShavingDynamicsViewModel
    from ._758 import RedressingSettings
    from ._759 import RollAngleRangeRelativeToAccuracy
    from ._760 import RollAngleReportObject
    from ._761 import ShaverRedressing
    from ._762 import ShavingDynamics
    from ._763 import ShavingDynamicsCalculation
    from ._764 import ShavingDynamicsCalculationForDesignedGears
    from ._765 import ShavingDynamicsCalculationForHobbedGears
    from ._766 import ShavingDynamicsConfiguration
    from ._767 import ShavingDynamicsViewModel
    from ._768 import ShavingDynamicsViewModelBase
else:
    import_structure = {
        '_746': ['ActiveProfileRangeCalculationSource'],
        '_747': ['AxialShaverRedressing'],
        '_748': ['ConventionalShavingDynamics'],
        '_749': ['ConventionalShavingDynamicsCalculationForDesignedGears'],
        '_750': ['ConventionalShavingDynamicsCalculationForHobbedGears'],
        '_751': ['ConventionalShavingDynamicsViewModel'],
        '_752': ['PlungeShaverDynamics'],
        '_753': ['PlungeShaverDynamicSettings'],
        '_754': ['PlungeShaverRedressing'],
        '_755': ['PlungeShavingDynamicsCalculationForDesignedGears'],
        '_756': ['PlungeShavingDynamicsCalculationForHobbedGears'],
        '_757': ['PlungeShavingDynamicsViewModel'],
        '_758': ['RedressingSettings'],
        '_759': ['RollAngleRangeRelativeToAccuracy'],
        '_760': ['RollAngleReportObject'],
        '_761': ['ShaverRedressing'],
        '_762': ['ShavingDynamics'],
        '_763': ['ShavingDynamicsCalculation'],
        '_764': ['ShavingDynamicsCalculationForDesignedGears'],
        '_765': ['ShavingDynamicsCalculationForHobbedGears'],
        '_766': ['ShavingDynamicsConfiguration'],
        '_767': ['ShavingDynamicsViewModel'],
        '_768': ['ShavingDynamicsViewModelBase'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
