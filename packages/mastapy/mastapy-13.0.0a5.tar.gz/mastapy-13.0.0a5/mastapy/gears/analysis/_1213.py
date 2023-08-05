"""_1213.py

AbstractGearSetAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_SET_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Analysis', 'AbstractGearSetAnalysis')

if TYPE_CHECKING:
    from mastapy.utility.model_validation import _1785, _1784


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractGearSetAnalysis',)


class AbstractGearSetAnalysis(_0.APIBase):
    """AbstractGearSetAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_SET_ANALYSIS

    class _Cast_AbstractGearSetAnalysis:
        """Special nested class for casting AbstractGearSetAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractGearSetAnalysis'):
            self._parent = parent

        @property
        def abstract_gear_set_rating(self):
            from mastapy.gears.rating import _353
            
            return self._parent._cast(_353.AbstractGearSetRating)

        @property
        def gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating import _360
            
            return self._parent._cast(_360.GearSetDutyCycleRating)

        @property
        def gear_set_rating(self):
            from mastapy.gears.rating import _361
            
            return self._parent._cast(_361.GearSetRating)

        @property
        def zerol_bevel_gear_set_rating(self):
            from mastapy.gears.rating.zerol_bevel import _369
            
            return self._parent._cast(_369.ZerolBevelGearSetRating)

        @property
        def worm_gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating.worm import _373
            
            return self._parent._cast(_373.WormGearSetDutyCycleRating)

        @property
        def worm_gear_set_rating(self):
            from mastapy.gears.rating.worm import _374
            
            return self._parent._cast(_374.WormGearSetRating)

        @property
        def straight_bevel_gear_set_rating(self):
            from mastapy.gears.rating.straight_bevel import _395
            
            return self._parent._cast(_395.StraightBevelGearSetRating)

        @property
        def straight_bevel_diff_gear_set_rating(self):
            from mastapy.gears.rating.straight_bevel_diff import _398
            
            return self._parent._cast(_398.StraightBevelDiffGearSetRating)

        @property
        def spiral_bevel_gear_set_rating(self):
            from mastapy.gears.rating.spiral_bevel import _402
            
            return self._parent._cast(_402.SpiralBevelGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(self):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _405
            
            return self._parent._cast(_405.KlingelnbergCycloPalloidSpiralBevelGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(self):
            from mastapy.gears.rating.klingelnberg_hypoid import _408
            
            return self._parent._cast(_408.KlingelnbergCycloPalloidHypoidGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(self):
            from mastapy.gears.rating.klingelnberg_conical import _411
            
            return self._parent._cast(_411.KlingelnbergCycloPalloidConicalGearSetRating)

        @property
        def hypoid_gear_set_rating(self):
            from mastapy.gears.rating.hypoid import _438
            
            return self._parent._cast(_438.HypoidGearSetRating)

        @property
        def face_gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating.face import _447
            
            return self._parent._cast(_447.FaceGearSetDutyCycleRating)

        @property
        def face_gear_set_rating(self):
            from mastapy.gears.rating.face import _448
            
            return self._parent._cast(_448.FaceGearSetRating)

        @property
        def cylindrical_gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating.cylindrical import _461
            
            return self._parent._cast(_461.CylindricalGearSetDutyCycleRating)

        @property
        def cylindrical_gear_set_rating(self):
            from mastapy.gears.rating.cylindrical import _462
            
            return self._parent._cast(_462.CylindricalGearSetRating)

        @property
        def conical_gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating.conical import _538
            
            return self._parent._cast(_538.ConicalGearSetDutyCycleRating)

        @property
        def conical_gear_set_rating(self):
            from mastapy.gears.rating.conical import _539
            
            return self._parent._cast(_539.ConicalGearSetRating)

        @property
        def concept_gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating.concept import _549
            
            return self._parent._cast(_549.ConceptGearSetDutyCycleRating)

        @property
        def concept_gear_set_rating(self):
            from mastapy.gears.rating.concept import _550
            
            return self._parent._cast(_550.ConceptGearSetRating)

        @property
        def bevel_gear_set_rating(self):
            from mastapy.gears.rating.bevel import _553
            
            return self._parent._cast(_553.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(self):
            from mastapy.gears.rating.agma_gleason_conical import _564
            
            return self._parent._cast(_564.AGMAGleasonConicalGearSetRating)

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
        def gear_set_design_analysis(self):
            from mastapy.gears.analysis import _1222
            
            return self._parent._cast(_1222.GearSetDesignAnalysis)

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
        def abstract_gear_set_analysis(self) -> 'AbstractGearSetAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractGearSetAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value is not None else ''

    @property
    def all_status_errors(self) -> 'List[_1785.StatusItem]':
        """List[StatusItem]: 'AllStatusErrors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllStatusErrors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def status(self) -> '_1784.Status':
        """Status: 'Status' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Status

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def cast_to(self) -> 'AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis':
        return self._Cast_AbstractGearSetAnalysis(self)
