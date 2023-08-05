"""_1515.py

RealMatrix
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.math_utility import _1504
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_REAL_MATRIX = python_net_import('SMT.MastaAPI.MathUtility', 'RealMatrix')


__docformat__ = 'restructuredtext en'
__all__ = ('RealMatrix',)


class RealMatrix(_1504.GenericMatrix[float, 'RealMatrix']):
    """RealMatrix

    This is a mastapy class.
    """

    TYPE = _REAL_MATRIX

    class _Cast_RealMatrix:
        """Special nested class for casting RealMatrix to subclasses."""

        def __init__(self, parent: 'RealMatrix'):
            self._parent = parent

        @property
        def generic_matrix(self):
            from mastapy.math_utility import _1515
            
            return self._parent._cast(_1504.GenericMatrix)

        @property
        def euler_parameters(self):
            from mastapy.math_utility import _1499
            
            return self._parent._cast(_1499.EulerParameters)

        @property
        def quaternion(self):
            from mastapy.math_utility import _1514
            
            return self._parent._cast(_1514.Quaternion)

        @property
        def real_vector(self):
            from mastapy.math_utility import _1516
            
            return self._parent._cast(_1516.RealVector)

        @property
        def square_matrix(self):
            from mastapy.math_utility import _1521
            
            return self._parent._cast(_1521.SquareMatrix)

        @property
        def vector_6d(self):
            from mastapy.math_utility import _1526
            
            return self._parent._cast(_1526.Vector6D)

        @property
        def real_matrix(self) -> 'RealMatrix':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RealMatrix.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def get_column_at(self, index: 'int') -> 'List[float]':
        """ 'GetColumnAt' is the original name of this method.

        Args:
            index (int)

        Returns:
            List[float]
        """

        index = int(index)
        return conversion.pn_to_mp_objects_in_list(self.wrapped.GetColumnAt(index if index else 0), float)

    def get_row_at(self, index: 'int') -> 'List[float]':
        """ 'GetRowAt' is the original name of this method.

        Args:
            index (int)

        Returns:
            List[float]
        """

        index = int(index)
        return conversion.pn_to_mp_objects_in_list(self.wrapped.GetRowAt(index if index else 0), float)

    @property
    def cast_to(self) -> 'RealMatrix._Cast_RealMatrix':
        return self._Cast_RealMatrix(self)
