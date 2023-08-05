"""_4973.py

BeltDriveCompoundModalAnalysisAtAStiffness
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5061
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'BeltDriveCompoundModalAnalysisAtAStiffness')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2558
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4843


__docformat__ = 'restructuredtext en'
__all__ = ('BeltDriveCompoundModalAnalysisAtAStiffness',)


class BeltDriveCompoundModalAnalysisAtAStiffness(_5061.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness):
    """BeltDriveCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_BeltDriveCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting BeltDriveCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'BeltDriveCompoundModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(self):
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
        def cvt_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5004
            
            return self._parent._cast(_5004.CVTCompoundModalAnalysisAtAStiffness)

        @property
        def belt_drive_compound_modal_analysis_at_a_stiffness(self) -> 'BeltDriveCompoundModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BeltDriveCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2558.BeltDrive':
        """BeltDrive: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2558.BeltDrive':
        """BeltDrive: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4843.BeltDriveModalAnalysisAtAStiffness]':
        """List[BeltDriveModalAnalysisAtAStiffness]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4843.BeltDriveModalAnalysisAtAStiffness]':
        """List[BeltDriveModalAnalysisAtAStiffness]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BeltDriveCompoundModalAnalysisAtAStiffness._Cast_BeltDriveCompoundModalAnalysisAtAStiffness':
        return self._Cast_BeltDriveCompoundModalAnalysisAtAStiffness(self)
