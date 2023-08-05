"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1413 import AGMA6123SplineHalfRating
    from ._1414 import AGMA6123SplineJointRating
    from ._1415 import DIN5466SplineHalfRating
    from ._1416 import DIN5466SplineRating
    from ._1417 import GBT17855SplineHalfRating
    from ._1418 import GBT17855SplineJointRating
    from ._1419 import SAESplineHalfRating
    from ._1420 import SAESplineJointRating
    from ._1421 import SplineHalfRating
    from ._1422 import SplineJointRating
else:
    import_structure = {
        '_1413': ['AGMA6123SplineHalfRating'],
        '_1414': ['AGMA6123SplineJointRating'],
        '_1415': ['DIN5466SplineHalfRating'],
        '_1416': ['DIN5466SplineRating'],
        '_1417': ['GBT17855SplineHalfRating'],
        '_1418': ['GBT17855SplineJointRating'],
        '_1419': ['SAESplineHalfRating'],
        '_1420': ['SAESplineJointRating'],
        '_1421': ['SplineHalfRating'],
        '_1422': ['SplineJointRating'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
