"""_2942.py

StraightBevelDiffGearSetCompoundSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2851
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'StraightBevelDiffGearSetCompoundSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2528
    from mastapy.system_model.analyses_and_results.system_deflections import _2796
    from mastapy.system_model.analyses_and_results.system_deflections.compound import _2940, _2941


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetCompoundSystemDeflection',)


class StraightBevelDiffGearSetCompoundSystemDeflection(_2851.BevelGearSetCompoundSystemDeflection):
    """StraightBevelDiffGearSetCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_StraightBevelDiffGearSetCompoundSystemDeflection:
        """Special nested class for casting StraightBevelDiffGearSetCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'StraightBevelDiffGearSetCompoundSystemDeflection'):
            self._parent = parent

        @property
        def bevel_gear_set_compound_system_deflection(self):
            return self._parent._cast(_2851.BevelGearSetCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2839
            
            return self._parent._cast(_2839.AGMAGleasonConicalGearSetCompoundSystemDeflection)

        @property
        def conical_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2867
            
            return self._parent._cast(_2867.ConicalGearSetCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2894
            
            return self._parent._cast(_2894.GearSetCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2933
            
            return self._parent._cast(_2933.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2833
            
            return self._parent._cast(_2833.AbstractAssemblyCompoundSystemDeflection)

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
        def straight_bevel_diff_gear_set_compound_system_deflection(self) -> 'StraightBevelDiffGearSetCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2528.StraightBevelDiffGearSet':
        """StraightBevelDiffGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2528.StraightBevelDiffGearSet':
        """StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2796.StraightBevelDiffGearSetSystemDeflection]':
        """List[StraightBevelDiffGearSetSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_gears_compound_system_deflection(self) -> 'List[_2940.StraightBevelDiffGearCompoundSystemDeflection]':
        """List[StraightBevelDiffGearCompoundSystemDeflection]: 'StraightBevelDiffGearsCompoundSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearsCompoundSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_meshes_compound_system_deflection(self) -> 'List[_2941.StraightBevelDiffGearMeshCompoundSystemDeflection]':
        """List[StraightBevelDiffGearMeshCompoundSystemDeflection]: 'StraightBevelDiffMeshesCompoundSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffMeshesCompoundSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_2796.StraightBevelDiffGearSetSystemDeflection]':
        """List[StraightBevelDiffGearSetSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelDiffGearSetCompoundSystemDeflection._Cast_StraightBevelDiffGearSetCompoundSystemDeflection':
        return self._Cast_StraightBevelDiffGearSetCompoundSystemDeflection(self)
