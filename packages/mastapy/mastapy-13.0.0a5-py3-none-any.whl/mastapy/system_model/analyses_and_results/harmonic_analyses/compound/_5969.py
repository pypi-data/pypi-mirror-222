"""_5969.py

TorqueConverterTurbineCompoundHarmonicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5888
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'TorqueConverterTurbineCompoundHarmonicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2592
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5804


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterTurbineCompoundHarmonicAnalysis',)


class TorqueConverterTurbineCompoundHarmonicAnalysis(_5888.CouplingHalfCompoundHarmonicAnalysis):
    """TorqueConverterTurbineCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_TorqueConverterTurbineCompoundHarmonicAnalysis:
        """Special nested class for casting TorqueConverterTurbineCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'TorqueConverterTurbineCompoundHarmonicAnalysis'):
            self._parent = parent

        @property
        def coupling_half_compound_harmonic_analysis(self):
            return self._parent._cast(_5888.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5926
            
            return self._parent._cast(_5926.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5874
            
            return self._parent._cast(_5874.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5928
            
            return self._parent._cast(_5928.PartCompoundHarmonicAnalysis)

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
        def torque_converter_turbine_compound_harmonic_analysis(self) -> 'TorqueConverterTurbineCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorqueConverterTurbineCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2592.TorqueConverterTurbine':
        """TorqueConverterTurbine: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5804.TorqueConverterTurbineHarmonicAnalysis]':
        """List[TorqueConverterTurbineHarmonicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5804.TorqueConverterTurbineHarmonicAnalysis]':
        """List[TorqueConverterTurbineHarmonicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'TorqueConverterTurbineCompoundHarmonicAnalysis._Cast_TorqueConverterTurbineCompoundHarmonicAnalysis':
        return self._Cast_TorqueConverterTurbineCompoundHarmonicAnalysis(self)
