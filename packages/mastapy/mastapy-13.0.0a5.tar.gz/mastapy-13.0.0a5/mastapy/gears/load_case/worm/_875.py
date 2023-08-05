"""_875.py

WormMeshLoadCase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.load_case import _872
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Worm', 'WormMeshLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('WormMeshLoadCase',)


class WormMeshLoadCase(_872.MeshLoadCase):
    """WormMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _WORM_MESH_LOAD_CASE

    class _Cast_WormMeshLoadCase:
        """Special nested class for casting WormMeshLoadCase to subclasses."""

        def __init__(self, parent: 'WormMeshLoadCase'):
            self._parent = parent

        @property
        def mesh_load_case(self):
            return self._parent._cast(_872.MeshLoadCase)

        @property
        def gear_mesh_design_analysis(self):
            from mastapy.gears.analysis import _1218
            
            return self._parent._cast(_1218.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.AbstractGearMeshAnalysis)

        @property
        def worm_mesh_load_case(self) -> 'WormMeshLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormMeshLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'WormMeshLoadCase._Cast_WormMeshLoadCase':
        return self._Cast_WormMeshLoadCase(self)
