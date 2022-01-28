#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import log2, ceil, floor

from prespa.filters.exceptions import NotSquareImage, DimensionNotIsPowerTwo, ModeNotDefine
from prespa.filters.utils import buildTHFA, createListWord

import numpy as np

modes = ['complete', 'limited']

def salt_denoise(img, mode='complete'):
    """Method for removing salt-like noise.
    
    Parameters
    ----------
    img : ndarray
        A square image of dimension n, where n is a power of 2. 
    mode : str (optional)
        Mode for valuation the transitions complete (slow) or limited (fast). Default is complete
    Returns
    ----------
    newImg : ndarray
        A treated image.

    Author
    ----------
    Valdigleis (valdigleis@gmail.com)
    """
    if mode not in modes:
        raise ModeNotDefine('The mode {} not is define in prespa.'.format(mode))
    (m, n) = img.shape
    if m != n:
        raise NotSquareImage('Image dimension is ({}, {}) but this filter has implemented for square images.'.format(m, n))
    if not (ceil(log2(m)) == floor(log2(m))):
        raise DimensionNotIsPowerTwo('Image dimension is  ({}, {}) but this filter has implemented for images with dimension being power two.'.format(m, n))
    d = int(log2(m))
    typeImage = img.dtype
    normalized = False
    if img.max() <= 1.0:
        machine, function_xi = buildTHFA(img, n, mode)
    else:
        normalized = True
        tImg = img/255
        machine, function_xi = buildTHFA(tImg, n, mode)
    words = createListWord(d)
    newIMG = np.zeros((m,n), dtype=float)
    for w in words:
        word = str(w)
        s, T = machine.compute(word)
        C = function_xi[s]
        i = C[0]
        j = C[1]
        if normalized:
            newIMG[i, j] = 255 * (tImg[i, j] * T.meanCollapse())
        else:
            newIMG[i, j] = tImg[i, j] * T.meanCollapse()
    newIMG = newIMG.astype(typeImage)
    return newIMG 
    

