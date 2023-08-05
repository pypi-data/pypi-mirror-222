"""_1211.py

AbstractGearAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Analysis', 'AbstractGearAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractGearAnalysis',)


class AbstractGearAnalysis(_0.APIBase):
    """AbstractGearAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_ANALYSIS

    class _Cast_AbstractGearAnalysis:
        """Special nested class for casting AbstractGearAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractGearAnalysis'):
            self._parent = parent

        @property
        def abstract_gear_rating(self):
            from mastapy.gears.rating import _352
            
            return self._parent._cast(_352.AbstractGearRating)

        @property
        def gear_duty_cycle_rating(self):
            from mastapy.gears.rating import _356
            
            return self._parent._cast(_356.GearDutyCycleRating)

        @property
        def gear_rating(self):
            from mastapy.gears.rating import _359
            
            return self._parent._cast(_359.GearRating)

        @property
        def zerol_bevel_gear_rating(self):
            from mastapy.gears.rating.zerol_bevel import _368
            
            return self._parent._cast(_368.ZerolBevelGearRating)

        @property
        def worm_gear_duty_cycle_rating(self):
            from mastapy.gears.rating.worm import _370
            
            return self._parent._cast(_370.WormGearDutyCycleRating)

        @property
        def worm_gear_rating(self):
            from mastapy.gears.rating.worm import _372
            
            return self._parent._cast(_372.WormGearRating)

        @property
        def straight_bevel_gear_rating(self):
            from mastapy.gears.rating.straight_bevel import _394
            
            return self._parent._cast(_394.StraightBevelGearRating)

        @property
        def straight_bevel_diff_gear_rating(self):
            from mastapy.gears.rating.straight_bevel_diff import _397
            
            return self._parent._cast(_397.StraightBevelDiffGearRating)

        @property
        def spiral_bevel_gear_rating(self):
            from mastapy.gears.rating.spiral_bevel import _401
            
            return self._parent._cast(_401.SpiralBevelGearRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(self):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _404
            
            return self._parent._cast(_404.KlingelnbergCycloPalloidSpiralBevelGearRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_rating(self):
            from mastapy.gears.rating.klingelnberg_hypoid import _407
            
            return self._parent._cast(_407.KlingelnbergCycloPalloidHypoidGearRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_rating(self):
            from mastapy.gears.rating.klingelnberg_conical import _410
            
            return self._parent._cast(_410.KlingelnbergCycloPalloidConicalGearRating)

        @property
        def hypoid_gear_rating(self):
            from mastapy.gears.rating.hypoid import _437
            
            return self._parent._cast(_437.HypoidGearRating)

        @property
        def face_gear_duty_cycle_rating(self):
            from mastapy.gears.rating.face import _443
            
            return self._parent._cast(_443.FaceGearDutyCycleRating)

        @property
        def face_gear_rating(self):
            from mastapy.gears.rating.face import _446
            
            return self._parent._cast(_446.FaceGearRating)

        @property
        def cylindrical_gear_duty_cycle_rating(self):
            from mastapy.gears.rating.cylindrical import _453
            
            return self._parent._cast(_453.CylindricalGearDutyCycleRating)

        @property
        def cylindrical_gear_rating(self):
            from mastapy.gears.rating.cylindrical import _458
            
            return self._parent._cast(_458.CylindricalGearRating)

        @property
        def conical_gear_duty_cycle_rating(self):
            from mastapy.gears.rating.conical import _535
            
            return self._parent._cast(_535.ConicalGearDutyCycleRating)

        @property
        def conical_gear_rating(self):
            from mastapy.gears.rating.conical import _537
            
            return self._parent._cast(_537.ConicalGearRating)

        @property
        def concept_gear_duty_cycle_rating(self):
            from mastapy.gears.rating.concept import _545
            
            return self._parent._cast(_545.ConceptGearDutyCycleRating)

        @property
        def concept_gear_rating(self):
            from mastapy.gears.rating.concept import _548
            
            return self._parent._cast(_548.ConceptGearRating)

        @property
        def bevel_gear_rating(self):
            from mastapy.gears.rating.bevel import _552
            
            return self._parent._cast(_552.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(self):
            from mastapy.gears.rating.agma_gleason_conical import _563
            
            return self._parent._cast(_563.AGMAGleasonConicalGearRating)

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
        def gear_design_analysis(self):
            from mastapy.gears.analysis import _1214
            
            return self._parent._cast(_1214.GearDesignAnalysis)

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
        def abstract_gear_analysis(self) -> 'AbstractGearAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractGearAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def name_with_gear_set_name(self) -> 'str':
        """str: 'NameWithGearSetName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NameWithGearSetName

        if temp is None:
            return ''

        return temp

    @property
    def planet_index(self) -> 'int':
        """int: 'PlanetIndex' is the original name of this property."""

        temp = self.wrapped.PlanetIndex

        if temp is None:
            return 0

        return temp

    @planet_index.setter
    def planet_index(self, value: 'int'):
        self.wrapped.PlanetIndex = int(value) if value is not None else 0

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result

    @property
    def cast_to(self) -> 'AbstractGearAnalysis._Cast_AbstractGearAnalysis':
        return self._Cast_AbstractGearAnalysis(self)
