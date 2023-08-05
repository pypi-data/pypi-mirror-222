﻿"""_1130.py

AGMA20151AccuracyGrades
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1134
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA20151_ACCURACY_GRADES = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances', 'AGMA20151AccuracyGrades')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMA20151AccuracyGrades',)


class AGMA20151AccuracyGrades(_1134.CylindricalAccuracyGrades):
    """AGMA20151AccuracyGrades

    This is a mastapy class.
    """

    TYPE = _AGMA20151_ACCURACY_GRADES

    class _Cast_AGMA20151AccuracyGrades:
        """Special nested class for casting AGMA20151AccuracyGrades to subclasses."""

        def __init__(self, parent: 'AGMA20151AccuracyGrades'):
            self._parent = parent

        @property
        def cylindrical_accuracy_grades(self):
            return self._parent._cast(_1134.CylindricalAccuracyGrades)

        @property
        def accuracy_grades(self):
            from mastapy.gears import _312
            
            return self._parent._cast(_312.AccuracyGrades)

        @property
        def agma20151_accuracy_grades(self) -> 'AGMA20151AccuracyGrades':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMA20151AccuracyGrades.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def helix_agma_quality_grade_new(self) -> 'int':
        """int: 'HelixAGMAQualityGradeNew' is the original name of this property."""

        temp = self.wrapped.HelixAGMAQualityGradeNew

        if temp is None:
            return 0

        return temp

    @helix_agma_quality_grade_new.setter
    def helix_agma_quality_grade_new(self, value: 'int'):
        self.wrapped.HelixAGMAQualityGradeNew = int(value) if value is not None else 0

    @property
    def helix_agma_quality_grade_old(self) -> 'int':
        """int: 'HelixAGMAQualityGradeOld' is the original name of this property."""

        temp = self.wrapped.HelixAGMAQualityGradeOld

        if temp is None:
            return 0

        return temp

    @helix_agma_quality_grade_old.setter
    def helix_agma_quality_grade_old(self, value: 'int'):
        self.wrapped.HelixAGMAQualityGradeOld = int(value) if value is not None else 0

    @property
    def pitch_agma_quality_grade_new(self) -> 'int':
        """int: 'PitchAGMAQualityGradeNew' is the original name of this property."""

        temp = self.wrapped.PitchAGMAQualityGradeNew

        if temp is None:
            return 0

        return temp

    @pitch_agma_quality_grade_new.setter
    def pitch_agma_quality_grade_new(self, value: 'int'):
        self.wrapped.PitchAGMAQualityGradeNew = int(value) if value is not None else 0

    @property
    def pitch_agma_quality_grade_old(self) -> 'int':
        """int: 'PitchAGMAQualityGradeOld' is the original name of this property."""

        temp = self.wrapped.PitchAGMAQualityGradeOld

        if temp is None:
            return 0

        return temp

    @pitch_agma_quality_grade_old.setter
    def pitch_agma_quality_grade_old(self, value: 'int'):
        self.wrapped.PitchAGMAQualityGradeOld = int(value) if value is not None else 0

    @property
    def profile_agma_quality_grade_new(self) -> 'int':
        """int: 'ProfileAGMAQualityGradeNew' is the original name of this property."""

        temp = self.wrapped.ProfileAGMAQualityGradeNew

        if temp is None:
            return 0

        return temp

    @profile_agma_quality_grade_new.setter
    def profile_agma_quality_grade_new(self, value: 'int'):
        self.wrapped.ProfileAGMAQualityGradeNew = int(value) if value is not None else 0

    @property
    def profile_agma_quality_grade_old(self) -> 'int':
        """int: 'ProfileAGMAQualityGradeOld' is the original name of this property."""

        temp = self.wrapped.ProfileAGMAQualityGradeOld

        if temp is None:
            return 0

        return temp

    @profile_agma_quality_grade_old.setter
    def profile_agma_quality_grade_old(self, value: 'int'):
        self.wrapped.ProfileAGMAQualityGradeOld = int(value) if value is not None else 0

    @property
    def radial_agma_quality_grade_new(self) -> 'int':
        """int: 'RadialAGMAQualityGradeNew' is the original name of this property."""

        temp = self.wrapped.RadialAGMAQualityGradeNew

        if temp is None:
            return 0

        return temp

    @radial_agma_quality_grade_new.setter
    def radial_agma_quality_grade_new(self, value: 'int'):
        self.wrapped.RadialAGMAQualityGradeNew = int(value) if value is not None else 0

    @property
    def radial_agma_quality_grade_old(self) -> 'int':
        """int: 'RadialAGMAQualityGradeOld' is the original name of this property."""

        temp = self.wrapped.RadialAGMAQualityGradeOld

        if temp is None:
            return 0

        return temp

    @radial_agma_quality_grade_old.setter
    def radial_agma_quality_grade_old(self, value: 'int'):
        self.wrapped.RadialAGMAQualityGradeOld = int(value) if value is not None else 0

    @property
    def cast_to(self) -> 'AGMA20151AccuracyGrades._Cast_AGMA20151AccuracyGrades':
        return self._Cast_AGMA20151AccuracyGrades(self)
