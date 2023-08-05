"""_1409.py

StandardSplineHalfDesign
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.detailed_rigid_connectors.splines import _1404
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STANDARD_SPLINE_HALF_DESIGN = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines', 'StandardSplineHalfDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('StandardSplineHalfDesign',)


class StandardSplineHalfDesign(_1404.SplineHalfDesign):
    """StandardSplineHalfDesign

    This is a mastapy class.
    """

    TYPE = _STANDARD_SPLINE_HALF_DESIGN

    class _Cast_StandardSplineHalfDesign:
        """Special nested class for casting StandardSplineHalfDesign to subclasses."""

        def __init__(self, parent: 'StandardSplineHalfDesign'):
            self._parent = parent

        @property
        def spline_half_design(self):
            return self._parent._cast(_1404.SplineHalfDesign)

        @property
        def detailed_rigid_connector_half_design(self):
            from mastapy.detailed_rigid_connectors import _1378
            
            return self._parent._cast(_1378.DetailedRigidConnectorHalfDesign)

        @property
        def din5480_spline_half_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1382
            
            return self._parent._cast(_1382.DIN5480SplineHalfDesign)

        @property
        def gbt3478_spline_half_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1386
            
            return self._parent._cast(_1386.GBT3478SplineHalfDesign)

        @property
        def iso4156_spline_half_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1389
            
            return self._parent._cast(_1389.ISO4156SplineHalfDesign)

        @property
        def sae_spline_half_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1397
            
            return self._parent._cast(_1397.SAESplineHalfDesign)

        @property
        def standard_spline_half_design(self) -> 'StandardSplineHalfDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StandardSplineHalfDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def root_fillet_radius_factor(self) -> 'float':
        """float: 'RootFilletRadiusFactor' is the original name of this property."""

        temp = self.wrapped.RootFilletRadiusFactor

        if temp is None:
            return 0.0

        return temp

    @root_fillet_radius_factor.setter
    def root_fillet_radius_factor(self, value: 'float'):
        self.wrapped.RootFilletRadiusFactor = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'StandardSplineHalfDesign._Cast_StandardSplineHalfDesign':
        return self._Cast_StandardSplineHalfDesign(self)
