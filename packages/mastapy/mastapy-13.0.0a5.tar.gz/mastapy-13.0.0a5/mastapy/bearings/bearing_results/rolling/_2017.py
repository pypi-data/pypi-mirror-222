"""_2017.py

LoadedRollerBearingRow
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results.rolling import _2021
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLER_BEARING_ROW = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedRollerBearingRow')

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2016, _1957


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedRollerBearingRow',)


class LoadedRollerBearingRow(_2021.LoadedRollingBearingRow):
    """LoadedRollerBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLER_BEARING_ROW

    class _Cast_LoadedRollerBearingRow:
        """Special nested class for casting LoadedRollerBearingRow to subclasses."""

        def __init__(self, parent: 'LoadedRollerBearingRow'):
            self._parent = parent

        @property
        def loaded_rolling_bearing_row(self):
            return self._parent._cast(_2021.LoadedRollingBearingRow)

        @property
        def loaded_asymmetric_spherical_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _1977
            
            return self._parent._cast(_1977.LoadedAsymmetricSphericalRollerBearingRow)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _1982
            
            return self._parent._cast(_1982.LoadedAxialThrustCylindricalRollerBearingRow)

        @property
        def loaded_axial_thrust_needle_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _1985
            
            return self._parent._cast(_1985.LoadedAxialThrustNeedleRollerBearingRow)

        @property
        def loaded_crossed_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _1993
            
            return self._parent._cast(_1993.LoadedCrossedRollerBearingRow)

        @property
        def loaded_cylindrical_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _1997
            
            return self._parent._cast(_1997.LoadedCylindricalRollerBearingRow)

        @property
        def loaded_needle_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2009
            
            return self._parent._cast(_2009.LoadedNeedleRollerBearingRow)

        @property
        def loaded_non_barrel_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2012
            
            return self._parent._cast(_2012.LoadedNonBarrelRollerBearingRow)

        @property
        def loaded_spherical_roller_radial_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2028
            
            return self._parent._cast(_2028.LoadedSphericalRollerRadialBearingRow)

        @property
        def loaded_spherical_roller_thrust_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2031
            
            return self._parent._cast(_2031.LoadedSphericalRollerThrustBearingRow)

        @property
        def loaded_taper_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2036
            
            return self._parent._cast(_2036.LoadedTaperRollerBearingRow)

        @property
        def loaded_toroidal_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2045
            
            return self._parent._cast(_2045.LoadedToroidalRollerBearingRow)

        @property
        def loaded_roller_bearing_row(self) -> 'LoadedRollerBearingRow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedRollerBearingRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def depth_of_maximum_shear_stress_chart_inner(self) -> 'Image':
        """Image: 'DepthOfMaximumShearStressChartInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DepthOfMaximumShearStressChartInner

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def depth_of_maximum_shear_stress_chart_outer(self) -> 'Image':
        """Image: 'DepthOfMaximumShearStressChartOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DepthOfMaximumShearStressChartOuter

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def hertzian_contact_width_inner(self) -> 'float':
        """float: 'HertzianContactWidthInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianContactWidthInner

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_contact_width_outer(self) -> 'float':
        """float: 'HertzianContactWidthOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianContactWidthOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_race_profile_warning(self) -> 'str':
        """str: 'InnerRaceProfileWarning' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRaceProfileWarning

        if temp is None:
            return ''

        return temp

    @property
    def maximum_normal_edge_stress_inner(self) -> 'float':
        """float: 'MaximumNormalEdgeStressInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalEdgeStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_edge_stress_outer(self) -> 'float':
        """float: 'MaximumNormalEdgeStressOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalEdgeStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_inner(self) -> 'float':
        """float: 'MaximumShearStressInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumShearStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_outer(self) -> 'float':
        """float: 'MaximumShearStressOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumShearStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_race_profile_warning(self) -> 'str':
        """str: 'OuterRaceProfileWarning' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRaceProfileWarning

        if temp is None:
            return ''

        return temp

    @property
    def roller_profile_warning(self) -> 'str':
        """str: 'RollerProfileWarning' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollerProfileWarning

        if temp is None:
            return ''

        return temp

    @property
    def shear_stress_chart_inner(self) -> 'Image':
        """Image: 'ShearStressChartInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShearStressChartInner

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def shear_stress_chart_outer(self) -> 'Image':
        """Image: 'ShearStressChartOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShearStressChartOuter

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def loaded_bearing(self) -> '_2016.LoadedRollerBearingResults':
        """LoadedRollerBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def lamina_dynamic_equivalent_loads(self) -> 'List[_1957.ForceAtLaminaGroupReportable]':
        """List[ForceAtLaminaGroupReportable]: 'LaminaDynamicEquivalentLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LaminaDynamicEquivalentLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'LoadedRollerBearingRow._Cast_LoadedRollerBearingRow':
        return self._Cast_LoadedRollerBearingRow(self)
