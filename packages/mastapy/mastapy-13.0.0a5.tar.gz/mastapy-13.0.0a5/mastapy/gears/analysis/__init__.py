"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1211 import AbstractGearAnalysis
    from ._1212 import AbstractGearMeshAnalysis
    from ._1213 import AbstractGearSetAnalysis
    from ._1214 import GearDesignAnalysis
    from ._1215 import GearImplementationAnalysis
    from ._1216 import GearImplementationAnalysisDutyCycle
    from ._1217 import GearImplementationDetail
    from ._1218 import GearMeshDesignAnalysis
    from ._1219 import GearMeshImplementationAnalysis
    from ._1220 import GearMeshImplementationAnalysisDutyCycle
    from ._1221 import GearMeshImplementationDetail
    from ._1222 import GearSetDesignAnalysis
    from ._1223 import GearSetGroupDutyCycle
    from ._1224 import GearSetImplementationAnalysis
    from ._1225 import GearSetImplementationAnalysisAbstract
    from ._1226 import GearSetImplementationAnalysisDutyCycle
    from ._1227 import GearSetImplementationDetail
else:
    import_structure = {
        '_1211': ['AbstractGearAnalysis'],
        '_1212': ['AbstractGearMeshAnalysis'],
        '_1213': ['AbstractGearSetAnalysis'],
        '_1214': ['GearDesignAnalysis'],
        '_1215': ['GearImplementationAnalysis'],
        '_1216': ['GearImplementationAnalysisDutyCycle'],
        '_1217': ['GearImplementationDetail'],
        '_1218': ['GearMeshDesignAnalysis'],
        '_1219': ['GearMeshImplementationAnalysis'],
        '_1220': ['GearMeshImplementationAnalysisDutyCycle'],
        '_1221': ['GearMeshImplementationDetail'],
        '_1222': ['GearSetDesignAnalysis'],
        '_1223': ['GearSetGroupDutyCycle'],
        '_1224': ['GearSetImplementationAnalysis'],
        '_1225': ['GearSetImplementationAnalysisAbstract'],
        '_1226': ['GearSetImplementationAnalysisDutyCycle'],
        '_1227': ['GearSetImplementationDetail'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
