#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from automata.exceptions import NotDefineTransition

from automata.tfmath import ZERO

"""This file provides the class that implements pseudo typical hesitant fuzzy automaton."""

class PNTHFA(object):
    def __init__(self, delta = None, F = None):
        self._s0 = 0
        self.__delta = delta
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

    def computePrefixes(self, word, deep):
        subStrings = []
        n = len(word)
        for i in range(n, 0, -1):
            S = word[0:i]
            subStrings.append(S)
            if len(subStrings) > deep:
                break
        output = ZERO
        for w in subStrings:
            s = self.compute(w)
            if s != None:
                output = output + self.__F[s]
        return output
    
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