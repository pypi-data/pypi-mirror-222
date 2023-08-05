"""_4592.py

CVTModalAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4560
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'CVTModalAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2568
    from mastapy.system_model.analyses_and_results.system_deflections import _2716


__docformat__ = 'restructuredtext en'
__all__ = ('CVTModalAnalysis',)


class CVTModalAnalysis(_4560.BeltDriveModalAnalysis):
    """CVTModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_MODAL_ANALYSIS

    class _Cast_CVTModalAnalysis:
        """Special nested class for casting CVTModalAnalysis to subclasses."""

        def __init__(self, parent: 'CVTModalAnalysis'):
            self._parent = parent

        @property
        def belt_drive_modal_analysis(self):
            return self._parent._cast(_4560.BeltDriveModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658
            
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
        def cvt_modal_analysis(self) -> 'CVTModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTModalAnalysis.TYPE'):
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
    def system_deflection_results(self) -> '_2716.CVTSystemDeflection':
        """CVTSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CVTModalAnalysis._Cast_CVTModalAnalysis':
        return self._Cast_CVTModalAnalysis(self)
