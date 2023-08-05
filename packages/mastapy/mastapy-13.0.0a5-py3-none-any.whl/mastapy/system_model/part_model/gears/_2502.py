"""_2502.py

BevelGearSet
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.part_model.gears import _2496
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelGearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearSet',)


class BevelGearSet(_2496.AGMAGleasonConicalGearSet):
    """BevelGearSet

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET

    class _Cast_BevelGearSet:
        """Special nested class for casting BevelGearSet to subclasses."""

        def __init__(self, parent: 'BevelGearSet'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set(self):
            return self._parent._cast(_2496.AGMAGleasonConicalGearSet)

        @property
        def conical_gear_set(self):
            from mastapy.system_model.part_model.gears import _2506
            
            return self._parent._cast(_2506.ConicalGearSet)

        @property
        def gear_set(self):
            from mastapy.system_model.part_model.gears import _2514
            
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
        def bevel_differential_gear_set(self):
            from mastapy.system_model.part_model.gears import _2498
            
            return self._parent._cast(_2498.BevelDifferentialGearSet)

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
        def bevel_gear_set(self) -> 'BevelGearSet':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BevelGearSet._Cast_BevelGearSet':
        return self._Cast_BevelGearSet(self)
