"""_6761.py

TorqueConverterPumpCompoundCriticalSpeedAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6681
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'TorqueConverterPumpCompoundCriticalSpeedAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2590
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6632


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterPumpCompoundCriticalSpeedAnalysis',)


class TorqueConverterPumpCompoundCriticalSpeedAnalysis(_6681.CouplingHalfCompoundCriticalSpeedAnalysis):
    """TorqueConverterPumpCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_TorqueConverterPumpCompoundCriticalSpeedAnalysis:
        """Special nested class for casting TorqueConverterPumpCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'TorqueConverterPumpCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def coupling_half_compound_critical_speed_analysis(self):
            return self._parent._cast(_6681.CouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6719
            
            return self._parent._cast(_6719.MountableComponentCompoundCriticalSpeedAnalysis)

        @property
        def component_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6667
            
            return self._parent._cast(_6667.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6721
            
            return self._parent._cast(_6721.PartCompoundCriticalSpeedAnalysis)

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
        def torque_converter_pump_compound_critical_speed_analysis(self) -> 'TorqueConverterPumpCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorqueConverterPumpCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2590.TorqueConverterPump':
        """TorqueConverterPump: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_6632.TorqueConverterPumpCriticalSpeedAnalysis]':
        """List[TorqueConverterPumpCriticalSpeedAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6632.TorqueConverterPumpCriticalSpeedAnalysis]':
        """List[TorqueConverterPumpCriticalSpeedAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'TorqueConverterPumpCompoundCriticalSpeedAnalysis._Cast_TorqueConverterPumpCompoundCriticalSpeedAnalysis':
        return self._Cast_TorqueConverterPumpCompoundCriticalSpeedAnalysis(self)
