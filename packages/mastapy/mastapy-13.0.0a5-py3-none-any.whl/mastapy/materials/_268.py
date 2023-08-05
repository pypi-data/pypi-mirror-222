"""_268.py

MaterialDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1817
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Materials', 'MaterialDatabase')

if TYPE_CHECKING:
    from mastapy.materials import _267


__docformat__ = 'restructuredtext en'
__all__ = ('MaterialDatabase',)


T = TypeVar('T', bound='_267.Material')


class MaterialDatabase(_1817.NamedDatabase[T]):
    """MaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _MATERIAL_DATABASE

    class _Cast_MaterialDatabase:
        """Special nested class for casting MaterialDatabase to subclasses."""

        def __init__(self, parent: 'MaterialDatabase'):
            self._parent = parent

        @property
        def named_database(self):
            return self._parent._cast(_1817.NamedDatabase)

        @property
        def sql_database(self):
            from mastapy.utility.databases import _1820, _1819
            
            return self._parent._cast(_1820.SQLDatabase)

        @property
        def database(self):
            from mastapy.utility.databases import _1813, _1819
            
            return self._parent._cast(_1813.Database)

        @property
        def shaft_material_database(self):
            from mastapy.shafts import _25
            
            return self._parent._cast(_25.ShaftMaterialDatabase)

        @property
        def bevel_gear_abstract_material_database(self):
            from mastapy.gears.materials import _581
            
            return self._parent._cast(_581.BevelGearAbstractMaterialDatabase)

        @property
        def bevel_gear_iso_material_database(self):
            from mastapy.gears.materials import _583
            
            return self._parent._cast(_583.BevelGearISOMaterialDatabase)

        @property
        def cylindrical_gear_agma_material_database(self):
            from mastapy.gears.materials import _586
            
            return self._parent._cast(_586.CylindricalGearAGMAMaterialDatabase)

        @property
        def cylindrical_gear_iso_material_database(self):
            from mastapy.gears.materials import _587
            
            return self._parent._cast(_587.CylindricalGearISOMaterialDatabase)

        @property
        def cylindrical_gear_material_database(self):
            from mastapy.gears.materials import _589
            
            return self._parent._cast(_589.CylindricalGearMaterialDatabase)

        @property
        def cylindrical_gear_plastic_material_database(self):
            from mastapy.gears.materials import _590
            
            return self._parent._cast(_590.CylindricalGearPlasticMaterialDatabase)

        @property
        def magnet_material_database(self):
            from mastapy.electric_machines import _1276
            
            return self._parent._cast(_1276.MagnetMaterialDatabase)

        @property
        def stator_rotor_material_database(self):
            from mastapy.electric_machines import _1294
            
            return self._parent._cast(_1294.StatorRotorMaterialDatabase)

        @property
        def winding_material_database(self):
            from mastapy.electric_machines import _1306
            
            return self._parent._cast(_1306.WindingMaterialDatabase)

        @property
        def cycloidal_disc_material_database(self):
            from mastapy.cycloidal import _1447
            
            return self._parent._cast(_1447.CycloidalDiscMaterialDatabase)

        @property
        def ring_pins_material_database(self):
            from mastapy.cycloidal import _1454
            
            return self._parent._cast(_1454.RingPinsMaterialDatabase)

        @property
        def material_database(self) -> 'MaterialDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MaterialDatabase._Cast_MaterialDatabase':
        return self._Cast_MaterialDatabase(self)
