"""_1457.py

BoltedJointMaterialDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1817
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Bolts', 'BoltedJointMaterialDatabase')

if TYPE_CHECKING:
    from mastapy.bolts import _1456


__docformat__ = 'restructuredtext en'
__all__ = ('BoltedJointMaterialDatabase',)


T = TypeVar('T', bound='_1456.BoltedJointMaterial')


class BoltedJointMaterialDatabase(_1817.NamedDatabase[T]):
    """BoltedJointMaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _BOLTED_JOINT_MATERIAL_DATABASE

    class _Cast_BoltedJointMaterialDatabase:
        """Special nested class for casting BoltedJointMaterialDatabase to subclasses."""

        def __init__(self, parent: 'BoltedJointMaterialDatabase'):
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
        def bolt_material_database(self):
            from mastapy.bolts import _1461
            
            return self._parent._cast(_1461.BoltMaterialDatabase)

        @property
        def clamped_section_material_database(self):
            from mastapy.bolts import _1466
            
            return self._parent._cast(_1466.ClampedSectionMaterialDatabase)

        @property
        def bolted_joint_material_database(self) -> 'BoltedJointMaterialDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BoltedJointMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BoltedJointMaterialDatabase._Cast_BoltedJointMaterialDatabase':
        return self._Cast_BoltedJointMaterialDatabase(self)
