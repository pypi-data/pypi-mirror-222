"""_7037.py

GearSetAdvancedTimeSteppingAnalysisForModulation
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7076
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'GearSetAdvancedTimeSteppingAnalysisForModulation')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2514
    from mastapy.math_utility import _1498
    from mastapy.system_model.analyses_and_results.system_deflections import _2742


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetAdvancedTimeSteppingAnalysisForModulation',)


class GearSetAdvancedTimeSteppingAnalysisForModulation(_7076.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation):
    """GearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_GearSetAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting GearSetAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'GearSetAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7076.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6973
            
            return self._parent._cast(_6973.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7057
            
            return self._parent._cast(_7057.PartAdvancedTimeSteppingAnalysisForModulation)

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
        def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6982
            
            return self._parent._cast(_6982.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6990
            
            return self._parent._cast(_6990.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6995
            
            return self._parent._cast(_6995.BevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7008
            
            return self._parent._cast(_7008.ConceptGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7011
            
            return self._parent._cast(_7011.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cylindrical_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7026
            
            return self._parent._cast(_7026.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def face_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7032
            
            return self._parent._cast(_7032.FaceGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7042
            
            return self._parent._cast(_7042.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7046
            
            return self._parent._cast(_7046.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7049
            
            return self._parent._cast(_7049.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7052
            
            return self._parent._cast(_7052.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def planetary_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7062
            
            return self._parent._cast(_7062.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7079
            
            return self._parent._cast(_7079.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_diff_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7085
            
            return self._parent._cast(_7085.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7088
            
            return self._parent._cast(_7088.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def worm_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7103
            
            return self._parent._cast(_7103.WormGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def zerol_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7106
            
            return self._parent._cast(_7106.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(self) -> 'GearSetAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def eignenmodes_indexed_by_mode_id(self) -> 'List[_1498.Eigenmodes]':
        """List[Eigenmodes]: 'EignenmodesIndexedByModeId' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EignenmodesIndexedByModeId

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def system_deflection_results(self) -> '_2742.GearSetSystemDeflection':
        """GearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation(self)
