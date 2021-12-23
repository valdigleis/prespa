#!/usr/bin/env python3
"""Exception classes used by automata and fuzzy hesitant elements."""


class THFEException(Exception):
    """The base class for THFE errors."""

    pass

class EmptyInput(THFEException):
    """Empty input to build THFE."""

    pass

class TypeNumericError(THFEException):
    """THe value used to build THFE not belongs to range [0,1]."""

    pass

class NotIsTHFE(THFEException):
    """The object not is THFE"""

    pass

class NumberOutRange(THFEException):
    """A number passed not belongs to interval [0,1]"""

    pass

class MachineException(Exception):
    """The base class for machine errors."""

    pass

class NotDefineTransition(MachineException):
    """The transitions not is define"""

    pass