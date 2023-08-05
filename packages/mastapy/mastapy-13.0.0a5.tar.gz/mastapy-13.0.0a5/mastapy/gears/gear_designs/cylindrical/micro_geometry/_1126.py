"""_1126.py

TotalLeadReliefWithDeviation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1111
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOTAL_LEAD_RELIEF_WITH_DEVIATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'TotalLeadReliefWithDeviation')


__docformat__ = 'restructuredtext en'
__all__ = ('TotalLeadReliefWithDeviation',)


class TotalLeadReliefWithDeviation(_1111.LeadReliefWithDeviation):
    """TotalLeadReliefWithDeviation

    This is a mastapy class.
    """

    TYPE = _TOTAL_LEAD_RELIEF_WITH_DEVIATION

    class _Cast_TotalLeadReliefWithDeviation:
        """Special nested class for casting TotalLeadReliefWithDeviation to subclasses."""

        def __init__(self, parent: 'TotalLeadReliefWithDeviation'):
            self._parent = parent

        @property
        def lead_relief_with_deviation(self):
            return self._parent._cast(_1111.LeadReliefWithDeviation)

        @property
        def relief_with_deviation(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1124
            
            return self._parent._cast(_1124.ReliefWithDeviation)

        @property
        def total_lead_relief_with_deviation(self) -> 'TotalLeadReliefWithDeviation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TotalLeadReliefWithDeviation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'TotalLeadReliefWithDeviation._Cast_TotalLeadReliefWithDeviation':
        return self._Cast_TotalLeadReliefWithDeviation(self)
