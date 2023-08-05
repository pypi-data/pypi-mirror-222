"""_2016.py

LoadedRollerBearingResults
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2020
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLER_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedRollerBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedRollerBearingResults',)


class LoadedRollerBearingResults(_2020.LoadedRollingBearingResults):
    """LoadedRollerBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLER_BEARING_RESULTS

    class _Cast_LoadedRollerBearingResults:
        """Special nested class for casting LoadedRollerBearingResults to subclasses."""

        def __init__(self, parent: 'LoadedRollerBearingResults'):
            self._parent = parent

        @property
        def loaded_rolling_bearing_results(self):
            return self._parent._cast(_2020.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(self):
            from mastapy.bearings.bearing_results import _1941
            
            return self._parent._cast(_1941.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(self):
            from mastapy.bearings.bearing_results import _1944
            
            return self._parent._cast(_1944.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(self):
            from mastapy.bearings.bearing_results import _1936
            
            return self._parent._cast(_1936.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(self):
            from mastapy.bearings import _1862
            
            return self._parent._cast(_1862.BearingLoadCaseResultsLightweight)

        @property
        def loaded_asymmetric_spherical_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1976
            
            return self._parent._cast(_1976.LoadedAsymmetricSphericalRollerBearingResults)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1981
            
            return self._parent._cast(_1981.LoadedAxialThrustCylindricalRollerBearingResults)

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1984
            
            return self._parent._cast(_1984.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_crossed_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1992
            
            return self._parent._cast(_1992.LoadedCrossedRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1996
            
            return self._parent._cast(_1996.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_needle_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2008
            
            return self._parent._cast(_2008.LoadedNeedleRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2011
            
            return self._parent._cast(_2011.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_spherical_roller_radial_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2027
            
            return self._parent._cast(_2027.LoadedSphericalRollerRadialBearingResults)

        @property
        def loaded_spherical_roller_thrust_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2030
            
            return self._parent._cast(_2030.LoadedSphericalRollerThrustBearingResults)

        @property
        def loaded_taper_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2035
            
            return self._parent._cast(_2035.LoadedTaperRollerBearingResults)

        @property
        def loaded_toroidal_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2044
            
            return self._parent._cast(_2044.LoadedToroidalRollerBearingResults)

        @property
        def loaded_roller_bearing_results(self) -> 'LoadedRollerBearingResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedRollerBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def element_angular_velocity(self) -> 'float':
        """float: 'ElementAngularVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def element_centrifugal_force(self) -> 'float':
        """float: 'ElementCentrifugalForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementCentrifugalForce

        if temp is None:
            return 0.0

        return temp

    @property
    def element_surface_velocity(self) -> 'float':
        """float: 'ElementSurfaceVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementSurfaceVelocity

        if temp is None:
            return 0.0

        return temp

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
    def cast_to(self) -> 'LoadedRollerBearingResults._Cast_LoadedRollerBearingResults':
        return self._Cast_LoadedRollerBearingResults(self)
