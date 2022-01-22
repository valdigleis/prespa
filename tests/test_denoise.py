#!/usr/bin/env python3


"""Class for testing the denoise methods."""
import unittest

import numpy as np

from skimage import io

from prespa.filters.denoise import denoise_salt

class TestDenoise(unittest.TestCase):

    def test_denoiseSalt(self):
        fig = io.imread('../images/noise-salt/01/airplane.pgm')
        nfig = denoise_salt(fig, 0)
        print(fig.dtype)
        print(nfig.dtype)
        T = (fig == nfig).all()
        self.assertEqual(T, False)

if __name__ == '__main__':
    unittest.main()
