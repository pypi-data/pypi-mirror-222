﻿"""_2375.py

FESubstructureWithSelectionForHarmonicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.fe import _2373
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_SUBSTRUCTURE_WITH_SELECTION_FOR_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.FE', 'FESubstructureWithSelectionForHarmonicAnalysis')

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses import _185
    from mastapy.system_model.fe import _2383


__docformat__ = 'restructuredtext en'
__all__ = ('FESubstructureWithSelectionForHarmonicAnalysis',)


class FESubstructureWithSelectionForHarmonicAnalysis(_2373.FESubstructureWithSelection):
    """FESubstructureWithSelectionForHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _FE_SUBSTRUCTURE_WITH_SELECTION_FOR_HARMONIC_ANALYSIS

    class _Cast_FESubstructureWithSelectionForHarmonicAnalysis:
        """Special nested class for casting FESubstructureWithSelectionForHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'FESubstructureWithSelectionForHarmonicAnalysis'):
            self._parent = parent

        @property
        def fe_substructure_with_selection(self):
            return self._parent._cast(_2373.FESubstructureWithSelection)

        @property
        def base_fe_with_selection(self):
            from mastapy.system_model.fe import _2343
            
            return self._parent._cast(_2343.BaseFEWithSelection)

        @property
        def fe_substructure_with_selection_for_harmonic_analysis(self) -> 'FESubstructureWithSelectionForHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FESubstructureWithSelectionForHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def alpha_damping_value(self) -> 'float':
        """float: 'AlphaDampingValue' is the original name of this property."""

        temp = self.wrapped.AlphaDampingValue

        if temp is None:
            return 0.0

        return temp

    @alpha_damping_value.setter
    def alpha_damping_value(self, value: 'float'):
        self.wrapped.AlphaDampingValue = float(value) if value is not None else 0.0

    @property
    def beta_damping_value(self) -> 'float':
        """float: 'BetaDampingValue' is the original name of this property."""

        temp = self.wrapped.BetaDampingValue

        if temp is None:
            return 0.0

        return temp

    @beta_damping_value.setter
    def beta_damping_value(self, value: 'float'):
        self.wrapped.BetaDampingValue = float(value) if value is not None else 0.0

    @property
    def frequency(self) -> 'float':
        """float: 'Frequency' is the original name of this property."""

        temp = self.wrapped.Frequency

        if temp is None:
            return 0.0

        return temp

    @frequency.setter
    def frequency(self, value: 'float'):
        self.wrapped.Frequency = float(value) if value is not None else 0.0

    @property
    def harmonic_draw_style(self) -> '_185.FEModelHarmonicAnalysisDrawStyle':
        """FEModelHarmonicAnalysisDrawStyle: 'HarmonicDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def boundary_conditions_all_nodes(self) -> 'List[_2383.NodeBoundaryConditionStaticAnalysis]':
        """List[NodeBoundaryConditionStaticAnalysis]: 'BoundaryConditionsAllNodes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoundaryConditionsAllNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def export_velocity_to_file(self):
        """ 'ExportVelocityToFile' is the original name of this method."""

        self.wrapped.ExportVelocityToFile()

    def solve_for_current_inputs(self):
        """ 'SolveForCurrentInputs' is the original name of this method."""

        self.wrapped.SolveForCurrentInputs()

    @property
    def cast_to(self) -> 'FESubstructureWithSelectionForHarmonicAnalysis._Cast_FESubstructureWithSelectionForHarmonicAnalysis':
        return self._Cast_FESubstructureWithSelectionForHarmonicAnalysis(self)
