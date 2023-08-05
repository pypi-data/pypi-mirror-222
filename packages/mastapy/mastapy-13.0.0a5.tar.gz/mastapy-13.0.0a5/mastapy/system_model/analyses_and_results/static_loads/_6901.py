"""_6901.py

PlanetaryGearSetLoadCase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6833
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PlanetaryGearSetLoadCase')

if TYPE_CHECKING:
    from mastapy.utility import _1580
    from mastapy.system_model.part_model.gears import _2524


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryGearSetLoadCase',)


class PlanetaryGearSetLoadCase(_6833.CylindricalGearSetLoadCase):
    """PlanetaryGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_LOAD_CASE

    class _Cast_PlanetaryGearSetLoadCase:
        """Special nested class for casting PlanetaryGearSetLoadCase to subclasses."""

        def __init__(self, parent: 'PlanetaryGearSetLoadCase'):
            self._parent = parent

        @property
        def cylindrical_gear_set_load_case(self):
            return self._parent._cast(_6833.CylindricalGearSetLoadCase)

        @property
        def gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6863
            
            return self._parent._cast(_6863.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6920
            
            return self._parent._cast(_6920.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6774
            
            return self._parent._cast(_6774.AbstractAssemblyLoadCase)

        @property
        def part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6896
            
            return self._parent._cast(_6896.PartLoadCase)

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
        def planetary_gear_set_load_case(self) -> 'PlanetaryGearSetLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetaryGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def include_gear_blank_elastic_distortion(self) -> '_1580.LoadCaseOverrideOption':
        """LoadCaseOverrideOption: 'IncludeGearBlankElasticDistortion' is the original name of this property."""

        temp = self.wrapped.IncludeGearBlankElasticDistortion

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Utility.LoadCaseOverrideOption')
        return constructor.new_from_mastapy('mastapy.utility._1580', 'LoadCaseOverrideOption')(value) if value is not None else None

    @include_gear_blank_elastic_distortion.setter
    def include_gear_blank_elastic_distortion(self, value: '_1580.LoadCaseOverrideOption'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Utility.LoadCaseOverrideOption')
        self.wrapped.IncludeGearBlankElasticDistortion = value

    @property
    def specify_separate_micro_geometry_for_each_planet_gear(self) -> 'bool':
        """bool: 'SpecifySeparateMicroGeometryForEachPlanetGear' is the original name of this property."""

        temp = self.wrapped.SpecifySeparateMicroGeometryForEachPlanetGear

        if temp is None:
            return False

        return temp

    @specify_separate_micro_geometry_for_each_planet_gear.setter
    def specify_separate_micro_geometry_for_each_planet_gear(self, value: 'bool'):
        self.wrapped.SpecifySeparateMicroGeometryForEachPlanetGear = bool(value) if value is not None else False

    @property
    def assembly_design(self) -> '_2524.PlanetaryGearSet':
        """PlanetaryGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PlanetaryGearSetLoadCase._Cast_PlanetaryGearSetLoadCase':
        return self._Cast_PlanetaryGearSetLoadCase(self)
