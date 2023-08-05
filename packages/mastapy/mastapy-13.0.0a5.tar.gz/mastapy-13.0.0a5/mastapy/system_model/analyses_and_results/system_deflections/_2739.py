﻿"""_2739.py

FEPartSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2668
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'FEPartSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2436
    from mastapy.system_model.analyses_and_results.static_loads import _6855
    from mastapy.nodal_analysis.component_mode_synthesis import _233
    from mastapy.nodal_analysis import _79
    from mastapy.system_model.analyses_and_results.power_flows import _4069
    from mastapy.math_utility.measured_vectors import _1555, _1551
    from mastapy.system_model.fe import _2393


__docformat__ = 'restructuredtext en'
__all__ = ('FEPartSystemDeflection',)


class FEPartSystemDeflection(_2668.AbstractShaftOrHousingSystemDeflection):
    """FEPartSystemDeflection

    This is a mastapy class.
    """

    TYPE = _FE_PART_SYSTEM_DEFLECTION

    class _Cast_FEPartSystemDeflection:
        """Special nested class for casting FEPartSystemDeflection to subclasses."""

        def __init__(self, parent: 'FEPartSystemDeflection'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_system_deflection(self):
            return self._parent._cast(_2668.AbstractShaftOrHousingSystemDeflection)

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
        def fe_part_system_deflection(self) -> 'FEPartSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEPartSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2436.FEPart':
        """FEPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6855.FEPartLoadCase':
        """FEPartLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def full_fe_results(self) -> '_233.StaticCMSResults':
        """StaticCMSResults: 'FullFEResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FullFEResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mass_in_world_coordinate_system_mn_rad_s_kg(self) -> '_79.NodalMatrix':
        """NodalMatrix: 'MassInWorldCoordinateSystemMNRadSKg' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassInWorldCoordinateSystemMNRadSKg

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4069.FEPartPowerFlow':
        """FEPartPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stiffness_in_world_coordinate_system_mn_rad(self) -> '_79.NodalMatrix':
        """NodalMatrix: 'StiffnessInWorldCoordinateSystemMNRad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessInWorldCoordinateSystemMNRad

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def applied_internal_forces_in_world_coordinate_system(self) -> 'List[_1555.VectorWithLinearAndAngularComponents]':
        """List[VectorWithLinearAndAngularComponents]: 'AppliedInternalForcesInWorldCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AppliedInternalForcesInWorldCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def node_results_in_shaft_coordinate_system(self) -> 'List[_1551.ForceAndDisplacementResults]':
        """List[ForceAndDisplacementResults]: 'NodeResultsInShaftCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodeResultsInShaftCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[FEPartSystemDeflection]':
        """List[FEPartSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def export(self) -> '_2393.SystemDeflectionFEExportOptions':
        """SystemDeflectionFEExportOptions: 'Export' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Export

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def export_displacements(self):
        """ 'ExportDisplacements' is the original name of this method."""

        self.wrapped.ExportDisplacements()

    def export_forces(self):
        """ 'ExportForces' is the original name of this method."""

        self.wrapped.ExportForces()

    @property
    def cast_to(self) -> 'FEPartSystemDeflection._Cast_FEPartSystemDeflection':
        return self._Cast_FEPartSystemDeflection(self)
