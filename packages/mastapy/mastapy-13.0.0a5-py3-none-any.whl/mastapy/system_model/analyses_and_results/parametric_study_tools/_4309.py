"""_4309.py

ConnectionParametricStudyTool
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7504
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'ConnectionParametricStudyTool')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2255
    from mastapy.utility_gui import _1838
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4366


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionParametricStudyTool',)


class ConnectionParametricStudyTool(_7504.ConnectionAnalysisCase):
    """ConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONNECTION_PARAMETRIC_STUDY_TOOL

    class _Cast_ConnectionParametricStudyTool:
        """Special nested class for casting ConnectionParametricStudyTool to subclasses."""

        def __init__(self, parent: 'ConnectionParametricStudyTool'):
            self._parent = parent

        @property
        def connection_analysis_case(self):
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
        def abstract_shaft_to_mountable_component_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4277
            
            return self._parent._cast(_4277.AbstractShaftToMountableComponentConnectionParametricStudyTool)

        @property
        def agma_gleason_conical_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4278
            
            return self._parent._cast(_4278.AGMAGleasonConicalGearMeshParametricStudyTool)

        @property
        def belt_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4283
            
            return self._parent._cast(_4283.BeltConnectionParametricStudyTool)

        @property
        def bevel_differential_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4285
            
            return self._parent._cast(_4285.BevelDifferentialGearMeshParametricStudyTool)

        @property
        def bevel_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4290
            
            return self._parent._cast(_4290.BevelGearMeshParametricStudyTool)

        @property
        def clutch_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4295
            
            return self._parent._cast(_4295.ClutchConnectionParametricStudyTool)

        @property
        def coaxial_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4298
            
            return self._parent._cast(_4298.CoaxialConnectionParametricStudyTool)

        @property
        def concept_coupling_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4300
            
            return self._parent._cast(_4300.ConceptCouplingConnectionParametricStudyTool)

        @property
        def concept_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4303
            
            return self._parent._cast(_4303.ConceptGearMeshParametricStudyTool)

        @property
        def conical_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4306
            
            return self._parent._cast(_4306.ConicalGearMeshParametricStudyTool)

        @property
        def coupling_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4311
            
            return self._parent._cast(_4311.CouplingConnectionParametricStudyTool)

        @property
        def cvt_belt_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4314
            
            return self._parent._cast(_4314.CVTBeltConnectionParametricStudyTool)

        @property
        def cycloidal_disc_central_bearing_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4318
            
            return self._parent._cast(_4318.CycloidalDiscCentralBearingConnectionParametricStudyTool)

        @property
        def cycloidal_disc_planetary_bearing_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4320
            
            return self._parent._cast(_4320.CycloidalDiscPlanetaryBearingConnectionParametricStudyTool)

        @property
        def cylindrical_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4321
            
            return self._parent._cast(_4321.CylindricalGearMeshParametricStudyTool)

        @property
        def face_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4334
            
            return self._parent._cast(_4334.FaceGearMeshParametricStudyTool)

        @property
        def gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4339
            
            return self._parent._cast(_4339.GearMeshParametricStudyTool)

        @property
        def hypoid_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4343
            
            return self._parent._cast(_4343.HypoidGearMeshParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4346
            
            return self._parent._cast(_4346.InterMountableComponentConnectionParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4347
            
            return self._parent._cast(_4347.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4350
            
            return self._parent._cast(_4350.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4353
            
            return self._parent._cast(_4353.KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool)

        @property
        def part_to_part_shear_coupling_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4372
            
            return self._parent._cast(_4372.PartToPartShearCouplingConnectionParametricStudyTool)

        @property
        def planetary_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4375
            
            return self._parent._cast(_4375.PlanetaryConnectionParametricStudyTool)

        @property
        def ring_pins_to_disc_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4382
            
            return self._parent._cast(_4382.RingPinsToDiscConnectionParametricStudyTool)

        @property
        def rolling_ring_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4384
            
            return self._parent._cast(_4384.RollingRingConnectionParametricStudyTool)

        @property
        def shaft_to_mountable_component_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4389
            
            return self._parent._cast(_4389.ShaftToMountableComponentConnectionParametricStudyTool)

        @property
        def spiral_bevel_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4391
            
            return self._parent._cast(_4391.SpiralBevelGearMeshParametricStudyTool)

        @property
        def spring_damper_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4394
            
            return self._parent._cast(_4394.SpringDamperConnectionParametricStudyTool)

        @property
        def straight_bevel_diff_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4397
            
            return self._parent._cast(_4397.StraightBevelDiffGearMeshParametricStudyTool)

        @property
        def straight_bevel_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4400
            
            return self._parent._cast(_4400.StraightBevelGearMeshParametricStudyTool)

        @property
        def torque_converter_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4409
            
            return self._parent._cast(_4409.TorqueConverterConnectionParametricStudyTool)

        @property
        def worm_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4415
            
            return self._parent._cast(_4415.WormGearMeshParametricStudyTool)

        @property
        def zerol_bevel_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4418
            
            return self._parent._cast(_4418.ZerolBevelGearMeshParametricStudyTool)

        @property
        def connection_parametric_study_tool(self) -> 'ConnectionParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2255.Connection':
        """Connection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2255.Connection':
        """Connection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def parametric_study_tool(self) -> '_4366.ParametricStudyTool':
        """ParametricStudyTool: 'ParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParametricStudyTool

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConnectionParametricStudyTool._Cast_ConnectionParametricStudyTool':
        return self._Cast_ConnectionParametricStudyTool(self)
