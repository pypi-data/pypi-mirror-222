"""_6436.py

GearSetCompoundDynamicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6474
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'GearSetCompoundDynamicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetCompoundDynamicAnalysis',)


class GearSetCompoundDynamicAnalysis(_6474.SpecialisedAssemblyCompoundDynamicAnalysis):
    """GearSetCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_GearSetCompoundDynamicAnalysis:
        """Special nested class for casting GearSetCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'GearSetCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def specialised_assembly_compound_dynamic_analysis(self):
            return self._parent._cast(_6474.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6376
            
            return self._parent._cast(_6376.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6455
            
            return self._parent._cast(_6455.PartCompoundDynamicAnalysis)

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
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6382
            
            return self._parent._cast(_6382.AGMAGleasonConicalGearSetCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6389
            
            return self._parent._cast(_6389.BevelDifferentialGearSetCompoundDynamicAnalysis)

        @property
        def bevel_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6394
            
            return self._parent._cast(_6394.BevelGearSetCompoundDynamicAnalysis)

        @property
        def concept_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6407
            
            return self._parent._cast(_6407.ConceptGearSetCompoundDynamicAnalysis)

        @property
        def conical_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6410
            
            return self._parent._cast(_6410.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6425
            
            return self._parent._cast(_6425.CylindricalGearSetCompoundDynamicAnalysis)

        @property
        def face_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6431
            
            return self._parent._cast(_6431.FaceGearSetCompoundDynamicAnalysis)

        @property
        def hypoid_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6440
            
            return self._parent._cast(_6440.HypoidGearSetCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6444
            
            return self._parent._cast(_6444.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6447
            
            return self._parent._cast(_6447.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6450
            
            return self._parent._cast(_6450.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def planetary_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6460
            
            return self._parent._cast(_6460.PlanetaryGearSetCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6477
            
            return self._parent._cast(_6477.SpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6483
            
            return self._parent._cast(_6483.StraightBevelDiffGearSetCompoundDynamicAnalysis)

        @property
        def straight_bevel_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6486
            
            return self._parent._cast(_6486.StraightBevelGearSetCompoundDynamicAnalysis)

        @property
        def worm_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6501
            
            return self._parent._cast(_6501.WormGearSetCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6504
            
            return self._parent._cast(_6504.ZerolBevelGearSetCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(self) -> 'GearSetCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_6307.GearSetDynamicAnalysis]':
        """List[GearSetDynamicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6307.GearSetDynamicAnalysis]':
        """List[GearSetDynamicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis':
        return self._Cast_GearSetCompoundDynamicAnalysis(self)
