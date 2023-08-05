﻿"""_902.py

CylindricalGearSetParetoOptimiser
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal.python_net import python_net_import
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_set_pareto_optimiser import _909
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_CYLINDRICAL_GEAR_SET_PARETO_OPTIMISER = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'CylindricalGearSetParetoOptimiser')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1025


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetParetoOptimiser',)


class CylindricalGearSetParetoOptimiser(_909.GearSetParetoOptimiser):
    """CylindricalGearSetParetoOptimiser

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_PARETO_OPTIMISER

    class _Cast_CylindricalGearSetParetoOptimiser:
        """Special nested class for casting CylindricalGearSetParetoOptimiser to subclasses."""

        def __init__(self, parent: 'CylindricalGearSetParetoOptimiser'):
            self._parent = parent

        @property
        def gear_set_pareto_optimiser(self):
            return self._parent._cast(_909.GearSetParetoOptimiser)

        @property
        def design_space_search_base(self):
            from mastapy.gears.gear_set_pareto_optimiser import _903, _908
            from mastapy.gears.rating import _353
            
            return self._parent._cast(_903.DesignSpaceSearchBase)

        @property
        def cylindrical_gear_set_pareto_optimiser(self) -> 'CylindricalGearSetParetoOptimiser':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetParetoOptimiser.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_space_search_strategy(self) -> 'str':
        """str: 'DesignSpaceSearchStrategy' is the original name of this property."""

        temp = self.wrapped.DesignSpaceSearchStrategy.SelectedItemName

        if temp is None:
            return ''

        return temp

    @design_space_search_strategy.setter
    def design_space_search_strategy(self, value: 'str'):
        self.wrapped.DesignSpaceSearchStrategy.SetSelectedItem(str(value) if value is not None else '')

    @property
    def design_space_search_strategy_duty_cycle(self) -> 'str':
        """str: 'DesignSpaceSearchStrategyDutyCycle' is the original name of this property."""

        temp = self.wrapped.DesignSpaceSearchStrategyDutyCycle.SelectedItemName

        if temp is None:
            return ''

        return temp

    @design_space_search_strategy_duty_cycle.setter
    def design_space_search_strategy_duty_cycle(self, value: 'str'):
        self.wrapped.DesignSpaceSearchStrategyDutyCycle.SetSelectedItem(str(value) if value is not None else '')

    @property
    def selected_candidate_geometry(self) -> '_1025.CylindricalGearSetDesign':
        """CylindricalGearSetDesign: 'SelectedCandidateGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SelectedCandidateGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def all_candidate_gear_sets(self) -> 'List[_1025.CylindricalGearSetDesign]':
        """List[CylindricalGearSetDesign]: 'AllCandidateGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllCandidateGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def candidate_gear_sets(self) -> 'List[_1025.CylindricalGearSetDesign]':
        """List[CylindricalGearSetDesign]: 'CandidateGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CandidateGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalGearSetParetoOptimiser._Cast_CylindricalGearSetParetoOptimiser':
        return self._Cast_CylindricalGearSetParetoOptimiser(self)
