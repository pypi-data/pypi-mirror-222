﻿"""_2783.py

ShaftHubConnectionSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2710
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ShaftHubConnectionSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2580
    from mastapy.detailed_rigid_connectors.rating import _1426
    from mastapy.system_model.analyses_and_results.static_loads import _6917
    from mastapy.system_model.analyses_and_results.power_flows import _4110
    from mastapy.bearings.bearing_results import _1928
    from mastapy.system_model.analyses_and_results.system_deflections.reporting import _2832


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftHubConnectionSystemDeflection',)


class ShaftHubConnectionSystemDeflection(_2710.ConnectorSystemDeflection):
    """ShaftHubConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_SYSTEM_DEFLECTION

    class _Cast_ShaftHubConnectionSystemDeflection:
        """Special nested class for casting ShaftHubConnectionSystemDeflection to subclasses."""

        def __init__(self, parent: 'ShaftHubConnectionSystemDeflection'):
            self._parent = parent

        @property
        def connector_system_deflection(self):
            return self._parent._cast(_2710.ConnectorSystemDeflection)

        @property
        def mountable_component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2764
            
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
        def shaft_hub_connection_system_deflection(self) -> 'ShaftHubConnectionSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftHubConnectionSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def limiting_friction(self) -> 'float':
        """float: 'LimitingFriction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LimitingFriction

        if temp is None:
            return 0.0

        return temp

    @property
    def node_pair_separations(self) -> 'List[float]':
        """List[float]: 'NodePairSeparations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairSeparations

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def node_radial_forces_on_inner(self) -> 'List[float]':
        """List[float]: 'NodeRadialForcesOnInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodeRadialForcesOnInner

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def normal_deflection_left_flank(self) -> 'List[float]':
        """List[float]: 'NormalDeflectionLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalDeflectionLeftFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def normal_deflection_right_flank(self) -> 'List[float]':
        """List[float]: 'NormalDeflectionRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalDeflectionRightFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def normal_deflection_tooth_centre(self) -> 'List[float]':
        """List[float]: 'NormalDeflectionToothCentre' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalDeflectionToothCentre

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def normal_force_left_flank(self) -> 'List[float]':
        """List[float]: 'NormalForceLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalForceLeftFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def normal_force_right_flank(self) -> 'List[float]':
        """List[float]: 'NormalForceRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalForceRightFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def normal_force_tooth_centre(self) -> 'List[float]':
        """List[float]: 'NormalForceToothCentre' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalForceToothCentre

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def normal_stiffness_left_flank(self) -> 'List[float]':
        """List[float]: 'NormalStiffnessLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalStiffnessLeftFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def normal_stiffness_right_flank(self) -> 'List[float]':
        """List[float]: 'NormalStiffnessRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalStiffnessRightFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def normal_stiffness_tooth_centre(self) -> 'List[float]':
        """List[float]: 'NormalStiffnessToothCentre' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalStiffnessToothCentre

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def number_of_major_diameter_contacts(self) -> 'int':
        """int: 'NumberOfMajorDiameterContacts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfMajorDiameterContacts

        if temp is None:
            return 0

        return temp

    @property
    def number_of_teeth_in_contact(self) -> 'int':
        """int: 'NumberOfTeethInContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfTeethInContact

        if temp is None:
            return 0

        return temp

    @property
    def tangential_force_left_flank(self) -> 'List[float]':
        """List[float]: 'TangentialForceLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TangentialForceLeftFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def tangential_force_right_flank(self) -> 'List[float]':
        """List[float]: 'TangentialForceRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TangentialForceRightFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def tangential_force_tooth_centre(self) -> 'List[float]':
        """List[float]: 'TangentialForceToothCentre' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TangentialForceToothCentre

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def tangential_force_on_spline(self) -> 'float':
        """float: 'TangentialForceOnSpline' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TangentialForceOnSpline

        if temp is None:
            return 0.0

        return temp

    @property
    def will_spline_slip(self) -> 'bool':
        """bool: 'WillSplineSlip' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WillSplineSlip

        if temp is None:
            return False

        return temp

    @property
    def component_design(self) -> '_2580.ShaftHubConnection':
        """ShaftHubConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_1426.ShaftHubConnectionRating':
        """ShaftHubConnectionRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6917.ShaftHubConnectionLoadCase':
        """ShaftHubConnectionLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4110.ShaftHubConnectionPowerFlow':
        """ShaftHubConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stiffness_matrix_in_local_coordinate_system(self) -> '_1928.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'StiffnessMatrixInLocalCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessMatrixInLocalCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stiffness_matrix_in_unrotated_coordinate_system(self) -> '_1928.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'StiffnessMatrixInUnrotatedCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessMatrixInUnrotatedCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def left_flank_contacts(self) -> 'List[_2832.SplineFlankContactReporting]':
        """List[SplineFlankContactReporting]: 'LeftFlankContacts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlankContacts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[ShaftHubConnectionSystemDeflection]':
        """List[ShaftHubConnectionSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def right_flank_contacts(self) -> 'List[_2832.SplineFlankContactReporting]':
        """List[SplineFlankContactReporting]: 'RightFlankContacts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlankContacts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def tip_contacts(self) -> 'List[_2832.SplineFlankContactReporting]':
        """List[SplineFlankContactReporting]: 'TipContacts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TipContacts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ShaftHubConnectionSystemDeflection._Cast_ShaftHubConnectionSystemDeflection':
        return self._Cast_ShaftHubConnectionSystemDeflection(self)
