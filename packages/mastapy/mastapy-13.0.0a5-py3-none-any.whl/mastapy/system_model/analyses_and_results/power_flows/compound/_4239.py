"""_4239.py

RootAssemblyCompoundPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4152
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'RootAssemblyCompoundPowerFlow')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.load_case_groups import _5633
    from mastapy.system_model.analyses_and_results.power_flows import _4109


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyCompoundPowerFlow',)


class RootAssemblyCompoundPowerFlow(_4152.AssemblyCompoundPowerFlow):
    """RootAssemblyCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_POWER_FLOW

    class _Cast_RootAssemblyCompoundPowerFlow:
        """Special nested class for casting RootAssemblyCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'RootAssemblyCompoundPowerFlow'):
            self._parent = parent

        @property
        def assembly_compound_power_flow(self):
            return self._parent._cast(_4152.AssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4145
            
            return self._parent._cast(_4145.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4224
            
            return self._parent._cast(_4224.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7512
            
            return self._parent._cast(_7512.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def root_assembly_compound_power_flow(self) -> 'RootAssemblyCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RootAssemblyCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def compound_static_load(self) -> '_5633.AbstractStaticLoadCaseGroup':
        """AbstractStaticLoadCaseGroup: 'CompoundStaticLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundStaticLoad

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4109.RootAssemblyPowerFlow]':
        """List[RootAssemblyPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4109.RootAssemblyPowerFlow]':
        """List[RootAssemblyPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def set_face_widths_for_specified_safety_factors(self):
        """ 'SetFaceWidthsForSpecifiedSafetyFactors' is the original name of this method."""

        self.wrapped.SetFaceWidthsForSpecifiedSafetyFactors()

    @property
    def cast_to(self) -> 'RootAssemblyCompoundPowerFlow._Cast_RootAssemblyCompoundPowerFlow':
        return self._Cast_RootAssemblyCompoundPowerFlow(self)
