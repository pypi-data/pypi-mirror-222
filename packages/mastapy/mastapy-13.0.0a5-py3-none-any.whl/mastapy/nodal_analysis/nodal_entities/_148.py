"""_148.py

SurfaceToSurfaceContactStiffnessEntity
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.nodal_analysis.nodal_entities import _125
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SURFACE_TO_SURFACE_CONTACT_STIFFNESS_ENTITY = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'SurfaceToSurfaceContactStiffnessEntity')

if TYPE_CHECKING:
    from mastapy.math_utility.stiffness_calculators import _1528


__docformat__ = 'restructuredtext en'
__all__ = ('SurfaceToSurfaceContactStiffnessEntity',)


class SurfaceToSurfaceContactStiffnessEntity(_125.ArbitraryNodalComponent):
    """SurfaceToSurfaceContactStiffnessEntity

    This is a mastapy class.
    """

    TYPE = _SURFACE_TO_SURFACE_CONTACT_STIFFNESS_ENTITY

    class _Cast_SurfaceToSurfaceContactStiffnessEntity:
        """Special nested class for casting SurfaceToSurfaceContactStiffnessEntity to subclasses."""

        def __init__(self, parent: 'SurfaceToSurfaceContactStiffnessEntity'):
            self._parent = parent

        @property
        def arbitrary_nodal_component(self):
            return self._parent._cast(_125.ArbitraryNodalComponent)

        @property
        def nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _142
            
            return self._parent._cast(_142.NodalComponent)

        @property
        def nodal_entity(self):
            from mastapy.nodal_analysis.nodal_entities import _144
            
            return self._parent._cast(_144.NodalEntity)

        @property
        def surface_to_surface_contact_stiffness_entity(self) -> 'SurfaceToSurfaceContactStiffnessEntity':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SurfaceToSurfaceContactStiffnessEntity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact(self) -> '_1528.SurfaceToSurfaceContact':
        """SurfaceToSurfaceContact: 'Contact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Contact

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SurfaceToSurfaceContactStiffnessEntity._Cast_SurfaceToSurfaceContactStiffnessEntity':
        return self._Cast_SurfaceToSurfaceContactStiffnessEntity(self)
