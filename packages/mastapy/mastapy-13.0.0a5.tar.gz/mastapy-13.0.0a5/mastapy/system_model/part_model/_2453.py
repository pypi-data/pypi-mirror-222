"""_2453.py

PlanetCarrierSettings
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.utility import _1585
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_SETTINGS = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'PlanetCarrierSettings')

if TYPE_CHECKING:
    from mastapy.system_model import _2202


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetCarrierSettings',)


class PlanetCarrierSettings(_1585.PerMachineSettings):
    """PlanetCarrierSettings

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_SETTINGS

    class _Cast_PlanetCarrierSettings:
        """Special nested class for casting PlanetCarrierSettings to subclasses."""

        def __init__(self, parent: 'PlanetCarrierSettings'):
            self._parent = parent

        @property
        def per_machine_settings(self):
            return self._parent._cast(_1585.PerMachineSettings)

        @property
        def persistent_singleton(self):
            from mastapy.utility import _1586
            
            return self._parent._cast(_1586.PersistentSingleton)

        @property
        def planet_carrier_settings(self) -> 'PlanetCarrierSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetCarrierSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planet_pin_manufacturing_errors_coordinate_system(self) -> '_2202.PlanetPinManufacturingErrorsCoordinateSystem':
        """PlanetPinManufacturingErrorsCoordinateSystem: 'PlanetPinManufacturingErrorsCoordinateSystem' is the original name of this property."""

        temp = self.wrapped.PlanetPinManufacturingErrorsCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.SystemModel.PlanetPinManufacturingErrorsCoordinateSystem')
        return constructor.new_from_mastapy('mastapy.system_model._2202', 'PlanetPinManufacturingErrorsCoordinateSystem')(value) if value is not None else None

    @planet_pin_manufacturing_errors_coordinate_system.setter
    def planet_pin_manufacturing_errors_coordinate_system(self, value: '_2202.PlanetPinManufacturingErrorsCoordinateSystem'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.SystemModel.PlanetPinManufacturingErrorsCoordinateSystem')
        self.wrapped.PlanetPinManufacturingErrorsCoordinateSystem = value

    @property
    def cast_to(self) -> 'PlanetCarrierSettings._Cast_PlanetCarrierSettings':
        return self._Cast_PlanetCarrierSettings(self)
