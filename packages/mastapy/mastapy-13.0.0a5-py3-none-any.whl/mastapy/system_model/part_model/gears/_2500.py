"""_2500.py

BevelDifferentialSunGear
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.part_model.gears import _2497
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialSunGear')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialSunGear',)


class BevelDifferentialSunGear(_2497.BevelDifferentialGear):
    """BevelDifferentialSunGear

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR

    class _Cast_BevelDifferentialSunGear:
        """Special nested class for casting BevelDifferentialSunGear to subclasses."""

        def __init__(self, parent: 'BevelDifferentialSunGear'):
            self._parent = parent

        @property
        def bevel_differential_gear(self):
            return self._parent._cast(_2497.BevelDifferentialGear)

        @property
        def bevel_gear(self):
            from mastapy.system_model.part_model.gears import _2501
            
            return self._parent._cast(_2501.BevelGear)

        @property
        def agma_gleason_conical_gear(self):
            from mastapy.system_model.part_model.gears import _2495
            
            return self._parent._cast(_2495.AGMAGleasonConicalGear)

        @property
        def conical_gear(self):
            from mastapy.system_model.part_model.gears import _2505
            
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
        def bevel_differential_sun_gear(self) -> 'BevelDifferentialSunGear':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialSunGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BevelDifferentialSunGear._Cast_BevelDifferentialSunGear':
        return self._Cast_BevelDifferentialSunGear(self)
