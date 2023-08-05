"""_618.py

CylindricalManufacturedGearSetLoadCase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.analysis import _1224
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MANUFACTURED_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'CylindricalManufacturedGearSetLoadCase')

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _622
    from mastapy.gears.rating.cylindrical import _462


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalManufacturedGearSetLoadCase',)


class CylindricalManufacturedGearSetLoadCase(_1224.GearSetImplementationAnalysis):
    """CylindricalManufacturedGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MANUFACTURED_GEAR_SET_LOAD_CASE

    class _Cast_CylindricalManufacturedGearSetLoadCase:
        """Special nested class for casting CylindricalManufacturedGearSetLoadCase to subclasses."""

        def __init__(self, parent: 'CylindricalManufacturedGearSetLoadCase'):
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
        def cylindrical_manufactured_gear_set_load_case(self) -> 'CylindricalManufacturedGearSetLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalManufacturedGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def manufacturing_configuration(self) -> '_622.CylindricalSetManufacturingConfig':
        """CylindricalSetManufacturingConfig: 'ManufacturingConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ManufacturingConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_462.CylindricalGearSetRating':
        """CylindricalGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalManufacturedGearSetLoadCase._Cast_CylindricalManufacturedGearSetLoadCase':
        return self._Cast_CylindricalManufacturedGearSetLoadCase(self)
