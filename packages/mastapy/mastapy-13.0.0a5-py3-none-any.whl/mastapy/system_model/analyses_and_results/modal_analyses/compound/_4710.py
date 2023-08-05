"""_4710.py

AGMAGleasonConicalGearSetCompoundModalAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4738
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'AGMAGleasonConicalGearSetCompoundModalAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4556


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearSetCompoundModalAnalysis',)


class AGMAGleasonConicalGearSetCompoundModalAnalysis(_4738.ConicalGearSetCompoundModalAnalysis):
    """AGMAGleasonConicalGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS

    class _Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearSetCompoundModalAnalysis'):
            self._parent = parent

        @property
        def conical_gear_set_compound_modal_analysis(self):
            return self._parent._cast(_4738.ConicalGearSetCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4764
            
            return self._parent._cast(_4764.GearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4802
            
            return self._parent._cast(_4802.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4704
            
            return self._parent._cast(_4704.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4783
            
            return self._parent._cast(_4783.PartCompoundModalAnalysis)

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
        def bevel_differential_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4717
            
            return self._parent._cast(_4717.BevelDifferentialGearSetCompoundModalAnalysis)

        @property
        def bevel_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4722
            
            return self._parent._cast(_4722.BevelGearSetCompoundModalAnalysis)

        @property
        def hypoid_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4768
            
            return self._parent._cast(_4768.HypoidGearSetCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4805
            
            return self._parent._cast(_4805.SpiralBevelGearSetCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4811
            
            return self._parent._cast(_4811.StraightBevelDiffGearSetCompoundModalAnalysis)

        @property
        def straight_bevel_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4814
            
            return self._parent._cast(_4814.StraightBevelGearSetCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4832
            
            return self._parent._cast(_4832.ZerolBevelGearSetCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(self) -> 'AGMAGleasonConicalGearSetCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearSetCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_4556.AGMAGleasonConicalGearSetModalAnalysis]':
        """List[AGMAGleasonConicalGearSetModalAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4556.AGMAGleasonConicalGearSetModalAnalysis]':
        """List[AGMAGleasonConicalGearSetModalAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis':
        return self._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis(self)
