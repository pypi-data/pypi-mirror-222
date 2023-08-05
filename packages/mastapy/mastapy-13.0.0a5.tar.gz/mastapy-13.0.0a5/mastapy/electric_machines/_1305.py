"""_1305.py

WindingMaterial
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.materials import _267
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WINDING_MATERIAL = python_net_import('SMT.MastaAPI.ElectricMachines', 'WindingMaterial')


__docformat__ = 'restructuredtext en'
__all__ = ('WindingMaterial',)


class WindingMaterial(_267.Material):
    """WindingMaterial

    This is a mastapy class.
    """

    TYPE = _WINDING_MATERIAL

    class _Cast_WindingMaterial:
        """Special nested class for casting WindingMaterial to subclasses."""

        def __init__(self, parent: 'WindingMaterial'):
            self._parent = parent

        @property
        def material(self):
            return self._parent._cast(_267.Material)

        @property
        def named_database_item(self):
            from mastapy.utility.databases import _1818
            
            return self._parent._cast(_1818.NamedDatabaseItem)

        @property
        def winding_material(self) -> 'WindingMaterial':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WindingMaterial.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def relative_permeability(self) -> 'float':
        """float: 'RelativePermeability' is the original name of this property."""

        temp = self.wrapped.RelativePermeability

        if temp is None:
            return 0.0

        return temp

    @relative_permeability.setter
    def relative_permeability(self, value: 'float'):
        self.wrapped.RelativePermeability = float(value) if value is not None else 0.0

    @property
    def temperature_coefficient_for_winding_resistivity(self) -> 'float':
        """float: 'TemperatureCoefficientForWindingResistivity' is the original name of this property."""

        temp = self.wrapped.TemperatureCoefficientForWindingResistivity

        if temp is None:
            return 0.0

        return temp

    @temperature_coefficient_for_winding_resistivity.setter
    def temperature_coefficient_for_winding_resistivity(self, value: 'float'):
        self.wrapped.TemperatureCoefficientForWindingResistivity = float(value) if value is not None else 0.0

    @property
    def winding_resistivity_at_20_degrees_c(self) -> 'float':
        """float: 'WindingResistivityAt20DegreesC' is the original name of this property."""

        temp = self.wrapped.WindingResistivityAt20DegreesC

        if temp is None:
            return 0.0

        return temp

    @winding_resistivity_at_20_degrees_c.setter
    def winding_resistivity_at_20_degrees_c(self, value: 'float'):
        self.wrapped.WindingResistivityAt20DegreesC = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'WindingMaterial._Cast_WindingMaterial':
        return self._Cast_WindingMaterial(self)
