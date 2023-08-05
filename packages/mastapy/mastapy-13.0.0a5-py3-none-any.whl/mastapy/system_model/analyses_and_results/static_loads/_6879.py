"""_6879.py

InterMountableComponentConnectionLoadCase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6817
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'InterMountableComponentConnectionLoadCase')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2264


__docformat__ = 'restructuredtext en'
__all__ = ('InterMountableComponentConnectionLoadCase',)


class InterMountableComponentConnectionLoadCase(_6817.ConnectionLoadCase):
    """InterMountableComponentConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE

    class _Cast_InterMountableComponentConnectionLoadCase:
        """Special nested class for casting InterMountableComponentConnectionLoadCase to subclasses."""

        def __init__(self, parent: 'InterMountableComponentConnectionLoadCase'):
            self._parent = parent

        @property
        def connection_load_case(self):
            return self._parent._cast(_6817.ConnectionLoadCase)

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
        def agma_gleason_conical_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6782
            
            return self._parent._cast(_6782.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def belt_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6788
            
            return self._parent._cast(_6788.BeltConnectionLoadCase)

        @property
        def bevel_differential_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6791
            
            return self._parent._cast(_6791.BevelDifferentialGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6796
            
            return self._parent._cast(_6796.BevelGearMeshLoadCase)

        @property
        def clutch_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6800
            
            return self._parent._cast(_6800.ClutchConnectionLoadCase)

        @property
        def concept_coupling_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6806
            
            return self._parent._cast(_6806.ConceptCouplingConnectionLoadCase)

        @property
        def concept_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6810
            
            return self._parent._cast(_6810.ConceptGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6814
            
            return self._parent._cast(_6814.ConicalGearMeshLoadCase)

        @property
        def coupling_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6819
            
            return self._parent._cast(_6819.CouplingConnectionLoadCase)

        @property
        def cvt_belt_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6822
            
            return self._parent._cast(_6822.CVTBeltConnectionLoadCase)

        @property
        def cylindrical_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6831
            
            return self._parent._cast(_6831.CylindricalGearMeshLoadCase)

        @property
        def face_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6853
            
            return self._parent._cast(_6853.FaceGearMeshLoadCase)

        @property
        def gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6860
            
            return self._parent._cast(_6860.GearMeshLoadCase)

        @property
        def hypoid_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6874
            
            return self._parent._cast(_6874.HypoidGearMeshLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6881
            
            return self._parent._cast(_6881.KlingelnbergCycloPalloidConicalGearMeshLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6884
            
            return self._parent._cast(_6884.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6887
            
            return self._parent._cast(_6887.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)

        @property
        def part_to_part_shear_coupling_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6897
            
            return self._parent._cast(_6897.PartToPartShearCouplingConnectionLoadCase)

        @property
        def ring_pins_to_disc_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6912
            
            return self._parent._cast(_6912.RingPinsToDiscConnectionLoadCase)

        @property
        def rolling_ring_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6914
            
            return self._parent._cast(_6914.RollingRingConnectionLoadCase)

        @property
        def spiral_bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6922
            
            return self._parent._cast(_6922.SpiralBevelGearMeshLoadCase)

        @property
        def spring_damper_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6924
            
            return self._parent._cast(_6924.SpringDamperConnectionLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6928
            
            return self._parent._cast(_6928.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6931
            
            return self._parent._cast(_6931.StraightBevelGearMeshLoadCase)

        @property
        def torque_converter_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6940
            
            return self._parent._cast(_6940.TorqueConverterConnectionLoadCase)

        @property
        def worm_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6951
            
            return self._parent._cast(_6951.WormGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6954
            
            return self._parent._cast(_6954.ZerolBevelGearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(self) -> 'InterMountableComponentConnectionLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InterMountableComponentConnectionLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_modal_damping_ratio(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'AdditionalModalDampingRatio' is the original name of this property."""

        temp = self.wrapped.AdditionalModalDampingRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @additional_modal_damping_ratio.setter
    def additional_modal_damping_ratio(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AdditionalModalDampingRatio = value

    @property
    def connection_design(self) -> '_2264.InterMountableComponentConnection':
        """InterMountableComponentConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase':
        return self._Cast_InterMountableComponentConnectionLoadCase(self)
