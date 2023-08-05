"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1239 import AbstractStator
    from ._1240 import AbstractToothAndSlot
    from ._1241 import CADConductor
    from ._1242 import CADElectricMachineDetail
    from ._1243 import CADMagnetsForLayer
    from ._1244 import CADRotor
    from ._1245 import CADStator
    from ._1246 import CADToothAndSlot
    from ._1247 import Coil
    from ._1248 import CoilPositionInSlot
    from ._1249 import CoolingDuctLayerSpecification
    from ._1250 import CoolingDuctShape
    from ._1251 import CoreLossBuildFactorSpecificationMethod
    from ._1252 import CoreLossCoefficients
    from ._1253 import DoubleLayerWindingSlotPositions
    from ._1254 import DQAxisConvention
    from ._1255 import Eccentricity
    from ._1256 import ElectricMachineDetail
    from ._1257 import ElectricMachineDetailInitialInformation
    from ._1258 import ElectricMachineMechanicalAnalysisMeshingOptions
    from ._1259 import ElectricMachineMeshingOptions
    from ._1260 import ElectricMachineMeshingOptionsBase
    from ._1261 import ElectricMachineSetup
    from ._1262 import ElectricMachineType
    from ._1263 import FillFactorSpecificationMethod
    from ._1264 import FluxBarrierOrWeb
    from ._1265 import FluxBarrierStyle
    from ._1266 import HairpinConductor
    from ._1267 import HarmonicLoadDataControlExcitationOptionForElectricMachineMode
    from ._1268 import IndividualConductorSpecificationSource
    from ._1269 import InteriorPermanentMagnetAndSynchronousReluctanceRotor
    from ._1270 import InteriorPermanentMagnetMachine
    from ._1271 import IronLossCoefficientSpecificationMethod
    from ._1272 import MagnetConfiguration
    from ._1273 import MagnetDesign
    from ._1274 import MagnetForLayer
    from ._1275 import MagnetMaterial
    from ._1276 import MagnetMaterialDatabase
    from ._1277 import MotorRotorSideFaceDetail
    from ._1278 import NonCADElectricMachineDetail
    from ._1279 import NotchShape
    from ._1280 import NotchSpecification
    from ._1281 import PermanentMagnetAssistedSynchronousReluctanceMachine
    from ._1282 import PermanentMagnetRotor
    from ._1283 import Phase
    from ._1284 import RegionID
    from ._1285 import Rotor
    from ._1286 import RotorInternalLayerSpecification
    from ._1287 import RotorSkewSlice
    from ._1288 import RotorType
    from ._1289 import SingleOrDoubleLayerWindings
    from ._1290 import SlotSectionDetail
    from ._1291 import Stator
    from ._1292 import StatorCutOutSpecification
    from ._1293 import StatorRotorMaterial
    from ._1294 import StatorRotorMaterialDatabase
    from ._1295 import SurfacePermanentMagnetMachine
    from ._1296 import SurfacePermanentMagnetRotor
    from ._1297 import SynchronousReluctanceMachine
    from ._1298 import ToothAndSlot
    from ._1299 import ToothSlotStyle
    from ._1300 import TwoDimensionalFEModelForAnalysis
    from ._1301 import UShapedLayerSpecification
    from ._1302 import VShapedMagnetLayerSpecification
    from ._1303 import WindingConductor
    from ._1304 import WindingConnection
    from ._1305 import WindingMaterial
    from ._1306 import WindingMaterialDatabase
    from ._1307 import Windings
    from ._1308 import WindingsViewer
    from ._1309 import WindingType
    from ._1310 import WireSizeSpecificationMethod
    from ._1311 import WoundFieldSynchronousMachine
else:
    import_structure = {
        '_1239': ['AbstractStator'],
        '_1240': ['AbstractToothAndSlot'],
        '_1241': ['CADConductor'],
        '_1242': ['CADElectricMachineDetail'],
        '_1243': ['CADMagnetsForLayer'],
        '_1244': ['CADRotor'],
        '_1245': ['CADStator'],
        '_1246': ['CADToothAndSlot'],
        '_1247': ['Coil'],
        '_1248': ['CoilPositionInSlot'],
        '_1249': ['CoolingDuctLayerSpecification'],
        '_1250': ['CoolingDuctShape'],
        '_1251': ['CoreLossBuildFactorSpecificationMethod'],
        '_1252': ['CoreLossCoefficients'],
        '_1253': ['DoubleLayerWindingSlotPositions'],
        '_1254': ['DQAxisConvention'],
        '_1255': ['Eccentricity'],
        '_1256': ['ElectricMachineDetail'],
        '_1257': ['ElectricMachineDetailInitialInformation'],
        '_1258': ['ElectricMachineMechanicalAnalysisMeshingOptions'],
        '_1259': ['ElectricMachineMeshingOptions'],
        '_1260': ['ElectricMachineMeshingOptionsBase'],
        '_1261': ['ElectricMachineSetup'],
        '_1262': ['ElectricMachineType'],
        '_1263': ['FillFactorSpecificationMethod'],
        '_1264': ['FluxBarrierOrWeb'],
        '_1265': ['FluxBarrierStyle'],
        '_1266': ['HairpinConductor'],
        '_1267': ['HarmonicLoadDataControlExcitationOptionForElectricMachineMode'],
        '_1268': ['IndividualConductorSpecificationSource'],
        '_1269': ['InteriorPermanentMagnetAndSynchronousReluctanceRotor'],
        '_1270': ['InteriorPermanentMagnetMachine'],
        '_1271': ['IronLossCoefficientSpecificationMethod'],
        '_1272': ['MagnetConfiguration'],
        '_1273': ['MagnetDesign'],
        '_1274': ['MagnetForLayer'],
        '_1275': ['MagnetMaterial'],
        '_1276': ['MagnetMaterialDatabase'],
        '_1277': ['MotorRotorSideFaceDetail'],
        '_1278': ['NonCADElectricMachineDetail'],
        '_1279': ['NotchShape'],
        '_1280': ['NotchSpecification'],
        '_1281': ['PermanentMagnetAssistedSynchronousReluctanceMachine'],
        '_1282': ['PermanentMagnetRotor'],
        '_1283': ['Phase'],
        '_1284': ['RegionID'],
        '_1285': ['Rotor'],
        '_1286': ['RotorInternalLayerSpecification'],
        '_1287': ['RotorSkewSlice'],
        '_1288': ['RotorType'],
        '_1289': ['SingleOrDoubleLayerWindings'],
        '_1290': ['SlotSectionDetail'],
        '_1291': ['Stator'],
        '_1292': ['StatorCutOutSpecification'],
        '_1293': ['StatorRotorMaterial'],
        '_1294': ['StatorRotorMaterialDatabase'],
        '_1295': ['SurfacePermanentMagnetMachine'],
        '_1296': ['SurfacePermanentMagnetRotor'],
        '_1297': ['SynchronousReluctanceMachine'],
        '_1298': ['ToothAndSlot'],
        '_1299': ['ToothSlotStyle'],
        '_1300': ['TwoDimensionalFEModelForAnalysis'],
        '_1301': ['UShapedLayerSpecification'],
        '_1302': ['VShapedMagnetLayerSpecification'],
        '_1303': ['WindingConductor'],
        '_1304': ['WindingConnection'],
        '_1305': ['WindingMaterial'],
        '_1306': ['WindingMaterialDatabase'],
        '_1307': ['Windings'],
        '_1308': ['WindingsViewer'],
        '_1309': ['WindingType'],
        '_1310': ['WireSizeSpecificationMethod'],
        '_1311': ['WoundFieldSynchronousMachine'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
