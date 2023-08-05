﻿"""_119.py

WilsonThetaTransientSolver
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.nodal_analysis.system_solvers import _116
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WILSON_THETA_TRANSIENT_SOLVER = python_net_import('SMT.MastaAPI.NodalAnalysis.SystemSolvers', 'WilsonThetaTransientSolver')


__docformat__ = 'restructuredtext en'
__all__ = ('WilsonThetaTransientSolver',)


class WilsonThetaTransientSolver(_116.StepHalvingTransientSolver):
    """WilsonThetaTransientSolver

    This is a mastapy class.
    """

    TYPE = _WILSON_THETA_TRANSIENT_SOLVER

    class _Cast_WilsonThetaTransientSolver:
        """Special nested class for casting WilsonThetaTransientSolver to subclasses."""

        def __init__(self, parent: 'WilsonThetaTransientSolver'):
            self._parent = parent

        @property
        def step_halving_transient_solver(self):
            return self._parent._cast(_116.StepHalvingTransientSolver)

        @property
        def internal_transient_solver(self):
            from mastapy.nodal_analysis.system_solvers import _104
            
            return self._parent._cast(_104.InternalTransientSolver)

        @property
        def transient_solver(self):
            from mastapy.nodal_analysis.system_solvers import _118
            
            return self._parent._cast(_118.TransientSolver)

        @property
        def dynamic_solver(self):
            from mastapy.nodal_analysis.system_solvers import _103
            
            return self._parent._cast(_103.DynamicSolver)

        @property
        def stiffness_solver(self):
            from mastapy.nodal_analysis.system_solvers import _117
            
            return self._parent._cast(_117.StiffnessSolver)

        @property
        def solver(self):
            from mastapy.nodal_analysis.system_solvers import _115
            
            return self._parent._cast(_115.Solver)

        @property
        def wilson_theta_transient_solver(self) -> 'WilsonThetaTransientSolver':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WilsonThetaTransientSolver.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'WilsonThetaTransientSolver._Cast_WilsonThetaTransientSolver':
        return self._Cast_WilsonThetaTransientSolver(self)
