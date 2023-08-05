"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5651 import AbstractAssemblyHarmonicAnalysis
    from ._5652 import AbstractPeriodicExcitationDetail
    from ._5653 import AbstractShaftHarmonicAnalysis
    from ._5654 import AbstractShaftOrHousingHarmonicAnalysis
    from ._5655 import AbstractShaftToMountableComponentConnectionHarmonicAnalysis
    from ._5656 import AGMAGleasonConicalGearHarmonicAnalysis
    from ._5657 import AGMAGleasonConicalGearMeshHarmonicAnalysis
    from ._5658 import AGMAGleasonConicalGearSetHarmonicAnalysis
    from ._5659 import AssemblyHarmonicAnalysis
    from ._5660 import BearingHarmonicAnalysis
    from ._5661 import BeltConnectionHarmonicAnalysis
    from ._5662 import BeltDriveHarmonicAnalysis
    from ._5663 import BevelDifferentialGearHarmonicAnalysis
    from ._5664 import BevelDifferentialGearMeshHarmonicAnalysis
    from ._5665 import BevelDifferentialGearSetHarmonicAnalysis
    from ._5666 import BevelDifferentialPlanetGearHarmonicAnalysis
    from ._5667 import BevelDifferentialSunGearHarmonicAnalysis
    from ._5668 import BevelGearHarmonicAnalysis
    from ._5669 import BevelGearMeshHarmonicAnalysis
    from ._5670 import BevelGearSetHarmonicAnalysis
    from ._5671 import BoltedJointHarmonicAnalysis
    from ._5672 import BoltHarmonicAnalysis
    from ._5673 import ClutchConnectionHarmonicAnalysis
    from ._5674 import ClutchHalfHarmonicAnalysis
    from ._5675 import ClutchHarmonicAnalysis
    from ._5676 import CoaxialConnectionHarmonicAnalysis
    from ._5677 import ComplianceAndForceData
    from ._5678 import ComponentHarmonicAnalysis
    from ._5679 import ConceptCouplingConnectionHarmonicAnalysis
    from ._5680 import ConceptCouplingHalfHarmonicAnalysis
    from ._5681 import ConceptCouplingHarmonicAnalysis
    from ._5682 import ConceptGearHarmonicAnalysis
    from ._5683 import ConceptGearMeshHarmonicAnalysis
    from ._5684 import ConceptGearSetHarmonicAnalysis
    from ._5685 import ConicalGearHarmonicAnalysis
    from ._5686 import ConicalGearMeshHarmonicAnalysis
    from ._5687 import ConicalGearSetHarmonicAnalysis
    from ._5688 import ConnectionHarmonicAnalysis
    from ._5689 import ConnectorHarmonicAnalysis
    from ._5690 import CouplingConnectionHarmonicAnalysis
    from ._5691 import CouplingHalfHarmonicAnalysis
    from ._5692 import CouplingHarmonicAnalysis
    from ._5693 import CVTBeltConnectionHarmonicAnalysis
    from ._5694 import CVTHarmonicAnalysis
    from ._5695 import CVTPulleyHarmonicAnalysis
    from ._5696 import CycloidalAssemblyHarmonicAnalysis
    from ._5697 import CycloidalDiscCentralBearingConnectionHarmonicAnalysis
    from ._5698 import CycloidalDiscHarmonicAnalysis
    from ._5699 import CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis
    from ._5700 import CylindricalGearHarmonicAnalysis
    from ._5701 import CylindricalGearMeshHarmonicAnalysis
    from ._5702 import CylindricalGearSetHarmonicAnalysis
    from ._5703 import CylindricalPlanetGearHarmonicAnalysis
    from ._5704 import DatumHarmonicAnalysis
    from ._2610 import DynamicModelForHarmonicAnalysis
    from ._5705 import ElectricMachinePeriodicExcitationDetail
    from ._5706 import ElectricMachineRotorXForcePeriodicExcitationDetail
    from ._5707 import ElectricMachineRotorXMomentPeriodicExcitationDetail
    from ._5708 import ElectricMachineRotorYForcePeriodicExcitationDetail
    from ._5709 import ElectricMachineRotorYMomentPeriodicExcitationDetail
    from ._5710 import ElectricMachineRotorZForcePeriodicExcitationDetail
    from ._5711 import ElectricMachineStatorToothAxialLoadsExcitationDetail
    from ._5712 import ElectricMachineStatorToothLoadsExcitationDetail
    from ._5713 import ElectricMachineStatorToothMomentsExcitationDetail
    from ._5714 import ElectricMachineStatorToothRadialLoadsExcitationDetail
    from ._5715 import ElectricMachineStatorToothTangentialLoadsExcitationDetail
    from ._5716 import ElectricMachineTorqueRipplePeriodicExcitationDetail
    from ._5717 import ExportOutputType
    from ._5718 import ExternalCADModelHarmonicAnalysis
    from ._5719 import FaceGearHarmonicAnalysis
    from ._5720 import FaceGearMeshHarmonicAnalysis
    from ._5721 import FaceGearSetHarmonicAnalysis
    from ._5722 import FEPartHarmonicAnalysis
    from ._5723 import FlexiblePinAssemblyHarmonicAnalysis
    from ._5724 import FrequencyOptionsForHarmonicAnalysisResults
    from ._5725 import GearHarmonicAnalysis
    from ._5726 import GearMeshExcitationDetail
    from ._5727 import GearMeshHarmonicAnalysis
    from ._5728 import GearMeshMisalignmentExcitationDetail
    from ._5729 import GearMeshTEExcitationDetail
    from ._5730 import GearSetHarmonicAnalysis
    from ._5731 import GeneralPeriodicExcitationDetail
    from ._5732 import GuideDxfModelHarmonicAnalysis
    from ._2614 import HarmonicAnalysis
    from ._5733 import HarmonicAnalysisDrawStyle
    from ._5734 import HarmonicAnalysisExportOptions
    from ._5735 import HarmonicAnalysisFEExportOptions
    from ._2615 import HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
    from ._5736 import HarmonicAnalysisOptions
    from ._5737 import HarmonicAnalysisRootAssemblyExportOptions
    from ._5738 import HarmonicAnalysisShaftExportOptions
    from ._5739 import HarmonicAnalysisTorqueInputType
    from ._5740 import HarmonicAnalysisWithVaryingStiffnessStaticLoadCase
    from ._5741 import HypoidGearHarmonicAnalysis
    from ._5742 import HypoidGearMeshHarmonicAnalysis
    from ._5743 import HypoidGearSetHarmonicAnalysis
    from ._5744 import InterMountableComponentConnectionHarmonicAnalysis
    from ._5745 import KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
    from ._5746 import KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis
    from ._5747 import KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
    from ._5748 import KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
    from ._5749 import KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis
    from ._5750 import KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
    from ._5751 import KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
    from ._5752 import KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis
    from ._5753 import KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
    from ._5754 import MassDiscHarmonicAnalysis
    from ._5755 import MeasurementComponentHarmonicAnalysis
    from ._5756 import MountableComponentHarmonicAnalysis
    from ._5757 import OilSealHarmonicAnalysis
    from ._5758 import PartHarmonicAnalysis
    from ._5759 import PartToPartShearCouplingConnectionHarmonicAnalysis
    from ._5760 import PartToPartShearCouplingHalfHarmonicAnalysis
    from ._5761 import PartToPartShearCouplingHarmonicAnalysis
    from ._5762 import PeriodicExcitationWithReferenceShaft
    from ._5763 import PlanetaryConnectionHarmonicAnalysis
    from ._5764 import PlanetaryGearSetHarmonicAnalysis
    from ._5765 import PlanetCarrierHarmonicAnalysis
    from ._5766 import PointLoadHarmonicAnalysis
    from ._5767 import PowerLoadHarmonicAnalysis
    from ._5768 import PulleyHarmonicAnalysis
    from ._5769 import ResponseCacheLevel
    from ._5770 import RingPinsHarmonicAnalysis
    from ._5771 import RingPinsToDiscConnectionHarmonicAnalysis
    from ._5772 import RollingRingAssemblyHarmonicAnalysis
    from ._5773 import RollingRingConnectionHarmonicAnalysis
    from ._5774 import RollingRingHarmonicAnalysis
    from ._5775 import RootAssemblyHarmonicAnalysis
    from ._5776 import ShaftHarmonicAnalysis
    from ._5777 import ShaftHubConnectionHarmonicAnalysis
    from ._5778 import ShaftToMountableComponentConnectionHarmonicAnalysis
    from ._5779 import SingleNodePeriodicExcitationWithReferenceShaft
    from ._5780 import SpecialisedAssemblyHarmonicAnalysis
    from ._5781 import SpeedOptionsForHarmonicAnalysisResults
    from ._5782 import SpiralBevelGearHarmonicAnalysis
    from ._5783 import SpiralBevelGearMeshHarmonicAnalysis
    from ._5784 import SpiralBevelGearSetHarmonicAnalysis
    from ._5785 import SpringDamperConnectionHarmonicAnalysis
    from ._5786 import SpringDamperHalfHarmonicAnalysis
    from ._5787 import SpringDamperHarmonicAnalysis
    from ._5788 import StiffnessOptionsForHarmonicAnalysis
    from ._5789 import StraightBevelDiffGearHarmonicAnalysis
    from ._5790 import StraightBevelDiffGearMeshHarmonicAnalysis
    from ._5791 import StraightBevelDiffGearSetHarmonicAnalysis
    from ._5792 import StraightBevelGearHarmonicAnalysis
    from ._5793 import StraightBevelGearMeshHarmonicAnalysis
    from ._5794 import StraightBevelGearSetHarmonicAnalysis
    from ._5795 import StraightBevelPlanetGearHarmonicAnalysis
    from ._5796 import StraightBevelSunGearHarmonicAnalysis
    from ._5797 import SynchroniserHalfHarmonicAnalysis
    from ._5798 import SynchroniserHarmonicAnalysis
    from ._5799 import SynchroniserPartHarmonicAnalysis
    from ._5800 import SynchroniserSleeveHarmonicAnalysis
    from ._5801 import TorqueConverterConnectionHarmonicAnalysis
    from ._5802 import TorqueConverterHarmonicAnalysis
    from ._5803 import TorqueConverterPumpHarmonicAnalysis
    from ._5804 import TorqueConverterTurbineHarmonicAnalysis
    from ._5805 import UnbalancedMassExcitationDetail
    from ._5806 import UnbalancedMassHarmonicAnalysis
    from ._5807 import VirtualComponentHarmonicAnalysis
    from ._5808 import WormGearHarmonicAnalysis
    from ._5809 import WormGearMeshHarmonicAnalysis
    from ._5810 import WormGearSetHarmonicAnalysis
    from ._5811 import ZerolBevelGearHarmonicAnalysis
    from ._5812 import ZerolBevelGearMeshHarmonicAnalysis
    from ._5813 import ZerolBevelGearSetHarmonicAnalysis
else:
    import_structure = {
        '_5651': ['AbstractAssemblyHarmonicAnalysis'],
        '_5652': ['AbstractPeriodicExcitationDetail'],
        '_5653': ['AbstractShaftHarmonicAnalysis'],
        '_5654': ['AbstractShaftOrHousingHarmonicAnalysis'],
        '_5655': ['AbstractShaftToMountableComponentConnectionHarmonicAnalysis'],
        '_5656': ['AGMAGleasonConicalGearHarmonicAnalysis'],
        '_5657': ['AGMAGleasonConicalGearMeshHarmonicAnalysis'],
        '_5658': ['AGMAGleasonConicalGearSetHarmonicAnalysis'],
        '_5659': ['AssemblyHarmonicAnalysis'],
        '_5660': ['BearingHarmonicAnalysis'],
        '_5661': ['BeltConnectionHarmonicAnalysis'],
        '_5662': ['BeltDriveHarmonicAnalysis'],
        '_5663': ['BevelDifferentialGearHarmonicAnalysis'],
        '_5664': ['BevelDifferentialGearMeshHarmonicAnalysis'],
        '_5665': ['BevelDifferentialGearSetHarmonicAnalysis'],
        '_5666': ['BevelDifferentialPlanetGearHarmonicAnalysis'],
        '_5667': ['BevelDifferentialSunGearHarmonicAnalysis'],
        '_5668': ['BevelGearHarmonicAnalysis'],
        '_5669': ['BevelGearMeshHarmonicAnalysis'],
        '_5670': ['BevelGearSetHarmonicAnalysis'],
        '_5671': ['BoltedJointHarmonicAnalysis'],
        '_5672': ['BoltHarmonicAnalysis'],
        '_5673': ['ClutchConnectionHarmonicAnalysis'],
        '_5674': ['ClutchHalfHarmonicAnalysis'],
        '_5675': ['ClutchHarmonicAnalysis'],
        '_5676': ['CoaxialConnectionHarmonicAnalysis'],
        '_5677': ['ComplianceAndForceData'],
        '_5678': ['ComponentHarmonicAnalysis'],
        '_5679': ['ConceptCouplingConnectionHarmonicAnalysis'],
        '_5680': ['ConceptCouplingHalfHarmonicAnalysis'],
        '_5681': ['ConceptCouplingHarmonicAnalysis'],
        '_5682': ['ConceptGearHarmonicAnalysis'],
        '_5683': ['ConceptGearMeshHarmonicAnalysis'],
        '_5684': ['ConceptGearSetHarmonicAnalysis'],
        '_5685': ['ConicalGearHarmonicAnalysis'],
        '_5686': ['ConicalGearMeshHarmonicAnalysis'],
        '_5687': ['ConicalGearSetHarmonicAnalysis'],
        '_5688': ['ConnectionHarmonicAnalysis'],
        '_5689': ['ConnectorHarmonicAnalysis'],
        '_5690': ['CouplingConnectionHarmonicAnalysis'],
        '_5691': ['CouplingHalfHarmonicAnalysis'],
        '_5692': ['CouplingHarmonicAnalysis'],
        '_5693': ['CVTBeltConnectionHarmonicAnalysis'],
        '_5694': ['CVTHarmonicAnalysis'],
        '_5695': ['CVTPulleyHarmonicAnalysis'],
        '_5696': ['CycloidalAssemblyHarmonicAnalysis'],
        '_5697': ['CycloidalDiscCentralBearingConnectionHarmonicAnalysis'],
        '_5698': ['CycloidalDiscHarmonicAnalysis'],
        '_5699': ['CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis'],
        '_5700': ['CylindricalGearHarmonicAnalysis'],
        '_5701': ['CylindricalGearMeshHarmonicAnalysis'],
        '_5702': ['CylindricalGearSetHarmonicAnalysis'],
        '_5703': ['CylindricalPlanetGearHarmonicAnalysis'],
        '_5704': ['DatumHarmonicAnalysis'],
        '_2610': ['DynamicModelForHarmonicAnalysis'],
        '_5705': ['ElectricMachinePeriodicExcitationDetail'],
        '_5706': ['ElectricMachineRotorXForcePeriodicExcitationDetail'],
        '_5707': ['ElectricMachineRotorXMomentPeriodicExcitationDetail'],
        '_5708': ['ElectricMachineRotorYForcePeriodicExcitationDetail'],
        '_5709': ['ElectricMachineRotorYMomentPeriodicExcitationDetail'],
        '_5710': ['ElectricMachineRotorZForcePeriodicExcitationDetail'],
        '_5711': ['ElectricMachineStatorToothAxialLoadsExcitationDetail'],
        '_5712': ['ElectricMachineStatorToothLoadsExcitationDetail'],
        '_5713': ['ElectricMachineStatorToothMomentsExcitationDetail'],
        '_5714': ['ElectricMachineStatorToothRadialLoadsExcitationDetail'],
        '_5715': ['ElectricMachineStatorToothTangentialLoadsExcitationDetail'],
        '_5716': ['ElectricMachineTorqueRipplePeriodicExcitationDetail'],
        '_5717': ['ExportOutputType'],
        '_5718': ['ExternalCADModelHarmonicAnalysis'],
        '_5719': ['FaceGearHarmonicAnalysis'],
        '_5720': ['FaceGearMeshHarmonicAnalysis'],
        '_5721': ['FaceGearSetHarmonicAnalysis'],
        '_5722': ['FEPartHarmonicAnalysis'],
        '_5723': ['FlexiblePinAssemblyHarmonicAnalysis'],
        '_5724': ['FrequencyOptionsForHarmonicAnalysisResults'],
        '_5725': ['GearHarmonicAnalysis'],
        '_5726': ['GearMeshExcitationDetail'],
        '_5727': ['GearMeshHarmonicAnalysis'],
        '_5728': ['GearMeshMisalignmentExcitationDetail'],
        '_5729': ['GearMeshTEExcitationDetail'],
        '_5730': ['GearSetHarmonicAnalysis'],
        '_5731': ['GeneralPeriodicExcitationDetail'],
        '_5732': ['GuideDxfModelHarmonicAnalysis'],
        '_2614': ['HarmonicAnalysis'],
        '_5733': ['HarmonicAnalysisDrawStyle'],
        '_5734': ['HarmonicAnalysisExportOptions'],
        '_5735': ['HarmonicAnalysisFEExportOptions'],
        '_2615': ['HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation'],
        '_5736': ['HarmonicAnalysisOptions'],
        '_5737': ['HarmonicAnalysisRootAssemblyExportOptions'],
        '_5738': ['HarmonicAnalysisShaftExportOptions'],
        '_5739': ['HarmonicAnalysisTorqueInputType'],
        '_5740': ['HarmonicAnalysisWithVaryingStiffnessStaticLoadCase'],
        '_5741': ['HypoidGearHarmonicAnalysis'],
        '_5742': ['HypoidGearMeshHarmonicAnalysis'],
        '_5743': ['HypoidGearSetHarmonicAnalysis'],
        '_5744': ['InterMountableComponentConnectionHarmonicAnalysis'],
        '_5745': ['KlingelnbergCycloPalloidConicalGearHarmonicAnalysis'],
        '_5746': ['KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis'],
        '_5747': ['KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis'],
        '_5748': ['KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis'],
        '_5749': ['KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis'],
        '_5750': ['KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis'],
        '_5751': ['KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis'],
        '_5752': ['KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis'],
        '_5753': ['KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis'],
        '_5754': ['MassDiscHarmonicAnalysis'],
        '_5755': ['MeasurementComponentHarmonicAnalysis'],
        '_5756': ['MountableComponentHarmonicAnalysis'],
        '_5757': ['OilSealHarmonicAnalysis'],
        '_5758': ['PartHarmonicAnalysis'],
        '_5759': ['PartToPartShearCouplingConnectionHarmonicAnalysis'],
        '_5760': ['PartToPartShearCouplingHalfHarmonicAnalysis'],
        '_5761': ['PartToPartShearCouplingHarmonicAnalysis'],
        '_5762': ['PeriodicExcitationWithReferenceShaft'],
        '_5763': ['PlanetaryConnectionHarmonicAnalysis'],
        '_5764': ['PlanetaryGearSetHarmonicAnalysis'],
        '_5765': ['PlanetCarrierHarmonicAnalysis'],
        '_5766': ['PointLoadHarmonicAnalysis'],
        '_5767': ['PowerLoadHarmonicAnalysis'],
        '_5768': ['PulleyHarmonicAnalysis'],
        '_5769': ['ResponseCacheLevel'],
        '_5770': ['RingPinsHarmonicAnalysis'],
        '_5771': ['RingPinsToDiscConnectionHarmonicAnalysis'],
        '_5772': ['RollingRingAssemblyHarmonicAnalysis'],
        '_5773': ['RollingRingConnectionHarmonicAnalysis'],
        '_5774': ['RollingRingHarmonicAnalysis'],
        '_5775': ['RootAssemblyHarmonicAnalysis'],
        '_5776': ['ShaftHarmonicAnalysis'],
        '_5777': ['ShaftHubConnectionHarmonicAnalysis'],
        '_5778': ['ShaftToMountableComponentConnectionHarmonicAnalysis'],
        '_5779': ['SingleNodePeriodicExcitationWithReferenceShaft'],
        '_5780': ['SpecialisedAssemblyHarmonicAnalysis'],
        '_5781': ['SpeedOptionsForHarmonicAnalysisResults'],
        '_5782': ['SpiralBevelGearHarmonicAnalysis'],
        '_5783': ['SpiralBevelGearMeshHarmonicAnalysis'],
        '_5784': ['SpiralBevelGearSetHarmonicAnalysis'],
        '_5785': ['SpringDamperConnectionHarmonicAnalysis'],
        '_5786': ['SpringDamperHalfHarmonicAnalysis'],
        '_5787': ['SpringDamperHarmonicAnalysis'],
        '_5788': ['StiffnessOptionsForHarmonicAnalysis'],
        '_5789': ['StraightBevelDiffGearHarmonicAnalysis'],
        '_5790': ['StraightBevelDiffGearMeshHarmonicAnalysis'],
        '_5791': ['StraightBevelDiffGearSetHarmonicAnalysis'],
        '_5792': ['StraightBevelGearHarmonicAnalysis'],
        '_5793': ['StraightBevelGearMeshHarmonicAnalysis'],
        '_5794': ['StraightBevelGearSetHarmonicAnalysis'],
        '_5795': ['StraightBevelPlanetGearHarmonicAnalysis'],
        '_5796': ['StraightBevelSunGearHarmonicAnalysis'],
        '_5797': ['SynchroniserHalfHarmonicAnalysis'],
        '_5798': ['SynchroniserHarmonicAnalysis'],
        '_5799': ['SynchroniserPartHarmonicAnalysis'],
        '_5800': ['SynchroniserSleeveHarmonicAnalysis'],
        '_5801': ['TorqueConverterConnectionHarmonicAnalysis'],
        '_5802': ['TorqueConverterHarmonicAnalysis'],
        '_5803': ['TorqueConverterPumpHarmonicAnalysis'],
        '_5804': ['TorqueConverterTurbineHarmonicAnalysis'],
        '_5805': ['UnbalancedMassExcitationDetail'],
        '_5806': ['UnbalancedMassHarmonicAnalysis'],
        '_5807': ['VirtualComponentHarmonicAnalysis'],
        '_5808': ['WormGearHarmonicAnalysis'],
        '_5809': ['WormGearMeshHarmonicAnalysis'],
        '_5810': ['WormGearSetHarmonicAnalysis'],
        '_5811': ['ZerolBevelGearHarmonicAnalysis'],
        '_5812': ['ZerolBevelGearMeshHarmonicAnalysis'],
        '_5813': ['ZerolBevelGearSetHarmonicAnalysis'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
