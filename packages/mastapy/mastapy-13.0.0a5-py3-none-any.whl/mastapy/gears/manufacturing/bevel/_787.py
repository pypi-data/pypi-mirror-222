"""_787.py

ConicalSetManufacturingAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.analysis import _1224
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_SET_MANUFACTURING_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalSetManufacturingAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalSetManufacturingAnalysis',)


class ConicalSetManufacturingAnalysis(_1224.GearSetImplementationAnalysis):
    """ConicalSetManufacturingAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_SET_MANUFACTURING_ANALYSIS

    class _Cast_ConicalSetManufacturingAnalysis:
        """Special nested class for casting ConicalSetManufacturingAnalysis to subclasses."""

        def __init__(self, parent: 'ConicalSetManufacturingAnalysis'):
            self._parent = parent

        @property
        def gear_set_implementation_analysis(self):
            return self._parent._cast(_1224.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_abstract(self):
            from mastapy.gears.analysis import _1225
            
            return self._parent._cast(_1225.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_design_analysis(self):
            from mastapy.gears.analysis import _1222
            
            return self._parent._cast(_1222.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1213
            
            return self._parent._cast(_1213.AbstractGearSetAnalysis)

        @property
        def conical_set_manufacturing_analysis(self) -> 'ConicalSetManufacturingAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalSetManufacturingAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalSetManufacturingAnalysis._Cast_ConicalSetManufacturingAnalysis':
        return self._Cast_ConicalSetManufacturingAnalysis(self)
