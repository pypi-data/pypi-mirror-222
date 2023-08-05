"""_1093.py

CylindricalGearLeadModificationAtProfilePosition
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1092
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_LEAD_MODIFICATION_AT_PROFILE_POSITION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'CylindricalGearLeadModificationAtProfilePosition')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1022


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearLeadModificationAtProfilePosition',)


class CylindricalGearLeadModificationAtProfilePosition(_1092.CylindricalGearLeadModification):
    """CylindricalGearLeadModificationAtProfilePosition

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_LEAD_MODIFICATION_AT_PROFILE_POSITION

    class _Cast_CylindricalGearLeadModificationAtProfilePosition:
        """Special nested class for casting CylindricalGearLeadModificationAtProfilePosition to subclasses."""

        def __init__(self, parent: 'CylindricalGearLeadModificationAtProfilePosition'):
            self._parent = parent

        @property
        def cylindrical_gear_lead_modification(self):
            return self._parent._cast(_1092.CylindricalGearLeadModification)

        @property
        def lead_modification(self):
            from mastapy.gears.micro_geometry import _569
            
            return self._parent._cast(_569.LeadModification)

        @property
        def modification(self):
            from mastapy.gears.micro_geometry import _576
            
            return self._parent._cast(_576.Modification)

        @property
        def cylindrical_gear_lead_modification_at_profile_position(self) -> 'CylindricalGearLeadModificationAtProfilePosition':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearLeadModificationAtProfilePosition.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def position_on_profile_factor(self) -> 'float':
        """float: 'PositionOnProfileFactor' is the original name of this property."""

        temp = self.wrapped.PositionOnProfileFactor

        if temp is None:
            return 0.0

        return temp

    @position_on_profile_factor.setter
    def position_on_profile_factor(self, value: 'float'):
        self.wrapped.PositionOnProfileFactor = float(value) if value is not None else 0.0

    @property
    def profile_measurement(self) -> '_1022.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'ProfileMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileMeasurement

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalGearLeadModificationAtProfilePosition._Cast_CylindricalGearLeadModificationAtProfilePosition':
        return self._Cast_CylindricalGearLeadModificationAtProfilePosition(self)
