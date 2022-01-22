#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import log2, ceil, floor

from prespa.filters.exceptions import NotSquareImage, DimensionNotIsPowerTwo, DepthType, DepthInconsistent, DepthNegative
from prespa.filters.utils import buildTreeAutomaton, createListWord

import numpy as np


def denoise_salt(img, depth=0):
    (m, n) = img.shape
    if m != n:
        raise NotSquareImage('Image dimension is ({}, {}) but this filter has implemented for square images.'.format(m, n))
    if not (ceil(log2(m)) == floor(log2(m))):
        raise DimensionNotIsPowerTwo('Image dimension is  ({}, {}) but this filter has implemented for images with dimension being power two.'.format(m, n))
    d = int(log2(m))
    if not isinstance(depth, int):
        raise DepthType('The depth not is an int value.')
    elif depth > d:
        raise DepthInconsistent('The input processing depth was {} but the depth for this image is {}.'.format(depth, d))
    elif depth < 0:
        raise DepthNegative('The input processing depth was negative value.')
    else:
        typeImage = img.dtype
        normalized = False
        if img.max() <= 1.0:
            machine, function_xi = buildTreeAutomaton(img, depth, n)
        else:
            normalized = True
            tImg = img/255
            machine, function_xi = buildTreeAutomaton(tImg, depth, n)
        words = createListWord(d)
        newIMG = np.zeros((m,n), dtype=float)
        for w in words:
            word = str(w)
            s = machine.compute(word)
            C = function_xi[s]
            i = C[0]
            j = C[1]
            T = machine.computePrefixes(word, depth)
            if normalized:
                newIMG[i, j] = 255 * (tImg[i, j] * T.meanCollapse())
            else:
                newIMG[i, j] = tImg[i, j] * T.meanCollapse()
        newIMG = newIMG.astype(typeImage)
        return newIMG 
