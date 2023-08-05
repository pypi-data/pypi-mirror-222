"""_6681.py

CouplingHalfCompoundCriticalSpeedAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6719
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'CouplingHalfCompoundCriticalSpeedAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6550


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHalfCompoundCriticalSpeedAnalysis',)


class CouplingHalfCompoundCriticalSpeedAnalysis(_6719.MountableComponentCompoundCriticalSpeedAnalysis):
    """CouplingHalfCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_CouplingHalfCompoundCriticalSpeedAnalysis:
        """Special nested class for casting CouplingHalfCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingHalfCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def mountable_component_compound_critical_speed_analysis(self):
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
        def clutch_half_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6665
            
            return self._parent._cast(_6665.ClutchHalfCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_half_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6670
            
            return self._parent._cast(_6670.ConceptCouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def cvt_pulley_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6684
            
            return self._parent._cast(_6684.CVTPulleyCompoundCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6724
            
            return self._parent._cast(_6724.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def pulley_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6730
            
            return self._parent._cast(_6730.PulleyCompoundCriticalSpeedAnalysis)

        @property
        def rolling_ring_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6734
            
            return self._parent._cast(_6734.RollingRingCompoundCriticalSpeedAnalysis)

        @property
        def spring_damper_half_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6746
            
            return self._parent._cast(_6746.SpringDamperHalfCompoundCriticalSpeedAnalysis)

        @property
        def synchroniser_half_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6756
            
            return self._parent._cast(_6756.SynchroniserHalfCompoundCriticalSpeedAnalysis)

        @property
        def synchroniser_part_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6757
            
            return self._parent._cast(_6757.SynchroniserPartCompoundCriticalSpeedAnalysis)

        @property
        def synchroniser_sleeve_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6758
            
            return self._parent._cast(_6758.SynchroniserSleeveCompoundCriticalSpeedAnalysis)

        @property
        def torque_converter_pump_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6761
            
            return self._parent._cast(_6761.TorqueConverterPumpCompoundCriticalSpeedAnalysis)

        @property
        def torque_converter_turbine_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6762
            
            return self._parent._cast(_6762.TorqueConverterTurbineCompoundCriticalSpeedAnalysis)

        @property
        def coupling_half_compound_critical_speed_analysis(self) -> 'CouplingHalfCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingHalfCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_6550.CouplingHalfCriticalSpeedAnalysis]':
        """List[CouplingHalfCriticalSpeedAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_6550.CouplingHalfCriticalSpeedAnalysis]':
        """List[CouplingHalfCriticalSpeedAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis':
        return self._Cast_CouplingHalfCompoundCriticalSpeedAnalysis(self)
