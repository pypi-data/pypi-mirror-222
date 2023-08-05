"""_864.py

ConicalGearLoadDistributionAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.ltca import _837
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_LOAD_DISTRIBUTION_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.LTCA.Conical', 'ConicalGearLoadDistributionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearLoadDistributionAnalysis',)


class ConicalGearLoadDistributionAnalysis(_837.GearLoadDistributionAnalysis):
    """ConicalGearLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_LOAD_DISTRIBUTION_ANALYSIS

    class _Cast_ConicalGearLoadDistributionAnalysis:
        """Special nested class for casting ConicalGearLoadDistributionAnalysis to subclasses."""

        def __init__(self, parent: 'ConicalGearLoadDistributionAnalysis'):
            self._parent = parent

        @property
        def gear_load_distribution_analysis(self):
            return self._parent._cast(_837.GearLoadDistributionAnalysis)

        @property
        def gear_implementation_analysis(self):
            from mastapy.gears.analysis import _1215
            
            return self._parent._cast(_1215.GearImplementationAnalysis)

        @property
        def gear_design_analysis(self):
            from mastapy.gears.analysis import _1214
            
            return self._parent._cast(_1214.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearAnalysis)

        @property
        def conical_gear_load_distribution_analysis(self) -> 'ConicalGearLoadDistributionAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearLoadDistributionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalGearLoadDistributionAnalysis._Cast_ConicalGearLoadDistributionAnalysis':
        return self._Cast_ConicalGearLoadDistributionAnalysis(self)
