"""_2506.py

ConicalGearSet
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2514
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConicalGearSet')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1152
    from mastapy.system_model.part_model.gears import _2505


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearSet',)


class ConicalGearSet(_2514.GearSet):
    """ConicalGearSet

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET

    class _Cast_ConicalGearSet:
        """Special nested class for casting ConicalGearSet to subclasses."""

        def __init__(self, parent: 'ConicalGearSet'):
            self._parent = parent

        @property
        def gear_set(self):
            return self._parent._cast(_2514.GearSet)

        @property
        def specialised_assembly(self):
            from mastapy.system_model.part_model import _2459
            
            return self._parent._cast(_2459.SpecialisedAssembly)

        @property
        def abstract_assembly(self):
            from mastapy.system_model.part_model import _2417
            
            return self._parent._cast(_2417.AbstractAssembly)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2451
            
            return self._parent._cast(_2451.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2190
            
            return self._parent._cast(_2190.DesignEntity)

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
        def zerol_bevel_gear_set(self):
            from mastapy.system_model.part_model.gears import _2536
            
            return self._parent._cast(_2536.ZerolBevelGearSet)

        @property
        def conical_gear_set(self) -> 'ConicalGearSet':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_set_design(self) -> '_1152.ConicalGearSetDesign':
        """ConicalGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_set_design(self) -> '_1152.ConicalGearSetDesign':
        """ConicalGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gears(self) -> 'List[_2505.ConicalGear]':
        """List[ConicalGear]: 'ConicalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalGearSet._Cast_ConicalGearSet':
        return self._Cast_ConicalGearSet(self)
