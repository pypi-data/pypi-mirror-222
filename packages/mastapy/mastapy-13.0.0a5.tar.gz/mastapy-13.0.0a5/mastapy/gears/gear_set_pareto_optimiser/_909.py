"""_909.py

GearSetParetoOptimiser
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_set_pareto_optimiser import _903, _908
from mastapy.gears.rating import _353
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_PARETO_OPTIMISER = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'GearSetParetoOptimiser')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs import _947


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetParetoOptimiser',)


class GearSetParetoOptimiser(_903.DesignSpaceSearchBase['_353.AbstractGearSetRating', '_908.GearSetOptimiserCandidate']):
    """GearSetParetoOptimiser

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_PARETO_OPTIMISER

    class _Cast_GearSetParetoOptimiser:
        """Special nested class for casting GearSetParetoOptimiser to subclasses."""

        def __init__(self, parent: 'GearSetParetoOptimiser'):
            self._parent = parent

        @property
        def design_space_search_base(self):
            return self._parent._cast(_903.DesignSpaceSearchBase)

        @property
        def cylindrical_gear_set_pareto_optimiser(self):
            from mastapy.gears.gear_set_pareto_optimiser import _902
            
            return self._parent._cast(_902.CylindricalGearSetParetoOptimiser)

        @property
        def face_gear_set_pareto_optimiser(self):
            from mastapy.gears.gear_set_pareto_optimiser import _905
            
            return self._parent._cast(_905.FaceGearSetParetoOptimiser)

        @property
        def hypoid_gear_set_pareto_optimiser(self):
            from mastapy.gears.gear_set_pareto_optimiser import _910
            
            return self._parent._cast(_910.HypoidGearSetParetoOptimiser)

        @property
        def spiral_bevel_gear_set_pareto_optimiser(self):
            from mastapy.gears.gear_set_pareto_optimiser import _935
            
            return self._parent._cast(_935.SpiralBevelGearSetParetoOptimiser)

        @property
        def straight_bevel_gear_set_pareto_optimiser(self):
            from mastapy.gears.gear_set_pareto_optimiser import _936
            
            return self._parent._cast(_936.StraightBevelGearSetParetoOptimiser)

        @property
        def gear_set_pareto_optimiser(self) -> 'GearSetParetoOptimiser':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetParetoOptimiser.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_designs_with_gears_which_cannot_be_manufactured_from_cutters(self) -> 'int':
        """int: 'NumberOfDesignsWithGearsWhichCannotBeManufacturedFromCutters' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfDesignsWithGearsWhichCannotBeManufacturedFromCutters

        if temp is None:
            return 0

        return temp

    @property
    def remove_candidates_which_cannot_be_manufactured_with_cutters_from_database(self) -> 'bool':
        """bool: 'RemoveCandidatesWhichCannotBeManufacturedWithCuttersFromDatabase' is the original name of this property."""

        temp = self.wrapped.RemoveCandidatesWhichCannotBeManufacturedWithCuttersFromDatabase

        if temp is None:
            return False

        return temp

    @remove_candidates_which_cannot_be_manufactured_with_cutters_from_database.setter
    def remove_candidates_which_cannot_be_manufactured_with_cutters_from_database(self, value: 'bool'):
        self.wrapped.RemoveCandidatesWhichCannotBeManufacturedWithCuttersFromDatabase = bool(value) if value is not None else False

    @property
    def remove_candidates_with_warnings(self) -> 'bool':
        """bool: 'RemoveCandidatesWithWarnings' is the original name of this property."""

        temp = self.wrapped.RemoveCandidatesWithWarnings

        if temp is None:
            return False

        return temp

    @remove_candidates_with_warnings.setter
    def remove_candidates_with_warnings(self, value: 'bool'):
        self.wrapped.RemoveCandidatesWithWarnings = bool(value) if value is not None else False

    @property
    def selected_candidate_geometry(self) -> '_947.GearSetDesign':
        """GearSetDesign: 'SelectedCandidateGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SelectedCandidateGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def all_candidate_gear_sets(self) -> 'List[_947.GearSetDesign]':
        """List[GearSetDesign]: 'AllCandidateGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllCandidateGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def candidate_gear_sets(self) -> 'List[_947.GearSetDesign]':
        """List[GearSetDesign]: 'CandidateGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CandidateGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def add_chart(self):
        """ 'AddChart' is the original name of this method."""

        self.wrapped.AddChart()

    def reset_charts(self):
        """ 'ResetCharts' is the original name of this method."""

        self.wrapped.ResetCharts()

    @property
    def cast_to(self) -> 'GearSetParetoOptimiser._Cast_GearSetParetoOptimiser':
        return self._Cast_GearSetParetoOptimiser(self)
