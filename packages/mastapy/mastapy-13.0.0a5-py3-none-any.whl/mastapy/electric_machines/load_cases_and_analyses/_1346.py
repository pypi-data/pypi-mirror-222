"""_1346.py

ElectricMachineFEMechanicalAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.electric_machines.load_cases_and_analyses import _1341
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_FE_MECHANICAL_ANALYSIS = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'ElectricMachineFEMechanicalAnalysis')

if TYPE_CHECKING:
    from mastapy.nodal_analysis.elmer import _171


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineFEMechanicalAnalysis',)


class ElectricMachineFEMechanicalAnalysis(_1341.ElectricMachineAnalysis):
    """ElectricMachineFEMechanicalAnalysis

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_FE_MECHANICAL_ANALYSIS

    class _Cast_ElectricMachineFEMechanicalAnalysis:
        """Special nested class for casting ElectricMachineFEMechanicalAnalysis to subclasses."""

        def __init__(self, parent: 'ElectricMachineFEMechanicalAnalysis'):
            self._parent = parent

        @property
        def electric_machine_analysis(self):
            return self._parent._cast(_1341.ElectricMachineAnalysis)

        @property
        def electric_machine_fe_mechanical_analysis(self) -> 'ElectricMachineFEMechanicalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineFEMechanicalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def viewable(self) -> '_171.ElmerResultsViewable':
        """ElmerResultsViewable: 'Viewable' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Viewable

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ElectricMachineFEMechanicalAnalysis._Cast_ElectricMachineFEMechanicalAnalysis':
        return self._Cast_ElectricMachineFEMechanicalAnalysis(self)
