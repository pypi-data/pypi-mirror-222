"""_4590.py

CouplingModalAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4658
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'CouplingModalAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2565
    from mastapy.system_model.analyses_and_results.system_deflections import _2713


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingModalAnalysis',)


class CouplingModalAnalysis(_4658.SpecialisedAssemblyModalAnalysis):
    """CouplingModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_MODAL_ANALYSIS

    class _Cast_CouplingModalAnalysis:
        """Special nested class for casting CouplingModalAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingModalAnalysis'):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis(self):
            return self._parent._cast(_4658.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4550
            
            return self._parent._cast(_4550.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4638
            
            return self._parent._cast(_4638.PartModalAnalysis)

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
        def clutch_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4573
            
            return self._parent._cast(_4573.ClutchModalAnalysis)

        @property
        def concept_coupling_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4578
            
            return self._parent._cast(_4578.ConceptCouplingModalAnalysis)

        @property
        def part_to_part_shear_coupling_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4641
            
            return self._parent._cast(_4641.PartToPartShearCouplingModalAnalysis)

        @property
        def spring_damper_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4664
            
            return self._parent._cast(_4664.SpringDamperModalAnalysis)

        @property
        def torque_converter_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4678
            
            return self._parent._cast(_4678.TorqueConverterModalAnalysis)

        @property
        def coupling_modal_analysis(self) -> 'CouplingModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingModalAnalysis.TYPE'):
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
    def system_deflection_results(self) -> '_2713.CouplingSystemDeflection':
        """CouplingSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingModalAnalysis._Cast_CouplingModalAnalysis':
        return self._Cast_CouplingModalAnalysis(self)
