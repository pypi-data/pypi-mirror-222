"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1379 import CustomSplineHalfDesign
    from ._1380 import CustomSplineJointDesign
    from ._1381 import DetailedSplineJointSettings
    from ._1382 import DIN5480SplineHalfDesign
    from ._1383 import DIN5480SplineJointDesign
    from ._1384 import DudleyEffectiveLengthApproximationOption
    from ._1385 import FitTypes
    from ._1386 import GBT3478SplineHalfDesign
    from ._1387 import GBT3478SplineJointDesign
    from ._1388 import HeatTreatmentTypes
    from ._1389 import ISO4156SplineHalfDesign
    from ._1390 import ISO4156SplineJointDesign
    from ._1391 import JISB1603SplineJointDesign
    from ._1392 import ManufacturingTypes
    from ._1393 import Modules
    from ._1394 import PressureAngleTypes
    from ._1395 import RootTypes
    from ._1396 import SAEFatigueLifeFactorTypes
    from ._1397 import SAESplineHalfDesign
    from ._1398 import SAESplineJointDesign
    from ._1399 import SAETorqueCycles
    from ._1400 import SplineDesignTypes
    from ._1401 import FinishingMethods
    from ._1402 import SplineFitClassType
    from ._1403 import SplineFixtureTypes
    from ._1404 import SplineHalfDesign
    from ._1405 import SplineJointDesign
    from ._1406 import SplineMaterial
    from ._1407 import SplineRatingTypes
    from ._1408 import SplineToleranceClassTypes
    from ._1409 import StandardSplineHalfDesign
    from ._1410 import StandardSplineJointDesign
else:
    import_structure = {
        '_1379': ['CustomSplineHalfDesign'],
        '_1380': ['CustomSplineJointDesign'],
        '_1381': ['DetailedSplineJointSettings'],
        '_1382': ['DIN5480SplineHalfDesign'],
        '_1383': ['DIN5480SplineJointDesign'],
        '_1384': ['DudleyEffectiveLengthApproximationOption'],
        '_1385': ['FitTypes'],
        '_1386': ['GBT3478SplineHalfDesign'],
        '_1387': ['GBT3478SplineJointDesign'],
        '_1388': ['HeatTreatmentTypes'],
        '_1389': ['ISO4156SplineHalfDesign'],
        '_1390': ['ISO4156SplineJointDesign'],
        '_1391': ['JISB1603SplineJointDesign'],
        '_1392': ['ManufacturingTypes'],
        '_1393': ['Modules'],
        '_1394': ['PressureAngleTypes'],
        '_1395': ['RootTypes'],
        '_1396': ['SAEFatigueLifeFactorTypes'],
        '_1397': ['SAESplineHalfDesign'],
        '_1398': ['SAESplineJointDesign'],
        '_1399': ['SAETorqueCycles'],
        '_1400': ['SplineDesignTypes'],
        '_1401': ['FinishingMethods'],
        '_1402': ['SplineFitClassType'],
        '_1403': ['SplineFixtureTypes'],
        '_1404': ['SplineHalfDesign'],
        '_1405': ['SplineJointDesign'],
        '_1406': ['SplineMaterial'],
        '_1407': ['SplineRatingTypes'],
        '_1408': ['SplineToleranceClassTypes'],
        '_1409': ['StandardSplineHalfDesign'],
        '_1410': ['StandardSplineJointDesign'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
