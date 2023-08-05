"""_1526.py

Vector6D
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.math_utility import _1516
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VECTOR_6D = python_net_import('SMT.MastaAPI.MathUtility', 'Vector6D')


__docformat__ = 'restructuredtext en'
__all__ = ('Vector6D',)


class Vector6D(_1516.RealVector):
    """Vector6D

    This is a mastapy class.
    """

    TYPE = _VECTOR_6D

    class _Cast_Vector6D:
        """Special nested class for casting Vector6D to subclasses."""

        def __init__(self, parent: 'Vector6D'):
            self._parent = parent

        @property
        def real_vector(self):
            return self._parent._cast(_1516.RealVector)

        @property
        def real_matrix(self):
            from mastapy.math_utility import _1515
            
            return self._parent._cast(_1515.RealMatrix)

        @property
        def generic_matrix(self):
            from mastapy.math_utility import _1504, _1515
            
            return self._parent._cast(_1504.GenericMatrix)

        @property
        def vector_6d(self) -> 'Vector6D':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Vector6D.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Vector6D._Cast_Vector6D':
        return self._Cast_Vector6D(self)
