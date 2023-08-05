"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4274 import AbstractAssemblyParametricStudyTool
    from ._4275 import AbstractShaftOrHousingParametricStudyTool
    from ._4276 import AbstractShaftParametricStudyTool
    from ._4277 import AbstractShaftToMountableComponentConnectionParametricStudyTool
    from ._4278 import AGMAGleasonConicalGearMeshParametricStudyTool
    from ._4279 import AGMAGleasonConicalGearParametricStudyTool
    from ._4280 import AGMAGleasonConicalGearSetParametricStudyTool
    from ._4281 import AssemblyParametricStudyTool
    from ._4282 import BearingParametricStudyTool
    from ._4283 import BeltConnectionParametricStudyTool
    from ._4284 import BeltDriveParametricStudyTool
    from ._4285 import BevelDifferentialGearMeshParametricStudyTool
    from ._4286 import BevelDifferentialGearParametricStudyTool
    from ._4287 import BevelDifferentialGearSetParametricStudyTool
    from ._4288 import BevelDifferentialPlanetGearParametricStudyTool
    from ._4289 import BevelDifferentialSunGearParametricStudyTool
    from ._4290 import BevelGearMeshParametricStudyTool
    from ._4291 import BevelGearParametricStudyTool
    from ._4292 import BevelGearSetParametricStudyTool
    from ._4293 import BoltedJointParametricStudyTool
    from ._4294 import BoltParametricStudyTool
    from ._4295 import ClutchConnectionParametricStudyTool
    from ._4296 import ClutchHalfParametricStudyTool
    from ._4297 import ClutchParametricStudyTool
    from ._4298 import CoaxialConnectionParametricStudyTool
    from ._4299 import ComponentParametricStudyTool
    from ._4300 import ConceptCouplingConnectionParametricStudyTool
    from ._4301 import ConceptCouplingHalfParametricStudyTool
    from ._4302 import ConceptCouplingParametricStudyTool
    from ._4303 import ConceptGearMeshParametricStudyTool
    from ._4304 import ConceptGearParametricStudyTool
    from ._4305 import ConceptGearSetParametricStudyTool
    from ._4306 import ConicalGearMeshParametricStudyTool
    from ._4307 import ConicalGearParametricStudyTool
    from ._4308 import ConicalGearSetParametricStudyTool
    from ._4309 import ConnectionParametricStudyTool
    from ._4310 import ConnectorParametricStudyTool
    from ._4311 import CouplingConnectionParametricStudyTool
    from ._4312 import CouplingHalfParametricStudyTool
    from ._4313 import CouplingParametricStudyTool
    from ._4314 import CVTBeltConnectionParametricStudyTool
    from ._4315 import CVTParametricStudyTool
    from ._4316 import CVTPulleyParametricStudyTool
    from ._4317 import CycloidalAssemblyParametricStudyTool
    from ._4318 import CycloidalDiscCentralBearingConnectionParametricStudyTool
    from ._4319 import CycloidalDiscParametricStudyTool
    from ._4320 import CycloidalDiscPlanetaryBearingConnectionParametricStudyTool
    from ._4321 import CylindricalGearMeshParametricStudyTool
    from ._4322 import CylindricalGearParametricStudyTool
    from ._4323 import CylindricalGearSetParametricStudyTool
    from ._4324 import CylindricalPlanetGearParametricStudyTool
    from ._4325 import DatumParametricStudyTool
    from ._4326 import DesignOfExperimentsVariableSetter
    from ._4327 import DoeValueSpecificationOption
    from ._4328 import DutyCycleResultsForAllComponents
    from ._4329 import DutyCycleResultsForAllGearSets
    from ._4330 import DutyCycleResultsForRootAssembly
    from ._4331 import DutyCycleResultsForSingleBearing
    from ._4332 import DutyCycleResultsForSingleShaft
    from ._4333 import ExternalCADModelParametricStudyTool
    from ._4334 import FaceGearMeshParametricStudyTool
    from ._4335 import FaceGearParametricStudyTool
    from ._4336 import FaceGearSetParametricStudyTool
    from ._4337 import FEPartParametricStudyTool
    from ._4338 import FlexiblePinAssemblyParametricStudyTool
    from ._4339 import GearMeshParametricStudyTool
    from ._4340 import GearParametricStudyTool
    from ._4341 import GearSetParametricStudyTool
    from ._4342 import GuideDxfModelParametricStudyTool
    from ._4343 import HypoidGearMeshParametricStudyTool
    from ._4344 import HypoidGearParametricStudyTool
    from ._4345 import HypoidGearSetParametricStudyTool
    from ._4346 import InterMountableComponentConnectionParametricStudyTool
    from ._4347 import KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool
    from ._4348 import KlingelnbergCycloPalloidConicalGearParametricStudyTool
    from ._4349 import KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
    from ._4350 import KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool
    from ._4351 import KlingelnbergCycloPalloidHypoidGearParametricStudyTool
    from ._4352 import KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
    from ._4353 import KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool
    from ._4354 import KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
    from ._4355 import KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
    from ._4356 import MassDiscParametricStudyTool
    from ._4357 import MeasurementComponentParametricStudyTool
    from ._4358 import MonteCarloDistribution
    from ._4359 import MountableComponentParametricStudyTool
    from ._4360 import OilSealParametricStudyTool
    from ._4361 import ParametricStudyDimension
    from ._4362 import ParametricStudyDOEResultVariable
    from ._4363 import ParametricStudyDOEResultVariableForParallelCoordinatesPlot
    from ._4364 import ParametricStudyHistogram
    from ._4365 import ParametricStudyStaticLoad
    from ._4366 import ParametricStudyTool
    from ._4367 import ParametricStudyToolOptions
    from ._4368 import ParametricStudyToolResultsForReporting
    from ._4369 import ParametricStudyToolStepResult
    from ._4370 import ParametricStudyVariable
    from ._4371 import PartParametricStudyTool
    from ._4372 import PartToPartShearCouplingConnectionParametricStudyTool
    from ._4373 import PartToPartShearCouplingHalfParametricStudyTool
    from ._4374 import PartToPartShearCouplingParametricStudyTool
    from ._4375 import PlanetaryConnectionParametricStudyTool
    from ._4376 import PlanetaryGearSetParametricStudyTool
    from ._4377 import PlanetCarrierParametricStudyTool
    from ._4378 import PointLoadParametricStudyTool
    from ._4379 import PowerLoadParametricStudyTool
    from ._4380 import PulleyParametricStudyTool
    from ._4381 import RingPinsParametricStudyTool
    from ._4382 import RingPinsToDiscConnectionParametricStudyTool
    from ._4383 import RollingRingAssemblyParametricStudyTool
    from ._4384 import RollingRingConnectionParametricStudyTool
    from ._4385 import RollingRingParametricStudyTool
    from ._4386 import RootAssemblyParametricStudyTool
    from ._4387 import ShaftHubConnectionParametricStudyTool
    from ._4388 import ShaftParametricStudyTool
    from ._4389 import ShaftToMountableComponentConnectionParametricStudyTool
    from ._4390 import SpecialisedAssemblyParametricStudyTool
    from ._4391 import SpiralBevelGearMeshParametricStudyTool
    from ._4392 import SpiralBevelGearParametricStudyTool
    from ._4393 import SpiralBevelGearSetParametricStudyTool
    from ._4394 import SpringDamperConnectionParametricStudyTool
    from ._4395 import SpringDamperHalfParametricStudyTool
    from ._4396 import SpringDamperParametricStudyTool
    from ._4397 import StraightBevelDiffGearMeshParametricStudyTool
    from ._4398 import StraightBevelDiffGearParametricStudyTool
    from ._4399 import StraightBevelDiffGearSetParametricStudyTool
    from ._4400 import StraightBevelGearMeshParametricStudyTool
    from ._4401 import StraightBevelGearParametricStudyTool
    from ._4402 import StraightBevelGearSetParametricStudyTool
    from ._4403 import StraightBevelPlanetGearParametricStudyTool
    from ._4404 import StraightBevelSunGearParametricStudyTool
    from ._4405 import SynchroniserHalfParametricStudyTool
    from ._4406 import SynchroniserParametricStudyTool
    from ._4407 import SynchroniserPartParametricStudyTool
    from ._4408 import SynchroniserSleeveParametricStudyTool
    from ._4409 import TorqueConverterConnectionParametricStudyTool
    from ._4410 import TorqueConverterParametricStudyTool
    from ._4411 import TorqueConverterPumpParametricStudyTool
    from ._4412 import TorqueConverterTurbineParametricStudyTool
    from ._4413 import UnbalancedMassParametricStudyTool
    from ._4414 import VirtualComponentParametricStudyTool
    from ._4415 import WormGearMeshParametricStudyTool
    from ._4416 import WormGearParametricStudyTool
    from ._4417 import WormGearSetParametricStudyTool
    from ._4418 import ZerolBevelGearMeshParametricStudyTool
    from ._4419 import ZerolBevelGearParametricStudyTool
    from ._4420 import ZerolBevelGearSetParametricStudyTool
else:
    import_structure = {
        '_4274': ['AbstractAssemblyParametricStudyTool'],
        '_4275': ['AbstractShaftOrHousingParametricStudyTool'],
        '_4276': ['AbstractShaftParametricStudyTool'],
        '_4277': ['AbstractShaftToMountableComponentConnectionParametricStudyTool'],
        '_4278': ['AGMAGleasonConicalGearMeshParametricStudyTool'],
        '_4279': ['AGMAGleasonConicalGearParametricStudyTool'],
        '_4280': ['AGMAGleasonConicalGearSetParametricStudyTool'],
        '_4281': ['AssemblyParametricStudyTool'],
        '_4282': ['BearingParametricStudyTool'],
        '_4283': ['BeltConnectionParametricStudyTool'],
        '_4284': ['BeltDriveParametricStudyTool'],
        '_4285': ['BevelDifferentialGearMeshParametricStudyTool'],
        '_4286': ['BevelDifferentialGearParametricStudyTool'],
        '_4287': ['BevelDifferentialGearSetParametricStudyTool'],
        '_4288': ['BevelDifferentialPlanetGearParametricStudyTool'],
        '_4289': ['BevelDifferentialSunGearParametricStudyTool'],
        '_4290': ['BevelGearMeshParametricStudyTool'],
        '_4291': ['BevelGearParametricStudyTool'],
        '_4292': ['BevelGearSetParametricStudyTool'],
        '_4293': ['BoltedJointParametricStudyTool'],
        '_4294': ['BoltParametricStudyTool'],
        '_4295': ['ClutchConnectionParametricStudyTool'],
        '_4296': ['ClutchHalfParametricStudyTool'],
        '_4297': ['ClutchParametricStudyTool'],
        '_4298': ['CoaxialConnectionParametricStudyTool'],
        '_4299': ['ComponentParametricStudyTool'],
        '_4300': ['ConceptCouplingConnectionParametricStudyTool'],
        '_4301': ['ConceptCouplingHalfParametricStudyTool'],
        '_4302': ['ConceptCouplingParametricStudyTool'],
        '_4303': ['ConceptGearMeshParametricStudyTool'],
        '_4304': ['ConceptGearParametricStudyTool'],
        '_4305': ['ConceptGearSetParametricStudyTool'],
        '_4306': ['ConicalGearMeshParametricStudyTool'],
        '_4307': ['ConicalGearParametricStudyTool'],
        '_4308': ['ConicalGearSetParametricStudyTool'],
        '_4309': ['ConnectionParametricStudyTool'],
        '_4310': ['ConnectorParametricStudyTool'],
        '_4311': ['CouplingConnectionParametricStudyTool'],
        '_4312': ['CouplingHalfParametricStudyTool'],
        '_4313': ['CouplingParametricStudyTool'],
        '_4314': ['CVTBeltConnectionParametricStudyTool'],
        '_4315': ['CVTParametricStudyTool'],
        '_4316': ['CVTPulleyParametricStudyTool'],
        '_4317': ['CycloidalAssemblyParametricStudyTool'],
        '_4318': ['CycloidalDiscCentralBearingConnectionParametricStudyTool'],
        '_4319': ['CycloidalDiscParametricStudyTool'],
        '_4320': ['CycloidalDiscPlanetaryBearingConnectionParametricStudyTool'],
        '_4321': ['CylindricalGearMeshParametricStudyTool'],
        '_4322': ['CylindricalGearParametricStudyTool'],
        '_4323': ['CylindricalGearSetParametricStudyTool'],
        '_4324': ['CylindricalPlanetGearParametricStudyTool'],
        '_4325': ['DatumParametricStudyTool'],
        '_4326': ['DesignOfExperimentsVariableSetter'],
        '_4327': ['DoeValueSpecificationOption'],
        '_4328': ['DutyCycleResultsForAllComponents'],
        '_4329': ['DutyCycleResultsForAllGearSets'],
        '_4330': ['DutyCycleResultsForRootAssembly'],
        '_4331': ['DutyCycleResultsForSingleBearing'],
        '_4332': ['DutyCycleResultsForSingleShaft'],
        '_4333': ['ExternalCADModelParametricStudyTool'],
        '_4334': ['FaceGearMeshParametricStudyTool'],
        '_4335': ['FaceGearParametricStudyTool'],
        '_4336': ['FaceGearSetParametricStudyTool'],
        '_4337': ['FEPartParametricStudyTool'],
        '_4338': ['FlexiblePinAssemblyParametricStudyTool'],
        '_4339': ['GearMeshParametricStudyTool'],
        '_4340': ['GearParametricStudyTool'],
        '_4341': ['GearSetParametricStudyTool'],
        '_4342': ['GuideDxfModelParametricStudyTool'],
        '_4343': ['HypoidGearMeshParametricStudyTool'],
        '_4344': ['HypoidGearParametricStudyTool'],
        '_4345': ['HypoidGearSetParametricStudyTool'],
        '_4346': ['InterMountableComponentConnectionParametricStudyTool'],
        '_4347': ['KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool'],
        '_4348': ['KlingelnbergCycloPalloidConicalGearParametricStudyTool'],
        '_4349': ['KlingelnbergCycloPalloidConicalGearSetParametricStudyTool'],
        '_4350': ['KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool'],
        '_4351': ['KlingelnbergCycloPalloidHypoidGearParametricStudyTool'],
        '_4352': ['KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool'],
        '_4353': ['KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool'],
        '_4354': ['KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool'],
        '_4355': ['KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool'],
        '_4356': ['MassDiscParametricStudyTool'],
        '_4357': ['MeasurementComponentParametricStudyTool'],
        '_4358': ['MonteCarloDistribution'],
        '_4359': ['MountableComponentParametricStudyTool'],
        '_4360': ['OilSealParametricStudyTool'],
        '_4361': ['ParametricStudyDimension'],
        '_4362': ['ParametricStudyDOEResultVariable'],
        '_4363': ['ParametricStudyDOEResultVariableForParallelCoordinatesPlot'],
        '_4364': ['ParametricStudyHistogram'],
        '_4365': ['ParametricStudyStaticLoad'],
        '_4366': ['ParametricStudyTool'],
        '_4367': ['ParametricStudyToolOptions'],
        '_4368': ['ParametricStudyToolResultsForReporting'],
        '_4369': ['ParametricStudyToolStepResult'],
        '_4370': ['ParametricStudyVariable'],
        '_4371': ['PartParametricStudyTool'],
        '_4372': ['PartToPartShearCouplingConnectionParametricStudyTool'],
        '_4373': ['PartToPartShearCouplingHalfParametricStudyTool'],
        '_4374': ['PartToPartShearCouplingParametricStudyTool'],
        '_4375': ['PlanetaryConnectionParametricStudyTool'],
        '_4376': ['PlanetaryGearSetParametricStudyTool'],
        '_4377': ['PlanetCarrierParametricStudyTool'],
        '_4378': ['PointLoadParametricStudyTool'],
        '_4379': ['PowerLoadParametricStudyTool'],
        '_4380': ['PulleyParametricStudyTool'],
        '_4381': ['RingPinsParametricStudyTool'],
        '_4382': ['RingPinsToDiscConnectionParametricStudyTool'],
        '_4383': ['RollingRingAssemblyParametricStudyTool'],
        '_4384': ['RollingRingConnectionParametricStudyTool'],
        '_4385': ['RollingRingParametricStudyTool'],
        '_4386': ['RootAssemblyParametricStudyTool'],
        '_4387': ['ShaftHubConnectionParametricStudyTool'],
        '_4388': ['ShaftParametricStudyTool'],
        '_4389': ['ShaftToMountableComponentConnectionParametricStudyTool'],
        '_4390': ['SpecialisedAssemblyParametricStudyTool'],
        '_4391': ['SpiralBevelGearMeshParametricStudyTool'],
        '_4392': ['SpiralBevelGearParametricStudyTool'],
        '_4393': ['SpiralBevelGearSetParametricStudyTool'],
        '_4394': ['SpringDamperConnectionParametricStudyTool'],
        '_4395': ['SpringDamperHalfParametricStudyTool'],
        '_4396': ['SpringDamperParametricStudyTool'],
        '_4397': ['StraightBevelDiffGearMeshParametricStudyTool'],
        '_4398': ['StraightBevelDiffGearParametricStudyTool'],
        '_4399': ['StraightBevelDiffGearSetParametricStudyTool'],
        '_4400': ['StraightBevelGearMeshParametricStudyTool'],
        '_4401': ['StraightBevelGearParametricStudyTool'],
        '_4402': ['StraightBevelGearSetParametricStudyTool'],
        '_4403': ['StraightBevelPlanetGearParametricStudyTool'],
        '_4404': ['StraightBevelSunGearParametricStudyTool'],
        '_4405': ['SynchroniserHalfParametricStudyTool'],
        '_4406': ['SynchroniserParametricStudyTool'],
        '_4407': ['SynchroniserPartParametricStudyTool'],
        '_4408': ['SynchroniserSleeveParametricStudyTool'],
        '_4409': ['TorqueConverterConnectionParametricStudyTool'],
        '_4410': ['TorqueConverterParametricStudyTool'],
        '_4411': ['TorqueConverterPumpParametricStudyTool'],
        '_4412': ['TorqueConverterTurbineParametricStudyTool'],
        '_4413': ['UnbalancedMassParametricStudyTool'],
        '_4414': ['VirtualComponentParametricStudyTool'],
        '_4415': ['WormGearMeshParametricStudyTool'],
        '_4416': ['WormGearParametricStudyTool'],
        '_4417': ['WormGearSetParametricStudyTool'],
        '_4418': ['ZerolBevelGearMeshParametricStudyTool'],
        '_4419': ['ZerolBevelGearParametricStudyTool'],
        '_4420': ['ZerolBevelGearSetParametricStudyTool'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
