"""_2284.py

BevelDifferentialGearMesh
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2286
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'BevelDifferentialGearMesh')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.bevel import _1177


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearMesh',)


class BevelDifferentialGearMesh(_2286.BevelGearMesh):
    """BevelDifferentialGearMesh

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH

    class _Cast_BevelDifferentialGearMesh:
        """Special nested class for casting BevelDifferentialGearMesh to subclasses."""

        def __init__(self, parent: 'BevelDifferentialGearMesh'):
            self._parent = parent

        @property
        def bevel_gear_mesh(self):
            return self._parent._cast(_2286.BevelGearMesh)

        @property
        def agma_gleason_conical_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2282
            
            return self._parent._cast(_2282.AGMAGleasonConicalGearMesh)

        @property
        def conical_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2290
            
            return self._parent._cast(_2290.ConicalGearMesh)

        @property
        def gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2296
            
            return self._parent._cast(_2296.GearMesh)

        @property
        def inter_mountable_component_connection(self):
            from mastapy.system_model.connections_and_sockets import _2264
            
            return self._parent._cast(_2264.InterMountableComponentConnection)

        @property
        def connection(self):
            from mastapy.system_model.connections_and_sockets import _2255
            
            return self._parent._cast(_2255.Connection)

        @property
        def design_entity(self):
            from mastapy.system_model import _2190
            
            return self._parent._cast(_2190.DesignEntity)

        @property
        def bevel_differential_gear_mesh(self) -> 'BevelDifferentialGearMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bevel_gear_mesh_design(self) -> '_1177.BevelGearMeshDesign':
        """BevelGearMeshDesign: 'BevelGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh':
        return self._Cast_BevelDifferentialGearMesh(self)
