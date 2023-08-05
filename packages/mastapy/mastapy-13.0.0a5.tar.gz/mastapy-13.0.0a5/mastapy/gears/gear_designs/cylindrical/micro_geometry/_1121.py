"""_1121.py

ProfileFormReliefWithDeviation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1122
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PROFILE_FORM_RELIEF_WITH_DEVIATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'ProfileFormReliefWithDeviation')


__docformat__ = 'restructuredtext en'
__all__ = ('ProfileFormReliefWithDeviation',)


class ProfileFormReliefWithDeviation(_1122.ProfileReliefWithDeviation):
    """ProfileFormReliefWithDeviation

    This is a mastapy class.
    """

    TYPE = _PROFILE_FORM_RELIEF_WITH_DEVIATION

    class _Cast_ProfileFormReliefWithDeviation:
        """Special nested class for casting ProfileFormReliefWithDeviation to subclasses."""

        def __init__(self, parent: 'ProfileFormReliefWithDeviation'):
            self._parent = parent

        @property
        def profile_relief_with_deviation(self):
            return self._parent._cast(_1122.ProfileReliefWithDeviation)

        @property
        def relief_with_deviation(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1124
            
            return self._parent._cast(_1124.ReliefWithDeviation)

        @property
        def profile_form_relief_with_deviation(self) -> 'ProfileFormReliefWithDeviation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ProfileFormReliefWithDeviation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ProfileFormReliefWithDeviation._Cast_ProfileFormReliefWithDeviation':
        return self._Cast_ProfileFormReliefWithDeviation(self)
