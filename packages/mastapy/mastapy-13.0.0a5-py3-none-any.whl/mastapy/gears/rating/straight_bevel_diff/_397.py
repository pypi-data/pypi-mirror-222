"""_397.py

StraightBevelDiffGearRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.rating.conical import _537
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.StraightBevelDiff', 'StraightBevelDiffGearRating')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel_diff import _962


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearRating',)


class StraightBevelDiffGearRating(_537.ConicalGearRating):
    """StraightBevelDiffGearRating

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_RATING

    class _Cast_StraightBevelDiffGearRating:
        """Special nested class for casting StraightBevelDiffGearRating to subclasses."""

        def __init__(self, parent: 'StraightBevelDiffGearRating'):
            self._parent = parent

        @property
        def conical_gear_rating(self):
            return self._parent._cast(_537.ConicalGearRating)

        @property
        def gear_rating(self):
            from mastapy.gears.rating import _359
            
            return self._parent._cast(_359.GearRating)

        @property
        def abstract_gear_rating(self):
            from mastapy.gears.rating import _352
            
            return self._parent._cast(_352.AbstractGearRating)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearAnalysis)

        @property
        def straight_bevel_diff_gear_rating(self) -> 'StraightBevelDiffGearRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cycles_to_fail(self) -> 'float':
        """float: 'CyclesToFail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CyclesToFail

        if temp is None:
            return 0.0

        return temp

    @property
    def cycles_to_fail_bending(self) -> 'float':
        """float: 'CyclesToFailBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CyclesToFailBending

        if temp is None:
            return 0.0

        return temp

    @property
    def cycles_to_fail_contact(self) -> 'float':
        """float: 'CyclesToFailContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CyclesToFailContact

        if temp is None:
            return 0.0

        return temp

    @property
    def time_to_fail(self) -> 'float':
        """float: 'TimeToFail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeToFail

        if temp is None:
            return 0.0

        return temp

    @property
    def time_to_fail_bending(self) -> 'float':
        """float: 'TimeToFailBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeToFailBending

        if temp is None:
            return 0.0

        return temp

    @property
    def time_to_fail_contact(self) -> 'float':
        """float: 'TimeToFailContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeToFailContact

        if temp is None:
            return 0.0

        return temp

    @property
    def straight_bevel_diff_gear(self) -> '_962.StraightBevelDiffGearDesign':
        """StraightBevelDiffGearDesign: 'StraightBevelDiffGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'StraightBevelDiffGearRating._Cast_StraightBevelDiffGearRating':
        return self._Cast_StraightBevelDiffGearRating(self)
