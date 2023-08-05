"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1337 import DynamicForceAnalysis
    from ._1338 import DynamicForceLoadCase
    from ._1339 import EfficiencyMapAnalysis
    from ._1340 import EfficiencyMapLoadCase
    from ._1341 import ElectricMachineAnalysis
    from ._1342 import ElectricMachineBasicMechanicalLossSettings
    from ._1343 import ElectricMachineControlStrategy
    from ._1344 import ElectricMachineEfficiencyMapSettings
    from ._1345 import ElectricMachineFEAnalysis
    from ._1346 import ElectricMachineFEMechanicalAnalysis
    from ._1347 import ElectricMachineLoadCase
    from ._1348 import ElectricMachineLoadCaseBase
    from ._1349 import ElectricMachineLoadCaseGroup
    from ._1350 import ElectricMachineMechanicalLoadCase
    from ._1351 import EndWindingInductanceMethod
    from ._1352 import LeadingOrLagging
    from ._1353 import LoadCaseType
    from ._1354 import LoadCaseTypeSelector
    from ._1355 import MotoringOrGenerating
    from ._1356 import NonLinearDQModelMultipleOperatingPointsLoadCase
    from ._1357 import NumberOfStepsPerOperatingPointSpecificationMethod
    from ._1358 import OperatingPointsSpecificationMethod
    from ._1359 import SingleOperatingPointAnalysis
    from ._1360 import SlotDetailForAnalysis
    from ._1361 import SpecifyTorqueOrCurrent
    from ._1362 import SpeedPointsDistribution
    from ._1363 import SpeedTorqueCurveAnalysis
    from ._1364 import SpeedTorqueCurveLoadCase
    from ._1365 import SpeedTorqueLoadCase
    from ._1366 import SpeedTorqueOperatingPoint
    from ._1367 import Temperatures
else:
    import_structure = {
        '_1337': ['DynamicForceAnalysis'],
        '_1338': ['DynamicForceLoadCase'],
        '_1339': ['EfficiencyMapAnalysis'],
        '_1340': ['EfficiencyMapLoadCase'],
        '_1341': ['ElectricMachineAnalysis'],
        '_1342': ['ElectricMachineBasicMechanicalLossSettings'],
        '_1343': ['ElectricMachineControlStrategy'],
        '_1344': ['ElectricMachineEfficiencyMapSettings'],
        '_1345': ['ElectricMachineFEAnalysis'],
        '_1346': ['ElectricMachineFEMechanicalAnalysis'],
        '_1347': ['ElectricMachineLoadCase'],
        '_1348': ['ElectricMachineLoadCaseBase'],
        '_1349': ['ElectricMachineLoadCaseGroup'],
        '_1350': ['ElectricMachineMechanicalLoadCase'],
        '_1351': ['EndWindingInductanceMethod'],
        '_1352': ['LeadingOrLagging'],
        '_1353': ['LoadCaseType'],
        '_1354': ['LoadCaseTypeSelector'],
        '_1355': ['MotoringOrGenerating'],
        '_1356': ['NonLinearDQModelMultipleOperatingPointsLoadCase'],
        '_1357': ['NumberOfStepsPerOperatingPointSpecificationMethod'],
        '_1358': ['OperatingPointsSpecificationMethod'],
        '_1359': ['SingleOperatingPointAnalysis'],
        '_1360': ['SlotDetailForAnalysis'],
        '_1361': ['SpecifyTorqueOrCurrent'],
        '_1362': ['SpeedPointsDistribution'],
        '_1363': ['SpeedTorqueCurveAnalysis'],
        '_1364': ['SpeedTorqueCurveLoadCase'],
        '_1365': ['SpeedTorqueLoadCase'],
        '_1366': ['SpeedTorqueOperatingPoint'],
        '_1367': ['Temperatures'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
