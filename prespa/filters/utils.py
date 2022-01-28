#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from prespa.automata.thfa import THFA

from prespa.automata.tfmath import ZERO, ONE, THFE

import numpy as np

import itertools

def createListWord(n):
    """Creates the list of word with size n on the alphabet {1,2,3,4}."""
    temp = [''.join(x) for x in itertools.product('1234', repeat=n)]
    L = [int(y) for y in temp]
    return L

def getMeasures(img, iLine, iCol, d):
    """Get measures in sub-image"""
    M = np.zeros((d,d), dtype=float)
    for i in range(d):
        for j in range(d):
            M[i][j] = img[i + iLine][j + iCol]
    return [M.min(), M.mean(), np.median(M), M.max()]

def buildTHFA(image=None, n=0, mode='complete'):
    
    function_xi = dict()

    states = set()
    delta = dict()
    F = dict()
    states.add(0)

    F[0] = ONE
    function_xi[0] = [0, 0, n]

    S = 0

    # Criando a função xi e as transições.
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

        c1 = [iLine, iCol, D]
        c2 = [iLine, iCol + D, D]
        c3 = [iLine + D, iCol, D]
        c4 = [iLine + D, iCol + D, D]

        function_xi[S1] = c1 
        function_xi[S2] = c2
        function_xi[S3] = c3
        function_xi[S4] = c4

        F[S1] = ONE
        F[S2] = ONE
        F[S3] = ONE
        F[S4] = ONE

        T1 = (S, '1', S1) 
        T2 = (S, '2', S2)
        T3 = (S, '3', S3)
        T4 = (S, '4', S4)

        if mode == 'complete':
            measuresS = getMeasures(image, iLine, iCol, desl)
            measuresS1 = getMeasures(image, c1[0], c1[1], c1[2])
            measuresS2 = getMeasures(image, c2[0], c2[1], c2[2])
            measuresS3 = getMeasures(image, c3[0], c3[1], c3[2])
            measuresS4 = getMeasures(image, c4[0], c4[1], c4[2])
            k = len(measuresS)
            sT1 = []
            sT2 = []
            sT3 = []
            sT4 = []
            for i in range(k):
                sT1.append( 1.0 - abs(measuresS[i] - measuresS1[i]))
                sT2.append( 1.0 - abs(measuresS[i] - measuresS2[i]))
                sT3.append( 1.0 - abs(measuresS[i] - measuresS3[i]))
                sT4.append( 1.0 - abs(measuresS[i] - measuresS4[i]))
            delta[T1] = THFE(*sT1)
            delta[T2] = THFE(*sT2)
            delta[T3] = THFE(*sT3)
            delta[T4] = THFE(*sT4)
        else:
            if c1[2] == 1:
                measuresS = getMeasures(image, iLine, iCol, desl)
                measuresS1 = getMeasures(image, c1[0], c1[1], c1[2])
                measuresS2 = getMeasures(image, c2[0], c2[1], c2[2])
                measuresS3 = getMeasures(image, c3[0], c3[1], c3[2])
                measuresS4 = getMeasures(image, c4[0], c4[1], c4[2])
                k = len(measuresS)
                sT1 = []
                sT2 = []
                sT3 = []
                sT4 = []
                for id in range(k):
                    sT1.append( 1.0 - abs(measuresS[id] - measuresS1[id]))
                    sT2.append( 1.0 - abs(measuresS[id] - measuresS2[id]))
                    sT3.append( 1.0 - abs(measuresS[id] - measuresS3[id]))
                    sT4.append( 1.0 - abs(measuresS[id] - measuresS4[id]))
                delta[T1] = THFE(*sT1)
                delta[T2] = THFE(*sT2)
                delta[T3] = THFE(*sT3)
                delta[T4] = THFE(*sT4)
            else:
                delta[T1] = ONE
                delta[T2] = ONE
                delta[T3] = ONE
                delta[T4] = ONE
        S = S + 1
    
    
    machine = THFA(delta, F)
    return machine, function_xi