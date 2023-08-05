"""_1162.py

KIMoSBevelHypoidSingleLoadCaseResultsData
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KI_MO_S_BEVEL_HYPOID_SINGLE_LOAD_CASE_RESULTS_DATA = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Conical', 'KIMoSBevelHypoidSingleLoadCaseResultsData')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1163


__docformat__ = 'restructuredtext en'
__all__ = ('KIMoSBevelHypoidSingleLoadCaseResultsData',)


class KIMoSBevelHypoidSingleLoadCaseResultsData(_0.APIBase):
    """KIMoSBevelHypoidSingleLoadCaseResultsData

    This is a mastapy class.
    """

    TYPE = _KI_MO_S_BEVEL_HYPOID_SINGLE_LOAD_CASE_RESULTS_DATA

    class _Cast_KIMoSBevelHypoidSingleLoadCaseResultsData:
        """Special nested class for casting KIMoSBevelHypoidSingleLoadCaseResultsData to subclasses."""

        def __init__(self, parent: 'KIMoSBevelHypoidSingleLoadCaseResultsData'):
            self._parent = parent

        @property
        def ki_mo_s_bevel_hypoid_single_load_case_results_data(self) -> 'KIMoSBevelHypoidSingleLoadCaseResultsData':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KIMoSBevelHypoidSingleLoadCaseResultsData.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_mesh_stiffness_per_unit_face_width(self) -> 'float':
        """float: 'AverageMeshStiffnessPerUnitFaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageMeshStiffnessPerUnitFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_pressure_chart(self) -> 'Image':
        """Image: 'ContactPressureChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactPressureChart

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def contact_ratio_under_load(self) -> 'float':
        """float: 'ContactRatioUnderLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactRatioUnderLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def efficiency(self) -> 'float':
        """float: 'Efficiency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Efficiency

        if temp is None:
            return 0.0

        return temp

    @property
    def flash_temperature_chart(self) -> 'Image':
        """Image: 'FlashTemperatureChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlashTemperatureChart

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def friction_coefficient_chart(self) -> 'Image':
        """Image: 'FrictionCoefficientChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrictionCoefficientChart

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def maximum_contact_pressure(self) -> 'float':
        """float: 'MaximumContactPressure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumContactPressure

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_flash_temperature(self) -> 'float':
        """float: 'MaximumFlashTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_friction_coefficient(self) -> 'float':
        """float: 'MaximumFrictionCoefficient' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumFrictionCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_pinion_root_stress(self) -> 'float':
        """float: 'MaximumPinionRootStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumPinionRootStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_sliding_velocity(self) -> 'float':
        """float: 'MaximumSlidingVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumSlidingVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_wheel_root_stress(self) -> 'float':
        """float: 'MaximumWheelRootStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumWheelRootStress

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_to_peak_te_linear_loaded(self) -> 'float':
        """float: 'PeakToPeakTELinearLoaded' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakToPeakTELinearLoaded

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_to_peak_te_linear_unloaded(self) -> 'float':
        """float: 'PeakToPeakTELinearUnloaded' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakToPeakTELinearUnloaded

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_root_stress_chart(self) -> 'Image':
        """Image: 'PinionRootStressChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionRootStressChart

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def pressure_velocity_pv_chart(self) -> 'Image':
        """Image: 'PressureVelocityPVChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PressureVelocityPVChart

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def sliding_velocity_chart(self) -> 'Image':
        """Image: 'SlidingVelocityChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingVelocityChart

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def wheel_root_stress_chart(self) -> 'Image':
        """Image: 'WheelRootStressChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelRootStressChart

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def single_rotation_angle_results(self) -> 'List[_1163.KIMoSBevelHypoidSingleRotationAngleResult]':
        """List[KIMoSBevelHypoidSingleRotationAngleResult]: 'SingleRotationAngleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SingleRotationAngleResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KIMoSBevelHypoidSingleLoadCaseResultsData._Cast_KIMoSBevelHypoidSingleLoadCaseResultsData':
        return self._Cast_KIMoSBevelHypoidSingleLoadCaseResultsData(self)
