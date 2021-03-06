#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from prespa.automata.exceptions import NotDefineTransition
from prespa.automata.tfmath import ZERO

"""This file provides the class that implements pseudo typical hesitant fuzzy automaton."""

class PNTHFA(object):
    def __init__(self, function_delta = None, F = None):
        self._s0 = 0
        self.__delta = function_delta
        self.__F = F

    def compute(self, word):
        S = 0
        for c in word:
            L = tuple([S, c])
            if L in self.__delta:
                S = self.__delta[L]
            else:
                raise NotDefineTransition('The transition {} not is define.'.format(L))
        return S

    def getValuationState(self, state):
        if state <= len(self):
            return self.__F[state]
        else:
            return None
    
    def __len__(self):
        return len(self.__F)    

    def __str__(self):
        output = ''
        S = set()
        X = set(["1", "2", "3", "4"])
        D = ''
        F = ''
        for key, value  in self.__delta.items():
            S.add(key[0])
            D = D + '\u03B4' + str(key) + '=' + str(value) + '\n'
        for key, value in self.__F.items():
            F = F + '\u03BC(' + str(key) + ')=' + str(value) + '\n'
        output = output + str(S) + "\n" + str(X) + "\n" + str(self.__s0) + '\n' + D + F
        return output