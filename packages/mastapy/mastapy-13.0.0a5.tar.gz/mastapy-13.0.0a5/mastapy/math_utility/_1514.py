﻿"""_1514.py

Quaternion
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.math_utility import _1516
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_QUATERNION = python_net_import('SMT.MastaAPI.MathUtility', 'Quaternion')


__docformat__ = 'restructuredtext en'
__all__ = ('Quaternion',)


class Quaternion(_1516.RealVector):
    """Quaternion

    This is a mastapy class.
    """

    TYPE = _QUATERNION

    class _Cast_Quaternion:
        """Special nested class for casting Quaternion to subclasses."""

        def __init__(self, parent: 'Quaternion'):
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
        def quaternion(self) -> 'Quaternion':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Quaternion.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Quaternion._Cast_Quaternion':
        return self._Cast_Quaternion(self)
