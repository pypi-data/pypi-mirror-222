"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4550 import AbstractAssemblyModalAnalysis
    from ._4551 import AbstractShaftModalAnalysis
    from ._4552 import AbstractShaftOrHousingModalAnalysis
    from ._4553 import AbstractShaftToMountableComponentConnectionModalAnalysis
    from ._4554 import AGMAGleasonConicalGearMeshModalAnalysis
    from ._4555 import AGMAGleasonConicalGearModalAnalysis
    from ._4556 import AGMAGleasonConicalGearSetModalAnalysis
    from ._4557 import AssemblyModalAnalysis
    from ._4558 import BearingModalAnalysis
    from ._4559 import BeltConnectionModalAnalysis
    from ._4560 import BeltDriveModalAnalysis
    from ._4561 import BevelDifferentialGearMeshModalAnalysis
    from ._4562 import BevelDifferentialGearModalAnalysis
    from ._4563 import BevelDifferentialGearSetModalAnalysis
    from ._4564 import BevelDifferentialPlanetGearModalAnalysis
    from ._4565 import BevelDifferentialSunGearModalAnalysis
    from ._4566 import BevelGearMeshModalAnalysis
    from ._4567 import BevelGearModalAnalysis
    from ._4568 import BevelGearSetModalAnalysis
    from ._4569 import BoltedJointModalAnalysis
    from ._4570 import BoltModalAnalysis
    from ._4571 import ClutchConnectionModalAnalysis
    from ._4572 import ClutchHalfModalAnalysis
    from ._4573 import ClutchModalAnalysis
    from ._4574 import CoaxialConnectionModalAnalysis
    from ._4575 import ComponentModalAnalysis
    from ._4576 import ConceptCouplingConnectionModalAnalysis
    from ._4577 import ConceptCouplingHalfModalAnalysis
    from ._4578 import ConceptCouplingModalAnalysis
    from ._4579 import ConceptGearMeshModalAnalysis
    from ._4580 import ConceptGearModalAnalysis
    from ._4581 import ConceptGearSetModalAnalysis
    from ._4582 import ConicalGearMeshModalAnalysis
    from ._4583 import ConicalGearModalAnalysis
    from ._4584 import ConicalGearSetModalAnalysis
    from ._4585 import ConnectionModalAnalysis
    from ._4586 import ConnectorModalAnalysis
    from ._4587 import CoordinateSystemForWhine
    from ._4588 import CouplingConnectionModalAnalysis
    from ._4589 import CouplingHalfModalAnalysis
    from ._4590 import CouplingModalAnalysis
    from ._4591 import CVTBeltConnectionModalAnalysis
    from ._4592 import CVTModalAnalysis
    from ._4593 import CVTPulleyModalAnalysis
    from ._4594 import CycloidalAssemblyModalAnalysis
    from ._4595 import CycloidalDiscCentralBearingConnectionModalAnalysis
    from ._4596 import CycloidalDiscModalAnalysis
    from ._4597 import CycloidalDiscPlanetaryBearingConnectionModalAnalysis
    from ._4598 import CylindricalGearMeshModalAnalysis
    from ._4599 import CylindricalGearModalAnalysis
    from ._4600 import CylindricalGearSetModalAnalysis
    from ._4601 import CylindricalPlanetGearModalAnalysis
    from ._4602 import DatumModalAnalysis
    from ._2611 import DynamicModelForModalAnalysis
    from ._4603 import DynamicsResponse3DChartType
    from ._4604 import DynamicsResponseType
    from ._4605 import ExternalCADModelModalAnalysis
    from ._4606 import FaceGearMeshModalAnalysis
    from ._4607 import FaceGearModalAnalysis
    from ._4608 import FaceGearSetModalAnalysis
    from ._4609 import FEPartModalAnalysis
    from ._4610 import FlexiblePinAssemblyModalAnalysis
    from ._4611 import FrequencyResponseAnalysisOptions
    from ._4612 import GearMeshModalAnalysis
    from ._4613 import GearModalAnalysis
    from ._4614 import GearSetModalAnalysis
    from ._4615 import GuideDxfModelModalAnalysis
    from ._4616 import HypoidGearMeshModalAnalysis
    from ._4617 import HypoidGearModalAnalysis
    from ._4618 import HypoidGearSetModalAnalysis
    from ._4619 import InterMountableComponentConnectionModalAnalysis
    from ._4620 import KlingelnbergCycloPalloidConicalGearMeshModalAnalysis
    from ._4621 import KlingelnbergCycloPalloidConicalGearModalAnalysis
    from ._4622 import KlingelnbergCycloPalloidConicalGearSetModalAnalysis
    from ._4623 import KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis
    from ._4624 import KlingelnbergCycloPalloidHypoidGearModalAnalysis
    from ._4625 import KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
    from ._4626 import KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis
    from ._4627 import KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
    from ._4628 import KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
    from ._4629 import MassDiscModalAnalysis
    from ._4630 import MeasurementComponentModalAnalysis
    from ._2617 import ModalAnalysis
    from ._4631 import ModalAnalysisBarModelFEExportOptions
    from ._4632 import ModalAnalysisDrawStyle
    from ._4633 import ModalAnalysisOptions
    from ._4634 import MountableComponentModalAnalysis
    from ._4635 import MultipleExcitationsSpeedRangeOption
    from ._4636 import OilSealModalAnalysis
    from ._4637 import OrderCutsChartSettings
    from ._4638 import PartModalAnalysis
    from ._4639 import PartToPartShearCouplingConnectionModalAnalysis
    from ._4640 import PartToPartShearCouplingHalfModalAnalysis
    from ._4641 import PartToPartShearCouplingModalAnalysis
    from ._4642 import PlanetaryConnectionModalAnalysis
    from ._4643 import PlanetaryGearSetModalAnalysis
    from ._4644 import PlanetCarrierModalAnalysis
    from ._4645 import PointLoadModalAnalysis
    from ._4646 import PowerLoadModalAnalysis
    from ._4647 import PulleyModalAnalysis
    from ._4648 import RingPinsModalAnalysis
    from ._4649 import RingPinsToDiscConnectionModalAnalysis
    from ._4650 import RollingRingAssemblyModalAnalysis
    from ._4651 import RollingRingConnectionModalAnalysis
    from ._4652 import RollingRingModalAnalysis
    from ._4653 import RootAssemblyModalAnalysis
    from ._4654 import ShaftHubConnectionModalAnalysis
    from ._4655 import ShaftModalAnalysis
    from ._4656 import ShaftModalAnalysisMode
    from ._4657 import ShaftToMountableComponentConnectionModalAnalysis
    from ._4658 import SpecialisedAssemblyModalAnalysis
    from ._4659 import SpiralBevelGearMeshModalAnalysis
    from ._4660 import SpiralBevelGearModalAnalysis
    from ._4661 import SpiralBevelGearSetModalAnalysis
    from ._4662 import SpringDamperConnectionModalAnalysis
    from ._4663 import SpringDamperHalfModalAnalysis
    from ._4664 import SpringDamperModalAnalysis
    from ._4665 import StraightBevelDiffGearMeshModalAnalysis
    from ._4666 import StraightBevelDiffGearModalAnalysis
    from ._4667 import StraightBevelDiffGearSetModalAnalysis
    from ._4668 import StraightBevelGearMeshModalAnalysis
    from ._4669 import StraightBevelGearModalAnalysis
    from ._4670 import StraightBevelGearSetModalAnalysis
    from ._4671 import StraightBevelPlanetGearModalAnalysis
    from ._4672 import StraightBevelSunGearModalAnalysis
    from ._4673 import SynchroniserHalfModalAnalysis
    from ._4674 import SynchroniserModalAnalysis
    from ._4675 import SynchroniserPartModalAnalysis
    from ._4676 import SynchroniserSleeveModalAnalysis
    from ._4677 import TorqueConverterConnectionModalAnalysis
    from ._4678 import TorqueConverterModalAnalysis
    from ._4679 import TorqueConverterPumpModalAnalysis
    from ._4680 import TorqueConverterTurbineModalAnalysis
    from ._4681 import UnbalancedMassModalAnalysis
    from ._4682 import VirtualComponentModalAnalysis
    from ._4683 import WaterfallChartSettings
    from ._4684 import WhineWaterfallExportOption
    from ._4685 import WhineWaterfallSettings
    from ._4686 import WormGearMeshModalAnalysis
    from ._4687 import WormGearModalAnalysis
    from ._4688 import WormGearSetModalAnalysis
    from ._4689 import ZerolBevelGearMeshModalAnalysis
    from ._4690 import ZerolBevelGearModalAnalysis
    from ._4691 import ZerolBevelGearSetModalAnalysis
else:
    import_structure = {
        '_4550': ['AbstractAssemblyModalAnalysis'],
        '_4551': ['AbstractShaftModalAnalysis'],
        '_4552': ['AbstractShaftOrHousingModalAnalysis'],
        '_4553': ['AbstractShaftToMountableComponentConnectionModalAnalysis'],
        '_4554': ['AGMAGleasonConicalGearMeshModalAnalysis'],
        '_4555': ['AGMAGleasonConicalGearModalAnalysis'],
        '_4556': ['AGMAGleasonConicalGearSetModalAnalysis'],
        '_4557': ['AssemblyModalAnalysis'],
        '_4558': ['BearingModalAnalysis'],
        '_4559': ['BeltConnectionModalAnalysis'],
        '_4560': ['BeltDriveModalAnalysis'],
        '_4561': ['BevelDifferentialGearMeshModalAnalysis'],
        '_4562': ['BevelDifferentialGearModalAnalysis'],
        '_4563': ['BevelDifferentialGearSetModalAnalysis'],
        '_4564': ['BevelDifferentialPlanetGearModalAnalysis'],
        '_4565': ['BevelDifferentialSunGearModalAnalysis'],
        '_4566': ['BevelGearMeshModalAnalysis'],
        '_4567': ['BevelGearModalAnalysis'],
        '_4568': ['BevelGearSetModalAnalysis'],
        '_4569': ['BoltedJointModalAnalysis'],
        '_4570': ['BoltModalAnalysis'],
        '_4571': ['ClutchConnectionModalAnalysis'],
        '_4572': ['ClutchHalfModalAnalysis'],
        '_4573': ['ClutchModalAnalysis'],
        '_4574': ['CoaxialConnectionModalAnalysis'],
        '_4575': ['ComponentModalAnalysis'],
        '_4576': ['ConceptCouplingConnectionModalAnalysis'],
        '_4577': ['ConceptCouplingHalfModalAnalysis'],
        '_4578': ['ConceptCouplingModalAnalysis'],
        '_4579': ['ConceptGearMeshModalAnalysis'],
        '_4580': ['ConceptGearModalAnalysis'],
        '_4581': ['ConceptGearSetModalAnalysis'],
        '_4582': ['ConicalGearMeshModalAnalysis'],
        '_4583': ['ConicalGearModalAnalysis'],
        '_4584': ['ConicalGearSetModalAnalysis'],
        '_4585': ['ConnectionModalAnalysis'],
        '_4586': ['ConnectorModalAnalysis'],
        '_4587': ['CoordinateSystemForWhine'],
        '_4588': ['CouplingConnectionModalAnalysis'],
        '_4589': ['CouplingHalfModalAnalysis'],
        '_4590': ['CouplingModalAnalysis'],
        '_4591': ['CVTBeltConnectionModalAnalysis'],
        '_4592': ['CVTModalAnalysis'],
        '_4593': ['CVTPulleyModalAnalysis'],
        '_4594': ['CycloidalAssemblyModalAnalysis'],
        '_4595': ['CycloidalDiscCentralBearingConnectionModalAnalysis'],
        '_4596': ['CycloidalDiscModalAnalysis'],
        '_4597': ['CycloidalDiscPlanetaryBearingConnectionModalAnalysis'],
        '_4598': ['CylindricalGearMeshModalAnalysis'],
        '_4599': ['CylindricalGearModalAnalysis'],
        '_4600': ['CylindricalGearSetModalAnalysis'],
        '_4601': ['CylindricalPlanetGearModalAnalysis'],
        '_4602': ['DatumModalAnalysis'],
        '_2611': ['DynamicModelForModalAnalysis'],
        '_4603': ['DynamicsResponse3DChartType'],
        '_4604': ['DynamicsResponseType'],
        '_4605': ['ExternalCADModelModalAnalysis'],
        '_4606': ['FaceGearMeshModalAnalysis'],
        '_4607': ['FaceGearModalAnalysis'],
        '_4608': ['FaceGearSetModalAnalysis'],
        '_4609': ['FEPartModalAnalysis'],
        '_4610': ['FlexiblePinAssemblyModalAnalysis'],
        '_4611': ['FrequencyResponseAnalysisOptions'],
        '_4612': ['GearMeshModalAnalysis'],
        '_4613': ['GearModalAnalysis'],
        '_4614': ['GearSetModalAnalysis'],
        '_4615': ['GuideDxfModelModalAnalysis'],
        '_4616': ['HypoidGearMeshModalAnalysis'],
        '_4617': ['HypoidGearModalAnalysis'],
        '_4618': ['HypoidGearSetModalAnalysis'],
        '_4619': ['InterMountableComponentConnectionModalAnalysis'],
        '_4620': ['KlingelnbergCycloPalloidConicalGearMeshModalAnalysis'],
        '_4621': ['KlingelnbergCycloPalloidConicalGearModalAnalysis'],
        '_4622': ['KlingelnbergCycloPalloidConicalGearSetModalAnalysis'],
        '_4623': ['KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis'],
        '_4624': ['KlingelnbergCycloPalloidHypoidGearModalAnalysis'],
        '_4625': ['KlingelnbergCycloPalloidHypoidGearSetModalAnalysis'],
        '_4626': ['KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis'],
        '_4627': ['KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis'],
        '_4628': ['KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis'],
        '_4629': ['MassDiscModalAnalysis'],
        '_4630': ['MeasurementComponentModalAnalysis'],
        '_2617': ['ModalAnalysis'],
        '_4631': ['ModalAnalysisBarModelFEExportOptions'],
        '_4632': ['ModalAnalysisDrawStyle'],
        '_4633': ['ModalAnalysisOptions'],
        '_4634': ['MountableComponentModalAnalysis'],
        '_4635': ['MultipleExcitationsSpeedRangeOption'],
        '_4636': ['OilSealModalAnalysis'],
        '_4637': ['OrderCutsChartSettings'],
        '_4638': ['PartModalAnalysis'],
        '_4639': ['PartToPartShearCouplingConnectionModalAnalysis'],
        '_4640': ['PartToPartShearCouplingHalfModalAnalysis'],
        '_4641': ['PartToPartShearCouplingModalAnalysis'],
        '_4642': ['PlanetaryConnectionModalAnalysis'],
        '_4643': ['PlanetaryGearSetModalAnalysis'],
        '_4644': ['PlanetCarrierModalAnalysis'],
        '_4645': ['PointLoadModalAnalysis'],
        '_4646': ['PowerLoadModalAnalysis'],
        '_4647': ['PulleyModalAnalysis'],
        '_4648': ['RingPinsModalAnalysis'],
        '_4649': ['RingPinsToDiscConnectionModalAnalysis'],
        '_4650': ['RollingRingAssemblyModalAnalysis'],
        '_4651': ['RollingRingConnectionModalAnalysis'],
        '_4652': ['RollingRingModalAnalysis'],
        '_4653': ['RootAssemblyModalAnalysis'],
        '_4654': ['ShaftHubConnectionModalAnalysis'],
        '_4655': ['ShaftModalAnalysis'],
        '_4656': ['ShaftModalAnalysisMode'],
        '_4657': ['ShaftToMountableComponentConnectionModalAnalysis'],
        '_4658': ['SpecialisedAssemblyModalAnalysis'],
        '_4659': ['SpiralBevelGearMeshModalAnalysis'],
        '_4660': ['SpiralBevelGearModalAnalysis'],
        '_4661': ['SpiralBevelGearSetModalAnalysis'],
        '_4662': ['SpringDamperConnectionModalAnalysis'],
        '_4663': ['SpringDamperHalfModalAnalysis'],
        '_4664': ['SpringDamperModalAnalysis'],
        '_4665': ['StraightBevelDiffGearMeshModalAnalysis'],
        '_4666': ['StraightBevelDiffGearModalAnalysis'],
        '_4667': ['StraightBevelDiffGearSetModalAnalysis'],
        '_4668': ['StraightBevelGearMeshModalAnalysis'],
        '_4669': ['StraightBevelGearModalAnalysis'],
        '_4670': ['StraightBevelGearSetModalAnalysis'],
        '_4671': ['StraightBevelPlanetGearModalAnalysis'],
        '_4672': ['StraightBevelSunGearModalAnalysis'],
        '_4673': ['SynchroniserHalfModalAnalysis'],
        '_4674': ['SynchroniserModalAnalysis'],
        '_4675': ['SynchroniserPartModalAnalysis'],
        '_4676': ['SynchroniserSleeveModalAnalysis'],
        '_4677': ['TorqueConverterConnectionModalAnalysis'],
        '_4678': ['TorqueConverterModalAnalysis'],
        '_4679': ['TorqueConverterPumpModalAnalysis'],
        '_4680': ['TorqueConverterTurbineModalAnalysis'],
        '_4681': ['UnbalancedMassModalAnalysis'],
        '_4682': ['VirtualComponentModalAnalysis'],
        '_4683': ['WaterfallChartSettings'],
        '_4684': ['WhineWaterfallExportOption'],
        '_4685': ['WhineWaterfallSettings'],
        '_4686': ['WormGearMeshModalAnalysis'],
        '_4687': ['WormGearModalAnalysis'],
        '_4688': ['WormGearSetModalAnalysis'],
        '_4689': ['ZerolBevelGearMeshModalAnalysis'],
        '_4690': ['ZerolBevelGearModalAnalysis'],
        '_4691': ['ZerolBevelGearSetModalAnalysis'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
