"""_1219.py

GearMeshImplementationAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.analysis import _1218
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_IMPLEMENTATION_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Analysis', 'GearMeshImplementationAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshImplementationAnalysis',)


class GearMeshImplementationAnalysis(_1218.GearMeshDesignAnalysis):
    """GearMeshImplementationAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_IMPLEMENTATION_ANALYSIS

    class _Cast_GearMeshImplementationAnalysis:
        """Special nested class for casting GearMeshImplementationAnalysis to subclasses."""

        def __init__(self, parent: 'GearMeshImplementationAnalysis'):
            self._parent = parent

        @property
        def gear_mesh_design_analysis(self):
            return self._parent._cast(_1218.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.AbstractGearMeshAnalysis)

        @property
        def cylindrical_manufactured_gear_mesh_load_case(self):
            from mastapy.gears.manufacturing.cylindrical import _616
            
            return self._parent._cast(_616.CylindricalManufacturedGearMeshLoadCase)

        @property
        def conical_mesh_manufacturing_analysis(self):
            from mastapy.gears.manufacturing.bevel import _781
            
            return self._parent._cast(_781.ConicalMeshManufacturingAnalysis)

        @property
        def gear_mesh_load_distribution_analysis(self):
            from mastapy.gears.ltca import _838
            
            return self._parent._cast(_838.GearMeshLoadDistributionAnalysis)

        @property
        def cylindrical_gear_mesh_load_distribution_analysis(self):
            from mastapy.gears.ltca.cylindrical import _854
            
            return self._parent._cast(_854.CylindricalGearMeshLoadDistributionAnalysis)

        @property
        def conical_mesh_load_distribution_analysis(self):
            from mastapy.gears.ltca.conical import _867
            
            return self._parent._cast(_867.ConicalMeshLoadDistributionAnalysis)

        @property
        def gear_mesh_implementation_analysis(self) -> 'GearMeshImplementationAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshImplementationAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis':
        return self._Cast_GearMeshImplementationAnalysis(self)
