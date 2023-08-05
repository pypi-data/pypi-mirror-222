"""_1316.py

ElectricMachineMechanicalResultsViewable
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.nodal_analysis.elmer import _171
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_MECHANICAL_RESULTS_VIEWABLE = python_net_import('SMT.MastaAPI.ElectricMachines.Results', 'ElectricMachineMechanicalResultsViewable')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineMechanicalResultsViewable',)


class ElectricMachineMechanicalResultsViewable(_171.ElmerResultsViewable):
    """ElectricMachineMechanicalResultsViewable

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_MECHANICAL_RESULTS_VIEWABLE

    class _Cast_ElectricMachineMechanicalResultsViewable:
        """Special nested class for casting ElectricMachineMechanicalResultsViewable to subclasses."""

        def __init__(self, parent: 'ElectricMachineMechanicalResultsViewable'):
            self._parent = parent

        @property
        def elmer_results_viewable(self):
            return self._parent._cast(_171.ElmerResultsViewable)

        @property
        def electric_machine_mechanical_results_viewable(self) -> 'ElectricMachineMechanicalResultsViewable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineMechanicalResultsViewable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElectricMachineMechanicalResultsViewable._Cast_ElectricMachineMechanicalResultsViewable':
        return self._Cast_ElectricMachineMechanicalResultsViewable(self)
