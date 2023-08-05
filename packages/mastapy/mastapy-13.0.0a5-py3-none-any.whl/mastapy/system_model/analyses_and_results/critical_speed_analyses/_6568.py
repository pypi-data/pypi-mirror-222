"""_6568.py

FaceGearSetCriticalSpeedAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6573
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'FaceGearSetCriticalSpeedAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2511
    from mastapy.system_model.analyses_and_results.static_loads import _6854
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6566, _6567


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetCriticalSpeedAnalysis',)


class FaceGearSetCriticalSpeedAnalysis(_6573.GearSetCriticalSpeedAnalysis):
    """FaceGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_CRITICAL_SPEED_ANALYSIS

    class _Cast_FaceGearSetCriticalSpeedAnalysis:
        """Special nested class for casting FaceGearSetCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'FaceGearSetCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def gear_set_critical_speed_analysis(self):
            return self._parent._cast(_6573.GearSetCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6611
            
            return self._parent._cast(_6611.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6511
            
            return self._parent._cast(_6511.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6592
            
            return self._parent._cast(_6592.PartCriticalSpeedAnalysis)

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
        def face_gear_set_critical_speed_analysis(self) -> 'FaceGearSetCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGearSetCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def assembly_load_case(self) -> '_6854.FaceGearSetLoadCase':
        """FaceGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def face_gears_critical_speed_analysis(self) -> 'List[_6566.FaceGearCriticalSpeedAnalysis]':
        """List[FaceGearCriticalSpeedAnalysis]: 'FaceGearsCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearsCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_meshes_critical_speed_analysis(self) -> 'List[_6567.FaceGearMeshCriticalSpeedAnalysis]':
        """List[FaceGearMeshCriticalSpeedAnalysis]: 'FaceMeshesCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshesCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FaceGearSetCriticalSpeedAnalysis._Cast_FaceGearSetCriticalSpeedAnalysis':
        return self._Cast_FaceGearSetCriticalSpeedAnalysis(self)
