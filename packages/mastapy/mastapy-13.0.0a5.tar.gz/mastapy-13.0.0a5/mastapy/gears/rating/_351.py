"""_351.py

AbstractGearMeshRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.analysis import _1212
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'AbstractGearMeshRating')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractGearMeshRating',)


class AbstractGearMeshRating(_1212.AbstractGearMeshAnalysis):
    """AbstractGearMeshRating

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_MESH_RATING

    class _Cast_AbstractGearMeshRating:
        """Special nested class for casting AbstractGearMeshRating to subclasses."""

        def __init__(self, parent: 'AbstractGearMeshRating'):
            self._parent = parent

        @property
        def abstract_gear_mesh_analysis(self):
            return self._parent._cast(_1212.AbstractGearMeshAnalysis)

        @property
        def gear_mesh_rating(self):
            from mastapy.gears.rating import _358
            
            return self._parent._cast(_358.GearMeshRating)

        @property
        def mesh_duty_cycle_rating(self):
            from mastapy.gears.rating import _363
            
            return self._parent._cast(_363.MeshDutyCycleRating)

        @property
        def zerol_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.zerol_bevel import _367
            
            return self._parent._cast(_367.ZerolBevelGearMeshRating)

        @property
        def worm_gear_mesh_rating(self):
            from mastapy.gears.rating.worm import _371
            
            return self._parent._cast(_371.WormGearMeshRating)

        @property
        def worm_mesh_duty_cycle_rating(self):
            from mastapy.gears.rating.worm import _375
            
            return self._parent._cast(_375.WormMeshDutyCycleRating)

        @property
        def straight_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.straight_bevel import _393
            
            return self._parent._cast(_393.StraightBevelGearMeshRating)

        @property
        def straight_bevel_diff_gear_mesh_rating(self):
            from mastapy.gears.rating.straight_bevel_diff import _396
            
            return self._parent._cast(_396.StraightBevelDiffGearMeshRating)

        @property
        def spiral_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.spiral_bevel import _400
            
            return self._parent._cast(_400.SpiralBevelGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _403
            
            return self._parent._cast(_403.KlingelnbergCycloPalloidSpiralBevelGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(self):
            from mastapy.gears.rating.klingelnberg_hypoid import _406
            
            return self._parent._cast(_406.KlingelnbergCycloPalloidHypoidGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(self):
            from mastapy.gears.rating.klingelnberg_conical import _409
            
            return self._parent._cast(_409.KlingelnbergCycloPalloidConicalGearMeshRating)

        @property
        def hypoid_gear_mesh_rating(self):
            from mastapy.gears.rating.hypoid import _436
            
            return self._parent._cast(_436.HypoidGearMeshRating)

        @property
        def face_gear_mesh_duty_cycle_rating(self):
            from mastapy.gears.rating.face import _444
            
            return self._parent._cast(_444.FaceGearMeshDutyCycleRating)

        @property
        def face_gear_mesh_rating(self):
            from mastapy.gears.rating.face import _445
            
            return self._parent._cast(_445.FaceGearMeshRating)

        @property
        def cylindrical_gear_mesh_rating(self):
            from mastapy.gears.rating.cylindrical import _456
            
            return self._parent._cast(_456.CylindricalGearMeshRating)

        @property
        def cylindrical_mesh_duty_cycle_rating(self):
            from mastapy.gears.rating.cylindrical import _464
            
            return self._parent._cast(_464.CylindricalMeshDutyCycleRating)

        @property
        def conical_gear_mesh_rating(self):
            from mastapy.gears.rating.conical import _536
            
            return self._parent._cast(_536.ConicalGearMeshRating)

        @property
        def conical_mesh_duty_cycle_rating(self):
            from mastapy.gears.rating.conical import _541
            
            return self._parent._cast(_541.ConicalMeshDutyCycleRating)

        @property
        def concept_gear_mesh_duty_cycle_rating(self):
            from mastapy.gears.rating.concept import _546
            
            return self._parent._cast(_546.ConceptGearMeshDutyCycleRating)

        @property
        def concept_gear_mesh_rating(self):
            from mastapy.gears.rating.concept import _547
            
            return self._parent._cast(_547.ConceptGearMeshRating)

        @property
        def bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.bevel import _551
            
            return self._parent._cast(_551.BevelGearMeshRating)

        @property
        def agma_gleason_conical_gear_mesh_rating(self):
            from mastapy.gears.rating.agma_gleason_conical import _562
            
            return self._parent._cast(_562.AGMAGleasonConicalGearMeshRating)

        @property
        def abstract_gear_mesh_rating(self) -> 'AbstractGearMeshRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def normalized_safety_factor_for_fatigue(self) -> 'float':
        """float: 'NormalizedSafetyFactorForFatigue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalizedSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_safety_factor_for_static(self) -> 'float':
        """float: 'NormalizedSafetyFactorForStatic' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalizedSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'AbstractGearMeshRating._Cast_AbstractGearMeshRating':
        return self._Cast_AbstractGearMeshRating(self)
