"""_492.py

PlasticSNCurveForTheSpecifiedOperatingConditions
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.materials import _601
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLASTIC_SN_CURVE_FOR_THE_SPECIFIED_OPERATING_CONDITIONS = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.PlasticVDI2736', 'PlasticSNCurveForTheSpecifiedOperatingConditions')

if TYPE_CHECKING:
    from mastapy.materials import _286


__docformat__ = 'restructuredtext en'
__all__ = ('PlasticSNCurveForTheSpecifiedOperatingConditions',)


class PlasticSNCurveForTheSpecifiedOperatingConditions(_601.PlasticSNCurve):
    """PlasticSNCurveForTheSpecifiedOperatingConditions

    This is a mastapy class.
    """

    TYPE = _PLASTIC_SN_CURVE_FOR_THE_SPECIFIED_OPERATING_CONDITIONS

    class _Cast_PlasticSNCurveForTheSpecifiedOperatingConditions:
        """Special nested class for casting PlasticSNCurveForTheSpecifiedOperatingConditions to subclasses."""

        def __init__(self, parent: 'PlasticSNCurveForTheSpecifiedOperatingConditions'):
            self._parent = parent

        @property
        def plastic_sn_curve(self):
            return self._parent._cast(_601.PlasticSNCurve)

        @property
        def plastic_sn_curve_for_the_specified_operating_conditions(self) -> 'PlasticSNCurveForTheSpecifiedOperatingConditions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlasticSNCurveForTheSpecifiedOperatingConditions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def flank_temperature(self) -> 'float':
        """float: 'FlankTemperature' is the original name of this property."""

        temp = self.wrapped.FlankTemperature

        if temp is None:
            return 0.0

        return temp

    @flank_temperature.setter
    def flank_temperature(self, value: 'float'):
        self.wrapped.FlankTemperature = float(value) if value is not None else 0.0

    @property
    def life_cycles(self) -> 'float':
        """float: 'LifeCycles' is the original name of this property."""

        temp = self.wrapped.LifeCycles

        if temp is None:
            return 0.0

        return temp

    @life_cycles.setter
    def life_cycles(self, value: 'float'):
        self.wrapped.LifeCycles = float(value) if value is not None else 0.0

    @property
    def lubricant(self) -> '_286.VDI2736LubricantType':
        """VDI2736LubricantType: 'Lubricant' is the original name of this property."""

        temp = self.wrapped.Lubricant

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Materials.VDI2736LubricantType')
        return constructor.new_from_mastapy('mastapy.materials._286', 'VDI2736LubricantType')(value) if value is not None else None

    @lubricant.setter
    def lubricant(self, value: '_286.VDI2736LubricantType'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Materials.VDI2736LubricantType')
        self.wrapped.Lubricant = value

    @property
    def root_temperature(self) -> 'float':
        """float: 'RootTemperature' is the original name of this property."""

        temp = self.wrapped.RootTemperature

        if temp is None:
            return 0.0

        return temp

    @root_temperature.setter
    def root_temperature(self, value: 'float'):
        self.wrapped.RootTemperature = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'PlasticSNCurveForTheSpecifiedOperatingConditions._Cast_PlasticSNCurveForTheSpecifiedOperatingConditions':
        return self._Cast_PlasticSNCurveForTheSpecifiedOperatingConditions(self)
