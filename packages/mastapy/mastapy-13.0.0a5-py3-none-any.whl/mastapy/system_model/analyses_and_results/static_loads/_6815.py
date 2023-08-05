﻿"""_6815.py

ConicalGearSetHarmonicLoadData
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6862
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_HARMONIC_LOAD_DATA = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConicalGearSetHarmonicLoadData')

if TYPE_CHECKING:
    from mastapy.gears import _347
    from mastapy.math_utility import _1503


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearSetHarmonicLoadData',)


class ConicalGearSetHarmonicLoadData(_6862.GearSetHarmonicLoadData):
    """ConicalGearSetHarmonicLoadData

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_HARMONIC_LOAD_DATA

    class _Cast_ConicalGearSetHarmonicLoadData:
        """Special nested class for casting ConicalGearSetHarmonicLoadData to subclasses."""

        def __init__(self, parent: 'ConicalGearSetHarmonicLoadData'):
            self._parent = parent

        @property
        def gear_set_harmonic_load_data(self):
            return self._parent._cast(_6862.GearSetHarmonicLoadData)

        @property
        def harmonic_load_data_base(self):
            from mastapy.electric_machines.harmonic_load_data import _1370
            
            return self._parent._cast(_1370.HarmonicLoadDataBase)

        @property
        def conical_gear_set_harmonic_load_data(self) -> 'ConicalGearSetHarmonicLoadData':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearSetHarmonicLoadData.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def te_specification_type(self) -> '_347.TESpecificationType':
        """TESpecificationType: 'TESpecificationType' is the original name of this property."""

        temp = self.wrapped.TESpecificationType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.TESpecificationType')
        return constructor.new_from_mastapy('mastapy.gears._347', 'TESpecificationType')(value) if value is not None else None

    @te_specification_type.setter
    def te_specification_type(self, value: '_347.TESpecificationType'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.TESpecificationType')
        self.wrapped.TESpecificationType = value

    @property
    def excitations(self) -> 'List[_1503.FourierSeries]':
        """List[FourierSeries]: 'Excitations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Excitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def read_data_from_gleason_gemsxml(self):
        """ 'ReadDataFromGleasonGEMSXML' is the original name of this method."""

        self.wrapped.ReadDataFromGleasonGEMSXML()

    def read_data_from_ki_mo_sxml(self):
        """ 'ReadDataFromKIMoSXML' is the original name of this method."""

        self.wrapped.ReadDataFromKIMoSXML()

    @property
    def cast_to(self) -> 'ConicalGearSetHarmonicLoadData._Cast_ConicalGearSetHarmonicLoadData':
        return self._Cast_ConicalGearSetHarmonicLoadData(self)
