"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1312 import DynamicForceResults
    from ._1313 import EfficiencyResults
    from ._1314 import ElectricMachineDQModel
    from ._1315 import ElectricMachineMechanicalResults
    from ._1316 import ElectricMachineMechanicalResultsViewable
    from ._1317 import ElectricMachineResults
    from ._1318 import ElectricMachineResultsForConductorTurn
    from ._1319 import ElectricMachineResultsForConductorTurnAtTimeStep
    from ._1320 import ElectricMachineResultsForLineToLine
    from ._1321 import ElectricMachineResultsForOpenCircuitAndOnLoad
    from ._1322 import ElectricMachineResultsForPhase
    from ._1323 import ElectricMachineResultsForPhaseAtTimeStep
    from ._1324 import ElectricMachineResultsForStatorToothAtTimeStep
    from ._1325 import ElectricMachineResultsLineToLineAtTimeStep
    from ._1326 import ElectricMachineResultsTimeStep
    from ._1327 import ElectricMachineResultsTimeStepAtLocation
    from ._1328 import ElectricMachineResultsViewable
    from ._1329 import ElectricMachineForceViewOptions
    from ._1331 import LinearDQModel
    from ._1332 import MaximumTorqueResultsPoints
    from ._1333 import NonLinearDQModel
    from ._1334 import NonLinearDQModelGeneratorSettings
    from ._1335 import OnLoadElectricMachineResults
    from ._1336 import OpenCircuitElectricMachineResults
else:
    import_structure = {
        '_1312': ['DynamicForceResults'],
        '_1313': ['EfficiencyResults'],
        '_1314': ['ElectricMachineDQModel'],
        '_1315': ['ElectricMachineMechanicalResults'],
        '_1316': ['ElectricMachineMechanicalResultsViewable'],
        '_1317': ['ElectricMachineResults'],
        '_1318': ['ElectricMachineResultsForConductorTurn'],
        '_1319': ['ElectricMachineResultsForConductorTurnAtTimeStep'],
        '_1320': ['ElectricMachineResultsForLineToLine'],
        '_1321': ['ElectricMachineResultsForOpenCircuitAndOnLoad'],
        '_1322': ['ElectricMachineResultsForPhase'],
        '_1323': ['ElectricMachineResultsForPhaseAtTimeStep'],
        '_1324': ['ElectricMachineResultsForStatorToothAtTimeStep'],
        '_1325': ['ElectricMachineResultsLineToLineAtTimeStep'],
        '_1326': ['ElectricMachineResultsTimeStep'],
        '_1327': ['ElectricMachineResultsTimeStepAtLocation'],
        '_1328': ['ElectricMachineResultsViewable'],
        '_1329': ['ElectricMachineForceViewOptions'],
        '_1331': ['LinearDQModel'],
        '_1332': ['MaximumTorqueResultsPoints'],
        '_1333': ['NonLinearDQModel'],
        '_1334': ['NonLinearDQModelGeneratorSettings'],
        '_1335': ['OnLoadElectricMachineResults'],
        '_1336': ['OpenCircuitElectricMachineResults'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
