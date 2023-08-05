"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2416 import Assembly
    from ._2417 import AbstractAssembly
    from ._2418 import AbstractShaft
    from ._2419 import AbstractShaftOrHousing
    from ._2420 import AGMALoadSharingTableApplicationLevel
    from ._2421 import AxialInternalClearanceTolerance
    from ._2422 import Bearing
    from ._2423 import BearingF0InputMethod
    from ._2424 import BearingRaceMountingOptions
    from ._2425 import Bolt
    from ._2426 import BoltedJoint
    from ._2427 import Component
    from ._2428 import ComponentsConnectedResult
    from ._2429 import ConnectedSockets
    from ._2430 import Connector
    from ._2431 import Datum
    from ._2432 import ElectricMachineSearchRegionSpecificationMethod
    from ._2433 import EnginePartLoad
    from ._2434 import EngineSpeed
    from ._2435 import ExternalCADModel
    from ._2436 import FEPart
    from ._2437 import FlexiblePinAssembly
    from ._2438 import GuideDxfModel
    from ._2439 import GuideImage
    from ._2440 import GuideModelUsage
    from ._2441 import InnerBearingRaceMountingOptions
    from ._2442 import InternalClearanceTolerance
    from ._2443 import LoadSharingModes
    from ._2444 import LoadSharingSettings
    from ._2445 import MassDisc
    from ._2446 import MeasurementComponent
    from ._2447 import MountableComponent
    from ._2448 import OilLevelSpecification
    from ._2449 import OilSeal
    from ._2450 import OuterBearingRaceMountingOptions
    from ._2451 import Part
    from ._2452 import PlanetCarrier
    from ._2453 import PlanetCarrierSettings
    from ._2454 import PointLoad
    from ._2455 import PowerLoad
    from ._2456 import RadialInternalClearanceTolerance
    from ._2457 import RootAssembly
    from ._2458 import ShaftDiameterModificationDueToRollingBearingRing
    from ._2459 import SpecialisedAssembly
    from ._2460 import UnbalancedMass
    from ._2461 import UnbalancedMassInclusionOption
    from ._2462 import VirtualComponent
    from ._2463 import WindTurbineBladeModeDetails
    from ._2464 import WindTurbineSingleBladeDetails
else:
    import_structure = {
        '_2416': ['Assembly'],
        '_2417': ['AbstractAssembly'],
        '_2418': ['AbstractShaft'],
        '_2419': ['AbstractShaftOrHousing'],
        '_2420': ['AGMALoadSharingTableApplicationLevel'],
        '_2421': ['AxialInternalClearanceTolerance'],
        '_2422': ['Bearing'],
        '_2423': ['BearingF0InputMethod'],
        '_2424': ['BearingRaceMountingOptions'],
        '_2425': ['Bolt'],
        '_2426': ['BoltedJoint'],
        '_2427': ['Component'],
        '_2428': ['ComponentsConnectedResult'],
        '_2429': ['ConnectedSockets'],
        '_2430': ['Connector'],
        '_2431': ['Datum'],
        '_2432': ['ElectricMachineSearchRegionSpecificationMethod'],
        '_2433': ['EnginePartLoad'],
        '_2434': ['EngineSpeed'],
        '_2435': ['ExternalCADModel'],
        '_2436': ['FEPart'],
        '_2437': ['FlexiblePinAssembly'],
        '_2438': ['GuideDxfModel'],
        '_2439': ['GuideImage'],
        '_2440': ['GuideModelUsage'],
        '_2441': ['InnerBearingRaceMountingOptions'],
        '_2442': ['InternalClearanceTolerance'],
        '_2443': ['LoadSharingModes'],
        '_2444': ['LoadSharingSettings'],
        '_2445': ['MassDisc'],
        '_2446': ['MeasurementComponent'],
        '_2447': ['MountableComponent'],
        '_2448': ['OilLevelSpecification'],
        '_2449': ['OilSeal'],
        '_2450': ['OuterBearingRaceMountingOptions'],
        '_2451': ['Part'],
        '_2452': ['PlanetCarrier'],
        '_2453': ['PlanetCarrierSettings'],
        '_2454': ['PointLoad'],
        '_2455': ['PowerLoad'],
        '_2456': ['RadialInternalClearanceTolerance'],
        '_2457': ['RootAssembly'],
        '_2458': ['ShaftDiameterModificationDueToRollingBearingRing'],
        '_2459': ['SpecialisedAssembly'],
        '_2460': ['UnbalancedMass'],
        '_2461': ['UnbalancedMassInclusionOption'],
        '_2462': ['VirtualComponent'],
        '_2463': ['WindTurbineBladeModeDetails'],
        '_2464': ['WindTurbineSingleBladeDetails'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
