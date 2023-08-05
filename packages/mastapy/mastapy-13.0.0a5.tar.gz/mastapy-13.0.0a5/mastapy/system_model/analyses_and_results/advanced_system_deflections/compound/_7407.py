"""_7407.py

ConnectionCompoundAdvancedSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7505
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'ConnectionCompoundAdvancedSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7274


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionCompoundAdvancedSystemDeflection',)


class ConnectionCompoundAdvancedSystemDeflection(_7505.ConnectionCompoundAnalysis):
    """ConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_ConnectionCompoundAdvancedSystemDeflection:
        """Special nested class for casting ConnectionCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'ConnectionCompoundAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def connection_compound_analysis(self):
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
        def abstract_shaft_to_mountable_component_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7375
            
            return self._parent._cast(_7375.AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7377
            
            return self._parent._cast(_7377.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection)

        @property
        def belt_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7381
            
            return self._parent._cast(_7381.BeltConnectionCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7384
            
            return self._parent._cast(_7384.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection)

        @property
        def bevel_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7389
            
            return self._parent._cast(_7389.BevelGearMeshCompoundAdvancedSystemDeflection)

        @property
        def clutch_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7394
            
            return self._parent._cast(_7394.ClutchConnectionCompoundAdvancedSystemDeflection)

        @property
        def coaxial_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7396
            
            return self._parent._cast(_7396.CoaxialConnectionCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7399
            
            return self._parent._cast(_7399.ConceptCouplingConnectionCompoundAdvancedSystemDeflection)

        @property
        def concept_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7402
            
            return self._parent._cast(_7402.ConceptGearMeshCompoundAdvancedSystemDeflection)

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7405
            
            return self._parent._cast(_7405.ConicalGearMeshCompoundAdvancedSystemDeflection)

        @property
        def coupling_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7410
            
            return self._parent._cast(_7410.CouplingConnectionCompoundAdvancedSystemDeflection)

        @property
        def cvt_belt_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7412
            
            return self._parent._cast(_7412.CVTBeltConnectionCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7416
            
            return self._parent._cast(_7416.CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7418
            
            return self._parent._cast(_7418.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection)

        @property
        def cylindrical_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7420
            
            return self._parent._cast(_7420.CylindricalGearMeshCompoundAdvancedSystemDeflection)

        @property
        def face_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7426
            
            return self._parent._cast(_7426.FaceGearMeshCompoundAdvancedSystemDeflection)

        @property
        def gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7431
            
            return self._parent._cast(_7431.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7435
            
            return self._parent._cast(_7435.HypoidGearMeshCompoundAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7437
            
            return self._parent._cast(_7437.InterMountableComponentConnectionCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7439
            
            return self._parent._cast(_7439.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7442
            
            return self._parent._cast(_7442.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7445
            
            return self._parent._cast(_7445.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7453
            
            return self._parent._cast(_7453.PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection)

        @property
        def planetary_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7455
            
            return self._parent._cast(_7455.PlanetaryConnectionCompoundAdvancedSystemDeflection)

        @property
        def ring_pins_to_disc_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7462
            
            return self._parent._cast(_7462.RingPinsToDiscConnectionCompoundAdvancedSystemDeflection)

        @property
        def rolling_ring_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7465
            
            return self._parent._cast(_7465.RollingRingConnectionCompoundAdvancedSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7469
            
            return self._parent._cast(_7469.ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7472
            
            return self._parent._cast(_7472.SpiralBevelGearMeshCompoundAdvancedSystemDeflection)

        @property
        def spring_damper_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7475
            
            return self._parent._cast(_7475.SpringDamperConnectionCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7478
            
            return self._parent._cast(_7478.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7481
            
            return self._parent._cast(_7481.StraightBevelGearMeshCompoundAdvancedSystemDeflection)

        @property
        def torque_converter_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7490
            
            return self._parent._cast(_7490.TorqueConverterConnectionCompoundAdvancedSystemDeflection)

        @property
        def worm_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7496
            
            return self._parent._cast(_7496.WormGearMeshCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7499
            
            return self._parent._cast(_7499.ZerolBevelGearMeshCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_advanced_system_deflection(self) -> 'ConnectionCompoundAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_7274.ConnectionAdvancedSystemDeflection]':
        """List[ConnectionAdvancedSystemDeflection]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_7274.ConnectionAdvancedSystemDeflection]':
        """List[ConnectionAdvancedSystemDeflection]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection':
        return self._Cast_ConnectionCompoundAdvancedSystemDeflection(self)
