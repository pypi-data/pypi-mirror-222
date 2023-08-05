"""_1484.py

ComplexMatrix
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.math_utility import _1504
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPLEX_MATRIX = python_net_import('SMT.MastaAPI.MathUtility', 'ComplexMatrix')


__docformat__ = 'restructuredtext en'
__all__ = ('ComplexMatrix',)


class ComplexMatrix(_1504.GenericMatrix[complex, 'ComplexMatrix']):
    """ComplexMatrix

    This is a mastapy class.
    """

    TYPE = _COMPLEX_MATRIX

    class _Cast_ComplexMatrix:
        """Special nested class for casting ComplexMatrix to subclasses."""

        def __init__(self, parent: 'ComplexMatrix'):
            self._parent = parent

        @property
        def generic_matrix(self):
            from mastapy.math_utility import _1484
            
            return self._parent._cast(_1504.GenericMatrix)

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
        def complex_matrix(self) -> 'ComplexMatrix':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ComplexMatrix.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ComplexMatrix._Cast_ComplexMatrix':
        return self._Cast_ComplexMatrix(self)
