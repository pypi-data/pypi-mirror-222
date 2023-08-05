"""_859.py

FaceGearSetLoadDistributionAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.ltca.cylindrical import _857
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_LOAD_DISTRIBUTION_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.LTCA.Cylindrical', 'FaceGearSetLoadDistributionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetLoadDistributionAnalysis',)


class FaceGearSetLoadDistributionAnalysis(_857.CylindricalGearSetLoadDistributionAnalysis):
    """FaceGearSetLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_LOAD_DISTRIBUTION_ANALYSIS

    class _Cast_FaceGearSetLoadDistributionAnalysis:
        """Special nested class for casting FaceGearSetLoadDistributionAnalysis to subclasses."""

        def __init__(self, parent: 'FaceGearSetLoadDistributionAnalysis'):
            self._parent = parent

        @property
        def cylindrical_gear_set_load_distribution_analysis(self):
            return self._parent._cast(_857.CylindricalGearSetLoadDistributionAnalysis)

        @property
        def gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca import _843
            
            return self._parent._cast(_843.GearSetLoadDistributionAnalysis)

        @property
        def gear_set_implementation_analysis(self):
            from mastapy.gears.analysis import _1224
            
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
        def face_gear_set_load_distribution_analysis(self) -> 'FaceGearSetLoadDistributionAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGearSetLoadDistributionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'FaceGearSetLoadDistributionAnalysis._Cast_FaceGearSetLoadDistributionAnalysis':
        return self._Cast_FaceGearSetLoadDistributionAnalysis(self)
