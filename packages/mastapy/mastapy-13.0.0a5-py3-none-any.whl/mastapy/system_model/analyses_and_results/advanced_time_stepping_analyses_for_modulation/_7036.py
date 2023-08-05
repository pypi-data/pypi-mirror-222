"""_7036.py

GearMeshAdvancedTimeSteppingAnalysisForModulation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7043
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'GearMeshAdvancedTimeSteppingAnalysisForModulation')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2296
    from mastapy.system_model.analyses_and_results.system_deflections import _2741


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshAdvancedTimeSteppingAnalysisForModulation',)


class GearMeshAdvancedTimeSteppingAnalysisForModulation(_7043.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation):
    """GearMeshAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting GearMeshAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'GearMeshAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7043.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7012
            
            return self._parent._cast(_7012.ConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def connection_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7504
            
            return self._parent._cast(_7504.ConnectionAnalysisCase)

        @property
        def connection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2631
            
            return self._parent._cast(_2631.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2635
            
            return self._parent._cast(_2635.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6981
            
            return self._parent._cast(_6981.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6989
            
            return self._parent._cast(_6989.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6994
            
            return self._parent._cast(_6994.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7007
            
            return self._parent._cast(_7007.ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7010
            
            return self._parent._cast(_7010.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cylindrical_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7025
            
            return self._parent._cast(_7025.CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def face_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7031
            
            return self._parent._cast(_7031.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7041
            
            return self._parent._cast(_7041.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7045
            
            return self._parent._cast(_7045.KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7048
            
            return self._parent._cast(_7048.KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7051
            
            return self._parent._cast(_7051.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7078
            
            return self._parent._cast(_7078.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_diff_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7084
            
            return self._parent._cast(_7084.StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7087
            
            return self._parent._cast(_7087.StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def worm_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7102
            
            return self._parent._cast(_7102.WormGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def zerol_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7105
            
            return self._parent._cast(_7105.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_mesh_advanced_time_stepping_analysis_for_modulation(self) -> 'GearMeshAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_teeth_passed(self) -> 'float':
        """float: 'NumberOfTeethPassed' is the original name of this property."""

        temp = self.wrapped.NumberOfTeethPassed

        if temp is None:
            return 0.0

        return temp

    @number_of_teeth_passed.setter
    def number_of_teeth_passed(self, value: 'float'):
        self.wrapped.NumberOfTeethPassed = float(value) if value is not None else 0.0

    @property
    def connection_design(self) -> '_2296.GearMesh':
        """GearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2741.GearMeshSystemDeflection':
        """GearMeshSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation(self)
