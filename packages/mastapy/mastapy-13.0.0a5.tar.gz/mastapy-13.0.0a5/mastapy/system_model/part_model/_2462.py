"""_2462.py

VirtualComponent
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.part_model import _2447
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'VirtualComponent')


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualComponent',)


class VirtualComponent(_2447.MountableComponent):
    """VirtualComponent

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT

    class _Cast_VirtualComponent:
        """Special nested class for casting VirtualComponent to subclasses."""

        def __init__(self, parent: 'VirtualComponent'):
            self._parent = parent

        @property
        def mountable_component(self):
            return self._parent._cast(_2447.MountableComponent)

        @property
        def component(self):
            from mastapy.system_model.part_model import _2427
            
            return self._parent._cast(_2427.Component)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2451
            
            return self._parent._cast(_2451.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2190
            
            return self._parent._cast(_2190.DesignEntity)

        @property
        def mass_disc(self):
            from mastapy.system_model.part_model import _2445
            
            return self._parent._cast(_2445.MassDisc)

        @property
        def measurement_component(self):
            from mastapy.system_model.part_model import _2446
            
            return self._parent._cast(_2446.MeasurementComponent)

        @property
        def point_load(self):
            from mastapy.system_model.part_model import _2454
            
            return self._parent._cast(_2454.PointLoad)

        @property
        def power_load(self):
            from mastapy.system_model.part_model import _2455
            
            return self._parent._cast(_2455.PowerLoad)

        @property
        def unbalanced_mass(self):
            from mastapy.system_model.part_model import _2460
            
            return self._parent._cast(_2460.UnbalancedMass)

        @property
        def virtual_component(self) -> 'VirtualComponent':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VirtualComponent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'VirtualComponent._Cast_VirtualComponent':
        return self._Cast_VirtualComponent(self)
