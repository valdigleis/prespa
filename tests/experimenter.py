from skimage import io
from skimage.metrics.simple_metrics import peak_signal_noise_ratio as psnr
from skimage.metrics.simple_metrics import normalized_root_mse as nrmse

from skimage.restoration import denoise_nl_means, denoise_wavelet, denoise_bilateral

from prespa.filters.denoise import salt_denoise

import numpy as np

def convertMatrixToTexTable(matrix):
    """Returns a LaTeX bmatrix

    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    if len(matrix.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(matrix).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{bmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{bmatrix}']
    return '\n'.join(rv)


print(">>>> Open images")

# Open original files
F01 = io.imread('../images/normal/airplane.pgm')
F02 = io.imread('../images/normal/brigde.pgm')
F03 = io.imread('../images/normal/cameraman.pgm')
F04 = io.imread('../images/normal/car.pgm')
F05 = io.imread('../images/normal/circle.pgm')
F06 = io.imread('../images/normal/lena.pgm')
F07 = io.imread('../images/normal/ships.pgm')
F08 = io.imread('../images/normal/vegetables.pgm')

# Open files with noise
M01 = io.imread('../images/noise-salt/01/airplane.pgm')
M02 = io.imread('../images/noise-salt/01/brigde.pgm')
M03 = io.imread('../images/noise-salt/01/cameraman.pgm')
M04 = io.imread('../images/noise-salt/01/car.pgm')
M05 = io.imread('../images/noise-salt/01/circle.pgm')
M06 = io.imread('../images/noise-salt/01/lena.pgm')
M07 = io.imread('../images/noise-salt/01/ships.pgm')
M08 = io.imread('../images/noise-salt/01/vegetables.pgm')

print(">>>> Run experimenter")

print(">>>> (Complete) Prespa Algorithm")

# Experimenter (my Algorithms)
pM01 = salt_denoise(M01)
pM02 = salt_denoise(M02)
pM03 = salt_denoise(M03)
pM04 = salt_denoise(M04)
pM05 = salt_denoise(M05)
pM06 = salt_denoise(M06)
pM07 = salt_denoise(M07)
pM08 = salt_denoise(M08)

print(">>>> (Limited) Prespa Algorithm")

# Experimenter (my Algorithms)
PM01 = salt_denoise(M01, 'limited')
PM02 = salt_denoise(M02, 'limited')
PM03 = salt_denoise(M03, 'limited')
PM04 = salt_denoise(M04, 'limited')
PM05 = salt_denoise(M05, 'limited')
PM06 = salt_denoise(M06, 'limited')
PM07 = salt_denoise(M07, 'limited')
PM08 = salt_denoise(M08, 'limited')

print(">>>> Bilateral algorithm")

bM01 = (255 * denoise_bilateral(M01)).astype(F01.dtype)
bM02 = (255 * denoise_bilateral(M02)).astype(F02.dtype)
bM03 = (255 * denoise_bilateral(M03)).astype(F03.dtype)
bM04 = (255 * denoise_bilateral(M04)).astype(F04.dtype)
bM05 = (255 * denoise_bilateral(M05)).astype(F05.dtype)
bM06 = (255 * denoise_bilateral(M06)).astype(F06.dtype)
bM07 = (255 * denoise_bilateral(M07)).astype(F07.dtype)
bM08 = (255 * denoise_bilateral(M08)).astype(F08.dtype)

print(">>>> Non-local means algorithm")

nM01 = (255 * denoise_nl_means(M01)).astype(F01.dtype)
nM02 = (255 * denoise_nl_means(M02)).astype(F02.dtype)
nM03 = (255 * denoise_nl_means(M03)).astype(F03.dtype)
nM04 = (255 * denoise_nl_means(M04)).astype(F04.dtype)
nM05 = (255 * denoise_nl_means(M05)).astype(F05.dtype)
nM06 = (255 * denoise_nl_means(M06)).astype(F06.dtype)
nM07 = (255 * denoise_nl_means(M07)).astype(F07.dtype)
nM08 = (255 * denoise_nl_means(M08)).astype(F08.dtype)

print(">>>> Denoise Wavelet algorithm")

wM01 = (255 * denoise_wavelet(M01)).astype(F01.dtype)
wM02 = (255 * denoise_wavelet(M02)).astype(F02.dtype)
wM03 = (255 * denoise_wavelet(M03)).astype(F03.dtype)
wM04 = (255 * denoise_wavelet(M04)).astype(F04.dtype)
wM05 = (255 * denoise_wavelet(M05)).astype(F05.dtype)
wM06 = (255 * denoise_wavelet(M06)).astype(F06.dtype)
wM07 = (255 * denoise_wavelet(M07)).astype(F07.dtype)
wM08 = (255 * denoise_wavelet(M08)).astype(F08.dtype)


print(">>>> Compute results")

# Compute PSNR
rP = np.zeros((8, 5))

rP[0, 0] = psnr(F01, pM01)
rP[1, 0] = psnr(F02, pM02)
rP[2, 0] = psnr(F03, pM03)
rP[3, 0] = psnr(F04, pM04)
rP[4, 0] = psnr(F05, pM05)
rP[5, 0] = psnr(F06, pM06)
rP[6, 0] = psnr(F07, pM07)
rP[7, 0] = psnr(F08, pM08)

rP[0, 1] = psnr(F01, PM01)
rP[1, 1] = psnr(F02, PM02)
rP[2, 1] = psnr(F03, PM03)
rP[3, 1] = psnr(F04, PM04)
rP[4, 1] = psnr(F05, PM05)
rP[5, 1] = psnr(F06, PM06)
rP[6, 1] = psnr(F07, PM07)
rP[7, 1] = psnr(F08, PM08)

rP[0, 2] = psnr(F01, bM01)
rP[1, 2] = psnr(F02, bM02)
rP[2, 2] = psnr(F03, bM03)
rP[3, 2] = psnr(F04, bM04)
rP[4, 2] = psnr(F05, bM05)
rP[5, 2] = psnr(F06, bM06)
rP[6, 2] = psnr(F07, bM07)
rP[7, 2] = psnr(F08, bM08)

rP[0, 3] = psnr(F01, nM01)
rP[1, 3] = psnr(F02, nM02)
rP[2, 3] = psnr(F03, nM03)
rP[3, 3] = psnr(F04, nM04)
rP[4, 3] = psnr(F05, nM05)
rP[5, 3] = psnr(F06, nM06)
rP[6, 3] = psnr(F07, nM07)
rP[7, 3] = psnr(F08, nM08)

rP[0, 4] = psnr(F01, wM01)
rP[1, 4] = psnr(F02, wM02)
rP[2, 4] = psnr(F03, wM03)
rP[3, 4] = psnr(F04, wM04)
rP[4, 4] = psnr(F05, wM05)
rP[5, 4] = psnr(F06, wM06)
rP[6, 4] = psnr(F07, wM07)
rP[7, 4] = psnr(F08, wM08)

print(convertMatrixToTexTable(rP))

# Compute NRMSE
rE = np.zeros((8, 5))

rE[0, 0] = nrmse(F01, pM01)
rE[1, 0] = nrmse(F02, pM02)
rE[2, 0] = nrmse(F03, pM03)
rE[3, 0] = nrmse(F04, pM04)
rE[4, 0] = nrmse(F05, pM05)
rE[5, 0] = nrmse(F06, pM06)
rE[6, 0] = nrmse(F07, pM07)
rE[7, 0] = nrmse(F08, pM08)

rE[0, 1] = nrmse(F01, PM01)
rE[1, 1] = nrmse(F02, PM02)
rE[2, 1] = nrmse(F03, PM03)
rE[3, 1] = nrmse(F04, PM04)
rE[4, 1] = nrmse(F05, PM05)
rE[5, 1] = nrmse(F06, PM06)
rE[6, 1] = nrmse(F07, PM07)
rE[7, 1] = nrmse(F08, PM08)

rE[0, 2] = nrmse(F01, bM01)
rE[1, 2] = nrmse(F02, bM02)
rE[2, 2] = nrmse(F03, bM03)
rE[3, 2] = nrmse(F04, bM04)
rE[4, 2] = nrmse(F05, bM05)
rE[5, 2] = nrmse(F06, bM06)
rE[6, 2] = nrmse(F07, bM07)
rE[7, 2] = nrmse(F08, bM08)

rE[0, 3] = nrmse(F01, nM01)
rE[1, 3] = nrmse(F02, nM02)
rE[2, 3] = nrmse(F03, nM03)
rE[3, 3] = nrmse(F04, nM04)
rE[4, 3] = nrmse(F05, nM05)
rE[5, 3] = nrmse(F06, nM06)
rE[6, 3] = nrmse(F07, nM07)
rE[7, 3] = nrmse(F08, nM08)

rE[0, 4] = nrmse(F01, wM01)
rE[1, 4] = nrmse(F02, wM02)
rE[2, 4] = nrmse(F03, wM03)
rE[3, 4] = nrmse(F04, wM04)
rE[4, 4] = nrmse(F05, wM05)
rE[5, 4] = nrmse(F06, wM06)
rE[6, 4] = nrmse(F07, wM07)
rE[7, 4] = nrmse(F08, wM08)

print(convertMatrixToTexTable(rE))