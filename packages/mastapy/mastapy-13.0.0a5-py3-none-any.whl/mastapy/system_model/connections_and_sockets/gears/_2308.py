"""_2308.py

StraightBevelDiffGearMesh
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2286
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'StraightBevelDiffGearMesh')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel_diff import _963


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearMesh',)


class StraightBevelDiffGearMesh(_2286.BevelGearMesh):
    """StraightBevelDiffGearMesh

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH

    class _Cast_StraightBevelDiffGearMesh:
        """Special nested class for casting StraightBevelDiffGearMesh to subclasses."""

        def __init__(self, parent: 'StraightBevelDiffGearMesh'):
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
        def straight_bevel_diff_gear_mesh(self) -> 'StraightBevelDiffGearMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bevel_gear_mesh_design(self) -> '_963.StraightBevelDiffGearMeshDesign':
        """StraightBevelDiffGearMeshDesign: 'BevelGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def straight_bevel_diff_gear_mesh_design(self) -> '_963.StraightBevelDiffGearMeshDesign':
        """StraightBevelDiffGearMeshDesign: 'StraightBevelDiffGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh':
        return self._Cast_StraightBevelDiffGearMesh(self)
