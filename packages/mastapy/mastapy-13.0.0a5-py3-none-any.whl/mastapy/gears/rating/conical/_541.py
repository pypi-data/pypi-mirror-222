"""_541.py

ConicalMeshDutyCycleRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _363
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Conical', 'ConicalMeshDutyCycleRating')

if TYPE_CHECKING:
    from mastapy.gears.rating.conical import _536


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshDutyCycleRating',)


class ConicalMeshDutyCycleRating(_363.MeshDutyCycleRating):
    """ConicalMeshDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_DUTY_CYCLE_RATING

    class _Cast_ConicalMeshDutyCycleRating:
        """Special nested class for casting ConicalMeshDutyCycleRating to subclasses."""

        def __init__(self, parent: 'ConicalMeshDutyCycleRating'):
            self._parent = parent

        @property
        def mesh_duty_cycle_rating(self):
            return self._parent._cast(_363.MeshDutyCycleRating)

        @property
        def abstract_gear_mesh_rating(self):
            from mastapy.gears.rating import _351
            
            return self._parent._cast(_351.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.AbstractGearMeshAnalysis)

        @property
        def conical_mesh_duty_cycle_rating(self) -> 'ConicalMeshDutyCycleRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalMeshDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_mesh_ratings(self) -> 'List[_536.ConicalGearMeshRating]':
        """List[ConicalGearMeshRating]: 'ConicalMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalMeshDutyCycleRating._Cast_ConicalMeshDutyCycleRating':
        return self._Cast_ConicalMeshDutyCycleRating(self)
