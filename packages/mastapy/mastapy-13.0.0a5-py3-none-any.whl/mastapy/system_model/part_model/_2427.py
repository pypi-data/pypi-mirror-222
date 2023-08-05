"""_2427.py

Component
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._math.vector_3d import Vector3D
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.part_model import _2451
from mastapy._internal.cast_exception import CastException

_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Component')
_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'Socket')

if TYPE_CHECKING:
    from mastapy.math_utility import _1489, _1490
    from mastapy.system_model.connections_and_sockets import (
        _2253, _2255, _2279, _2274
    )
    from mastapy.system_model.part_model import _2428


__docformat__ = 'restructuredtext en'
__all__ = ('Component',)


class Component(_2451.Part):
    """Component

    This is a mastapy class.
    """

    TYPE = _COMPONENT

    class _Cast_Component:
        """Special nested class for casting Component to subclasses."""

        def __init__(self, parent: 'Component'):
            self._parent = parent

        @property
        def part(self):
            return self._parent._cast(_2451.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2190
            
            return self._parent._cast(_2190.DesignEntity)

        @property
        def abstract_shaft(self):
            from mastapy.system_model.part_model import _2418
            
            return self._parent._cast(_2418.AbstractShaft)

        @property
        def abstract_shaft_or_housing(self):
            from mastapy.system_model.part_model import _2419
            
            return self._parent._cast(_2419.AbstractShaftOrHousing)

        @property
        def bearing(self):
            from mastapy.system_model.part_model import _2422
            
            return self._parent._cast(_2422.Bearing)

        @property
        def bolt(self):
            from mastapy.system_model.part_model import _2425
            
            return self._parent._cast(_2425.Bolt)

        @property
        def connector(self):
            from mastapy.system_model.part_model import _2430
            
            return self._parent._cast(_2430.Connector)

        @property
        def datum(self):
            from mastapy.system_model.part_model import _2431
            
            return self._parent._cast(_2431.Datum)

        @property
        def external_cad_model(self):
            from mastapy.system_model.part_model import _2435
            
            return self._parent._cast(_2435.ExternalCADModel)

        @property
        def fe_part(self):
            from mastapy.system_model.part_model import _2436
            
            return self._parent._cast(_2436.FEPart)

        @property
        def guide_dxf_model(self):
            from mastapy.system_model.part_model import _2438
            
            return self._parent._cast(_2438.GuideDxfModel)

        @property
        def mass_disc(self):
            from mastapy.system_model.part_model import _2445
            
            return self._parent._cast(_2445.MassDisc)

        @property
        def measurement_component(self):
            from mastapy.system_model.part_model import _2446
            
            return self._parent._cast(_2446.MeasurementComponent)

        @property
        def mountable_component(self):
            from mastapy.system_model.part_model import _2447
            
            return self._parent._cast(_2447.MountableComponent)

        @property
        def oil_seal(self):
            from mastapy.system_model.part_model import _2449
            
            return self._parent._cast(_2449.OilSeal)

        @property
        def planet_carrier(self):
            from mastapy.system_model.part_model import _2452
            
            return self._parent._cast(_2452.PlanetCarrier)

        @property
        def point_load(self):
            from mastapy.system_model.part_model import _2454
            
            return self._parent._cast(_2454.PointLoad)

        @property
        def power_load(self):
            from mastapy.system_model.part_model import _2455
            
            return self._parent._cast(_2455.PowerLoad)

        @property
        def unbalanced_mass(self):
            from mastapy.system_model.part_model import _2460
            
            return self._parent._cast(_2460.UnbalancedMass)

        @property
        def virtual_component(self):
            from mastapy.system_model.part_model import _2462
            
            return self._parent._cast(_2462.VirtualComponent)

        @property
        def shaft(self):
            from mastapy.system_model.part_model.shaft_model import _2465
            
            return self._parent._cast(_2465.Shaft)

        @property
        def agma_gleason_conical_gear(self):
            from mastapy.system_model.part_model.gears import _2495
            
            return self._parent._cast(_2495.AGMAGleasonConicalGear)

        @property
        def bevel_differential_gear(self):
            from mastapy.system_model.part_model.gears import _2497
            
            return self._parent._cast(_2497.BevelDifferentialGear)

        @property
        def bevel_differential_planet_gear(self):
            from mastapy.system_model.part_model.gears import _2499
            
            return self._parent._cast(_2499.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(self):
            from mastapy.system_model.part_model.gears import _2500
            
            return self._parent._cast(_2500.BevelDifferentialSunGear)

        @property
        def bevel_gear(self):
            from mastapy.system_model.part_model.gears import _2501
            
            return self._parent._cast(_2501.BevelGear)

        @property
        def concept_gear(self):
            from mastapy.system_model.part_model.gears import _2503
            
            return self._parent._cast(_2503.ConceptGear)

        @property
        def conical_gear(self):
            from mastapy.system_model.part_model.gears import _2505
            
            return self._parent._cast(_2505.ConicalGear)

        @property
        def cylindrical_gear(self):
            from mastapy.system_model.part_model.gears import _2507
            
            return self._parent._cast(_2507.CylindricalGear)

        @property
        def cylindrical_planet_gear(self):
            from mastapy.system_model.part_model.gears import _2509
            
            return self._parent._cast(_2509.CylindricalPlanetGear)

        @property
        def face_gear(self):
            from mastapy.system_model.part_model.gears import _2510
            
            return self._parent._cast(_2510.FaceGear)

        @property
        def gear(self):
            from mastapy.system_model.part_model.gears import _2512
            
            return self._parent._cast(_2512.Gear)

        @property
        def hypoid_gear(self):
            from mastapy.system_model.part_model.gears import _2516
            
            return self._parent._cast(_2516.HypoidGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(self):
            from mastapy.system_model.part_model.gears import _2518
            
            return self._parent._cast(_2518.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(self):
            from mastapy.system_model.part_model.gears import _2520
            
            return self._parent._cast(_2520.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(self):
            from mastapy.system_model.part_model.gears import _2522
            
            return self._parent._cast(_2522.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def spiral_bevel_gear(self):
            from mastapy.system_model.part_model.gears import _2525
            
            return self._parent._cast(_2525.SpiralBevelGear)

        @property
        def straight_bevel_diff_gear(self):
            from mastapy.system_model.part_model.gears import _2527
            
            return self._parent._cast(_2527.StraightBevelDiffGear)

        @property
        def straight_bevel_gear(self):
            from mastapy.system_model.part_model.gears import _2529
            
            return self._parent._cast(_2529.StraightBevelGear)

        @property
        def straight_bevel_planet_gear(self):
            from mastapy.system_model.part_model.gears import _2531
            
            return self._parent._cast(_2531.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(self):
            from mastapy.system_model.part_model.gears import _2532
            
            return self._parent._cast(_2532.StraightBevelSunGear)

        @property
        def worm_gear(self):
            from mastapy.system_model.part_model.gears import _2533
            
            return self._parent._cast(_2533.WormGear)

        @property
        def zerol_bevel_gear(self):
            from mastapy.system_model.part_model.gears import _2535
            
            return self._parent._cast(_2535.ZerolBevelGear)

        @property
        def cycloidal_disc(self):
            from mastapy.system_model.part_model.cycloidal import _2551
            
            return self._parent._cast(_2551.CycloidalDisc)

        @property
        def ring_pins(self):
            from mastapy.system_model.part_model.cycloidal import _2552
            
            return self._parent._cast(_2552.RingPins)

        @property
        def clutch_half(self):
            from mastapy.system_model.part_model.couplings import _2561
            
            return self._parent._cast(_2561.ClutchHalf)

        @property
        def concept_coupling_half(self):
            from mastapy.system_model.part_model.couplings import _2564
            
            return self._parent._cast(_2564.ConceptCouplingHalf)

        @property
        def coupling_half(self):
            from mastapy.system_model.part_model.couplings import _2566
            
            return self._parent._cast(_2566.CouplingHalf)

        @property
        def cvt_pulley(self):
            from mastapy.system_model.part_model.couplings import _2569
            
            return self._parent._cast(_2569.CVTPulley)

        @property
        def part_to_part_shear_coupling_half(self):
            from mastapy.system_model.part_model.couplings import _2571
            
            return self._parent._cast(_2571.PartToPartShearCouplingHalf)

        @property
        def pulley(self):
            from mastapy.system_model.part_model.couplings import _2572
            
            return self._parent._cast(_2572.Pulley)

        @property
        def rolling_ring(self):
            from mastapy.system_model.part_model.couplings import _2578
            
            return self._parent._cast(_2578.RollingRing)

        @property
        def shaft_hub_connection(self):
            from mastapy.system_model.part_model.couplings import _2580
            
            return self._parent._cast(_2580.ShaftHubConnection)

        @property
        def spring_damper_half(self):
            from mastapy.system_model.part_model.couplings import _2583
            
            return self._parent._cast(_2583.SpringDamperHalf)

        @property
        def synchroniser_half(self):
            from mastapy.system_model.part_model.couplings import _2586
            
            return self._parent._cast(_2586.SynchroniserHalf)

        @property
        def synchroniser_part(self):
            from mastapy.system_model.part_model.couplings import _2587
            
            return self._parent._cast(_2587.SynchroniserPart)

        @property
        def synchroniser_sleeve(self):
            from mastapy.system_model.part_model.couplings import _2588
            
            return self._parent._cast(_2588.SynchroniserSleeve)

        @property
        def torque_converter_pump(self):
            from mastapy.system_model.part_model.couplings import _2590
            
            return self._parent._cast(_2590.TorqueConverterPump)

        @property
        def torque_converter_turbine(self):
            from mastapy.system_model.part_model.couplings import _2592
            
            return self._parent._cast(_2592.TorqueConverterTurbine)

        @property
        def component(self) -> 'Component':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Component.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing_full_model(self) -> 'Image':
        """Image: 'TwoDDrawingFullModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TwoDDrawingFullModel

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def additional_modal_damping_ratio(self) -> 'float':
        """float: 'AdditionalModalDampingRatio' is the original name of this property."""

        temp = self.wrapped.AdditionalModalDampingRatio

        if temp is None:
            return 0.0

        return temp

    @additional_modal_damping_ratio.setter
    def additional_modal_damping_ratio(self, value: 'float'):
        self.wrapped.AdditionalModalDampingRatio = float(value) if value is not None else 0.0

    @property
    def length(self) -> 'float':
        """float: 'Length' is the original name of this property."""

        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    def length(self, value: 'float'):
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def polar_inertia(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'PolarInertia' is the original name of this property."""

        temp = self.wrapped.PolarInertia

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @polar_inertia.setter
    def polar_inertia(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.PolarInertia = value

    @property
    def polar_inertia_for_synchroniser_sizing_only(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'PolarInertiaForSynchroniserSizingOnly' is the original name of this property."""

        temp = self.wrapped.PolarInertiaForSynchroniserSizingOnly

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @polar_inertia_for_synchroniser_sizing_only.setter
    def polar_inertia_for_synchroniser_sizing_only(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.PolarInertiaForSynchroniserSizingOnly = value

    @property
    def reason_mass_properties_are_unknown(self) -> 'str':
        """str: 'ReasonMassPropertiesAreUnknown' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReasonMassPropertiesAreUnknown

        if temp is None:
            return ''

        return temp

    @property
    def reason_mass_properties_are_zero(self) -> 'str':
        """str: 'ReasonMassPropertiesAreZero' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReasonMassPropertiesAreZero

        if temp is None:
            return ''

        return temp

    @property
    def translation(self) -> 'str':
        """str: 'Translation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Translation

        if temp is None:
            return ''

        return temp

    @property
    def transverse_inertia(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'TransverseInertia' is the original name of this property."""

        temp = self.wrapped.TransverseInertia

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @transverse_inertia.setter
    def transverse_inertia(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.TransverseInertia = value

    @property
    def x_axis(self) -> 'str':
        """str: 'XAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.XAxis

        if temp is None:
            return ''

        return temp

    @property
    def y_axis(self) -> 'str':
        """str: 'YAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.YAxis

        if temp is None:
            return ''

        return temp

    @property
    def z_axis(self) -> 'str':
        """str: 'ZAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZAxis

        if temp is None:
            return ''

        return temp

    @property
    def coordinate_system_euler_angles(self) -> 'Vector3D':
        """Vector3D: 'CoordinateSystemEulerAngles' is the original name of this property."""

        temp = self.wrapped.CoordinateSystemEulerAngles

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @coordinate_system_euler_angles.setter
    def coordinate_system_euler_angles(self, value: 'Vector3D'):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.CoordinateSystemEulerAngles = value

    @property
    def local_coordinate_system(self) -> '_1489.CoordinateSystem3D':
        """CoordinateSystem3D: 'LocalCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LocalCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def position(self) -> 'Vector3D':
        """Vector3D: 'Position' is the original name of this property."""

        temp = self.wrapped.Position

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @position.setter
    def position(self, value: 'Vector3D'):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.Position = value

    @property
    def component_connections(self) -> 'List[_2253.ComponentConnection]':
        """List[ComponentConnection]: 'ComponentConnections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def available_socket_offsets(self) -> 'List[str]':
        """List[str]: 'AvailableSocketOffsets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AvailableSocketOffsets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    @property
    def centre_offset(self) -> 'float':
        """float: 'CentreOffset' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CentreOffset

        if temp is None:
            return 0.0

        return temp

    @property
    def translation_vector(self) -> 'Vector3D':
        """Vector3D: 'TranslationVector' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TranslationVector

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def x_axis_vector(self) -> 'Vector3D':
        """Vector3D: 'XAxisVector' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.XAxisVector

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def y_axis_vector(self) -> 'Vector3D':
        """Vector3D: 'YAxisVector' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.YAxisVector

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def z_axis_vector(self) -> 'Vector3D':
        """Vector3D: 'ZAxisVector' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZAxisVector

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    def can_connect_to(self, component: 'Component') -> 'bool':
        """ 'CanConnectTo' is the original name of this method.

        Args:
            component (mastapy.system_model.part_model.Component)

        Returns:
            bool
        """

        method_result = self.wrapped.CanConnectTo(component.wrapped if component else None)
        return method_result

    def can_delete_connection(self, connection: '_2255.Connection') -> 'bool':
        """ 'CanDeleteConnection' is the original name of this method.

        Args:
            connection (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            bool
        """

        method_result = self.wrapped.CanDeleteConnection(connection.wrapped if connection else None)
        return method_result

    def connect_to(self, component: 'Component') -> '_2428.ComponentsConnectedResult':
        """ 'ConnectTo' is the original name of this method.

        Args:
            component (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.part_model.ComponentsConnectedResult
        """

        method_result = self.wrapped.ConnectTo.Overloads[_COMPONENT](component.wrapped if component else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def connect_to_socket(self, socket: '_2279.Socket') -> '_2428.ComponentsConnectedResult':
        """ 'ConnectTo' is the original name of this method.

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)

        Returns:
            mastapy.system_model.part_model.ComponentsConnectedResult
        """

        method_result = self.wrapped.ConnectTo.Overloads[_SOCKET](socket.wrapped if socket else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def create_coordinate_system_editor(self) -> '_1490.CoordinateSystemEditor':
        """ 'CreateCoordinateSystemEditor' is the original name of this method.

        Returns:
            mastapy.math_utility.CoordinateSystemEditor
        """

        method_result = self.wrapped.CreateCoordinateSystemEditor()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def diameter_at_middle_of_connection(self, connection: '_2255.Connection') -> 'float':
        """ 'DiameterAtMiddleOfConnection' is the original name of this method.

        Args:
            connection (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            float
        """

        method_result = self.wrapped.DiameterAtMiddleOfConnection(connection.wrapped if connection else None)
        return method_result

    def diameter_of_socket_for(self, connection: '_2255.Connection') -> 'float':
        """ 'DiameterOfSocketFor' is the original name of this method.

        Args:
            connection (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            float
        """

        method_result = self.wrapped.DiameterOfSocketFor(connection.wrapped if connection else None)
        return method_result

    def is_coaxially_connected_to(self, component: 'Component') -> 'bool':
        """ 'IsCoaxiallyConnectedTo' is the original name of this method.

        Args:
            component (mastapy.system_model.part_model.Component)

        Returns:
            bool
        """

        method_result = self.wrapped.IsCoaxiallyConnectedTo(component.wrapped if component else None)
        return method_result

    def is_directly_connected_to(self, component: 'Component') -> 'bool':
        """ 'IsDirectlyConnectedTo' is the original name of this method.

        Args:
            component (mastapy.system_model.part_model.Component)

        Returns:
            bool
        """

        method_result = self.wrapped.IsDirectlyConnectedTo(component.wrapped if component else None)
        return method_result

    def is_directly_or_indirectly_connected_to(self, component: 'Component') -> 'bool':
        """ 'IsDirectlyOrIndirectlyConnectedTo' is the original name of this method.

        Args:
            component (mastapy.system_model.part_model.Component)

        Returns:
            bool
        """

        method_result = self.wrapped.IsDirectlyOrIndirectlyConnectedTo(component.wrapped if component else None)
        return method_result

    def move_all_concentric_parts_radially(self, delta_x: 'float', delta_y: 'float') -> 'bool':
        """ 'MoveAllConcentricPartsRadially' is the original name of this method.

        Args:
            delta_x (float)
            delta_y (float)

        Returns:
            bool
        """

        delta_x = float(delta_x)
        delta_y = float(delta_y)
        method_result = self.wrapped.MoveAllConcentricPartsRadially(delta_x if delta_x else 0.0, delta_y if delta_y else 0.0)
        return method_result

    def move_along_axis(self, delta: 'float'):
        """ 'MoveAlongAxis' is the original name of this method.

        Args:
            delta (float)
        """

        delta = float(delta)
        self.wrapped.MoveAlongAxis(delta if delta else 0.0)

    def move_with_concentric_parts_to_new_origin(self, target_origin: 'Vector3D') -> 'bool':
        """ 'MoveWithConcentricPartsToNewOrigin' is the original name of this method.

        Args:
            target_origin (Vector3D)

        Returns:
            bool
        """

        target_origin = conversion.mp_to_pn_vector3d(target_origin)
        method_result = self.wrapped.MoveWithConcentricPartsToNewOrigin(target_origin)
        return method_result

    def possible_sockets_to_connect_with_component(self, component: 'Component') -> 'List[_2279.Socket]':
        """ 'PossibleSocketsToConnectWith' is the original name of this method.

        Args:
            component (mastapy.system_model.part_model.Component)

        Returns:
            List[mastapy.system_model.connections_and_sockets.Socket]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.PossibleSocketsToConnectWith.Overloads[_COMPONENT](component.wrapped if component else None))

    def possible_sockets_to_connect_with(self, socket: '_2279.Socket') -> 'List[_2279.Socket]':
        """ 'PossibleSocketsToConnectWith' is the original name of this method.

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)

        Returns:
            List[mastapy.system_model.connections_and_sockets.Socket]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.PossibleSocketsToConnectWith.Overloads[_SOCKET](socket.wrapped if socket else None))

    def set_position_and_axis_of_component_and_connected_components(self, origin: 'Vector3D', z_axis: 'Vector3D') -> '_2274.RealignmentResult':
        """ 'SetPositionAndAxisOfComponentAndConnectedComponents' is the original name of this method.

        Args:
            origin (Vector3D)
            z_axis (Vector3D)

        Returns:
            mastapy.system_model.connections_and_sockets.RealignmentResult
        """

        origin = conversion.mp_to_pn_vector3d(origin)
        z_axis = conversion.mp_to_pn_vector3d(z_axis)
        method_result = self.wrapped.SetPositionAndAxisOfComponentAndConnectedComponents(origin, z_axis)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def set_position_and_rotation_of_component_and_connected_components(self, new_coordinate_system: '_1489.CoordinateSystem3D') -> '_2274.RealignmentResult':
        """ 'SetPositionAndRotationOfComponentAndConnectedComponents' is the original name of this method.

        Args:
            new_coordinate_system (mastapy.math_utility.CoordinateSystem3D)

        Returns:
            mastapy.system_model.connections_and_sockets.RealignmentResult
        """

        method_result = self.wrapped.SetPositionAndRotationOfComponentAndConnectedComponents(new_coordinate_system.wrapped if new_coordinate_system else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def set_position_of_component_and_connected_components(self, position: 'Vector3D') -> '_2274.RealignmentResult':
        """ 'SetPositionOfComponentAndConnectedComponents' is the original name of this method.

        Args:
            position (Vector3D)

        Returns:
            mastapy.system_model.connections_and_sockets.RealignmentResult
        """

        position = conversion.mp_to_pn_vector3d(position)
        method_result = self.wrapped.SetPositionOfComponentAndConnectedComponents(position)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def socket_named(self, socket_name: 'str') -> '_2279.Socket':
        """ 'SocketNamed' is the original name of this method.

        Args:
            socket_name (str)

        Returns:
            mastapy.system_model.connections_and_sockets.Socket
        """

        socket_name = str(socket_name)
        method_result = self.wrapped.SocketNamed(socket_name if socket_name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def try_connect_to(self, component: 'Component', hint_offset: Optional['float'] = float('nan')) -> '_2428.ComponentsConnectedResult':
        """ 'TryConnectTo' is the original name of this method.

        Args:
            component (mastapy.system_model.part_model.Component)
            hint_offset (float, optional)

        Returns:
            mastapy.system_model.part_model.ComponentsConnectedResult
        """

        hint_offset = float(hint_offset)
        method_result = self.wrapped.TryConnectTo(component.wrapped if component else None, hint_offset if hint_offset else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'Component._Cast_Component':
        return self._Cast_Component(self)
