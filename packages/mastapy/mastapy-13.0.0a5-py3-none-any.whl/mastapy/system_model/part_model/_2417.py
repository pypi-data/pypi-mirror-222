"""_2417.py

AbstractAssembly
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2451
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'AbstractAssembly')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2427


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractAssembly',)


class AbstractAssembly(_2451.Part):
    """AbstractAssembly

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY

    class _Cast_AbstractAssembly:
        """Special nested class for casting AbstractAssembly to subclasses."""

        def __init__(self, parent: 'AbstractAssembly'):
            self._parent = parent

        @property
        def part(self):
            return self._parent._cast(_2451.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2190
            
            return self._parent._cast(_2190.DesignEntity)

        @property
        def assembly(self):
            from mastapy.system_model.part_model import _2416
            
            return self._parent._cast(_2416.Assembly)

        @property
        def bolted_joint(self):
            from mastapy.system_model.part_model import _2426
            
            return self._parent._cast(_2426.BoltedJoint)

        @property
        def flexible_pin_assembly(self):
            from mastapy.system_model.part_model import _2437
            
            return self._parent._cast(_2437.FlexiblePinAssembly)

        @property
        def root_assembly(self):
            from mastapy.system_model.part_model import _2457
            
            return self._parent._cast(_2457.RootAssembly)

        @property
        def specialised_assembly(self):
            from mastapy.system_model.part_model import _2459
            
            return self._parent._cast(_2459.SpecialisedAssembly)

        @property
        def agma_gleason_conical_gear_set(self):
            from mastapy.system_model.part_model.gears import _2496
            
            return self._parent._cast(_2496.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear_set(self):
            from mastapy.system_model.part_model.gears import _2498
            
            return self._parent._cast(_2498.BevelDifferentialGearSet)

        @property
        def bevel_gear_set(self):
            from mastapy.system_model.part_model.gears import _2502
            
            return self._parent._cast(_2502.BevelGearSet)

        @property
        def concept_gear_set(self):
            from mastapy.system_model.part_model.gears import _2504
            
            return self._parent._cast(_2504.ConceptGearSet)

        @property
        def conical_gear_set(self):
            from mastapy.system_model.part_model.gears import _2506
            
            return self._parent._cast(_2506.ConicalGearSet)

        @property
        def cylindrical_gear_set(self):
            from mastapy.system_model.part_model.gears import _2508
            
            return self._parent._cast(_2508.CylindricalGearSet)

        @property
        def face_gear_set(self):
            from mastapy.system_model.part_model.gears import _2511
            
            return self._parent._cast(_2511.FaceGearSet)

        @property
        def gear_set(self):
            from mastapy.system_model.part_model.gears import _2514
            
            return self._parent._cast(_2514.GearSet)

        @property
        def hypoid_gear_set(self):
            from mastapy.system_model.part_model.gears import _2517
            
            return self._parent._cast(_2517.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(self):
            from mastapy.system_model.part_model.gears import _2519
            
            return self._parent._cast(_2519.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(self):
            from mastapy.system_model.part_model.gears import _2521
            
            return self._parent._cast(_2521.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self):
            from mastapy.system_model.part_model.gears import _2523
            
            return self._parent._cast(_2523.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def planetary_gear_set(self):
            from mastapy.system_model.part_model.gears import _2524
            
            return self._parent._cast(_2524.PlanetaryGearSet)

        @property
        def spiral_bevel_gear_set(self):
            from mastapy.system_model.part_model.gears import _2526
            
            return self._parent._cast(_2526.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear_set(self):
            from mastapy.system_model.part_model.gears import _2528
            
            return self._parent._cast(_2528.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear_set(self):
            from mastapy.system_model.part_model.gears import _2530
            
            return self._parent._cast(_2530.StraightBevelGearSet)

        @property
        def worm_gear_set(self):
            from mastapy.system_model.part_model.gears import _2534
            
            return self._parent._cast(_2534.WormGearSet)

        @property
        def zerol_bevel_gear_set(self):
            from mastapy.system_model.part_model.gears import _2536
            
            return self._parent._cast(_2536.ZerolBevelGearSet)

        @property
        def cycloidal_assembly(self):
            from mastapy.system_model.part_model.cycloidal import _2550
            
            return self._parent._cast(_2550.CycloidalAssembly)

        @property
        def belt_drive(self):
            from mastapy.system_model.part_model.couplings import _2558
            
            return self._parent._cast(_2558.BeltDrive)

        @property
        def clutch(self):
            from mastapy.system_model.part_model.couplings import _2560
            
            return self._parent._cast(_2560.Clutch)

        @property
        def concept_coupling(self):
            from mastapy.system_model.part_model.couplings import _2563
            
            return self._parent._cast(_2563.ConceptCoupling)

        @property
        def coupling(self):
            from mastapy.system_model.part_model.couplings import _2565
            
            return self._parent._cast(_2565.Coupling)

        @property
        def cvt(self):
            from mastapy.system_model.part_model.couplings import _2568
            
            return self._parent._cast(_2568.CVT)

        @property
        def part_to_part_shear_coupling(self):
            from mastapy.system_model.part_model.couplings import _2570
            
            return self._parent._cast(_2570.PartToPartShearCoupling)

        @property
        def rolling_ring_assembly(self):
            from mastapy.system_model.part_model.couplings import _2579
            
            return self._parent._cast(_2579.RollingRingAssembly)

        @property
        def spring_damper(self):
            from mastapy.system_model.part_model.couplings import _2582
            
            return self._parent._cast(_2582.SpringDamper)

        @property
        def synchroniser(self):
            from mastapy.system_model.part_model.couplings import _2584
            
            return self._parent._cast(_2584.Synchroniser)

        @property
        def torque_converter(self):
            from mastapy.system_model.part_model.couplings import _2589
            
            return self._parent._cast(_2589.TorqueConverter)

        @property
        def abstract_assembly(self) -> 'AbstractAssembly':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractAssembly.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mass_of_assembly(self) -> 'float':
        """float: 'MassOfAssembly' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassOfAssembly

        if temp is None:
            return 0.0

        return temp

    @property
    def components_with_unknown_mass_properties(self) -> 'List[_2427.Component]':
        """List[Component]: 'ComponentsWithUnknownMassProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentsWithUnknownMassProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def components_with_zero_mass_properties(self) -> 'List[_2427.Component]':
        """List[Component]: 'ComponentsWithZeroMassProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentsWithZeroMassProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractAssembly._Cast_AbstractAssembly':
        return self._Cast_AbstractAssembly(self)
