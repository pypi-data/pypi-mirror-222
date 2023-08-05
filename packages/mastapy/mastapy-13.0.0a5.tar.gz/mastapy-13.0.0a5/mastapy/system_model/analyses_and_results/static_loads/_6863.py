"""_6863.py

GearSetLoadCase
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.analyses_and_results.static_loads import _6920
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'GearSetLoadCase')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5412
    from mastapy.system_model.analyses_and_results.static_loads import _6891, _6858, _6860
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6979
    from mastapy.system_model.part_model.gears import _2514


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetLoadCase',)


class GearSetLoadCase(_6920.SpecialisedAssemblyLoadCase):
    """GearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_LOAD_CASE

    class _Cast_GearSetLoadCase:
        """Special nested class for casting GearSetLoadCase to subclasses."""

        def __init__(self, parent: 'GearSetLoadCase'):
            self._parent = parent

        @property
        def specialised_assembly_load_case(self):
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
        def agma_gleason_conical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6783
            
            return self._parent._cast(_6783.AGMAGleasonConicalGearSetLoadCase)

        @property
        def bevel_differential_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6792
            
            return self._parent._cast(_6792.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6797
            
            return self._parent._cast(_6797.BevelGearSetLoadCase)

        @property
        def concept_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6811
            
            return self._parent._cast(_6811.ConceptGearSetLoadCase)

        @property
        def conical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6816
            
            return self._parent._cast(_6816.ConicalGearSetLoadCase)

        @property
        def cylindrical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6833
            
            return self._parent._cast(_6833.CylindricalGearSetLoadCase)

        @property
        def face_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6854
            
            return self._parent._cast(_6854.FaceGearSetLoadCase)

        @property
        def hypoid_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6875
            
            return self._parent._cast(_6875.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6882
            
            return self._parent._cast(_6882.KlingelnbergCycloPalloidConicalGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6885
            
            return self._parent._cast(_6885.KlingelnbergCycloPalloidHypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6888
            
            return self._parent._cast(_6888.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)

        @property
        def planetary_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6901
            
            return self._parent._cast(_6901.PlanetaryGearSetLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6923
            
            return self._parent._cast(_6923.SpiralBevelGearSetLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6929
            
            return self._parent._cast(_6929.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6932
            
            return self._parent._cast(_6932.StraightBevelGearSetLoadCase)

        @property
        def worm_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6952
            
            return self._parent._cast(_6952.WormGearSetLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6955
            
            return self._parent._cast(_6955.ZerolBevelGearSetLoadCase)

        @property
        def gear_set_load_case(self) -> 'GearSetLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitation_data_is_up_to_date(self) -> 'bool':
        """bool: 'ExcitationDataIsUpToDate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitationDataIsUpToDate

        if temp is None:
            return False

        return temp

    @property
    def gear_mesh_stiffness_model(self) -> '_5412.GearMeshStiffnessModel':
        """GearMeshStiffnessModel: 'GearMeshStiffnessModel' is the original name of this property."""

        temp = self.wrapped.GearMeshStiffnessModel

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.GearMeshStiffnessModel')
        return constructor.new_from_mastapy('mastapy.system_model.analyses_and_results.mbd_analyses._5412', 'GearMeshStiffnessModel')(value) if value is not None else None

    @gear_mesh_stiffness_model.setter
    def gear_mesh_stiffness_model(self, value: '_5412.GearMeshStiffnessModel'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.GearMeshStiffnessModel')
        self.wrapped.GearMeshStiffnessModel = value

    @property
    def mesh_stiffness_source(self) -> 'overridable.Overridable_MeshStiffnessSource':
        """overridable.Overridable_MeshStiffnessSource: 'MeshStiffnessSource' is the original name of this property."""

        temp = self.wrapped.MeshStiffnessSource

        if temp is None:
            return None

        value = overridable.Overridable_MeshStiffnessSource.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @mesh_stiffness_source.setter
    def mesh_stiffness_source(self, value: 'overridable.Overridable_MeshStiffnessSource.implicit_type()'):
        wrapper_type = overridable.Overridable_MeshStiffnessSource.wrapper_type()
        enclosed_type = overridable.Overridable_MeshStiffnessSource.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value if value is not None else None, is_overridden)
        self.wrapped.MeshStiffnessSource = value

    @property
    def use_advanced_model_in_advanced_time_stepping_analysis_for_modulation(self) -> 'bool':
        """bool: 'UseAdvancedModelInAdvancedTimeSteppingAnalysisForModulation' is the original name of this property."""

        temp = self.wrapped.UseAdvancedModelInAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return False

        return temp

    @use_advanced_model_in_advanced_time_stepping_analysis_for_modulation.setter
    def use_advanced_model_in_advanced_time_stepping_analysis_for_modulation(self, value: 'bool'):
        self.wrapped.UseAdvancedModelInAdvancedTimeSteppingAnalysisForModulation = bool(value) if value is not None else False

    @property
    def advanced_time_stepping_analysis_for_modulation_options(self) -> '_6979.AdvancedTimeSteppingAnalysisForModulationOptions':
        """AdvancedTimeSteppingAnalysisForModulationOptions: 'AdvancedTimeSteppingAnalysisForModulationOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdvancedTimeSteppingAnalysisForModulationOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def gears(self) -> 'List[_6858.GearLoadCase]':
        """List[GearLoadCase]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gears_without_clones(self) -> 'List[_6858.GearLoadCase]':
        """List[GearLoadCase]: 'GearsWithoutClones' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearsWithoutClones

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshes_without_planetary_duplicates(self) -> 'List[_6860.GearMeshLoadCase]':
        """List[GearMeshLoadCase]: 'MeshesWithoutPlanetaryDuplicates' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshesWithoutPlanetaryDuplicates

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearSetLoadCase._Cast_GearSetLoadCase':
        return self._Cast_GearSetLoadCase(self)
