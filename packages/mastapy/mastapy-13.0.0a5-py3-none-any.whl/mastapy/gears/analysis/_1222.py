"""_1222.py

GearSetDesignAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.analysis import _1213
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_DESIGN_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Analysis', 'GearSetDesignAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetDesignAnalysis',)


class GearSetDesignAnalysis(_1213.AbstractGearSetAnalysis):
    """GearSetDesignAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_DESIGN_ANALYSIS

    class _Cast_GearSetDesignAnalysis:
        """Special nested class for casting GearSetDesignAnalysis to subclasses."""

        def __init__(self, parent: 'GearSetDesignAnalysis'):
            self._parent = parent

        @property
        def abstract_gear_set_analysis(self):
            return self._parent._cast(_1213.AbstractGearSetAnalysis)

        @property
        def cylindrical_manufactured_gear_set_duty_cycle(self):
            from mastapy.gears.manufacturing.cylindrical import _617
            
            return self._parent._cast(_617.CylindricalManufacturedGearSetDutyCycle)

        @property
        def cylindrical_manufactured_gear_set_load_case(self):
            from mastapy.gears.manufacturing.cylindrical import _618
            
            return self._parent._cast(_618.CylindricalManufacturedGearSetLoadCase)

        @property
        def cylindrical_set_manufacturing_config(self):
            from mastapy.gears.manufacturing.cylindrical import _622
            
            return self._parent._cast(_622.CylindricalSetManufacturingConfig)

        @property
        def conical_set_manufacturing_analysis(self):
            from mastapy.gears.manufacturing.bevel import _787
            
            return self._parent._cast(_787.ConicalSetManufacturingAnalysis)

        @property
        def conical_set_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _788
            
            return self._parent._cast(_788.ConicalSetManufacturingConfig)

        @property
        def conical_set_micro_geometry_config(self):
            from mastapy.gears.manufacturing.bevel import _789
            
            return self._parent._cast(_789.ConicalSetMicroGeometryConfig)

        @property
        def conical_set_micro_geometry_config_base(self):
            from mastapy.gears.manufacturing.bevel import _790
            
            return self._parent._cast(_790.ConicalSetMicroGeometryConfigBase)

        @property
        def gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca import _843
            
            return self._parent._cast(_843.GearSetLoadDistributionAnalysis)

        @property
        def cylindrical_gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca.cylindrical import _857
            
            return self._parent._cast(_857.CylindricalGearSetLoadDistributionAnalysis)

        @property
        def face_gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca.cylindrical import _859
            
            return self._parent._cast(_859.FaceGearSetLoadDistributionAnalysis)

        @property
        def conical_gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca.conical import _865
            
            return self._parent._cast(_865.ConicalGearSetLoadDistributionAnalysis)

        @property
        def gear_set_load_case_base(self):
            from mastapy.gears.load_case import _871
            
            return self._parent._cast(_871.GearSetLoadCaseBase)

        @property
        def worm_gear_set_load_case(self):
            from mastapy.gears.load_case.worm import _874
            
            return self._parent._cast(_874.WormGearSetLoadCase)

        @property
        def face_gear_set_load_case(self):
            from mastapy.gears.load_case.face import _877
            
            return self._parent._cast(_877.FaceGearSetLoadCase)

        @property
        def cylindrical_gear_set_load_case(self):
            from mastapy.gears.load_case.cylindrical import _880
            
            return self._parent._cast(_880.CylindricalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(self):
            from mastapy.gears.load_case.conical import _883
            
            return self._parent._cast(_883.ConicalGearSetLoadCase)

        @property
        def concept_gear_set_load_case(self):
            from mastapy.gears.load_case.concept import _886
            
            return self._parent._cast(_886.ConceptGearSetLoadCase)

        @property
        def bevel_set_load_case(self):
            from mastapy.gears.load_case.bevel import _890
            
            return self._parent._cast(_890.BevelSetLoadCase)

        @property
        def cylindrical_gear_set_tiff_analysis(self):
            from mastapy.gears.gear_two_d_fe_analysis import _893
            
            return self._parent._cast(_893.CylindricalGearSetTIFFAnalysis)

        @property
        def cylindrical_gear_set_tiff_analysis_duty_cycle(self):
            from mastapy.gears.gear_two_d_fe_analysis import _894
            
            return self._parent._cast(_894.CylindricalGearSetTIFFAnalysisDutyCycle)

        @property
        def face_gear_set_micro_geometry(self):
            from mastapy.gears.gear_designs.face import _993
            
            return self._parent._cast(_993.FaceGearSetMicroGeometry)

        @property
        def cylindrical_gear_set_micro_geometry(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1103
            
            return self._parent._cast(_1103.CylindricalGearSetMicroGeometry)

        @property
        def cylindrical_gear_set_micro_geometry_duty_cycle(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1104
            
            return self._parent._cast(_1104.CylindricalGearSetMicroGeometryDutyCycle)

        @property
        def gear_set_fe_model(self):
            from mastapy.gears.fe_model import _1196
            
            return self._parent._cast(_1196.GearSetFEModel)

        @property
        def cylindrical_gear_set_fe_model(self):
            from mastapy.gears.fe_model.cylindrical import _1199
            
            return self._parent._cast(_1199.CylindricalGearSetFEModel)

        @property
        def conical_set_fe_model(self):
            from mastapy.gears.fe_model.conical import _1202
            
            return self._parent._cast(_1202.ConicalSetFEModel)

        @property
        def gear_set_implementation_analysis(self):
            from mastapy.gears.analysis import _1224
            
            return self._parent._cast(_1224.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_abstract(self):
            from mastapy.gears.analysis import _1225
            
            return self._parent._cast(_1225.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_implementation_analysis_duty_cycle(self):
            from mastapy.gears.analysis import _1226
            
            return self._parent._cast(_1226.GearSetImplementationAnalysisDutyCycle)

        @property
        def gear_set_implementation_detail(self):
            from mastapy.gears.analysis import _1227
            
            return self._parent._cast(_1227.GearSetImplementationDetail)

        @property
        def gear_set_design_analysis(self) -> 'GearSetDesignAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetDesignAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearSetDesignAnalysis._Cast_GearSetDesignAnalysis':
        return self._Cast_GearSetDesignAnalysis(self)
