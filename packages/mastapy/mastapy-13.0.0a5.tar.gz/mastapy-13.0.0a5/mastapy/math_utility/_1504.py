"""_1504.py

GenericMatrix
"""
from __future__ import annotations

from typing import (
    TYPE_CHECKING, List, TypeVar, Generic
)

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GENERIC_MATRIX = python_net_import('SMT.MastaAPI.MathUtility', 'GenericMatrix')


__docformat__ = 'restructuredtext en'
__all__ = ('GenericMatrix',)


TElement = TypeVar('TElement', bound='object')
TMatrix = TypeVar('TMatrix', bound='GenericMatrix')


class GenericMatrix(_0.APIBase, Generic[TElement, TMatrix]):
    """GenericMatrix

    This is a mastapy class.

    Generic Types:
        TElement
        TMatrix
    """

    TYPE = _GENERIC_MATRIX

    class _Cast_GenericMatrix:
        """Special nested class for casting GenericMatrix to subclasses."""

        def __init__(self, parent: 'GenericMatrix'):
            self._parent = parent

        @property
        def complex_matrix(self):
            from mastapy.math_utility import _1484
            
            return self._parent._cast(_1484.ComplexMatrix)

        @property
        def complex_vector(self):
            from mastapy.math_utility import _1486
            
            return self._parent._cast(_1486.ComplexVector)

        @property
        def complex_vector_3d(self):
            from mastapy.math_utility import _1487
            
            return self._parent._cast(_1487.ComplexVector3D)

        @property
        def complex_vector_6d(self):
            from mastapy.math_utility import _1488
            
            return self._parent._cast(_1488.ComplexVector6D)

        @property
        def euler_parameters(self):
            from mastapy.math_utility import _1499
            
            return self._parent._cast(_1499.EulerParameters)

        @property
        def quaternion(self):
            from mastapy.math_utility import _1514
            
            return self._parent._cast(_1514.Quaternion)

        @property
        def real_matrix(self):
            from mastapy.math_utility import _1515
            
            return self._parent._cast(_1515.RealMatrix)

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
        def generic_matrix(self) -> 'GenericMatrix':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GenericMatrix.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_columns(self) -> 'int':
        """int: 'NumberOfColumns' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfColumns

        if temp is None:
            return 0

        return temp

    @property
    def number_of_entries(self) -> 'int':
        """int: 'NumberOfEntries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfEntries

        if temp is None:
            return 0

        return temp

    @property
    def number_of_rows(self) -> 'int':
        """int: 'NumberOfRows' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfRows

        if temp is None:
            return 0

        return temp

    @property
    def data(self) -> 'List[TElement]':
        """List[TElement]: 'Data' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Data

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def get_column_at(self, index: 'int') -> 'List[TElement]':
        """ 'GetColumnAt' is the original name of this method.

        Args:
            index (int)

        Returns:
            List[TElement]
        """

        index = int(index)
        return conversion.pn_to_mp_objects_in_list(self.wrapped.GetColumnAt(index if index else 0))

    def get_row_at(self, row_index: 'int') -> 'List[TElement]':
        """ 'GetRowAt' is the original name of this method.

        Args:
            row_index (int)

        Returns:
            List[TElement]
        """

        row_index = int(row_index)
        return conversion.pn_to_mp_objects_in_list(self.wrapped.GetRowAt(row_index if row_index else 0))

    @property
    def cast_to(self) -> 'GenericMatrix._Cast_GenericMatrix':
        return self._Cast_GenericMatrix(self)
