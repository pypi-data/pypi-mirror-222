"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._655 import ActiveProcessMethod
    from ._656 import AnalysisMethod
    from ._657 import CalculateLeadDeviationAccuracy
    from ._658 import CalculatePitchDeviationAccuracy
    from ._659 import CalculateProfileDeviationAccuracy
    from ._660 import CentreDistanceOffsetMethod
    from ._661 import CutterHeadSlideError
    from ._662 import GearMountingError
    from ._663 import HobbingProcessCalculation
    from ._664 import HobbingProcessGearShape
    from ._665 import HobbingProcessLeadCalculation
    from ._666 import HobbingProcessMarkOnShaft
    from ._667 import HobbingProcessPitchCalculation
    from ._668 import HobbingProcessProfileCalculation
    from ._669 import HobbingProcessSimulationInput
    from ._670 import HobbingProcessSimulationNew
    from ._671 import HobbingProcessSimulationViewModel
    from ._672 import HobbingProcessTotalModificationCalculation
    from ._673 import HobManufactureError
    from ._674 import HobResharpeningError
    from ._675 import ManufacturedQualityGrade
    from ._676 import MountingError
    from ._677 import ProcessCalculation
    from ._678 import ProcessGearShape
    from ._679 import ProcessLeadCalculation
    from ._680 import ProcessPitchCalculation
    from ._681 import ProcessProfileCalculation
    from ._682 import ProcessSimulationInput
    from ._683 import ProcessSimulationNew
    from ._684 import ProcessSimulationViewModel
    from ._685 import ProcessTotalModificationCalculation
    from ._686 import RackManufactureError
    from ._687 import RackMountingError
    from ._688 import WormGrinderManufactureError
    from ._689 import WormGrindingCutterCalculation
    from ._690 import WormGrindingLeadCalculation
    from ._691 import WormGrindingProcessCalculation
    from ._692 import WormGrindingProcessGearShape
    from ._693 import WormGrindingProcessMarkOnShaft
    from ._694 import WormGrindingProcessPitchCalculation
    from ._695 import WormGrindingProcessProfileCalculation
    from ._696 import WormGrindingProcessSimulationInput
    from ._697 import WormGrindingProcessSimulationNew
    from ._698 import WormGrindingProcessSimulationViewModel
    from ._699 import WormGrindingProcessTotalModificationCalculation
else:
    import_structure = {
        '_655': ['ActiveProcessMethod'],
        '_656': ['AnalysisMethod'],
        '_657': ['CalculateLeadDeviationAccuracy'],
        '_658': ['CalculatePitchDeviationAccuracy'],
        '_659': ['CalculateProfileDeviationAccuracy'],
        '_660': ['CentreDistanceOffsetMethod'],
        '_661': ['CutterHeadSlideError'],
        '_662': ['GearMountingError'],
        '_663': ['HobbingProcessCalculation'],
        '_664': ['HobbingProcessGearShape'],
        '_665': ['HobbingProcessLeadCalculation'],
        '_666': ['HobbingProcessMarkOnShaft'],
        '_667': ['HobbingProcessPitchCalculation'],
        '_668': ['HobbingProcessProfileCalculation'],
        '_669': ['HobbingProcessSimulationInput'],
        '_670': ['HobbingProcessSimulationNew'],
        '_671': ['HobbingProcessSimulationViewModel'],
        '_672': ['HobbingProcessTotalModificationCalculation'],
        '_673': ['HobManufactureError'],
        '_674': ['HobResharpeningError'],
        '_675': ['ManufacturedQualityGrade'],
        '_676': ['MountingError'],
        '_677': ['ProcessCalculation'],
        '_678': ['ProcessGearShape'],
        '_679': ['ProcessLeadCalculation'],
        '_680': ['ProcessPitchCalculation'],
        '_681': ['ProcessProfileCalculation'],
        '_682': ['ProcessSimulationInput'],
        '_683': ['ProcessSimulationNew'],
        '_684': ['ProcessSimulationViewModel'],
        '_685': ['ProcessTotalModificationCalculation'],
        '_686': ['RackManufactureError'],
        '_687': ['RackMountingError'],
        '_688': ['WormGrinderManufactureError'],
        '_689': ['WormGrindingCutterCalculation'],
        '_690': ['WormGrindingLeadCalculation'],
        '_691': ['WormGrindingProcessCalculation'],
        '_692': ['WormGrindingProcessGearShape'],
        '_693': ['WormGrindingProcessMarkOnShaft'],
        '_694': ['WormGrindingProcessPitchCalculation'],
        '_695': ['WormGrindingProcessProfileCalculation'],
        '_696': ['WormGrindingProcessSimulationInput'],
        '_697': ['WormGrindingProcessSimulationNew'],
        '_698': ['WormGrindingProcessSimulationViewModel'],
        '_699': ['WormGrindingProcessTotalModificationCalculation'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
