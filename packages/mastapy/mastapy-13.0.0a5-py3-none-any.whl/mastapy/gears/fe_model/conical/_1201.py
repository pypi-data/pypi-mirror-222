"""_1201.py

ConicalMeshFEModel
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.fe_model import _1194
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_FE_MODEL = python_net_import('SMT.MastaAPI.Gears.FEModel.Conical', 'ConicalMeshFEModel')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshFEModel',)


class ConicalMeshFEModel(_1194.GearMeshFEModel):
    """ConicalMeshFEModel

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_FE_MODEL

    class _Cast_ConicalMeshFEModel:
        """Special nested class for casting ConicalMeshFEModel to subclasses."""

        def __init__(self, parent: 'ConicalMeshFEModel'):
            self._parent = parent

        @property
        def gear_mesh_fe_model(self):
            return self._parent._cast(_1194.GearMeshFEModel)

        @property
        def gear_mesh_implementation_detail(self):
            from mastapy.gears.analysis import _1221
            
            return self._parent._cast(_1221.GearMeshImplementationDetail)

        @property
        def gear_mesh_design_analysis(self):
            from mastapy.gears.analysis import _1218
            
            return self._parent._cast(_1218.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.AbstractGearMeshAnalysis)

        @property
        def conical_mesh_fe_model(self) -> 'ConicalMeshFEModel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalMeshFEModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalMeshFEModel._Cast_ConicalMeshFEModel':
        return self._Cast_ConicalMeshFEModel(self)
