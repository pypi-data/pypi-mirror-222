"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6505 import ExcelBatchDutyCycleCreator
    from ._6506 import ExcelBatchDutyCycleSpectraCreatorDetails
    from ._6507 import ExcelFileDetails
    from ._6508 import ExcelSheet
    from ._6509 import ExcelSheetDesignStateSelector
    from ._6510 import MASTAFileDetails
else:
    import_structure = {
        '_6505': ['ExcelBatchDutyCycleCreator'],
        '_6506': ['ExcelBatchDutyCycleSpectraCreatorDetails'],
        '_6507': ['ExcelFileDetails'],
        '_6508': ['ExcelSheet'],
        '_6509': ['ExcelSheetDesignStateSelector'],
        '_6510': ['MASTAFileDetails'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
