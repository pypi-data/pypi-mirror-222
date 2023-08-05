"""_4462.py

CVTCompoundParametricStudyTool
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4431
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'CVTCompoundParametricStudyTool')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4315


__docformat__ = 'restructuredtext en'
__all__ = ('CVTCompoundParametricStudyTool',)


class CVTCompoundParametricStudyTool(_4431.BeltDriveCompoundParametricStudyTool):
    """CVTCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CVT_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_CVTCompoundParametricStudyTool:
        """Special nested class for casting CVTCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'CVTCompoundParametricStudyTool'):
            self._parent = parent

        @property
        def belt_drive_compound_parametric_study_tool(self):
            return self._parent._cast(_4431.BeltDriveCompoundParametricStudyTool)

        @property
        def specialised_assembly_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4519
            
            return self._parent._cast(_4519.SpecialisedAssemblyCompoundParametricStudyTool)

        @property
        def abstract_assembly_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4421
            
            return self._parent._cast(_4421.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4500
            
            return self._parent._cast(_4500.PartCompoundParametricStudyTool)

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
        def cvt_compound_parametric_study_tool(self) -> 'CVTCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4315.CVTParametricStudyTool]':
        """List[CVTParametricStudyTool]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4315.CVTParametricStudyTool]':
        """List[CVTParametricStudyTool]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CVTCompoundParametricStudyTool._Cast_CVTCompoundParametricStudyTool':
        return self._Cast_CVTCompoundParametricStudyTool(self)
