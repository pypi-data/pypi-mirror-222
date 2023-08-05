"""_2712.py

CouplingHalfSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2764
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'CouplingHalfSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2566
    from mastapy.system_model.analyses_and_results.power_flows import _4050


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHalfSystemDeflection',)


class CouplingHalfSystemDeflection(_2764.MountableComponentSystemDeflection):
    """CouplingHalfSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_SYSTEM_DEFLECTION

    class _Cast_CouplingHalfSystemDeflection:
        """Special nested class for casting CouplingHalfSystemDeflection to subclasses."""

        def __init__(self, parent: 'CouplingHalfSystemDeflection'):
            self._parent = parent

        @property
        def mountable_component_system_deflection(self):
            return self._parent._cast(_2764.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2697
            
            return self._parent._cast(_2697.ComponentSystemDeflection)

        @property
        def part_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2767
            
            return self._parent._cast(_2767.PartSystemDeflection)

        @property
        def part_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7513
            
            return self._parent._cast(_7513.PartFEAnalysis)

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
        def clutch_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2694
            
            return self._parent._cast(_2694.ClutchHalfSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2700
            
            return self._parent._cast(_2700.ConceptCouplingHalfSystemDeflection)

        @property
        def cvt_pulley_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2715
            
            return self._parent._cast(_2715.CVTPulleySystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2769
            
            return self._parent._cast(_2769.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def pulley_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2775
            
            return self._parent._cast(_2775.PulleySystemDeflection)

        @property
        def rolling_ring_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2781
            
            return self._parent._cast(_2781.RollingRingSystemDeflection)

        @property
        def spring_damper_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2793
            
            return self._parent._cast(_2793.SpringDamperHalfSystemDeflection)

        @property
        def synchroniser_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2803
            
            return self._parent._cast(_2803.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2804
            
            return self._parent._cast(_2804.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2805
            
            return self._parent._cast(_2805.SynchroniserSleeveSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2811
            
            return self._parent._cast(_2811.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2813
            
            return self._parent._cast(_2813.TorqueConverterTurbineSystemDeflection)

        @property
        def coupling_half_system_deflection(self) -> 'CouplingHalfSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingHalfSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2566.CouplingHalf':
        """CouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4050.CouplingHalfPowerFlow':
        """CouplingHalfPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection':
        return self._Cast_CouplingHalfSystemDeflection(self)
