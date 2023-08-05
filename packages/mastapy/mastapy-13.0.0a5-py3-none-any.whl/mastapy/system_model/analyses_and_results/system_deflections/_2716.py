"""_2716.py

CVTSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2682
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'CVTSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2568
    from mastapy.system_model.analyses_and_results.power_flows import _4053


__docformat__ = 'restructuredtext en'
__all__ = ('CVTSystemDeflection',)


class CVTSystemDeflection(_2682.BeltDriveSystemDeflection):
    """CVTSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CVT_SYSTEM_DEFLECTION

    class _Cast_CVTSystemDeflection:
        """Special nested class for casting CVTSystemDeflection to subclasses."""

        def __init__(self, parent: 'CVTSystemDeflection'):
            self._parent = parent

        @property
        def belt_drive_system_deflection(self):
            return self._parent._cast(_2682.BeltDriveSystemDeflection)

        @property
        def specialised_assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2788
            
            return self._parent._cast(_2788.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2667
            
            return self._parent._cast(_2667.AbstractAssemblySystemDeflection)

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
        def cvt_system_deflection(self) -> 'CVTSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def minimum_belt_clamping_force_safety_factor(self) -> 'float':
        """float: 'MinimumBeltClampingForceSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumBeltClampingForceSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_required_clamping_force(self) -> 'float':
        """float: 'MinimumRequiredClampingForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumRequiredClampingForce

        if temp is None:
            return 0.0

        return temp

    @property
    def assembly_design(self) -> '_2568.CVT':
        """CVT: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4053.CVTPowerFlow':
        """CVTPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CVTSystemDeflection._Cast_CVTSystemDeflection':
        return self._Cast_CVTSystemDeflection(self)
