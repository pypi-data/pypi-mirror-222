"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2105 import LoadedFluidFilmBearingPad
    from ._2106 import LoadedFluidFilmBearingResults
    from ._2107 import LoadedGreaseFilledJournalBearingResults
    from ._2108 import LoadedPadFluidFilmBearingResults
    from ._2109 import LoadedPlainJournalBearingResults
    from ._2110 import LoadedPlainJournalBearingRow
    from ._2111 import LoadedPlainOilFedJournalBearing
    from ._2112 import LoadedPlainOilFedJournalBearingRow
    from ._2113 import LoadedTiltingJournalPad
    from ._2114 import LoadedTiltingPadJournalBearingResults
    from ._2115 import LoadedTiltingPadThrustBearingResults
    from ._2116 import LoadedTiltingThrustPad
else:
    import_structure = {
        '_2105': ['LoadedFluidFilmBearingPad'],
        '_2106': ['LoadedFluidFilmBearingResults'],
        '_2107': ['LoadedGreaseFilledJournalBearingResults'],
        '_2108': ['LoadedPadFluidFilmBearingResults'],
        '_2109': ['LoadedPlainJournalBearingResults'],
        '_2110': ['LoadedPlainJournalBearingRow'],
        '_2111': ['LoadedPlainOilFedJournalBearing'],
        '_2112': ['LoadedPlainOilFedJournalBearingRow'],
        '_2113': ['LoadedTiltingJournalPad'],
        '_2114': ['LoadedTiltingPadJournalBearingResults'],
        '_2115': ['LoadedTiltingPadThrustBearingResults'],
        '_2116': ['LoadedTiltingThrustPad'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
