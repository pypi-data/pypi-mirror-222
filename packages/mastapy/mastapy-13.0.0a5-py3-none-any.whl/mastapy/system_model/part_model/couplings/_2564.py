"""_2564.py

ConceptCouplingHalf
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.part_model.couplings import _2566
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ConceptCouplingHalf')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingHalf',)


class ConceptCouplingHalf(_2566.CouplingHalf):
    """ConceptCouplingHalf

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF

    class _Cast_ConceptCouplingHalf:
        """Special nested class for casting ConceptCouplingHalf to subclasses."""

        def __init__(self, parent: 'ConceptCouplingHalf'):
            self._parent = parent

        @property
        def coupling_half(self):
            return self._parent._cast(_2566.CouplingHalf)

        @property
        def mountable_component(self):
            from mastapy.system_model.part_model import _2447
            
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
        def concept_coupling_half(self) -> 'ConceptCouplingHalf':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptCouplingHalf.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConceptCouplingHalf._Cast_ConceptCouplingHalf':
        return self._Cast_ConceptCouplingHalf(self)
