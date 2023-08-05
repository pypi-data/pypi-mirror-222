"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1423 import AGMA6123SplineJointDutyCycleRating
    from ._1424 import GBT17855SplineJointDutyCycleRating
    from ._1425 import SAESplineJointDutyCycleRating
else:
    import_structure = {
        '_1423': ['AGMA6123SplineJointDutyCycleRating'],
        '_1424': ['GBT17855SplineJointDutyCycleRating'],
        '_1425': ['SAESplineJointDutyCycleRating'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
