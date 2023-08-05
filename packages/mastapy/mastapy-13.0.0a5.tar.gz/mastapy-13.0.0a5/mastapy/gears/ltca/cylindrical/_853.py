"""_853.py

CylindricalGearLoadDistributionAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.ltca import _837
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_LOAD_DISTRIBUTION_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.LTCA.Cylindrical', 'CylindricalGearLoadDistributionAnalysis')

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical import _458
    from mastapy.gears.gear_two_d_fe_analysis import _895


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearLoadDistributionAnalysis',)


class CylindricalGearLoadDistributionAnalysis(_837.GearLoadDistributionAnalysis):
    """CylindricalGearLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_LOAD_DISTRIBUTION_ANALYSIS

    class _Cast_CylindricalGearLoadDistributionAnalysis:
        """Special nested class for casting CylindricalGearLoadDistributionAnalysis to subclasses."""

        def __init__(self, parent: 'CylindricalGearLoadDistributionAnalysis'):
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
        def cylindrical_gear_load_distribution_analysis(self) -> 'CylindricalGearLoadDistributionAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearLoadDistributionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self) -> '_458.CylindricalGearRating':
        """CylindricalGearRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tiff_analysis(self) -> '_895.CylindricalGearTIFFAnalysis':
        """CylindricalGearTIFFAnalysis: 'TIFFAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TIFFAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalGearLoadDistributionAnalysis._Cast_CylindricalGearLoadDistributionAnalysis':
        return self._Cast_CylindricalGearLoadDistributionAnalysis(self)
