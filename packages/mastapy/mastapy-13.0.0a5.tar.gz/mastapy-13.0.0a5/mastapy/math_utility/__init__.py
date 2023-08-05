"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1479 import Range
    from ._1480 import AcousticWeighting
    from ._1481 import AlignmentAxis
    from ._1482 import Axis
    from ._1483 import CirclesOnAxis
    from ._1484 import ComplexMatrix
    from ._1485 import ComplexPartDisplayOption
    from ._1486 import ComplexVector
    from ._1487 import ComplexVector3D
    from ._1488 import ComplexVector6D
    from ._1489 import CoordinateSystem3D
    from ._1490 import CoordinateSystemEditor
    from ._1491 import CoordinateSystemForRotation
    from ._1492 import CoordinateSystemForRotationOrigin
    from ._1493 import DataPrecision
    from ._1494 import DegreeOfFreedom
    from ._1495 import DynamicsResponseScalarResult
    from ._1496 import DynamicsResponseScaling
    from ._1497 import Eigenmode
    from ._1498 import Eigenmodes
    from ._1499 import EulerParameters
    from ._1500 import ExtrapolationOptions
    from ._1501 import FacetedBody
    from ._1502 import FacetedSurface
    from ._1503 import FourierSeries
    from ._1504 import GenericMatrix
    from ._1505 import GriddedSurface
    from ._1506 import HarmonicValue
    from ._1507 import InertiaTensor
    from ._1508 import MassProperties
    from ._1509 import MaxMinMean
    from ._1510 import ComplexMagnitudeMethod
    from ._1511 import MultipleFourierSeriesInterpolator
    from ._1512 import Named2DLocation
    from ._1513 import PIDControlUpdateMethod
    from ._1514 import Quaternion
    from ._1515 import RealMatrix
    from ._1516 import RealVector
    from ._1517 import ResultOptionsFor3DVector
    from ._1518 import RotationAxis
    from ._1519 import RoundedOrder
    from ._1520 import SinCurve
    from ._1521 import SquareMatrix
    from ._1522 import StressPoint
    from ._1523 import TransformMatrix3D
    from ._1524 import TranslationRotation
    from ._1525 import Vector2DListAccessor
    from ._1526 import Vector6D
else:
    import_structure = {
        '_1479': ['Range'],
        '_1480': ['AcousticWeighting'],
        '_1481': ['AlignmentAxis'],
        '_1482': ['Axis'],
        '_1483': ['CirclesOnAxis'],
        '_1484': ['ComplexMatrix'],
        '_1485': ['ComplexPartDisplayOption'],
        '_1486': ['ComplexVector'],
        '_1487': ['ComplexVector3D'],
        '_1488': ['ComplexVector6D'],
        '_1489': ['CoordinateSystem3D'],
        '_1490': ['CoordinateSystemEditor'],
        '_1491': ['CoordinateSystemForRotation'],
        '_1492': ['CoordinateSystemForRotationOrigin'],
        '_1493': ['DataPrecision'],
        '_1494': ['DegreeOfFreedom'],
        '_1495': ['DynamicsResponseScalarResult'],
        '_1496': ['DynamicsResponseScaling'],
        '_1497': ['Eigenmode'],
        '_1498': ['Eigenmodes'],
        '_1499': ['EulerParameters'],
        '_1500': ['ExtrapolationOptions'],
        '_1501': ['FacetedBody'],
        '_1502': ['FacetedSurface'],
        '_1503': ['FourierSeries'],
        '_1504': ['GenericMatrix'],
        '_1505': ['GriddedSurface'],
        '_1506': ['HarmonicValue'],
        '_1507': ['InertiaTensor'],
        '_1508': ['MassProperties'],
        '_1509': ['MaxMinMean'],
        '_1510': ['ComplexMagnitudeMethod'],
        '_1511': ['MultipleFourierSeriesInterpolator'],
        '_1512': ['Named2DLocation'],
        '_1513': ['PIDControlUpdateMethod'],
        '_1514': ['Quaternion'],
        '_1515': ['RealMatrix'],
        '_1516': ['RealVector'],
        '_1517': ['ResultOptionsFor3DVector'],
        '_1518': ['RotationAxis'],
        '_1519': ['RoundedOrder'],
        '_1520': ['SinCurve'],
        '_1521': ['SquareMatrix'],
        '_1522': ['StressPoint'],
        '_1523': ['TransformMatrix3D'],
        '_1524': ['TranslationRotation'],
        '_1525': ['Vector2DListAccessor'],
        '_1526': ['Vector6D'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
