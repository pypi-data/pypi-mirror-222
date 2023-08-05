"""_747.py

AxialShaverRedressing
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _761, _748
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AXIAL_SHAVER_REDRESSING = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics', 'AxialShaverRedressing')


__docformat__ = 'restructuredtext en'
__all__ = ('AxialShaverRedressing',)


class AxialShaverRedressing(_761.ShaverRedressing['_748.ConventionalShavingDynamics']):
    """AxialShaverRedressing

    This is a mastapy class.
    """

    TYPE = _AXIAL_SHAVER_REDRESSING

    class _Cast_AxialShaverRedressing:
        """Special nested class for casting AxialShaverRedressing to subclasses."""

        def __init__(self, parent: 'AxialShaverRedressing'):
            self._parent = parent

        @property
        def shaver_redressing(self):
            return self._parent._cast(_761.ShaverRedressing)

        @property
        def axial_shaver_redressing(self) -> 'AxialShaverRedressing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AxialShaverRedressing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AxialShaverRedressing._Cast_AxialShaverRedressing':
        return self._Cast_AxialShaverRedressing(self)
