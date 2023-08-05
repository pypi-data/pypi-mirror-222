"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1568 import Command
    from ._1569 import AnalysisRunInformation
    from ._1570 import DispatcherHelper
    from ._1571 import EnvironmentSummary
    from ._1572 import ExternalFullFEFileOption
    from ._1573 import FileHistory
    from ._1574 import FileHistoryItem
    from ._1575 import FolderMonitor
    from ._1577 import IndependentReportablePropertiesBase
    from ._1578 import InputNamePrompter
    from ._1579 import IntegerRange
    from ._1580 import LoadCaseOverrideOption
    from ._1581 import MethodOutcome
    from ._1582 import MethodOutcomeWithResult
    from ._1583 import MKLVersion
    from ._1584 import NumberFormatInfoSummary
    from ._1585 import PerMachineSettings
    from ._1586 import PersistentSingleton
    from ._1587 import ProgramSettings
    from ._1588 import PushbulletSettings
    from ._1589 import RoundingMethods
    from ._1590 import SelectableFolder
    from ._1591 import SystemDirectory
    from ._1592 import SystemDirectoryPopulator
else:
    import_structure = {
        '_1568': ['Command'],
        '_1569': ['AnalysisRunInformation'],
        '_1570': ['DispatcherHelper'],
        '_1571': ['EnvironmentSummary'],
        '_1572': ['ExternalFullFEFileOption'],
        '_1573': ['FileHistory'],
        '_1574': ['FileHistoryItem'],
        '_1575': ['FolderMonitor'],
        '_1577': ['IndependentReportablePropertiesBase'],
        '_1578': ['InputNamePrompter'],
        '_1579': ['IntegerRange'],
        '_1580': ['LoadCaseOverrideOption'],
        '_1581': ['MethodOutcome'],
        '_1582': ['MethodOutcomeWithResult'],
        '_1583': ['MKLVersion'],
        '_1584': ['NumberFormatInfoSummary'],
        '_1585': ['PerMachineSettings'],
        '_1586': ['PersistentSingleton'],
        '_1587': ['ProgramSettings'],
        '_1588': ['PushbulletSettings'],
        '_1589': ['RoundingMethods'],
        '_1590': ['SelectableFolder'],
        '_1591': ['SystemDirectory'],
        '_1592': ['SystemDirectoryPopulator'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
