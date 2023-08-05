"""_6554.py

CVTCriticalSpeedAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6521
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'CVTCriticalSpeedAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2568


__docformat__ = 'restructuredtext en'
__all__ = ('CVTCriticalSpeedAnalysis',)


class CVTCriticalSpeedAnalysis(_6521.BeltDriveCriticalSpeedAnalysis):
    """CVTCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_CRITICAL_SPEED_ANALYSIS

    class _Cast_CVTCriticalSpeedAnalysis:
        """Special nested class for casting CVTCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'CVTCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def belt_drive_critical_speed_analysis(self):
            return self._parent._cast(_6521.BeltDriveCriticalSpeedAnalysis)

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
        def cvt_critical_speed_analysis(self) -> 'CVTCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2568.CVT':
        """CVT: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CVTCriticalSpeedAnalysis._Cast_CVTCriticalSpeedAnalysis':
        return self._Cast_CVTCriticalSpeedAnalysis(self)
