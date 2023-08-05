"""_889.py

BevelMeshLoadCase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.load_case.conical import _884
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Bevel', 'BevelMeshLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelMeshLoadCase',)


class BevelMeshLoadCase(_884.ConicalMeshLoadCase):
    """BevelMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_MESH_LOAD_CASE

    class _Cast_BevelMeshLoadCase:
        """Special nested class for casting BevelMeshLoadCase to subclasses."""

        def __init__(self, parent: 'BevelMeshLoadCase'):
            self._parent = parent

        @property
        def conical_mesh_load_case(self):
            return self._parent._cast(_884.ConicalMeshLoadCase)

        @property
        def mesh_load_case(self):
            from mastapy.gears.load_case import _872
            
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
        def bevel_mesh_load_case(self) -> 'BevelMeshLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelMeshLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BevelMeshLoadCase._Cast_BevelMeshLoadCase':
        return self._Cast_BevelMeshLoadCase(self)
