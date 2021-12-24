#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from prespa.automata.machine import PNTHFA
from prespa.automata.tfmath import ZERO, ONE, THFE

import numpy as np

import itertools


def getMeasures(img, iLine, iCol, d):
    """Get measures in sub-image"""
    M = np.zeros((d,d), dtype=float)
    for i in range(d):
        for j in range(d):
            M[i][j] = img[i + iLine][j + iCol]
    return [M.min(), M.mean(), np.median(M), M.max()]


def buildTreeAutomaton(img=None, depth=0, n=0):
    """Build the tree automaton"""
    function_xi = dict()

    states = set()
    delta = dict()
    F = dict()
    states.add(0)

    F[0] = ONE
    function_xi[0] = [0, 0, n]
    
    S = 0
    measures = dict()
    
    while True:
        C = function_xi[S]

        iLine = C[0]
        iCol = C[1]
        desl = C[2]

        D = int(desl/2)
        if D == 0:
            break

        S1 = len(states)
        S2 = S1 + 1
        S3 = S2 + 1
        S4 = S3 + 1

        states.add(S1)
        states.add(S2)
        states.add(S3)
        states.add(S4)

        d1 = (S, '1')
        d2 = (S, '2')
        d3 = (S, '3')
        d4 = (S, '4')

        delta[d1] = S1
        delta[d2] = S2
        delta[d3] = S3
        delta[d4] = S4

        c1 = [iLine, iCol, D]
        c2 = [iLine, iCol + D, D]
        c3 = [iLine + D, iCol, D]
        c4 = [iLine + D, iCol + D, D]

        function_xi[S1] = c1 
        function_xi[S2] = c2
        function_xi[S3] = c3
        function_xi[S4] = c4

        if S == 0:
            measures[S] = getMeasures(img, iLine, iCol, desl)
            measures[S1] = getMeasures(img, c1[0], c1[1], c1[2])
            measures[S2] = getMeasures(img, c2[0], c2[1], c2[2])
            measures[S3] = getMeasures(img, c3[0], c3[1], c3[2])
            measures[S4] = getMeasures(img, c4[0], c4[1], c4[2])
        else:
            measures[S1] = getMeasures(img, c1[0], c1[1], c1[2])
            measures[S2] = getMeasures(img, c2[0], c2[1], c2[2])
            measures[S3] = getMeasures(img, c3[0], c3[1], c3[2])
            measures[S4] = getMeasures(img, c4[0], c4[1], c4[2])

        L0 = measures[S]
        L1 = measures[S1]
        L2 = measures[S2]
        L3 = measures[S3]
        L4 = measures[S4]

        del measures[S]

        k = len(L0)

        Sim1 = []
        Sim2 = []
        Sim3 = []
        Sim4 = []

        for e in range(k):
            Sim1.append( 1.0 - abs(L0[e] - L1[e]) )
            Sim2.append( 1.0 - abs(L0[e] - L2[e]) )
            Sim3.append( 1.0 - abs(L0[e] - L3[e]) )
            Sim4.append( 1.0 - abs(L0[e] - L4[e]) )
        
        F[S1] = THFE(*Sim1)
        F[S2] = THFE(*Sim2)
        F[S3] = THFE(*Sim3)
        F[S4] = THFE(*Sim4)

        S = S + 1
    measures = None
    machine = PNTHFA(delta, F)
    return machine, function_xi

def createListWord(n):
    """Creates the list of word with size n on the alphabet {1,2,3,4}."""
    temp = [''.join(x) for x in itertools.product('1234', repeat=n)]
    L = [int(y) for y in temp]
    return L
