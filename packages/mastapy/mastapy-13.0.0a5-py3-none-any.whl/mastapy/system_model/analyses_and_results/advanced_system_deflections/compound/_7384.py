"""_7384.py

BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7389
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'BevelDifferentialGearMeshCompoundAdvancedSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2284
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7251


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearMeshCompoundAdvancedSystemDeflection',)


class BevelDifferentialGearMeshCompoundAdvancedSystemDeflection(_7389.BevelGearMeshCompoundAdvancedSystemDeflection):
    """BevelDifferentialGearMeshCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_BevelDifferentialGearMeshCompoundAdvancedSystemDeflection:
        """Special nested class for casting BevelDifferentialGearMeshCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'BevelDifferentialGearMeshCompoundAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_advanced_system_deflection(self):
            return self._parent._cast(_7389.BevelGearMeshCompoundAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7377
            
            return self._parent._cast(_7377.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection)

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7405
            
            return self._parent._cast(_7405.ConicalGearMeshCompoundAdvancedSystemDeflection)

        @property
        def gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7431
            
            return self._parent._cast(_7431.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7437
            
            return self._parent._cast(_7437.InterMountableComponentConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7407
            
            return self._parent._cast(_7407.ConnectionCompoundAdvancedSystemDeflection)

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
        def bevel_differential_gear_mesh_compound_advanced_system_deflection(self) -> 'BevelDifferentialGearMeshCompoundAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearMeshCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2284.BevelDifferentialGearMesh':
        """BevelDifferentialGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2284.BevelDifferentialGearMesh':
        """BevelDifferentialGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_7251.BevelDifferentialGearMeshAdvancedSystemDeflection]':
        """List[BevelDifferentialGearMeshAdvancedSystemDeflection]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_7251.BevelDifferentialGearMeshAdvancedSystemDeflection]':
        """List[BevelDifferentialGearMeshAdvancedSystemDeflection]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelDifferentialGearMeshCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshCompoundAdvancedSystemDeflection':
        return self._Cast_BevelDifferentialGearMeshCompoundAdvancedSystemDeflection(self)
