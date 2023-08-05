﻿"""_218.py

PoissonRatioOrthotropicComponents
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POISSON_RATIO_ORTHOTROPIC_COMPONENTS = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting', 'PoissonRatioOrthotropicComponents')


__docformat__ = 'restructuredtext en'
__all__ = ('PoissonRatioOrthotropicComponents',)


class PoissonRatioOrthotropicComponents(_0.APIBase):
    """PoissonRatioOrthotropicComponents

    This is a mastapy class.
    """

    TYPE = _POISSON_RATIO_ORTHOTROPIC_COMPONENTS

    class _Cast_PoissonRatioOrthotropicComponents:
        """Special nested class for casting PoissonRatioOrthotropicComponents to subclasses."""

        def __init__(self, parent: 'PoissonRatioOrthotropicComponents'):
            self._parent = parent

        @property
        def poisson_ratio_orthotropic_components(self) -> 'PoissonRatioOrthotropicComponents':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PoissonRatioOrthotropicComponents.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def nu_xy(self) -> 'float':
        """float: 'NuXY' is the original name of this property."""

        temp = self.wrapped.NuXY

        if temp is None:
            return 0.0

        return temp

    @nu_xy.setter
    def nu_xy(self, value: 'float'):
        self.wrapped.NuXY = float(value) if value is not None else 0.0

    @property
    def nu_xz(self) -> 'float':
        """float: 'NuXZ' is the original name of this property."""

        temp = self.wrapped.NuXZ

        if temp is None:
            return 0.0

        return temp

    @nu_xz.setter
    def nu_xz(self, value: 'float'):
        self.wrapped.NuXZ = float(value) if value is not None else 0.0

    @property
    def nu_yz(self) -> 'float':
        """float: 'NuYZ' is the original name of this property."""

        temp = self.wrapped.NuYZ

        if temp is None:
            return 0.0

        return temp

    @nu_yz.setter
    def nu_yz(self, value: 'float'):
        self.wrapped.NuYZ = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'PoissonRatioOrthotropicComponents._Cast_PoissonRatioOrthotropicComponents':
        return self._Cast_PoissonRatioOrthotropicComponents(self)
