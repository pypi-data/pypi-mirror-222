"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5645 import AbstractAssemblyStaticLoadCaseGroup
    from ._5646 import ComponentStaticLoadCaseGroup
    from ._5647 import ConnectionStaticLoadCaseGroup
    from ._5648 import DesignEntityStaticLoadCaseGroup
    from ._5649 import GearSetStaticLoadCaseGroup
    from ._5650 import PartStaticLoadCaseGroup
else:
    import_structure = {
        '_5645': ['AbstractAssemblyStaticLoadCaseGroup'],
        '_5646': ['ComponentStaticLoadCaseGroup'],
        '_5647': ['ConnectionStaticLoadCaseGroup'],
        '_5648': ['DesignEntityStaticLoadCaseGroup'],
        '_5649': ['GearSetStaticLoadCaseGroup'],
        '_5650': ['PartStaticLoadCaseGroup'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
