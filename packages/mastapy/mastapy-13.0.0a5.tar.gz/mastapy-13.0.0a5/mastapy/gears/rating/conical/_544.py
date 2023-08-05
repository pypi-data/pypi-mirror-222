"""_544.py

ConicalRateableMesh
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.rating import _365
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_RATEABLE_MESH = python_net_import('SMT.MastaAPI.Gears.Rating.Conical', 'ConicalRateableMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalRateableMesh',)


class ConicalRateableMesh(_365.RateableMesh):
    """ConicalRateableMesh

    This is a mastapy class.
    """

    TYPE = _CONICAL_RATEABLE_MESH

    class _Cast_ConicalRateableMesh:
        """Special nested class for casting ConicalRateableMesh to subclasses."""

        def __init__(self, parent: 'ConicalRateableMesh'):
            self._parent = parent

        @property
        def rateable_mesh(self):
            return self._parent._cast(_365.RateableMesh)

        @property
        def iso10300_rateable_mesh(self):
            from mastapy.gears.rating.iso_10300 import _425
            
            return self._parent._cast(_425.ISO10300RateableMesh)

        @property
        def hypoid_rateable_mesh(self):
            from mastapy.gears.rating.hypoid.standards import _442
            
            return self._parent._cast(_442.HypoidRateableMesh)

        @property
        def spiral_bevel_rateable_mesh(self):
            from mastapy.gears.rating.bevel.standards import _561
            
            return self._parent._cast(_561.SpiralBevelRateableMesh)

        @property
        def agma_gleason_conical_rateable_mesh(self):
            from mastapy.gears.rating.agma_gleason_conical import _565
            
            return self._parent._cast(_565.AGMAGleasonConicalRateableMesh)

        @property
        def conical_rateable_mesh(self) -> 'ConicalRateableMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalRateableMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalRateableMesh._Cast_ConicalRateableMesh':
        return self._Cast_ConicalRateableMesh(self)
