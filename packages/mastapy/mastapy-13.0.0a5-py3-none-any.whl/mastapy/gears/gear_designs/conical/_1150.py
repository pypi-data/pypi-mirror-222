"""_1150.py

ConicalGearDesign
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.gear_designs import _944
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Conical', 'ConicalGearDesign')

if TYPE_CHECKING:
    from mastapy.gears import _331
    from mastapy.gears.manufacturing.bevel import _793
    from mastapy.gears.gear_designs.cylindrical import _1074


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearDesign',)


class ConicalGearDesign(_944.GearDesign):
    """ConicalGearDesign

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_DESIGN

    class _Cast_ConicalGearDesign:
        """Special nested class for casting ConicalGearDesign to subclasses."""

        def __init__(self, parent: 'ConicalGearDesign'):
            self._parent = parent

        @property
        def gear_design(self):
            return self._parent._cast(_944.GearDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _945
            
            return self._parent._cast(_945.GearDesignComponent)

        @property
        def zerol_bevel_gear_design(self):
            from mastapy.gears.gear_designs.zerol_bevel import _949
            
            return self._parent._cast(_949.ZerolBevelGearDesign)

        @property
        def straight_bevel_gear_design(self):
            from mastapy.gears.gear_designs.straight_bevel import _958
            
            return self._parent._cast(_958.StraightBevelGearDesign)

        @property
        def straight_bevel_diff_gear_design(self):
            from mastapy.gears.gear_designs.straight_bevel_diff import _962
            
            return self._parent._cast(_962.StraightBevelDiffGearDesign)

        @property
        def spiral_bevel_gear_design(self):
            from mastapy.gears.gear_designs.spiral_bevel import _966
            
            return self._parent._cast(_966.SpiralBevelGearDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self):
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _970
            
            return self._parent._cast(_970.KlingelnbergCycloPalloidSpiralBevelGearDesign)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_design(self):
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _974
            
            return self._parent._cast(_974.KlingelnbergCycloPalloidHypoidGearDesign)

        @property
        def klingelnberg_conical_gear_design(self):
            from mastapy.gears.gear_designs.klingelnberg_conical import _978
            
            return self._parent._cast(_978.KlingelnbergConicalGearDesign)

        @property
        def hypoid_gear_design(self):
            from mastapy.gears.gear_designs.hypoid import _982
            
            return self._parent._cast(_982.HypoidGearDesign)

        @property
        def bevel_gear_design(self):
            from mastapy.gears.gear_designs.bevel import _1176
            
            return self._parent._cast(_1176.BevelGearDesign)

        @property
        def agma_gleason_conical_gear_design(self):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1189
            
            return self._parent._cast(_1189.AGMAGleasonConicalGearDesign)

        @property
        def conical_gear_design(self) -> 'ConicalGearDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cutter_edge_radius_concave(self) -> 'float':
        """float: 'CutterEdgeRadiusConcave' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CutterEdgeRadiusConcave

        if temp is None:
            return 0.0

        return temp

    @property
    def cutter_edge_radius_convex(self) -> 'float':
        """float: 'CutterEdgeRadiusConvex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CutterEdgeRadiusConvex

        if temp is None:
            return 0.0

        return temp

    @property
    def face_angle(self) -> 'float':
        """float: 'FaceAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def hand(self) -> '_331.Hand':
        """Hand: 'Hand' is the original name of this property."""

        temp = self.wrapped.Hand

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.Hand')
        return constructor.new_from_mastapy('mastapy.gears._331', 'Hand')(value) if value is not None else None

    @hand.setter
    def hand(self, value: '_331.Hand'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.Hand')
        self.wrapped.Hand = value

    @property
    def inner_root_diameter(self) -> 'float':
        """float: 'InnerRootDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRootDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_tip_diameter(self) -> 'float':
        """float: 'InnerTipDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerTipDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_root_diameter(self) -> 'float':
        """float: 'OuterRootDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRootDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def root_angle(self) -> 'float':
        """float: 'RootAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def straddle_mounted(self) -> 'bool':
        """bool: 'StraddleMounted' is the original name of this property."""

        temp = self.wrapped.StraddleMounted

        if temp is None:
            return False

        return temp

    @straddle_mounted.setter
    def straddle_mounted(self, value: 'bool'):
        self.wrapped.StraddleMounted = bool(value) if value is not None else False

    @property
    def use_cutter_tilt(self) -> 'bool':
        """bool: 'UseCutterTilt' is the original name of this property."""

        temp = self.wrapped.UseCutterTilt

        if temp is None:
            return False

        return temp

    @use_cutter_tilt.setter
    def use_cutter_tilt(self, value: 'bool'):
        self.wrapped.UseCutterTilt = bool(value) if value is not None else False

    @property
    def flank_measurement_border(self) -> '_793.FlankMeasurementBorder':
        """FlankMeasurementBorder: 'FlankMeasurementBorder' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlankMeasurementBorder

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def surface_roughness(self) -> '_1074.SurfaceRoughness':
        """SurfaceRoughness: 'SurfaceRoughness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SurfaceRoughness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalGearDesign._Cast_ConicalGearDesign':
        return self._Cast_ConicalGearDesign(self)
