"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._769 import AbstractTCA
    from ._770 import BevelMachineSettingOptimizationResult
    from ._771 import ConicalFlankDeviationsData
    from ._772 import ConicalGearManufacturingAnalysis
    from ._773 import ConicalGearManufacturingConfig
    from ._774 import ConicalGearMicroGeometryConfig
    from ._775 import ConicalGearMicroGeometryConfigBase
    from ._776 import ConicalMeshedGearManufacturingAnalysis
    from ._777 import ConicalMeshedWheelFlankManufacturingConfig
    from ._778 import ConicalMeshFlankManufacturingConfig
    from ._779 import ConicalMeshFlankMicroGeometryConfig
    from ._780 import ConicalMeshFlankNURBSMicroGeometryConfig
    from ._781 import ConicalMeshManufacturingAnalysis
    from ._782 import ConicalMeshManufacturingConfig
    from ._783 import ConicalMeshMicroGeometryConfig
    from ._784 import ConicalMeshMicroGeometryConfigBase
    from ._785 import ConicalPinionManufacturingConfig
    from ._786 import ConicalPinionMicroGeometryConfig
    from ._787 import ConicalSetManufacturingAnalysis
    from ._788 import ConicalSetManufacturingConfig
    from ._789 import ConicalSetMicroGeometryConfig
    from ._790 import ConicalSetMicroGeometryConfigBase
    from ._791 import ConicalWheelManufacturingConfig
    from ._792 import EaseOffBasedTCA
    from ._793 import FlankMeasurementBorder
    from ._794 import HypoidAdvancedLibrary
    from ._795 import MachineTypes
    from ._796 import ManufacturingMachine
    from ._797 import ManufacturingMachineDatabase
    from ._798 import PinionBevelGeneratingModifiedRollMachineSettings
    from ._799 import PinionBevelGeneratingTiltMachineSettings
    from ._800 import PinionConcave
    from ._801 import PinionConicalMachineSettingsSpecified
    from ._802 import PinionConvex
    from ._803 import PinionFinishMachineSettings
    from ._804 import PinionHypoidFormateTiltMachineSettings
    from ._805 import PinionHypoidGeneratingTiltMachineSettings
    from ._806 import PinionMachineSettingsSMT
    from ._807 import PinionRoughMachineSetting
    from ._808 import Wheel
    from ._809 import WheelFormatMachineTypes
else:
    import_structure = {
        '_769': ['AbstractTCA'],
        '_770': ['BevelMachineSettingOptimizationResult'],
        '_771': ['ConicalFlankDeviationsData'],
        '_772': ['ConicalGearManufacturingAnalysis'],
        '_773': ['ConicalGearManufacturingConfig'],
        '_774': ['ConicalGearMicroGeometryConfig'],
        '_775': ['ConicalGearMicroGeometryConfigBase'],
        '_776': ['ConicalMeshedGearManufacturingAnalysis'],
        '_777': ['ConicalMeshedWheelFlankManufacturingConfig'],
        '_778': ['ConicalMeshFlankManufacturingConfig'],
        '_779': ['ConicalMeshFlankMicroGeometryConfig'],
        '_780': ['ConicalMeshFlankNURBSMicroGeometryConfig'],
        '_781': ['ConicalMeshManufacturingAnalysis'],
        '_782': ['ConicalMeshManufacturingConfig'],
        '_783': ['ConicalMeshMicroGeometryConfig'],
        '_784': ['ConicalMeshMicroGeometryConfigBase'],
        '_785': ['ConicalPinionManufacturingConfig'],
        '_786': ['ConicalPinionMicroGeometryConfig'],
        '_787': ['ConicalSetManufacturingAnalysis'],
        '_788': ['ConicalSetManufacturingConfig'],
        '_789': ['ConicalSetMicroGeometryConfig'],
        '_790': ['ConicalSetMicroGeometryConfigBase'],
        '_791': ['ConicalWheelManufacturingConfig'],
        '_792': ['EaseOffBasedTCA'],
        '_793': ['FlankMeasurementBorder'],
        '_794': ['HypoidAdvancedLibrary'],
        '_795': ['MachineTypes'],
        '_796': ['ManufacturingMachine'],
        '_797': ['ManufacturingMachineDatabase'],
        '_798': ['PinionBevelGeneratingModifiedRollMachineSettings'],
        '_799': ['PinionBevelGeneratingTiltMachineSettings'],
        '_800': ['PinionConcave'],
        '_801': ['PinionConicalMachineSettingsSpecified'],
        '_802': ['PinionConvex'],
        '_803': ['PinionFinishMachineSettings'],
        '_804': ['PinionHypoidFormateTiltMachineSettings'],
        '_805': ['PinionHypoidGeneratingTiltMachineSettings'],
        '_806': ['PinionMachineSettingsSMT'],
        '_807': ['PinionRoughMachineSetting'],
        '_808': ['Wheel'],
        '_809': ['WheelFormatMachineTypes'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
