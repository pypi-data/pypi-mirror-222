"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4421 import AbstractAssemblyCompoundParametricStudyTool
    from ._4422 import AbstractShaftCompoundParametricStudyTool
    from ._4423 import AbstractShaftOrHousingCompoundParametricStudyTool
    from ._4424 import AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool
    from ._4425 import AGMAGleasonConicalGearCompoundParametricStudyTool
    from ._4426 import AGMAGleasonConicalGearMeshCompoundParametricStudyTool
    from ._4427 import AGMAGleasonConicalGearSetCompoundParametricStudyTool
    from ._4428 import AssemblyCompoundParametricStudyTool
    from ._4429 import BearingCompoundParametricStudyTool
    from ._4430 import BeltConnectionCompoundParametricStudyTool
    from ._4431 import BeltDriveCompoundParametricStudyTool
    from ._4432 import BevelDifferentialGearCompoundParametricStudyTool
    from ._4433 import BevelDifferentialGearMeshCompoundParametricStudyTool
    from ._4434 import BevelDifferentialGearSetCompoundParametricStudyTool
    from ._4435 import BevelDifferentialPlanetGearCompoundParametricStudyTool
    from ._4436 import BevelDifferentialSunGearCompoundParametricStudyTool
    from ._4437 import BevelGearCompoundParametricStudyTool
    from ._4438 import BevelGearMeshCompoundParametricStudyTool
    from ._4439 import BevelGearSetCompoundParametricStudyTool
    from ._4440 import BoltCompoundParametricStudyTool
    from ._4441 import BoltedJointCompoundParametricStudyTool
    from ._4442 import ClutchCompoundParametricStudyTool
    from ._4443 import ClutchConnectionCompoundParametricStudyTool
    from ._4444 import ClutchHalfCompoundParametricStudyTool
    from ._4445 import CoaxialConnectionCompoundParametricStudyTool
    from ._4446 import ComponentCompoundParametricStudyTool
    from ._4447 import ConceptCouplingCompoundParametricStudyTool
    from ._4448 import ConceptCouplingConnectionCompoundParametricStudyTool
    from ._4449 import ConceptCouplingHalfCompoundParametricStudyTool
    from ._4450 import ConceptGearCompoundParametricStudyTool
    from ._4451 import ConceptGearMeshCompoundParametricStudyTool
    from ._4452 import ConceptGearSetCompoundParametricStudyTool
    from ._4453 import ConicalGearCompoundParametricStudyTool
    from ._4454 import ConicalGearMeshCompoundParametricStudyTool
    from ._4455 import ConicalGearSetCompoundParametricStudyTool
    from ._4456 import ConnectionCompoundParametricStudyTool
    from ._4457 import ConnectorCompoundParametricStudyTool
    from ._4458 import CouplingCompoundParametricStudyTool
    from ._4459 import CouplingConnectionCompoundParametricStudyTool
    from ._4460 import CouplingHalfCompoundParametricStudyTool
    from ._4461 import CVTBeltConnectionCompoundParametricStudyTool
    from ._4462 import CVTCompoundParametricStudyTool
    from ._4463 import CVTPulleyCompoundParametricStudyTool
    from ._4464 import CycloidalAssemblyCompoundParametricStudyTool
    from ._4465 import CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool
    from ._4466 import CycloidalDiscCompoundParametricStudyTool
    from ._4467 import CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool
    from ._4468 import CylindricalGearCompoundParametricStudyTool
    from ._4469 import CylindricalGearMeshCompoundParametricStudyTool
    from ._4470 import CylindricalGearSetCompoundParametricStudyTool
    from ._4471 import CylindricalPlanetGearCompoundParametricStudyTool
    from ._4472 import DatumCompoundParametricStudyTool
    from ._4473 import ExternalCADModelCompoundParametricStudyTool
    from ._4474 import FaceGearCompoundParametricStudyTool
    from ._4475 import FaceGearMeshCompoundParametricStudyTool
    from ._4476 import FaceGearSetCompoundParametricStudyTool
    from ._4477 import FEPartCompoundParametricStudyTool
    from ._4478 import FlexiblePinAssemblyCompoundParametricStudyTool
    from ._4479 import GearCompoundParametricStudyTool
    from ._4480 import GearMeshCompoundParametricStudyTool
    from ._4481 import GearSetCompoundParametricStudyTool
    from ._4482 import GuideDxfModelCompoundParametricStudyTool
    from ._4483 import HypoidGearCompoundParametricStudyTool
    from ._4484 import HypoidGearMeshCompoundParametricStudyTool
    from ._4485 import HypoidGearSetCompoundParametricStudyTool
    from ._4486 import InterMountableComponentConnectionCompoundParametricStudyTool
    from ._4487 import KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
    from ._4488 import KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool
    from ._4489 import KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
    from ._4490 import KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
    from ._4491 import KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool
    from ._4492 import KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
    from ._4493 import KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool
    from ._4494 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool
    from ._4495 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool
    from ._4496 import MassDiscCompoundParametricStudyTool
    from ._4497 import MeasurementComponentCompoundParametricStudyTool
    from ._4498 import MountableComponentCompoundParametricStudyTool
    from ._4499 import OilSealCompoundParametricStudyTool
    from ._4500 import PartCompoundParametricStudyTool
    from ._4501 import PartToPartShearCouplingCompoundParametricStudyTool
    from ._4502 import PartToPartShearCouplingConnectionCompoundParametricStudyTool
    from ._4503 import PartToPartShearCouplingHalfCompoundParametricStudyTool
    from ._4504 import PlanetaryConnectionCompoundParametricStudyTool
    from ._4505 import PlanetaryGearSetCompoundParametricStudyTool
    from ._4506 import PlanetCarrierCompoundParametricStudyTool
    from ._4507 import PointLoadCompoundParametricStudyTool
    from ._4508 import PowerLoadCompoundParametricStudyTool
    from ._4509 import PulleyCompoundParametricStudyTool
    from ._4510 import RingPinsCompoundParametricStudyTool
    from ._4511 import RingPinsToDiscConnectionCompoundParametricStudyTool
    from ._4512 import RollingRingAssemblyCompoundParametricStudyTool
    from ._4513 import RollingRingCompoundParametricStudyTool
    from ._4514 import RollingRingConnectionCompoundParametricStudyTool
    from ._4515 import RootAssemblyCompoundParametricStudyTool
    from ._4516 import ShaftCompoundParametricStudyTool
    from ._4517 import ShaftHubConnectionCompoundParametricStudyTool
    from ._4518 import ShaftToMountableComponentConnectionCompoundParametricStudyTool
    from ._4519 import SpecialisedAssemblyCompoundParametricStudyTool
    from ._4520 import SpiralBevelGearCompoundParametricStudyTool
    from ._4521 import SpiralBevelGearMeshCompoundParametricStudyTool
    from ._4522 import SpiralBevelGearSetCompoundParametricStudyTool
    from ._4523 import SpringDamperCompoundParametricStudyTool
    from ._4524 import SpringDamperConnectionCompoundParametricStudyTool
    from ._4525 import SpringDamperHalfCompoundParametricStudyTool
    from ._4526 import StraightBevelDiffGearCompoundParametricStudyTool
    from ._4527 import StraightBevelDiffGearMeshCompoundParametricStudyTool
    from ._4528 import StraightBevelDiffGearSetCompoundParametricStudyTool
    from ._4529 import StraightBevelGearCompoundParametricStudyTool
    from ._4530 import StraightBevelGearMeshCompoundParametricStudyTool
    from ._4531 import StraightBevelGearSetCompoundParametricStudyTool
    from ._4532 import StraightBevelPlanetGearCompoundParametricStudyTool
    from ._4533 import StraightBevelSunGearCompoundParametricStudyTool
    from ._4534 import SynchroniserCompoundParametricStudyTool
    from ._4535 import SynchroniserHalfCompoundParametricStudyTool
    from ._4536 import SynchroniserPartCompoundParametricStudyTool
    from ._4537 import SynchroniserSleeveCompoundParametricStudyTool
    from ._4538 import TorqueConverterCompoundParametricStudyTool
    from ._4539 import TorqueConverterConnectionCompoundParametricStudyTool
    from ._4540 import TorqueConverterPumpCompoundParametricStudyTool
    from ._4541 import TorqueConverterTurbineCompoundParametricStudyTool
    from ._4542 import UnbalancedMassCompoundParametricStudyTool
    from ._4543 import VirtualComponentCompoundParametricStudyTool
    from ._4544 import WormGearCompoundParametricStudyTool
    from ._4545 import WormGearMeshCompoundParametricStudyTool
    from ._4546 import WormGearSetCompoundParametricStudyTool
    from ._4547 import ZerolBevelGearCompoundParametricStudyTool
    from ._4548 import ZerolBevelGearMeshCompoundParametricStudyTool
    from ._4549 import ZerolBevelGearSetCompoundParametricStudyTool
else:
    import_structure = {
        '_4421': ['AbstractAssemblyCompoundParametricStudyTool'],
        '_4422': ['AbstractShaftCompoundParametricStudyTool'],
        '_4423': ['AbstractShaftOrHousingCompoundParametricStudyTool'],
        '_4424': ['AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool'],
        '_4425': ['AGMAGleasonConicalGearCompoundParametricStudyTool'],
        '_4426': ['AGMAGleasonConicalGearMeshCompoundParametricStudyTool'],
        '_4427': ['AGMAGleasonConicalGearSetCompoundParametricStudyTool'],
        '_4428': ['AssemblyCompoundParametricStudyTool'],
        '_4429': ['BearingCompoundParametricStudyTool'],
        '_4430': ['BeltConnectionCompoundParametricStudyTool'],
        '_4431': ['BeltDriveCompoundParametricStudyTool'],
        '_4432': ['BevelDifferentialGearCompoundParametricStudyTool'],
        '_4433': ['BevelDifferentialGearMeshCompoundParametricStudyTool'],
        '_4434': ['BevelDifferentialGearSetCompoundParametricStudyTool'],
        '_4435': ['BevelDifferentialPlanetGearCompoundParametricStudyTool'],
        '_4436': ['BevelDifferentialSunGearCompoundParametricStudyTool'],
        '_4437': ['BevelGearCompoundParametricStudyTool'],
        '_4438': ['BevelGearMeshCompoundParametricStudyTool'],
        '_4439': ['BevelGearSetCompoundParametricStudyTool'],
        '_4440': ['BoltCompoundParametricStudyTool'],
        '_4441': ['BoltedJointCompoundParametricStudyTool'],
        '_4442': ['ClutchCompoundParametricStudyTool'],
        '_4443': ['ClutchConnectionCompoundParametricStudyTool'],
        '_4444': ['ClutchHalfCompoundParametricStudyTool'],
        '_4445': ['CoaxialConnectionCompoundParametricStudyTool'],
        '_4446': ['ComponentCompoundParametricStudyTool'],
        '_4447': ['ConceptCouplingCompoundParametricStudyTool'],
        '_4448': ['ConceptCouplingConnectionCompoundParametricStudyTool'],
        '_4449': ['ConceptCouplingHalfCompoundParametricStudyTool'],
        '_4450': ['ConceptGearCompoundParametricStudyTool'],
        '_4451': ['ConceptGearMeshCompoundParametricStudyTool'],
        '_4452': ['ConceptGearSetCompoundParametricStudyTool'],
        '_4453': ['ConicalGearCompoundParametricStudyTool'],
        '_4454': ['ConicalGearMeshCompoundParametricStudyTool'],
        '_4455': ['ConicalGearSetCompoundParametricStudyTool'],
        '_4456': ['ConnectionCompoundParametricStudyTool'],
        '_4457': ['ConnectorCompoundParametricStudyTool'],
        '_4458': ['CouplingCompoundParametricStudyTool'],
        '_4459': ['CouplingConnectionCompoundParametricStudyTool'],
        '_4460': ['CouplingHalfCompoundParametricStudyTool'],
        '_4461': ['CVTBeltConnectionCompoundParametricStudyTool'],
        '_4462': ['CVTCompoundParametricStudyTool'],
        '_4463': ['CVTPulleyCompoundParametricStudyTool'],
        '_4464': ['CycloidalAssemblyCompoundParametricStudyTool'],
        '_4465': ['CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool'],
        '_4466': ['CycloidalDiscCompoundParametricStudyTool'],
        '_4467': ['CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool'],
        '_4468': ['CylindricalGearCompoundParametricStudyTool'],
        '_4469': ['CylindricalGearMeshCompoundParametricStudyTool'],
        '_4470': ['CylindricalGearSetCompoundParametricStudyTool'],
        '_4471': ['CylindricalPlanetGearCompoundParametricStudyTool'],
        '_4472': ['DatumCompoundParametricStudyTool'],
        '_4473': ['ExternalCADModelCompoundParametricStudyTool'],
        '_4474': ['FaceGearCompoundParametricStudyTool'],
        '_4475': ['FaceGearMeshCompoundParametricStudyTool'],
        '_4476': ['FaceGearSetCompoundParametricStudyTool'],
        '_4477': ['FEPartCompoundParametricStudyTool'],
        '_4478': ['FlexiblePinAssemblyCompoundParametricStudyTool'],
        '_4479': ['GearCompoundParametricStudyTool'],
        '_4480': ['GearMeshCompoundParametricStudyTool'],
        '_4481': ['GearSetCompoundParametricStudyTool'],
        '_4482': ['GuideDxfModelCompoundParametricStudyTool'],
        '_4483': ['HypoidGearCompoundParametricStudyTool'],
        '_4484': ['HypoidGearMeshCompoundParametricStudyTool'],
        '_4485': ['HypoidGearSetCompoundParametricStudyTool'],
        '_4486': ['InterMountableComponentConnectionCompoundParametricStudyTool'],
        '_4487': ['KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool'],
        '_4488': ['KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool'],
        '_4489': ['KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool'],
        '_4490': ['KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool'],
        '_4491': ['KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool'],
        '_4492': ['KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool'],
        '_4493': ['KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool'],
        '_4494': ['KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool'],
        '_4495': ['KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool'],
        '_4496': ['MassDiscCompoundParametricStudyTool'],
        '_4497': ['MeasurementComponentCompoundParametricStudyTool'],
        '_4498': ['MountableComponentCompoundParametricStudyTool'],
        '_4499': ['OilSealCompoundParametricStudyTool'],
        '_4500': ['PartCompoundParametricStudyTool'],
        '_4501': ['PartToPartShearCouplingCompoundParametricStudyTool'],
        '_4502': ['PartToPartShearCouplingConnectionCompoundParametricStudyTool'],
        '_4503': ['PartToPartShearCouplingHalfCompoundParametricStudyTool'],
        '_4504': ['PlanetaryConnectionCompoundParametricStudyTool'],
        '_4505': ['PlanetaryGearSetCompoundParametricStudyTool'],
        '_4506': ['PlanetCarrierCompoundParametricStudyTool'],
        '_4507': ['PointLoadCompoundParametricStudyTool'],
        '_4508': ['PowerLoadCompoundParametricStudyTool'],
        '_4509': ['PulleyCompoundParametricStudyTool'],
        '_4510': ['RingPinsCompoundParametricStudyTool'],
        '_4511': ['RingPinsToDiscConnectionCompoundParametricStudyTool'],
        '_4512': ['RollingRingAssemblyCompoundParametricStudyTool'],
        '_4513': ['RollingRingCompoundParametricStudyTool'],
        '_4514': ['RollingRingConnectionCompoundParametricStudyTool'],
        '_4515': ['RootAssemblyCompoundParametricStudyTool'],
        '_4516': ['ShaftCompoundParametricStudyTool'],
        '_4517': ['ShaftHubConnectionCompoundParametricStudyTool'],
        '_4518': ['ShaftToMountableComponentConnectionCompoundParametricStudyTool'],
        '_4519': ['SpecialisedAssemblyCompoundParametricStudyTool'],
        '_4520': ['SpiralBevelGearCompoundParametricStudyTool'],
        '_4521': ['SpiralBevelGearMeshCompoundParametricStudyTool'],
        '_4522': ['SpiralBevelGearSetCompoundParametricStudyTool'],
        '_4523': ['SpringDamperCompoundParametricStudyTool'],
        '_4524': ['SpringDamperConnectionCompoundParametricStudyTool'],
        '_4525': ['SpringDamperHalfCompoundParametricStudyTool'],
        '_4526': ['StraightBevelDiffGearCompoundParametricStudyTool'],
        '_4527': ['StraightBevelDiffGearMeshCompoundParametricStudyTool'],
        '_4528': ['StraightBevelDiffGearSetCompoundParametricStudyTool'],
        '_4529': ['StraightBevelGearCompoundParametricStudyTool'],
        '_4530': ['StraightBevelGearMeshCompoundParametricStudyTool'],
        '_4531': ['StraightBevelGearSetCompoundParametricStudyTool'],
        '_4532': ['StraightBevelPlanetGearCompoundParametricStudyTool'],
        '_4533': ['StraightBevelSunGearCompoundParametricStudyTool'],
        '_4534': ['SynchroniserCompoundParametricStudyTool'],
        '_4535': ['SynchroniserHalfCompoundParametricStudyTool'],
        '_4536': ['SynchroniserPartCompoundParametricStudyTool'],
        '_4537': ['SynchroniserSleeveCompoundParametricStudyTool'],
        '_4538': ['TorqueConverterCompoundParametricStudyTool'],
        '_4539': ['TorqueConverterConnectionCompoundParametricStudyTool'],
        '_4540': ['TorqueConverterPumpCompoundParametricStudyTool'],
        '_4541': ['TorqueConverterTurbineCompoundParametricStudyTool'],
        '_4542': ['UnbalancedMassCompoundParametricStudyTool'],
        '_4543': ['VirtualComponentCompoundParametricStudyTool'],
        '_4544': ['WormGearCompoundParametricStudyTool'],
        '_4545': ['WormGearMeshCompoundParametricStudyTool'],
        '_4546': ['WormGearSetCompoundParametricStudyTool'],
        '_4547': ['ZerolBevelGearCompoundParametricStudyTool'],
        '_4548': ['ZerolBevelGearMeshCompoundParametricStudyTool'],
        '_4549': ['ZerolBevelGearSetCompoundParametricStudyTool'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
