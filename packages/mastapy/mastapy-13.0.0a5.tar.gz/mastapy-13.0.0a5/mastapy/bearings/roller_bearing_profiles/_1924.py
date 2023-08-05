"""_1924.py

RollerBearingUserSpecifiedProfile
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.bearings.roller_bearing_profiles import _1923
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLER_BEARING_USER_SPECIFIED_PROFILE = python_net_import('SMT.MastaAPI.Bearings.RollerBearingProfiles', 'RollerBearingUserSpecifiedProfile')

if TYPE_CHECKING:
    from mastapy.bearings.roller_bearing_profiles import _1914, _1916, _1926


__docformat__ = 'restructuredtext en'
__all__ = ('RollerBearingUserSpecifiedProfile',)


class RollerBearingUserSpecifiedProfile(_1923.RollerBearingProfile):
    """RollerBearingUserSpecifiedProfile

    This is a mastapy class.
    """

    TYPE = _ROLLER_BEARING_USER_SPECIFIED_PROFILE

    class _Cast_RollerBearingUserSpecifiedProfile:
        """Special nested class for casting RollerBearingUserSpecifiedProfile to subclasses."""

        def __init__(self, parent: 'RollerBearingUserSpecifiedProfile'):
            self._parent = parent

        @property
        def roller_bearing_profile(self):
            return self._parent._cast(_1923.RollerBearingProfile)

        @property
        def roller_bearing_user_specified_profile(self) -> 'RollerBearingUserSpecifiedProfile':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollerBearingUserSpecifiedProfile.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def data_to_use(self) -> '_1914.ProfileDataToUse':
        """ProfileDataToUse: 'DataToUse' is the original name of this property."""

        temp = self.wrapped.DataToUse

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bearings.RollerBearingProfiles.ProfileDataToUse')
        return constructor.new_from_mastapy('mastapy.bearings.roller_bearing_profiles._1914', 'ProfileDataToUse')(value) if value is not None else None

    @data_to_use.setter
    def data_to_use(self, value: '_1914.ProfileDataToUse'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Bearings.RollerBearingProfiles.ProfileDataToUse')
        self.wrapped.DataToUse = value

    @property
    def number_of_points(self) -> 'int':
        """int: 'NumberOfPoints' is the original name of this property."""

        temp = self.wrapped.NumberOfPoints

        if temp is None:
            return 0

        return temp

    @number_of_points.setter
    def number_of_points(self, value: 'int'):
        self.wrapped.NumberOfPoints = int(value) if value is not None else 0

    @property
    def profile_to_fit(self) -> '_1916.ProfileToFit':
        """ProfileToFit: 'ProfileToFit' is the original name of this property."""

        temp = self.wrapped.ProfileToFit

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bearings.RollerBearingProfiles.ProfileToFit')
        return constructor.new_from_mastapy('mastapy.bearings.roller_bearing_profiles._1916', 'ProfileToFit')(value) if value is not None else None

    @profile_to_fit.setter
    def profile_to_fit(self, value: '_1916.ProfileToFit'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Bearings.RollerBearingProfiles.ProfileToFit')
        self.wrapped.ProfileToFit = value

    @property
    def points(self) -> 'List[_1926.UserSpecifiedProfilePoint]':
        """List[UserSpecifiedProfilePoint]: 'Points' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Points

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def set_to_full_range(self):
        """ 'SetToFullRange' is the original name of this method."""

        self.wrapped.SetToFullRange()

    @property
    def cast_to(self) -> 'RollerBearingUserSpecifiedProfile._Cast_RollerBearingUserSpecifiedProfile':
        return self._Cast_RollerBearingUserSpecifiedProfile(self)
