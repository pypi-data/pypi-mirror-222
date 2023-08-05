"""_1544.py

ParetoOptimisationVariable
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.math_utility.optimisation import _1545
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_OPTIMISATION_VARIABLE = python_net_import('SMT.MastaAPI.MathUtility.Optimisation', 'ParetoOptimisationVariable')

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1546


__docformat__ = 'restructuredtext en'
__all__ = ('ParetoOptimisationVariable',)


class ParetoOptimisationVariable(_1545.ParetoOptimisationVariableBase):
    """ParetoOptimisationVariable

    This is a mastapy class.
    """

    TYPE = _PARETO_OPTIMISATION_VARIABLE

    class _Cast_ParetoOptimisationVariable:
        """Special nested class for casting ParetoOptimisationVariable to subclasses."""

        def __init__(self, parent: 'ParetoOptimisationVariable'):
            self._parent = parent

        @property
        def pareto_optimisation_variable_base(self):
            return self._parent._cast(_1545.ParetoOptimisationVariableBase)

        @property
        def pareto_optimisation_input(self):
            from mastapy.math_utility.optimisation import _1538
            
            return self._parent._cast(_1538.ParetoOptimisationInput)

        @property
        def pareto_optimisation_output(self):
            from mastapy.math_utility.optimisation import _1539
            
            return self._parent._cast(_1539.ParetoOptimisationOutput)

        @property
        def pareto_optimisation_variable(self) -> 'ParetoOptimisationVariable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ParetoOptimisationVariable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def property_target_for_dominant_candidate_search(self) -> '_1546.PropertyTargetForDominantCandidateSearch':
        """PropertyTargetForDominantCandidateSearch: 'PropertyTargetForDominantCandidateSearch' is the original name of this property."""

        temp = self.wrapped.PropertyTargetForDominantCandidateSearch

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.MathUtility.Optimisation.PropertyTargetForDominantCandidateSearch')
        return constructor.new_from_mastapy('mastapy.math_utility.optimisation._1546', 'PropertyTargetForDominantCandidateSearch')(value) if value is not None else None

    @property_target_for_dominant_candidate_search.setter
    def property_target_for_dominant_candidate_search(self, value: '_1546.PropertyTargetForDominantCandidateSearch'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.MathUtility.Optimisation.PropertyTargetForDominantCandidateSearch')
        self.wrapped.PropertyTargetForDominantCandidateSearch = value

    @property
    def cast_to(self) -> 'ParetoOptimisationVariable._Cast_ParetoOptimisationVariable':
        return self._Cast_ParetoOptimisationVariable(self)
