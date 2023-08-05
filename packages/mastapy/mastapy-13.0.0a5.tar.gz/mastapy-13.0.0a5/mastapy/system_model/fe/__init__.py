"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2338 import AlignConnectedComponentOptions
    from ._2339 import AlignmentMethod
    from ._2340 import AlignmentMethodForRaceBearing
    from ._2341 import AlignmentUsingAxialNodePositions
    from ._2342 import AngleSource
    from ._2343 import BaseFEWithSelection
    from ._2344 import BatchOperations
    from ._2345 import BearingNodeAlignmentOption
    from ._2346 import BearingNodeOption
    from ._2347 import BearingRaceNodeLink
    from ._2348 import BearingRacePosition
    from ._2349 import ComponentOrientationOption
    from ._2350 import ContactPairWithSelection
    from ._2351 import CoordinateSystemWithSelection
    from ._2352 import CreateConnectedComponentOptions
    from ._2353 import DegreeOfFreedomBoundaryCondition
    from ._2354 import DegreeOfFreedomBoundaryConditionAngular
    from ._2355 import DegreeOfFreedomBoundaryConditionLinear
    from ._2356 import ElectricMachineDataSet
    from ._2357 import ElectricMachineDynamicLoadData
    from ._2358 import ElementFaceGroupWithSelection
    from ._2359 import ElementPropertiesWithSelection
    from ._2360 import FEEntityGroupWithSelection
    from ._2361 import FEExportSettings
    from ._2362 import FEPartDRIVASurfaceSelection
    from ._2363 import FEPartWithBatchOptions
    from ._2364 import FEStiffnessGeometry
    from ._2365 import FEStiffnessTester
    from ._2366 import FESubstructure
    from ._2367 import FESubstructureExportOptions
    from ._2368 import FESubstructureNode
    from ._2369 import FESubstructureNodeModeShape
    from ._2370 import FESubstructureNodeModeShapes
    from ._2371 import FESubstructureType
    from ._2372 import FESubstructureWithBatchOptions
    from ._2373 import FESubstructureWithSelection
    from ._2374 import FESubstructureWithSelectionComponents
    from ._2375 import FESubstructureWithSelectionForHarmonicAnalysis
    from ._2376 import FESubstructureWithSelectionForModalAnalysis
    from ._2377 import FESubstructureWithSelectionForStaticAnalysis
    from ._2378 import GearMeshingOptions
    from ._2379 import IndependentMASTACreatedCondensationNode
    from ._2380 import LinkComponentAxialPositionErrorReporter
    from ._2381 import LinkNodeSource
    from ._2382 import MaterialPropertiesWithSelection
    from ._2383 import NodeBoundaryConditionStaticAnalysis
    from ._2384 import NodeGroupWithSelection
    from ._2385 import NodeSelectionDepthOption
    from ._2386 import OptionsWhenExternalFEFileAlreadyExists
    from ._2387 import PerLinkExportOptions
    from ._2388 import PerNodeExportOptions
    from ._2389 import RaceBearingFE
    from ._2390 import RaceBearingFESystemDeflection
    from ._2391 import RaceBearingFEWithSelection
    from ._2392 import ReplacedShaftSelectionHelper
    from ._2393 import SystemDeflectionFEExportOptions
    from ._2394 import ThermalExpansionOption
else:
    import_structure = {
        '_2338': ['AlignConnectedComponentOptions'],
        '_2339': ['AlignmentMethod'],
        '_2340': ['AlignmentMethodForRaceBearing'],
        '_2341': ['AlignmentUsingAxialNodePositions'],
        '_2342': ['AngleSource'],
        '_2343': ['BaseFEWithSelection'],
        '_2344': ['BatchOperations'],
        '_2345': ['BearingNodeAlignmentOption'],
        '_2346': ['BearingNodeOption'],
        '_2347': ['BearingRaceNodeLink'],
        '_2348': ['BearingRacePosition'],
        '_2349': ['ComponentOrientationOption'],
        '_2350': ['ContactPairWithSelection'],
        '_2351': ['CoordinateSystemWithSelection'],
        '_2352': ['CreateConnectedComponentOptions'],
        '_2353': ['DegreeOfFreedomBoundaryCondition'],
        '_2354': ['DegreeOfFreedomBoundaryConditionAngular'],
        '_2355': ['DegreeOfFreedomBoundaryConditionLinear'],
        '_2356': ['ElectricMachineDataSet'],
        '_2357': ['ElectricMachineDynamicLoadData'],
        '_2358': ['ElementFaceGroupWithSelection'],
        '_2359': ['ElementPropertiesWithSelection'],
        '_2360': ['FEEntityGroupWithSelection'],
        '_2361': ['FEExportSettings'],
        '_2362': ['FEPartDRIVASurfaceSelection'],
        '_2363': ['FEPartWithBatchOptions'],
        '_2364': ['FEStiffnessGeometry'],
        '_2365': ['FEStiffnessTester'],
        '_2366': ['FESubstructure'],
        '_2367': ['FESubstructureExportOptions'],
        '_2368': ['FESubstructureNode'],
        '_2369': ['FESubstructureNodeModeShape'],
        '_2370': ['FESubstructureNodeModeShapes'],
        '_2371': ['FESubstructureType'],
        '_2372': ['FESubstructureWithBatchOptions'],
        '_2373': ['FESubstructureWithSelection'],
        '_2374': ['FESubstructureWithSelectionComponents'],
        '_2375': ['FESubstructureWithSelectionForHarmonicAnalysis'],
        '_2376': ['FESubstructureWithSelectionForModalAnalysis'],
        '_2377': ['FESubstructureWithSelectionForStaticAnalysis'],
        '_2378': ['GearMeshingOptions'],
        '_2379': ['IndependentMASTACreatedCondensationNode'],
        '_2380': ['LinkComponentAxialPositionErrorReporter'],
        '_2381': ['LinkNodeSource'],
        '_2382': ['MaterialPropertiesWithSelection'],
        '_2383': ['NodeBoundaryConditionStaticAnalysis'],
        '_2384': ['NodeGroupWithSelection'],
        '_2385': ['NodeSelectionDepthOption'],
        '_2386': ['OptionsWhenExternalFEFileAlreadyExists'],
        '_2387': ['PerLinkExportOptions'],
        '_2388': ['PerNodeExportOptions'],
        '_2389': ['RaceBearingFE'],
        '_2390': ['RaceBearingFESystemDeflection'],
        '_2391': ['RaceBearingFEWithSelection'],
        '_2392': ['ReplacedShaftSelectionHelper'],
        '_2393': ['SystemDeflectionFEExportOptions'],
        '_2394': ['ThermalExpansionOption'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
