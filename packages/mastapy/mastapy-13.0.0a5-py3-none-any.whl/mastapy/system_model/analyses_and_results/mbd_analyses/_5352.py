"""_5352.py

AbstractShaftOrHousingMultibodyDynamicsAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5378
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'AbstractShaftOrHousingMultibodyDynamicsAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2419


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftOrHousingMultibodyDynamicsAnalysis',)


class AbstractShaftOrHousingMultibodyDynamicsAnalysis(_5378.ComponentMultibodyDynamicsAnalysis):
    """AbstractShaftOrHousingMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis:
        """Special nested class for casting AbstractShaftOrHousingMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractShaftOrHousingMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def component_multibody_dynamics_analysis(self):
            return self._parent._cast(_5378.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5440
            
            return self._parent._cast(_5440.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7515
            
            return self._parent._cast(_7515.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7511
            
            return self._parent._cast(_7511.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2639
            
            return self._parent._cast(_2639.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2635
            
            return self._parent._cast(_2635.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def abstract_shaft_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5351
            
            return self._parent._cast(_5351.AbstractShaftMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5398
            
            return self._parent._cast(_5398.CycloidalDiscMultibodyDynamicsAnalysis)

        @property
        def fe_part_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5409
            
            return self._parent._cast(_5409.FEPartMultibodyDynamicsAnalysis)

        @property
        def shaft_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5459
            
            return self._parent._cast(_5459.ShaftMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_or_housing_multibody_dynamics_analysis(self) -> 'AbstractShaftOrHousingMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftOrHousingMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_rigid_body_degrees_of_freedom(self) -> 'int':
        """int: 'NumberOfRigidBodyDegreesOfFreedom' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfRigidBodyDegreesOfFreedom

        if temp is None:
            return 0

        return temp

    @property
    def component_design(self) -> '_2419.AbstractShaftOrHousing':
        """AbstractShaftOrHousing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractShaftOrHousingMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis':
        return self._Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis(self)
