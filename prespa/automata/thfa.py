from prespa.automata.exceptions import NotDefineTransition
from prespa.automata.tfmath import ZERO, ONE

"""This file provides the class that implements Typical Hesitant Fuzzy Automaton."""

class THFA(object):
    
    def __init__(self, function_delta = None, valuation_delta = None, F = None):
        self._s0 = 0
        self.__delta = function_delta
        self.__valuation = valuation_delta 
        self.__F = F

    def compute(self, word):
        vCompute = ONE
        s = 0
        for c in word:
            D = [s, c]
            if D in self.__delta:
                s = self.__delta[D]
                V = [D[1], c, s]
                vCompute = vCompute * self.__valuation[V]
            else:
                raise NotDefineTransition('The transition \u03BC({s}, {c}) not is define.')
        return vCompute * self.__F[s]

    def __len__(self):
        return len(self.__F)    

    def __str__(self):
        output = ''
        S = set()
        X = set(["1", "2", "3", "4"])
        D = ''
        F = ''
        for key, value  in self.__valuation.items():
            S.add(key[0])
            D = D + '\u03B4(' + str(key[0]) + ',' + str(key[1]) + ',' + str(key[2]) + ')=' + str(value) + '\n'
        for key, value in self.__F.items():
            F = F + '\u03BC(' + str(key) + ')=' + str(value) + '\n'
        output = output + str(S) + "\n" + str(X) + "\n" + str(self.__s0) + '\n' + D + F
        return output