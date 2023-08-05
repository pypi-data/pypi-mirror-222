"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1603 import Acceleration
    from ._1604 import Angle
    from ._1605 import AnglePerUnitTemperature
    from ._1606 import AngleSmall
    from ._1607 import AngleVerySmall
    from ._1608 import AngularAcceleration
    from ._1609 import AngularCompliance
    from ._1610 import AngularJerk
    from ._1611 import AngularStiffness
    from ._1612 import AngularVelocity
    from ._1613 import Area
    from ._1614 import AreaSmall
    from ._1615 import CarbonEmissionFactor
    from ._1616 import CurrentDensity
    from ._1617 import CurrentPerLength
    from ._1618 import Cycles
    from ._1619 import Damage
    from ._1620 import DamageRate
    from ._1621 import DataSize
    from ._1622 import Decibel
    from ._1623 import Density
    from ._1624 import ElectricalResistance
    from ._1625 import ElectricalResistivity
    from ._1626 import ElectricCurrent
    from ._1627 import Energy
    from ._1628 import EnergyPerUnitArea
    from ._1629 import EnergyPerUnitAreaSmall
    from ._1630 import EnergySmall
    from ._1631 import Enum
    from ._1632 import FlowRate
    from ._1633 import Force
    from ._1634 import ForcePerUnitLength
    from ._1635 import ForcePerUnitPressure
    from ._1636 import ForcePerUnitTemperature
    from ._1637 import FractionMeasurementBase
    from ._1638 import FractionPerTemperature
    from ._1639 import Frequency
    from ._1640 import FuelConsumptionEngine
    from ._1641 import FuelEfficiencyVehicle
    from ._1642 import Gradient
    from ._1643 import HeatConductivity
    from ._1644 import HeatTransfer
    from ._1645 import HeatTransferCoefficientForPlasticGearTooth
    from ._1646 import HeatTransferResistance
    from ._1647 import Impulse
    from ._1648 import Index
    from ._1649 import Inductance
    from ._1650 import Integer
    from ._1651 import InverseShortLength
    from ._1652 import InverseShortTime
    from ._1653 import Jerk
    from ._1654 import KinematicViscosity
    from ._1655 import LengthLong
    from ._1656 import LengthMedium
    from ._1657 import LengthPerUnitTemperature
    from ._1658 import LengthShort
    from ._1659 import LengthToTheFourth
    from ._1660 import LengthVeryLong
    from ._1661 import LengthVeryShort
    from ._1662 import LengthVeryShortPerLengthShort
    from ._1663 import LinearAngularDamping
    from ._1664 import LinearAngularStiffnessCrossTerm
    from ._1665 import LinearDamping
    from ._1666 import LinearFlexibility
    from ._1667 import LinearStiffness
    from ._1668 import MagneticFieldStrength
    from ._1669 import MagneticFlux
    from ._1670 import MagneticFluxDensity
    from ._1671 import MagneticVectorPotential
    from ._1672 import MagnetomotiveForce
    from ._1673 import Mass
    from ._1674 import MassPerUnitLength
    from ._1675 import MassPerUnitTime
    from ._1676 import MomentOfInertia
    from ._1677 import MomentOfInertiaPerUnitLength
    from ._1678 import MomentPerUnitPressure
    from ._1679 import Number
    from ._1680 import Percentage
    from ._1681 import Power
    from ._1682 import PowerPerSmallArea
    from ._1683 import PowerPerUnitTime
    from ._1684 import PowerSmall
    from ._1685 import PowerSmallPerArea
    from ._1686 import PowerSmallPerMass
    from ._1687 import PowerSmallPerUnitAreaPerUnitTime
    from ._1688 import PowerSmallPerUnitTime
    from ._1689 import PowerSmallPerVolume
    from ._1690 import Pressure
    from ._1691 import PressurePerUnitTime
    from ._1692 import PressureVelocityProduct
    from ._1693 import PressureViscosityCoefficient
    from ._1694 import Price
    from ._1695 import PricePerUnitMass
    from ._1696 import QuadraticAngularDamping
    from ._1697 import QuadraticDrag
    from ._1698 import RescaledMeasurement
    from ._1699 import Rotatum
    from ._1700 import SafetyFactor
    from ._1701 import SpecificAcousticImpedance
    from ._1702 import SpecificHeat
    from ._1703 import SquareRootOfUnitForcePerUnitArea
    from ._1704 import StiffnessPerUnitFaceWidth
    from ._1705 import Stress
    from ._1706 import Temperature
    from ._1707 import TemperatureDifference
    from ._1708 import TemperaturePerUnitTime
    from ._1709 import Text
    from ._1710 import ThermalContactCoefficient
    from ._1711 import ThermalExpansionCoefficient
    from ._1712 import ThermoElasticFactor
    from ._1713 import Time
    from ._1714 import TimeShort
    from ._1715 import TimeVeryShort
    from ._1716 import Torque
    from ._1717 import TorqueConverterInverseK
    from ._1718 import TorqueConverterK
    from ._1719 import TorquePerCurrent
    from ._1720 import TorquePerSquareRootOfPower
    from ._1721 import TorquePerUnitTemperature
    from ._1722 import Velocity
    from ._1723 import VelocitySmall
    from ._1724 import Viscosity
    from ._1725 import Voltage
    from ._1726 import VoltagePerAngularVelocity
    from ._1727 import Volume
    from ._1728 import WearCoefficient
    from ._1729 import Yank
else:
    import_structure = {
        '_1603': ['Acceleration'],
        '_1604': ['Angle'],
        '_1605': ['AnglePerUnitTemperature'],
        '_1606': ['AngleSmall'],
        '_1607': ['AngleVerySmall'],
        '_1608': ['AngularAcceleration'],
        '_1609': ['AngularCompliance'],
        '_1610': ['AngularJerk'],
        '_1611': ['AngularStiffness'],
        '_1612': ['AngularVelocity'],
        '_1613': ['Area'],
        '_1614': ['AreaSmall'],
        '_1615': ['CarbonEmissionFactor'],
        '_1616': ['CurrentDensity'],
        '_1617': ['CurrentPerLength'],
        '_1618': ['Cycles'],
        '_1619': ['Damage'],
        '_1620': ['DamageRate'],
        '_1621': ['DataSize'],
        '_1622': ['Decibel'],
        '_1623': ['Density'],
        '_1624': ['ElectricalResistance'],
        '_1625': ['ElectricalResistivity'],
        '_1626': ['ElectricCurrent'],
        '_1627': ['Energy'],
        '_1628': ['EnergyPerUnitArea'],
        '_1629': ['EnergyPerUnitAreaSmall'],
        '_1630': ['EnergySmall'],
        '_1631': ['Enum'],
        '_1632': ['FlowRate'],
        '_1633': ['Force'],
        '_1634': ['ForcePerUnitLength'],
        '_1635': ['ForcePerUnitPressure'],
        '_1636': ['ForcePerUnitTemperature'],
        '_1637': ['FractionMeasurementBase'],
        '_1638': ['FractionPerTemperature'],
        '_1639': ['Frequency'],
        '_1640': ['FuelConsumptionEngine'],
        '_1641': ['FuelEfficiencyVehicle'],
        '_1642': ['Gradient'],
        '_1643': ['HeatConductivity'],
        '_1644': ['HeatTransfer'],
        '_1645': ['HeatTransferCoefficientForPlasticGearTooth'],
        '_1646': ['HeatTransferResistance'],
        '_1647': ['Impulse'],
        '_1648': ['Index'],
        '_1649': ['Inductance'],
        '_1650': ['Integer'],
        '_1651': ['InverseShortLength'],
        '_1652': ['InverseShortTime'],
        '_1653': ['Jerk'],
        '_1654': ['KinematicViscosity'],
        '_1655': ['LengthLong'],
        '_1656': ['LengthMedium'],
        '_1657': ['LengthPerUnitTemperature'],
        '_1658': ['LengthShort'],
        '_1659': ['LengthToTheFourth'],
        '_1660': ['LengthVeryLong'],
        '_1661': ['LengthVeryShort'],
        '_1662': ['LengthVeryShortPerLengthShort'],
        '_1663': ['LinearAngularDamping'],
        '_1664': ['LinearAngularStiffnessCrossTerm'],
        '_1665': ['LinearDamping'],
        '_1666': ['LinearFlexibility'],
        '_1667': ['LinearStiffness'],
        '_1668': ['MagneticFieldStrength'],
        '_1669': ['MagneticFlux'],
        '_1670': ['MagneticFluxDensity'],
        '_1671': ['MagneticVectorPotential'],
        '_1672': ['MagnetomotiveForce'],
        '_1673': ['Mass'],
        '_1674': ['MassPerUnitLength'],
        '_1675': ['MassPerUnitTime'],
        '_1676': ['MomentOfInertia'],
        '_1677': ['MomentOfInertiaPerUnitLength'],
        '_1678': ['MomentPerUnitPressure'],
        '_1679': ['Number'],
        '_1680': ['Percentage'],
        '_1681': ['Power'],
        '_1682': ['PowerPerSmallArea'],
        '_1683': ['PowerPerUnitTime'],
        '_1684': ['PowerSmall'],
        '_1685': ['PowerSmallPerArea'],
        '_1686': ['PowerSmallPerMass'],
        '_1687': ['PowerSmallPerUnitAreaPerUnitTime'],
        '_1688': ['PowerSmallPerUnitTime'],
        '_1689': ['PowerSmallPerVolume'],
        '_1690': ['Pressure'],
        '_1691': ['PressurePerUnitTime'],
        '_1692': ['PressureVelocityProduct'],
        '_1693': ['PressureViscosityCoefficient'],
        '_1694': ['Price'],
        '_1695': ['PricePerUnitMass'],
        '_1696': ['QuadraticAngularDamping'],
        '_1697': ['QuadraticDrag'],
        '_1698': ['RescaledMeasurement'],
        '_1699': ['Rotatum'],
        '_1700': ['SafetyFactor'],
        '_1701': ['SpecificAcousticImpedance'],
        '_1702': ['SpecificHeat'],
        '_1703': ['SquareRootOfUnitForcePerUnitArea'],
        '_1704': ['StiffnessPerUnitFaceWidth'],
        '_1705': ['Stress'],
        '_1706': ['Temperature'],
        '_1707': ['TemperatureDifference'],
        '_1708': ['TemperaturePerUnitTime'],
        '_1709': ['Text'],
        '_1710': ['ThermalContactCoefficient'],
        '_1711': ['ThermalExpansionCoefficient'],
        '_1712': ['ThermoElasticFactor'],
        '_1713': ['Time'],
        '_1714': ['TimeShort'],
        '_1715': ['TimeVeryShort'],
        '_1716': ['Torque'],
        '_1717': ['TorqueConverterInverseK'],
        '_1718': ['TorqueConverterK'],
        '_1719': ['TorquePerCurrent'],
        '_1720': ['TorquePerSquareRootOfPower'],
        '_1721': ['TorquePerUnitTemperature'],
        '_1722': ['Velocity'],
        '_1723': ['VelocitySmall'],
        '_1724': ['Viscosity'],
        '_1725': ['Voltage'],
        '_1726': ['VoltagePerAngularVelocity'],
        '_1727': ['Volume'],
        '_1728': ['WearCoefficient'],
        '_1729': ['Yank'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
