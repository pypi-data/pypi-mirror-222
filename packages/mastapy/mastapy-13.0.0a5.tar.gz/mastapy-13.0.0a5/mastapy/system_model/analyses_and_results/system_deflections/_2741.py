"""_2741.py

GearMeshSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy.system_model.analyses_and_results.system_deflections import _2749
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'GearMeshSystemDeflection')

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _69
    from mastapy.system_model.connections_and_sockets.gears import _2296
    from mastapy.system_model.analyses_and_results.system_deflections import _2743, _2763
    from mastapy.math_utility.measured_vectors import _1555
    from mastapy.gears.rating import _358
    from mastapy.system_model.analyses_and_results.power_flows import _4071


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshSystemDeflection',)


class GearMeshSystemDeflection(_2749.InterMountableComponentConnectionSystemDeflection):
    """GearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_SYSTEM_DEFLECTION

    class _Cast_GearMeshSystemDeflection:
        """Special nested class for casting GearMeshSystemDeflection to subclasses."""

        def __init__(self, parent: 'GearMeshSystemDeflection'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_system_deflection(self):
            return self._parent._cast(_2749.InterMountableComponentConnectionSystemDeflection)

        @property
        def connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2709
            
            return self._parent._cast(_2709.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7506
            
            return self._parent._cast(_7506.ConnectionFEAnalysis)

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
        def agma_gleason_conical_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2671
            
            return self._parent._cast(_2671.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def bevel_differential_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2683
            
            return self._parent._cast(_2683.BevelDifferentialGearMeshSystemDeflection)

        @property
        def bevel_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2688
            
            return self._parent._cast(_2688.BevelGearMeshSystemDeflection)

        @property
        def concept_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2702
            
            return self._parent._cast(_2702.ConceptGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2706
            
            return self._parent._cast(_2706.ConicalGearMeshSystemDeflection)

        @property
        def cylindrical_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2721
            
            return self._parent._cast(_2721.CylindricalGearMeshSystemDeflection)

        @property
        def cylindrical_gear_mesh_system_deflection_timestep(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2722
            
            return self._parent._cast(_2722.CylindricalGearMeshSystemDeflectionTimestep)

        @property
        def cylindrical_gear_mesh_system_deflection_with_ltca_results(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2723
            
            return self._parent._cast(_2723.CylindricalGearMeshSystemDeflectionWithLTCAResults)

        @property
        def face_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2736
            
            return self._parent._cast(_2736.FaceGearMeshSystemDeflection)

        @property
        def hypoid_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2745
            
            return self._parent._cast(_2745.HypoidGearMeshSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2750
            
            return self._parent._cast(_2750.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2753
            
            return self._parent._cast(_2753.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2756
            
            return self._parent._cast(_2756.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection)

        @property
        def spiral_bevel_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2789
            
            return self._parent._cast(_2789.SpiralBevelGearMeshSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2795
            
            return self._parent._cast(_2795.StraightBevelDiffGearMeshSystemDeflection)

        @property
        def straight_bevel_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2798
            
            return self._parent._cast(_2798.StraightBevelGearMeshSystemDeflection)

        @property
        def worm_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2818
            
            return self._parent._cast(_2818.WormGearMeshSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2821
            
            return self._parent._cast(_2821.ZerolBevelGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(self) -> 'GearMeshSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def calculated_mesh_stiffness_along_face_width(self) -> 'float':
        """float: 'CalculatedMeshStiffnessAlongFaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedMeshStiffnessAlongFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def flank_sign(self) -> 'float':
        """float: 'FlankSign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlankSign

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_a_torque_left_flank(self) -> 'float':
        """float: 'GearATorqueLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearATorqueLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_a_torque_right_flank(self) -> 'float':
        """float: 'GearATorqueRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearATorqueRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_torque_left_flank(self) -> 'float':
        """float: 'GearBTorqueLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBTorqueLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_torque_right_flank(self) -> 'float':
        """float: 'GearBTorqueRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBTorqueRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_mesh_contact_status(self) -> '_69.GearMeshContactStatus':
        """GearMeshContactStatus: 'GearMeshContactStatus' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshContactStatus

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.NodalAnalysis.GearMeshContactStatus')
        return constructor.new_from_mastapy('mastapy.nodal_analysis._69', 'GearMeshContactStatus')(value) if value is not None else None

    @property
    def is_in_contact(self) -> 'bool':
        """bool: 'IsInContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsInContact

        if temp is None:
            return False

        return temp

    @property
    def load_in_loa_from_stiffness_model(self) -> 'float':
        """float: 'LoadInLOAFromStiffnessModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadInLOAFromStiffnessModel

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_possible_mesh_stiffness_along_face_width(self) -> 'float':
        """float: 'MaximumPossibleMeshStiffnessAlongFaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumPossibleMeshStiffnessAlongFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_power(self) -> 'float':
        """float: 'MeshPower' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshPower

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_power_gear_a_left_flank(self) -> 'float':
        """float: 'MeshPowerGearALeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshPowerGearALeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_power_gear_a_right_flank(self) -> 'float':
        """float: 'MeshPowerGearARightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshPowerGearARightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_power_gear_b_left_flank(self) -> 'float':
        """float: 'MeshPowerGearBLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshPowerGearBLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_power_gear_b_right_flank(self) -> 'float':
        """float: 'MeshPowerGearBRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshPowerGearBRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_separation_left_flank(self) -> 'float':
        """float: 'MinimumSeparationLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumSeparationLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_separation_right_flank(self) -> 'float':
        """float: 'MinimumSeparationRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumSeparationRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def moment_about_centre_from_ltca(self) -> 'float':
        """float: 'MomentAboutCentreFromLTCA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MomentAboutCentreFromLTCA

        if temp is None:
            return 0.0

        return temp

    @property
    def moment_about_centre_from_stiffness_model(self) -> 'float':
        """float: 'MomentAboutCentreFromStiffnessModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MomentAboutCentreFromStiffnessModel

        if temp is None:
            return 0.0

        return temp

    @property
    def node_pair_backlash_on_left_side(self) -> 'List[float]':
        """List[float]: 'NodePairBacklashOnLeftSide' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairBacklashOnLeftSide

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def node_pair_backlash_on_right_side(self) -> 'List[float]':
        """List[float]: 'NodePairBacklashOnRightSide' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairBacklashOnRightSide

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def node_pair_contact_status(self) -> 'List[str]':
        """List[str]: 'NodePairContactStatus' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairContactStatus

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def node_pair_deflections(self) -> 'List[float]':
        """List[float]: 'NodePairDeflections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairDeflections

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def node_pair_load_in_loa(self) -> 'List[float]':
        """List[float]: 'NodePairLoadInLOA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairLoadInLOA

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def node_pair_load_in_loa_left_flank(self) -> 'List[float]':
        """List[float]: 'NodePairLoadInLOALeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairLoadInLOALeftFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def node_pair_load_in_loa_right_flank(self) -> 'List[float]':
        """List[float]: 'NodePairLoadInLOARightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairLoadInLOARightFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def node_pair_mesh_stiffness(self) -> 'List[float]':
        """List[float]: 'NodePairMeshStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairMeshStiffness

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def node_pair_mesh_stiffness_z_theta(self) -> 'List[float]':
        """List[float]: 'NodePairMeshStiffnessZTheta' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairMeshStiffnessZTheta

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def node_pair_mesh_stiffness_theta_z(self) -> 'List[float]':
        """List[float]: 'NodePairMeshStiffnessThetaZ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairMeshStiffnessThetaZ

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def node_pair_mesh_stiffness_theta_theta(self) -> 'List[float]':
        """List[float]: 'NodePairMeshStiffnessThetaTheta' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairMeshStiffnessThetaTheta

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def node_pair_separations(self) -> 'List[float]':
        """List[float]: 'NodePairSeparations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairSeparations

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def node_pair_separations_left_flank(self) -> 'List[float]':
        """List[float]: 'NodePairSeparationsLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairSeparationsLeftFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def node_pair_separations_right_flank(self) -> 'List[float]':
        """List[float]: 'NodePairSeparationsRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairSeparationsRightFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def node_pair_separations_inactive_flank(self) -> 'List[float]':
        """List[float]: 'NodePairSeparationsInactiveFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairSeparationsInactiveFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def number_of_teeth_in_contact(self) -> 'int':
        """int: 'NumberOfTeethInContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfTeethInContact

        if temp is None:
            return 0

        return temp

    @property
    def stiffness_kzz(self) -> 'float':
        """float: 'StiffnessKzz' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessKzz

        if temp is None:
            return 0.0

        return temp

    @property
    def total_contact_length(self) -> 'float':
        """float: 'TotalContactLength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalContactLength

        if temp is None:
            return 0.0

        return temp

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
    def gear_a(self) -> '_2743.GearSystemDeflection':
        """GearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_total_mesh_force_in_wcs(self) -> '_1555.VectorWithLinearAndAngularComponents':
        """VectorWithLinearAndAngularComponents: 'GearATotalMeshForceInWCS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearATotalMeshForceInWCS

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b(self) -> '_2743.GearSystemDeflection':
        """GearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_total_mesh_force_in_wcs(self) -> '_1555.VectorWithLinearAndAngularComponents':
        """VectorWithLinearAndAngularComponents: 'GearBTotalMeshForceInWCS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBTotalMeshForceInWCS

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mean_contact_point_in_world_coordinate_system(self) -> 'Vector3D':
        """Vector3D: 'MeanContactPointInWorldCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanContactPointInWorldCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def rating(self) -> '_358.GearMeshRating':
        """GearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_separations(self) -> 'List[_2763.MeshSeparationsAtFaceWidth]':
        """List[MeshSeparationsAtFaceWidth]: 'MeshSeparations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshSeparations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def power_flow_results(self) -> '_4071.GearMeshPowerFlow':
        """GearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearMeshSystemDeflection._Cast_GearMeshSystemDeflection':
        return self._Cast_GearMeshSystemDeflection(self)
