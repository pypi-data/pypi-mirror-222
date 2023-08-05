"""_1225.py

GearSetImplementationAnalysisAbstract
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.analysis import _1222
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_IMPLEMENTATION_ANALYSIS_ABSTRACT = python_net_import('SMT.MastaAPI.Gears.Analysis', 'GearSetImplementationAnalysisAbstract')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetImplementationAnalysisAbstract',)


class GearSetImplementationAnalysisAbstract(_1222.GearSetDesignAnalysis):
    """GearSetImplementationAnalysisAbstract

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_IMPLEMENTATION_ANALYSIS_ABSTRACT

    class _Cast_GearSetImplementationAnalysisAbstract:
        """Special nested class for casting GearSetImplementationAnalysisAbstract to subclasses."""

        def __init__(self, parent: 'GearSetImplementationAnalysisAbstract'):
            self._parent = parent

        @property
        def gear_set_design_analysis(self):
            return self._parent._cast(_1222.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1213
            
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
        def conical_set_manufacturing_analysis(self):
            from mastapy.gears.manufacturing.bevel import _787
            
            return self._parent._cast(_787.ConicalSetManufacturingAnalysis)

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
        def cylindrical_gear_set_micro_geometry_duty_cycle(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1104
            
            return self._parent._cast(_1104.CylindricalGearSetMicroGeometryDutyCycle)

        @property
        def gear_set_implementation_analysis(self):
            from mastapy.gears.analysis import _1224
            
            return self._parent._cast(_1224.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_duty_cycle(self):
            from mastapy.gears.analysis import _1226
            
            return self._parent._cast(_1226.GearSetImplementationAnalysisDutyCycle)

        @property
        def gear_set_implementation_analysis_abstract(self) -> 'GearSetImplementationAnalysisAbstract':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetImplementationAnalysisAbstract.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract':
        return self._Cast_GearSetImplementationAnalysisAbstract(self)
