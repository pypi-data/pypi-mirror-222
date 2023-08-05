"""_607.py

CylindricalCutterDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1817
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_CUTTER_DATABASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'CylindricalCutterDatabase')

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters import _710


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalCutterDatabase',)


T = TypeVar('T', bound='_710.CylindricalGearRealCutterDesign')


class CylindricalCutterDatabase(_1817.NamedDatabase[T]):
    """CylindricalCutterDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _CYLINDRICAL_CUTTER_DATABASE

    class _Cast_CylindricalCutterDatabase:
        """Special nested class for casting CylindricalCutterDatabase to subclasses."""

        def __init__(self, parent: 'CylindricalCutterDatabase'):
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
        def cylindrical_hob_database(self):
            from mastapy.gears.manufacturing.cylindrical import _612
            
            return self._parent._cast(_612.CylindricalHobDatabase)

        @property
        def cylindrical_shaper_database(self):
            from mastapy.gears.manufacturing.cylindrical import _623
            
            return self._parent._cast(_623.CylindricalShaperDatabase)

        @property
        def cylindrical_formed_wheel_grinder_database(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _702
            
            return self._parent._cast(_702.CylindricalFormedWheelGrinderDatabase)

        @property
        def cylindrical_gear_plunge_shaver_database(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _708
            
            return self._parent._cast(_708.CylindricalGearPlungeShaverDatabase)

        @property
        def cylindrical_gear_shaver_database(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _713
            
            return self._parent._cast(_713.CylindricalGearShaverDatabase)

        @property
        def cylindrical_worm_grinder_database(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _714
            
            return self._parent._cast(_714.CylindricalWormGrinderDatabase)

        @property
        def cylindrical_cutter_database(self) -> 'CylindricalCutterDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalCutterDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalCutterDatabase._Cast_CylindricalCutterDatabase':
        return self._Cast_CylindricalCutterDatabase(self)
