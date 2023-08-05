"""_7301.py

GearSetAdvancedSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7340
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'GearSetAdvancedSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7316
    from mastapy.system_model.part_model.gears import _2514
    from mastapy.gears.rating import _361


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetAdvancedSystemDeflection',)


class GearSetAdvancedSystemDeflection(_7340.SpecialisedAssemblyAdvancedSystemDeflection):
    """GearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_GearSetAdvancedSystemDeflection:
        """Special nested class for casting GearSetAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'GearSetAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def specialised_assembly_advanced_system_deflection(self):
            return self._parent._cast(_7340.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7236
            
            return self._parent._cast(_7236.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7321
            
            return self._parent._cast(_7321.PartAdvancedSystemDeflection)

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
        def agma_gleason_conical_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7245
            
            return self._parent._cast(_7245.AGMAGleasonConicalGearSetAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7252
            
            return self._parent._cast(_7252.BevelDifferentialGearSetAdvancedSystemDeflection)

        @property
        def bevel_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7257
            
            return self._parent._cast(_7257.BevelGearSetAdvancedSystemDeflection)

        @property
        def concept_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7270
            
            return self._parent._cast(_7270.ConceptGearSetAdvancedSystemDeflection)

        @property
        def conical_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7273
            
            return self._parent._cast(_7273.ConicalGearSetAdvancedSystemDeflection)

        @property
        def cylindrical_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7289
            
            return self._parent._cast(_7289.CylindricalGearSetAdvancedSystemDeflection)

        @property
        def face_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7296
            
            return self._parent._cast(_7296.FaceGearSetAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7305
            
            return self._parent._cast(_7305.HypoidGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7309
            
            return self._parent._cast(_7309.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7312
            
            return self._parent._cast(_7312.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7315
            
            return self._parent._cast(_7315.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def planetary_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7326
            
            return self._parent._cast(_7326.PlanetaryGearSetAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7343
            
            return self._parent._cast(_7343.SpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7349
            
            return self._parent._cast(_7349.StraightBevelDiffGearSetAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7352
            
            return self._parent._cast(_7352.StraightBevelGearSetAdvancedSystemDeflection)

        @property
        def worm_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7368
            
            return self._parent._cast(_7368.WormGearSetAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7371
            
            return self._parent._cast(_7371.ZerolBevelGearSetAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(self) -> 'GearSetAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def use_ltca_in_advanced_system_deflection(self) -> '_7316.UseLtcaInAsdOption':
        """UseLtcaInAsdOption: 'UseLTCAInAdvancedSystemDeflection' is the original name of this property."""

        temp = self.wrapped.UseLTCAInAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.UseLtcaInAsdOption')
        return constructor.new_from_mastapy('mastapy.system_model.analyses_and_results.advanced_system_deflections._7316', 'UseLtcaInAsdOption')(value) if value is not None else None

    @use_ltca_in_advanced_system_deflection.setter
    def use_ltca_in_advanced_system_deflection(self, value: '_7316.UseLtcaInAsdOption'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.UseLtcaInAsdOption')
        self.wrapped.UseLTCAInAdvancedSystemDeflection = value

    @property
    def assembly_design(self) -> '_2514.GearSet':
        """GearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_361.GearSetRating':
        """GearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection':
        return self._Cast_GearSetAdvancedSystemDeflection(self)
