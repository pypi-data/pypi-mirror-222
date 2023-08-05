"""_986.py

FaceGearDesign
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.gears.gear_designs import _944
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_FACE_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Face', 'FaceGearDesign')

if TYPE_CHECKING:
    from mastapy.gears import _331


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearDesign',)


class FaceGearDesign(_944.GearDesign):
    """FaceGearDesign

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_DESIGN

    class _Cast_FaceGearDesign:
        """Special nested class for casting FaceGearDesign to subclasses."""

        def __init__(self, parent: 'FaceGearDesign'):
            self._parent = parent

        @property
        def gear_design(self):
            return self._parent._cast(_944.GearDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _945
            
            return self._parent._cast(_945.GearDesignComponent)

        @property
        def face_gear_pinion_design(self):
            from mastapy.gears.gear_designs.face import _991
            
            return self._parent._cast(_991.FaceGearPinionDesign)

        @property
        def face_gear_wheel_design(self):
            from mastapy.gears.gear_designs.face import _994
            
            return self._parent._cast(_994.FaceGearWheelDesign)

        @property
        def face_gear_design(self) -> 'FaceGearDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def iso_material(self) -> 'str':
        """str: 'ISOMaterial' is the original name of this property."""

        temp = self.wrapped.ISOMaterial.SelectedItemName

        if temp is None:
            return ''

        return temp

    @iso_material.setter
    def iso_material(self, value: 'str'):
        self.wrapped.ISOMaterial.SetSelectedItem(str(value) if value is not None else '')

    @property
    def mean_point_to_crossing_point(self) -> 'float':
        """float: 'MeanPointToCrossingPoint' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanPointToCrossingPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_angle(self) -> 'float':
        """float: 'PitchAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PitchAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_diameter(self) -> 'float':
        """float: 'ReferenceDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReferenceDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def working_pitch_diameter(self) -> 'float':
        """float: 'WorkingPitchDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorkingPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def working_pitch_radius(self) -> 'float':
        """float: 'WorkingPitchRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorkingPitchRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'FaceGearDesign._Cast_FaceGearDesign':
        return self._Cast_FaceGearDesign(self)
