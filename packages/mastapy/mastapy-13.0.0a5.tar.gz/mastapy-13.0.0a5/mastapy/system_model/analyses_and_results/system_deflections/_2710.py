﻿"""_2710.py

ConnectorSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy.system_model.analyses_and_results.system_deflections import _2764
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ConnectorSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2430
    from mastapy.math_utility.measured_vectors import _1555
    from mastapy.system_model.analyses_and_results.system_deflections import _2739
    from mastapy.system_model.fe import _2368
    from mastapy.system_model.analyses_and_results.power_flows import _4048


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectorSystemDeflection',)


class ConnectorSystemDeflection(_2764.MountableComponentSystemDeflection):
    """ConnectorSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_SYSTEM_DEFLECTION

    class _Cast_ConnectorSystemDeflection:
        """Special nested class for casting ConnectorSystemDeflection to subclasses."""

        def __init__(self, parent: 'ConnectorSystemDeflection'):
            self._parent = parent

        @property
        def mountable_component_system_deflection(self):
            return self._parent._cast(_2764.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2697
            
            return self._parent._cast(_2697.ComponentSystemDeflection)

        @property
        def part_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2767
            
            return self._parent._cast(_2767.PartSystemDeflection)

        @property
        def part_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7513
            
            return self._parent._cast(_7513.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7514
            
            return self._parent._cast(_7514.PartStaticLoadAnalysisCase)

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
        def bearing_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2680
            
            return self._parent._cast(_2680.BearingSystemDeflection)

        @property
        def oil_seal_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2766
            
            return self._parent._cast(_2766.OilSealSystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2783
            
            return self._parent._cast(_2783.ShaftHubConnectionSystemDeflection)

        @property
        def connector_system_deflection(self) -> 'ConnectorSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectorSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def convergence_delta_energy(self) -> 'float':
        """float: 'ConvergenceDeltaEnergy' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConvergenceDeltaEnergy

        if temp is None:
            return 0.0

        return temp

    @property
    def linear_force_on_inner(self) -> 'Vector3D':
        """Vector3D: 'LinearForceOnInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinearForceOnInner

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def moment_on_inner(self) -> 'Vector3D':
        """Vector3D: 'MomentOnInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MomentOnInner

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def component_design(self) -> '_2430.Connector':
        """Connector: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def force_on_outer_support_in_lcs(self) -> '_1555.VectorWithLinearAndAngularComponents':
        """VectorWithLinearAndAngularComponents: 'ForceOnOuterSupportInLCS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceOnOuterSupportInLCS

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def force_on_outer_support_in_wcs(self) -> '_1555.VectorWithLinearAndAngularComponents':
        """VectorWithLinearAndAngularComponents: 'ForceOnOuterSupportInWCS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceOnOuterSupportInWCS

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_fe_part(self) -> '_2739.FEPartSystemDeflection':
        """FEPartSystemDeflection: 'OuterFEPart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterFEPart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_fe_substructure_nodes(self) -> 'List[_2368.FESubstructureNode]':
        """List[FESubstructureNode]: 'OuterFESubstructureNodes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterFESubstructureNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def power_flow_results(self) -> '_4048.ConnectorPowerFlow':
        """ConnectorPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConnectorSystemDeflection._Cast_ConnectorSystemDeflection':
        return self._Cast_ConnectorSystemDeflection(self)
