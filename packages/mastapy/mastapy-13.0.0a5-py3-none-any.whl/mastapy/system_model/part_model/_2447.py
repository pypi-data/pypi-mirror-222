"""_2447.py

MountableComponent
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from mastapy._internal import constructor
from mastapy.system_model.part_model import _2427
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'MountableComponent')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2418, _2428
    from mastapy.system_model.connections_and_sockets import _2255, _2259, _2252


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponent',)


class MountableComponent(_2427.Component):
    """MountableComponent

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT

    class _Cast_MountableComponent:
        """Special nested class for casting MountableComponent to subclasses."""

        def __init__(self, parent: 'MountableComponent'):
            self._parent = parent

        @property
        def component(self):
            return self._parent._cast(_2427.Component)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2451
            
            return self._parent._cast(_2451.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2190
            
            return self._parent._cast(_2190.DesignEntity)

        @property
        def bearing(self):
            from mastapy.system_model.part_model import _2422
            
            return self._parent._cast(_2422.Bearing)

        @property
        def connector(self):
            from mastapy.system_model.part_model import _2430
            
            return self._parent._cast(_2430.Connector)

        @property
        def mass_disc(self):
            from mastapy.system_model.part_model import _2445
            
            return self._parent._cast(_2445.MassDisc)

        @property
        def measurement_component(self):
            from mastapy.system_model.part_model import _2446
            
            return self._parent._cast(_2446.MeasurementComponent)

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
        def mountable_component(self) -> 'MountableComponent':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MountableComponent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotation_about_axis(self) -> 'float':
        """float: 'RotationAboutAxis' is the original name of this property."""

        temp = self.wrapped.RotationAboutAxis

        if temp is None:
            return 0.0

        return temp

    @rotation_about_axis.setter
    def rotation_about_axis(self, value: 'float'):
        self.wrapped.RotationAboutAxis = float(value) if value is not None else 0.0

    @property
    def inner_component(self) -> '_2418.AbstractShaft':
        """AbstractShaft: 'InnerComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerComponent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection(self) -> '_2255.Connection':
        """Connection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket(self) -> '_2259.CylindricalSocket':
        """CylindricalSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def is_mounted(self) -> 'bool':
        """bool: 'IsMounted' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsMounted

        if temp is None:
            return False

        return temp

    def mount_on(self, shaft: '_2418.AbstractShaft', offset: Optional['float'] = float('nan')) -> '_2252.CoaxialConnection':
        """ 'MountOn' is the original name of this method.

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)

        Returns:
            mastapy.system_model.connections_and_sockets.CoaxialConnection
        """

        offset = float(offset)
        method_result = self.wrapped.MountOn(shaft.wrapped if shaft else None, offset if offset else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def try_mount_on(self, shaft: '_2418.AbstractShaft', offset: Optional['float'] = float('nan')) -> '_2428.ComponentsConnectedResult':
        """ 'TryMountOn' is the original name of this method.

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)

        Returns:
            mastapy.system_model.part_model.ComponentsConnectedResult
        """

        offset = float(offset)
        method_result = self.wrapped.TryMountOn(shaft.wrapped if shaft else None, offset if offset else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'MountableComponent._Cast_MountableComponent':
        return self._Cast_MountableComponent(self)
