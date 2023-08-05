"""_2558.py

BeltDrive
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.system_model.part_model import _2459
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'BeltDrive')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2559, _2572
    from mastapy.system_model.connections_and_sockets import _2251


__docformat__ = 'restructuredtext en'
__all__ = ('BeltDrive',)


class BeltDrive(_2459.SpecialisedAssembly):
    """BeltDrive

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE

    class _Cast_BeltDrive:
        """Special nested class for casting BeltDrive to subclasses."""

        def __init__(self, parent: 'BeltDrive'):
            self._parent = parent

        @property
        def specialised_assembly(self):
            return self._parent._cast(_2459.SpecialisedAssembly)

        @property
        def abstract_assembly(self):
            from mastapy.system_model.part_model import _2417
            
            return self._parent._cast(_2417.AbstractAssembly)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2451
            
            return self._parent._cast(_2451.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2190
            
            return self._parent._cast(_2190.DesignEntity)

        @property
        def cvt(self):
            from mastapy.system_model.part_model.couplings import _2568
            
            return self._parent._cast(_2568.CVT)

        @property
        def belt_drive(self) -> 'BeltDrive':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BeltDrive.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def belt_length(self) -> 'float':
        """float: 'BeltLength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BeltLength

        if temp is None:
            return 0.0

        return temp

    @property
    def belt_mass(self) -> 'float':
        """float: 'BeltMass' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BeltMass

        if temp is None:
            return 0.0

        return temp

    @property
    def belt_mass_per_unit_length(self) -> 'float':
        """float: 'BeltMassPerUnitLength' is the original name of this property."""

        temp = self.wrapped.BeltMassPerUnitLength

        if temp is None:
            return 0.0

        return temp

    @belt_mass_per_unit_length.setter
    def belt_mass_per_unit_length(self, value: 'float'):
        self.wrapped.BeltMassPerUnitLength = float(value) if value is not None else 0.0

    @property
    def pre_tension(self) -> 'float':
        """float: 'PreTension' is the original name of this property."""

        temp = self.wrapped.PreTension

        if temp is None:
            return 0.0

        return temp

    @pre_tension.setter
    def pre_tension(self, value: 'float'):
        self.wrapped.PreTension = float(value) if value is not None else 0.0

    @property
    def specify_stiffness_for_unit_length(self) -> 'bool':
        """bool: 'SpecifyStiffnessForUnitLength' is the original name of this property."""

        temp = self.wrapped.SpecifyStiffnessForUnitLength

        if temp is None:
            return False

        return temp

    @specify_stiffness_for_unit_length.setter
    def specify_stiffness_for_unit_length(self, value: 'bool'):
        self.wrapped.SpecifyStiffnessForUnitLength = bool(value) if value is not None else False

    @property
    def stiffness(self) -> 'float':
        """float: 'Stiffness' is the original name of this property."""

        temp = self.wrapped.Stiffness

        if temp is None:
            return 0.0

        return temp

    @stiffness.setter
    def stiffness(self, value: 'float'):
        self.wrapped.Stiffness = float(value) if value is not None else 0.0

    @property
    def stiffness_for_unit_length(self) -> 'float':
        """float: 'StiffnessForUnitLength' is the original name of this property."""

        temp = self.wrapped.StiffnessForUnitLength

        if temp is None:
            return 0.0

        return temp

    @stiffness_for_unit_length.setter
    def stiffness_for_unit_length(self, value: 'float'):
        self.wrapped.StiffnessForUnitLength = float(value) if value is not None else 0.0

    @property
    def type_of_belt(self) -> '_2559.BeltDriveType':
        """BeltDriveType: 'TypeOfBelt' is the original name of this property."""

        temp = self.wrapped.TypeOfBelt

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.SystemModel.PartModel.Couplings.BeltDriveType')
        return constructor.new_from_mastapy('mastapy.system_model.part_model.couplings._2559', 'BeltDriveType')(value) if value is not None else None

    @type_of_belt.setter
    def type_of_belt(self, value: '_2559.BeltDriveType'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.SystemModel.PartModel.Couplings.BeltDriveType')
        self.wrapped.TypeOfBelt = value

    @property
    def belt_connections(self) -> 'List[_2251.BeltConnection]':
        """List[BeltConnection]: 'BeltConnections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BeltConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def pulleys(self) -> 'List[_2572.Pulley]':
        """List[Pulley]: 'Pulleys' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Pulleys

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BeltDrive._Cast_BeltDrive':
        return self._Cast_BeltDrive(self)
