"""_2909.py

MassDiscCompoundSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2957
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'MassDiscCompoundSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2445
    from mastapy.system_model.analyses_and_results.system_deflections import _2761


__docformat__ = 'restructuredtext en'
__all__ = ('MassDiscCompoundSystemDeflection',)


class MassDiscCompoundSystemDeflection(_2957.VirtualComponentCompoundSystemDeflection):
    """MassDiscCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_MassDiscCompoundSystemDeflection:
        """Special nested class for casting MassDiscCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'MassDiscCompoundSystemDeflection'):
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
        def mass_disc_compound_system_deflection(self) -> 'MassDiscCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MassDiscCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2445.MassDisc':
        """MassDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_2761.MassDiscSystemDeflection]':
        """List[MassDiscSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[MassDiscCompoundSystemDeflection]':
        """List[MassDiscCompoundSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_2761.MassDiscSystemDeflection]':
        """List[MassDiscSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'MassDiscCompoundSystemDeflection._Cast_MassDiscCompoundSystemDeflection':
        return self._Cast_MassDiscCompoundSystemDeflection(self)
