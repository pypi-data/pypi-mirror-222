"""_2956.py

UnbalancedMassCompoundSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2957
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'UnbalancedMassCompoundSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2460
    from mastapy.system_model.analyses_and_results.system_deflections import _2816


__docformat__ = 'restructuredtext en'
__all__ = ('UnbalancedMassCompoundSystemDeflection',)


class UnbalancedMassCompoundSystemDeflection(_2957.VirtualComponentCompoundSystemDeflection):
    """UnbalancedMassCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_UnbalancedMassCompoundSystemDeflection:
        """Special nested class for casting UnbalancedMassCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'UnbalancedMassCompoundSystemDeflection'):
            self._parent = parent

        @property
        def virtual_component_compound_system_deflection(self):
            return self._parent._cast(_2957.VirtualComponentCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2911
            
            return self._parent._cast(_2911.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2858
            
            return self._parent._cast(_2858.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2913
            
            return self._parent._cast(_2913.PartCompoundSystemDeflection)

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
        def unbalanced_mass_compound_system_deflection(self) -> 'UnbalancedMassCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'UnbalancedMassCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2460.UnbalancedMass':
        """UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_2816.UnbalancedMassSystemDeflection]':
        """List[UnbalancedMassSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_2816.UnbalancedMassSystemDeflection]':
        """List[UnbalancedMassSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'UnbalancedMassCompoundSystemDeflection._Cast_UnbalancedMassCompoundSystemDeflection':
        return self._Cast_UnbalancedMassCompoundSystemDeflection(self)
