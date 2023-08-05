﻿"""_5012.py

CylindricalGearSetCompoundModalAnalysisAtAStiffness
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5023
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'CylindricalGearSetCompoundModalAnalysisAtAStiffness')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2508
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4882
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5010, _5011


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetCompoundModalAnalysisAtAStiffness',)


class CylindricalGearSetCompoundModalAnalysisAtAStiffness(_5023.GearSetCompoundModalAnalysisAtAStiffness):
    """CylindricalGearSetCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_CylindricalGearSetCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting CylindricalGearSetCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'CylindricalGearSetCompoundModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def gear_set_compound_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_5023.GearSetCompoundModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5061
            
            return self._parent._cast(_5061.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4963
            
            return self._parent._cast(_4963.AbstractAssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5042
            
            return self._parent._cast(_5042.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7512
            
            return self._parent._cast(_7512.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5047
            
            return self._parent._cast(_5047.PlanetaryGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_stiffness(self) -> 'CylindricalGearSetCompoundModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2508.CylindricalGearSet':
        """CylindricalGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2508.CylindricalGearSet':
        """CylindricalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4882.CylindricalGearSetModalAnalysisAtAStiffness]':
        """List[CylindricalGearSetModalAnalysisAtAStiffness]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gears_compound_modal_analysis_at_a_stiffness(self) -> 'List[_5010.CylindricalGearCompoundModalAnalysisAtAStiffness]':
        """List[CylindricalGearCompoundModalAnalysisAtAStiffness]: 'CylindricalGearsCompoundModalAnalysisAtAStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearsCompoundModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_meshes_compound_modal_analysis_at_a_stiffness(self) -> 'List[_5011.CylindricalGearMeshCompoundModalAnalysisAtAStiffness]':
        """List[CylindricalGearMeshCompoundModalAnalysisAtAStiffness]: 'CylindricalMeshesCompoundModalAnalysisAtAStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshesCompoundModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4882.CylindricalGearSetModalAnalysisAtAStiffness]':
        """List[CylindricalGearSetModalAnalysisAtAStiffness]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalGearSetCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearSetCompoundModalAnalysisAtAStiffness':
        return self._Cast_CylindricalGearSetCompoundModalAnalysisAtAStiffness(self)
