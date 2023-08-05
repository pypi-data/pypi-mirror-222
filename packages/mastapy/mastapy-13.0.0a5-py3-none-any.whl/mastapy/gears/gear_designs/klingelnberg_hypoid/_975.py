"""_975.py

KlingelnbergCycloPalloidHypoidGearMeshDesign
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.klingelnberg_conical import _979
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.KlingelnbergHypoid', 'KlingelnbergCycloPalloidHypoidGearMeshDesign')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _976, _974, _977


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearMeshDesign',)


class KlingelnbergCycloPalloidHypoidGearMeshDesign(_979.KlingelnbergConicalGearMeshDesign):
    """KlingelnbergCycloPalloidHypoidGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_DESIGN

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshDesign:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshDesign to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGearMeshDesign'):
            self._parent = parent

        @property
        def klingelnberg_conical_gear_mesh_design(self):
            return self._parent._cast(_979.KlingelnbergConicalGearMeshDesign)

        @property
        def conical_gear_mesh_design(self):
            from mastapy.gears.gear_designs.conical import _1151
            
            return self._parent._cast(_1151.ConicalGearMeshDesign)

        @property
        def gear_mesh_design(self):
            from mastapy.gears.gear_designs import _946
            
            return self._parent._cast(_946.GearMeshDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _945
            
            return self._parent._cast(_945.GearDesignComponent)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_design(self) -> 'KlingelnbergCycloPalloidHypoidGearMeshDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearMeshDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> '_976.KlingelnbergCycloPalloidHypoidGearSetDesign':
        """KlingelnbergCycloPalloidHypoidGearSetDesign: 'KlingelnbergCycloPalloidHypoidGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears(self) -> 'List[_974.KlingelnbergCycloPalloidHypoidGearDesign]':
        """List[KlingelnbergCycloPalloidHypoidGearDesign]: 'KlingelnbergCycloPalloidHypoidGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshed_gears(self) -> 'List[_977.KlingelnbergCycloPalloidHypoidMeshedGearDesign]':
        """List[KlingelnbergCycloPalloidHypoidMeshedGearDesign]: 'KlingelnbergCycloPalloidHypoidMeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGearMeshDesign._Cast_KlingelnbergCycloPalloidHypoidGearMeshDesign':
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshDesign(self)
