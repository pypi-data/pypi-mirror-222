"""_2444.py

LoadSharingSettings
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOAD_SHARING_SETTINGS = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'LoadSharingSettings')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2443, _2420


__docformat__ = 'restructuredtext en'
__all__ = ('LoadSharingSettings',)


class LoadSharingSettings(_0.APIBase):
    """LoadSharingSettings

    This is a mastapy class.
    """

    TYPE = _LOAD_SHARING_SETTINGS

    class _Cast_LoadSharingSettings:
        """Special nested class for casting LoadSharingSettings to subclasses."""

        def __init__(self, parent: 'LoadSharingSettings'):
            self._parent = parent

        @property
        def load_sharing_settings(self) -> 'LoadSharingSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadSharingSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetary_load_sharing(self) -> '_2443.LoadSharingModes':
        """LoadSharingModes: 'PlanetaryLoadSharing' is the original name of this property."""

        temp = self.wrapped.PlanetaryLoadSharing

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.SystemModel.PartModel.LoadSharingModes')
        return constructor.new_from_mastapy('mastapy.system_model.part_model._2443', 'LoadSharingModes')(value) if value is not None else None

    @planetary_load_sharing.setter
    def planetary_load_sharing(self, value: '_2443.LoadSharingModes'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.SystemModel.PartModel.LoadSharingModes')
        self.wrapped.PlanetaryLoadSharing = value

    @property
    def planetary_load_sharing_agma_application_level(self) -> '_2420.AGMALoadSharingTableApplicationLevel':
        """AGMALoadSharingTableApplicationLevel: 'PlanetaryLoadSharingAGMAApplicationLevel' is the original name of this property."""

        temp = self.wrapped.PlanetaryLoadSharingAGMAApplicationLevel

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.SystemModel.PartModel.AGMALoadSharingTableApplicationLevel')
        return constructor.new_from_mastapy('mastapy.system_model.part_model._2420', 'AGMALoadSharingTableApplicationLevel')(value) if value is not None else None

    @planetary_load_sharing_agma_application_level.setter
    def planetary_load_sharing_agma_application_level(self, value: '_2420.AGMALoadSharingTableApplicationLevel'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.SystemModel.PartModel.AGMALoadSharingTableApplicationLevel')
        self.wrapped.PlanetaryLoadSharingAGMAApplicationLevel = value

    @property
    def cast_to(self) -> 'LoadSharingSettings._Cast_LoadSharingSettings':
        return self._Cast_LoadSharingSettings(self)
