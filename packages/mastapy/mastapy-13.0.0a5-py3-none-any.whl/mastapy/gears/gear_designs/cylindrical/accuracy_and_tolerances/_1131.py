"""_1131.py

AGMAISO13281B14AccuracyGrader
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1138
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMAISO13281B14_ACCURACY_GRADER = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances', 'AGMAISO13281B14AccuracyGrader')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAISO13281B14AccuracyGrader',)


class AGMAISO13281B14AccuracyGrader(_1138.ISO132812013AccuracyGrader):
    """AGMAISO13281B14AccuracyGrader

    This is a mastapy class.
    """

    TYPE = _AGMAISO13281B14_ACCURACY_GRADER

    class _Cast_AGMAISO13281B14AccuracyGrader:
        """Special nested class for casting AGMAISO13281B14AccuracyGrader to subclasses."""

        def __init__(self, parent: 'AGMAISO13281B14AccuracyGrader'):
            self._parent = parent

        @property
        def iso132812013_accuracy_grader(self):
            return self._parent._cast(_1138.ISO132812013AccuracyGrader)

        @property
        def iso1328_accuracy_grader_common(self):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1139
            
            return self._parent._cast(_1139.ISO1328AccuracyGraderCommon)

        @property
        def cylindrical_accuracy_grader_with_profile_form_and_slope(self):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1133
            
            return self._parent._cast(_1133.CylindricalAccuracyGraderWithProfileFormAndSlope)

        @property
        def cylindrical_accuracy_grader(self):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1132
            
            return self._parent._cast(_1132.CylindricalAccuracyGrader)

        @property
        def agmaiso13281b14_accuracy_grader(self) -> 'AGMAISO13281B14AccuracyGrader':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAISO13281B14AccuracyGrader.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AGMAISO13281B14AccuracyGrader._Cast_AGMAISO13281B14AccuracyGrader':
        return self._Cast_AGMAISO13281B14AccuracyGrader(self)
