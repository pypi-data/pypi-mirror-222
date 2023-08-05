"""_170.py

ElmerResultsFromElectroMagneticAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.nodal_analysis.elmer import _169
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELMER_RESULTS_FROM_ELECTRO_MAGNETIC_ANALYSIS = python_net_import('SMT.MastaAPI.NodalAnalysis.Elmer', 'ElmerResultsFromElectroMagneticAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ElmerResultsFromElectroMagneticAnalysis',)


class ElmerResultsFromElectroMagneticAnalysis(_169.ElmerResults):
    """ElmerResultsFromElectroMagneticAnalysis

    This is a mastapy class.
    """

    TYPE = _ELMER_RESULTS_FROM_ELECTRO_MAGNETIC_ANALYSIS

    class _Cast_ElmerResultsFromElectroMagneticAnalysis:
        """Special nested class for casting ElmerResultsFromElectroMagneticAnalysis to subclasses."""

        def __init__(self, parent: 'ElmerResultsFromElectroMagneticAnalysis'):
            self._parent = parent

        @property
        def elmer_results(self):
            return self._parent._cast(_169.ElmerResults)

        @property
        def elmer_results_from_electro_magnetic_analysis(self) -> 'ElmerResultsFromElectroMagneticAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElmerResultsFromElectroMagneticAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElmerResultsFromElectroMagneticAnalysis._Cast_ElmerResultsFromElectroMagneticAnalysis':
        return self._Cast_ElmerResultsFromElectroMagneticAnalysis(self)
