"""_6431.py

FaceGearSetCompoundDynamicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6436
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'FaceGearSetCompoundDynamicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2511
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6429, _6430


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetCompoundDynamicAnalysis',)


class FaceGearSetCompoundDynamicAnalysis(_6436.GearSetCompoundDynamicAnalysis):
    """FaceGearSetCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_FaceGearSetCompoundDynamicAnalysis:
        """Special nested class for casting FaceGearSetCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'FaceGearSetCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def gear_set_compound_dynamic_analysis(self):
            return self._parent._cast(_6436.GearSetCompoundDynamicAnalysis)

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
        def face_gear_set_compound_dynamic_analysis(self) -> 'FaceGearSetCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGearSetCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2511.FaceGearSet':
        """FaceGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2511.FaceGearSet':
        """FaceGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6302.FaceGearSetDynamicAnalysis]':
        """List[FaceGearSetDynamicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_gears_compound_dynamic_analysis(self) -> 'List[_6429.FaceGearCompoundDynamicAnalysis]':
        """List[FaceGearCompoundDynamicAnalysis]: 'FaceGearsCompoundDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearsCompoundDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_meshes_compound_dynamic_analysis(self) -> 'List[_6430.FaceGearMeshCompoundDynamicAnalysis]':
        """List[FaceGearMeshCompoundDynamicAnalysis]: 'FaceMeshesCompoundDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshesCompoundDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6302.FaceGearSetDynamicAnalysis]':
        """List[FaceGearSetDynamicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FaceGearSetCompoundDynamicAnalysis._Cast_FaceGearSetCompoundDynamicAnalysis':
        return self._Cast_FaceGearSetCompoundDynamicAnalysis(self)
