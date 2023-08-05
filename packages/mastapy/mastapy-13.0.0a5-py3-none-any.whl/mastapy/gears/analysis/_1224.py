"""_1224.py

GearSetImplementationAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from mastapy._internal import constructor
from mastapy.gears.analysis import _1225
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_IMPLEMENTATION_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Analysis', 'GearSetImplementationAnalysis')

if TYPE_CHECKING:
    from mastapy import _7525


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetImplementationAnalysis',)


class GearSetImplementationAnalysis(_1225.GearSetImplementationAnalysisAbstract):
    """GearSetImplementationAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_IMPLEMENTATION_ANALYSIS

    class _Cast_GearSetImplementationAnalysis:
        """Special nested class for casting GearSetImplementationAnalysis to subclasses."""

        def __init__(self, parent: 'GearSetImplementationAnalysis'):
            self._parent = parent

        @property
        def gear_set_implementation_analysis_abstract(self):
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
        def cylindrical_manufactured_gear_set_load_case(self):
            from mastapy.gears.manufacturing.cylindrical import _618
            
            return self._parent._cast(_618.CylindricalManufacturedGearSetLoadCase)

        @property
        def conical_set_manufacturing_analysis(self):
            from mastapy.gears.manufacturing.bevel import _787
            
            return self._parent._cast(_787.ConicalSetManufacturingAnalysis)

        @property
        def gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca import _843
            
            return self._parent._cast(_843.GearSetLoadDistributionAnalysis)

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
        def gear_set_implementation_analysis(self) -> 'GearSetImplementationAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetImplementationAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def valid_results_ready(self) -> 'bool':
        """bool: 'ValidResultsReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ValidResultsReady

        if temp is None:
            return False

        return temp

    def perform_analysis(self, run_all_planetary_meshes: Optional['bool'] = True):
        """ 'PerformAnalysis' is the original name of this method.

        Args:
            run_all_planetary_meshes (bool, optional)
        """

        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        self.wrapped.PerformAnalysis(run_all_planetary_meshes if run_all_planetary_meshes else False)

    def perform_analysis_with_progress(self, run_all_planetary_meshes: 'bool', progress: '_7525.TaskProgress'):
        """ 'PerformAnalysisWithProgress' is the original name of this method.

        Args:
            run_all_planetary_meshes (bool)
            progress (mastapy.TaskProgress)
        """

        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        self.wrapped.PerformAnalysisWithProgress(run_all_planetary_meshes if run_all_planetary_meshes else False, progress.wrapped if progress else None)

    def results_ready_for(self, run_all_planetary_meshes: Optional['bool'] = True) -> 'bool':
        """ 'ResultsReadyFor' is the original name of this method.

        Args:
            run_all_planetary_meshes (bool, optional)

        Returns:
            bool
        """

        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        method_result = self.wrapped.ResultsReadyFor(run_all_planetary_meshes if run_all_planetary_meshes else False)
        return method_result

    @property
    def cast_to(self) -> 'GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis':
        return self._Cast_GearSetImplementationAnalysis(self)
