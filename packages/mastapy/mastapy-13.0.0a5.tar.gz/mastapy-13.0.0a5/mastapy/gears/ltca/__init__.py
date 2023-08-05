"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._822 import ConicalGearFilletStressResults
    from ._823 import ConicalGearRootFilletStressResults
    from ._824 import ContactResultType
    from ._825 import CylindricalGearFilletNodeStressResults
    from ._826 import CylindricalGearFilletNodeStressResultsColumn
    from ._827 import CylindricalGearFilletNodeStressResultsRow
    from ._828 import CylindricalGearRootFilletStressResults
    from ._829 import CylindricalMeshedGearLoadDistributionAnalysis
    from ._830 import GearBendingStiffness
    from ._831 import GearBendingStiffnessNode
    from ._832 import GearContactStiffness
    from ._833 import GearContactStiffnessNode
    from ._834 import GearFilletNodeStressResults
    from ._835 import GearFilletNodeStressResultsColumn
    from ._836 import GearFilletNodeStressResultsRow
    from ._837 import GearLoadDistributionAnalysis
    from ._838 import GearMeshLoadDistributionAnalysis
    from ._839 import GearMeshLoadDistributionAtRotation
    from ._840 import GearMeshLoadedContactLine
    from ._841 import GearMeshLoadedContactPoint
    from ._842 import GearRootFilletStressResults
    from ._843 import GearSetLoadDistributionAnalysis
    from ._844 import GearStiffness
    from ._845 import GearStiffnessNode
    from ._846 import MeshedGearLoadDistributionAnalysisAtRotation
    from ._847 import UseAdvancedLTCAOptions
else:
    import_structure = {
        '_822': ['ConicalGearFilletStressResults'],
        '_823': ['ConicalGearRootFilletStressResults'],
        '_824': ['ContactResultType'],
        '_825': ['CylindricalGearFilletNodeStressResults'],
        '_826': ['CylindricalGearFilletNodeStressResultsColumn'],
        '_827': ['CylindricalGearFilletNodeStressResultsRow'],
        '_828': ['CylindricalGearRootFilletStressResults'],
        '_829': ['CylindricalMeshedGearLoadDistributionAnalysis'],
        '_830': ['GearBendingStiffness'],
        '_831': ['GearBendingStiffnessNode'],
        '_832': ['GearContactStiffness'],
        '_833': ['GearContactStiffnessNode'],
        '_834': ['GearFilletNodeStressResults'],
        '_835': ['GearFilletNodeStressResultsColumn'],
        '_836': ['GearFilletNodeStressResultsRow'],
        '_837': ['GearLoadDistributionAnalysis'],
        '_838': ['GearMeshLoadDistributionAnalysis'],
        '_839': ['GearMeshLoadDistributionAtRotation'],
        '_840': ['GearMeshLoadedContactLine'],
        '_841': ['GearMeshLoadedContactPoint'],
        '_842': ['GearRootFilletStressResults'],
        '_843': ['GearSetLoadDistributionAnalysis'],
        '_844': ['GearStiffness'],
        '_845': ['GearStiffnessNode'],
        '_846': ['MeshedGearLoadDistributionAnalysisAtRotation'],
        '_847': ['UseAdvancedLTCAOptions'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
