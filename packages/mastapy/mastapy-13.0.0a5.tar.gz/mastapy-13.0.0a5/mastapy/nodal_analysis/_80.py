﻿"""_80.py

NodalMatrixRow
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODAL_MATRIX_ROW = python_net_import('SMT.MastaAPI.NodalAnalysis', 'NodalMatrixRow')


__docformat__ = 'restructuredtext en'
__all__ = ('NodalMatrixRow',)


class NodalMatrixRow(_0.APIBase):
    """NodalMatrixRow

    This is a mastapy class.
    """

    TYPE = _NODAL_MATRIX_ROW

    class _Cast_NodalMatrixRow:
        """Special nested class for casting NodalMatrixRow to subclasses."""

        def __init__(self, parent: 'NodalMatrixRow'):
            self._parent = parent

        @property
        def nodal_matrix_row(self) -> 'NodalMatrixRow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NodalMatrixRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comma_separated_values(self) -> 'str':
        """str: 'CommaSeparatedValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CommaSeparatedValues

        if temp is None:
            return ''

        return temp

    @property
    def degree_of_freedom(self) -> 'int':
        """int: 'DegreeOfFreedom' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DegreeOfFreedom

        if temp is None:
            return 0

        return temp

    @property
    def node_index(self) -> 'int':
        """int: 'NodeIndex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodeIndex

        if temp is None:
            return 0

        return temp

    @property
    def values(self) -> 'List[float]':
        """List[float]: 'Values' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Values

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    @property
    def cast_to(self) -> 'NodalMatrixRow._Cast_NodalMatrixRow':
        return self._Cast_NodalMatrixRow(self)
