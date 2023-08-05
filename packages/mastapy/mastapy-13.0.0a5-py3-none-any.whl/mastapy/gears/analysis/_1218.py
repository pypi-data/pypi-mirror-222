"""_1218.py

GearMeshDesignAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.analysis import _1212
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_DESIGN_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Analysis', 'GearMeshDesignAnalysis')

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1214


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshDesignAnalysis',)


class GearMeshDesignAnalysis(_1212.AbstractGearMeshAnalysis):
    """GearMeshDesignAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_DESIGN_ANALYSIS

    class _Cast_GearMeshDesignAnalysis:
        """Special nested class for casting GearMeshDesignAnalysis to subclasses."""

        def __init__(self, parent: 'GearMeshDesignAnalysis'):
            self._parent = parent

        @property
        def abstract_gear_mesh_analysis(self):
            return self._parent._cast(_1212.AbstractGearMeshAnalysis)

        @property
        def cylindrical_manufactured_gear_mesh_duty_cycle(self):
            from mastapy.gears.manufacturing.cylindrical import _615
            
            return self._parent._cast(_615.CylindricalManufacturedGearMeshDutyCycle)

        @property
        def cylindrical_manufactured_gear_mesh_load_case(self):
            from mastapy.gears.manufacturing.cylindrical import _616
            
            return self._parent._cast(_616.CylindricalManufacturedGearMeshLoadCase)

        @property
        def cylindrical_mesh_manufacturing_config(self):
            from mastapy.gears.manufacturing.cylindrical import _619
            
            return self._parent._cast(_619.CylindricalMeshManufacturingConfig)

        @property
        def conical_mesh_manufacturing_analysis(self):
            from mastapy.gears.manufacturing.bevel import _781
            
            return self._parent._cast(_781.ConicalMeshManufacturingAnalysis)

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
        def mesh_load_case(self):
            from mastapy.gears.load_case import _872
            
            return self._parent._cast(_872.MeshLoadCase)

        @property
        def worm_mesh_load_case(self):
            from mastapy.gears.load_case.worm import _875
            
            return self._parent._cast(_875.WormMeshLoadCase)

        @property
        def face_mesh_load_case(self):
            from mastapy.gears.load_case.face import _878
            
            return self._parent._cast(_878.FaceMeshLoadCase)

        @property
        def cylindrical_mesh_load_case(self):
            from mastapy.gears.load_case.cylindrical import _881
            
            return self._parent._cast(_881.CylindricalMeshLoadCase)

        @property
        def conical_mesh_load_case(self):
            from mastapy.gears.load_case.conical import _884
            
            return self._parent._cast(_884.ConicalMeshLoadCase)

        @property
        def concept_mesh_load_case(self):
            from mastapy.gears.load_case.concept import _887
            
            return self._parent._cast(_887.ConceptMeshLoadCase)

        @property
        def bevel_mesh_load_case(self):
            from mastapy.gears.load_case.bevel import _889
            
            return self._parent._cast(_889.BevelMeshLoadCase)

        @property
        def cylindrical_gear_mesh_tiff_analysis(self):
            from mastapy.gears.gear_two_d_fe_analysis import _891
            
            return self._parent._cast(_891.CylindricalGearMeshTIFFAnalysis)

        @property
        def cylindrical_gear_mesh_tiff_analysis_duty_cycle(self):
            from mastapy.gears.gear_two_d_fe_analysis import _892
            
            return self._parent._cast(_892.CylindricalGearMeshTIFFAnalysisDutyCycle)

        @property
        def face_gear_mesh_micro_geometry(self):
            from mastapy.gears.gear_designs.face import _989
            
            return self._parent._cast(_989.FaceGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1094
            
            return self._parent._cast(_1094.CylindricalGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry_duty_cycle(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1095
            
            return self._parent._cast(_1095.CylindricalGearMeshMicroGeometryDutyCycle)

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
        def gear_mesh_implementation_analysis(self):
            from mastapy.gears.analysis import _1219
            
            return self._parent._cast(_1219.GearMeshImplementationAnalysis)

        @property
        def gear_mesh_implementation_analysis_duty_cycle(self):
            from mastapy.gears.analysis import _1220
            
            return self._parent._cast(_1220.GearMeshImplementationAnalysisDutyCycle)

        @property
        def gear_mesh_implementation_detail(self):
            from mastapy.gears.analysis import _1221
            
            return self._parent._cast(_1221.GearMeshImplementationDetail)

        @property
        def gear_mesh_design_analysis(self) -> 'GearMeshDesignAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshDesignAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_a(self) -> '_1214.GearDesignAnalysis':
        """GearDesignAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b(self) -> '_1214.GearDesignAnalysis':
        """GearDesignAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis':
        return self._Cast_GearMeshDesignAnalysis(self)
