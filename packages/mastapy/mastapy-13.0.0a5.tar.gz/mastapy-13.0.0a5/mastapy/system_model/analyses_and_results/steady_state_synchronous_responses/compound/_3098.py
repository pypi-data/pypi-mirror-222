"""_3098.py

AbstractAssemblyCompoundSteadyStateSynchronousResponse
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3177
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'AbstractAssemblyCompoundSteadyStateSynchronousResponse')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2965


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractAssemblyCompoundSteadyStateSynchronousResponse',)


class AbstractAssemblyCompoundSteadyStateSynchronousResponse(_3177.PartCompoundSteadyStateSynchronousResponse):
    """AbstractAssemblyCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting AbstractAssemblyCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'AbstractAssemblyCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def part_compound_steady_state_synchronous_response(self):
            return self._parent._cast(_3177.PartCompoundSteadyStateSynchronousResponse)

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
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3104
            
            return self._parent._cast(_3104.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3105
            
            return self._parent._cast(_3105.AssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def belt_drive_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3108
            
            return self._parent._cast(_3108.BeltDriveCompoundSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3111
            
            return self._parent._cast(_3111.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3116
            
            return self._parent._cast(_3116.BevelGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def bolted_joint_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3118
            
            return self._parent._cast(_3118.BoltedJointCompoundSteadyStateSynchronousResponse)

        @property
        def clutch_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3119
            
            return self._parent._cast(_3119.ClutchCompoundSteadyStateSynchronousResponse)

        @property
        def concept_coupling_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3124
            
            return self._parent._cast(_3124.ConceptCouplingCompoundSteadyStateSynchronousResponse)

        @property
        def concept_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3129
            
            return self._parent._cast(_3129.ConceptGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def conical_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3132
            
            return self._parent._cast(_3132.ConicalGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def coupling_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3135
            
            return self._parent._cast(_3135.CouplingCompoundSteadyStateSynchronousResponse)

        @property
        def cvt_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3139
            
            return self._parent._cast(_3139.CVTCompoundSteadyStateSynchronousResponse)

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3141
            
            return self._parent._cast(_3141.CycloidalAssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3147
            
            return self._parent._cast(_3147.CylindricalGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def face_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3153
            
            return self._parent._cast(_3153.FaceGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3155
            
            return self._parent._cast(_3155.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3158
            
            return self._parent._cast(_3158.GearSetCompoundSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3162
            
            return self._parent._cast(_3162.HypoidGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3166
            
            return self._parent._cast(_3166.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3169
            
            return self._parent._cast(_3169.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3172
            
            return self._parent._cast(_3172.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3178
            
            return self._parent._cast(_3178.PartToPartShearCouplingCompoundSteadyStateSynchronousResponse)

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3182
            
            return self._parent._cast(_3182.PlanetaryGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3189
            
            return self._parent._cast(_3189.RollingRingAssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def root_assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3192
            
            return self._parent._cast(_3192.RootAssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3196
            
            return self._parent._cast(_3196.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3199
            
            return self._parent._cast(_3199.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def spring_damper_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3200
            
            return self._parent._cast(_3200.SpringDamperCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3205
            
            return self._parent._cast(_3205.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3208
            
            return self._parent._cast(_3208.StraightBevelGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def synchroniser_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3211
            
            return self._parent._cast(_3211.SynchroniserCompoundSteadyStateSynchronousResponse)

        @property
        def torque_converter_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3215
            
            return self._parent._cast(_3215.TorqueConverterCompoundSteadyStateSynchronousResponse)

        @property
        def worm_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3223
            
            return self._parent._cast(_3223.WormGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3226
            
            return self._parent._cast(_3226.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(self) -> 'AbstractAssemblyCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractAssemblyCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_2965.AbstractAssemblySteadyStateSynchronousResponse]':
        """List[AbstractAssemblySteadyStateSynchronousResponse]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2965.AbstractAssemblySteadyStateSynchronousResponse]':
        """List[AbstractAssemblySteadyStateSynchronousResponse]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse':
        return self._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse(self)
