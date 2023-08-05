"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2168 import AxialFeedJournalBearing
    from ._2169 import AxialGrooveJournalBearing
    from ._2170 import AxialHoleJournalBearing
    from ._2171 import CircumferentialFeedJournalBearing
    from ._2172 import CylindricalHousingJournalBearing
    from ._2173 import MachineryEncasedJournalBearing
    from ._2174 import PadFluidFilmBearing
    from ._2175 import PedestalJournalBearing
    from ._2176 import PlainGreaseFilledJournalBearing
    from ._2177 import PlainGreaseFilledJournalBearingHousingType
    from ._2178 import PlainJournalBearing
    from ._2179 import PlainJournalHousing
    from ._2180 import PlainOilFedJournalBearing
    from ._2181 import TiltingPadJournalBearing
    from ._2182 import TiltingPadThrustBearing
else:
    import_structure = {
        '_2168': ['AxialFeedJournalBearing'],
        '_2169': ['AxialGrooveJournalBearing'],
        '_2170': ['AxialHoleJournalBearing'],
        '_2171': ['CircumferentialFeedJournalBearing'],
        '_2172': ['CylindricalHousingJournalBearing'],
        '_2173': ['MachineryEncasedJournalBearing'],
        '_2174': ['PadFluidFilmBearing'],
        '_2175': ['PedestalJournalBearing'],
        '_2176': ['PlainGreaseFilledJournalBearing'],
        '_2177': ['PlainGreaseFilledJournalBearingHousingType'],
        '_2178': ['PlainJournalBearing'],
        '_2179': ['PlainJournalHousing'],
        '_2180': ['PlainOilFedJournalBearing'],
        '_2181': ['TiltingPadJournalBearing'],
        '_2182': ['TiltingPadThrustBearing'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
