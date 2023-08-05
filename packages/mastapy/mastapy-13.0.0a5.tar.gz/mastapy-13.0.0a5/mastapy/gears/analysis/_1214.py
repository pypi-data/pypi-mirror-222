"""_1214.py

GearDesignAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.analysis import _1211
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_DESIGN_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Analysis', 'GearDesignAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearDesignAnalysis',)


class GearDesignAnalysis(_1211.AbstractGearAnalysis):
    """GearDesignAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_DESIGN_ANALYSIS

    class _Cast_GearDesignAnalysis:
        """Special nested class for casting GearDesignAnalysis to subclasses."""

        def __init__(self, parent: 'GearDesignAnalysis'):
            self._parent = parent

        @property
        def abstract_gear_analysis(self):
            return self._parent._cast(_1211.AbstractGearAnalysis)

        @property
        def cylindrical_gear_manufacturing_config(self):
            from mastapy.gears.manufacturing.cylindrical import _609
            
            return self._parent._cast(_609.CylindricalGearManufacturingConfig)

        @property
        def cylindrical_manufactured_gear_duty_cycle(self):
            from mastapy.gears.manufacturing.cylindrical import _613
            
            return self._parent._cast(_613.CylindricalManufacturedGearDutyCycle)

        @property
        def cylindrical_manufactured_gear_load_case(self):
            from mastapy.gears.manufacturing.cylindrical import _614
            
            return self._parent._cast(_614.CylindricalManufacturedGearLoadCase)

        @property
        def conical_gear_manufacturing_analysis(self):
            from mastapy.gears.manufacturing.bevel import _772
            
            return self._parent._cast(_772.ConicalGearManufacturingAnalysis)

        @property
        def conical_gear_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _773
            
            return self._parent._cast(_773.ConicalGearManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config(self):
            from mastapy.gears.manufacturing.bevel import _774
            
            return self._parent._cast(_774.ConicalGearMicroGeometryConfig)

        @property
        def conical_gear_micro_geometry_config_base(self):
            from mastapy.gears.manufacturing.bevel import _775
            
            return self._parent._cast(_775.ConicalGearMicroGeometryConfigBase)

        @property
        def conical_pinion_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _785
            
            return self._parent._cast(_785.ConicalPinionManufacturingConfig)

        @property
        def conical_pinion_micro_geometry_config(self):
            from mastapy.gears.manufacturing.bevel import _786
            
            return self._parent._cast(_786.ConicalPinionMicroGeometryConfig)

        @property
        def conical_wheel_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _791
            
            return self._parent._cast(_791.ConicalWheelManufacturingConfig)

        @property
        def gear_load_distribution_analysis(self):
            from mastapy.gears.ltca import _837
            
            return self._parent._cast(_837.GearLoadDistributionAnalysis)

        @property
        def cylindrical_gear_load_distribution_analysis(self):
            from mastapy.gears.ltca.cylindrical import _853
            
            return self._parent._cast(_853.CylindricalGearLoadDistributionAnalysis)

        @property
        def conical_gear_load_distribution_analysis(self):
            from mastapy.gears.ltca.conical import _864
            
            return self._parent._cast(_864.ConicalGearLoadDistributionAnalysis)

        @property
        def gear_load_case_base(self):
            from mastapy.gears.load_case import _870
            
            return self._parent._cast(_870.GearLoadCaseBase)

        @property
        def worm_gear_load_case(self):
            from mastapy.gears.load_case.worm import _873
            
            return self._parent._cast(_873.WormGearLoadCase)

        @property
        def face_gear_load_case(self):
            from mastapy.gears.load_case.face import _876
            
            return self._parent._cast(_876.FaceGearLoadCase)

        @property
        def cylindrical_gear_load_case(self):
            from mastapy.gears.load_case.cylindrical import _879
            
            return self._parent._cast(_879.CylindricalGearLoadCase)

        @property
        def conical_gear_load_case(self):
            from mastapy.gears.load_case.conical import _882
            
            return self._parent._cast(_882.ConicalGearLoadCase)

        @property
        def concept_gear_load_case(self):
            from mastapy.gears.load_case.concept import _885
            
            return self._parent._cast(_885.ConceptGearLoadCase)

        @property
        def bevel_load_case(self):
            from mastapy.gears.load_case.bevel import _888
            
            return self._parent._cast(_888.BevelLoadCase)

        @property
        def cylindrical_gear_tiff_analysis(self):
            from mastapy.gears.gear_two_d_fe_analysis import _895
            
            return self._parent._cast(_895.CylindricalGearTIFFAnalysis)

        @property
        def cylindrical_gear_tiff_analysis_duty_cycle(self):
            from mastapy.gears.gear_two_d_fe_analysis import _896
            
            return self._parent._cast(_896.CylindricalGearTIFFAnalysisDutyCycle)

        @property
        def face_gear_micro_geometry(self):
            from mastapy.gears.gear_designs.face import _990
            
            return self._parent._cast(_990.FaceGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1096
            
            return self._parent._cast(_1096.CylindricalGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry_base(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1097
            
            return self._parent._cast(_1097.CylindricalGearMicroGeometryBase)

        @property
        def cylindrical_gear_micro_geometry_duty_cycle(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1098
            
            return self._parent._cast(_1098.CylindricalGearMicroGeometryDutyCycle)

        @property
        def cylindrical_gear_micro_geometry_per_tooth(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1100
            
            return self._parent._cast(_1100.CylindricalGearMicroGeometryPerTooth)

        @property
        def gear_fe_model(self):
            from mastapy.gears.fe_model import _1193
            
            return self._parent._cast(_1193.GearFEModel)

        @property
        def cylindrical_gear_fe_model(self):
            from mastapy.gears.fe_model.cylindrical import _1197
            
            return self._parent._cast(_1197.CylindricalGearFEModel)

        @property
        def conical_gear_fe_model(self):
            from mastapy.gears.fe_model.conical import _1200
            
            return self._parent._cast(_1200.ConicalGearFEModel)

        @property
        def gear_implementation_analysis(self):
            from mastapy.gears.analysis import _1215
            
            return self._parent._cast(_1215.GearImplementationAnalysis)

        @property
        def gear_implementation_analysis_duty_cycle(self):
            from mastapy.gears.analysis import _1216
            
            return self._parent._cast(_1216.GearImplementationAnalysisDutyCycle)

        @property
        def gear_implementation_detail(self):
            from mastapy.gears.analysis import _1217
            
            return self._parent._cast(_1217.GearImplementationDetail)

        @property
        def gear_design_analysis(self) -> 'GearDesignAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearDesignAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearDesignAnalysis._Cast_GearDesignAnalysis':
        return self._Cast_GearDesignAnalysis(self)
