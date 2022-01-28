from prespa.automata.exceptions import NotDefineTransition
from prespa.automata.tfmath import ZERO, ONE

"""This file provides the class that implements Typical Hesitant Fuzzy Automaton."""

class THFA(object):
    
    def __init__(self, delta = None, F = None):
        self._s0 = 0
        self.__delta = delta 
        self.__F = F
        self.__deltaAux = dict()
        self.__startDeltaAux()

    def __startDeltaAux(self):
        for D in self.__delta:
            L = (D[0], D[1])
            self.__deltaAux[L] = D[2]

    def compute(self, word):
        vCompute = ONE
        s = 0
        for c in word:
            L = (s, c)
            if L in self.__deltaAux:
                p = self.__deltaAux[L]
                T = (s, c, p)
                vCompute = vCompute * self.__delta[T]
                s = p
            else:
                NotDefineTransition(f'The transition for the pair ({s}, {c}) not is define.')
        return s, vCompute

    def __len__(self):
        return len(self.__F)    

    def __str__(self):
        output = ''
        S = set()
        X = set(["1", "2", "3", "4"])
        D = ''
        F = ''
        for key, v  in self.__delta.items():
            s1 = key[0]
            c = key[1]
            s2 = key[2]
            S.add(s1)
            S.add(s2)
            D = D + '\u03B4(' + str(s1) + ',' + c + ',' + str(s2) + ')=' + str(v) + '\n'
        for key, value in self.__F.items():
            F = F + '\u03BC(' + str(key) + ')=' + str(value) + '\n'
        output = output + str(S) + "\n" + str(X) + "\n" + str(self.__s0) + '\n' + D + F
        return output