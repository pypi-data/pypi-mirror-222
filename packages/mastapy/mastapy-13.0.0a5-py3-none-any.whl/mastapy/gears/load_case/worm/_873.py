"""_873.py

WormGearLoadCase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.load_case import _870
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Worm', 'WormGearLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearLoadCase',)


class WormGearLoadCase(_870.GearLoadCaseBase):
    """WormGearLoadCase

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_LOAD_CASE

    class _Cast_WormGearLoadCase:
        """Special nested class for casting WormGearLoadCase to subclasses."""

        def __init__(self, parent: 'WormGearLoadCase'):
            self._parent = parent

        @property
        def gear_load_case_base(self):
            return self._parent._cast(_870.GearLoadCaseBase)

        @property
        def gear_design_analysis(self):
            from mastapy.gears.analysis import _1214
            
            return self._parent._cast(_1214.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearAnalysis)

        @property
        def worm_gear_load_case(self) -> 'WormGearLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGearLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'WormGearLoadCase._Cast_WormGearLoadCase':
        return self._Cast_WormGearLoadCase(self)
