"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7236 import AbstractAssemblyAdvancedSystemDeflection
    from ._7237 import AbstractShaftAdvancedSystemDeflection
    from ._7238 import AbstractShaftOrHousingAdvancedSystemDeflection
    from ._7239 import AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection
    from ._7240 import AdvancedSystemDeflection
    from ._7241 import AdvancedSystemDeflectionOptions
    from ._7242 import AdvancedSystemDeflectionSubAnalysis
    from ._7243 import AGMAGleasonConicalGearAdvancedSystemDeflection
    from ._7244 import AGMAGleasonConicalGearMeshAdvancedSystemDeflection
    from ._7245 import AGMAGleasonConicalGearSetAdvancedSystemDeflection
    from ._7246 import AssemblyAdvancedSystemDeflection
    from ._7247 import BearingAdvancedSystemDeflection
    from ._7248 import BeltConnectionAdvancedSystemDeflection
    from ._7249 import BeltDriveAdvancedSystemDeflection
    from ._7250 import BevelDifferentialGearAdvancedSystemDeflection
    from ._7251 import BevelDifferentialGearMeshAdvancedSystemDeflection
    from ._7252 import BevelDifferentialGearSetAdvancedSystemDeflection
    from ._7253 import BevelDifferentialPlanetGearAdvancedSystemDeflection
    from ._7254 import BevelDifferentialSunGearAdvancedSystemDeflection
    from ._7255 import BevelGearAdvancedSystemDeflection
    from ._7256 import BevelGearMeshAdvancedSystemDeflection
    from ._7257 import BevelGearSetAdvancedSystemDeflection
    from ._7258 import BoltAdvancedSystemDeflection
    from ._7259 import BoltedJointAdvancedSystemDeflection
    from ._7260 import ClutchAdvancedSystemDeflection
    from ._7261 import ClutchConnectionAdvancedSystemDeflection
    from ._7262 import ClutchHalfAdvancedSystemDeflection
    from ._7263 import CoaxialConnectionAdvancedSystemDeflection
    from ._7264 import ComponentAdvancedSystemDeflection
    from ._7265 import ConceptCouplingAdvancedSystemDeflection
    from ._7266 import ConceptCouplingConnectionAdvancedSystemDeflection
    from ._7267 import ConceptCouplingHalfAdvancedSystemDeflection
    from ._7268 import ConceptGearAdvancedSystemDeflection
    from ._7269 import ConceptGearMeshAdvancedSystemDeflection
    from ._7270 import ConceptGearSetAdvancedSystemDeflection
    from ._7271 import ConicalGearAdvancedSystemDeflection
    from ._7272 import ConicalGearMeshAdvancedSystemDeflection
    from ._7273 import ConicalGearSetAdvancedSystemDeflection
    from ._7274 import ConnectionAdvancedSystemDeflection
    from ._7275 import ConnectorAdvancedSystemDeflection
    from ._7276 import ContactChartPerToothPass
    from ._7277 import CouplingAdvancedSystemDeflection
    from ._7278 import CouplingConnectionAdvancedSystemDeflection
    from ._7279 import CouplingHalfAdvancedSystemDeflection
    from ._7280 import CVTAdvancedSystemDeflection
    from ._7281 import CVTBeltConnectionAdvancedSystemDeflection
    from ._7282 import CVTPulleyAdvancedSystemDeflection
    from ._7283 import CycloidalAssemblyAdvancedSystemDeflection
    from ._7284 import CycloidalDiscAdvancedSystemDeflection
    from ._7285 import CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection
    from ._7286 import CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection
    from ._7287 import CylindricalGearAdvancedSystemDeflection
    from ._7288 import CylindricalGearMeshAdvancedSystemDeflection
    from ._7289 import CylindricalGearSetAdvancedSystemDeflection
    from ._7290 import CylindricalMeshedGearAdvancedSystemDeflection
    from ._7291 import CylindricalPlanetGearAdvancedSystemDeflection
    from ._7292 import DatumAdvancedSystemDeflection
    from ._7293 import ExternalCADModelAdvancedSystemDeflection
    from ._7294 import FaceGearAdvancedSystemDeflection
    from ._7295 import FaceGearMeshAdvancedSystemDeflection
    from ._7296 import FaceGearSetAdvancedSystemDeflection
    from ._7297 import FEPartAdvancedSystemDeflection
    from ._7298 import FlexiblePinAssemblyAdvancedSystemDeflection
    from ._7299 import GearAdvancedSystemDeflection
    from ._7300 import GearMeshAdvancedSystemDeflection
    from ._7301 import GearSetAdvancedSystemDeflection
    from ._7302 import GuideDxfModelAdvancedSystemDeflection
    from ._7303 import HypoidGearAdvancedSystemDeflection
    from ._7304 import HypoidGearMeshAdvancedSystemDeflection
    from ._7305 import HypoidGearSetAdvancedSystemDeflection
    from ._7306 import InterMountableComponentConnectionAdvancedSystemDeflection
    from ._7307 import KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
    from ._7308 import KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection
    from ._7309 import KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
    from ._7310 import KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
    from ._7311 import KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection
    from ._7312 import KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
    from ._7313 import KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
    from ._7314 import KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection
    from ._7315 import KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection
    from ._7316 import UseLtcaInAsdOption
    from ._7317 import MassDiscAdvancedSystemDeflection
    from ._7318 import MeasurementComponentAdvancedSystemDeflection
    from ._7319 import MountableComponentAdvancedSystemDeflection
    from ._7320 import OilSealAdvancedSystemDeflection
    from ._7321 import PartAdvancedSystemDeflection
    from ._7322 import PartToPartShearCouplingAdvancedSystemDeflection
    from ._7323 import PartToPartShearCouplingConnectionAdvancedSystemDeflection
    from ._7324 import PartToPartShearCouplingHalfAdvancedSystemDeflection
    from ._7325 import PlanetaryConnectionAdvancedSystemDeflection
    from ._7326 import PlanetaryGearSetAdvancedSystemDeflection
    from ._7327 import PlanetCarrierAdvancedSystemDeflection
    from ._7328 import PointLoadAdvancedSystemDeflection
    from ._7329 import PowerLoadAdvancedSystemDeflection
    from ._7330 import PulleyAdvancedSystemDeflection
    from ._7331 import RingPinsAdvancedSystemDeflection
    from ._7332 import RingPinsToDiscConnectionAdvancedSystemDeflection
    from ._7333 import RollingRingAdvancedSystemDeflection
    from ._7334 import RollingRingAssemblyAdvancedSystemDeflection
    from ._7335 import RollingRingConnectionAdvancedSystemDeflection
    from ._7336 import RootAssemblyAdvancedSystemDeflection
    from ._7337 import ShaftAdvancedSystemDeflection
    from ._7338 import ShaftHubConnectionAdvancedSystemDeflection
    from ._7339 import ShaftToMountableComponentConnectionAdvancedSystemDeflection
    from ._7340 import SpecialisedAssemblyAdvancedSystemDeflection
    from ._7341 import SpiralBevelGearAdvancedSystemDeflection
    from ._7342 import SpiralBevelGearMeshAdvancedSystemDeflection
    from ._7343 import SpiralBevelGearSetAdvancedSystemDeflection
    from ._7344 import SpringDamperAdvancedSystemDeflection
    from ._7345 import SpringDamperConnectionAdvancedSystemDeflection
    from ._7346 import SpringDamperHalfAdvancedSystemDeflection
    from ._7347 import StraightBevelDiffGearAdvancedSystemDeflection
    from ._7348 import StraightBevelDiffGearMeshAdvancedSystemDeflection
    from ._7349 import StraightBevelDiffGearSetAdvancedSystemDeflection
    from ._7350 import StraightBevelGearAdvancedSystemDeflection
    from ._7351 import StraightBevelGearMeshAdvancedSystemDeflection
    from ._7352 import StraightBevelGearSetAdvancedSystemDeflection
    from ._7353 import StraightBevelPlanetGearAdvancedSystemDeflection
    from ._7354 import StraightBevelSunGearAdvancedSystemDeflection
    from ._7355 import SynchroniserAdvancedSystemDeflection
    from ._7356 import SynchroniserHalfAdvancedSystemDeflection
    from ._7357 import SynchroniserPartAdvancedSystemDeflection
    from ._7358 import SynchroniserSleeveAdvancedSystemDeflection
    from ._7359 import TorqueConverterAdvancedSystemDeflection
    from ._7360 import TorqueConverterConnectionAdvancedSystemDeflection
    from ._7361 import TorqueConverterPumpAdvancedSystemDeflection
    from ._7362 import TorqueConverterTurbineAdvancedSystemDeflection
    from ._7363 import TransmissionErrorToOtherPowerLoad
    from ._7364 import UnbalancedMassAdvancedSystemDeflection
    from ._7365 import VirtualComponentAdvancedSystemDeflection
    from ._7366 import WormGearAdvancedSystemDeflection
    from ._7367 import WormGearMeshAdvancedSystemDeflection
    from ._7368 import WormGearSetAdvancedSystemDeflection
    from ._7369 import ZerolBevelGearAdvancedSystemDeflection
    from ._7370 import ZerolBevelGearMeshAdvancedSystemDeflection
    from ._7371 import ZerolBevelGearSetAdvancedSystemDeflection
else:
    import_structure = {
        '_7236': ['AbstractAssemblyAdvancedSystemDeflection'],
        '_7237': ['AbstractShaftAdvancedSystemDeflection'],
        '_7238': ['AbstractShaftOrHousingAdvancedSystemDeflection'],
        '_7239': ['AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection'],
        '_7240': ['AdvancedSystemDeflection'],
        '_7241': ['AdvancedSystemDeflectionOptions'],
        '_7242': ['AdvancedSystemDeflectionSubAnalysis'],
        '_7243': ['AGMAGleasonConicalGearAdvancedSystemDeflection'],
        '_7244': ['AGMAGleasonConicalGearMeshAdvancedSystemDeflection'],
        '_7245': ['AGMAGleasonConicalGearSetAdvancedSystemDeflection'],
        '_7246': ['AssemblyAdvancedSystemDeflection'],
        '_7247': ['BearingAdvancedSystemDeflection'],
        '_7248': ['BeltConnectionAdvancedSystemDeflection'],
        '_7249': ['BeltDriveAdvancedSystemDeflection'],
        '_7250': ['BevelDifferentialGearAdvancedSystemDeflection'],
        '_7251': ['BevelDifferentialGearMeshAdvancedSystemDeflection'],
        '_7252': ['BevelDifferentialGearSetAdvancedSystemDeflection'],
        '_7253': ['BevelDifferentialPlanetGearAdvancedSystemDeflection'],
        '_7254': ['BevelDifferentialSunGearAdvancedSystemDeflection'],
        '_7255': ['BevelGearAdvancedSystemDeflection'],
        '_7256': ['BevelGearMeshAdvancedSystemDeflection'],
        '_7257': ['BevelGearSetAdvancedSystemDeflection'],
        '_7258': ['BoltAdvancedSystemDeflection'],
        '_7259': ['BoltedJointAdvancedSystemDeflection'],
        '_7260': ['ClutchAdvancedSystemDeflection'],
        '_7261': ['ClutchConnectionAdvancedSystemDeflection'],
        '_7262': ['ClutchHalfAdvancedSystemDeflection'],
        '_7263': ['CoaxialConnectionAdvancedSystemDeflection'],
        '_7264': ['ComponentAdvancedSystemDeflection'],
        '_7265': ['ConceptCouplingAdvancedSystemDeflection'],
        '_7266': ['ConceptCouplingConnectionAdvancedSystemDeflection'],
        '_7267': ['ConceptCouplingHalfAdvancedSystemDeflection'],
        '_7268': ['ConceptGearAdvancedSystemDeflection'],
        '_7269': ['ConceptGearMeshAdvancedSystemDeflection'],
        '_7270': ['ConceptGearSetAdvancedSystemDeflection'],
        '_7271': ['ConicalGearAdvancedSystemDeflection'],
        '_7272': ['ConicalGearMeshAdvancedSystemDeflection'],
        '_7273': ['ConicalGearSetAdvancedSystemDeflection'],
        '_7274': ['ConnectionAdvancedSystemDeflection'],
        '_7275': ['ConnectorAdvancedSystemDeflection'],
        '_7276': ['ContactChartPerToothPass'],
        '_7277': ['CouplingAdvancedSystemDeflection'],
        '_7278': ['CouplingConnectionAdvancedSystemDeflection'],
        '_7279': ['CouplingHalfAdvancedSystemDeflection'],
        '_7280': ['CVTAdvancedSystemDeflection'],
        '_7281': ['CVTBeltConnectionAdvancedSystemDeflection'],
        '_7282': ['CVTPulleyAdvancedSystemDeflection'],
        '_7283': ['CycloidalAssemblyAdvancedSystemDeflection'],
        '_7284': ['CycloidalDiscAdvancedSystemDeflection'],
        '_7285': ['CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection'],
        '_7286': ['CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection'],
        '_7287': ['CylindricalGearAdvancedSystemDeflection'],
        '_7288': ['CylindricalGearMeshAdvancedSystemDeflection'],
        '_7289': ['CylindricalGearSetAdvancedSystemDeflection'],
        '_7290': ['CylindricalMeshedGearAdvancedSystemDeflection'],
        '_7291': ['CylindricalPlanetGearAdvancedSystemDeflection'],
        '_7292': ['DatumAdvancedSystemDeflection'],
        '_7293': ['ExternalCADModelAdvancedSystemDeflection'],
        '_7294': ['FaceGearAdvancedSystemDeflection'],
        '_7295': ['FaceGearMeshAdvancedSystemDeflection'],
        '_7296': ['FaceGearSetAdvancedSystemDeflection'],
        '_7297': ['FEPartAdvancedSystemDeflection'],
        '_7298': ['FlexiblePinAssemblyAdvancedSystemDeflection'],
        '_7299': ['GearAdvancedSystemDeflection'],
        '_7300': ['GearMeshAdvancedSystemDeflection'],
        '_7301': ['GearSetAdvancedSystemDeflection'],
        '_7302': ['GuideDxfModelAdvancedSystemDeflection'],
        '_7303': ['HypoidGearAdvancedSystemDeflection'],
        '_7304': ['HypoidGearMeshAdvancedSystemDeflection'],
        '_7305': ['HypoidGearSetAdvancedSystemDeflection'],
        '_7306': ['InterMountableComponentConnectionAdvancedSystemDeflection'],
        '_7307': ['KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection'],
        '_7308': ['KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection'],
        '_7309': ['KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection'],
        '_7310': ['KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection'],
        '_7311': ['KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection'],
        '_7312': ['KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection'],
        '_7313': ['KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection'],
        '_7314': ['KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection'],
        '_7315': ['KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection'],
        '_7316': ['UseLtcaInAsdOption'],
        '_7317': ['MassDiscAdvancedSystemDeflection'],
        '_7318': ['MeasurementComponentAdvancedSystemDeflection'],
        '_7319': ['MountableComponentAdvancedSystemDeflection'],
        '_7320': ['OilSealAdvancedSystemDeflection'],
        '_7321': ['PartAdvancedSystemDeflection'],
        '_7322': ['PartToPartShearCouplingAdvancedSystemDeflection'],
        '_7323': ['PartToPartShearCouplingConnectionAdvancedSystemDeflection'],
        '_7324': ['PartToPartShearCouplingHalfAdvancedSystemDeflection'],
        '_7325': ['PlanetaryConnectionAdvancedSystemDeflection'],
        '_7326': ['PlanetaryGearSetAdvancedSystemDeflection'],
        '_7327': ['PlanetCarrierAdvancedSystemDeflection'],
        '_7328': ['PointLoadAdvancedSystemDeflection'],
        '_7329': ['PowerLoadAdvancedSystemDeflection'],
        '_7330': ['PulleyAdvancedSystemDeflection'],
        '_7331': ['RingPinsAdvancedSystemDeflection'],
        '_7332': ['RingPinsToDiscConnectionAdvancedSystemDeflection'],
        '_7333': ['RollingRingAdvancedSystemDeflection'],
        '_7334': ['RollingRingAssemblyAdvancedSystemDeflection'],
        '_7335': ['RollingRingConnectionAdvancedSystemDeflection'],
        '_7336': ['RootAssemblyAdvancedSystemDeflection'],
        '_7337': ['ShaftAdvancedSystemDeflection'],
        '_7338': ['ShaftHubConnectionAdvancedSystemDeflection'],
        '_7339': ['ShaftToMountableComponentConnectionAdvancedSystemDeflection'],
        '_7340': ['SpecialisedAssemblyAdvancedSystemDeflection'],
        '_7341': ['SpiralBevelGearAdvancedSystemDeflection'],
        '_7342': ['SpiralBevelGearMeshAdvancedSystemDeflection'],
        '_7343': ['SpiralBevelGearSetAdvancedSystemDeflection'],
        '_7344': ['SpringDamperAdvancedSystemDeflection'],
        '_7345': ['SpringDamperConnectionAdvancedSystemDeflection'],
        '_7346': ['SpringDamperHalfAdvancedSystemDeflection'],
        '_7347': ['StraightBevelDiffGearAdvancedSystemDeflection'],
        '_7348': ['StraightBevelDiffGearMeshAdvancedSystemDeflection'],
        '_7349': ['StraightBevelDiffGearSetAdvancedSystemDeflection'],
        '_7350': ['StraightBevelGearAdvancedSystemDeflection'],
        '_7351': ['StraightBevelGearMeshAdvancedSystemDeflection'],
        '_7352': ['StraightBevelGearSetAdvancedSystemDeflection'],
        '_7353': ['StraightBevelPlanetGearAdvancedSystemDeflection'],
        '_7354': ['StraightBevelSunGearAdvancedSystemDeflection'],
        '_7355': ['SynchroniserAdvancedSystemDeflection'],
        '_7356': ['SynchroniserHalfAdvancedSystemDeflection'],
        '_7357': ['SynchroniserPartAdvancedSystemDeflection'],
        '_7358': ['SynchroniserSleeveAdvancedSystemDeflection'],
        '_7359': ['TorqueConverterAdvancedSystemDeflection'],
        '_7360': ['TorqueConverterConnectionAdvancedSystemDeflection'],
        '_7361': ['TorqueConverterPumpAdvancedSystemDeflection'],
        '_7362': ['TorqueConverterTurbineAdvancedSystemDeflection'],
        '_7363': ['TransmissionErrorToOtherPowerLoad'],
        '_7364': ['UnbalancedMassAdvancedSystemDeflection'],
        '_7365': ['VirtualComponentAdvancedSystemDeflection'],
        '_7366': ['WormGearAdvancedSystemDeflection'],
        '_7367': ['WormGearMeshAdvancedSystemDeflection'],
        '_7368': ['WormGearSetAdvancedSystemDeflection'],
        '_7369': ['ZerolBevelGearAdvancedSystemDeflection'],
        '_7370': ['ZerolBevelGearMeshAdvancedSystemDeflection'],
        '_7371': ['ZerolBevelGearSetAdvancedSystemDeflection'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
