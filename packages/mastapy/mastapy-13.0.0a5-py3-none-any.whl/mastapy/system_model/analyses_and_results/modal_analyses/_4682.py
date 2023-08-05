"""_4682.py

VirtualComponentModalAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4634
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'VirtualComponentModalAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.system_deflections import _2817


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualComponentModalAnalysis',)


class VirtualComponentModalAnalysis(_4634.MountableComponentModalAnalysis):
    """VirtualComponentModalAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_MODAL_ANALYSIS

    class _Cast_VirtualComponentModalAnalysis:
        """Special nested class for casting VirtualComponentModalAnalysis to subclasses."""

        def __init__(self, parent: 'VirtualComponentModalAnalysis'):
            self._parent = parent

        @property
        def mountable_component_modal_analysis(self):
            return self._parent._cast(_4634.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4575
            
            return self._parent._cast(_4575.ComponentModalAnalysis)

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
        def mass_disc_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4629
            
            return self._parent._cast(_4629.MassDiscModalAnalysis)

        @property
        def measurement_component_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4630
            
            return self._parent._cast(_4630.MeasurementComponentModalAnalysis)

        @property
        def point_load_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4645
            
            return self._parent._cast(_4645.PointLoadModalAnalysis)

        @property
        def power_load_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646
            
            return self._parent._cast(_4646.PowerLoadModalAnalysis)

        @property
        def unbalanced_mass_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681
            
            return self._parent._cast(_4681.UnbalancedMassModalAnalysis)

        @property
        def virtual_component_modal_analysis(self) -> 'VirtualComponentModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VirtualComponentModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2462.VirtualComponent':
        """VirtualComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2817.VirtualComponentSystemDeflection':
        """VirtualComponentSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis':
        return self._Cast_VirtualComponentModalAnalysis(self)
