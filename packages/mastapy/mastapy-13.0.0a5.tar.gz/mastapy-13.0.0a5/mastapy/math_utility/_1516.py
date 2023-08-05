"""_1516.py

RealVector
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.math_utility import _1515
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_REAL_VECTOR = python_net_import('SMT.MastaAPI.MathUtility', 'RealVector')


__docformat__ = 'restructuredtext en'
__all__ = ('RealVector',)


class RealVector(_1515.RealMatrix):
    """RealVector

    This is a mastapy class.
    """

    TYPE = _REAL_VECTOR

    class _Cast_RealVector:
        """Special nested class for casting RealVector to subclasses."""

        def __init__(self, parent: 'RealVector'):
            self._parent = parent

        @property
        def real_matrix(self):
            return self._parent._cast(_1515.RealMatrix)

        @property
        def generic_matrix(self):
            from mastapy.math_utility import _1504
            
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
        def vector_6d(self):
            from mastapy.math_utility import _1526
            
            return self._parent._cast(_1526.Vector6D)

        @property
        def real_vector(self) -> 'RealVector':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RealVector.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'RealVector._Cast_RealVector':
        return self._Cast_RealVector(self)
