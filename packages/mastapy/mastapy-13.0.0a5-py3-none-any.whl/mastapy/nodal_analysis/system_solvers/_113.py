﻿"""_113.py

SingularValuesAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SINGULAR_VALUES_ANALYSIS = python_net_import('SMT.MastaAPI.NodalAnalysis.SystemSolvers', 'SingularValuesAnalysis')

if TYPE_CHECKING:
    from mastapy.nodal_analysis.system_solvers import _114


__docformat__ = 'restructuredtext en'
__all__ = ('SingularValuesAnalysis',)


class SingularValuesAnalysis(_0.APIBase):
    """SingularValuesAnalysis

    This is a mastapy class.
    """

    TYPE = _SINGULAR_VALUES_ANALYSIS

    class _Cast_SingularValuesAnalysis:
        """Special nested class for casting SingularValuesAnalysis to subclasses."""

        def __init__(self, parent: 'SingularValuesAnalysis'):
            self._parent = parent

        @property
        def singular_values_analysis(self) -> 'SingularValuesAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SingularValuesAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def condition_number(self) -> 'float':
        """float: 'ConditionNumber' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConditionNumber

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_matrix_degrees_of_freedom(self) -> 'int':
        """int: 'StiffnessMatrixDegreesOfFreedom' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessMatrixDegreesOfFreedom

        if temp is None:
            return 0

        return temp

    @property
    def stiffness_matrix_rank(self) -> 'int':
        """int: 'StiffnessMatrixRank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessMatrixRank

        if temp is None:
            return 0

        return temp

    @property
    def largest_singular_vectors(self) -> 'List[_114.SingularVectorAnalysis]':
        """List[SingularVectorAnalysis]: 'LargestSingularVectors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LargestSingularVectors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def smallest_singular_vectors(self) -> 'List[_114.SingularVectorAnalysis]':
        """List[SingularVectorAnalysis]: 'SmallestSingularVectors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallestSingularVectors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SingularValuesAnalysis._Cast_SingularValuesAnalysis':
        return self._Cast_SingularValuesAnalysis(self)
