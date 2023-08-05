"""_4007.py

ShaftComplexShape
"""
from __future__ import annotations

from typing import (
    TYPE_CHECKING, List, TypeVar, Generic
)

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_COMPLEX_SHAPE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.RotorDynamics', 'ShaftComplexShape')

if TYPE_CHECKING:
    from mastapy.utility.units_and_measurements import _1596


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftComplexShape',)


TLinearMeasurement = TypeVar('TLinearMeasurement', bound='_1596.MeasurementBase')
TAngularMeasurement = TypeVar('TAngularMeasurement', bound='_1596.MeasurementBase')


class ShaftComplexShape(_0.APIBase, Generic[TLinearMeasurement, TAngularMeasurement]):
    """ShaftComplexShape

    This is a mastapy class.

    Generic Types:
        TLinearMeasurement
        TAngularMeasurement
    """

    TYPE = _SHAFT_COMPLEX_SHAPE

    class _Cast_ShaftComplexShape:
        """Special nested class for casting ShaftComplexShape to subclasses."""

        def __init__(self, parent: 'ShaftComplexShape'):
            self._parent = parent

        @property
        def shaft_forced_complex_shape(self):
            from mastapy.system_model.analyses_and_results.rotor_dynamics import _4008
            
            return self._parent._cast(_4008.ShaftForcedComplexShape)

        @property
        def shaft_modal_complex_shape(self):
            from mastapy.system_model.analyses_and_results.rotor_dynamics import _4009
            
            return self._parent._cast(_4009.ShaftModalComplexShape)

        @property
        def shaft_modal_complex_shape_at_speeds(self):
            from mastapy.system_model.analyses_and_results.rotor_dynamics import _4010
            
            return self._parent._cast(_4010.ShaftModalComplexShapeAtSpeeds)

        @property
        def shaft_modal_complex_shape_at_stiffness(self):
            from mastapy.system_model.analyses_and_results.rotor_dynamics import _4011
            
            return self._parent._cast(_4011.ShaftModalComplexShapeAtStiffness)

        @property
        def shaft_complex_shape(self) -> 'ShaftComplexShape':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftComplexShape.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_imaginary(self) -> 'List[Vector3D]':
        """List[Vector3D]: 'AngularImaginary' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularImaginary

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)
        return value

    @property
    def angular_magnitude(self) -> 'List[Vector3D]':
        """List[Vector3D]: 'AngularMagnitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularMagnitude

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)
        return value

    @property
    def angular_phase(self) -> 'List[Vector3D]':
        """List[Vector3D]: 'AngularPhase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularPhase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)
        return value

    @property
    def angular_real(self) -> 'List[Vector3D]':
        """List[Vector3D]: 'AngularReal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularReal

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)
        return value

    @property
    def linear_imaginary(self) -> 'List[Vector3D]':
        """List[Vector3D]: 'LinearImaginary' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinearImaginary

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)
        return value

    @property
    def linear_magnitude(self) -> 'List[Vector3D]':
        """List[Vector3D]: 'LinearMagnitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinearMagnitude

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)
        return value

    @property
    def linear_phase(self) -> 'List[Vector3D]':
        """List[Vector3D]: 'LinearPhase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinearPhase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)
        return value

    @property
    def linear_real(self) -> 'List[Vector3D]':
        """List[Vector3D]: 'LinearReal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinearReal

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)
        return value

    @property
    def cast_to(self) -> 'ShaftComplexShape._Cast_ShaftComplexShape':
        return self._Cast_ShaftComplexShape(self)
