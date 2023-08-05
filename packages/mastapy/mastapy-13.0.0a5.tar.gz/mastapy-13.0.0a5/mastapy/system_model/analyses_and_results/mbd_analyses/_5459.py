"""_5459.py

ShaftMultibodyDynamicsAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5351
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'ShaftMultibodyDynamicsAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2465
    from mastapy.system_model.analyses_and_results.static_loads import _6918


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftMultibodyDynamicsAnalysis',)


class ShaftMultibodyDynamicsAnalysis(_5351.AbstractShaftMultibodyDynamicsAnalysis):
    """ShaftMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_ShaftMultibodyDynamicsAnalysis:
        """Special nested class for casting ShaftMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'ShaftMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def abstract_shaft_multibody_dynamics_analysis(self):
            return self._parent._cast(_5351.AbstractShaftMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_or_housing_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5352
            
            return self._parent._cast(_5352.AbstractShaftOrHousingMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5378
            
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
        def shaft_multibody_dynamics_analysis(self) -> 'ShaftMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_velocities(self) -> 'List[float]':
        """List[float]: 'AngularVelocities' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularVelocities

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_x_deflections(self) -> 'List[float]':
        """List[float]: 'ElasticLocalXDeflections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalXDeflections

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_y_deflections(self) -> 'List[float]':
        """List[float]: 'ElasticLocalYDeflections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalYDeflections

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_z_deflections(self) -> 'List[float]':
        """List[float]: 'ElasticLocalZDeflections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalZDeflections

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_theta_x_deflections(self) -> 'List[float]':
        """List[float]: 'ElasticLocalThetaXDeflections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalThetaXDeflections

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_theta_y_deflections(self) -> 'List[float]':
        """List[float]: 'ElasticLocalThetaYDeflections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalThetaYDeflections

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_radial_deflections(self) -> 'List[float]':
        """List[float]: 'ElasticRadialDeflections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticRadialDeflections

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_twists(self) -> 'List[float]':
        """List[float]: 'ElasticTwists' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticTwists

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def component_design(self) -> '_2465.Shaft':
        """Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6918.ShaftLoadCase':
        """ShaftLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[ShaftMultibodyDynamicsAnalysis]':
        """List[ShaftMultibodyDynamicsAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ShaftMultibodyDynamicsAnalysis._Cast_ShaftMultibodyDynamicsAnalysis':
        return self._Cast_ShaftMultibodyDynamicsAnalysis(self)
