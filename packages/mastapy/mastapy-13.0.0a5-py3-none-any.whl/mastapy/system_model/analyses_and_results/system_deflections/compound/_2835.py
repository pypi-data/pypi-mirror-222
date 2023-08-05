"""_2835.py

AbstractShaftOrHousingCompoundSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2858
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'AbstractShaftOrHousingCompoundSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2668


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftOrHousingCompoundSystemDeflection',)


class AbstractShaftOrHousingCompoundSystemDeflection(_2858.ComponentCompoundSystemDeflection):
    """AbstractShaftOrHousingCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_AbstractShaftOrHousingCompoundSystemDeflection:
        """Special nested class for casting AbstractShaftOrHousingCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'AbstractShaftOrHousingCompoundSystemDeflection'):
            self._parent = parent

        @property
        def component_compound_system_deflection(self):
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
        def abstract_shaft_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2834
            
            return self._parent._cast(_2834.AbstractShaftCompoundSystemDeflection)

        @property
        def cycloidal_disc_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2878
            
            return self._parent._cast(_2878.CycloidalDiscCompoundSystemDeflection)

        @property
        def fe_part_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2890
            
            return self._parent._cast(_2890.FEPartCompoundSystemDeflection)

        @property
        def shaft_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2929
            
            return self._parent._cast(_2929.ShaftCompoundSystemDeflection)

        @property
        def abstract_shaft_or_housing_compound_system_deflection(self) -> 'AbstractShaftOrHousingCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftOrHousingCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_2668.AbstractShaftOrHousingSystemDeflection]':
        """List[AbstractShaftOrHousingSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_2668.AbstractShaftOrHousingSystemDeflection]':
        """List[AbstractShaftOrHousingSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftOrHousingCompoundSystemDeflection._Cast_AbstractShaftOrHousingCompoundSystemDeflection':
        return self._Cast_AbstractShaftOrHousingCompoundSystemDeflection(self)
