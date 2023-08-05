"""_945.py

GearDesignComponent
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_DESIGN_COMPONENT = python_net_import('SMT.MastaAPI.Gears.GearDesigns', 'GearDesignComponent')

if TYPE_CHECKING:
    from mastapy.utility.scripting import _1732


__docformat__ = 'restructuredtext en'
__all__ = ('GearDesignComponent',)


class GearDesignComponent(_0.APIBase):
    """GearDesignComponent

    This is a mastapy class.
    """

    TYPE = _GEAR_DESIGN_COMPONENT

    class _Cast_GearDesignComponent:
        """Special nested class for casting GearDesignComponent to subclasses."""

        def __init__(self, parent: 'GearDesignComponent'):
            self._parent = parent

        @property
        def gear_design(self):
            from mastapy.gears.gear_designs import _944
            
            return self._parent._cast(_944.GearDesign)

        @property
        def gear_mesh_design(self):
            from mastapy.gears.gear_designs import _946
            
            return self._parent._cast(_946.GearMeshDesign)

        @property
        def gear_set_design(self):
            from mastapy.gears.gear_designs import _947
            
            return self._parent._cast(_947.GearSetDesign)

        @property
        def zerol_bevel_gear_design(self):
            from mastapy.gears.gear_designs.zerol_bevel import _949
            
            return self._parent._cast(_949.ZerolBevelGearDesign)

        @property
        def zerol_bevel_gear_mesh_design(self):
            from mastapy.gears.gear_designs.zerol_bevel import _950
            
            return self._parent._cast(_950.ZerolBevelGearMeshDesign)

        @property
        def zerol_bevel_gear_set_design(self):
            from mastapy.gears.gear_designs.zerol_bevel import _951
            
            return self._parent._cast(_951.ZerolBevelGearSetDesign)

        @property
        def zerol_bevel_meshed_gear_design(self):
            from mastapy.gears.gear_designs.zerol_bevel import _952
            
            return self._parent._cast(_952.ZerolBevelMeshedGearDesign)

        @property
        def worm_design(self):
            from mastapy.gears.gear_designs.worm import _953
            
            return self._parent._cast(_953.WormDesign)

        @property
        def worm_gear_design(self):
            from mastapy.gears.gear_designs.worm import _954
            
            return self._parent._cast(_954.WormGearDesign)

        @property
        def worm_gear_mesh_design(self):
            from mastapy.gears.gear_designs.worm import _955
            
            return self._parent._cast(_955.WormGearMeshDesign)

        @property
        def worm_gear_set_design(self):
            from mastapy.gears.gear_designs.worm import _956
            
            return self._parent._cast(_956.WormGearSetDesign)

        @property
        def worm_wheel_design(self):
            from mastapy.gears.gear_designs.worm import _957
            
            return self._parent._cast(_957.WormWheelDesign)

        @property
        def straight_bevel_gear_design(self):
            from mastapy.gears.gear_designs.straight_bevel import _958
            
            return self._parent._cast(_958.StraightBevelGearDesign)

        @property
        def straight_bevel_gear_mesh_design(self):
            from mastapy.gears.gear_designs.straight_bevel import _959
            
            return self._parent._cast(_959.StraightBevelGearMeshDesign)

        @property
        def straight_bevel_gear_set_design(self):
            from mastapy.gears.gear_designs.straight_bevel import _960
            
            return self._parent._cast(_960.StraightBevelGearSetDesign)

        @property
        def straight_bevel_meshed_gear_design(self):
            from mastapy.gears.gear_designs.straight_bevel import _961
            
            return self._parent._cast(_961.StraightBevelMeshedGearDesign)

        @property
        def straight_bevel_diff_gear_design(self):
            from mastapy.gears.gear_designs.straight_bevel_diff import _962
            
            return self._parent._cast(_962.StraightBevelDiffGearDesign)

        @property
        def straight_bevel_diff_gear_mesh_design(self):
            from mastapy.gears.gear_designs.straight_bevel_diff import _963
            
            return self._parent._cast(_963.StraightBevelDiffGearMeshDesign)

        @property
        def straight_bevel_diff_gear_set_design(self):
            from mastapy.gears.gear_designs.straight_bevel_diff import _964
            
            return self._parent._cast(_964.StraightBevelDiffGearSetDesign)

        @property
        def straight_bevel_diff_meshed_gear_design(self):
            from mastapy.gears.gear_designs.straight_bevel_diff import _965
            
            return self._parent._cast(_965.StraightBevelDiffMeshedGearDesign)

        @property
        def spiral_bevel_gear_design(self):
            from mastapy.gears.gear_designs.spiral_bevel import _966
            
            return self._parent._cast(_966.SpiralBevelGearDesign)

        @property
        def spiral_bevel_gear_mesh_design(self):
            from mastapy.gears.gear_designs.spiral_bevel import _967
            
            return self._parent._cast(_967.SpiralBevelGearMeshDesign)

        @property
        def spiral_bevel_gear_set_design(self):
            from mastapy.gears.gear_designs.spiral_bevel import _968
            
            return self._parent._cast(_968.SpiralBevelGearSetDesign)

        @property
        def spiral_bevel_meshed_gear_design(self):
            from mastapy.gears.gear_designs.spiral_bevel import _969
            
            return self._parent._cast(_969.SpiralBevelMeshedGearDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self):
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _970
            
            return self._parent._cast(_970.KlingelnbergCycloPalloidSpiralBevelGearDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_design(self):
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _971
            
            return self._parent._cast(_971.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(self):
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _972
            
            return self._parent._cast(_972.KlingelnbergCycloPalloidSpiralBevelGearSetDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_meshed_gear_design(self):
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _973
            
            return self._parent._cast(_973.KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_design(self):
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _974
            
            return self._parent._cast(_974.KlingelnbergCycloPalloidHypoidGearDesign)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_design(self):
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _975
            
            return self._parent._cast(_975.KlingelnbergCycloPalloidHypoidGearMeshDesign)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_design(self):
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _976
            
            return self._parent._cast(_976.KlingelnbergCycloPalloidHypoidGearSetDesign)

        @property
        def klingelnberg_cyclo_palloid_hypoid_meshed_gear_design(self):
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _977
            
            return self._parent._cast(_977.KlingelnbergCycloPalloidHypoidMeshedGearDesign)

        @property
        def klingelnberg_conical_gear_design(self):
            from mastapy.gears.gear_designs.klingelnberg_conical import _978
            
            return self._parent._cast(_978.KlingelnbergConicalGearDesign)

        @property
        def klingelnberg_conical_gear_mesh_design(self):
            from mastapy.gears.gear_designs.klingelnberg_conical import _979
            
            return self._parent._cast(_979.KlingelnbergConicalGearMeshDesign)

        @property
        def klingelnberg_conical_gear_set_design(self):
            from mastapy.gears.gear_designs.klingelnberg_conical import _980
            
            return self._parent._cast(_980.KlingelnbergConicalGearSetDesign)

        @property
        def klingelnberg_conical_meshed_gear_design(self):
            from mastapy.gears.gear_designs.klingelnberg_conical import _981
            
            return self._parent._cast(_981.KlingelnbergConicalMeshedGearDesign)

        @property
        def hypoid_gear_design(self):
            from mastapy.gears.gear_designs.hypoid import _982
            
            return self._parent._cast(_982.HypoidGearDesign)

        @property
        def hypoid_gear_mesh_design(self):
            from mastapy.gears.gear_designs.hypoid import _983
            
            return self._parent._cast(_983.HypoidGearMeshDesign)

        @property
        def hypoid_gear_set_design(self):
            from mastapy.gears.gear_designs.hypoid import _984
            
            return self._parent._cast(_984.HypoidGearSetDesign)

        @property
        def hypoid_meshed_gear_design(self):
            from mastapy.gears.gear_designs.hypoid import _985
            
            return self._parent._cast(_985.HypoidMeshedGearDesign)

        @property
        def face_gear_design(self):
            from mastapy.gears.gear_designs.face import _986
            
            return self._parent._cast(_986.FaceGearDesign)

        @property
        def face_gear_mesh_design(self):
            from mastapy.gears.gear_designs.face import _988
            
            return self._parent._cast(_988.FaceGearMeshDesign)

        @property
        def face_gear_pinion_design(self):
            from mastapy.gears.gear_designs.face import _991
            
            return self._parent._cast(_991.FaceGearPinionDesign)

        @property
        def face_gear_set_design(self):
            from mastapy.gears.gear_designs.face import _992
            
            return self._parent._cast(_992.FaceGearSetDesign)

        @property
        def face_gear_wheel_design(self):
            from mastapy.gears.gear_designs.face import _994
            
            return self._parent._cast(_994.FaceGearWheelDesign)

        @property
        def cylindrical_gear_design(self):
            from mastapy.gears.gear_designs.cylindrical import _1009
            
            return self._parent._cast(_1009.CylindricalGearDesign)

        @property
        def cylindrical_gear_mesh_design(self):
            from mastapy.gears.gear_designs.cylindrical import _1015
            
            return self._parent._cast(_1015.CylindricalGearMeshDesign)

        @property
        def cylindrical_gear_set_design(self):
            from mastapy.gears.gear_designs.cylindrical import _1025
            
            return self._parent._cast(_1025.CylindricalGearSetDesign)

        @property
        def cylindrical_planetary_gear_set_design(self):
            from mastapy.gears.gear_designs.cylindrical import _1037
            
            return self._parent._cast(_1037.CylindricalPlanetaryGearSetDesign)

        @property
        def cylindrical_planet_gear_design(self):
            from mastapy.gears.gear_designs.cylindrical import _1038
            
            return self._parent._cast(_1038.CylindricalPlanetGearDesign)

        @property
        def conical_gear_design(self):
            from mastapy.gears.gear_designs.conical import _1150
            
            return self._parent._cast(_1150.ConicalGearDesign)

        @property
        def conical_gear_mesh_design(self):
            from mastapy.gears.gear_designs.conical import _1151
            
            return self._parent._cast(_1151.ConicalGearMeshDesign)

        @property
        def conical_gear_set_design(self):
            from mastapy.gears.gear_designs.conical import _1152
            
            return self._parent._cast(_1152.ConicalGearSetDesign)

        @property
        def conical_meshed_gear_design(self):
            from mastapy.gears.gear_designs.conical import _1155
            
            return self._parent._cast(_1155.ConicalMeshedGearDesign)

        @property
        def concept_gear_design(self):
            from mastapy.gears.gear_designs.concept import _1172
            
            return self._parent._cast(_1172.ConceptGearDesign)

        @property
        def concept_gear_mesh_design(self):
            from mastapy.gears.gear_designs.concept import _1173
            
            return self._parent._cast(_1173.ConceptGearMeshDesign)

        @property
        def concept_gear_set_design(self):
            from mastapy.gears.gear_designs.concept import _1174
            
            return self._parent._cast(_1174.ConceptGearSetDesign)

        @property
        def bevel_gear_design(self):
            from mastapy.gears.gear_designs.bevel import _1176
            
            return self._parent._cast(_1176.BevelGearDesign)

        @property
        def bevel_gear_mesh_design(self):
            from mastapy.gears.gear_designs.bevel import _1177
            
            return self._parent._cast(_1177.BevelGearMeshDesign)

        @property
        def bevel_gear_set_design(self):
            from mastapy.gears.gear_designs.bevel import _1178
            
            return self._parent._cast(_1178.BevelGearSetDesign)

        @property
        def bevel_meshed_gear_design(self):
            from mastapy.gears.gear_designs.bevel import _1179
            
            return self._parent._cast(_1179.BevelMeshedGearDesign)

        @property
        def agma_gleason_conical_gear_design(self):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1189
            
            return self._parent._cast(_1189.AGMAGleasonConicalGearDesign)

        @property
        def agma_gleason_conical_gear_mesh_design(self):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1190
            
            return self._parent._cast(_1190.AGMAGleasonConicalGearMeshDesign)

        @property
        def agma_gleason_conical_gear_set_design(self):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1191
            
            return self._parent._cast(_1191.AGMAGleasonConicalGearSetDesign)

        @property
        def agma_gleason_conical_meshed_gear_design(self):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1192
            
            return self._parent._cast(_1192.AGMAGleasonConicalMeshedGearDesign)

        @property
        def gear_design_component(self) -> 'GearDesignComponent':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearDesignComponent.TYPE'):
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
    def user_specified_data(self) -> '_1732.UserSpecifiedData':
        """UserSpecifiedData: 'UserSpecifiedData' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UserSpecifiedData

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

    def dispose(self):
        """ 'Dispose' is the original name of this method."""

        self.wrapped.Dispose()

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

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.dispose()

    @property
    def cast_to(self) -> 'GearDesignComponent._Cast_GearDesignComponent':
        return self._Cast_GearDesignComponent(self)
