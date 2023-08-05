"""_2028.py

LoadedSphericalRollerRadialBearingRow
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2017
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_SPHERICAL_ROLLER_RADIAL_BEARING_ROW = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedSphericalRollerRadialBearingRow')

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2027


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedSphericalRollerRadialBearingRow',)


class LoadedSphericalRollerRadialBearingRow(_2017.LoadedRollerBearingRow):
    """LoadedSphericalRollerRadialBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_SPHERICAL_ROLLER_RADIAL_BEARING_ROW

    class _Cast_LoadedSphericalRollerRadialBearingRow:
        """Special nested class for casting LoadedSphericalRollerRadialBearingRow to subclasses."""

        def __init__(self, parent: 'LoadedSphericalRollerRadialBearingRow'):
            self._parent = parent

        @property
        def loaded_roller_bearing_row(self):
            return self._parent._cast(_2017.LoadedRollerBearingRow)

        @property
        def loaded_rolling_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2021
            
            return self._parent._cast(_2021.LoadedRollingBearingRow)

        @property
        def loaded_spherical_roller_radial_bearing_row(self) -> 'LoadedSphericalRollerRadialBearingRow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedSphericalRollerRadialBearingRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self) -> '_2027.LoadedSphericalRollerRadialBearingResults':
        """LoadedSphericalRollerRadialBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'LoadedSphericalRollerRadialBearingRow._Cast_LoadedSphericalRollerRadialBearingRow':
        return self._Cast_LoadedSphericalRollerRadialBearingRow(self)
