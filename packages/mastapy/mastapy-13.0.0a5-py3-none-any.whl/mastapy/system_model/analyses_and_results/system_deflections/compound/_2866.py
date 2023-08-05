"""_2866.py

ConicalGearMeshCompoundSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2893
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'ConicalGearMeshCompoundSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2706


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearMeshCompoundSystemDeflection',)


class ConicalGearMeshCompoundSystemDeflection(_2893.GearMeshCompoundSystemDeflection):
    """ConicalGearMeshCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_ConicalGearMeshCompoundSystemDeflection:
        """Special nested class for casting ConicalGearMeshCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'ConicalGearMeshCompoundSystemDeflection'):
            self._parent = parent

        @property
        def gear_mesh_compound_system_deflection(self):
            return self._parent._cast(_2893.GearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2899
            
            return self._parent._cast(_2899.InterMountableComponentConnectionCompoundSystemDeflection)

        @property
        def connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2868
            
            return self._parent._cast(_2868.ConnectionCompoundSystemDeflection)

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
        def agma_gleason_conical_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2838
            
            return self._parent._cast(_2838.AGMAGleasonConicalGearMeshCompoundSystemDeflection)

        @property
        def bevel_differential_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2845
            
            return self._parent._cast(_2845.BevelDifferentialGearMeshCompoundSystemDeflection)

        @property
        def bevel_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2850
            
            return self._parent._cast(_2850.BevelGearMeshCompoundSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2897
            
            return self._parent._cast(_2897.HypoidGearMeshCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2901
            
            return self._parent._cast(_2901.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2904
            
            return self._parent._cast(_2904.KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2907
            
            return self._parent._cast(_2907.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2935
            
            return self._parent._cast(_2935.SpiralBevelGearMeshCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2941
            
            return self._parent._cast(_2941.StraightBevelDiffGearMeshCompoundSystemDeflection)

        @property
        def straight_bevel_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2944
            
            return self._parent._cast(_2944.StraightBevelGearMeshCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2962
            
            return self._parent._cast(_2962.ZerolBevelGearMeshCompoundSystemDeflection)

        @property
        def conical_gear_mesh_compound_system_deflection(self) -> 'ConicalGearMeshCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearMeshCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self) -> 'List[ConicalGearMeshCompoundSystemDeflection]':
        """List[ConicalGearMeshCompoundSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_2706.ConicalGearMeshSystemDeflection]':
        """List[ConicalGearMeshSystemDeflection]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_2706.ConicalGearMeshSystemDeflection]':
        """List[ConicalGearMeshSystemDeflection]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalGearMeshCompoundSystemDeflection._Cast_ConicalGearMeshCompoundSystemDeflection':
        return self._Cast_ConicalGearMeshCompoundSystemDeflection(self)
