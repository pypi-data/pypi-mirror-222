"""_364.py

MeshSingleFlankRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MESH_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'MeshSingleFlankRating')

if TYPE_CHECKING:
    from mastapy.gears import _317
    from mastapy.materials.efficiency import _292
    from mastapy.gears.rating import _362


__docformat__ = 'restructuredtext en'
__all__ = ('MeshSingleFlankRating',)


class MeshSingleFlankRating(_0.APIBase):
    """MeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _MESH_SINGLE_FLANK_RATING

    class _Cast_MeshSingleFlankRating:
        """Special nested class for casting MeshSingleFlankRating to subclasses."""

        def __init__(self, parent: 'MeshSingleFlankRating'):
            self._parent = parent

        @property
        def klingelnberg_conical_mesh_single_flank_rating(self):
            from mastapy.gears.rating.klingelnberg_conical.kn3030 import _412
            
            return self._parent._cast(_412.KlingelnbergConicalMeshSingleFlankRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_mesh_single_flank_rating(self):
            from mastapy.gears.rating.klingelnberg_conical.kn3030 import _416
            
            return self._parent._cast(_416.KlingelnbergCycloPalloidHypoidMeshSingleFlankRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_mesh_single_flank_rating(self):
            from mastapy.gears.rating.klingelnberg_conical.kn3030 import _417
            
            return self._parent._cast(_417.KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating)

        @property
        def iso10300_mesh_single_flank_rating(self):
            from mastapy.gears.rating.iso_10300 import _420
            
            return self._parent._cast(_420.ISO10300MeshSingleFlankRating)

        @property
        def iso10300_mesh_single_flank_rating_bevel_method_b2(self):
            from mastapy.gears.rating.iso_10300 import _421
            
            return self._parent._cast(_421.ISO10300MeshSingleFlankRatingBevelMethodB2)

        @property
        def iso10300_mesh_single_flank_rating_hypoid_method_b2(self):
            from mastapy.gears.rating.iso_10300 import _422
            
            return self._parent._cast(_422.ISO10300MeshSingleFlankRatingHypoidMethodB2)

        @property
        def iso10300_mesh_single_flank_rating_method_b1(self):
            from mastapy.gears.rating.iso_10300 import _423
            
            return self._parent._cast(_423.ISO10300MeshSingleFlankRatingMethodB1)

        @property
        def iso10300_mesh_single_flank_rating_method_b2(self):
            from mastapy.gears.rating.iso_10300 import _424
            
            return self._parent._cast(_424.ISO10300MeshSingleFlankRatingMethodB2)

        @property
        def gleason_hypoid_mesh_single_flank_rating(self):
            from mastapy.gears.rating.hypoid.standards import _441
            
            return self._parent._cast(_441.GleasonHypoidMeshSingleFlankRating)

        @property
        def cylindrical_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical import _465
            
            return self._parent._cast(_465.CylindricalMeshSingleFlankRating)

        @property
        def metal_plastic_or_plastic_metal_vdi2736_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _487
            
            return self._parent._cast(_487.MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating)

        @property
        def plastic_gear_vdi2736_abstract_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _489
            
            return self._parent._cast(_489.PlasticGearVDI2736AbstractMeshSingleFlankRating)

        @property
        def plastic_plastic_vdi2736_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _491
            
            return self._parent._cast(_491.PlasticPlasticVDI2736MeshSingleFlankRating)

        @property
        def iso63361996_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _509
            
            return self._parent._cast(_509.ISO63361996MeshSingleFlankRating)

        @property
        def iso63362006_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _511
            
            return self._parent._cast(_511.ISO63362006MeshSingleFlankRating)

        @property
        def iso63362019_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _513
            
            return self._parent._cast(_513.ISO63362019MeshSingleFlankRating)

        @property
        def iso6336_abstract_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _515
            
            return self._parent._cast(_515.ISO6336AbstractMeshSingleFlankRating)

        @property
        def iso6336_abstract_metal_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _517
            
            return self._parent._cast(_517.ISO6336AbstractMetalMeshSingleFlankRating)

        @property
        def din3990_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.din3990 import _530
            
            return self._parent._cast(_530.DIN3990MeshSingleFlankRating)

        @property
        def agma2101_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.agma import _532
            
            return self._parent._cast(_532.AGMA2101MeshSingleFlankRating)

        @property
        def conical_mesh_single_flank_rating(self):
            from mastapy.gears.rating.conical import _543
            
            return self._parent._cast(_543.ConicalMeshSingleFlankRating)

        @property
        def agma_spiral_bevel_mesh_single_flank_rating(self):
            from mastapy.gears.rating.bevel.standards import _555
            
            return self._parent._cast(_555.AGMASpiralBevelMeshSingleFlankRating)

        @property
        def gleason_spiral_bevel_mesh_single_flank_rating(self):
            from mastapy.gears.rating.bevel.standards import _557
            
            return self._parent._cast(_557.GleasonSpiralBevelMeshSingleFlankRating)

        @property
        def spiral_bevel_mesh_single_flank_rating(self):
            from mastapy.gears.rating.bevel.standards import _559
            
            return self._parent._cast(_559.SpiralBevelMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(self) -> 'MeshSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MeshSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def coefficient_of_friction_calculation_method(self) -> '_317.CoefficientOfFrictionCalculationMethod':
        """CoefficientOfFrictionCalculationMethod: 'CoefficientOfFrictionCalculationMethod' is the original name of this property."""

        temp = self.wrapped.CoefficientOfFrictionCalculationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.CoefficientOfFrictionCalculationMethod')
        return constructor.new_from_mastapy('mastapy.gears._317', 'CoefficientOfFrictionCalculationMethod')(value) if value is not None else None

    @coefficient_of_friction_calculation_method.setter
    def coefficient_of_friction_calculation_method(self, value: '_317.CoefficientOfFrictionCalculationMethod'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.CoefficientOfFrictionCalculationMethod')
        self.wrapped.CoefficientOfFrictionCalculationMethod = value

    @property
    def efficiency_rating_method(self) -> '_292.EfficiencyRatingMethod':
        """EfficiencyRatingMethod: 'EfficiencyRatingMethod' is the original name of this property."""

        temp = self.wrapped.EfficiencyRatingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Materials.Efficiency.EfficiencyRatingMethod')
        return constructor.new_from_mastapy('mastapy.materials.efficiency._292', 'EfficiencyRatingMethod')(value) if value is not None else None

    @efficiency_rating_method.setter
    def efficiency_rating_method(self, value: '_292.EfficiencyRatingMethod'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Materials.Efficiency.EfficiencyRatingMethod')
        self.wrapped.EfficiencyRatingMethod = value

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
    def power(self) -> 'float':
        """float: 'Power' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Power

        if temp is None:
            return 0.0

        return temp

    @property
    def rating_standard_name(self) -> 'str':
        """str: 'RatingStandardName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatingStandardName

        if temp is None:
            return ''

        return temp

    @property
    def gear_single_flank_ratings(self) -> 'List[_362.GearSingleFlankRating]':
        """List[GearSingleFlankRating]: 'GearSingleFlankRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

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
    def cast_to(self) -> 'MeshSingleFlankRating._Cast_MeshSingleFlankRating':
        return self._Cast_MeshSingleFlankRating(self)
