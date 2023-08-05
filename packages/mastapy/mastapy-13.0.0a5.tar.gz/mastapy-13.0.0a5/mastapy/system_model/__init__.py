"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2187 import Design
    from ._2188 import ComponentDampingOption
    from ._2189 import ConceptCouplingSpeedRatioSpecificationMethod
    from ._2190 import DesignEntity
    from ._2191 import DesignEntityId
    from ._2192 import DesignSettings
    from ._2193 import DutyCycleImporter
    from ._2194 import DutyCycleImporterDesignEntityMatch
    from ._2195 import ElectricMachineGroup
    from ._2196 import ExternalFullFELoader
    from ._2197 import HypoidWindUpRemovalMethod
    from ._2198 import IncludeDutyCycleOption
    from ._2199 import MASTASettings
    from ._2200 import MemorySummary
    from ._2201 import MeshStiffnessModel
    from ._2202 import PlanetPinManufacturingErrorsCoordinateSystem
    from ._2203 import PowerLoadDragTorqueSpecificationMethod
    from ._2204 import PowerLoadInputTorqueSpecificationMethod
    from ._2205 import PowerLoadPIDControlSpeedInputType
    from ._2206 import PowerLoadType
    from ._2207 import RelativeComponentAlignment
    from ._2208 import RelativeOffsetOption
    from ._2209 import SystemReporting
    from ._2210 import ThermalExpansionOptionForGroundedNodes
    from ._2211 import TransmissionTemperatureSet
else:
    import_structure = {
        '_2187': ['Design'],
        '_2188': ['ComponentDampingOption'],
        '_2189': ['ConceptCouplingSpeedRatioSpecificationMethod'],
        '_2190': ['DesignEntity'],
        '_2191': ['DesignEntityId'],
        '_2192': ['DesignSettings'],
        '_2193': ['DutyCycleImporter'],
        '_2194': ['DutyCycleImporterDesignEntityMatch'],
        '_2195': ['ElectricMachineGroup'],
        '_2196': ['ExternalFullFELoader'],
        '_2197': ['HypoidWindUpRemovalMethod'],
        '_2198': ['IncludeDutyCycleOption'],
        '_2199': ['MASTASettings'],
        '_2200': ['MemorySummary'],
        '_2201': ['MeshStiffnessModel'],
        '_2202': ['PlanetPinManufacturingErrorsCoordinateSystem'],
        '_2203': ['PowerLoadDragTorqueSpecificationMethod'],
        '_2204': ['PowerLoadInputTorqueSpecificationMethod'],
        '_2205': ['PowerLoadPIDControlSpeedInputType'],
        '_2206': ['PowerLoadType'],
        '_2207': ['RelativeComponentAlignment'],
        '_2208': ['RelativeOffsetOption'],
        '_2209': ['SystemReporting'],
        '_2210': ['ThermalExpansionOptionForGroundedNodes'],
        '_2211': ['TransmissionTemperatureSet'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
