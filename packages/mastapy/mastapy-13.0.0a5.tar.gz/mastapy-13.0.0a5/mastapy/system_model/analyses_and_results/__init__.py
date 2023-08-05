"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2601 import CompoundAnalysis
    from ._2602 import SingleAnalysis
    from ._2603 import AdvancedSystemDeflectionAnalysis
    from ._2604 import AdvancedSystemDeflectionSubAnalysis
    from ._2605 import AdvancedTimeSteppingAnalysisForModulation
    from ._2606 import CompoundParametricStudyToolAnalysis
    from ._2607 import CriticalSpeedAnalysis
    from ._2608 import DynamicAnalysis
    from ._2609 import DynamicModelAtAStiffnessAnalysis
    from ._2610 import DynamicModelForHarmonicAnalysis
    from ._2611 import DynamicModelForModalAnalysis
    from ._2612 import DynamicModelForStabilityAnalysis
    from ._2613 import DynamicModelForSteadyStateSynchronousResponseAnalysis
    from ._2614 import HarmonicAnalysis
    from ._2615 import HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
    from ._2616 import HarmonicAnalysisOfSingleExcitationAnalysis
    from ._2617 import ModalAnalysis
    from ._2618 import ModalAnalysisAtASpeed
    from ._2619 import ModalAnalysisAtAStiffness
    from ._2620 import ModalAnalysisForHarmonicAnalysis
    from ._2621 import MultibodyDynamicsAnalysis
    from ._2622 import ParametricStudyToolAnalysis
    from ._2623 import PowerFlowAnalysis
    from ._2624 import StabilityAnalysis
    from ._2625 import SteadyStateSynchronousResponseAnalysis
    from ._2626 import SteadyStateSynchronousResponseAtASpeedAnalysis
    from ._2627 import SteadyStateSynchronousResponseOnAShaftAnalysis
    from ._2628 import SystemDeflectionAnalysis
    from ._2629 import TorsionalSystemDeflectionAnalysis
    from ._2630 import AnalysisCaseVariable
    from ._2631 import ConnectionAnalysis
    from ._2632 import Context
    from ._2633 import DesignEntityAnalysis
    from ._2634 import DesignEntityGroupAnalysis
    from ._2635 import DesignEntitySingleContextAnalysis
    from ._2639 import PartAnalysis
    from ._2640 import CompoundAdvancedSystemDeflectionAnalysis
    from ._2641 import CompoundAdvancedSystemDeflectionSubAnalysis
    from ._2642 import CompoundAdvancedTimeSteppingAnalysisForModulation
    from ._2643 import CompoundCriticalSpeedAnalysis
    from ._2644 import CompoundDynamicAnalysis
    from ._2645 import CompoundDynamicModelAtAStiffnessAnalysis
    from ._2646 import CompoundDynamicModelForHarmonicAnalysis
    from ._2647 import CompoundDynamicModelForModalAnalysis
    from ._2648 import CompoundDynamicModelForStabilityAnalysis
    from ._2649 import CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis
    from ._2650 import CompoundHarmonicAnalysis
    from ._2651 import CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
    from ._2652 import CompoundHarmonicAnalysisOfSingleExcitationAnalysis
    from ._2653 import CompoundModalAnalysis
    from ._2654 import CompoundModalAnalysisAtASpeed
    from ._2655 import CompoundModalAnalysisAtAStiffness
    from ._2656 import CompoundModalAnalysisForHarmonicAnalysis
    from ._2657 import CompoundMultibodyDynamicsAnalysis
    from ._2658 import CompoundPowerFlowAnalysis
    from ._2659 import CompoundStabilityAnalysis
    from ._2660 import CompoundSteadyStateSynchronousResponseAnalysis
    from ._2661 import CompoundSteadyStateSynchronousResponseAtASpeedAnalysis
    from ._2662 import CompoundSteadyStateSynchronousResponseOnAShaftAnalysis
    from ._2663 import CompoundSystemDeflectionAnalysis
    from ._2664 import CompoundTorsionalSystemDeflectionAnalysis
    from ._2665 import TESetUpForDynamicAnalysisOptions
    from ._2666 import TimeOptions
else:
    import_structure = {
        '_2601': ['CompoundAnalysis'],
        '_2602': ['SingleAnalysis'],
        '_2603': ['AdvancedSystemDeflectionAnalysis'],
        '_2604': ['AdvancedSystemDeflectionSubAnalysis'],
        '_2605': ['AdvancedTimeSteppingAnalysisForModulation'],
        '_2606': ['CompoundParametricStudyToolAnalysis'],
        '_2607': ['CriticalSpeedAnalysis'],
        '_2608': ['DynamicAnalysis'],
        '_2609': ['DynamicModelAtAStiffnessAnalysis'],
        '_2610': ['DynamicModelForHarmonicAnalysis'],
        '_2611': ['DynamicModelForModalAnalysis'],
        '_2612': ['DynamicModelForStabilityAnalysis'],
        '_2613': ['DynamicModelForSteadyStateSynchronousResponseAnalysis'],
        '_2614': ['HarmonicAnalysis'],
        '_2615': ['HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation'],
        '_2616': ['HarmonicAnalysisOfSingleExcitationAnalysis'],
        '_2617': ['ModalAnalysis'],
        '_2618': ['ModalAnalysisAtASpeed'],
        '_2619': ['ModalAnalysisAtAStiffness'],
        '_2620': ['ModalAnalysisForHarmonicAnalysis'],
        '_2621': ['MultibodyDynamicsAnalysis'],
        '_2622': ['ParametricStudyToolAnalysis'],
        '_2623': ['PowerFlowAnalysis'],
        '_2624': ['StabilityAnalysis'],
        '_2625': ['SteadyStateSynchronousResponseAnalysis'],
        '_2626': ['SteadyStateSynchronousResponseAtASpeedAnalysis'],
        '_2627': ['SteadyStateSynchronousResponseOnAShaftAnalysis'],
        '_2628': ['SystemDeflectionAnalysis'],
        '_2629': ['TorsionalSystemDeflectionAnalysis'],
        '_2630': ['AnalysisCaseVariable'],
        '_2631': ['ConnectionAnalysis'],
        '_2632': ['Context'],
        '_2633': ['DesignEntityAnalysis'],
        '_2634': ['DesignEntityGroupAnalysis'],
        '_2635': ['DesignEntitySingleContextAnalysis'],
        '_2639': ['PartAnalysis'],
        '_2640': ['CompoundAdvancedSystemDeflectionAnalysis'],
        '_2641': ['CompoundAdvancedSystemDeflectionSubAnalysis'],
        '_2642': ['CompoundAdvancedTimeSteppingAnalysisForModulation'],
        '_2643': ['CompoundCriticalSpeedAnalysis'],
        '_2644': ['CompoundDynamicAnalysis'],
        '_2645': ['CompoundDynamicModelAtAStiffnessAnalysis'],
        '_2646': ['CompoundDynamicModelForHarmonicAnalysis'],
        '_2647': ['CompoundDynamicModelForModalAnalysis'],
        '_2648': ['CompoundDynamicModelForStabilityAnalysis'],
        '_2649': ['CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis'],
        '_2650': ['CompoundHarmonicAnalysis'],
        '_2651': ['CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation'],
        '_2652': ['CompoundHarmonicAnalysisOfSingleExcitationAnalysis'],
        '_2653': ['CompoundModalAnalysis'],
        '_2654': ['CompoundModalAnalysisAtASpeed'],
        '_2655': ['CompoundModalAnalysisAtAStiffness'],
        '_2656': ['CompoundModalAnalysisForHarmonicAnalysis'],
        '_2657': ['CompoundMultibodyDynamicsAnalysis'],
        '_2658': ['CompoundPowerFlowAnalysis'],
        '_2659': ['CompoundStabilityAnalysis'],
        '_2660': ['CompoundSteadyStateSynchronousResponseAnalysis'],
        '_2661': ['CompoundSteadyStateSynchronousResponseAtASpeedAnalysis'],
        '_2662': ['CompoundSteadyStateSynchronousResponseOnAShaftAnalysis'],
        '_2663': ['CompoundSystemDeflectionAnalysis'],
        '_2664': ['CompoundTorsionalSystemDeflectionAnalysis'],
        '_2665': ['TESetUpForDynamicAnalysisOptions'],
        '_2666': ['TimeOptions'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
