"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7372 import AbstractAssemblyCompoundAdvancedSystemDeflection
    from ._7373 import AbstractShaftCompoundAdvancedSystemDeflection
    from ._7374 import AbstractShaftOrHousingCompoundAdvancedSystemDeflection
    from ._7375 import AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
    from ._7376 import AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
    from ._7377 import AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
    from ._7378 import AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
    from ._7379 import AssemblyCompoundAdvancedSystemDeflection
    from ._7380 import BearingCompoundAdvancedSystemDeflection
    from ._7381 import BeltConnectionCompoundAdvancedSystemDeflection
    from ._7382 import BeltDriveCompoundAdvancedSystemDeflection
    from ._7383 import BevelDifferentialGearCompoundAdvancedSystemDeflection
    from ._7384 import BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
    from ._7385 import BevelDifferentialGearSetCompoundAdvancedSystemDeflection
    from ._7386 import BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
    from ._7387 import BevelDifferentialSunGearCompoundAdvancedSystemDeflection
    from ._7388 import BevelGearCompoundAdvancedSystemDeflection
    from ._7389 import BevelGearMeshCompoundAdvancedSystemDeflection
    from ._7390 import BevelGearSetCompoundAdvancedSystemDeflection
    from ._7391 import BoltCompoundAdvancedSystemDeflection
    from ._7392 import BoltedJointCompoundAdvancedSystemDeflection
    from ._7393 import ClutchCompoundAdvancedSystemDeflection
    from ._7394 import ClutchConnectionCompoundAdvancedSystemDeflection
    from ._7395 import ClutchHalfCompoundAdvancedSystemDeflection
    from ._7396 import CoaxialConnectionCompoundAdvancedSystemDeflection
    from ._7397 import ComponentCompoundAdvancedSystemDeflection
    from ._7398 import ConceptCouplingCompoundAdvancedSystemDeflection
    from ._7399 import ConceptCouplingConnectionCompoundAdvancedSystemDeflection
    from ._7400 import ConceptCouplingHalfCompoundAdvancedSystemDeflection
    from ._7401 import ConceptGearCompoundAdvancedSystemDeflection
    from ._7402 import ConceptGearMeshCompoundAdvancedSystemDeflection
    from ._7403 import ConceptGearSetCompoundAdvancedSystemDeflection
    from ._7404 import ConicalGearCompoundAdvancedSystemDeflection
    from ._7405 import ConicalGearMeshCompoundAdvancedSystemDeflection
    from ._7406 import ConicalGearSetCompoundAdvancedSystemDeflection
    from ._7407 import ConnectionCompoundAdvancedSystemDeflection
    from ._7408 import ConnectorCompoundAdvancedSystemDeflection
    from ._7409 import CouplingCompoundAdvancedSystemDeflection
    from ._7410 import CouplingConnectionCompoundAdvancedSystemDeflection
    from ._7411 import CouplingHalfCompoundAdvancedSystemDeflection
    from ._7412 import CVTBeltConnectionCompoundAdvancedSystemDeflection
    from ._7413 import CVTCompoundAdvancedSystemDeflection
    from ._7414 import CVTPulleyCompoundAdvancedSystemDeflection
    from ._7415 import CycloidalAssemblyCompoundAdvancedSystemDeflection
    from ._7416 import CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection
    from ._7417 import CycloidalDiscCompoundAdvancedSystemDeflection
    from ._7418 import CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection
    from ._7419 import CylindricalGearCompoundAdvancedSystemDeflection
    from ._7420 import CylindricalGearMeshCompoundAdvancedSystemDeflection
    from ._7421 import CylindricalGearSetCompoundAdvancedSystemDeflection
    from ._7422 import CylindricalPlanetGearCompoundAdvancedSystemDeflection
    from ._7423 import DatumCompoundAdvancedSystemDeflection
    from ._7424 import ExternalCADModelCompoundAdvancedSystemDeflection
    from ._7425 import FaceGearCompoundAdvancedSystemDeflection
    from ._7426 import FaceGearMeshCompoundAdvancedSystemDeflection
    from ._7427 import FaceGearSetCompoundAdvancedSystemDeflection
    from ._7428 import FEPartCompoundAdvancedSystemDeflection
    from ._7429 import FlexiblePinAssemblyCompoundAdvancedSystemDeflection
    from ._7430 import GearCompoundAdvancedSystemDeflection
    from ._7431 import GearMeshCompoundAdvancedSystemDeflection
    from ._7432 import GearSetCompoundAdvancedSystemDeflection
    from ._7433 import GuideDxfModelCompoundAdvancedSystemDeflection
    from ._7434 import HypoidGearCompoundAdvancedSystemDeflection
    from ._7435 import HypoidGearMeshCompoundAdvancedSystemDeflection
    from ._7436 import HypoidGearSetCompoundAdvancedSystemDeflection
    from ._7437 import InterMountableComponentConnectionCompoundAdvancedSystemDeflection
    from ._7438 import KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection
    from ._7439 import KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection
    from ._7440 import KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection
    from ._7441 import KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection
    from ._7442 import KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection
    from ._7443 import KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection
    from ._7444 import KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection
    from ._7445 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7446 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection
    from ._7447 import MassDiscCompoundAdvancedSystemDeflection
    from ._7448 import MeasurementComponentCompoundAdvancedSystemDeflection
    from ._7449 import MountableComponentCompoundAdvancedSystemDeflection
    from ._7450 import OilSealCompoundAdvancedSystemDeflection
    from ._7451 import PartCompoundAdvancedSystemDeflection
    from ._7452 import PartToPartShearCouplingCompoundAdvancedSystemDeflection
    from ._7453 import PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection
    from ._7454 import PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
    from ._7455 import PlanetaryConnectionCompoundAdvancedSystemDeflection
    from ._7456 import PlanetaryGearSetCompoundAdvancedSystemDeflection
    from ._7457 import PlanetCarrierCompoundAdvancedSystemDeflection
    from ._7458 import PointLoadCompoundAdvancedSystemDeflection
    from ._7459 import PowerLoadCompoundAdvancedSystemDeflection
    from ._7460 import PulleyCompoundAdvancedSystemDeflection
    from ._7461 import RingPinsCompoundAdvancedSystemDeflection
    from ._7462 import RingPinsToDiscConnectionCompoundAdvancedSystemDeflection
    from ._7463 import RollingRingAssemblyCompoundAdvancedSystemDeflection
    from ._7464 import RollingRingCompoundAdvancedSystemDeflection
    from ._7465 import RollingRingConnectionCompoundAdvancedSystemDeflection
    from ._7466 import RootAssemblyCompoundAdvancedSystemDeflection
    from ._7467 import ShaftCompoundAdvancedSystemDeflection
    from ._7468 import ShaftHubConnectionCompoundAdvancedSystemDeflection
    from ._7469 import ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
    from ._7470 import SpecialisedAssemblyCompoundAdvancedSystemDeflection
    from ._7471 import SpiralBevelGearCompoundAdvancedSystemDeflection
    from ._7472 import SpiralBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7473 import SpiralBevelGearSetCompoundAdvancedSystemDeflection
    from ._7474 import SpringDamperCompoundAdvancedSystemDeflection
    from ._7475 import SpringDamperConnectionCompoundAdvancedSystemDeflection
    from ._7476 import SpringDamperHalfCompoundAdvancedSystemDeflection
    from ._7477 import StraightBevelDiffGearCompoundAdvancedSystemDeflection
    from ._7478 import StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection
    from ._7479 import StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
    from ._7480 import StraightBevelGearCompoundAdvancedSystemDeflection
    from ._7481 import StraightBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7482 import StraightBevelGearSetCompoundAdvancedSystemDeflection
    from ._7483 import StraightBevelPlanetGearCompoundAdvancedSystemDeflection
    from ._7484 import StraightBevelSunGearCompoundAdvancedSystemDeflection
    from ._7485 import SynchroniserCompoundAdvancedSystemDeflection
    from ._7486 import SynchroniserHalfCompoundAdvancedSystemDeflection
    from ._7487 import SynchroniserPartCompoundAdvancedSystemDeflection
    from ._7488 import SynchroniserSleeveCompoundAdvancedSystemDeflection
    from ._7489 import TorqueConverterCompoundAdvancedSystemDeflection
    from ._7490 import TorqueConverterConnectionCompoundAdvancedSystemDeflection
    from ._7491 import TorqueConverterPumpCompoundAdvancedSystemDeflection
    from ._7492 import TorqueConverterTurbineCompoundAdvancedSystemDeflection
    from ._7493 import UnbalancedMassCompoundAdvancedSystemDeflection
    from ._7494 import VirtualComponentCompoundAdvancedSystemDeflection
    from ._7495 import WormGearCompoundAdvancedSystemDeflection
    from ._7496 import WormGearMeshCompoundAdvancedSystemDeflection
    from ._7497 import WormGearSetCompoundAdvancedSystemDeflection
    from ._7498 import ZerolBevelGearCompoundAdvancedSystemDeflection
    from ._7499 import ZerolBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7500 import ZerolBevelGearSetCompoundAdvancedSystemDeflection
else:
    import_structure = {
        '_7372': ['AbstractAssemblyCompoundAdvancedSystemDeflection'],
        '_7373': ['AbstractShaftCompoundAdvancedSystemDeflection'],
        '_7374': ['AbstractShaftOrHousingCompoundAdvancedSystemDeflection'],
        '_7375': ['AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection'],
        '_7376': ['AGMAGleasonConicalGearCompoundAdvancedSystemDeflection'],
        '_7377': ['AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection'],
        '_7378': ['AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection'],
        '_7379': ['AssemblyCompoundAdvancedSystemDeflection'],
        '_7380': ['BearingCompoundAdvancedSystemDeflection'],
        '_7381': ['BeltConnectionCompoundAdvancedSystemDeflection'],
        '_7382': ['BeltDriveCompoundAdvancedSystemDeflection'],
        '_7383': ['BevelDifferentialGearCompoundAdvancedSystemDeflection'],
        '_7384': ['BevelDifferentialGearMeshCompoundAdvancedSystemDeflection'],
        '_7385': ['BevelDifferentialGearSetCompoundAdvancedSystemDeflection'],
        '_7386': ['BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection'],
        '_7387': ['BevelDifferentialSunGearCompoundAdvancedSystemDeflection'],
        '_7388': ['BevelGearCompoundAdvancedSystemDeflection'],
        '_7389': ['BevelGearMeshCompoundAdvancedSystemDeflection'],
        '_7390': ['BevelGearSetCompoundAdvancedSystemDeflection'],
        '_7391': ['BoltCompoundAdvancedSystemDeflection'],
        '_7392': ['BoltedJointCompoundAdvancedSystemDeflection'],
        '_7393': ['ClutchCompoundAdvancedSystemDeflection'],
        '_7394': ['ClutchConnectionCompoundAdvancedSystemDeflection'],
        '_7395': ['ClutchHalfCompoundAdvancedSystemDeflection'],
        '_7396': ['CoaxialConnectionCompoundAdvancedSystemDeflection'],
        '_7397': ['ComponentCompoundAdvancedSystemDeflection'],
        '_7398': ['ConceptCouplingCompoundAdvancedSystemDeflection'],
        '_7399': ['ConceptCouplingConnectionCompoundAdvancedSystemDeflection'],
        '_7400': ['ConceptCouplingHalfCompoundAdvancedSystemDeflection'],
        '_7401': ['ConceptGearCompoundAdvancedSystemDeflection'],
        '_7402': ['ConceptGearMeshCompoundAdvancedSystemDeflection'],
        '_7403': ['ConceptGearSetCompoundAdvancedSystemDeflection'],
        '_7404': ['ConicalGearCompoundAdvancedSystemDeflection'],
        '_7405': ['ConicalGearMeshCompoundAdvancedSystemDeflection'],
        '_7406': ['ConicalGearSetCompoundAdvancedSystemDeflection'],
        '_7407': ['ConnectionCompoundAdvancedSystemDeflection'],
        '_7408': ['ConnectorCompoundAdvancedSystemDeflection'],
        '_7409': ['CouplingCompoundAdvancedSystemDeflection'],
        '_7410': ['CouplingConnectionCompoundAdvancedSystemDeflection'],
        '_7411': ['CouplingHalfCompoundAdvancedSystemDeflection'],
        '_7412': ['CVTBeltConnectionCompoundAdvancedSystemDeflection'],
        '_7413': ['CVTCompoundAdvancedSystemDeflection'],
        '_7414': ['CVTPulleyCompoundAdvancedSystemDeflection'],
        '_7415': ['CycloidalAssemblyCompoundAdvancedSystemDeflection'],
        '_7416': ['CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection'],
        '_7417': ['CycloidalDiscCompoundAdvancedSystemDeflection'],
        '_7418': ['CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection'],
        '_7419': ['CylindricalGearCompoundAdvancedSystemDeflection'],
        '_7420': ['CylindricalGearMeshCompoundAdvancedSystemDeflection'],
        '_7421': ['CylindricalGearSetCompoundAdvancedSystemDeflection'],
        '_7422': ['CylindricalPlanetGearCompoundAdvancedSystemDeflection'],
        '_7423': ['DatumCompoundAdvancedSystemDeflection'],
        '_7424': ['ExternalCADModelCompoundAdvancedSystemDeflection'],
        '_7425': ['FaceGearCompoundAdvancedSystemDeflection'],
        '_7426': ['FaceGearMeshCompoundAdvancedSystemDeflection'],
        '_7427': ['FaceGearSetCompoundAdvancedSystemDeflection'],
        '_7428': ['FEPartCompoundAdvancedSystemDeflection'],
        '_7429': ['FlexiblePinAssemblyCompoundAdvancedSystemDeflection'],
        '_7430': ['GearCompoundAdvancedSystemDeflection'],
        '_7431': ['GearMeshCompoundAdvancedSystemDeflection'],
        '_7432': ['GearSetCompoundAdvancedSystemDeflection'],
        '_7433': ['GuideDxfModelCompoundAdvancedSystemDeflection'],
        '_7434': ['HypoidGearCompoundAdvancedSystemDeflection'],
        '_7435': ['HypoidGearMeshCompoundAdvancedSystemDeflection'],
        '_7436': ['HypoidGearSetCompoundAdvancedSystemDeflection'],
        '_7437': ['InterMountableComponentConnectionCompoundAdvancedSystemDeflection'],
        '_7438': ['KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection'],
        '_7439': ['KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection'],
        '_7440': ['KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection'],
        '_7441': ['KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection'],
        '_7442': ['KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection'],
        '_7443': ['KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection'],
        '_7444': ['KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection'],
        '_7445': ['KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection'],
        '_7446': ['KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection'],
        '_7447': ['MassDiscCompoundAdvancedSystemDeflection'],
        '_7448': ['MeasurementComponentCompoundAdvancedSystemDeflection'],
        '_7449': ['MountableComponentCompoundAdvancedSystemDeflection'],
        '_7450': ['OilSealCompoundAdvancedSystemDeflection'],
        '_7451': ['PartCompoundAdvancedSystemDeflection'],
        '_7452': ['PartToPartShearCouplingCompoundAdvancedSystemDeflection'],
        '_7453': ['PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection'],
        '_7454': ['PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection'],
        '_7455': ['PlanetaryConnectionCompoundAdvancedSystemDeflection'],
        '_7456': ['PlanetaryGearSetCompoundAdvancedSystemDeflection'],
        '_7457': ['PlanetCarrierCompoundAdvancedSystemDeflection'],
        '_7458': ['PointLoadCompoundAdvancedSystemDeflection'],
        '_7459': ['PowerLoadCompoundAdvancedSystemDeflection'],
        '_7460': ['PulleyCompoundAdvancedSystemDeflection'],
        '_7461': ['RingPinsCompoundAdvancedSystemDeflection'],
        '_7462': ['RingPinsToDiscConnectionCompoundAdvancedSystemDeflection'],
        '_7463': ['RollingRingAssemblyCompoundAdvancedSystemDeflection'],
        '_7464': ['RollingRingCompoundAdvancedSystemDeflection'],
        '_7465': ['RollingRingConnectionCompoundAdvancedSystemDeflection'],
        '_7466': ['RootAssemblyCompoundAdvancedSystemDeflection'],
        '_7467': ['ShaftCompoundAdvancedSystemDeflection'],
        '_7468': ['ShaftHubConnectionCompoundAdvancedSystemDeflection'],
        '_7469': ['ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection'],
        '_7470': ['SpecialisedAssemblyCompoundAdvancedSystemDeflection'],
        '_7471': ['SpiralBevelGearCompoundAdvancedSystemDeflection'],
        '_7472': ['SpiralBevelGearMeshCompoundAdvancedSystemDeflection'],
        '_7473': ['SpiralBevelGearSetCompoundAdvancedSystemDeflection'],
        '_7474': ['SpringDamperCompoundAdvancedSystemDeflection'],
        '_7475': ['SpringDamperConnectionCompoundAdvancedSystemDeflection'],
        '_7476': ['SpringDamperHalfCompoundAdvancedSystemDeflection'],
        '_7477': ['StraightBevelDiffGearCompoundAdvancedSystemDeflection'],
        '_7478': ['StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection'],
        '_7479': ['StraightBevelDiffGearSetCompoundAdvancedSystemDeflection'],
        '_7480': ['StraightBevelGearCompoundAdvancedSystemDeflection'],
        '_7481': ['StraightBevelGearMeshCompoundAdvancedSystemDeflection'],
        '_7482': ['StraightBevelGearSetCompoundAdvancedSystemDeflection'],
        '_7483': ['StraightBevelPlanetGearCompoundAdvancedSystemDeflection'],
        '_7484': ['StraightBevelSunGearCompoundAdvancedSystemDeflection'],
        '_7485': ['SynchroniserCompoundAdvancedSystemDeflection'],
        '_7486': ['SynchroniserHalfCompoundAdvancedSystemDeflection'],
        '_7487': ['SynchroniserPartCompoundAdvancedSystemDeflection'],
        '_7488': ['SynchroniserSleeveCompoundAdvancedSystemDeflection'],
        '_7489': ['TorqueConverterCompoundAdvancedSystemDeflection'],
        '_7490': ['TorqueConverterConnectionCompoundAdvancedSystemDeflection'],
        '_7491': ['TorqueConverterPumpCompoundAdvancedSystemDeflection'],
        '_7492': ['TorqueConverterTurbineCompoundAdvancedSystemDeflection'],
        '_7493': ['UnbalancedMassCompoundAdvancedSystemDeflection'],
        '_7494': ['VirtualComponentCompoundAdvancedSystemDeflection'],
        '_7495': ['WormGearCompoundAdvancedSystemDeflection'],
        '_7496': ['WormGearMeshCompoundAdvancedSystemDeflection'],
        '_7497': ['WormGearSetCompoundAdvancedSystemDeflection'],
        '_7498': ['ZerolBevelGearCompoundAdvancedSystemDeflection'],
        '_7499': ['ZerolBevelGearMeshCompoundAdvancedSystemDeflection'],
        '_7500': ['ZerolBevelGearSetCompoundAdvancedSystemDeflection'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
