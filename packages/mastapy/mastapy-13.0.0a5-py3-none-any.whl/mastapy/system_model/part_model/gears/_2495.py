"""_2495.py

AGMAGleasonConicalGear
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.part_model.gears import _2505
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'AGMAGleasonConicalGear')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGear',)


class AGMAGleasonConicalGear(_2505.ConicalGear):
    """AGMAGleasonConicalGear

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR

    class _Cast_AGMAGleasonConicalGear:
        """Special nested class for casting AGMAGleasonConicalGear to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGear'):
            self._parent = parent

        @property
        def conical_gear(self):
            return self._parent._cast(_2505.ConicalGear)

        @property
        def gear(self):
            from mastapy.system_model.part_model.gears import _2512
            
            return self._parent._cast(_2512.Gear)

        @property
        def mountable_component(self):
            from mastapy.system_model.part_model import _2447
            
            return self._parent._cast(_2447.MountableComponent)

        @property
        def component(self):
            from mastapy.system_model.part_model import _2427
            
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
        def hypoid_gear(self):
            from mastapy.system_model.part_model.gears import _2516
            
            return self._parent._cast(_2516.HypoidGear)

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
        def zerol_bevel_gear(self):
            from mastapy.system_model.part_model.gears import _2535
            
            return self._parent._cast(_2535.ZerolBevelGear)

        @property
        def agma_gleason_conical_gear(self) -> 'AGMAGleasonConicalGear':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear':
        return self._Cast_AGMAGleasonConicalGear(self)
