"""_894.py

CylindricalGearSetTIFFAnalysisDutyCycle
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1222
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_TIFF_ANALYSIS_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Gears.GearTwoDFEAnalysis', 'CylindricalGearSetTIFFAnalysisDutyCycle')

if TYPE_CHECKING:
    from mastapy.gears.gear_two_d_fe_analysis import _896


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetTIFFAnalysisDutyCycle',)


class CylindricalGearSetTIFFAnalysisDutyCycle(_1222.GearSetDesignAnalysis):
    """CylindricalGearSetTIFFAnalysisDutyCycle

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_TIFF_ANALYSIS_DUTY_CYCLE

    class _Cast_CylindricalGearSetTIFFAnalysisDutyCycle:
        """Special nested class for casting CylindricalGearSetTIFFAnalysisDutyCycle to subclasses."""

        def __init__(self, parent: 'CylindricalGearSetTIFFAnalysisDutyCycle'):
            self._parent = parent

        @property
        def gear_set_design_analysis(self):
            return self._parent._cast(_1222.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1213
            
            return self._parent._cast(_1213.AbstractGearSetAnalysis)

        @property
        def cylindrical_gear_set_tiff_analysis_duty_cycle(self) -> 'CylindricalGearSetTIFFAnalysisDutyCycle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetTIFFAnalysisDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gears(self) -> 'List[_896.CylindricalGearTIFFAnalysisDutyCycle]':
        """List[CylindricalGearTIFFAnalysisDutyCycle]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalGearSetTIFFAnalysisDutyCycle._Cast_CylindricalGearSetTIFFAnalysisDutyCycle':
        return self._Cast_CylindricalGearSetTIFFAnalysisDutyCycle(self)
