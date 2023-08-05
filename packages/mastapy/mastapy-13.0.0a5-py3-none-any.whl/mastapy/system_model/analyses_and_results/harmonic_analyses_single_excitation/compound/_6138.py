﻿"""_6138.py

ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6167
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2288
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6008


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation',)


class ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation(_6167.GearMeshCompoundHarmonicAnalysisOfSingleExcitation):
    """ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6167.GearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6173
            
            return self._parent._cast(_6173.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6143
            
            return self._parent._cast(_6143.ConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def concept_gear_mesh_compound_harmonic_analysis_of_single_excitation(self) -> 'ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2288.ConceptGearMesh':
        """ConceptGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2288.ConceptGearMesh':
        """ConceptGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6008.ConceptGearMeshHarmonicAnalysisOfSingleExcitation]':
        """List[ConceptGearMeshHarmonicAnalysisOfSingleExcitation]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_6008.ConceptGearMeshHarmonicAnalysisOfSingleExcitation]':
        """List[ConceptGearMeshHarmonicAnalysisOfSingleExcitation]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation':
        return self._Cast_ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation(self)
