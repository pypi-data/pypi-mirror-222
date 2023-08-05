"""_6415.py

CouplingHalfCompoundDynamicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6453
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'CouplingHalfCompoundDynamicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6285


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHalfCompoundDynamicAnalysis',)


class CouplingHalfCompoundDynamicAnalysis(_6453.MountableComponentCompoundDynamicAnalysis):
    """CouplingHalfCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_CouplingHalfCompoundDynamicAnalysis:
        """Special nested class for casting CouplingHalfCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingHalfCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def mountable_component_compound_dynamic_analysis(self):
            return self._parent._cast(_6453.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6401
            
            return self._parent._cast(_6401.ComponentCompoundDynamicAnalysis)

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
        def clutch_half_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6399
            
            return self._parent._cast(_6399.ClutchHalfCompoundDynamicAnalysis)

        @property
        def concept_coupling_half_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6404
            
            return self._parent._cast(_6404.ConceptCouplingHalfCompoundDynamicAnalysis)

        @property
        def cvt_pulley_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6418
            
            return self._parent._cast(_6418.CVTPulleyCompoundDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6458
            
            return self._parent._cast(_6458.PartToPartShearCouplingHalfCompoundDynamicAnalysis)

        @property
        def pulley_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6464
            
            return self._parent._cast(_6464.PulleyCompoundDynamicAnalysis)

        @property
        def rolling_ring_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6468
            
            return self._parent._cast(_6468.RollingRingCompoundDynamicAnalysis)

        @property
        def spring_damper_half_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6480
            
            return self._parent._cast(_6480.SpringDamperHalfCompoundDynamicAnalysis)

        @property
        def synchroniser_half_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6490
            
            return self._parent._cast(_6490.SynchroniserHalfCompoundDynamicAnalysis)

        @property
        def synchroniser_part_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6491
            
            return self._parent._cast(_6491.SynchroniserPartCompoundDynamicAnalysis)

        @property
        def synchroniser_sleeve_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6492
            
            return self._parent._cast(_6492.SynchroniserSleeveCompoundDynamicAnalysis)

        @property
        def torque_converter_pump_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6495
            
            return self._parent._cast(_6495.TorqueConverterPumpCompoundDynamicAnalysis)

        @property
        def torque_converter_turbine_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6496
            
            return self._parent._cast(_6496.TorqueConverterTurbineCompoundDynamicAnalysis)

        @property
        def coupling_half_compound_dynamic_analysis(self) -> 'CouplingHalfCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingHalfCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_6285.CouplingHalfDynamicAnalysis]':
        """List[CouplingHalfDynamicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_6285.CouplingHalfDynamicAnalysis]':
        """List[CouplingHalfDynamicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis':
        return self._Cast_CouplingHalfCompoundDynamicAnalysis(self)
