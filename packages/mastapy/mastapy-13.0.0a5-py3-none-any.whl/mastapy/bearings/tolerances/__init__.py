"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1888 import BearingConnectionComponent
    from ._1889 import InternalClearanceClass
    from ._1890 import BearingToleranceClass
    from ._1891 import BearingToleranceDefinitionOptions
    from ._1892 import FitType
    from ._1893 import InnerRingTolerance
    from ._1894 import InnerSupportTolerance
    from ._1895 import InterferenceDetail
    from ._1896 import InterferenceTolerance
    from ._1897 import ITDesignation
    from ._1898 import MountingSleeveDiameterDetail
    from ._1899 import OuterRingTolerance
    from ._1900 import OuterSupportTolerance
    from ._1901 import RaceDetail
    from ._1902 import RaceRoundnessAtAngle
    from ._1903 import RadialSpecificationMethod
    from ._1904 import RingTolerance
    from ._1905 import RoundnessSpecification
    from ._1906 import RoundnessSpecificationType
    from ._1907 import SupportDetail
    from ._1908 import SupportMaterialSource
    from ._1909 import SupportTolerance
    from ._1910 import SupportToleranceLocationDesignation
    from ._1911 import ToleranceCombination
    from ._1912 import TypeOfFit
else:
    import_structure = {
        '_1888': ['BearingConnectionComponent'],
        '_1889': ['InternalClearanceClass'],
        '_1890': ['BearingToleranceClass'],
        '_1891': ['BearingToleranceDefinitionOptions'],
        '_1892': ['FitType'],
        '_1893': ['InnerRingTolerance'],
        '_1894': ['InnerSupportTolerance'],
        '_1895': ['InterferenceDetail'],
        '_1896': ['InterferenceTolerance'],
        '_1897': ['ITDesignation'],
        '_1898': ['MountingSleeveDiameterDetail'],
        '_1899': ['OuterRingTolerance'],
        '_1900': ['OuterSupportTolerance'],
        '_1901': ['RaceDetail'],
        '_1902': ['RaceRoundnessAtAngle'],
        '_1903': ['RadialSpecificationMethod'],
        '_1904': ['RingTolerance'],
        '_1905': ['RoundnessSpecification'],
        '_1906': ['RoundnessSpecificationType'],
        '_1907': ['SupportDetail'],
        '_1908': ['SupportMaterialSource'],
        '_1909': ['SupportTolerance'],
        '_1910': ['SupportToleranceLocationDesignation'],
        '_1911': ['ToleranceCombination'],
        '_1912': ['TypeOfFit'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
