"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._606 import CutterFlankSections
    from ._607 import CylindricalCutterDatabase
    from ._608 import CylindricalGearBlank
    from ._609 import CylindricalGearManufacturingConfig
    from ._610 import CylindricalGearSpecifiedMicroGeometry
    from ._611 import CylindricalGearSpecifiedProfile
    from ._612 import CylindricalHobDatabase
    from ._613 import CylindricalManufacturedGearDutyCycle
    from ._614 import CylindricalManufacturedGearLoadCase
    from ._615 import CylindricalManufacturedGearMeshDutyCycle
    from ._616 import CylindricalManufacturedGearMeshLoadCase
    from ._617 import CylindricalManufacturedGearSetDutyCycle
    from ._618 import CylindricalManufacturedGearSetLoadCase
    from ._619 import CylindricalMeshManufacturingConfig
    from ._620 import CylindricalMftFinishingMethods
    from ._621 import CylindricalMftRoughingMethods
    from ._622 import CylindricalSetManufacturingConfig
    from ._623 import CylindricalShaperDatabase
    from ._624 import Flank
    from ._625 import GearManufacturingConfigurationViewModel
    from ._626 import GearManufacturingConfigurationViewModelPlaceholder
    from ._627 import GearSetConfigViewModel
    from ._628 import HobEdgeTypes
    from ._629 import LeadModificationSegment
    from ._630 import MicroGeometryInputs
    from ._631 import MicroGeometryInputsLead
    from ._632 import MicroGeometryInputsProfile
    from ._633 import ModificationSegment
    from ._634 import ProfileModificationSegment
    from ._635 import SuitableCutterSetup
else:
    import_structure = {
        '_606': ['CutterFlankSections'],
        '_607': ['CylindricalCutterDatabase'],
        '_608': ['CylindricalGearBlank'],
        '_609': ['CylindricalGearManufacturingConfig'],
        '_610': ['CylindricalGearSpecifiedMicroGeometry'],
        '_611': ['CylindricalGearSpecifiedProfile'],
        '_612': ['CylindricalHobDatabase'],
        '_613': ['CylindricalManufacturedGearDutyCycle'],
        '_614': ['CylindricalManufacturedGearLoadCase'],
        '_615': ['CylindricalManufacturedGearMeshDutyCycle'],
        '_616': ['CylindricalManufacturedGearMeshLoadCase'],
        '_617': ['CylindricalManufacturedGearSetDutyCycle'],
        '_618': ['CylindricalManufacturedGearSetLoadCase'],
        '_619': ['CylindricalMeshManufacturingConfig'],
        '_620': ['CylindricalMftFinishingMethods'],
        '_621': ['CylindricalMftRoughingMethods'],
        '_622': ['CylindricalSetManufacturingConfig'],
        '_623': ['CylindricalShaperDatabase'],
        '_624': ['Flank'],
        '_625': ['GearManufacturingConfigurationViewModel'],
        '_626': ['GearManufacturingConfigurationViewModelPlaceholder'],
        '_627': ['GearSetConfigViewModel'],
        '_628': ['HobEdgeTypes'],
        '_629': ['LeadModificationSegment'],
        '_630': ['MicroGeometryInputs'],
        '_631': ['MicroGeometryInputsLead'],
        '_632': ['MicroGeometryInputsProfile'],
        '_633': ['ModificationSegment'],
        '_634': ['ProfileModificationSegment'],
        '_635': ['SuitableCutterSetup'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
