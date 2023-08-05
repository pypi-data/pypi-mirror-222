"""_4883.py

CylindricalPlanetGearModalAnalysisAtAStiffness
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4881
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'CylindricalPlanetGearModalAnalysisAtAStiffness')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2509


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalPlanetGearModalAnalysisAtAStiffness',)


class CylindricalPlanetGearModalAnalysisAtAStiffness(_4881.CylindricalGearModalAnalysisAtAStiffness):
    """CylindricalPlanetGearModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_CylindricalPlanetGearModalAnalysisAtAStiffness:
        """Special nested class for casting CylindricalPlanetGearModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'CylindricalPlanetGearModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def cylindrical_gear_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4881.CylindricalGearModalAnalysisAtAStiffness)

        @property
        def gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4893
            
            return self._parent._cast(_4893.GearModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4911
            
            return self._parent._cast(_4911.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4858
            
            return self._parent._cast(_4858.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4913
            
            return self._parent._cast(_4913.PartModalAnalysisAtAStiffness)

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
        def cylindrical_planet_gear_modal_analysis_at_a_stiffness(self) -> 'CylindricalPlanetGearModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalPlanetGearModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2509.CylindricalPlanetGear':
        """CylindricalPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness':
        return self._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness(self)
