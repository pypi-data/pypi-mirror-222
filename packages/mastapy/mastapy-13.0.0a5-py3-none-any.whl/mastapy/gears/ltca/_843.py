"""_843.py

GearSetLoadDistributionAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.analysis import _1224
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_LOAD_DISTRIBUTION_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.LTCA', 'GearSetLoadDistributionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetLoadDistributionAnalysis',)


class GearSetLoadDistributionAnalysis(_1224.GearSetImplementationAnalysis):
    """GearSetLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_LOAD_DISTRIBUTION_ANALYSIS

    class _Cast_GearSetLoadDistributionAnalysis:
        """Special nested class for casting GearSetLoadDistributionAnalysis to subclasses."""

        def __init__(self, parent: 'GearSetLoadDistributionAnalysis'):
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
        def cylindrical_gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca.cylindrical import _857
            
            return self._parent._cast(_857.CylindricalGearSetLoadDistributionAnalysis)

        @property
        def face_gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca.cylindrical import _859
            
            return self._parent._cast(_859.FaceGearSetLoadDistributionAnalysis)

        @property
        def conical_gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca.conical import _865
            
            return self._parent._cast(_865.ConicalGearSetLoadDistributionAnalysis)

        @property
        def gear_set_load_distribution_analysis(self) -> 'GearSetLoadDistributionAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetLoadDistributionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_a_system_deflection_analysis(self) -> 'bool':
        """bool: 'IsASystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsASystemDeflectionAnalysis

        if temp is None:
            return False

        return temp

    @property
    def cast_to(self) -> 'GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis':
        return self._Cast_GearSetLoadDistributionAnalysis(self)
