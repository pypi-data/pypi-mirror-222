﻿"""_4609.py

FEPartModalAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4552
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'FEPartModalAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2436
    from mastapy.system_model.analyses_and_results.static_loads import _6855
    from mastapy.system_model.analyses_and_results.system_deflections import _2739
    from mastapy.nodal_analysis.component_mode_synthesis import _230


__docformat__ = 'restructuredtext en'
__all__ = ('FEPartModalAnalysis',)


class FEPartModalAnalysis(_4552.AbstractShaftOrHousingModalAnalysis):
    """FEPartModalAnalysis

    This is a mastapy class.
    """

    TYPE = _FE_PART_MODAL_ANALYSIS

    class _Cast_FEPartModalAnalysis:
        """Special nested class for casting FEPartModalAnalysis to subclasses."""

        def __init__(self, parent: 'FEPartModalAnalysis'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_modal_analysis(self):
            return self._parent._cast(_4552.AbstractShaftOrHousingModalAnalysis)

        @property
        def component_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4575
            
            return self._parent._cast(_4575.ComponentModalAnalysis)

        @property
        def part_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4638
            
            return self._parent._cast(_4638.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7514
            
            return self._parent._cast(_7514.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7511
            
            return self._parent._cast(_7511.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2639
            
            return self._parent._cast(_2639.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2635
            
            return self._parent._cast(_2635.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def fe_part_modal_analysis(self) -> 'FEPartModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEPartModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2436.FEPart':
        """FEPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6855.FEPartLoadCase':
        """FEPartLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2739.FEPartSystemDeflection':
        """FEPartSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def modal_full_fe_results(self) -> 'List[_230.ModalCMSResults]':
        """List[ModalCMSResults]: 'ModalFullFEResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModalFullFEResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[FEPartModalAnalysis]':
        """List[FEPartModalAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def calculate_all_strain_and_kinetic_energies(self):
        """ 'CalculateAllStrainAndKineticEnergies' is the original name of this method."""

        self.wrapped.CalculateAllStrainAndKineticEnergies()

    def calculate_mode_shapes(self):
        """ 'CalculateModeShapes' is the original name of this method."""

        self.wrapped.CalculateModeShapes()

    def calculate_selected_strain_and_kinetic_energy(self):
        """ 'CalculateSelectedStrainAndKineticEnergy' is the original name of this method."""

        self.wrapped.CalculateSelectedStrainAndKineticEnergy()

    @property
    def cast_to(self) -> 'FEPartModalAnalysis._Cast_FEPartModalAnalysis':
        return self._Cast_FEPartModalAnalysis(self)
