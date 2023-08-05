"""_6417.py

CVTCompoundDynamicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6386
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'CVTCompoundDynamicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6287


__docformat__ = 'restructuredtext en'
__all__ = ('CVTCompoundDynamicAnalysis',)


class CVTCompoundDynamicAnalysis(_6386.BeltDriveCompoundDynamicAnalysis):
    """CVTCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_CVTCompoundDynamicAnalysis:
        """Special nested class for casting CVTCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'CVTCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def belt_drive_compound_dynamic_analysis(self):
            return self._parent._cast(_6386.BeltDriveCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6474
            
            return self._parent._cast(_6474.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6376
            
            return self._parent._cast(_6376.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6455
            
            return self._parent._cast(_6455.PartCompoundDynamicAnalysis)

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
        def cvt_compound_dynamic_analysis(self) -> 'CVTCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6287.CVTDynamicAnalysis]':
        """List[CVTDynamicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6287.CVTDynamicAnalysis]':
        """List[CVTDynamicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CVTCompoundDynamicAnalysis._Cast_CVTCompoundDynamicAnalysis':
        return self._Cast_CVTCompoundDynamicAnalysis(self)
