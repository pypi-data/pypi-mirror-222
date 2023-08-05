"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2163 import AbstractXmlVariableAssignment
    from ._2164 import BearingImportFile
    from ._2165 import RollingBearingImporter
    from ._2166 import XmlBearingTypeMapping
    from ._2167 import XMLVariableAssignment
else:
    import_structure = {
        '_2163': ['AbstractXmlVariableAssignment'],
        '_2164': ['BearingImportFile'],
        '_2165': ['RollingBearingImporter'],
        '_2166': ['XmlBearingTypeMapping'],
        '_2167': ['XMLVariableAssignment'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
