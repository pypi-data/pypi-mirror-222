"""_4200.py

FaceGearSetCompoundPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4205
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'FaceGearSetCompoundPowerFlow')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2511
    from mastapy.system_model.analyses_and_results.power_flows import _4068
    from mastapy.system_model.analyses_and_results.power_flows.compound import _4198, _4199


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetCompoundPowerFlow',)


class FaceGearSetCompoundPowerFlow(_4205.GearSetCompoundPowerFlow):
    """FaceGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_COMPOUND_POWER_FLOW

    class _Cast_FaceGearSetCompoundPowerFlow:
        """Special nested class for casting FaceGearSetCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'FaceGearSetCompoundPowerFlow'):
            self._parent = parent

        @property
        def gear_set_compound_power_flow(self):
            return self._parent._cast(_4205.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4243
            
            return self._parent._cast(_4243.SpecialisedAssemblyCompoundPowerFlow)

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
        def face_gear_set_compound_power_flow(self) -> 'FaceGearSetCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGearSetCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2511.FaceGearSet':
        """FaceGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2511.FaceGearSet':
        """FaceGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4068.FaceGearSetPowerFlow]':
        """List[FaceGearSetPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_gears_compound_power_flow(self) -> 'List[_4198.FaceGearCompoundPowerFlow]':
        """List[FaceGearCompoundPowerFlow]: 'FaceGearsCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearsCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_meshes_compound_power_flow(self) -> 'List[_4199.FaceGearMeshCompoundPowerFlow]':
        """List[FaceGearMeshCompoundPowerFlow]: 'FaceMeshesCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshesCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4068.FaceGearSetPowerFlow]':
        """List[FaceGearSetPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FaceGearSetCompoundPowerFlow._Cast_FaceGearSetCompoundPowerFlow':
        return self._Cast_FaceGearSetCompoundPowerFlow(self)
