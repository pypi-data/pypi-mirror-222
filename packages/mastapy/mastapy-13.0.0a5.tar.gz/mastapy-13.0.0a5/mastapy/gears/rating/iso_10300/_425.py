"""_425.py

ISO10300RateableMesh
"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy.gears.rating.conical import _544
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO10300_RATEABLE_MESH = python_net_import('SMT.MastaAPI.Gears.Rating.Iso10300', 'ISO10300RateableMesh')

if TYPE_CHECKING:
    from mastapy.gears.rating.virtual_cylindrical_gears import _387


__docformat__ = 'restructuredtext en'
__all__ = ('ISO10300RateableMesh',)


T = TypeVar('T', bound='_387.VirtualCylindricalGearBasic')


class ISO10300RateableMesh(_544.ConicalRateableMesh, Generic[T]):
    """ISO10300RateableMesh

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _ISO10300_RATEABLE_MESH

    class _Cast_ISO10300RateableMesh:
        """Special nested class for casting ISO10300RateableMesh to subclasses."""

        def __init__(self, parent: 'ISO10300RateableMesh'):
            self._parent = parent

        @property
        def conical_rateable_mesh(self):
            return self._parent._cast(_544.ConicalRateableMesh)

        @property
        def rateable_mesh(self):
            from mastapy.gears.rating import _365
            
            return self._parent._cast(_365.RateableMesh)

        @property
        def iso10300_rateable_mesh(self) -> 'ISO10300RateableMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISO10300RateableMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ISO10300RateableMesh._Cast_ISO10300RateableMesh':
        return self._Cast_ISO10300RateableMesh(self)
