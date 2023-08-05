"""_958.py

StraightBevelGearDesign
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.gear_designs.bevel import _1176
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.StraightBevel', 'StraightBevelGearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearDesign',)


class StraightBevelGearDesign(_1176.BevelGearDesign):
    """StraightBevelGearDesign

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_DESIGN

    class _Cast_StraightBevelGearDesign:
        """Special nested class for casting StraightBevelGearDesign to subclasses."""

        def __init__(self, parent: 'StraightBevelGearDesign'):
            self._parent = parent

        @property
        def bevel_gear_design(self):
            return self._parent._cast(_1176.BevelGearDesign)

        @property
        def agma_gleason_conical_gear_design(self):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1189
            
            return self._parent._cast(_1189.AGMAGleasonConicalGearDesign)

        @property
        def conical_gear_design(self):
            from mastapy.gears.gear_designs.conical import _1150
            
            return self._parent._cast(_1150.ConicalGearDesign)

        @property
        def gear_design(self):
            from mastapy.gears.gear_designs import _944
            
            return self._parent._cast(_944.GearDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _945
            
            return self._parent._cast(_945.GearDesignComponent)

        @property
        def straight_bevel_gear_design(self) -> 'StraightBevelGearDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'StraightBevelGearDesign._Cast_StraightBevelGearDesign':
        return self._Cast_StraightBevelGearDesign(self)
