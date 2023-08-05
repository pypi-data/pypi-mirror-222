"""_2009.py

LoadedNeedleRollerBearingRow
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _1997
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NEEDLE_ROLLER_BEARING_ROW = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedNeedleRollerBearingRow')

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2008


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedNeedleRollerBearingRow',)


class LoadedNeedleRollerBearingRow(_1997.LoadedCylindricalRollerBearingRow):
    """LoadedNeedleRollerBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_NEEDLE_ROLLER_BEARING_ROW

    class _Cast_LoadedNeedleRollerBearingRow:
        """Special nested class for casting LoadedNeedleRollerBearingRow to subclasses."""

        def __init__(self, parent: 'LoadedNeedleRollerBearingRow'):
            self._parent = parent

        @property
        def loaded_cylindrical_roller_bearing_row(self):
            return self._parent._cast(_1997.LoadedCylindricalRollerBearingRow)

        @property
        def loaded_non_barrel_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2012
            
            return self._parent._cast(_2012.LoadedNonBarrelRollerBearingRow)

        @property
        def loaded_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2017
            
            return self._parent._cast(_2017.LoadedRollerBearingRow)

        @property
        def loaded_rolling_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2021
            
            return self._parent._cast(_2021.LoadedRollingBearingRow)

        @property
        def loaded_needle_roller_bearing_row(self) -> 'LoadedNeedleRollerBearingRow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedNeedleRollerBearingRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cage_land_sliding_power_loss(self) -> 'float':
        """float: 'CageLandSlidingPowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CageLandSlidingPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def rolling_power_loss(self) -> 'float':
        """float: 'RollingPowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def rolling_power_loss_traction_coefficient(self) -> 'float':
        """float: 'RollingPowerLossTractionCoefficient' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingPowerLossTractionCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_power_loss(self) -> 'float':
        """float: 'SlidingPowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_power_loss_traction_coefficient(self) -> 'float':
        """float: 'SlidingPowerLossTractionCoefficient' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingPowerLossTractionCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def total_power_loss(self) -> 'float':
        """float: 'TotalPowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def total_power_loss_traction_coefficient(self) -> 'float':
        """float: 'TotalPowerLossTractionCoefficient' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalPowerLossTractionCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def loaded_bearing(self) -> '_2008.LoadedNeedleRollerBearingResults':
        """LoadedNeedleRollerBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'LoadedNeedleRollerBearingRow._Cast_LoadedNeedleRollerBearingRow':
        return self._Cast_LoadedNeedleRollerBearingRow(self)
