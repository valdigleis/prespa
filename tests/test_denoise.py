#!/usr/bin/env python3


"""Class for testing the denoise methods."""
import unittest

import numpy as np

from skimage import io

from prespa.filters.denoise import salt_denoise

import matplotlib.pyplot as plt


class TestDenoise(unittest.TestCase):

    def test_SaltDenoise(self):
        ori = io.imread('../images/normal/airplane.pgm')
        fig = io.imread('../images/noise-salt/01/airplane.pgm')
        nfig = salt_denoise(fig, 'limited')

        figure, axes = plt.subplots(nrows=1, ncols=3,  sharex=True, sharey=True, figsize=(8, 4))

        axes[0].imshow(ori, cmap=plt.cm.gray)
        axes[0].set_title('Original image')

        axes[1].imshow(fig, cmap=plt.cm.gray)
        axes[1].set_title('Noise image')

        axes[2].imshow(nfig, cmap=plt.cm.gray)
        axes[2].set_title('Prespa image')

        for ax in axes:
            ax.axis('off')
        
        plt.tight_layout()
        plt.show()

        T = (fig == nfig).all()
        self.assertEqual(T, False)

if __name__ == '__main__':
    unittest.main()
