﻿"""_390.py

VirtualCylindricalGearSet
"""
from __future__ import annotations

from typing import (
    TYPE_CHECKING, List, TypeVar, Generic
)

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_CYLINDRICAL_GEAR_SET = python_net_import('SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears', 'VirtualCylindricalGearSet')

if TYPE_CHECKING:
    from mastapy.gears.rating.virtual_cylindrical_gears import _387


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualCylindricalGearSet',)


T = TypeVar('T', bound='_387.VirtualCylindricalGearBasic')


class VirtualCylindricalGearSet(_0.APIBase, Generic[T]):
    """VirtualCylindricalGearSet

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _VIRTUAL_CYLINDRICAL_GEAR_SET

    class _Cast_VirtualCylindricalGearSet:
        """Special nested class for casting VirtualCylindricalGearSet to subclasses."""

        def __init__(self, parent: 'VirtualCylindricalGearSet'):
            self._parent = parent

        @property
        def bevel_virtual_cylindrical_gear_set_iso10300_method_b1(self):
            from mastapy.gears.rating.virtual_cylindrical_gears import _377
            
            return self._parent._cast(_377.BevelVirtualCylindricalGearSetISO10300MethodB1)

        @property
        def bevel_virtual_cylindrical_gear_set_iso10300_method_b2(self):
            from mastapy.gears.rating.virtual_cylindrical_gears import _378
            
            return self._parent._cast(_378.BevelVirtualCylindricalGearSetISO10300MethodB2)

        @property
        def hypoid_virtual_cylindrical_gear_set_iso10300_method_b1(self):
            from mastapy.gears.rating.virtual_cylindrical_gears import _380
            
            return self._parent._cast(_380.HypoidVirtualCylindricalGearSetISO10300MethodB1)

        @property
        def hypoid_virtual_cylindrical_gear_set_iso10300_method_b2(self):
            from mastapy.gears.rating.virtual_cylindrical_gears import _381
            
            return self._parent._cast(_381.HypoidVirtualCylindricalGearSetISO10300MethodB2)

        @property
        def klingelnberg_virtual_cylindrical_gear_set(self):
            from mastapy.gears.rating.virtual_cylindrical_gears import _385
            
            return self._parent._cast(_385.KlingelnbergVirtualCylindricalGearSet)

        @property
        def virtual_cylindrical_gear_set_iso10300_method_b1(self):
            from mastapy.gears.rating.virtual_cylindrical_gears import _391
            
            return self._parent._cast(_391.VirtualCylindricalGearSetISO10300MethodB1)

        @property
        def virtual_cylindrical_gear_set_iso10300_method_b2(self):
            from mastapy.gears.rating.virtual_cylindrical_gears import _392
            
            return self._parent._cast(_392.VirtualCylindricalGearSetISO10300MethodB2)

        @property
        def virtual_cylindrical_gear_set(self) -> 'VirtualCylindricalGearSet':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VirtualCylindricalGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def effective_face_width_of_virtual_cylindrical_gears(self) -> 'float':
        """float: 'EffectiveFaceWidthOfVirtualCylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EffectiveFaceWidthOfVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def face_contact_ratio_transverse_for_virtual_cylindrical_gears(self) -> 'float':
        """float: 'FaceContactRatioTransverseForVirtualCylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceContactRatioTransverseForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width_of_virtual_cylindrical_gears(self) -> 'float':
        """float: 'FaceWidthOfVirtualCylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceWidthOfVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_contact_ratio_normal_for_virtual_cylindrical_gears(self) -> 'float':
        """float: 'TransverseContactRatioNormalForVirtualCylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseContactRatioNormalForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_contact_ratio_for_virtual_cylindrical_gears(self) -> 'float':
        """float: 'TransverseContactRatioForVirtualCylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseContactRatioForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def virtual_centre_distance(self) -> 'float':
        """float: 'VirtualCentreDistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VirtualCentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def virtual_contact_ratio_transverse_for_virtual_cylindrical_gears(self) -> 'float':
        """float: 'VirtualContactRatioTransverseForVirtualCylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VirtualContactRatioTransverseForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def virtual_pinion(self) -> 'T':
        """T: 'VirtualPinion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VirtualPinion

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def virtual_wheel(self) -> 'T':
        """T: 'VirtualWheel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VirtualWheel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def virtual_cylindrical_gears(self) -> 'List[T]':
        """List[T]: 'VirtualCylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VirtualCylindricalGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'VirtualCylindricalGearSet._Cast_VirtualCylindricalGearSet':
        return self._Cast_VirtualCylindricalGearSet(self)
