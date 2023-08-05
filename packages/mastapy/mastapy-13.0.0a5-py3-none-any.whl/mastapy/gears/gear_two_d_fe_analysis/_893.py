"""_893.py

CylindricalGearSetTIFFAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1222
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_TIFF_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.GearTwoDFEAnalysis', 'CylindricalGearSetTIFFAnalysis')

if TYPE_CHECKING:
    from mastapy.gears.gear_two_d_fe_analysis import _895


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetTIFFAnalysis',)


class CylindricalGearSetTIFFAnalysis(_1222.GearSetDesignAnalysis):
    """CylindricalGearSetTIFFAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_TIFF_ANALYSIS

    class _Cast_CylindricalGearSetTIFFAnalysis:
        """Special nested class for casting CylindricalGearSetTIFFAnalysis to subclasses."""

        def __init__(self, parent: 'CylindricalGearSetTIFFAnalysis'):
            self._parent = parent

        @property
        def gear_set_design_analysis(self):
            return self._parent._cast(_1222.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1213
            
            return self._parent._cast(_1213.AbstractGearSetAnalysis)

        @property
        def cylindrical_gear_set_tiff_analysis(self) -> 'CylindricalGearSetTIFFAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetTIFFAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gears(self) -> 'List[_895.CylindricalGearTIFFAnalysis]':
        """List[CylindricalGearTIFFAnalysis]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalGearSetTIFFAnalysis._Cast_CylindricalGearSetTIFFAnalysis':
        return self._Cast_CylindricalGearSetTIFFAnalysis(self)
