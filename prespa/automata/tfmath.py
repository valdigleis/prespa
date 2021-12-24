#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from prespa.automata.exceptions import NumberOutRange, EmptyInput, TypeNumericError, NotIsTHFE

"""This file provides the class and also predefined objects for working with typical hesitant fuzzy math."""

class THFE(object):
    """This class provides an implementation for the notion of Typical Fuzzy Heitant Element."""

    def __init__(self, *values):
        if len(values) > 0:
            self.__degrees = set()
            for i in range(len(values)):
                if not isinstance(values[i], float):
                    raise TypeNumericError('The value {} not is an instance of float.'.format(values[i]))
                elif values[i] < 0.0 or values[i] > 1.0:
                    raise NumberOutRange('The value {} not belongs to range [0,1]'.format(values[i]))
                else:
                    self.__degrees.add(values[i])
            self.__ubound = max(self.__degrees)
            self.__lbound = min(self.__degrees)
        else:
            raise EmptyInput
    
    def getDegrees(self):
        """Returns the fuzzy degress belongs to THFE"""
        return self.__degrees

    def getUpperBound(self):
        """Returns the upper bound this THFE"""
        return self.__ubound

    def getLowerBound(self):
        """Returns the lower bound this THFE"""
        return self.__lbound
    
    def meanCollapse(self):
        """Collapses the THFE to a value in the range [0.1] using the arithmetic mean."""
        S = 0.0
        for x in self.__degrees:
            S = S + x
        return S/len(self.__degrees)

    def __add__(self, other):
        """Compute max combination."""
        if not isinstance(other, THFE):
            raise NotIsTHFE('Both objects must be THFE')
        if self.__ubound <= other.getLowerBound():
            return other
        else:
            S = set()
            for x in self.__degrees:
                for y in other.getDegrees():
                    S.add(max(x, y))
            return THFE(*S)

    def __mul__(self, other):
        """Compute min combination."""
        if not isinstance(other, THFE):
            raise NotIsTHFE('Both objects must be THFE')
        if self.__ubound <= other.getLowerBound():
            return self
        else:
            S = set()
            for x in self.__degrees:
                for y in other.getDegrees():
                    S.add(min(x, y))
            return THFE(*S)

    def __eq__(self, other):
        """Verify if two THFE are equals."""
        if not isinstance(other, THFE):
            raise NotIsTHFE('Both objects must be THFE')
        else:
            return self.__degrees == other.getDegrees()

    def __str__(self) -> str:
        return str(self.__degrees)


ONE = THFE(1.0)
ZERO = THFE(0.0)