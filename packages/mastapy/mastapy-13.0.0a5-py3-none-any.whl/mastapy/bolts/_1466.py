"""_1466.py

ClampedSectionMaterialDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.bolts import _1457, _1456
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLAMPED_SECTION_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Bolts', 'ClampedSectionMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('ClampedSectionMaterialDatabase',)


class ClampedSectionMaterialDatabase(_1457.BoltedJointMaterialDatabase['_1456.BoltedJointMaterial']):
    """ClampedSectionMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _CLAMPED_SECTION_MATERIAL_DATABASE

    class _Cast_ClampedSectionMaterialDatabase:
        """Special nested class for casting ClampedSectionMaterialDatabase to subclasses."""

        def __init__(self, parent: 'ClampedSectionMaterialDatabase'):
            self._parent = parent

        @property
        def bolted_joint_material_database(self):
            return self._parent._cast(_1457.BoltedJointMaterialDatabase)

        @property
        def named_database(self):
            from mastapy.utility.databases import _1817
            
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
        def clamped_section_material_database(self) -> 'ClampedSectionMaterialDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ClampedSectionMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ClampedSectionMaterialDatabase._Cast_ClampedSectionMaterialDatabase':
        return self._Cast_ClampedSectionMaterialDatabase(self)
