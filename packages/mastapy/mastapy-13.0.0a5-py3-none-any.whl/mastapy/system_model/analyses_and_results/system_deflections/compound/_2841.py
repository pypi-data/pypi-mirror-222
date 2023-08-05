"""_2841.py

BearingCompoundSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2869
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'BearingCompoundSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2422
    from mastapy.bearings.bearing_results import _1935
    from mastapy.system_model.analyses_and_results.system_deflections import _2680


__docformat__ = 'restructuredtext en'
__all__ = ('BearingCompoundSystemDeflection',)


class BearingCompoundSystemDeflection(_2869.ConnectorCompoundSystemDeflection):
    """BearingCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEARING_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_BearingCompoundSystemDeflection:
        """Special nested class for casting BearingCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'BearingCompoundSystemDeflection'):
            self._parent = parent

        @property
        def connector_compound_system_deflection(self):
            return self._parent._cast(_2869.ConnectorCompoundSystemDeflection)

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
        def bearing_compound_system_deflection(self) -> 'BearingCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BearingCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_element_stress_for_iso2812007_dynamic_equivalent_load(self) -> 'float':
        """float: 'MaximumElementStressForISO2812007DynamicEquivalentLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumElementStressForISO2812007DynamicEquivalentLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_element_stress_for_isots162812008_dynamic_equivalent_load(self) -> 'float':
        """float: 'MaximumElementStressForISOTS162812008DynamicEquivalentLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumElementStressForISOTS162812008DynamicEquivalentLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self) -> '_2422.Bearing':
        """Bearing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_1935.LoadedBearingDutyCycle':
        """LoadedBearingDutyCycle: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_2680.BearingSystemDeflection]':
        """List[BearingSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[BearingCompoundSystemDeflection]':
        """List[BearingCompoundSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_2680.BearingSystemDeflection]':
        """List[BearingSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BearingCompoundSystemDeflection._Cast_BearingCompoundSystemDeflection':
        return self._Cast_BearingCompoundSystemDeflection(self)
