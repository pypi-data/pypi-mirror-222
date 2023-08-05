"""_1217.py

GearImplementationDetail
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.analysis import _1214
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_IMPLEMENTATION_DETAIL = python_net_import('SMT.MastaAPI.Gears.Analysis', 'GearImplementationDetail')

if TYPE_CHECKING:
    from mastapy.utility.scripting import _1732


__docformat__ = 'restructuredtext en'
__all__ = ('GearImplementationDetail',)


class GearImplementationDetail(_1214.GearDesignAnalysis):
    """GearImplementationDetail

    This is a mastapy class.
    """

    TYPE = _GEAR_IMPLEMENTATION_DETAIL

    class _Cast_GearImplementationDetail:
        """Special nested class for casting GearImplementationDetail to subclasses."""

        def __init__(self, parent: 'GearImplementationDetail'):
            self._parent = parent

        @property
        def gear_design_analysis(self):
            return self._parent._cast(_1214.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearAnalysis)

        @property
        def cylindrical_gear_manufacturing_config(self):
            from mastapy.gears.manufacturing.cylindrical import _609
            
            return self._parent._cast(_609.CylindricalGearManufacturingConfig)

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
        def gear_implementation_detail(self) -> 'GearImplementationDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearImplementationDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(self) -> 'GearImplementationDetail._Cast_GearImplementationDetail':
        return self._Cast_GearImplementationDetail(self)
