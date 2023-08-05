"""_3784.py

CouplingStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3844
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'CouplingStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2565


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingStabilityAnalysis',)


class CouplingStabilityAnalysis(_3844.SpecialisedAssemblyStabilityAnalysis):
    """CouplingStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_STABILITY_ANALYSIS

    class _Cast_CouplingStabilityAnalysis:
        """Special nested class for casting CouplingStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingStabilityAnalysis'):
            self._parent = parent

        @property
        def specialised_assembly_stability_analysis(self):
            return self._parent._cast(_3844.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3745
            
            return self._parent._cast(_3745.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3825
            
            return self._parent._cast(_3825.PartStabilityAnalysis)

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
        def clutch_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3768
            
            return self._parent._cast(_3768.ClutchStabilityAnalysis)

        @property
        def concept_coupling_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3773
            
            return self._parent._cast(_3773.ConceptCouplingStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3828
            
            return self._parent._cast(_3828.PartToPartShearCouplingStabilityAnalysis)

        @property
        def spring_damper_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3850
            
            return self._parent._cast(_3850.SpringDamperStabilityAnalysis)

        @property
        def torque_converter_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3867
            
            return self._parent._cast(_3867.TorqueConverterStabilityAnalysis)

        @property
        def coupling_stability_analysis(self) -> 'CouplingStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2565.Coupling':
        """Coupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis':
        return self._Cast_CouplingStabilityAnalysis(self)
