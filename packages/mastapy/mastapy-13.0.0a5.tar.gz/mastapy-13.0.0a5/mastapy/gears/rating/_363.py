"""_363.py

MeshDutyCycleRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _351
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MESH_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'MeshDutyCycleRating')

if TYPE_CHECKING:
    from mastapy.gears.rating import _356


__docformat__ = 'restructuredtext en'
__all__ = ('MeshDutyCycleRating',)


class MeshDutyCycleRating(_351.AbstractGearMeshRating):
    """MeshDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _MESH_DUTY_CYCLE_RATING

    class _Cast_MeshDutyCycleRating:
        """Special nested class for casting MeshDutyCycleRating to subclasses."""

        def __init__(self, parent: 'MeshDutyCycleRating'):
            self._parent = parent

        @property
        def abstract_gear_mesh_rating(self):
            return self._parent._cast(_351.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.AbstractGearMeshAnalysis)

        @property
        def worm_mesh_duty_cycle_rating(self):
            from mastapy.gears.rating.worm import _375
            
            return self._parent._cast(_375.WormMeshDutyCycleRating)

        @property
        def face_gear_mesh_duty_cycle_rating(self):
            from mastapy.gears.rating.face import _444
            
            return self._parent._cast(_444.FaceGearMeshDutyCycleRating)

        @property
        def cylindrical_mesh_duty_cycle_rating(self):
            from mastapy.gears.rating.cylindrical import _464
            
            return self._parent._cast(_464.CylindricalMeshDutyCycleRating)

        @property
        def conical_mesh_duty_cycle_rating(self):
            from mastapy.gears.rating.conical import _541
            
            return self._parent._cast(_541.ConicalMeshDutyCycleRating)

        @property
        def concept_gear_mesh_duty_cycle_rating(self):
            from mastapy.gears.rating.concept import _546
            
            return self._parent._cast(_546.ConceptGearMeshDutyCycleRating)

        @property
        def mesh_duty_cycle_rating(self) -> 'MeshDutyCycleRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MeshDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def energy_loss(self) -> 'float':
        """float: 'EnergyLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EnergyLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_efficiency(self) -> 'float':
        """float: 'MeshEfficiency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshEfficiency

        if temp is None:
            return 0.0

        return temp

    @property
    def total_energy(self) -> 'float':
        """float: 'TotalEnergy' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalEnergy

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_duty_cycle_ratings(self) -> 'List[_356.GearDutyCycleRating]':
        """List[GearDutyCycleRating]: 'GearDutyCycleRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'MeshDutyCycleRating._Cast_MeshDutyCycleRating':
        return self._Cast_MeshDutyCycleRating(self)
