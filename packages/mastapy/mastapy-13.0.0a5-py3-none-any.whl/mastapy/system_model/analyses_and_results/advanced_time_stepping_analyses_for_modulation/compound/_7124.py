"""_7124.py

BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7112
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound', 'BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6994


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation',)


class BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation(_7112.AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation):
    """BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7112.AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7140
            
            return self._parent._cast(_7140.ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7166
            
            return self._parent._cast(_7166.GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def inter_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7172
            
            return self._parent._cast(_7172.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7142
            
            return self._parent._cast(_7142.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7119
            
            return self._parent._cast(_7119.BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spiral_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7207
            
            return self._parent._cast(_7207.SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7213
            
            return self._parent._cast(_7213.StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7216
            
            return self._parent._cast(_7216.StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def zerol_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7234
            
            return self._parent._cast(_7234.ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_6994.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation]':
        """List[BevelGearMeshAdvancedTimeSteppingAnalysisForModulation]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6994.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation]':
        """List[BevelGearMeshAdvancedTimeSteppingAnalysisForModulation]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation(self)
