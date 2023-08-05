﻿"""_947.py

GearSetDesign
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.gears.gear_designs import _945
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_GEAR_SET_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns', 'GearSetDesign')

if TYPE_CHECKING:
    from mastapy.gears.fe_model import _1196
    from mastapy.gears import _326
    from mastapy.gears.gear_designs import _944


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetDesign',)


class GearSetDesign(_945.GearDesignComponent):
    """GearSetDesign

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_DESIGN

    class _Cast_GearSetDesign:
        """Special nested class for casting GearSetDesign to subclasses."""

        def __init__(self, parent: 'GearSetDesign'):
            self._parent = parent

        @property
        def gear_design_component(self):
            return self._parent._cast(_945.GearDesignComponent)

        @property
        def zerol_bevel_gear_set_design(self):
            from mastapy.gears.gear_designs.zerol_bevel import _951
            
            return self._parent._cast(_951.ZerolBevelGearSetDesign)

        @property
        def worm_gear_set_design(self):
            from mastapy.gears.gear_designs.worm import _956
            
            return self._parent._cast(_956.WormGearSetDesign)

        @property
        def straight_bevel_gear_set_design(self):
            from mastapy.gears.gear_designs.straight_bevel import _960
            
            return self._parent._cast(_960.StraightBevelGearSetDesign)

        @property
        def straight_bevel_diff_gear_set_design(self):
            from mastapy.gears.gear_designs.straight_bevel_diff import _964
            
            return self._parent._cast(_964.StraightBevelDiffGearSetDesign)

        @property
        def spiral_bevel_gear_set_design(self):
            from mastapy.gears.gear_designs.spiral_bevel import _968
            
            return self._parent._cast(_968.SpiralBevelGearSetDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(self):
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _972
            
            return self._parent._cast(_972.KlingelnbergCycloPalloidSpiralBevelGearSetDesign)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_design(self):
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _976
            
            return self._parent._cast(_976.KlingelnbergCycloPalloidHypoidGearSetDesign)

        @property
        def klingelnberg_conical_gear_set_design(self):
            from mastapy.gears.gear_designs.klingelnberg_conical import _980
            
            return self._parent._cast(_980.KlingelnbergConicalGearSetDesign)

        @property
        def hypoid_gear_set_design(self):
            from mastapy.gears.gear_designs.hypoid import _984
            
            return self._parent._cast(_984.HypoidGearSetDesign)

        @property
        def face_gear_set_design(self):
            from mastapy.gears.gear_designs.face import _992
            
            return self._parent._cast(_992.FaceGearSetDesign)

        @property
        def cylindrical_gear_set_design(self):
            from mastapy.gears.gear_designs.cylindrical import _1025
            
            return self._parent._cast(_1025.CylindricalGearSetDesign)

        @property
        def cylindrical_planetary_gear_set_design(self):
            from mastapy.gears.gear_designs.cylindrical import _1037
            
            return self._parent._cast(_1037.CylindricalPlanetaryGearSetDesign)

        @property
        def conical_gear_set_design(self):
            from mastapy.gears.gear_designs.conical import _1152
            
            return self._parent._cast(_1152.ConicalGearSetDesign)

        @property
        def concept_gear_set_design(self):
            from mastapy.gears.gear_designs.concept import _1174
            
            return self._parent._cast(_1174.ConceptGearSetDesign)

        @property
        def bevel_gear_set_design(self):
            from mastapy.gears.gear_designs.bevel import _1178
            
            return self._parent._cast(_1178.BevelGearSetDesign)

        @property
        def agma_gleason_conical_gear_set_design(self):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1191
            
            return self._parent._cast(_1191.AGMAGleasonConicalGearSetDesign)

        @property
        def gear_set_design(self) -> 'GearSetDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_contact_ratio_rating_for_nvh(self) -> 'float':
        """float: 'AxialContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialContactRatioRatingForNVH

        if temp is None:
            return 0.0

        return temp

    @property
    def fe_model(self) -> 'str':
        """str: 'FEModel' is the original name of this property."""

        temp = self.wrapped.FEModel.SelectedItemName

        if temp is None:
            return ''

        return temp

    @fe_model.setter
    def fe_model(self, value: 'str'):
        self.wrapped.FEModel.SetSelectedItem(str(value) if value is not None else '')

    @property
    def gear_set_drawing(self) -> 'Image':
        """Image: 'GearSetDrawing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDrawing

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def largest_mesh_ratio(self) -> 'float':
        """float: 'LargestMeshRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LargestMeshRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def largest_number_of_teeth(self) -> 'int':
        """int: 'LargestNumberOfTeeth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LargestNumberOfTeeth

        if temp is None:
            return 0

        return temp

    @property
    def long_name(self) -> 'str':
        """str: 'LongName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LongName

        if temp is None:
            return ''

        return temp

    @property
    def mass(self) -> 'float':
        """float: 'Mass' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mass

        if temp is None:
            return 0.0

        return temp

    @property
    def name_including_tooth_numbers(self) -> 'str':
        """str: 'NameIncludingToothNumbers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NameIncludingToothNumbers

        if temp is None:
            return ''

        return temp

    @property
    def required_safety_factor_for_bending(self) -> 'float':
        """float: 'RequiredSafetyFactorForBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RequiredSafetyFactorForBending

        if temp is None:
            return 0.0

        return temp

    @property
    def required_safety_factor_for_contact(self) -> 'float':
        """float: 'RequiredSafetyFactorForContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RequiredSafetyFactorForContact

        if temp is None:
            return 0.0

        return temp

    @property
    def required_safety_factor_for_static_bending(self) -> 'float':
        """float: 'RequiredSafetyFactorForStaticBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RequiredSafetyFactorForStaticBending

        if temp is None:
            return 0.0

        return temp

    @property
    def required_safety_factor_for_static_contact(self) -> 'float':
        """float: 'RequiredSafetyFactorForStaticContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RequiredSafetyFactorForStaticContact

        if temp is None:
            return 0.0

        return temp

    @property
    def smallest_number_of_teeth(self) -> 'int':
        """int: 'SmallestNumberOfTeeth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallestNumberOfTeeth

        if temp is None:
            return 0

        return temp

    @property
    def transverse_contact_ratio_rating_for_nvh(self) -> 'float':
        """float: 'TransverseContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseContactRatioRatingForNVH

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_and_axial_contact_ratio_rating_for_nvh(self) -> 'float':
        """float: 'TransverseAndAxialContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseAndAxialContactRatioRatingForNVH

        if temp is None:
            return 0.0

        return temp

    @property
    def active_ltcafe_model(self) -> '_1196.GearSetFEModel':
        """GearSetFEModel: 'ActiveLTCAFEModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveLTCAFEModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tifffe_model(self) -> '_1196.GearSetFEModel':
        """GearSetFEModel: 'TIFFFEModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TIFFFEModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def transmission_properties_gears(self) -> '_326.GearSetDesignGroup':
        """GearSetDesignGroup: 'TransmissionPropertiesGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransmissionPropertiesGears

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears(self) -> 'List[_944.GearDesign]':
        """List[GearDesign]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def ltcafe_models(self) -> 'List[_1196.GearSetFEModel]':
        """List[GearSetFEModel]: 'LTCAFEModels' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LTCAFEModels

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def create_new_fe_model(self):
        """ 'CreateNewFEModel' is the original name of this method."""

        self.wrapped.CreateNewFEModel()

    def create_new_tifffe_model(self):
        """ 'CreateNewTIFFFEModel' is the original name of this method."""

        self.wrapped.CreateNewTIFFFEModel()

    def copy(self, include_fe: Optional['bool'] = False) -> 'GearSetDesign':
        """ 'Copy' is the original name of this method.

        Args:
            include_fe (bool, optional)

        Returns:
            mastapy.gears.gear_designs.GearSetDesign
        """

        include_fe = bool(include_fe)
        method_result = self.wrapped.Copy(include_fe if include_fe else False)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'GearSetDesign._Cast_GearSetDesign':
        return self._Cast_GearSetDesign(self)
