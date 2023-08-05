"""_4456.py

ConnectionCompoundParametricStudyTool
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7505
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'ConnectionCompoundParametricStudyTool')

if TYPE_CHECKING:
    from mastapy.utility_gui import _1838
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4309


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionCompoundParametricStudyTool',)


class ConnectionCompoundParametricStudyTool(_7505.ConnectionCompoundAnalysis):
    """ConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_ConnectionCompoundParametricStudyTool:
        """Special nested class for casting ConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'ConnectionCompoundParametricStudyTool'):
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
        def abstract_shaft_to_mountable_component_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4424
            
            return self._parent._cast(_4424.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool)

        @property
        def agma_gleason_conical_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4426
            
            return self._parent._cast(_4426.AGMAGleasonConicalGearMeshCompoundParametricStudyTool)

        @property
        def belt_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4430
            
            return self._parent._cast(_4430.BeltConnectionCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4433
            
            return self._parent._cast(_4433.BevelDifferentialGearMeshCompoundParametricStudyTool)

        @property
        def bevel_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4438
            
            return self._parent._cast(_4438.BevelGearMeshCompoundParametricStudyTool)

        @property
        def clutch_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4443
            
            return self._parent._cast(_4443.ClutchConnectionCompoundParametricStudyTool)

        @property
        def coaxial_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4445
            
            return self._parent._cast(_4445.CoaxialConnectionCompoundParametricStudyTool)

        @property
        def concept_coupling_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4448
            
            return self._parent._cast(_4448.ConceptCouplingConnectionCompoundParametricStudyTool)

        @property
        def concept_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4451
            
            return self._parent._cast(_4451.ConceptGearMeshCompoundParametricStudyTool)

        @property
        def conical_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4454
            
            return self._parent._cast(_4454.ConicalGearMeshCompoundParametricStudyTool)

        @property
        def coupling_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4459
            
            return self._parent._cast(_4459.CouplingConnectionCompoundParametricStudyTool)

        @property
        def cvt_belt_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4461
            
            return self._parent._cast(_4461.CVTBeltConnectionCompoundParametricStudyTool)

        @property
        def cycloidal_disc_central_bearing_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4465
            
            return self._parent._cast(_4465.CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4467
            
            return self._parent._cast(_4467.CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool)

        @property
        def cylindrical_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4469
            
            return self._parent._cast(_4469.CylindricalGearMeshCompoundParametricStudyTool)

        @property
        def face_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4475
            
            return self._parent._cast(_4475.FaceGearMeshCompoundParametricStudyTool)

        @property
        def gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4480
            
            return self._parent._cast(_4480.GearMeshCompoundParametricStudyTool)

        @property
        def hypoid_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4484
            
            return self._parent._cast(_4484.HypoidGearMeshCompoundParametricStudyTool)

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4486
            
            return self._parent._cast(_4486.InterMountableComponentConnectionCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4488
            
            return self._parent._cast(_4488.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4491
            
            return self._parent._cast(_4491.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4494
            
            return self._parent._cast(_4494.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool)

        @property
        def part_to_part_shear_coupling_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4502
            
            return self._parent._cast(_4502.PartToPartShearCouplingConnectionCompoundParametricStudyTool)

        @property
        def planetary_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4504
            
            return self._parent._cast(_4504.PlanetaryConnectionCompoundParametricStudyTool)

        @property
        def ring_pins_to_disc_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4511
            
            return self._parent._cast(_4511.RingPinsToDiscConnectionCompoundParametricStudyTool)

        @property
        def rolling_ring_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4514
            
            return self._parent._cast(_4514.RollingRingConnectionCompoundParametricStudyTool)

        @property
        def shaft_to_mountable_component_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4518
            
            return self._parent._cast(_4518.ShaftToMountableComponentConnectionCompoundParametricStudyTool)

        @property
        def spiral_bevel_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4521
            
            return self._parent._cast(_4521.SpiralBevelGearMeshCompoundParametricStudyTool)

        @property
        def spring_damper_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4524
            
            return self._parent._cast(_4524.SpringDamperConnectionCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4527
            
            return self._parent._cast(_4527.StraightBevelDiffGearMeshCompoundParametricStudyTool)

        @property
        def straight_bevel_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4530
            
            return self._parent._cast(_4530.StraightBevelGearMeshCompoundParametricStudyTool)

        @property
        def torque_converter_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4539
            
            return self._parent._cast(_4539.TorqueConverterConnectionCompoundParametricStudyTool)

        @property
        def worm_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4545
            
            return self._parent._cast(_4545.WormGearMeshCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4548
            
            return self._parent._cast(_4548.ZerolBevelGearMeshCompoundParametricStudyTool)

        @property
        def connection_compound_parametric_study_tool(self) -> 'ConnectionCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def data_logger(self) -> '_1838.DataLoggerWithCharts':
        """DataLoggerWithCharts: 'DataLogger' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DataLogger

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases(self) -> 'List[_4309.ConnectionParametricStudyTool]':
        """List[ConnectionParametricStudyTool]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4309.ConnectionParametricStudyTool]':
        """List[ConnectionParametricStudyTool]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool':
        return self._Cast_ConnectionCompoundParametricStudyTool(self)
