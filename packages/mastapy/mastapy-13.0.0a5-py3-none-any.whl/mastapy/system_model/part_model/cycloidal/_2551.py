"""_2551.py

CycloidalDisc
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.part_model import _2418
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_CYCLOIDAL_DISC = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Cycloidal', 'CycloidalDisc')

if TYPE_CHECKING:
    from mastapy.cycloidal import _1444
    from mastapy.materials import _267
    from mastapy.system_model.part_model import _2444
    from mastapy.system_model.connections_and_sockets.cycloidal import _2322


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDisc',)


class CycloidalDisc(_2418.AbstractShaft):
    """CycloidalDisc

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC

    class _Cast_CycloidalDisc:
        """Special nested class for casting CycloidalDisc to subclasses."""

        def __init__(self, parent: 'CycloidalDisc'):
            self._parent = parent

        @property
        def abstract_shaft(self):
            return self._parent._cast(_2418.AbstractShaft)

        @property
        def abstract_shaft_or_housing(self):
            from mastapy.system_model.part_model import _2419
            
            return self._parent._cast(_2419.AbstractShaftOrHousing)

        @property
        def component(self):
            from mastapy.system_model.part_model import _2427
            
            return self._parent._cast(_2427.Component)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2451
            
            return self._parent._cast(_2451.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2190
            
            return self._parent._cast(_2190.DesignEntity)

        @property
        def cycloidal_disc(self) -> 'CycloidalDisc':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDisc.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bore_diameter(self) -> 'float':
        """float: 'BoreDiameter' is the original name of this property."""

        temp = self.wrapped.BoreDiameter

        if temp is None:
            return 0.0

        return temp

    @bore_diameter.setter
    def bore_diameter(self, value: 'float'):
        self.wrapped.BoreDiameter = float(value) if value is not None else 0.0

    @property
    def disc_material_database(self) -> 'str':
        """str: 'DiscMaterialDatabase' is the original name of this property."""

        temp = self.wrapped.DiscMaterialDatabase.SelectedItemName

        if temp is None:
            return ''

        return temp

    @disc_material_database.setter
    def disc_material_database(self, value: 'str'):
        self.wrapped.DiscMaterialDatabase.SetSelectedItem(str(value) if value is not None else '')

    @property
    def hole_diameter_for_eccentric_bearing(self) -> 'float':
        """float: 'HoleDiameterForEccentricBearing' is the original name of this property."""

        temp = self.wrapped.HoleDiameterForEccentricBearing

        if temp is None:
            return 0.0

        return temp

    @hole_diameter_for_eccentric_bearing.setter
    def hole_diameter_for_eccentric_bearing(self, value: 'float'):
        self.wrapped.HoleDiameterForEccentricBearing = float(value) if value is not None else 0.0

    @property
    def length(self) -> 'float':
        """float: 'Length' is the original name of this property."""

        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    def length(self, value: 'float'):
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def number_of_planetary_sockets(self) -> 'int':
        """int: 'NumberOfPlanetarySockets' is the original name of this property."""

        temp = self.wrapped.NumberOfPlanetarySockets

        if temp is None:
            return 0

        return temp

    @number_of_planetary_sockets.setter
    def number_of_planetary_sockets(self, value: 'int'):
        self.wrapped.NumberOfPlanetarySockets = int(value) if value is not None else 0

    @property
    def cycloidal_disc_design(self) -> '_1444.CycloidalDiscDesign':
        """CycloidalDiscDesign: 'CycloidalDiscDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CycloidalDiscDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def disc_material(self) -> '_267.Material':
        """Material: 'DiscMaterial' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DiscMaterial

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def load_sharing_settings(self) -> '_2444.LoadSharingSettings':
        """LoadSharingSettings: 'LoadSharingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadSharingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetary_bearing_sockets(self) -> 'List[_2322.CycloidalDiscPlanetaryBearingSocket]':
        """List[CycloidalDiscPlanetaryBearingSocket]: 'PlanetaryBearingSockets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetaryBearingSockets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CycloidalDisc._Cast_CycloidalDisc':
        return self._Cast_CycloidalDisc(self)
