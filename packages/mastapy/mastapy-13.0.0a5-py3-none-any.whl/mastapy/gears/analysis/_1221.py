"""_1221.py

GearMeshImplementationDetail
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.analysis import _1218
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_IMPLEMENTATION_DETAIL = python_net_import('SMT.MastaAPI.Gears.Analysis', 'GearMeshImplementationDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshImplementationDetail',)


class GearMeshImplementationDetail(_1218.GearMeshDesignAnalysis):
    """GearMeshImplementationDetail

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_IMPLEMENTATION_DETAIL

    class _Cast_GearMeshImplementationDetail:
        """Special nested class for casting GearMeshImplementationDetail to subclasses."""

        def __init__(self, parent: 'GearMeshImplementationDetail'):
            self._parent = parent

        @property
        def gear_mesh_design_analysis(self):
            return self._parent._cast(_1218.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.AbstractGearMeshAnalysis)

        @property
        def cylindrical_mesh_manufacturing_config(self):
            from mastapy.gears.manufacturing.cylindrical import _619
            
            return self._parent._cast(_619.CylindricalMeshManufacturingConfig)

        @property
        def conical_mesh_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _782
            
            return self._parent._cast(_782.ConicalMeshManufacturingConfig)

        @property
        def conical_mesh_micro_geometry_config(self):
            from mastapy.gears.manufacturing.bevel import _783
            
            return self._parent._cast(_783.ConicalMeshMicroGeometryConfig)

        @property
        def conical_mesh_micro_geometry_config_base(self):
            from mastapy.gears.manufacturing.bevel import _784
            
            return self._parent._cast(_784.ConicalMeshMicroGeometryConfigBase)

        @property
        def face_gear_mesh_micro_geometry(self):
            from mastapy.gears.gear_designs.face import _989
            
            return self._parent._cast(_989.FaceGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1094
            
            return self._parent._cast(_1094.CylindricalGearMeshMicroGeometry)

        @property
        def gear_mesh_fe_model(self):
            from mastapy.gears.fe_model import _1194
            
            return self._parent._cast(_1194.GearMeshFEModel)

        @property
        def cylindrical_gear_mesh_fe_model(self):
            from mastapy.gears.fe_model.cylindrical import _1198
            
            return self._parent._cast(_1198.CylindricalGearMeshFEModel)

        @property
        def conical_mesh_fe_model(self):
            from mastapy.gears.fe_model.conical import _1201
            
            return self._parent._cast(_1201.ConicalMeshFEModel)

        @property
        def gear_mesh_implementation_detail(self) -> 'GearMeshImplementationDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshImplementationDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearMeshImplementationDetail._Cast_GearMeshImplementationDetail':
        return self._Cast_GearMeshImplementationDetail(self)
