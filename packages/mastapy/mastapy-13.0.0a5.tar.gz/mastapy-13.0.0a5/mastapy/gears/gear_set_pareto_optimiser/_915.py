"""_915.py

MicroGeometryDesignSpaceSearchChartInformation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.gear_set_pareto_optimiser import _901, _914
from mastapy.gears.ltca.cylindrical import _857
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_DESIGN_SPACE_SEARCH_CHART_INFORMATION = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'MicroGeometryDesignSpaceSearchChartInformation')

if TYPE_CHECKING:
    from mastapy.gears.gear_set_pareto_optimiser import _913


__docformat__ = 'restructuredtext en'
__all__ = ('MicroGeometryDesignSpaceSearchChartInformation',)


class MicroGeometryDesignSpaceSearchChartInformation(_901.ChartInfoBase['_857.CylindricalGearSetLoadDistributionAnalysis', '_914.MicroGeometryDesignSpaceSearchCandidate']):
    """MicroGeometryDesignSpaceSearchChartInformation

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_DESIGN_SPACE_SEARCH_CHART_INFORMATION

    class _Cast_MicroGeometryDesignSpaceSearchChartInformation:
        """Special nested class for casting MicroGeometryDesignSpaceSearchChartInformation to subclasses."""

        def __init__(self, parent: 'MicroGeometryDesignSpaceSearchChartInformation'):
            self._parent = parent

        @property
        def chart_info_base(self):
            return self._parent._cast(_901.ChartInfoBase)

        @property
        def micro_geometry_design_space_search_chart_information(self) -> 'MicroGeometryDesignSpaceSearchChartInformation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MicroGeometryDesignSpaceSearchChartInformation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def optimiser(self) -> '_913.MicroGeometryDesignSpaceSearch':
        """MicroGeometryDesignSpaceSearch: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Optimiser

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'MicroGeometryDesignSpaceSearchChartInformation._Cast_MicroGeometryDesignSpaceSearchChartInformation':
        return self._Cast_MicroGeometryDesignSpaceSearchChartInformation(self)
