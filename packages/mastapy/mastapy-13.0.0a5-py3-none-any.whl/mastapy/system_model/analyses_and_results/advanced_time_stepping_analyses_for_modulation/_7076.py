"""_7076.py

SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6973
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2459
    from mastapy.system_model.analyses_and_results.system_deflections import _2788


__docformat__ = 'restructuredtext en'
__all__ = ('SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation',)


class SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation(_6973.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation):
    """SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(self):
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
        def belt_drive_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6987
            
            return self._parent._cast(_6987.BeltDriveAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6990
            
            return self._parent._cast(_6990.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6995
            
            return self._parent._cast(_6995.BevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bolted_joint_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6997
            
            return self._parent._cast(_6997.BoltedJointAdvancedTimeSteppingAnalysisForModulation)

        @property
        def clutch_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6998
            
            return self._parent._cast(_6998.ClutchAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_coupling_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7003
            
            return self._parent._cast(_7003.ConceptCouplingAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7008
            
            return self._parent._cast(_7008.ConceptGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7011
            
            return self._parent._cast(_7011.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def coupling_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7014
            
            return self._parent._cast(_7014.CouplingAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cvt_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7017
            
            return self._parent._cast(_7017.CVTAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cycloidal_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7020
            
            return self._parent._cast(_7020.CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cylindrical_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7026
            
            return self._parent._cast(_7026.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def face_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7032
            
            return self._parent._cast(_7032.FaceGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def flexible_pin_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7034
            
            return self._parent._cast(_7034.FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7037
            
            return self._parent._cast(_7037.GearSetAdvancedTimeSteppingAnalysisForModulation)

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
        def part_to_part_shear_coupling_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7058
            
            return self._parent._cast(_7058.PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation)

        @property
        def planetary_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7062
            
            return self._parent._cast(_7062.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def rolling_ring_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7070
            
            return self._parent._cast(_7070.RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7079
            
            return self._parent._cast(_7079.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spring_damper_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7080
            
            return self._parent._cast(_7080.SpringDamperAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_diff_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7085
            
            return self._parent._cast(_7085.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7088
            
            return self._parent._cast(_7088.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def synchroniser_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7091
            
            return self._parent._cast(_7091.SynchroniserAdvancedTimeSteppingAnalysisForModulation)

        @property
        def torque_converter_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7095
            
            return self._parent._cast(_7095.TorqueConverterAdvancedTimeSteppingAnalysisForModulation)

        @property
        def worm_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7103
            
            return self._parent._cast(_7103.WormGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def zerol_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7106
            
            return self._parent._cast(_7106.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(self) -> 'SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2459.SpecialisedAssembly':
        """SpecialisedAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2788.SpecialisedAssemblySystemDeflection':
        """SpecialisedAssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation(self)
